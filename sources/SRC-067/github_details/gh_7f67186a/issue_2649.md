# [Issue #2649] FlashAttentionForwardSm120: use_tma_O incorrectly True on SM_121 → AttributeError on tma_atom_O=None

source: https://github.com/Dao-AILab/flash-attention/issues/2649
state: closed | updated: 2026-07-29T16:30:38Z
labels: 

## 正文

## Summary

`flash_fwd.py:658` sets `self.use_tma_O` with a guard that fires incorrectly on SM_121, causing an `AttributeError` when the kernel tries to access `tma_atom_O._trait` on a `None` object.

## Environment

- flash-attn-4: v4.0.0b16
- nvidia-cutlass-dsl: 4.5.2
- CUDA: 12.8
- GPU: NVIDIA GB10 (sm_121 — consumer Blackwell / DGX Spark)

## Root Cause

`FlashAttentionForwardSm120` defines `arch = 80` as a **class attribute**. However, `BaseDSL.__init__` (called via `super().__init__()`) clobbers `self.arch` with `BaseDSL._get_dsl().get_arch_enum()`, which on SM_121 returns `Arch.sm_121`.

The current guard:
```python
self.use_tma_O = self.arch >= Arch.sm_90
```

On SM_121: `Arch.sm_121 >= Arch.sm_90` → `True`. The kernel then tries `tma_atom_O._trait`, but `tma_atom_O = None` (SM_121 is not in the TMA-O initialization branch) → `AttributeError: 'NoneType' object has no attribute '_trait'`.

## Fix

```python
# flash_fwd.py:658
# Old:
self.use_tma_O = self.arch >= Arch.sm_90
# New:
self.use_tma_O = Arch.sm_90 <= self.arch < Arch.sm_120
```

SM_121 should use the SM_80 code path (which it already does for everything else), not the SM_120 TMA-O path.

## Verification

Applied this patch locally on GB10 (SM_121). Confirmed: `AttributeError` on `tma_atom_O` no longer occurs. Base MHA forward tests pass numerically.

## Related

This was found during SM_121 (GB10 consumer Blackwell) bringup. SM_121 inherits the SM_80 kernel path — most SM_80 code works correctly, but this guard condition was overly broad.

## 评论 (4)

### Johnsonms · 2026-06-13

Hi @TyGu1 Could you please have  a try to the PR of @larsmic?

### larsmic · 2026-06-14

Hi, i want you to save your time trying if my PR runs for you. I did not include a fix to this Issue in my PR. I only locally applied the fix described here. Sorry for the confusion, i edited my PR comment. 

### hebo1221 · 2026-07-24

This is fixed on current `main` by #2656 (`5835c733e7e9c07606b045255768e8a7e9e851bd`), which restricts `use_tma_O` to `Arch.sm_90 <= self.arch < Arch.sm_120`.

I revalidated the merged code on a GB10 / SM121 today with a BF16 forward+backward case (`batch=2`, `seqlen_q=seqlen_k=128`, `heads=4`, `head_dim=64`), including preallocated gradient outputs: `1 passed`.

The forward path no longer hits the `tma_atom_O is None` failure. This issue should be safe to close.

### drisspg · 2026-07-29

great will close as fixed
