# [Issue #3057] [Bug] sequential pipeline cannot trace models whose forward is decorated without functools.wraps (Qwen3.8 / Qwen3_5GatedDeltaNet)

source: https://github.com/vllm-project/llm-compressor/issues/3057
state: closed | updated: 2026-08-22T19:14:31Z
labels: bug, tracing

## 正文

## Describe the bug

The sequential-pipeline calibration path (used by GPTQ, SparseGPT, and AWQ via this pipeline) cannot trace any model whose module `forward` is wrapped by a decorator that does **not** apply `functools.wraps`. This blocks quantization of such models entirely.

Concretely, in transformers >= 5.x the `Qwen3_5GatedDeltaNet.forward` method is decorated with `@force_accelerate_hooks("conv1d")` (defined in [`transformers/integrations/accelerate.py`](https://github.com/huggingface/transformers/blob/main/src/transformers/integrations/accelerate.py)). That decorator returns an inner function:

```python
def force_accelerate_hooks(...):
    def wrapped(self, *args, **kwargs):
        ...
        return fn(self, *args, **kwargs)
    return wrapped
```

and does **not** apply `functools.wraps`, so the wrapper has neither `__wrapped__` nor the original `__name__`.

## Root cause

In `src/llmcompressor/pipelines/sequential/ast_helpers.py`, `autowrap_forward` does:

```python
source = inspect.getsource(module.forward)   # returns the wrapper's source
...
exec(code, namespace)
new_forward = namespace["forward"].__get__(module)   # <-- KeyError: 'forward'
```

Because `inspect.getsource(module.forward)` returns the source of the **wrapper** (the inner `def wrapped(self, *args, **kwargs)`), the re-exec'd code defines a function named `wrapped`, not `forward`. The subsequent `namespace["forward"]` lookup therefore raises `KeyError: 'forward'`.

`inspect.unwrap` does **not** help here because the wrapper has no `__wrapped__` attribute, so there is nothing to unwrap — `inspect.unwrap(module.forward)` returns the wrapper unchanged.

## Steps to reproduce

```python
import torch
from llmcompressor.pipelines.sequential.ast_helpers import autowrap_forward


# Mirrors the shape of transformers' force_accelerate_hooks:
# a decorator that does NOT use functools.wraps.
def force_conv1d(fn):
    def wrapped(self, *args, **kwargs):
        return fn(self, *args, **kwargs)
    return wrapped


class Mod(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 4)

    @force_conv1d
    def forward(self, x):
        return self.linear(x)


with autowrap_forward(Mod(), ignore=[]):
    pass
```

### Error

```
KeyError: 'forward'
```

at `src/llmcompressor/pipelines/sequential/ast_helpers.py`, line `new_forward = namespace["forward"].__get__(module)`.

### Real-world impact

Running a sequential GPTQ calibration of `Qwen/Qwen3.8-27B` (64-layer hybrid: 16 full-attention + 48 `Qwen3_5GatedDeltaNet` layers) fails immediately during tracing. The same failure applies to any model using a `forward` decorated this way under transformers >= 5.x.

## Expected behavior

`autowrap_forward` should resolve the decorated method to the original `forward` function before calling `inspect.getsource`, so the re-exec'd code defines `forward` and the lookup succeeds. The decorator's behaviour (e.g. accelerate hook setup) should be preserved — `inspect.getsource` on the original function includes its decorator line, so re-executing it re-applies the decorator.

## Environment

- llm-compressor: main (commit `44e78dcc`)
- transformers >= 5.x (provides `force_accelerate_hooks`)
- Model: `Qwen/Qwen3.8-27B`

A fix is forthcoming in a linked PR.

## 评论 (2)

### coderabbitai[bot] · 2026-08-19

<!-- This is an auto-generated issue plan by CodeRabbit -->

<details>
<summary>⚠️ Possible Duplicate Issue(s)</summary>

- https://github.com/vllm-project/llm-compressor/issues/2172
</details>
<details>
<summary>🔗 Related PRs</summary>

vllm-project/llm-compressor#2462 - [Bugfix] QAC with basic pipeline [merged]
vllm-project/llm-compressor#2591 - [bugfix][awq] fix kv_cache + awq bug [merged]
vllm-project/llm-compressor#2781 - [Autowrapper] [Tracing] Unpin Gemma4, support tracing `UserDict` and `IfExp` [merged]
vllm-project/llm-compressor#2823 - [Bugfix] Fix KV cache tests with transformers v5 [closed]
</details>

---
<details>
<summary>📝 Issue Planner</summary>

<sub>Check the box below or use the `@coderabbitai plan` command to generate an implementation plan and prompts that you can use with your favorite coding assistant.</sub>

- [ ] <!-- {"checkboxId":"8d4f2b9c-3e1a-4f7c-a9b2-d5e8f1c4a7b9"} --> Create Plan
</details>


---
<details>
<summary> 🧪 Issue enrichment is currently in open beta.</summary>


You can configure auto-planning by selecting labels in the issue_enrichment configuration.

To disable automatic issue enrichment, add the following to your `.coderabbit.yaml`:
```yaml
issue_enrichment:
  auto_enrich:
    enabled: false
```
</details>

💬 Have feedback or questions? Drop into our [discord](https://discord.gg/coderabbit)!

### kylesayrs · 2026-08-19

Thanks for the catch!
