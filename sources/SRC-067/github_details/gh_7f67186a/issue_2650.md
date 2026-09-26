# [Issue #2650] _flash_attn_bwd: UnboundLocalError for dQ_single_wg on SM_12x (arch//10 == 12)

source: https://github.com/Dao-AILab/flash-attention/issues/2650
state: open | updated: 2026-07-24T06:00:03Z
labels: 

## 正文

## Summary

`interface.py` raises `UnboundLocalError: local variable 'dQ_single_wg' referenced before assignment` on SM_12x (SM_120, SM_121) in the backward pass.

## Environment

- flash-attn-4: v4.0.0b16
- nvidia-cutlass-dsl: 4.5.2
- CUDA: 12.8
- GPU: NVIDIA GB10 (sm_121 — consumer Blackwell / DGX Spark)

## Root Cause

In `_flash_attn_bwd`, `dQ_single_wg` is used in `compile_key` for `arch // 10 in [8, 9, 12]`:

```python
compile_key = (..., dQ_single_wg if arch // 10 in [8, 9, 12] else None, ...)
```

However, `dQ_single_wg` is only set inside `if arch // 10 == 9:` — the SM_12x branch (`if arch // 10 == 12:`) never sets it:

```python
if arch // 10 == 9:
    dQ_single_wg = ...   # set here
    ...
elif arch // 10 == 8:
    dQ_single_wg = ...   # set here
    ...
if arch // 10 == 12:
    # dQ_single_wg never set here → UnboundLocalError
    ...
```

When `arch // 10 == 12`, the `compile_key` line runs before the variable is initialized → `UnboundLocalError`.

## Fix

Add `dQ_single_wg = False` inside the `if arch // 10 == 12:` branch:

```python
if arch // 10 == 12:
    dQ_single_wg = False   # SM_12x doesn't use single-WG dQ; avoids UnboundLocalError
    ...
```

## Verification

Applied locally on GB10 (SM_121). `UnboundLocalError` no longer occurs in the backward pass. MHA backward tests pass numerically.

## Related

Found during SM_121 (GB10 consumer Blackwell) bringup. Affects SM_120 and SM_121 equally. See also: issue for `use_tma_O` guard (filed separately).

## 评论 (1)

### hebo1221 · 2026-07-24

This is fixed on current `main` by #2671 (`6e646e0099952b768ff2fe229ea9027c26438e7c`), which initializes `dQ_single_wg = False` in the SM12x backward configuration.

I revalidated the merged code on a GB10 / SM121 today with a BF16 forward+backward case (`batch=2`, `seqlen_q=seqlen_k=128`, `heads=4`, `head_dim=64`), including preallocated gradient outputs: `1 passed`.

The backward path completes without the reported `UnboundLocalError`. This issue should be safe to close.
