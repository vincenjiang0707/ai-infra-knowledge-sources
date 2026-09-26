# [Issue #2651] FlashAttentionBackwardSm80: compute_softmax_scale_log2 overwrites softmax_scale with None → DSLRuntimeError

source: https://github.com/Dao-AILab/flash-attention/issues/2651
state: open | updated: 2026-07-24T06:03:10Z
labels: 

## 正文

## Summary

`flash_bwd.py` overwrites `softmax_scale` with `None` when `score_mod is None`, causing a `DSLRuntimeError` because the kernel requires a non-None `Float32` for dK scaling.

## Environment

- flash-attn-4: v4.0.0b16
- nvidia-cutlass-dsl: 4.5.2
- CUDA: 12.8
- GPU: NVIDIA GB10 (sm_121 — consumer Blackwell / DGX Spark)

## Root Cause

In `FlashAttentionBackwardSm80.__call__` (around line 440):

```python
softmax_scale_log2, softmax_scale = utils.compute_softmax_scale_log2(
    softmax_scale, score_mod, score_mod_type
)
```

`utils.compute_softmax_scale_log2` returns `(log2_value, None)` when `score_mod is None` (the common case). This assignment clobbers the original `Float32` value of `softmax_scale` with `None`.

Later in the kernel, `softmax_scale` is used unconditionally for dK scaling:

```python
# kernel requires Float32, gets None → DSLRuntimeError
```

The error message is: `DSLRuntimeError: argument expects Float32 but got NoneType`.

## Fix

Use a throwaway variable to preserve the original `softmax_scale`:

```python
# flash_bwd.py ~line 440
# Old:
softmax_scale_log2, softmax_scale = utils.compute_softmax_scale_log2(...)
# New:
softmax_scale_log2, _ = utils.compute_softmax_scale_log2(...)
```

`softmax_scale_log2` is needed for the kernel's log2 path; `softmax_scale` (the original Float32) must remain unchanged.

## Verification

Applied locally on GB10 (SM_121). `DSLRuntimeError` for `softmax_scale` argument no longer occurs. MHA backward tests pass numerically.

## Related

Found during SM_121 (GB10 consumer Blackwell) bringup. This bug affects all architectures using `FlashAttentionBackwardSm80` when `score_mod is None` (standard attention without custom score modifiers).

## 评论 (1)

### hebo1221 · 2026-07-24

Fixed on current `main` by #2671 (`6e646e0099952b768ff2fe229ea9027c26438e7c`): the SM80/SM12x backward path now keeps the original `softmax_scale` and assigns the second `compute_softmax_scale_log2` result to `_`.

Validated on GB10 / SM121 against the current merged code with BF16 MHA (`batch=9`, `seqlen_q=seqlen_k=128`, `heads=6`, `head_dim=64`) and a local window of `(98, 107)`. Forward and backward both completed and passed the repository's PyTorch-reference checks (`1 passed`; max dQ/dK/dV error `0.0078125`).

This issue should be safe to close.
