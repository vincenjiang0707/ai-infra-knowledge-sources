# [Issue #4568] [Tracking] Kimi-K3-NVFP4 end-to-end kernel support

source: https://github.com/flashinfer-ai/flashinfer/issues/4568
state: open | updated: 2026-09-25T04:50:42Z
labels: priority: must have (P0), op: misc, op: linear attention

## 正文

## Goal

Track end-to-end FlashInfer kernel support for [`nvidia/Kimi-K3-NVFP4`](https://huggingface.co/nvidia/Kimi-K3-NVFP4) on B200/B300, with vLLM integration that does not require the checkpoint's compatibility patch.

Kimi-K3 is a 93-layer hybrid model with 69 KDA layers, 24 MLA layers, Attention Residuals (AttnRes), Stable LatentMoE, and a multimodal vision tower. The checkpoint uses mixed `NVFP4` experts and `FP8_PB_WO` attention projections.

## Kernel coverage checklist

### Text model

- [ ] **KDA prefill:** chunked KDA with width-4 causal convolution, SiLU, state checkpointing/paging, and CUDA Graph support.
- [x] **KDA decode primitive:** fused convolution + recurrent KDA + gated RMSNorm for production head shapes (#4243).
- [ ] **KDA serving coverage:** indexed/paged states, packed inputs, B200/B300 dispatch and performance across TP shapes (#4182, #3885, #4417, #4483).
- [ ] **MLA prefill/decode:** BF16 I/O, FP8 KV cache, query quantization, packed low-head/variable-Q decode, CUDA Graphs and prefix caching (#4178).
- [ ] **AttnRes:** graph-safe fused block-residual accumulation/normalization for `attn_res_block_size=12`, including the final output AttnRes path.
- [ ] **K3 router:** FP32 `[M, 896]` sigmoid routing with correction bias, top-16 selection, renormalized weights, and reusable graph-safe workspace. The current AlphaMoE router in #4339 supports only `E <= 512` and softmax-style selected weights.
- [ ] **Stable LatentMoE:** fused `7168 -> 3584` routed projection/norm, 896 routed experts + 2 shared experts, and `3584 -> 7168` output/tail with TP/EP communication.
- [ ] **NVFP4 SiTU experts:** group-size-16 NVFP4 experts with SiTU (`beta=4`, `linear_beta=25`) and correct scale handling across TRTLLM-GEN/CUTLASS/CuTe DSL backends (#4180, #4009, #4460). TP8-local Cake backend and complete 52-row B200/B300 report: #5183.
- [ ] **Mixed projection GEMMs:** serialized 128x128 per-block `FP8_PB_WO` KDA/MLA projections, fused-projection padding/trim, and absorbed-MLA weight preparation without runtime dequantization patches.

### FP8 GEMM inventory

The checkpoint's `hf_quant_config.json` marks 16 KDA/MLA projection target names as `FP8_PB_WO`. Track optimized kernels for the logical GEMMs below; fused names are alternate serving layouts rather than additional model math.

| Area | Manifest modules | Global logical shape(s), `K -> N` | Layers |
|---|---|---:|---:|
| KDA Q/K/V | `q_proj`, `k_proj`, `v_proj` | `7168 -> 12288` each | 69 |
| KDA output gate | `g_proj` | `7168 -> 12288` | 69 |
| KDA decay/beta path | `f_a_proj`, `f_b_proj`, `b_proj` | `7168 -> 128`, `128 -> 12288`, `7168 -> 96` | 69 |
| KDA fused input | `fused_qkvg_proj`, `in_proj_qkvgfab` | `7168 -> 49152`; `7168 -> 49376` before TP padding/trim | 69 |
| MLA query | `q_a_proj`, `q_b_proj` | `7168 -> 1536`, `1536 -> 18432` | 24 |
| MLA latent KV | `kv_a_proj_with_mqa`, `kv_b_proj` | `7168 -> 576`, `512 -> 24576` | 24 |
| MLA fused input | `fused_qkv_a_proj`, `fused_qkv_a_proj_with_mqa` | fused Q-A + latent-KV-A/MQA outputs; honor TP-local padding and split points | 24 |
| MLA output gate | `g_proj` | `7168 -> 12288` | 24 |
| Attention output | `o_proj` | `12288 -> 7168` | 93 |

Required FP8 GEMM coverage:

- [ ] BF16 input/output with serialized FP8 E4M3 weights and 128x128 block scales, including UE8M0 requantization/layout preparation.
- [ ] Both prefill (`M = tokens`) and decode (`M = active sequences`) regimes, including small-M latency and throughput-saturated batches.
- [ ] TP1 and TP8 row/column-parallel shapes; TP-local output sizes that are not multiples of 128 must use deterministic zero-padding and trim before fused-output splitting.
- [ ] Fused KDA/MLA projections and their unfused equivalents produce matching results, with arbitrary valid TP-local strides.
- [ ] MLA decode weight absorption consumes the serialized 2D block-scale layout without retaining a dequantized FP32/BF16 weight copy in the steady-state path.
- [ ] Query/input quantization, scale conversion, workspace reuse, and kernel selection are CUDA Graph safe with no per-step allocation or host synchronization.
- [ ] DeepGEMM and non-DeepGEMM/FlashInfer fallback paths have correctness parity and explicit dispatch tests; unsupported shapes must not silently run an unintended slow path.
- [ ] Benchmarks cover every unique `(M, N, K)` family above on B200 and B300 and report complete-call time, including activation quantization and scale/layout preparation.

### Multimodal path

- [ ] Vision patch embedding (`14x14` Conv2D), 27-layer ViT attention/MLP, 2x2 spatial merge + temporal pooling, and PatchMergerV2 projection (`1024 -> 7168`).
- [ ] Variable image/video token counts under CUDA Graph-compatible serving, with parity to the reference vision implementation.

## Reference configuration

| Item | Value |
|---|---|
| Hardware | B200 / B300 (SM100 / SM103) |
| Initial serving target | TP8, `modelopt_mixed`, `flashinfer_trtllm` MoE |
| Hidden size / layers | 7168 / 93 |
| KDA | 69 layers, 96 heads, head dim 128, conv width 4 |
| MLA | 24 layers, `q_lora_rank=1536`, `kv_lora_rank=512` |
| MoE | 896 routed experts, top-16, 2 shared experts, latent width 3584 |
| Quantization | NVFP4 experts (group size 16), FP8 per-block attention projections, FP8 KV |
| Context | 1,048,576 architectural maximum; 196,608 validated TP8 baseline |

TP12 saturated-decode shape gaps are tracked separately in #4542.

## Acceptance criteria

- [ ] Text-only and multimodal outputs match the reference implementation within dtype-appropriate tolerances.
- [ ] Prefill, decode, CUDA Graph replay, prefix caching, ragged batches, and changing cache/state indices are covered by tests.
- [ ] A public benchmark reports complete-call latency/throughput for each major kernel family on B200 and B300, including metadata preparation and quantization overhead.
- [ ] The published `nvidia/Kimi-K3-NVFP4` checkpoint serves through upstream vLLM with FlashInfer backends and no repository-provided `sitecustomize.py` compatibility patch.

## References

- Model/checkpoint: https://huggingface.co/nvidia/Kimi-K3-NVFP4
- Existing KDA tracker/API work: #4254, #4483
- Kimi-K3 TP12 follow-up: #4542
- vLLM mixed FP8 dispatch: https://github.com/vllm-project/vllm/pull/50617
- vLLM fused projections: https://github.com/vllm-project/vllm/pull/52406
- vLLM NVFP4 SiTU scale fix: https://github.com/vllm-project/vllm/pull/52405


## 评论 (7)

### aleozlx · 2026-08-31

@qiching 

to confirm

- is it P0
- any ETA expectation (according to the longest task)

### yyihuang · 2026-09-25

@xinli-sw Update for this request: [feat(cake_kda): add strided prefill state checkpoints and packed decode](https://github.com/flashinfer-ai/flashinfer/pull/4445) was merged on 2026-08-16 (UTC).

A serving-contract update for the KDA portion of this tracker is merged.

- Adds strided prefill state checkpoints, indexed/noncompact recurrent-state pools, and serving-native packed T=1 Kimi-K3 decode.
- Preserves caller-owned output, current-stream execution and reusable CUDA Graph workspace; supersedes the earlier packed-decode proposal #4378.

This covers part of the KDA serving checklist; it does not establish end-to-end Kimi-K3-NVFP4 support or completion of the other operators.


### yyihuang · 2026-09-25

@xinli-sw Update for this request: [feat(cake_kda): add optimized H12 packed decode across SM100 family](https://github.com/flashinfer-ai/flashinfer/pull/4562) was merged on 2026-08-18 (UTC).

The optimized packed KDA decode update is merged.

- Adds generated fixed-H12/D128 packed-decode variants and a batch selector across the SM100 family.
- Keeps row-strided beta, indexed/noncompact state, inactive graph-padding rows, caller-owned output and CUDA Graph replay; inputs outside the optimized bands retain the existing route.

This addresses the packed H12 serving path only; other head counts and end-to-end model integration remain separate work.


### yyihuang · 2026-09-25

@xinli-sw Update for this request: [feat(cake_kda): add fp32 state & long context kda prefill kernels](https://github.com/flashinfer-ai/flashinfer/pull/4845) was merged on 2026-09-05 (UTC).

The Blackwell recurrent-KDA prefill portfolio with FP32 state and long-context support is merged.

- Covers BF16 compact/indexed state, FP32 indexed state, sparse state pools and intermediate checkpoints.
- Includes qualified contexts through 1,048,576 tokens and B200/B300/GB300 validation reported in the PR.

This advances KDA prefill/state coverage; it does not by itself complete MLA, routing, SiTU experts or the remaining end-to-end checklist.


### yyihuang · 2026-09-25

@xinli-sw Update for this request: [feat(cake_kda): add fused decode backend for B200 and B300](https://github.com/flashinfer-ai/flashinfer/pull/4967) was merged on 2026-09-11 (UTC).

A generated fused KDA decode backend is merged for SM100a/B200 and SM103a/B300.

- Supports FP32/BF16 recurrent state, nullable/repeated indices with sequential updates, padded strides and signed 64-bit slot offsets.
- Supports caller-owned output and CUDA Graph capture. Select backend="cake" explicitly, or backend="auto" with the required host-known state-index mode; the default remains cute-dsl.

This notification is for the supported fused-decode contracts, not a claim that all TP layouts or the full Kimi-K3 model are complete.


### yyihuang · 2026-09-25

@xinli-sw The Cake KDA prefill update in [PR #5452](https://github.com/flashinfer-ai/flashinfer/pull/5452) was merged on 2026-09-25 (UTC). This advances the KDA prefill and serving-coverage portions of this request.

- Adds a bounded prepared-plan cache with pointer rebinding and a workspace byte budget, reducing repeated preparation overhead and supporting CUDA Graph replay on cache hits.
- Adds FP32 intermediate-state/checkpoint support for the qualified unbounded-gate paths, cached affine-split execution, and a fused affine epilogue. Bounded-gate callers retain the validated BF16 checkpoint rows.
- Publishes and validates the generated SM100/SM103 kernels on B200 and GB300, including Kimi-K3 TP8-local H12 bounded-gate prefill and packed prefix/residual workloads. The PR includes kernel, wrapper, and serving measurements with their respective scopes.

This is a KDA prefill delivery, not completion of the full Kimi-K3-NVFP4 checklist. The PR documents remaining B200 unbounded-gate split-performance and dense-H12 unbounded-carrier limitations; these should not be inferred as covered by the bounded Kimi-K3 results.


### yyihuang · 2026-09-25

@xinli-sw [PR #5531](https://github.com/flashinfer-ai/flashinfer/pull/5531) was merged on 2026-09-25 (UTC), delivering the experimental Cake Kimi-K3 fused MoE router on SM100/SM103.

- Routes FP32 logits `[M, 896]`: selects top-16 using `sigmoid(logits) + correction_bias`, then normalizes the selected unbiased sigmoid scores into routing weights. The bias affects selection only.
- Builds the expert-aligned grouped-GEMM route plan in the same launch, with `block_m` 8 or 16. The prepared runner supports allocation-free execution and CUDA Graph replay with updated values in the bound input buffers.
- Covers M = 1, 2, 4, ..., 8192 (powers of two); shapes outside this supported set raise `NotImplementedError`. The PR reports 44 tests per architecture and 28/28 source/export bitwise-validation rows on both B200 and GB300.
- Reported cold-L2 CUPTI geometric-mean speedup over SGLang `route_radix` + `moe_align_block_size` is 1.416x on B200 and 1.753x on GB300 across those 28 shapes.

This delivers the K3 router portion of the checklist for the supported shapes. It does not complete the separate SiTU expert, Stable LatentMoE, MLA, projection, or full-model integration requirements.

