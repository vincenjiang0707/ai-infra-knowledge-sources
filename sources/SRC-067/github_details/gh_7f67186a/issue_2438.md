# [Issue #2438] pack_gqa fails on SM120 (SM80 CuTe DSL path): crd2idx coordinate resolution error

source: https://github.com/Dao-AILab/flash-attention/issues/2438
state: closed | updated: 2026-08-14T22:02:07Z
labels: 

## 正文

## Description

`pack_gqa=True` fails on SM120 (NVIDIA GB10 / DGX Spark) with a CuTe DSL layout algebra error. GQA works with `pack_gqa=False`.

## Reproduction

```python
import torch
from flash_attn.cute.interface import flash_attn_func

q = torch.randn(2, 512, 8, 64, device="cuda", dtype=torch.bfloat16)
k = torch.randn(2, 512, 2, 64, device="cuda", dtype=torch.bfloat16)
v = torch.randn(2, 512, 2, 64, device="cuda", dtype=torch.bfloat16)

# Fails:
out, _ = flash_attn_func(q, k, v, pack_gqa=True)

# Works:
out, _ = flash_attn_func(q, k, v, pack_gqa=False)
```

## Error

```
loc("tPrPtr[i] = utils.elem_pointer(tensor, ((h_idx, m_idx),)).toint()"
    ("flash_attn/cute/pack_gqa.py":139:20)):
error: unable to compute crd2idx with '!cute.layout<"(?):(?{i64 div=8})">'
       and '!cute.coord<"((?,?))">'
ValueError: Operation creation failed
```

The hierarchical coordinate `((h_idx, m_idx),)` passed to `elem_pointer` at `pack_gqa.py:139` can't be resolved against the packed tensor's layout.

## Environment

- SM121a (NVIDIA GB10, DGX Spark)
- CUDA 13.0, Driver 580.126.09
- nvidia-cutlass-dsl 4.4.1+
- flash-attn-4 (dev, main branch)

Also fails with `pack_gqa=None` (auto-selects `True` for GQA configs).

Contributed by Second Nature Computing (https://joinsecondnature.com)

## 评论 (4)

### sorryhyun · 2026-04-08

I verified this happens on sm120 (5060ti) too and older nvidia-cutlass-dsl does not help either.

### blake-snc · 2026-04-26

Quick update on this — the user-facing exposure is now sidestepped by #2484, but the underlying bug is still present.

#2484 forces `self.pack_gqa = False` inside `FlashAttentionForwardSm120.__init__`, so any GQA workload routed through `flash_attn_func` on SM120 goes through the non-packed path. That means callers using the public entry no longer hit the `crd2idx` error reported here. Anyone constructing `FlashAttentionForwardSm120` directly with `pack_gqa=True` still trips it.

The actual root cause — `Sm80.__call__` is missing the `pack_gqa_layout(mQ/mO/mLSE, ...)` calls that `Sm90.__call__` (L273) and `Sm100.__call__` (L504) apply, plus the Sm80 mainloop's tile sizing assumes `tile_m` divides the seqlen dimension cleanly which fails for the packed `(qhead_per_kvhead, seqlen_q)` layout when `qhead_per_kvhead` does not divide `tile_m` — is unchanged. A proper fix would add the three `pack_gqa_layout` calls in `Sm80.__call__` and either round `tile_m` to a multiple of `qhead_per_kvhead` or fall back to the non-packed path on the divisibility mismatch. I have a candidate patch for this and can put it up as a follow-up PR if maintainers are interested; would want SM80 hardware validation before posting since the change touches shared `Sm80.__call__`.


### hebo1221 · 2026-07-24

Fixed on current `main` by #2656 (`5835c733e7e9c07606b045255768e8a7e9e851bd`), which implements the SM80/SM120 Pack-GQA layout, Q-load, head indexing, and epilogue path end to end.

I revalidated the merged code on GB10 / SM121 today with BF16 GQA (`batch=9`, `seqlen_q=seqlen_k=128`, `6` Q heads / `3` KV heads, `head_dim=64`). The repository test exercised `pack_gqa=False`, `pack_gqa=True`, and `pack_gqa=None` (auto) in the same run; forward and backward all passed their PyTorch-reference checks (`1 passed`, max output error `0.00390625`, max dQ/dK/dV error `0.0078125`).

The reported non-TMA `crd2idx` failure no longer reproduces. This issue should be safe to close.

### blake-snc · 2026-08-14

Confirmed fixed on current main by #2656, per @hebo1221 above, thank you. Our SM120 hardware is currently allocated, so I did not re-run the repro at head; closing on that confirmation.

