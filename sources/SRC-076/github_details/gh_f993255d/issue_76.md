# [Issue #76] [torch.AcceleratorError] causes entire benchmark to crash

source: https://github.com/ScalingIntelligence/KernelBench/issues/76
state: open | updated: 2026-01-22T08:51:56Z
labels: 

## 正文

When one of the kernels produces a bug that affects the GPU. all follow-on computations on the GPU are broken.

E.g.:
```
torch.AcceleratorError: CUDA error: an illegal memory access was encountered
```

After that even doing some basic torch calculation causes the same torch error. (Therefore it is not possible to recover from this within the same python process (or so it seems at least)).

Have you encountered this? @simonguozirui do you know how to overcome such an error? (I am wondering whether the eval pipeline needs to be re-written for such a case, e.g. via bash scripts so that the eval pipeline can be in independent python processes?)

## 评论 (4)

### ai-nikolai · 2025-10-28

Perhaps the answer can be something similar to this https://github.com/wzzll123/MultiKernelBench/blob/05e3ff4d39953ac7c5368f28d09314b0740aa6f0/evaluation.py#L28 in `MultiKernelBench`

### ai-nikolai · 2025-11-13

If anyone is interested in this issue, tag me, we are working on a fix.

### jiito · 2026-01-15

@ai-nikolai I'm running into this now with our implementation in `inspect_evals`. Did you find a fix?

### ai-nikolai · 2026-01-22

Hi @jiito , thanks for following-up. We are close to fixing it (there were many follow-on issues as well). 

Hopefully we will publish this soon. I will keep you posted.
