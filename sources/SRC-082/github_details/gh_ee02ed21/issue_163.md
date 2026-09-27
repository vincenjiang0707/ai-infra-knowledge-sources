# [Issue #163] Possible Bug in "_search_module_scale" Function

source: https://github.com/mit-han-lab/llm-awq/issues/163
state: open | updated: 2026-07-16T14:55:45Z
labels: 

## 正文

In the function `_search_module_scale`. https://github.com/mit-han-lab/llm-awq/blob/79019832efd37e4c24a695442880190858aa605e/awq/quantize/auto_scale.py#L131
)
```
for fc in linears2scale:
   fc.weight.mul_(scales.view(1, -1).to(fc.weight.device))
   fc.weight.data = w_quantize_func(fc.weight.data) / (scales.view(1, -1))
```

The FC weights are updated for each scale used in the grid search. But shouldn't the weight be reset to the original values for the next iteration? Otherwise, wouldn't the scale value be compounded?

Or Am I not observing something here?

## 评论 (1)

### Chessing234 · 2026-07-16

PR up: clone org_sd before the scale grid search so CPU in-place updates do not compound.
