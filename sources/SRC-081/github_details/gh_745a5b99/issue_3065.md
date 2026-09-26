# [Issue #3065] [Bug]: autowrap_forward fails with NameError for models defined in __main__ under cProfile/runpy

source: https://github.com/vllm-project/llm-compressor/issues/3065
state: closed | updated: 2026-08-23T15:01:30Z
labels: bug

## 正文

### ⚙️ Your current environment

<details>
<summary>The output of <code>python collect_env.py</code></summary>

```text
### Environment Information ###
Operating System: `macOS-26.5.2-arm64-arm-64bit`
Python Version: `3.12.5`
llm-compressor Version: `0.13.1.dev24+g48116705`
compressed-tensors Version: `0.18.1a20260818`
transformers Version: `5.15.0`
torch Version: `2.13.0`
CUDA Devices: `None`
AMD Devices: `None`
NPU Devices: `None`
MPS Devices: `['arm']`
```

</details>

Note: `tools/collect_env.py` currently crashes on Apple Silicon, so the output above required a local patch. Filed separately as #3064.

### 🐛 Describe the bug

`autowrap_forward` builds the namespace for the recompiled forward from `sys.modules[module.__class__.__module__].__dict__` in `src/llmcompressor/pipelines/sequential/ast_helpers.py`.

For a model class defined in a script, `__module__` is `"__main__"`. Runners such as `cProfile` and `runpy` exec the script into a fresh globals dict without installing it as `sys.modules["__main__"]`, so that lookup returns the runner's own module namespace instead of the script's. Names from the script are then missing, and the subsequent `exec` raises:

```
RuntimeError: --- <Autowrapped ParameterAccessWrapper ...>:1 ---
name 'torch' is not defined
```

Minimal demonstration of the cause:

```python
import sys, torch

class Wrapper(torch.nn.Module):
    def forward(self, x):
        return torch.relu(x)

mod = sys.modules.get(Wrapper.__module__)
print(mod.__file__, "torch" in mod.__dict__)
```

- direct run: `/tmp/diag.py True`
- under `python3 -m cProfile`: `.../cProfile.py False`

I hit this trying to profile `benchmarks/bench_trace_subgraphs.py`, whose `ParameterAccessWrapper` is defined in the benchmark script.

Proposed fix: autowrap_forward already calls inspect.getsource(module.forward), and inspect.getsourcelines calls unwrap internally — so the parsed source belongs to the unwrapped function. Taking the namespace from that same function keeps source and globals consistent by construction:

```python
forward_fn = inspect.unwrap(module.forward)
namespace = getattr(forward_fn, "__globals__", None)
if namespace is None:
    namespace = sys.modules[module.__class__.__module__].__dict__
namespace = namespace.copy()
```

The `inspect.unwrap` is load-bearing. Using `module.forward.__globals__` directly fails for HF models, since `forward` is decorated and `functools.wraps` does not copy `__globals__` — you get the decorator's namespace while `getsource` returns the original's. I confirmed this: it breaks 6 tests including `test_trace_subgraphs[1-5]`.

With `unwrap`, all 32 tests in `tests/llmcompressor/pipelines/sequential/` pass and the reproduction below completes. Happy to open a PR, with a subprocess-based regression test if you would like one.

### 🛠️ Steps to reproduce

Fails:

```bash
python3 -m cProfile -o /tmp/x.prof benchmarks/bench_trace_subgraphs.py \
  --num-targets 2000 --targets-per-subgraph 300 \
  --num-parameters 5000 --num-parameter-accesses 20 --repeat 1
```

Succeeds — identical arguments, without `-m cProfile`:

```bash
python3 benchmarks/bench_trace_subgraphs.py \
  --num-targets 2000 --targets-per-subgraph 300 \
  --num-parameters 5000 --num-parameter-accesses 20 --repeat 1
```

Also reproduces under `runpy`, or with any model class defined in `__main__`.

## 评论 (2)

### Umar-Farooq07 · 2026-08-22

I am new to AI . I am passionate about AI so  I am doing research on this issue . I'll try to fix it if I can . 


### Umar-Farooq07 · 2026-08-23

Don't rely on me because I might take time because I haven't done this before and not an expert in AI . I am doing this to upgrade myself and help others in future as well. I'll try my best to do it 
