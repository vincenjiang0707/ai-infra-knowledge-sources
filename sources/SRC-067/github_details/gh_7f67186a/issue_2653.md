# [Issue #2653] _flash_attn_fwd/_flash_attn_bwd: DSLRuntimeError — window_size_left/right expects Int32 but gets plain Python int

source: https://github.com/Dao-AILab/flash-attention/issues/2653
state: open | updated: 2026-07-24T06:03:12Z
labels: 

## 正文

## Summary

`interface.py` passes plain Python `int` for `window_size_left`/`window_size_right` to `cute.compile` on SM_80 and SM_12x code paths, but `cute.compile` requires `cutlass.Int32` for `Optional[Int32]` kernel parameters → `DSLRuntimeError`.

## Environment

- flash-attn-4: v4.0.0b16
- nvidia-cutlass-dsl: 4.5.2
- CUDA: 12.8
- GPU: NVIDIA GB10 (sm_121 — consumer Blackwell / DGX Spark)

## Root Cause

The kernel signatures declare `window_size_left: Optional[Int32]` and `window_size_right: Optional[Int32]`. `cute.compile` uses argument types for type-template specialization — it requires `cutlass.Int32`, not plain Python `int`.

The SM_90 path implicitly coerces (or takes a different compile route), so this issue is not visible on H100/H200. The SM_80 and SM_12x else-branches in both `_flash_attn_fwd` and `_flash_attn_bwd` pass raw Python `int` values directly into `compile_args`:

```python
# interface.py — SM_80/12x path
compile_args = (..., window_size_left, window_size_right, ...)
#                     ^^^^^^^^^^^^^^^^ plain int → DSLRuntimeError
```

Error:
```
DSLRuntimeError: argument #13 (window_size_left): expects (Int32, NoneType) but got int
```

## Fix

Cast to `Int32` before building `compile_args`, in both the forward and backward compile paths:

```python
# interface.py — add before compile_args in BOTH _flash_attn_fwd and _flash_attn_bwd
window_size_left_typed = Int32(window_size_left) if window_size_left is not None else None
window_size_right_typed = Int32(window_size_right) if window_size_right is not None else None
```

Then use `window_size_left_typed` / `window_size_right_typed` in the `compile_args` tuple instead of the raw values. `Int32` is already imported: `from cutlass import Int32, Float32`.

## Verification

Applied locally on GB10 (SM_121). `DSLRuntimeError` for `window_size_left` argument no longer occurs. Sliding window forward tests now run and produce results (the **forward** is numerically correct; note: backward has a separate pre-existing limitation where `AttentionMask` in `FlashAttentionBackwardSm80.kernel()` ignores `mask_local=True` — but that is a different bug, not related to this type cast).

## Affected Tests

- `test_dpa_fa4_sliding_window` (all 8 variants) — previously crashed at compile step with this error
- Any test that passes non-None `window_size_left/right` through the SM_80 or SM_12x code path

## Note

This affects all non-SM_90 hardware. Users on A100/H100 (SM_80/SM_90) without `window_size` set would not see this issue since the default `window_size=(-1, -1)` may be handled differently.

## 评论 (1)

### hebo1221 · 2026-07-24

Fixed on current `main` by #2671 (`6e646e0099952b768ff2fe229ea9027c26438e7c`), which corrected the SM120 compile-time argument handling and wired local-window parameters through the backward kernel.

Validated on GB10 / SM121 against the current merged code with BF16 MHA (`batch=9`, `seqlen_q=seqlen_k=128`, `heads=6`, `head_dim=64`) and a local window of `(98, 107)`. Forward and backward both completed and passed the repository's PyTorch-reference checks (`1 passed`; max dQ/dK/dV error `0.0078125`).

The non-None window arguments compile and the local-attention numerical checks pass, so this issue should be safe to close.
