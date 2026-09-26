# [Issue #5674] gfx942: sliding-window decode forced to 2D (no KV-split) — poor low-batch occupancy

source: https://github.com/ROCm/aiter/issues/5674
state: open | updated: 2026-09-18T15:37:43Z
labels: 

## 正文

## Summary
In `unified_attention`, `use_2d_kernel(...)` returns `True` whenever `sliding_window > 0`, so **windowed (sliding-window) decode is always routed to the 2D kernel**, which does **no KV-split** across workgroups. At low batch this cannot fill the CUs on **gfx942 (MI325)** — a windowed decode step attends to at most `window` keys per query but still runs as a handful of workgroups.

## Evidence (microbench, gfx942)
Shape: `head_size 256`, GQA 32/16, sliding window 1024, fp8 KV cache, context 8192 (window-corrected bytes), `bench_unified_attention.py`.

| batch | achieved | % of 6 TB/s |
|------:|---------:|------------:|
| 1 | ~100 GB/s | ~2% |
| 64 | ~2350 GB/s | ~39% |

Sweeping the 2D-path config knobs (BLOCK_M / TILE_SIZE / num_warps / num_stages / waves_per_eu) at batch 1 yields **no meaningful improvement** — the ceiling is structural (no KV-split), not a config issue.

## Proposal
Provide a **KV-split / 3D path for windowed decode**: split the ≤`window` keys per sequence into segments so low-batch windowed decode can occupy the CUs, then reduce. The 3D path already carries a `SLIDING_WINDOW` parameter; the change is to let `use_2d_kernel` fall through to 3D for windowed decode (at least on gfx942 / when batch is low) and ensure the 3D kernel masks the window correctly. Must stay bit-comparable and not regress high batch (where 2D is already ~39%).

## Notes
gfx942-scoped proposal; verify no regression on other archs before widening. Correctness gating is required (windowed masking in the 3D path). These shapes occur in models with interleaved local attention such as the public Gemma-4-31B.

## 评论 (1)

### mpashkovskii · 2026-09-18

## Investigation: naive 2D->3D routing does not work; needs window-aware KV-split

Tested routing windowed decode through the existing 3D path on gfx942 (head_size 256, GQA 32/16, window 1024, fp8 KV, ctx 8192, window-corrected GB/s):

| batch | 2D (current) | 3D (forced) | correctness |
|------:|-------------:|------------:|:-----------:|
| 1  | 161 GB/s | 169 GB/s (flat) | PASS (max_diff 0.001) |
| 64 | 3824 GB/s | 441 GB/s (**regression**) | PASS |

**Good news:** the 3D kernel masks the sliding window correctly (all `-test` pass).

**But** simply making `use_2d_kernel` fall through to 3D gives no low-batch win and badly regresses high batch. Root cause: the non-gfx12 3D path segments the **full `max_seqlen_k`** (8192), not the window. For sliding decode only the last `window` (1024) keys are valid, so most segments are empty/masked — no occupancy benefit at low batch, pure overhead at high batch. (The gfx12 branch already special-cases `SLIDING_WINDOW > 0 -> num_segments = 1`.)

**What a real fix needs:** window-aware KV-split — segment only the last `window` keys (offset the key range to `[kv_len - window, kv_len)`) so the split fills the CUs without reading/masking the full context. That is a kernel-level change (segment-to-key mapping), not just a `select_3d_config` tweak.

**Decision:** not landing the naive routing (it regresses batch 64). Leaving this open with the window-aware-split approach as the path forward. Note the payoff is modest — windowed decode reads at most `window` keys, so the absolute cost at low batch is small and end-to-end decode is GEMM-dominated.
