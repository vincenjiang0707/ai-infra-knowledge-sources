# [Issue #3064] [Bug]: tools/collect_env.py crashes on Apple Silicon (torch.mps has no get_device_name)

source: https://github.com/vllm-project/llm-compressor/issues/3064
state: closed | updated: 2026-08-25T18:10:33Z
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

Note: the output above required the patch described below. The unpatched script crashes before printing anything on this machine.

### 🐛 Describe the bug

`tools/collect_env.py` crashes on Apple Silicon, so macOS users cannot produce the environment block this bug report template asks for.

```
Traceback (most recent call last):
  File "tools/collect_env.py", line 60, in <module>
    collect_environment_info()
  File "tools/collect_env.py", line 40, in collect_environment_info
    cuda_devices, amd_devices, npu_devices = get_torch_hardware_info()
  File "tools/collect_env.py", line 27, in get_torch_hardware_info
    name = torch.get_device_module().get_device_name(i)
AttributeError: module 'torch.mps' has no attribute 'get_device_name'
```

Cause: on Apple Silicon `torch.accelerator.is_available()` returns `True` because MPS counts as an accelerator, so the device loop in `get_torch_hardware_info` runs. `torch.get_device_module()` then returns `torch.mps`, which does not implement `get_device_name`. The surrounding `except ImportError` only catches a missing torch, so the `AttributeError` propagates and the script exits without printing anything.

Proposed fix:

- guard with `hasattr(device_module, "get_device_name")` rather than special-casing MPS, so any future backend lacking that method degrades gracefully
- report MPS devices in their own field
- widen the except to `(ImportError, AttributeError)` — a diagnostic tool should degrade rather than crash, since anyone running it is already debugging something else

I have this working locally against `48116705` and am happy to open a PR.

### 🛠️ Steps to reproduce

On any Apple Silicon Mac with torch installed:

```bash
python3 tools/collect_env.py
```

No model, GPU, or dataset required.

## 评论 (1)

### brian-dellabetta · 2026-08-20

Hi @Isitthakkar11 , thanks for raising, feel free to open a PR to wrap it in a try/catch fallback for MPS devices
