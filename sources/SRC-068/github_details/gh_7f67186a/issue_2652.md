# [Issue #2652] atomic_add_fp32: TypeError on nvvm.atomicrmw(res=T.f32(), ...) — 'res' kwarg removed in cutlass-dsl 4.5.2

source: https://github.com/Dao-AILab/flash-attention/issues/2652
state: open | updated: 2026-07-24T06:03:13Z
labels: 

## 正文

## Summary

`utils.py` calls `nvvm.atomicrmw(res=T.f32(), ...)` but the `res` keyword argument was removed from the `nvvm.atomicrmw` API in nvidia-cutlass-dsl 4.5.2, causing a `TypeError`.

## Environment

- flash-attn-4: v4.0.0b16
- **nvidia-cutlass-dsl: 4.5.2** (the version where `res` was removed)
- CUDA: 12.8
- GPU: NVIDIA GB10 (sm_121 — consumer Blackwell / DGX Spark)

## Root Cause

In `utils.py` (around line 486), `atomic_add_fp32` calls:

```python
nvvm.atomicrmw(res=T.f32(), op=nvvm.AtomicBinOp.fadd, ptr=ptr, a=value, ...)
```

In nvidia-cutlass-dsl 4.5.2, the `res` keyword argument was removed from `nvvm.atomicrmw`. The return value is now implicit (the function returns the old value directly). Passing `res=` raises:

```
TypeError: atomicrmw() got an unexpected keyword argument 'res'
```

## Fix

Remove the `res=T.f32()` argument:

```python
# utils.py ~line 486
# Old:
nvvm.atomicrmw(res=T.f32(), op=nvvm.AtomicBinOp.fadd, ptr=ptr, a=value, ...)
# New:
nvvm.atomicrmw(op=nvvm.AtomicBinOp.fadd, ptr=ptr, a=value, ...)
```

## Verification

Applied locally on GB10 (SM_121) with nvidia-cutlass-dsl 4.5.2. `TypeError` no longer occurs.

## Note

This is a compatibility break between flash-attn-4 b16 and nvidia-cutlass-dsl 4.5.2. Users on cutlass-dsl ≤ 4.5.1 would not see this issue, but 4.5.2 is now the current release.

## 评论 (1)

### hebo1221 · 2026-07-24

Fixed on current `main` by #2671 (`6e646e0099952b768ff2fe229ea9027c26438e7c`): `atomic_add_fp32` now calls `nvvm.atomicrmw` without the removed `res=` argument.

Validated on GB10 / SM121 against the current merged code with BF16 MHA (`batch=9`, `seqlen_q=seqlen_k=128`, `heads=6`, `head_dim=64`) and a local window of `(98, 107)`. Forward and backward both completed and passed the repository's PyTorch-reference checks (`1 passed`; max dQ/dK/dV error `0.0078125`).

The backward kernel compiles and runs with the current CUTLASS DSL API, so this issue should be safe to close.
