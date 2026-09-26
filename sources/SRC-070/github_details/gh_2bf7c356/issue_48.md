# [Issue #48] How to apply Moe MLP to recv_x returned by dispatch when num_expert_per_rank > 1

source: https://github.com/deepseek-ai/DeepEP/issues/48
state: closed | updated: 2026-09-18T09:57:12Z
labels: 

## 正文

In the case of normal kernels and `num_expert_per_rank > 1`, for example, token A in rank 0 is dispatched to rank 1 for experts M and N.
A is dispatched only once into recv_x of rank 1 with topk indices. How can I use group gemm based MLP to feed forward token A in recv_x?
If I duplicate A into two token seperately for experts M and N, it's more complicated in combine process. Because combine function would use the origin handle returned by dispatch function, and shape[0] of the new hidden states computed with duplicating A and applying MLP is different from shape[0] of the recv_x returned by dispatch function.

## 评论 (2)

### LyricZhao · 2025-03-06

You can refer to our design the Chrome tracing in https://github.com/deepseek-ai/profile-data.

> How can I use group gemm based MLP to feed forward token A in recv_x?

If you use DeepGEMM, you must expand one tokens to several experts.

> If I duplicate A into two token seperately for experts M and N, it's more complicated in combine process.

So there is a reduction kernel before the combine all2all.

### LyricZhao · 2025-03-06

We follow the current design, because if we expand at the end of dispatch, for some models with more than one experts per GPU selected for a single token, it will cost much more VRAM. This is a tradeoff between VRAM and performance (expand/reduce kernel is not very slow).
