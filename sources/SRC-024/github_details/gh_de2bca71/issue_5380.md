# [Issue #5380] [Config] bf16_tuned_gemm.csv ships no gfx942 rows - every bf16 GEMM falls back to torch on MI300X

source: https://github.com/ROCm/aiter/issues/5380
state: open | updated: 2026-09-09T18:09:39Z
labels: 

## 正文

**Environment**: 8x MI300X (gfx942, 304 CU), ROCm 7.2, amd-aiter 0.1.19.post3, via SGLang 0.5.19.

## Issue
`aiter/configs/bf16_tuned_gemm.csv` in `main` contains **120 `gfx1250` rows and 112 `gfx950` rows, and zero `gfx942` rows**.

The runtime lookup keys on `(gfx, cu_num, M, N, K, ...)`, so on MI300X nothing can ever match and every bf16 GEMM logs:

```
[aiter] shape is M:8192, N:32, K:6144 dtype='torch.bfloat16' ... not found tuned config in
/tmp/aiter_configs/bf16_tuned_gemm.csv, will use default config! using torch solution:0
```

## Scale
Serving GLM-5.3 (753B DSA MoE) we counted **952 such misses per boot**, concentrated on the DSA indexer projection shapes `M in {8, 80, 88, 8192} x N in {32, 256} x K=6144` - which is the O(L^2) long-context hot path, so it is not a rare corner.

## Request
Ship gfx942 rows for the common shapes, or document that MI300X users should self-tune with `csrc/gemm_a16w16/gemm_a16w16_tune.py`. We are generating a gfx942 table for these shapes and are happy to contribute it back if useful.


## 评论 (1)

### skimanwhite · 2026-09-09

## Follow-up: we tuned all 123 shapes and measured **no end-to-end change** - correcting our own impact claim

We generated a gfx942 table for the shapes our workload actually hits and re-measured. In fairness to whoever triages this, the impact framing in the original report was overstated and we want to correct it rather than leave it standing.

**What we did.** Ran `csrc/gemm_a16w16/gemm_a16w16_tune.py` over 123 recorded shapes (collected via `AITER_TUNE_GEMM=1`) on 8x MI300X. 123/123 rows written, 0 errors, ~28 minutes. `bf16_tuned_gemm.csv` went from 0 to 123 `gfx942` rows, so the `not found tuned config ... using torch solution:0` messages are gone.

**End-to-end result: nothing measurable.** Same server config, warm two-pass methodology, three repeat passes after tuning:

| context | before tuning | after tuning (3 passes) |
|---|---|---|
| ~104k prefill | 4,639 tok/s | 4,716 / 4,565 / 4,578 tok/s |
| decode @ ~46k | 44.8 tok/s | 45.1 / 45.3 / 45.0 tok/s |

(Our ~8k and ~50k points swing widely between passes with or without tuning, so we do not read anything into those.)

**Why we think the original framing was wrong.** We described these shapes as the "O(L^2) long-context hot path". They are the DSA indexer **projections**, which are O(L), not O(L^2) - the quadratic part is `fp8_mqa_logits`, a different kernel that does not appear in this table. And the tuned kernels land around 390 TFLOPS on the large shapes:

```
32768x256x6144   264.6us   389.6 TFLOPS
    1x32x6144      5.3us     0.07 TFLOPS
```

which is apparently not far from what the torch fallback was already achieving for these shapes. The many small `M x 32 x 6144` entries are single-digit-microsecond GEMMs, so 952 misses per boot sounds worse than it is.

**What we think still stands.** `bf16_tuned_gemm.csv` shipping only `gfx1250` and `gfx950` rows, with the lookup keyed on `(gfx, cu_num, ...)`, does mean MI300X users get no tuned bf16 GEMMs and a wall of log noise. That is worth fixing or documenting - we just no longer claim it is a significant performance loss, at least for this model's shapes.

Our offer to contribute the gfx942 table stands if it is useful, with the caveat above that we could not measure a benefit from it.

