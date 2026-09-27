# [Issue #3712] [Feature] Performant Blockwise 128x128 FP8 MoE Group Gemms for SM10x GPUs

source: https://github.com/flashinfer-ai/flashinfer/issues/3712
state: closed | updated: 2026-09-27T00:40:49Z
labels: priority: must have (P0), model: qwen3.5 / 3.6 / 3.8, op: moe

## 正文

[Feature] Performant Blockwise 128x128 FP8 MoE Group Gemms for SM10x GPUs

Currently, SGLang is using DeepGemm kernels for Blockwise 128x128 FP8 MoE Group Gemms for SM10x GPUs, but the simulation shows that the kernels only achieve ~50% of the projection, and even just 30-50% in the Prefill phase (in 8k1k TP mapping).

The request is to have new Blockwise 128x128 FP8 MoE Group Gemms (or MoE) implementations that can push the performance to 80% of the projection.

Expected perf gain is: +14% for Ctx iter perf and +5% e2e perf for Qwen 3.5 on SM10x GPUs for TP setting.

My current guess is that DeepGemm kernels are more optimized for EP (and wideEP) settings but less optimized for TP settings. But ideally we want an implementation that is not slower than DeepGemm kernels for EP/wideEP setting, while being faster than DeepGemm kernels for TP setting.

The desired backend is cute-dsl, but it is also okay if this must be implemented with trtllm-gen backend.

## 评论 (11)

### nvpohanh · 2026-06-24

cc @YAMY1234 @leejnau 

### xinli-sw · 2026-06-25

cc @sricketts 

### aleozlx · 2026-07-08

@Aneureka may be able to follow up with cute dsl kernel dev team to check on this

### Aneureka · 2026-07-08

!claim

### flashinfer-bot · 2026-07-08

This issue is already assigned. If you'd like to take over, ask a maintainer to use `!assign @Aneureka`.

### aleozlx · 2026-07-15

kernel dev team is looking. currently no solution yet

### nv-yunzheq · 2026-08-26

@nvpohanh There is a PR to try to address the problem #4734 Could you take a look to see if it will address the problem mentioned here?

### nvpohanh · 2026-08-27

Thanks! However, currently SGLang does not call the `group_deepgemm_fp8_nt_groupwise()` function call directly for blockwise FP8 MoE yet. Verifying this would need to make some SGLang-side code changes.

I think we can merge it first for now and we will verify if it can improve Qwen 3.5 FP8 or Qwen 3.8 FP8 perf. Thanks!

cc @YAMY1234 

### nv-yunzheq · 2026-09-15

Given that the improved kernel has been merged, the issue is closed automatically.
Please reopen the issue if the PR does not address the underlying performance issues.

### yyihuang · 2026-09-26

@nvpohanh [PR #5500](https://github.com/flashinfer-ai/flashinfer/pull/5500) was merged on 2026-09-26 (UTC), delivering a Cake prepared contiguous grouped FP8 GEMM for SM100a/B200, following the math contract of #4734.

- Entry point: `flashinfer.gemm.prepare_group_gemm_fp8_nt_groupwise_contiguous(...).launch()`. It consumes FP8 E4M3 activations and expert weights, FP32 per-row K/128 activation scales and 128x128 weight block scales, with FP32 accumulation and BF16 output.
- Supports sorted expert indices, empty experts, and expert boundaries at arbitrary rows. M/G must be positive; N/K must be positive multiples of 128. The first launch initializes descriptors outside CUDA Graph capture; subsequent launches submit one kernel and can be captured.
- The PR's updated B200 cold-L2 CUPTI comparison reports 1.006-1.163x speedups over the CuTe-DSL operator across the six TP8/EP8/WideEP32 workloads, with a 1.082x geometric mean.
- Source/export outputs match bitwise on all 29 reported validation rows. Only 19/29 pass every export/performance gate; some small correctness cases are slower than CuTe-DSL, so the six-workload speedup is not a universal claim.

This delivers the standalone B200 kernel. B300/SM103a, SGLang integration, and the requested Qwen context/end-to-end gains are not established by this PR. Cake follow-up tracking is under #4254.


### yyihuang · 2026-09-27

@nvpohanh Merged: https://github.com/flashinfer-ai/flashinfer/pull/5567

Following #4734 / #5500, this adds the **SM100a/B200 grouped FP8 gate/up GEMM + SwiGLU + FP8 group-quantization** operator: `flashinfer.gemm.prepare_group_gemm_fp8_nt_groupwise_contiguous_silu_quant(...).launch()`.

- Returns FP8 E4M3 activations and per-token 128-group scales. M >= 2048 uses one fused kernel; smaller M uses grouped GEMM followed by a fused activation/quantization kernel, reducing three launches to two.
- Requires expert-sorted rows, **128-row-aligned internal expert boundaries**, M <= 8192, `2H % 256 == 0`, and `K % 512 == 0`. Empty experts and a partial final expert block are supported. This is narrower routing than the standalone #5500 GEMM.
- The first launch initializes descriptors outside CUDA Graph capture; subsequent prepared launches are capturable.

The PR reports 29 passing B200 tests and 11/11 export rows passing all gates. Across three wide-EP32 performance routings, geometric-mean speedup is 1.275x over the faster of the CuTe-DSL-GEMM and Cake-GEMM three-kernel chains.

This delivers the gate/up stage through quantized activation output on B200. It does not establish B300 support, full-MoE/SGLang integration, or the requested Qwen context/end-to-end gains.

