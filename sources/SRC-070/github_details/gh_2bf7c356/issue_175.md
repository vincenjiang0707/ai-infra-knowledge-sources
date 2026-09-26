# [Issue #175] Why minimum Byte Size Forced to 2 when calculation hidden bytes for FP8 in get_hidden_bytes()

source: https://github.com/deepseek-ai/DeepEP/issues/175
state: closed | updated: 2026-09-18T09:44:24Z
labels: 

## 正文

in https://github.com/deepseek-ai/DeepEP/blob/main/README.md Interfaces and examples section,

def get_hidden_bytes(x: torch.Tensor) -> int:
    t = x[0] if isinstance(x, tuple) else x
    return t.size(1) * max(t.element_size(), 2)

FP8 tensors use 1 byte per element, but the function forces a 2-byte minimum，Is there a memory/performance trade-off?

## 评论 (1)

### LyricZhao · 2025-05-27

Dispatch can use FP8, but combine always uses BF16 (2 bytes). Using BF16 for combine is important for model performance/precision.
