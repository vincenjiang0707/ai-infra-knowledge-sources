# [Issue #5195] bug: Numeric divergence between the mHC layer and its Pallas kernel

source: https://github.com/AI-Hypercomputer/maxtext/issues/5195
state: open | updated: 2026-09-20T13:50:26Z
labels: bug

## 正文

### Bug report

DeepSeek v4. The reference path had its own mapping helper that cast alpha_scale and
beta down to self.dtype before computing sigmoid(alpha_scale * h + beta),
while the Pallas path called common.compute_sigmoid_gate, which keeps the
scale and bias in float32. With dtype: bfloat16 the two branches therefore
gated on different numbers, so toggling use_mhc_pallas_kernel changed the
layer's output beyond accumulation noise.
Fixed in PR:
https://github.com/AI-Hypercomputer/maxtext/pull/5179

### Logs/Output

_No response_

### Environment Information

_No response_

### Additional Context

_No response_

## 评论 (3)

### Kaustubh1235 · 2026-09-12

I will take this issue. Please assign it to me.

The problem seems to be a type mismatch between the mHC layer and its Pallas kernel. The mHC layer casts `alpha_scale` and `beta` to `self.dtype` before computing the sigmoid, while the Pallas kernel uses `float32`. I would first check the `compute_sigmoid_gate` function in the Pallas kernel. A small fix would involve ensuring both paths use the same data type, likely by casting within `compute_sigmoid_gate` to match `self.dtype`. I will verify the fix by comparing outputs with and without `use_mhc_pallas_kernel`.


### denis-mil · 2026-09-12

> I will take this issue. Please assign it to me.
> 
> The problem seems to be a type mismatch between the mHC layer and its Pallas kernel. The mHC layer casts `alpha_scale` and `beta` to `self.dtype` before computing the sigmoid, while the Pallas kernel uses `float32`. I would first check the `compute_sigmoid_gate` function in the Pallas kernel. A small fix would involve ensuring both paths use the same data type, likely by casting within `compute_sigmoid_gate` to match `self.dtype`. I will verify the fix by comparing outputs with and without `use_mhc_pallas_kernel`.

Hi @Kaustubh1235, thanks for offering to look into this! This issue has actually already been addressed and fixed in PR #5179.

### Kaustubh1235 · 2026-09-20

Thanks for letting me know, Denis. I'll check out the PR to see the changes made.

