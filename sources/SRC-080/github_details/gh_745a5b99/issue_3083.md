# [Issue #3083] [Bug]: requires_compute_capability crashes at collection time on Apple Silicon

source: https://github.com/vllm-project/llm-compressor/issues/3083
state: closed | updated: 2026-08-25T18:29:30Z
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

Note: `tools/collect_env.py` currently crashes on Apple Silicon, so the output above required a local patch. Filed separately as #3064 (PR #3068).

### 🐛 Describe the bug

`requires_compute_capability` in `tests/testing_utils.py` guards on `torch.accelerator.is_available()`, which returns True on Apple Silicon because MPS counts as an accelerator. It then calls `get_device_capability`, which `torch.mps` does not implement.

Because this runs in a decorator, it fails at **collection** time — the whole test module becomes unusable, not just the gated test:

```
tests/llmcompressor/modifiers/transform/awq/test_base.py:788: in <module>
    @requires_compute_capability(9, 0)  # Requires H100 or higher
tests/testing_utils.py:386: in requires_compute_capability
    device_capability = torch.get_device_module().get_device_capability(0)
E   AttributeError: module 'torch.mps' has no attribute 'get_device_capability'

Interrupted: 1 error during collection
no tests collected, 1 error in 0.21s
```

Independently hit by @robertlangdonn while working on #3074, who noted it as the same class of gap as #3064.

Same root cause as #3064: `torch.accelerator` unifies availability and device count across backends, but not every backend implements the per-device query functions built on top of it. The skip reason on the line above ("CUDA not available") suggests this function was written for CUDA and later retrofitted onto the generic accelerator API.

Proposed fix: skip when the backend doesn't report a compute capability. Skipping is the correct outcome — a machine without CUDA genuinely can't satisfy "requires H100", so a crash is never the right answer here.

With the fix, that module goes from 0 collected to 20 collected: 18 pass, 1 skips (the H100-gated test, correctly), and 2 fail for unrelated reasons — those two require CUDA directly (`AssertionError: Torch not compiled with CUDA enabled`) and are out of scope.

I have this working locally and am opening a PR alongside this issue.

### 🛠️ Steps to reproduce

On any Apple Silicon Mac:

```bash
python3 -m pytest tests/llmcompressor/modifiers/transform/awq/test_base.py --collect-only -q
```

## 评论 (1)

### Isitthakkar11 · 2026-08-25

Thanks @dsikka — PR is already up at #3084. Could you add the ready label so CI can run? I don't have permission to add it.
