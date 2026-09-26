# [Issue #4254] [CAKE] Long-term CAKE-generated Kernel Progress Tracker

source: https://github.com/flashinfer-ai/flashinfer/issues/4254
state: open | updated: 2026-09-25T10:12:47Z
labels: needs-triage, op: misc, op: linear attention

## 正文

To track multi-platform kernels generated from CAKE 🍰.

We are more than happy to take any new kernel challenges!

**Feel free to reach out/leave your comments/create sub-issues here to submit your customized CAKE kernel request. And we will bake it for you!**

**We know many of you have been asking for training kernels—and we heard you.** You have had your CAKE going forward; now it is time to take it **back**! Follow the dedicated forward & backward tracker at #4642, bring us your toughest training bottleneck, and let us bake the full pass together. 🍰🔥

## Pull requests

### Communication

- #5528 — CAKE-generated SM100 eight-peer fused residual-add + two-track RMSNorm + BF16 combine (`flashinfer.comm.cake_fused_norm_combine`, one launch per rank, one-shot Lamport below 256 tokens / fence-free owner reduce at and above); B200 export validation **6/6 pass** with bitwise source/export parity; vs the unchanged customer kernel on its four resolved shapes GM **1.208048×** (T1 1.038×, T8 1.169×, T64 1.129×, T256 1.555×; T1024/T2048 export-only because the customer kernel stalls there).
- #5540 — CAKE-generated SM103 (B300) eight-peer fused residual-add + two-track RMSNorm + BF16 combine, follow-up to #5528 (`flashinfer.comm.cake_fused_norm_combine` now resolves the module by device capability); 8x B300 validation 6/6 rows correct, customer-kernel GM 1.198x.
- #5512 — CAKE-generated SM100/SM103 DCP all-to-all kernels for CP2 and CP4.
- #5514 — CAKE-generated SM100 world-size-4 TRT-LLM MoE all-reduce fusion union (one-shot Lamport all-reduce + MoE expert reduction + residual + RMSNorm in one kernel) behind `trtllm_moe_allreduce_fusion(backend="cake")`; B200 export validation **10/10 pass** with bitwise source/export parity; vs `backend="trtllm"` GM **1.077623×** (8/10 rows faster, up to 1.398112× at FP16/T128/E16/PDL).
- #5263 — generated Ulysses all-to-all for SM100/SM103, world sizes 2/4/6/8; B200 export validation **40/40 pass**. Pre-export source speedups vs FlashInfer: **1.351450× / 1.333965× / 1.368140× / 1.299633×**; vs NCCL: **1.460209× / 1.481353× / 1.668339× / 1.545083×**. Separate large-BF16 source/export ratios: **0.999980× / 1.000501× / 0.999021× / 1.001774×**. SM103 compile/link passed; B300 runtime correctness and performance remain unmeasured.
- #4730 — opt-in SM100/SM103 fused MoE all-reduce (TP2/TP4/TP8); final native validation 32/32 (B200 20/20, B300 12/12), 28 symbols and 96 dispatch cases; live-baseline GM speedups **1.122930× / 1.121959×** (B200/B300), minimum **1.065517× / 1.059156×**; measured source `cc8a5d2cc35c`. SGLang integration: [sgl-project/sglang#39214](https://github.com/sgl-project/sglang/pull/39214), source `5f53aee2a236`, with end-to-end validation focused on correctness. **TP8 B200 and B300 each pass 16/16 real BF16 payload comparisons**, finite with zero tolerance mismatches at `atol=rtol=0.01`; all eight ranks call the fused API in eager execution and graph capture, including batch size 1, with **35 actual full decode graph replay observations per architecture**. GSM8K16 on each architecture: reference **13/16**, fused **15/16**; no scored regressions, but the two differences are trailing-number parser sensitivity and both original per-question score-equality analyses remain FAIL. Each consumer mode produces identical text/token sequences across B200 and B300 for all 16 examples; all finite/stop, route/consume-once, full-graph replay, and cleanup checks pass. Correctness evaluation is complete with these scoring limitations. Kernel speedups above are separate from these SGLang correctness checks.
- #4784
- #4822 
- #5116 — SM100/SM103 TP8 packed-QKV all-gather matmul; source/cuTile speedup is greater than 1 for all seven shapes on eight B200 and eight B300 GPUs (GM **1.370700× / 1.347343×**). Real Llama-3.1-70B-Instruct true-SP TP8 end-to-end correctness passes on both architectures with synchronization disabled: **96/96 candidate/native and 96/96 native-stability request sequences match per architecture**. SGLang integration: [sgl-project/sglang#36766](https://github.com/sgl-project/sglang/pull/36766).
- #4875
- #5169 — reduce SM120 PCIe IPC all-reduce publication overhead (TP4/TP8)

### Attention

#### FMHA

##### Paged Attention

- #4980 
- #5369

##### Paged Attention with DCP

- #5111 — enable the existing DCP speculative attention family on SM107.

- #4518

##### GQA

- #5302 — experimental prepared SM110 GQA decode API and optimized generated routes.

- #5052 
- #5474 — experimental on-device load-balanced BF16 paged GQA decode for SM100/SM103 (kernel-owned length-aware scheduler for ragged batches, one persistent launch that replays under CUDA Graph for any KV-length distribution; ragged AgentX rows 1.05–1.49× vs trtllm-gen on GB200 and 1.00–1.45× on B300, uniform within a few percent; MTP q_len>1 correct but not yet a fast path)
- #5490 — packed-row MTP fast path for the #5474 balanced GQA decode (q_len_per_req 3–8 served by 32/64-row packed tiles, each KV block streamed once per request; vs trtllm-gen MTP: GB300 1.10–1.86×, B200 agentx q7 1.00× / ragged and long rows 1.24–1.32× / uniform hkv8 q7 0.89×; q_len=1 programs unchanged)

##### MiniMax Sparse Attention

- #5402 — NVFP4 paged-KV MSA decode for SM100/SM103 with an explicit layout contract.

- #4355

##### NVFP4 Attention

- #4543
- #5283 
- #5443

##### Sage Attention SM120 INT8

- #4951
- #5083 
- #5127 — cover 25 SM120 Sage parameter combinations and fix stale tensor-map reuse with the grid-constant ABI; 79 GPU tests pass, with lower median GPU latency in all four measured comparisons.


##### VSA Block Sparse Attention

- #4593
- #4804

##### Sage-FP8 Block Sparse Attention SM100/SM103

- #5442 — variable-shape Sage-FP8 block-sparse attention for SM100/SM103 (any batch/head count, GQA, unaligned Sq/Sk, per-row KV counts, rank-1/2/3 block sizes, optional LSE) plus a fused Sage quantizer, wired into `bsa_attn_sm100_blk64_fwd(..., backend="cake")`. Same-node CUPTI cold-L2 vs the CuTe Sage path at B8/H32/S4096 (32 B1/H8 calls, kernel-sum), 10% / 50% / 90% density: B200 **2.89× / 1.56× / 1.34×** (858 TFLOPS at 50%), B300 **3.03× / 1.64× / 1.39×** (968 TFLOPS); fused quantizer **19.5× / 19.0×** vs the torch recipe with bit-exact scales. 12/12 tests pass on both architectures; compute-sanitizer synccheck + memcheck clean.

##### Dense Self-Attention (MiniMax-H3)

- #5472 — dense BF16 self-attention for SM120 with a Cake kernel route.

##### Packed-Varlen Attention (MiniMax-H3)

- #5539 — SM120a (RTX 5090 / RTX PRO 6000 Blackwell, GB202) FP8 E4M3 non-causal packed-varlen self-attention (`[T, 56, 128]` BF16 THD + int32 `cu_seqlens`, FP32 softmax; per-token Q / per-128-key-block segment-centred K / 2^8-biased P / per-(segment, channel) V scales, `mma.sync kind::f8f6f4` ping-pong persistent kernel, four launches per call), from #4532 (candidate 5090-K2); FP32-oracle correct (atol = rtol = 0.1) on every packed boundary / tail / empty-segment row, all 9 representative shapes (T = 33472–109952, tails, trailing padding) faster than the fastest FlashInfer BF16 ragged route on both boards: PRO 6000 1.82–1.87× (attention at ~84 % of the FP8 tensor-pipe ceiling), RTX 5090 1.93–1.97×; 0.7–2.3 GiB peak extra memory vs 2.1–5.7 GiB for the BF16 routes.
- #5545 — SM120a (RTX 5090 / RTX PRO 6000 Blackwell, GB202) **experimental NVFP4-QK / FP8-PV** non-causal packed-varlen self-attention (`[T, 56, 128]` BF16 THD + int32 `cu_seqlens`, FP32 softmax; E2M1 Q / K with UE4M3 per-16-channel block scales after segment-mean centring, a fixed orthonormal signed-Hadamard rotation and per-token / per-128-key-block prescale, `mma.sync m16n8k64 kind::mxf4nvf4.block_scale` for QK^T; 2^8-biased E4M3 P and per-(segment, channel) E4M3 V^T through `mma.sync m16n8k32 kind::f8f6f4`; same four-launch ping-pong persistent operator and host plan as #5539), from #4532 (candidate 5090-K2, NVFP4 variant); FP32-oracle correct at the FP4 block-scaled tolerance (atol 1.0 / rtol 0.1; relative L2 0.135–0.143 vs 0.05 for the FP8 operator — the measured E2M1 error budget, left to the requester's disposition) on every packed boundary / tail / empty-segment row; all 9 representative shapes (T = 33472–109952, tails, trailing padding) faster than the FP8 operator on both boards — PRO 6000 1.255–1.286× (attention at ~84 % of the mixed FP4/FP8 tensor-pipe ceiling), RTX 5090 1.446–1.48× — and 2.29–2.90× faster than the fastest FlashInfer BF16 ragged route; 0.5–1.7 GiB peak extra memory (E2M1 codes + scales are 9/16 of the FP8 operand bytes).

- #5530 — split partial-wave work over K/V and combine partial outputs for the BF16/NVFP4 packed-varlen attention families on SM100/SM103; follows #5499.

- #5499

#### MLA

##### K Concatenation

- #4860 

##### Decode

- #4557 — generated TRT-LLM MLA decode backend for SM100 and SM103 (B200 148 SMs + GB300 152 SMs, dual-target catalog): 15-stage unified pipeline with Split-KV reduction, paged-KV BF16/FP8, longest-first persistent CLC work order. GB300 (same-process vs live TRT-LLM Gen, cold-L2 paired CUPTI): 32/32 correctness rows, **60/60** floors, geomean **1.220390×**, weakest block 1.005947×. B200: 32/32 correctness rows, **60/60** floors across 20 rows, geomean of row medians **1.193288×**, weakest block 1.018258×; CLC rows 1.04–1.39× (007781 1.389466×, 007790 1.322585×), FP8 page-64 **1.042276×** (batch 16 × 4096 tokens; store-path-bound partial-O epilogue rewritten as SMEM-staged full-sector stores). Follow-up #5547 (package regenerated from Cake main with a per-V-stage `o_done` handshake in the FP8 page-64 producer): B200 **60/60**, geomean **1.192307×**, FP8 page-64 **1.063356×** (18.673 µs vs 19.872 µs live); GB300 **60/60**, geomean **1.228218×**, FP8 page-64 **1.110487×** (17.056 µs vs 18.944 µs live); FULL32 32/32, unit tests 18/18, screens/CLC/FORMAL/generic+sanitizers all green on both targets.
- #5547 

##### Sparse MLA DSV4

- #4573 — All94 direct semantic/shape cases pass strict correctness, zero fallback and baseline/CAKE speedup above1: **1.736584 → 1.500323 ms (1.157473424×)**, minimum **1.012062499×**. Public correctness tests passed100/100; separate synccheck/racecheck passed. Direct benchmark/helper/physical durations: **55.183819 / 64.835800 / 76.874102 s**.
- Fresh real SGLang DeepSeek-V4-Flash TP4 A: **130570.767202148 → 120242.376625977 ms (1.085896427×)**. Counterbalanced B: **126203.928368164 → 125388.164241211 ms (1.006505910×)**. The canonical pair passes. Each repeat has **512 exact output tokens across eight requests**, **24 exact ordered route records per side**, **eight traces** and **zero fallback**.
- A measured/physical duration: **3179.785394688 / 3231.103028100 s**; B: **3072.548526656 / 3132.407019200 s**. Combined measured runtime is **6252.333921344 s** and physical span is **6524.988085600 s**. These elapsed durations are distinct from GPU active milliseconds.

#### Fused Pre-Attention (MiniMax-H3)

- #5516 — pipeline the NVFP4 Q/K normalization, RoPE and pack stage on SM100a/SM103a; byte-identical follow-up to #5496.
- #5529 — fuse NVFP4 QKV GEMM with Q/K RMSNorm, RoPE and destination-major NVFP4 packing on SM100a/SM103a; follows the segmented route in #5496 / #5516.

- #4690 
- #5060 — MXFP8 pre-attention for SM100a (B200) and SM103a (B300), from #4532 (candidate 2A)
- #5137 — add SM100a (B200) support to MiniMax-H3 BF16 pre-attention, preserving SM103a support
- #5496
- #5493 — SM120a (RTX 5090 / RTX PRO 6000 Blackwell, GB202) FP8 and NVFP4 fused pre-attention (RMSNorm + indexed AdaLN + activation quantization → `mma.sync` QKV GEMM 5376→21504 → Q/K RMSNorm + 3-D RoPE, BF16 / E4M3 / NVFP4 outputs), from #4532 (candidate 5090-K1); all 6 representative M (33472–109952) faster than the segmented chain on both boards: FP8 3.06–3.11× (PRO 6000) / 2.17–2.26× (5090), NVFP4 3.89–3.94× / 3.52–3.69×; fused peak memory 2.1–9.6 GiB vs baselines that OOM at M=109952 on the 32 GB 5090

#### QKV Quantize-and-Pack (MiniMax-H3)

- #5527 — one-pass QKV quantize-and-pack helpers for SM100a (B200) and SM103a (B300 / GB300), from #4532 (candidate 7): BF16 Q/K/V `[M, 56, 128]` (three tensors or the kind slices of one fused projection output, read in place) → destination-major `[P, M, 56/P, 3, 128]` Ulysses send buffers for P = 1/2/4/8, quantized per destination in one HBM pass to NVFP4 (E2M1 + swizzled E4M3 block-16 scales, the #5496 layout) or MXFP8 (E4M3 + swizzled UE8M0 block-32 scales, the #5060 layout), byte-exact with the segmented `fp4_quantize` / `mxfp8_quantize` path incl. zeroed scale-tile padding; all 48 representative rows (P × T ∈ {33472 … 109952}) faster than the segmented chain on B200, B300 and GB300: NVFP4 10.5–11.3×, MXFP8 15.2–17.2×, streaming at 5.5–7.3 TB/s (the byte-matched `torch.add` ceiling of each GPU).

#### Fused Output Projection (MiniMax-H3)

- #5525 — direct-layout output projection plus indexed gate and residual on SM100/SM103, with BF16, MXFP8 and NVFP4 variants.

- #5524 — SM120a (RTX 5090 / RTX PRO 6000 Blackwell, GB202) FP8 and NVFP4 fused attention output projection (in-kernel per-token FP8 / block-16 NVFP4 activation quantization → `mma.sync` GEMM 7168→5376 → indexed gate × output + residual, BF16 out), from #4532 (candidate 5090-K3); all 6 representative M (33472–109952) faster than the segmented chain on both boards: FP8 3.11–3.13× (PRO 6000) / 1.99–2.00× (5090), NVFP4 1.88–1.90× / 1.57–1.61×; fused peak memory 1.3–5.4 GiB, no memory-limited shape on either board

### Linear Attention & State Space

#### Recurrent KDA

##### Prefill

- #5440 — regenerate BF16 KDA modules with tile-anchored unbounded-gate decay.
- #5452 — prepared prefill plan cache, FP32 intermediate states, and a sequential route for unbounded FP32-state prefill.

- #4262
- #4313
- #4351
- #4675
- #4728 
- #4845  2.82x vs flashkda
- #5278 — TF32 KDA prefill kernels and prepared inference API for SM103a, with FP32 recurrent state and BF16 checkpoints.
- #5363 
- #5370 

##### Decode

- #4279
- #4314
- #4562
- #4967 — fused KDA decode backend for B200 and B300, with FP32/BF16 recurrent state

##### Prefill and decode

- #4445
- #4535
- #4571

##### Historical Training

- #4636 — paired recurrent training for SM100a/SM103a; historical implementation subsequently removed in #4965. See #4642 for training work.
- #4726 — recurrent training template dispatch; historical implementation subsequently removed in #4965. See #4642 for training work.

#### Gated Delta Rule

##### Context-parallel prefill

- #5320 — merged opt-in SM100/SM103 context-parallel prefill backend, from #4078.

##### General Updates

- #4572 — honor intermediate cache step strides
- #4745 

##### Source-only Blackwell backend

- #4581 — source-only generated backend for SM100 and SM103
- #5243 — optimize SM100/SM103 prefill kernels; B200 B4/S2048 repeats **0.0748635 / 0.0748000 ms**, with **137/137** qualified performance rows on each architecture. Default prefill dispatch remains CuTe.
- #5378 — Qwen3.5 TP2 seven-token BF16 verify decode rows for SM100/SM103 (H=8/HV=16, B=1..8, T=7 and T=8, strided and contiguous inputs); public API on B200 under CUDA-graph replay B1/T7 **0.007520 / 0.009440 ms (1.255×)** vs CuTe, B2 **1.24×**, B4 **1.21–1.23×**, B8 **1.09–1.10×**, B1/T8 **1.26–1.28×**; all rows match the FP32 oracle with bit-exact state pools. SGLang integration: [sgl-project/sglang#40656](https://github.com/sgl-project/sglang/pull/40656) (draft).

#### Mamba

##### SSDCombined

- #4576

##### Selective State Update

- #4616

### GEMM / BMM

#### BF16 x FP4 GEMM

- #5138 — generated BF16 x FP4 GEMM kernels for SM100a and SM103a

#### Blackwell all-gather matmul

- #4722 — opt-in generated backend for SM100 and SM103, world sizes 2 and 4

#### NVFP4 SVDQuant GEMM

- #5076 — opt-in generated NVFP4 SVDQuant GEMM backend for SM100 and SM103.

#### BF16 BMM

- #4370 — opt-in generated backend for SM100a and SM103a

#### DeepGEMM

- #5523 — generated Blackwell DeepGEMM-family package for SM100a and SM103a (sparse MXFP4/MXFP8 MQA indexer, fused routing gate, fused mHC, source and v3 mixture-of-experts pipelines, FP8 1D1D / mixed FP8xFP4 / native FP4 / FP4 K-grouped / FP8 batched GEMM); one producer tree for both architectures (the mixed FP8xFP4 SM100a section from that tree plus the harness commit admitting the specialized schedules on SM100), exports validated on B200 and GB300, source schedules faster than native DeepGEMM on 112/118 (GB300) and 103/118 (B200) model rows; replaces #4564

#### TinyGEMM2

- #4423 — add a STAGES=16 generated kernel tier for single-wave large-K shapes.
- #4849 — enable generated tinygemm2_sm100 variants on SM107 (Rubin).

- #4274

#### Blackwell Router GEMM

- #4594

#### Grouped FP8 GEMM

- #5500 — prepared contiguous grouped FP8 GEMM program family for SM100a.

#### Fused FC1 + SwiGLU (MiniMax-H3)

- #5491 — fused RMSNorm + indexed AdaLN + FC1 + SwiGLU for SM100a (B200) and SM103a (B300) in BF16, MXFP8 and NVFP4 W4A4, from #4532 (candidate 5); all 47 representative shapes faster than the segmented FlashInfer chain on both arches (BF16 up to 1.25×, MXFP8 up to 2.01×, NVFP4 up to 2.28×)
- #5506 — 256-column quantized GEMM tiles and 128-byte-row block-scale TMA for the #5491 MiniMax-H3 fused FC1 + SwiGLU on SM100a (B200) and SM103a (B300); the complete fused NVFP4 operator is now faster than FlashInfer's bare `mm_fp4` on all 47 representative shapes (B200 1.02–1.25×, was 0.81–0.96× at the production centers; B300 1.10–1.64×, was 0.87–0.96× at P=8), MXFP8 1.06–1.60× (B200) / 1.07–1.59× (B300) vs bare `mm_mxfp8`; 1.22–1.32× / 1.08–1.31× over the #5491 NVFP4 operator
- #5513 — 256x448 CTA-pair GEMM tile (two N=224 `cta_group::2` MMAs per K-set, alternating TMEM scale windows, packed BF16 drain) for the #5506 MiniMax-H3 fused FC1 + SwiGLU NVFP4 kernel on SM100a (B200) and SM103a (B300): bit-exact, GEMM kernel 1.020–1.043× (B200) / 1.021–1.027× (B300) over #5506; fused NVFP4 operator vs bare `mm_fp4` 1.05–1.29× (B200, geomean 1.13) / 1.12–1.79× (B300, geomean 1.53) on all 47 representative shapes; NVFP4 weight-scale layout moves to 128 combined 224-row sub-tiles (`prepare_fc1_weight_nvfp4`)
- #5521 — SM120a (RTX 5090 / RTX PRO 6000 Blackwell, GB202) fused RMSNorm + indexed AdaLN + FP8 / NVFP4 FC1 (5376→28672) + SwiGLU with `mma.sync` (`kind::f8f6f4` / `kind::mxf4nvf4.block_scale`), from #4532 (candidate 5090-K4); all 6 representative M (33472–109952) faster than the segmented `mm_fp4` / `bmm_fp8` chain on both boards: NVFP4 1.52–1.53× (PRO 6000, 1339–1348 TFLOPS) / 1.45–1.49× (5090), FP8 2.68–2.71× / 1.57–1.59×; fused peak memory 1.8–5.2 GiB vs 3.9–12.1 GiB for the chain

### MoE & Routing

#### Fused MoE

- #5183 — TP8-local Kimi-K3 NVFP4 SiTU experts for SM100/SM103; all 52 B200/B300 correctness and export qualification rows pass, with complete latency and duration tables.

#### AlphaMoE

- #4287
- #4339
- #4340

#### MegaMoE

- #5359 — runtime-batch and fixed-tile policies for the experimental MXFP8 EP16 backend.
- #5480 — experimental fused W4A8 MegaMoE EP16 backend on GB300.

- #4810
- #5126
- #4819 
- #5431
- #5509
- #4970 
- #5148 
- #5433 

#### BGMV MoE

- #4821 — prepared Blackwell backend for SM100

#### DeepSeek Fused Routing

- #4587 — current Cake/FlashInfer: B200 1.0194–1.2101x and GB300 1.2665–1.5738x (15/15 each)

#### Kimi-K3 Fused Router

- #5531 — one-launch Kimi-K3 fused MoE router (896 experts, top-16 on `sigmoid + bias`, renormalized unbiased weights, expert-aligned route plan for `block_m` 8/16) for SM100a (B200) and SM103a (GB300); 44 tests per arch, export 28/28 rows bitwise source/export on both; vs SGLang `route_radix` + `moe_align_block_size` (CUPTI, cold L2): B200 GM **1.416×** (min 1.136, 28/28 > 1), GB300 GM **1.753×** (min 1.234, 28/28 > 1); round 7 re-export (Q4S arm: `min_blocks=4` cluster build at M512–M2048, lane-parallel M emit) lifted the B200 mid rows M256–M2048 from 1.00–1.19× to 1.14–1.31×.
- #5548 — follow-up to #5531: the M (M256) and Q4S (M512–M2048) programs drop the redundant per-thread `__threadfence()` in front of the cooperative grid join (the join is already a gpu-scope release/acquire); bit-identical route plans, 44 tests per arch, export 28/28 rows bitwise source/export on both; vs the #5531 programs on the same nodes (paired cold-L2 CUPTI) M256 +3 %, M512 +5–7 %, M1024 +5 %, M2048 +3–4 % on B200 and GB300, other rows unchanged; vs SGLang `route_radix` + `moe_align_block_size`: B200 GM **1.447×** (min 1.211, 28/28 > 1), GB300 GM **1.837×** (min 1.287, 28/28 > 1).

#### Warp Decode

- #5134 — extend NVFP4 warp-decode to seven public MoE configurations on SM100 and SM103, T1–32
- #4855 
- #5036 

### Activation & Quantization

#### MXFP8 Quantization

- #4820 — opt-in generated backend for grouped MXFP8 quantization on SM100 and SM103

#### Fused SwiGLU / MXFP8 Quantization

- #4638 — fused Blackwell SwiGLU MXFP8 quantization, forward and backward; also tracked in #4642.

#### Softmax

- #4282

### Sampling

- #5439 — fused radix top-k → sparse top-p → sampling pipeline (`flashinfer.cake_sampling`) for compute capability 9.0+: one generated source JIT-compiled per capability (SM90a/100a/103a/107a/110a), measured on B200 and B300 (Hopper/Rubin are compile targets so far). Exact, deterministic `top_k_first` semantics (ties by ascending index, 64-bit fixed-point top-p, bitwise replay across stream launch / CUDA graph / every kernel variant), no size-based fallback (streaming stage 1 for large batch × vocab). B200 CUPTI kernel time vs `top_k_first` (k=50, p=0.9): **3.0–3.9×** at vocab 128256/151936/262144 for batch ≤ 32, **2.3–3.2×** at batch 64, **1.7–2.4×** at batch 128; B300 **2.5–4.8×**; k=1000 at batch 64/128 **2.7–3.9×**. 35 pipeline tests + 207 replayed upstream sampling unit tests pass on B200 (35 on B300); compute-sanitizer synccheck/memcheck/racecheck clean. Remaining exception: vocab 32768 with k=1000 at batch ≤ 2 is slower than the `joint` rejection sampler under stream launch (0.68×), faster under CUDA-graph replay.
- #5482

### Cross-family Support

#### Architecture Support

- #5467 — SM107 enablement for Cake DSv3 routing, BGMV MoE, concat-MLA-K, VSA, FlashKDA decode, GDN, and packed KDA.









## 评论 (6)

### Kim2026-dev · 2026-08-14

# CAKE kernel candidates for MiniMax-H3 on B300 and RTX 5090

Thank you for inviting customized kernel challenges in the CAKE tracker. We have
a MiniMax-H3 FL2VA runtime based on Sol Engine and SGLang and would like to ask
whether any of the standalone kernels below would be useful CAKE challenges.

These are independent candidates rather than a request for the CAKE team to
implement all of them. We will take care of Sol Engine/SGLang integration,
collectives, quantized checkpoints, calibration, end-to-end validation, and
deployment.

The two targets are:

- NVIDIA B300 / SM103a, with Ulysses SP1/SP2/SP4/SP8;
- NVIDIA RTX 5090 / SM120, quantized execution and SP1 only.

## B300 / SM103a candidates

Common H3 dimensions:

- hidden size: 5,376
- heads: 56
- head dimension: 128
- attention inner dimension: 7,168
- FFN dimension: 14,336
- supported Ulysses degree `P`: 1, 2, 4, or 8
- heads per rank after all-to-all: `56 / P` = 56, 28, 14, or 7
- non-causal packed-varlen attention
- batch size: 1

For B300, we are interested in separate shape specializations for SP1, SP2,
SP4, and SP8.

Nominal `M` values for our main 768p duration buckets are:

| Duration | Global packed rows `T` | SP1 `M` | SP2 `M` | SP4 `M` | SP8 `M` |
|---:|---:|---:|---:|---:|---:|
| 4 s | 33,472 | 33,472 | 16,736 | 8,368 | 4,184 |
| 5 s | 38,592 | 38,592 | 19,296 | 9,648 | 4,824 |
| 6 s | 48,768 | 48,768 | 24,384 | 12,192 | 6,096 |
| 8 s | 58,944 | 58,944 | 29,472 | 14,736 | 7,368 |
| 10 s | 74,240 | 74,240 | 37,120 | 18,560 | 9,280 |
| 15 s | 109,952 | 109,952 | 54,976 | 27,488 | 13,744 |

Prompt length makes `M` slightly dynamic, so kernels need tail handling around
these values. We can provide exact tensor traces and a PyTorch reference for each
operator below.

## 1. Fused BF16 pre-attention kernel — highest priority

Reference operation:

```text
x [M, 5376]
  -> RMSNorm
  -> indexed AdaLN scale/shift
  -> BF16 QKV GEMM [M, 5376] x [5376, 21504]
  -> Q/K RMSNorm over D=128
  -> 3-D RoPE on Q/K
  -> destination-major BF16 QKV
       [P, M, 56/P, 3, 128]
```

The output is only a send buffer; NCCL all-to-all is outside the kernel. The goal
is to avoid writing normalized x, modulated x, ordinary QKV, normalized Q/K, and
RoPE Q/K to HBM. `P` may be implemented as four compile-time specializations
instead of one dynamic kernel if that produces better code.

## 2. Fused low-precision pre-attention kernels

Same operation and output layout as kernel 1, with two independent variants:

```text
A. MXFP8/FP8 QKV GEMM
   -> BF16 Q/K RMSNorm + RoPE
   -> destination-major E4M3 QKV + scales

B. NVFP4 W4A4 QKV GEMM
   -> BF16 Q/K RMSNorm + RoPE
   -> destination-major NVFP4 QKV + block scales
```

An additional NVFP4-GEMM-to-E4M3-output variant is useful if the matching NVFP4
attention kernel is not accurate enough.

We will provide prepacked weights and scale tensors. The kernel does not need to
create or calibrate quantized weights.

## 3. Packed-varlen FlashAttention-4 kernels

Input after our existing Ulysses all-to-all:

```text
Q/K/V: [T, 56/P, 128]
cu_seqlens: int32
causal: false
output: BF16 [T, 56/P, 128]
```

Nominal `T` centers are 33,472, 38,592, 48,768, 58,944, 74,240, and
109,952. Requested standalone variants:

```text
A. BF16 FA4
B. E4M3 FP8 FA4 with explicit descales
C. experimental block-scaled NVFP4 FA4
```

For C, we would be interested in a genuine low-precision Tensor Core implementation
rather than NVFP4 storage followed by BF16 matmuls. Softmax remains FP32. It would
be helpful to report the actual QK and PV MMA dtypes separately; a hybrid
NVFP4-QK / FP8-or-BF16-PV candidate would also be useful.

## 4. Direct-layout attention output projection

Reference operation:

```text
inverse-Ulysses receive layout [P, M, 56/P, 128]
  -> read without a standalone unpack/transpose
  -> O GEMM [M, 7168] x [7168, 5376]
  -> indexed gate * output + residual
  -> BF16 [M, 5376]
```

Requested GEMM variants: BF16, MXFP8/FP8, and NVFP4 W4A4. The collective itself
is outside the kernel.

## 5. Fused RMSNorm + AdaLN + FC1 + SwiGLU

Reference operation:

```text
x [M, 5376]
  -> RMSNorm
  -> indexed AdaLN scale/shift
  -> FC1 [M, 5376] x [5376, 28672]
  -> split gate/up
  -> SiLU(gate) * up
  -> BF16 [M, 14336]
```

Requested GEMM variants: BF16, MXFP8/FP8, and NVFP4 W4A4.

## 6. Persistent full MLP candidate

Reference operation:

```text
RMSNorm + indexed AdaLN
  -> FC1 [M, 5376] x [5376, 28672]
  -> SwiGLU
  -> FC2 [M, 14336] x [14336, 5376]
  -> indexed gate * output + residual
  -> BF16 [M, 5376]
```

Requested variants: BF16, MXFP8/FP8, and NVFP4 W4A4. This is only worth keeping
if it beats kernel 5 plus a tuned standalone FC2 GEMM; CAKE does not need to solve
that scheduling decision outside the kernel benchmark.

## 7. Quantize-and-pack helper kernels

These are useful fallbacks when the GEMM epilogue cannot write the communication
layout directly:

```text
BF16 Q/K/V [M, 56, 128]
  -> destination-major E4M3 + scales [P, M, 56/P, 3, 128]

BF16 Q/K/V [M, 56, 128]
  -> destination-major NVFP4 + block scales [P, M, 56/P, 3, 128]
```

Quantization and relayout should happen in one HBM pass.

## RTX 5090 / SM120 quantized SP1 candidates

If CAKE currently supports SM120, we would also appreciate considering a smaller
set of single-GPU kernels for the quantized H3 FL2VA path on RTX 5090. This target
uses SP1 only, so there is no Ulysses layout or collective in these kernels.

For SP1, `M = T`; the nominal M values are 33,472, 38,592, 48,768, 58,944,
74,240, and 109,952 for 4/5/6/8/10/15 seconds. We are interested in two quantized
GEMM formats:

- W8A8 E4M3 FP8;
- NVIDIA-compatible block-scaled NVFP4 W4A4.

BF16 is used as the numerical reference but does not need a separately tuned 5090
kernel in this request.

### 5090-K1. Quantized fused pre-attention

```text
x [M, 5376]
  -> RMSNorm + indexed AdaLN
  -> FP8 or NVFP4 QKV GEMM [M, 5376] x [5376, 21504]
  -> BF16 Q/K RMSNorm + 3-D RoPE
  -> Q/K/V [M, 56, 128]
```

Useful output variants would be BF16, E4M3 plus scales, and NVFP4 plus block
scales, so that we can connect the best one to the corresponding attention path.

### 5090-K2. Quantized packed-varlen FA4

```text
Q/K/V [T, 56, 128]
cu_seqlens: int32
causal: false
output: BF16 [T, 56, 128]
```

The requested candidates are E4M3 FP8 FA4 and experimental block-scaled NVFP4
FA4. Softmax should remain FP32. For the NVFP4 candidate, it would be helpful to
report the QK and PV MMA dtypes separately and include a hybrid NVFP4-QK /
FP8-or-BF16-PV result if it is more accurate or faster.

### 5090-K3. Quantized attention output projection

```text
attention output [M, 7168]
  -> FP8 or NVFP4 O GEMM [M, 7168] x [7168, 5376]
  -> indexed gate * output + residual
  -> BF16 [M, 5376]
```

### 5090-K4. Quantized FC1 + SwiGLU

```text
x [M, 5376]
  -> RMSNorm + indexed AdaLN
  -> FP8 or NVFP4 FC1 [M, 5376] x [5376, 28672]
  -> SwiGLU
  -> BF16 [M, 14336]
```

### 5090-K5. Quantized persistent full MLP candidate

```text
RMSNorm + indexed AdaLN
  -> FP8 or NVFP4 FC1
  -> SwiGLU
  -> FP8 or NVFP4 FC2 [M, 14336] x [14336, 5376]
  -> indexed gate * output + residual
  -> BF16 [M, 5376]
```

As with the B300 candidates, this full MLP would only be useful if it outperforms
the fused FC1 + SwiGLU kernel followed by a tuned standalone FC2 kernel. We will
provide prepacked quantized weights and scales; weight conversion and calibration
are not part of the kernel request.

For RTX 5090, our preferred starting point would be **5090-K4 NVFP4 FC1 +
SwiGLU**, followed by 5090-K1 and the FP8/NVFP4 attention candidates.

## Integration

For any selected candidate, a FlashInfer-compatible kernel implementation and
basic benchmark results would be very helpful. We will handle the Sol
Engine/SGLang integration and end-to-end evaluation.


### robin-fain · 2026-08-16

# Kimi K3 TP12 kernels for saturated decode on GB300 NVL72

Hi CAKE team — we are testing TP12 as a Kimi K3 decode configuration on a
GB300 NVL72 rack. Before filing separate kernel issues, we would like to check
whether the uncovered shapes below fit the kind of problems CAKE wants to take
on.

The target is the high-throughput decode regime: we increase decode batch size
until the GB300 reaches its throughput saturation region. The relevant `B` is
therefore empirical and depends on the complete runtime, sequence lengths, and
memory footprint; it is not fixed in this request. The relevant operating range
is the part of the batch sweep where aggregate decode throughput approaches its
plateau.

## GB300 platform topology

![GB300 compute-tray connectivity](https://docs.nvidia.com/enterprise-reference-architectures/nvl72-ai-factory/latest/_images/nvl72-ai-factory-03.png)

Source: [NVIDIA GB300 NVL Compute Tray](https://docs.nvidia.com/enterprise-reference-architectures/nvl72-ai-factory/latest/components.html#nvidia-gb300-nvl-compute-tray)

## Why TP12 exposes different shapes

Relevant Kimi K3 dimensions are:

```text
layers                         93
KDA / Gated-MLA layers         69 / 24
hidden size                    7168
KDA heads                      96
KDA head dimension             128
KDA convolution width          4
TP degree                      12
local KDA heads                8
routed latent width            3584
experts / selected experts     896 / 16
```

Our reading of the current public work is summarized below. Please correct us
if any of these shapes are already covered on SM103a.

| Area | Public coverage we found | Shape left by TP12 |
|---|---|---|
| Full fused KDA decode | local heads 12/24/32/48/96 | `H=8, D=128` |
| Packed CAKE KDA (#4378) | `T=1, H=12, D=128`, post-convolution | `H=8`; throughput-scale batches |
| AlphaMoE router (#4339) | up to 512 experts, softmax-style routing | 896 experts with K3 sigmoid routing |
| K3 LatentMoE fused tail | TP8 and TP16 | TP12 |

## Shape A: full KDA decode with eight local heads

This is the main candidate. K3 runs this operation in 69 layers, so it remains
important even when the GPU is driven by a large active batch.

The operation boundary we use is:

```text
packed projected input       BF16 [B, 3072]       # 3 * H * D
convolution state            BF16 [slots, 3072, 3]
recurrent state              BF16 [slots, 8, 128, 128]
state index                  INT32 [B]
raw output gate              BF16 [B, 8, 128]

width-4 causal convolution
  -> SiLU
  -> recurrent KDA update
  -> output gate + RMSNorm
  -> BF16 [1, B, 8, 128]
```

The point we would benchmark most heavily is `H=8, D=128, T=1` across the batch
sweep where aggregate decode throughput approaches saturation on SM103a.
Indexed states, changing batch size, and CUDA Graph execution are part of the
serving path. We are happy to adapt our integration to whichever ABI is most
natural for CAKE or FlashInfer.

## Shape B: K3 routing in the throughput-saturated decode regime

This is a smaller, independent candidate. The routing rule differs from the
currently published AlphaMoE router:

```text
logits                      FP32 [M, 896]
expert correction bias      FP32 [896]
selected experts            16

scores = sigmoid(logits)
ids = topk(scores + correction_bias, 16)
weights = gather(scores, ids)
weights = weights / reduce_sum(weights)

output weights              FP32 [M, 16]
output ids                  INT32 [M, 16]
```

The bias participates in selection but not in the returned weights. `M` follows
the decode batch sweep through the throughput saturation region. We include
this for completeness, but it is behind the KDA shape in priority.

## Optional: TP12 LatentMoE tail

There is also a TP12 gap in the fused LatentMoE tail. For our decode setup,
however, we would first measure whether this remains worthwhile around the
throughput saturation region before asking anyone to spend time on it.

For reference, the mathematical boundary is:

```text
routed_partial              BF16 [M, 3584] per TP rank
shared_partial              BF16 [M, 7168] per TP rank

latent = RMSNorm(AllReduce12(routed_partial))
output = latent @ up_weight.T + AllReduce12(shared_partial)
```

The unusual part of TP12 is that 7168 is not divisible by 12. If
communication-aware multi-GPU kernels are currently of interest to CAKE, this
could be considered separately. Otherwise we will keep it outside the request.

## Links

- packed `T=1, H=12` KDA: <https://github.com/flashinfer-ai/flashinfer/pull/4378>
- AlphaMoE router: <https://github.com/flashinfer-ai/flashinfer/pull/4339>
- Kimi K3 configuration: <https://huggingface.co/moonshotai/Kimi-K3/raw/main/config.json>


### yzh119 · 2026-08-16

Hi @robin-fain would you mind turning the comment into a sub issue?

### robin-fain · 2026-08-16

> Hi [@robin-fain](https://github.com/robin-fain) would you mind turning the comment into a sub issue?

ok

### Zhaojp-Frank · 2026-08-24

Wonderful, I read through the paper and it's cool.
btw, any plan to open source CAKE? @yyihuang @yzh119 

### Ramshankar07 · 2026-09-13

### CAKE warp-decode geometry request: DeepSeek-V4-Flash (and two FP8 siblings)

Thank you for the open invitation on this tracker. We run a small programme that benchmarks
decode-path kernels for four specific checkpoints at production batch sizes. NVFP4 warp decode
(#4855, #5036, #5134) lands squarely on the shape we care most about — the MoE top-k gather at
decode — and we would like to ask what it would take to reach a geometry we can actually run.

We are not asking for all of the below. We want to know which, if any, is a reasonable CAKE
challenge, and what you would need from us.

**Our operating point is the one warp decode is built for.** Traced to Patel et al.
(arXiv:2311.18677): decode batch is **≤20 tokens/iteration for 60–70%** of conversational
serving and a **single token for >20%** of coding traffic, with median outputs of 13 and 129
tokens. `kMaximumTokens = 32` contains that entirely. We have no interest in batch 256.

#### The primary ask: DeepSeek-V4-Flash-0731

| | |
|---|---|
| hidden size `H` | **4096** |
| MoE intermediate `I` | **2048** |
| routed experts `E` | **256** |
| top-k | **6** |
| shared experts | 1 |
| layers | 43, plus 1 MTP layer |
| activation | SwiGLU, `hidden_act: "silu"`, with **`swiglu_limit: 10.0`** |
| routed-expert dtype | **`"expert_dtype": "fp4"`** (top-level config field) |

We lead with this one for two reasons. It is the only one of our three MoE targets whose routed
experts are **already in a 4-bit format**, so it does not require us to produce and validate a
requantised checkpoint first. And you already run this checkpoint — #4573 measures the CAKE
sparse-MLA backend on real SGLang serving DeepSeek-V4-Flash at TP4, so the model is in your
harness and the integration path is one you have exercised.

Two things we cannot resolve from the config and would rather ask than assume:

- The config says `fp4`, not NVFP4. **Is its packing and block-scale layout compatible with the
  shuffled MajorK / R128c4 ABI the warp-decode routes expect**, or is that a conversion step?
  (`quantization_config` in the same file declares `quant_method: fp8`, but that governs
  attention, dense and shared-expert weights — the routed experts are the `expert_dtype` field.)
- `swiglu_limit: 10.0` is a **clamped** SwiGLU. The contract header's `Activation` enum carries
  `kSwiGLU` and `kSiLU`; is a clamp a parameter you can thread through an existing
  activation-qualified route, or is it a third activation?

#### The two FP8 siblings, for context rather than as a request

| model | H | I | E | top-k | shared | routed-expert precision |
|---|---:|---:|---:|---:|---:|---|
| GLM-5.3-Flash | 4096 | 2048 | 288 | 8 | 1 | FP8 E4M3 blockwise 128×128 |
| Qwen3.8-Flash-Next-FP8 | 2560 | 640 | 512 | 10 | 1 | FP8 E4M3 blockwise 128×128 |

Qwen3.8-Flash-Next is interesting because it is the near-miss: it shares the routing shape of
your existing `kH2048I512E512K10` route exactly — 512 experts, top-10 — and differs only in the
tile, H 2048 → 2560 and I 512 → 640. That existing route's four fields match Qwen3-Next-80B-A3B
exactly, i.e. the generation before ours. We note #5134 adds H=2560 at `768 / 384 / top-4`, so
the hidden size is already within reach.

Both would need an NVFP4 checkpoint from us. A third-party conversion exists for GLM
(`RedHatAI/GLM-5.3-Flash-NVFP4`); for Qwen3.8-Flash-Next we would have to make one. So the
question underneath both: **is there any appetite for the output-centric decode path against
FP8 blockwise 128×128 weights, or does that ABI difference make it a different kernel rather
than a new route?** If the answer is "NVFP4 only", that is a useful answer and we will plan
around it.

#### What we would do

We are not asking for integration. We would provide exact shapes and a reference, run
`benchmarks/cake_warp_decode.py --mode correctness` on B200, and benchmark against
`trtllm_fp4_block_scale_routed_moe` at T=1…32 — the same comparator as #5036 — publishing the
result either way, including regressions. Our prior is your own number rather than any blog
claim: **1.090404× geomean (0.928586–1.321875×) over 128 SwiGLU comparisons, with 6
regressions.**

One question on method, since you measure this carefully: for a *new* geometry, is the
`--mode correctness` dense matrix (T=1…32 per activation-qualified geometry) the gate you would
want run before proposing a route, or is there a calibration step ahead of it — something like
the discovery/held-out route-seed procedure #4855 describes for the T23 boundary?

