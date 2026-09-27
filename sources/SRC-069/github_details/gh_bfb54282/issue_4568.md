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


## 评论 (20)

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

### yyihuang · 2026-09-25

@xinli-sw [PR #5548](https://github.com/flashinfer-ai/flashinfer/pull/5548) was merged on 2026-09-25 (UTC), as a performance follow-up to the Cake Kimi-K3 fused router delivered in [PR #5531](https://github.com/flashinfer-ai/flashinfer/pull/5531).

- Removes a redundant per-thread device fence before the cooperative grid synchronization in the M256 and M512/M1024/M2048 routes on SM100/SM103. The grid join supplies the required release/acquire synchronization.
- Preserves the routing semantics, expert-aligned plans, public APIs, and supported shape set.
- The PR reports paired same-node improvements over the previous programs of about 3% at M256, 5–7% at M512, 5% at M1024, and 3–4% at M2048 on B200 and GB300.
- Validation reported in the PR includes 44 public tests per architecture, bitwise source/export parity on all 28 shapes per architecture, and passing synchronization/race sanitizer checks.

This updates the K3 router portion of the checklist; it does not complete the other Kimi-K3 kernel or model-integration requirements.


### yyihuang · 2026-09-26

@xinli-sw Merged: https://github.com/flashinfer-ai/flashinfer/pull/5543

This follows up on #5452 for Cake KDA prepared prefill on SM100/SM103 (B200/B300):

- Replaces the fixed affine-split threshold with architecture- and gate-specific measured cost models, and improves window allocation for packed long/short sequences.
- Reduces prepared-plan cache/rebind overhead and combines affine index preparation into one kernel. The PR reports every tested Kimi-K3 bounded-gate row faster than the Triton reference on both architectures.
- Separately adds the missing dense `[tokens, 12]` beta variants for the unbounded softplus gate (sequential, FP32 checkpoint, and affine paths), with 359/359 export-validation rows matching the source bitwise per architecture. This unbounded-gate extension is distinct from Kimi-K3's bounded-gate path.

This advances the KDA prefill/serving portion of this issue; it does not complete the full end-to-end checklist. Some unbounded-gate long-pack cases still trail the reference, as documented in the PR.


### yyihuang · 2026-09-26

@xinli-sw Merged: https://github.com/flashinfer-ai/flashinfer/pull/5134

The relevant part for this issue is Cake NVFP4 warp-decode support for the Kimi-K3 latent expert bank: H=3584, I=3072, 896 experts, top-16, SiTU with gate beta=4 and linear beta=25, for decode token counts 1–32 on SM100/SM103 (B200/B300).

The PR reports correctness validation and separate synccheck/racecheck runs with zero errors for the exported routes. For this Kimi-K3 configuration, all 32 token-count rows on each architecture beat the official FlashInfer baseline and meet the export no-regression gate (at most 3% slower than the source implementation).

This covers the standalone NVFP4 expert-bank decode path. It does not establish completion of the surrounding Stable LatentMoE projections/norm, shared experts, TP/EP communication, or end-to-end serving integration, and does not claim coverage across all requested backends.


### yyihuang · 2026-09-26

@xinli-sw [PR #5554](https://github.com/flashinfer-ai/flashinfer/pull/5554) was merged on 2026-09-26 (UTC), delivering the experimental Cake Kimi-K3 vision tower on SM100/SM103 (B200/B300).

- Covers 14x14 patch embedding, the 27-layer MoonViT-3D attention/MLP encoder, final normalization, 2x2 spatial merge with temporal pooling, and PatchMergerV2 projection to BF16 `[N, 7168]` outputs.
- Consumes normalized BF16 patches `[T, 3, 14, 14]` and packed image/video grids. Supported grids have `1 <= t <= 4` and positive even `h, w <= 512`. `prepare_kimi_k3_vision_tower` binds a grid layout and reusable buffers; its runner launches without allocation or host synchronization and supports CUDA Graph replay with updated pixel values in the bound buffer. A different grid layout requires its own prepared plan.
- The PR reports 22/22 export-validation rows passing per architecture, bitwise source/export parity, and FP32-oracle accuracy checks. Reported geometric-mean speedup over the BF16 reference tower using the fastest measured FlashInfer attention route is 1.945x on B200 and 1.990x on B300.

This delivers the standalone vision-tower portion of the multimodal checklist. Full-checkpoint vLLM integration without compatibility patches and the remaining text-model requirements are still separate acceptance criteria.


### yyihuang · 2026-09-26

@xinli-sw Merged: https://github.com/flashinfer-ai/flashinfer/pull/5564

This is a performance follow-up to #5531 / #5548 for the **K3 router checklist item**, targeting the largest supported batches on SM100/SM103 (B200/GB300).

- Optimizes the four combinations of `M = 4096 / 8192` and `block_m = 8 / 16` with warp-per-row top-16 selection and paired expert-segment sorting, using four CTAs per SM on both architectures.
- Preserves routing over FP32 `[M, 896]` logits: bias affects selection only, returned weights normalize the selected unbiased sigmoid scores, and ties prefer the lower expert ID. Expert-aligned route plans, public APIs, and the supported shape set are unchanged; the other 24 shape programs per architecture are unchanged.
- The PR reports source-side paired speedups over #5548 of **1.206–1.319x on B200** (geomean 1.266x) and **1.144–1.186x on GB300** (geomean 1.163x) across the four affected shapes. These are incremental kernel improvements over the previous Cake router.

Reported validation includes 44 package tests per architecture, bitwise source/export parity on all 28 shapes per architecture, and clean synccheck/racecheck runs.

This improves the standalone router for the specified batch sizes. The SiTU experts, Stable LatentMoE, MLA, projection kernels, and full-model integration requirements remain separate checklist items.


### yyihuang · 2026-09-26

@xinli-sw Merged: https://github.com/flashinfer-ai/flashinfer/pull/5565

This follows #5543 for the Cake BF16 KDA prefill implementation on SM100/SM103 (B200/GB300), relevant to this issue's prefill and checkpoint/paging coverage.

- Moves FP32 checkpoint writes off the recurrence's compute-warp critical path and improves the gate scan and state restore.
- Fixes a page64 phase-tracking deadlock in the bounded-gate, FP32-pool checkpoint route: affected sequences longer than 128 tokens could hang on the route for sequences up to 256 tokens.
- Fixes the nvcc host-pass guard for rank-3 TMA reduce-add and aligns the checkpoint-panel descriptor with the FP32 carrier layout. Public APIs, plan-cache behavior, and route selection are unchanged.

The PR reports bitwise source/export agreement for output, final state, and checkpoint rows on all 359 validation rows per architecture, 71 passing package tests per architecture, and clean synccheck/memcheck runs. The benchmark coverage includes Kimi-K3 bounded-gate H12/H16 workloads; the separately reported unbounded-softplus improvements should not be read as Kimi-K3 bounded-gate speedups.

This updates the KDA prefill implementation and its checkpoint handling; the remaining model-kernel and end-to-end integration checklist items remain separate.


### yyihuang · 2026-09-26

@xinli-sw Merged: https://github.com/flashinfer-ai/flashinfer/pull/5570

This is the performance follow-up to #5554 for the experimental Cake Kimi-K3 vision tower on SM100/SM103 (B200/B300/GB300), covering the existing 27-layer MoonViT-3D encoder and PatchMergerV2 implementation.

- Adds packed BF16 residual epilogues, residual/norm-weight prefetch, a packed FP16-pair RoPE table, and attention-descriptor prefetch.
- Updates the tile-selection policy and enables programmatic dependent launch across the tower's stages in the generated bindings.

The PR reports all 22 validation rows passing on each architecture, including bitwise source/export parity, the FP32-oracle comparison gates, and source/export timing qualification. Those timing ratios measure export parity, not incremental speedup over #5554 or full-model throughput.

This updates the standalone vision-tower implementation. Checkpoint integration and end-to-end multimodal serving remain separate acceptance criteria.


### yyihuang · 2026-09-26

@xinli-sw Merged: https://github.com/flashinfer-ai/flashinfer/pull/5572

This delivers an **experimental Cake backend for the Kimi-K3 serialized FP8_PB_WO KDA/MLA projection GEMMs** on SM100/SM103 (B200/B300).

- Adds weight/workspace preparation, an allocation-free prepared runner with CUDA Graph capture, and `flashinfer.gemm.kimi_k3_fp8_projection`.
- Consumes serialized E4M3 weights with ModelOpt 128x128 FP32 block scales, requantizes/prepacks weights to UE8M0 once, quantizes BF16 activations per token in 1x128 blocks, and returns BF16 outputs. Handles padded weights, valid-column trimming, fused-projection output views, and even output row strides.
- Covers 22 representative TP1/TP8 KDA/MLA projection families across decode and prefill sizes. The report includes 132 performance rows and 88 additional correctness rows per architecture.

The PR reports 220/220 rows correct and 30 passing package tests on each GPU. Against the fastest tested complete FP8 chain, reported geometric-mean speedups are 1.639x on B200 (131/132 rows faster; TP1 kv_b at M=256 is 0.976x) and 1.626x on B300 (132/132). Seven source/export rows did not pass timing qualification, although all passed correctness.

This delivers the standalone projection backend. It does not by itself implement absorbed-MLA weight preparation, automatic vLLM integration, or the full checkpoint-serving acceptance criteria.


### yyihuang · 2026-09-26

@xinli-sw Merged: https://github.com/flashinfer-ai/flashinfer/pull/5568

This follows #5564 for the **K3 router checklist item** on SM100/SM103 (B200/GB300).

- Optimizes the 12 routed shapes with M = 256/512/1024/2048/4096/8192 and `block_m` = 8/16 using split cooperative barriers and, for the largest batches, a warp-level shortcut in the first radix-selection round.
- Preserves top-16 selection over 896 biased sigmoid scores, normalization of the selected unbiased weights, tie ordering, and expert-aligned route plans. APIs and the supported shape set are unchanged; the 16 smaller shape routes keep the same kernel logic.
- The PR reports paired kernel speedups over #5564 of approximately 1.057–1.061x geometric mean across the 12 affected shapes, with every changed row faster in both runs on each architecture.

Reported validation includes bitwise source/export parity on all 28 shapes per architecture, 44 package tests per architecture, and clean synccheck/racecheck runs.

This updates the standalone router; the SiTU expert, Stable LatentMoE, MLA, projection, and full-model integration requirements remain separate checklist items.


### yyihuang · 2026-09-26

@xinli-sw Merged: https://github.com/flashinfer-ai/flashinfer/pull/5573

Scope clarification for this tracker: this follows #5565 in the shared Cake KDA prefill implementation on SM100/SM103, but its new performance route applies **only to the unbounded gate** (`lower_bound is None`). Kimi-K3's bounded-gate composite continues to use the #5565 correction chain, so this merge does not claim a new bounded-gate Kimi-K3 speedup.

- Adds a fused-apply schedule for long unbounded-gate sequences, using exported chunk operators, pair-map/prefix processing, and one apply kernel in place of the additional correction/map chain passes.
- Fixes the H12 beta-word export used by that new route, restricts the route to the unbounded gate, and retains the correction-chain fallback via `CAKE_KDA_AFFINE_APPLY=0`.

The PR reports 359/359 source/export validation rows matching bitwise per architecture and 76 passing package tests on both B200 and GB300, including fallback and bounded-gate regression coverage. Apply-versus-chain validation is within one BF16 ulp on the tested H12/H16 outputs; it is not a claim of bitwise identity between the two schedules.

This is a shared-prefill implementation follow-up; the remaining Kimi-K3 end-to-end acceptance criteria are unchanged.


### yyihuang · 2026-09-27

@xinli-sw Merged: https://github.com/flashinfer-ai/flashinfer/pull/5575

This delivers the **experimental Stable LatentMoE front/tail projection backend** for Kimi-K3, through `flashinfer.kimi_k3_latent_moe` with `backend="cake"`.

- Front: computes FP32 router logits `[T, 896]`, the BF16 7168-to-3584 routed projection, and the shared-expert SiTU intermediate in one launch.
- Tail: sums caller-supplied routed partials, applies KimiRMSNorm, and combines the rank-local up-projection with the shared-down contribution into BF16 `[T, 7168]`. Decode uses one launch; prefill uses RMSNorm plus GEMM. The final cross-rank all-reduce remains the caller's responsibility.
- Supports TP1/TP8 and model-layout BF16 weights, with prepared allocation-free runners and CUDA Graph replay. The current planner explicitly requires **148 SMs** on SM100/SM103; other SM counts, TP12, and EP are outside this delivery.

The PR reports 39 passing package tests on each B200/B300 test configuration. Export timing qualification passed 49/60 rows per architecture; clock/drift failures remain disclosed, with those configurations covered by correctness tests.

This delivers the projection groups around the routed experts, not the routed-expert computation, top-k router selection, communication, or full-model integration. It does not fulfill the separate TP12 tail request in #4542.


### yyihuang · 2026-09-27

@xinli-sw Merged: https://github.com/flashinfer-ai/flashinfer/pull/5552

This adds the **Cake Kimi-K3 FP8 paged MLA attention backend** on SM100/SM103, accessible through `trtllm_batch_decode_with_kv_cache_mla(..., backend="cake")` and `flashinfer.mla.KimiK3MlaFp8PagedAttention`.

- Accepts **FP8 E4M3 query and KV cache** with page size 64 and 512 latent + 64 additional QK channels, producing BF16 output. Query quantization is outside this attention operator.
- Covers TP8-local H12 and global H96 decode, packed variable-Q/MTP cases through `cum_seq_lens_q` (tested q lengths up to 8), and incremental prefill with ragged KV, prefix reuse, and changing page tables. Prepared launches support caller-owned buffers and CUDA Graph replay.
- DCP, LSE output, sparse top-k MLA, and NVFP4/uint8 caches are explicitly unsupported. This therefore does not fulfill the separate CuTe-DSL/DCP request #4658 or NVFP4 MLA request #4644.

The PR reports 22 passing route tests per GPU and 27/28 export rows passing all gates per architecture; one long-prefill row fails only clock qualification. Performance is shape-dependent: 20/27 B200 and 16/27 B300 benchmark rows beat the fastest existing FlashInfer route, with regressions disclosed on other rows.

This advances the FP8 MLA attention item; cache production and end-to-end serving integration remain separate.


### yyihuang · 2026-09-27

@xinli-sw Merged: https://github.com/flashinfer-ai/flashinfer/pull/5577

This advances the **packed variable-Q MLA decode** item with a separate experimental Cake DCP implementation on SM100/SM103, complementing the non-DCP FP8 paged MLA route in #5552. The focused request is #4658.

- `flashinfer.mla.cake_mla_varq_dcp_decode` / `prepare_cake_mla_varq_dcp_decode` support `cum_seq_lens_q`, rank-local paged KV, per-query global causal masking, and natural-log LSE for cross-rank merging. Prepared runners support caller-owned buffers and CUDA Graph replay.
- Query and cache must share BF16 or FP8 E4M3 dtype; keys are 512 latent + 64 RoPE channels, outputs are BF16, and registered routes cover page sizes 32/64/128 with up to 128 heads. Low-head correctness tests include H12/H24/H48 in BF16; the published FP8 performance matrix does not establish FP8 H12 performance.
- Query quantization, cache production, cross-rank communication/merging, and vLLM integration remain outside this operator. Access is through the explicit APIs above; #5552's existing dispatch does not acquire DCP/LSE support from this change.

The PR reports **1.1791x B200 / 1.1817x GB300 geometric-mean speedup** versus CuTe-DSL across 24 performance rows, all faster on both GPUs, with 22 passing / 3 skipped package tests per GPU. These are attention-kernel results; the full end-to-end checklist remains open.
