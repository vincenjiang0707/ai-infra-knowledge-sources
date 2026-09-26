# [Issue #5243] [Perf] 0.1.21 slower than 0.1.19 for GLM-5.3 MXFP4 on gfx950 (−18 % prefill, −10 % throughput); FlyDSL MoE tuning?

source: https://github.com/ROCm/aiter/issues/5243
state: open | updated: 2026-09-06T19:42:20Z
labels: 

## 正文

Field report on **0.1.21 vs 0.1.19 for GLM-5.3 (full, `glm_moe_dsa`) on 4x MI355X**, in case it is useful for the release notes: 0.1.21 is a consistent slowdown for us, with identical accuracy.

Setup: ROCm 7.2.3, vLLM fork (2026-08-27), Quark MXFP4 checkpoint (`amd/GLM-5.3-Quark-MXFP4-AttnFP8`), fp8 KV, MTP k=3, TP4, block size 16, same instance, same night, back to back:

| | 0.1.19 | 0.1.21 (+ flydsl 0.3.2) |
|---|---:|---:|
| prefill, 128k prompt | 13 461 tok/s | 11 013 tok/s (−18 %) |
| 900k-token needle prefill | 127 s | 136 s |
| decode, single stream | 119 / 127 tok/s | 110 / 110 tok/s |
| throughput, 64 concurrent | 619 / 631 tok/s | 559 / 566 tok/s (−10 %) |
| perplexity (held-out) | 1.31810 | 1.31809 |
| needles 30k–900k | 4/4 | 4/4 |

Our 0.1.19 image carries a locally tuned `a8w8_blockscale_tuned_gemm.csv` for the four attention/dense shapes of this model (untuned, those fell back to `libtype=torch`). 0.1.21 routes the MXFP4 MoE GEMMs through FlyDSL instead, so our tuning no longer applies — that is our working explanation for the gap, not a claim. Two questions:

1. Is there a tuner for the FlyDSL MoE kernels comparable to `aiter/utility/pretune.py` for `module_gemm_a8w8_blockscale_tune`, or config files (`AITER_CONFIG_FMOE` / `AITER_CONFIG_GROUPED_FMOE`) we should populate for gfx950 + these shapes (hidden 6144, 256 experts, top-8, intermediate 1536)?
2. Two packaging notes that cost us time, in case they help others: 0.1.21 requires `flydsl==0.3.2` (with 0.2.4 the MXFP4 MoE path dies in `mixed_moe_gemm_2stage_common.py` with `Operand 3 of operation "rocdl.raw.ptr.buffer.load" must be a Value (contained a None item)`, which looks like a Triton/Gluon problem but is not), and the `hipcc -v` workaround for ROCm 7.2 lives in aiter's own `aiter/jit/utils/cpp_extension.py`, so a wheel upgrade silently reverts it.

Happy to run any tuning flow you suggest and report numbers.

## 评论 (1)

### stefanskiasan · 2026-09-06

Follow-up with evidence from your own tuning tables rather than from our
end-to-end numbers.

`aiter/configs/model_configs/glm5_fp4_tuned_fmoe.csv` carries the tuner's
measured `us` per shape. Comparing tag `v0.1.19` against `v0.1.21.post1`, for
`gfx950 / model_dim 6144 / inter_dim 512 / expert 257 / topk 9` (that is the
TP4 slice of GLM-5.3, MXFP4 both sides, `QuantType.per_1x32`, Silu):

| Tokens | 0.1.19 µs | 0.1.21 µs | Δ | same kernel? |
|---:|---:|---:|---:|---|
| 1 | 23.29 | 18.87 | −19.0 % | no |
| 256 | 226.90 | 217.86 | −4.0 % | no |
| 2048 | 392.51 | 366.60 | −6.6 % | no |
| 4096 | 614.15 | 540.77 | −11.9 % | no |
| 8192 | 876.67 | 880.49 | +0.4 % | no |
| **16384** | **1439.86** | **1625.86** | **+12.9 %** | **yes** |
| 32768 | 2623.92 | 2997.84 | +14.3 % | stage-2 differs |

Most shapes improved. The interesting row is **16384**, because there the
tuner picked the *identical* kernel pair and the *identical* `block_m` in both
versions:

```
0.1.19: block_m=128  flydsl_mxmoe_g1_a4w4_128x256x256
                     flydsl_mxmoe_g2_a4w4_128x256x256_f4out
0.1.21: block_m=128  flydsl_mxmoe_g1_a4w4_128x256x256
                     flydsl_mxmoe_g2_a4w4_128x256x256_f4out
```

Same kernel, same tile shape, same tuner, 12.9 % more time. That is not a
configuration or dispatch issue — it points at the kernel implementation or at
the FlyDSL version underneath (0.3.2 landed 25.08., between the two tags).

At 32768 the stage-2 kernel does differ (`_f4out` was added), so that row is
less conclusive; 16384 is the clean comparison.

Note this also means the table does **not** explain the end-to-end regression
we originally reported: at 8192 — our `max-num-batched-tokens` — the tuner
measures +0.4 %, i.e. no change. So there are likely two separate things here,
and the 16384 row is the one that is reproducible from your side alone,
without our serving setup.

Related: #5227 reverted #4994 ("fuse stage-1 fp8 quant on the heuristic FlyDSL
fallback") on 03.09. with the note "due to bad quality", seven hours after
merge. The MXFP4 MoE path is clearly in motion right now.
