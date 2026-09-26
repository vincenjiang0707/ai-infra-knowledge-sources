# [Issue #5450] Autotuner tuning_buckets override maps runtime M DOWN while SM100 cute-dsl tactics are only valid for M <= tuned bucket: vLLM warmup crash (Invalid MXFP8 split-K tactic)

source: https://github.com/flashinfer-ai/flashinfer/issues/5450
state: open | updated: 2026-09-22T15:03:57Z
labels: needs-triage

## 正文

# FlashInfer autotuner's `tuning_buckets` override maps runtime M DOWN, but SM100 block-scaled cute-dsl tactics are only valid for M ≤ tuned bucket — engine crash at vLLM warmup, silent envelope violation at serving

## Environment

- FlashInfer **0.6.18.post1** (pip, inside `vllm/vllm-openai:nightly` as of 2026-09-22)
- NVIDIA DGX Station GB300 (SM103, `sm_103a`), CUDA 13.x
- vLLM nightly (`3df4ae153` era), DeepSeek-V4.1-Flash + DSpark speculative decoding
- Both upstream `main`s today still carry the behavior described below.

## The crash

vLLM's warmup (`vllm/model_executor/warmup/kernel_warmup.py`) runs dummy forwards inside `autotune(tuning_buckets=...)`. With spec-decode enabled, the DSpark draft model forward runs at M = 8 reqs × 3 tokens = **24** — not a bucket value. The engine dies at startup:

```
ValueError: Invalid MXFP8 split-K tactic: ((128, 16), (1, 1), True, False, 4)
```

at `flashinfer/gemm/gemm_base.py:5327`, called from `mm_mxfp8` → `CuteDSLMxfp8GemmRunner.forward`.

## Root cause: the bucket-mapper direction is inconsistent between tune and apply

`mm_mxfp8`'s own tuning config uses `map_to_hybrid_bucket_uncapped` (`fused_moe/utils.py:276`), which rounds **up** (`next_positive_power_of_2`), and the split-K MMA tile is likewise chosen by rounding M up (`dense_blockscaled_gemm_sm100_splitk.py: mma_tiler_mn_for_m`: 8/16/32). So a tactic tuned at bucket b is valid for every M ≤ b — the two are consistent.

But inside `autotune(tuning_buckets=...)` the autotuner **replaces the op's mapper** with `make_bucket_mapper(buckets, round_map=round_up)` (`autotuner.py:1524-1526`), and `round_up` defaults to **False** = floor (`autotuner.py:832`, `:950`). So inside the context:

- M=24 → looked up at **bucket 16** → tactic with tile (128,16), split_k=4
- `forward()` computes `mma_tiler_mn_for_m(24)` = **(128,32)** → validation at `gemm_base.py:5314-5327` fails → raise

Outside the context (cudagraph capture, serving), the op's own round-up mapper is restored (the override is a per-thread stack popped on exit), so M=24 → bucket 32 → tile (128,32) → valid. **That's why the crash only ever appears inside vLLM's warmup** — the engine crash-loops at boot while the identical model/weights/cache serve fine once warmup is bypassed.

Relevant code:

```python
# gemm_base.py forward(), ~5314:
if is_split_k:
    if (cluster_shape_mn != (1, 1) or not swap_ab or use_prefetch
        or not out.is_contiguous()
        or not split_k_kernel_cls.is_valid_tactic(m, real_k, Float8E4M3FN, split_k_slices)
        or mma_tiler_mn != split_k_kernel_cls.mma_tiler_mn_for_m(m)):   # the kill line
        raise ValueError(f"Invalid MXFP8 split-K tactic: {tactic}")
```

## Standalone repro (no vLLM needed, any Blackwell GPU)

https://gist.github.com/ebfio/e53b51a8f3e9df0ca89e4f78e66a0846 — tunes `(N=1792, K=5120)` — tunes `(N=1792, K=5120)` (DeepSeek-V4.1 `fused_wqa_wkv` at TP1; narrow N, so split-K wins) with `tuning_buckets=(1,2,4,8,16,32,64,128,256)`, then calls the same op at non-bucket M values under all three mapper regimes, in one process, same cache:

```
tuned tactics per bucket (tile, cluster, swap_ab, prefetch, split_k):
    M=   1..8: ((128, 8), (1, 1), True, False, 4)
    M=  16   : ((128, 16), (1, 1), True, False, 4)
    M=  32   : ((128, 32), (1, 1), True, False, 2)
    M>= 64   : persistent kernels, split_k=1

inside autotune(tuning_buckets=..., round_up=False [default]):
  floor-mapped: M=24 FAILED -> Invalid MXFP8 split-K tactic: ((128, 16), (1, 1), True, False, 4)
  floor-mapped: M=12 FAILED -> Invalid MXFP8 split-K tactic: ((128, 8), (1, 1), True, False, 4)
  floor-mapped: M=40 FAILED -> Invalid MXFP8 split-K tactic: ((128, 32), (1, 1), True, False, 2)
outside any autotune context (op mapper, rounds up):
  no-context: M=24 OK / M=12 OK / M=40 OK
inside autotune(tuning_buckets=..., round_up=True):
  ceil-mapped: M=24 OK / M=12 OK / M=40 OK

RESULT: BUG REPRODUCED
```

Measured on GB300 (10,3). The floor-mapped failures are byte-identical to the engine crash, including the exact tactic tuples.

Notes:
- This is **not** a cache-key collision and a cold tune reproduces it: cache keys are `(op, runner class, bucket-mapped shapes, extras)` (`ProfilingCacheKey`, `autotuner.py:1095`) — no mapping direction. One call at a large M profiles *every* override bucket, so the poisoned pair (bucket 16 → (128,16) split-K) is cached deterministically on any fresh tune for this shape.
- The saved tactic is **correct for its bucket** — the tuner's search space is fine. The mismatch is bucket-vs-runtime-M under floor mapping.

## Why this is worse than the raise: silent envelope violations

The base (non-split-K) candidate tactics include swap-AB tiles (128, 8/16/32) (`kernels/utils.py:19-22`), and the persistent kernel's `can_implement` requires `kernel_n ≤ tile_n` for tiles under 64 (`dense_blockscaled_gemm_sm100.py:1673`) — in swap-AB, `kernel_n` is the token count. **Those base tactics get no apply-time check.** Under floor mapping, a (128,16) swap-AB winner tuned at bucket 16 can be applied at M=24, silently outside its envelope. The split-K validator is just the one place that notices.

The same tactic generator serves `mm_fp4` cute-dsl (`_get_sm100_block_scaled_tactics`, shared by both), so NVFP4 models with speculative decoding are exposed to the same family. Scope: cute-dsl only — CUTLASS's runner uses integer config indices with no M-dependent apply validation; the TRT-LLM path is a separate issue (vllm-project/vllm#58031).

## Two fix directions (maintainer call)

1. **Honor the op's mapping direction when buckets are overridden** (or default `round_up=True` for the override): then a tactic at bucket b is only ever applied to M ≤ b, which is exactly the envelope both split-K and the small-tile base tactics guarantee.
2. **Size small tiles against the profile's `DynamicDim.max`** (next bucket) instead of `opt`, so a bucket-16 winner is valid through M=32.

Either way, the apply-side can be hardened independently: re-derive the tile from runtime M and keep the tuned slice count, falling back to the untuned low-M tactic when split-K can't serve that M (draft patch available — `flashinfer_splitk_apply.patch`, happy to turn it into a PR).

## Downstream fix (vLLM side)

vLLM works around this today with one line in `kernel_warmup.py:363`:

```python
with fi_utils.autotune(tuning_buckets=tuning_buckets, round_up=True):
```

Tune-context mapping then equals serving-time mapping; tactic choices and the cache file are unchanged (profiling is per bucket), only the dummy run's execution path changes. PR incoming, referencing this issue.


## 评论 (1)

### ebfio · 2026-09-22

Downstream vLLM fix (one line) is up: https://github.com/vllm-project/vllm/pull/58165 — verified live on GB300; the crash-looping boot comes up clean and serves with full CUDA graphs. Happy to contribute the apply-side hardening patch as a PR here if maintainers want belt-and-braces.
