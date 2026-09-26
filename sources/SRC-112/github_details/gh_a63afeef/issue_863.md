# [Issue #863] Profile test / 性能分析测试

source: https://github.com/SemiAnalysisAI/InferenceX/issues/863
state: open | updated: 2026-07-04T05:11:49Z
labels: 

## 正文

@claude do a profile run with dsr1 fp4 on MI355X with any conc, then help me analyze compute-comms overlap of the resultant trace, and the matrix shapes

## 中文说明
请求对 DeepSeek-R1 FP4 MI355X 进行 profile 运行（任意并发），然后分析生成的 trace 中计算与通信的重叠情况以及矩阵形状。


## 评论 (10)

### Klaud-Cold · 2026-03-04

Claude Code is working… <img src="https://github.com/user-attachments/assets/5ac382c7-e004-429b-8e35-7feb3e8f9c6f" width="14px" height="14px" style="vertical-align: middle; margin-left: 4px;" />

I'll analyze this and get back to you.

[View job run](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22683911875)

### Klaud-Cold · 2026-03-04

**Claude finished @Oseltamivir's task in 22m 6s** —— [View job](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22683911875)

---
### Profile Analysis: DSR1 FP4 MI355X (SGLang, TP4, Conc=64)

- [x] Trigger profile workflow for `dsr1-fp4-mi355x-sglang`
- [x] Wait for profile run to complete — [Run #22690179054](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22690179054) ✅
- [x] Retrieve Perfetto trace link
- [x] Analyze compute-comms overlap
- [x] Analyze matrix shapes

**Perfetto Trace:** [Open in Perfetto](https://semianalysisai.github.io/InferenceX-trace-storage/?src=https%3A%2F%2Fraw.githubusercontent.com%2FSemiAnalysisAI%2FInferenceX-trace-storage%2Fa38de337a90bf15d8669c2acd0c8936670d77399%2Fprofiles%2Ff65d6b4b1e0eb7744b9987ede6b1d11735f6dcf2%2Fmi355x%2Fsglang%2Fdsr1_1k1k_fp4_tp4_ep1_conc64%2Ftrace.json.gz&title=dsr1_1k1k_fp4_tp4_ep1_conc64)

---

### Compute-Comms Overlap Analysis

**Key finding: There is ZERO compute-comms overlap.** All GPU kernels (compute and communication) execute on a **single HIP stream** per TP rank (`[TPxx] stream 7`). Since there is only one stream, all operations are strictly serialized — no GEMM can run concurrently with any `cross_device_reduce` or `rcclGenericKernel`.

The communication primitives used are:
- **`aiter::cross_device_reduce_2stage`** — custom 2-stage allreduce via direct GPU memory access (used for attention output and MoE allreduces)
- **`rcclGenericKernel`** — RCCL collective (used for initial all-gather in decode setup)

#### Decode Step Time Breakdown (single step, 64 tokens)

| Category | Count | Time (ms) | % |
|---|---|---|---|
| MoE Expert GEMM (CK MXFP4) | 116 | 7.41 | 36.9% |
| Dense GEMM (hipBLASLt) | 184 | 3.29 | 16.4% |
| **Communication** | **124** | **2.10** | **10.5%** |
| Other (copy/elem/etc) | 265 | 1.29 | 6.4% |
| MLA Attention (INT8) | 61 | 1.19 | 5.9% |
| MoE Routing/Sorting | 232 | 1.15 | 5.8% |
| RMSNorm + Quant | 245 | 1.07 | 5.3% |
| Attention Misc (rope/cache/reduce) | 123 | 0.79 | 3.9% |
| Batched GEMM (A16W-FP4) | 122 | 0.64 | 3.2% |
| Router GEMM (FP16) | 58 | 0.36 | 1.8% |
| Shared Expert GEMM (FP4) | 6 | 0.26 | 1.3% |
| TopK Selection | 58 | 0.24 | 1.2% |
| Shared Expert Append | 58 | 0.23 | 1.2% |
| Quantization | 6 | 0.04 | 0.2% |
| **TOTAL** | **1658** | **20.06** | **100%** |

**Decode wall-clock: 20.11ms** | GPU utilization: **99.7%** (virtually no idle bubbles between kernels)

#### Communication Pattern Per Layer
Each of the 61 DeepSeek-R1 layers issues **~2 allreduce calls**:
1. **Attention output allreduce** (~13-15μs per `cross_device_reduce`)
2. **MoE/FFN output allreduce** (~13-15μs per `cross_device_reduce`)

In decode, the per-call `cross_device_reduce` is very fast (~12-20μs) since it's only reducing 64 tokens × 7168 hidden dim across 4 ranks. Communication is **10.5% of total** — modest but could still be overlapped with compute for a ~2ms win.

#### Prefill Phase Comparison
The prefill phase tells a different story:
- **GPU utilization: 13.9%** (wall=759ms, active=106ms)
- Comms: 55.5ms (52.5%) — dominated by one large `cross_device_reduce` of ~35ms
- Massive idle gaps due to CPU-side scheduling overhead

---

### Matrix Shapes Analysis

**Config: TP=4, 61 layers (3 dense + 58 MoE), hidden=7168, MLA, 256 experts (8 active/token)**

#### Per-Layer GEMM Operations (Decode, B=64 tokens)

| Operation | Kernel Type | Shape (M × N × K) | Precision | Avg Duration |
|---|---|---|---|---|
| q_a_proj | hipBLASLt (Cijk MT16x64x256) | 64 × 1536 × 7168 | BF16 | ~22μs |
| kv_a_proj | hipBLASLt (Cijk MT32x64x128) | 64 × 576 × 7168 | BF16 | ~11μs |
| kv_b_proj | aiter batched (a16wfp4 M16xN64xK128) | 64 × 256 × 512 | A16W-FP4 | ~5μs |
| MLA Decode Attention | aiter (mla_a8w8_qh16) | 64 heads × 1 × seq_len | INT8 | ~19μs |
| o_proj | aiter batched (a16wfp4 M16xN32xK512) | 64 × 4096 × 512 | A16W-FP4 | ~6μs |
| Router gate | Triton (a16_w16_atomic K256 KSPLIT=14) | 64 × 256 × 7168 | BF16 | ~6μs |
| Shared Expert gate_up | Triton (afp4wfp4 M64xN256xK256) | 64 × 4608 × 7168 | FP4×FP4 | ~54μs |
| Shared Expert down | Triton (afp4wfp4 M64xN256xK256) | 64 × 7168 × 4608 | FP4×FP4 | ~35μs |
| MoE Expert gate_up | CK moe_mxgemm (grouped) | [8×64] × 2048 × 7168 | MXFP4 | ~64μs |
| MoE Expert down | CK moe_mxgemm (grouped) | [8×64] × 7168 × 2048 | MXFP4 | ~55μs |
| Dense FFN gate_up (layers 0-2) | hipBLASLt (Cijk MT32x64x256) | 64 × 4608 × 7168 | BF16 | ~19μs |

#### Key Observations

1. **MoE Expert GEMMs dominate** at 36.9% of decode time. The CK `moe_mxgemm_2lds` kernel processes grouped experts using MXFP4 precision with 2-LDS buffering — each call handles all 8 active experts' tokens simultaneously.

2. **hipBLASLt tile choices** reflect small-M decode shapes:
   - `MT16x64x256` for q_a_proj (N=1536 is small)
   - `MT32x64x128` for kv_a_proj (N=576 even smaller)
   - `MT32x64x256` for dense FFN/gate_up
   - These are all M=64 (batch size), latency-bound GEMM shapes

3. **Shared expert uses Triton FP4×FP4 GEMM** (`afp4wfp4`), while routed experts use **CK MXFP4 GEMM** (`moe_mxgemm`). The shared expert kernels are ~2× slower per-FLOP than CK because Triton's FP4 codegen on MI355X is less optimized than CK's hand-tuned MFMA pipelines.

4. **MLA attention** uses INT8 quantized decode (`mla_a8w8_qh16_qseqlen1_gqaratio16_ps`) — specifically optimized for single-token decode with GQA ratio 16 and query head count 16 per rank.

5. **No multi-stream overlap opportunity is exploited** — adding a second stream for comms could save ~2ms per decode step (10.5% improvement) by overlapping `cross_device_reduce` with independent next-layer compute.

### Oseltamivir · 2026-03-04

@claude do a profile run with dsr1 fp4 on B200 and H200 with any conc, then analyze compute-comms overlap of the resultant trace, and the matrix shapes

### Klaud-Cold · 2026-03-04

**Claude finished @Oseltamivir's task in 31m 45s** —— [View job](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22691854556)

---
### Profile Analysis: DSR1 FP4 B200 vs FP8 H200 (SGLang, Conc=64)

- [x] Trigger profile workflow for `dsr1-fp4-b200-sglang` (TP4 EP4, conc=64) — [Run #22691898054](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22691898054) ✅
- [x] Trigger profile workflow for `dsr1-fp8-h200-sglang` (TP8, conc=64) — [Run #22691898656](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22691898656) ✅
  - **Note:** FP4 is not available for H200 in SGLang configs, used FP8 instead
- [x] Wait for both profile runs to complete
- [x] Retrieve Perfetto trace links
- [x] Analyze compute-comms overlap for B200
- [x] Analyze compute-comms overlap for H200
- [x] Analyze matrix shapes for both

**Perfetto Traces:**
- **B200 FP4 TP4 EP4:** [Open in Perfetto](https://semianalysisai.github.io/InferenceX-trace-storage/?src=https%3A%2F%2Fraw.githubusercontent.com%2FSemiAnalysisAI%2FInferenceX-trace-storage%2Fa83f57a427bf9d45c5c047a60eb7ba1f0625beb5%2Fprofiles%2Ff65d6b4b1e0eb7744b9987ede6b1d11735f6dcf2%2Fb200%2Fsglang%2Fdsr1_1k1k_fp4_tp4_ep4_conc64%2Ftrace.json.gz&title=dsr1_1k1k_fp4_tp4_ep4_conc64)
- **H200 FP8 TP8:** [Open in Perfetto](https://semianalysisai.github.io/InferenceX-trace-storage/?src=https%3A%2F%2Fraw.githubusercontent.com%2FSemiAnalysisAI%2FInferenceX-trace-storage%2F055155ee44cbd90cb8333061b2ac517b8726a73f%2Fprofiles%2Ff65d6b4b1e0eb7744b9987ede6b1d11735f6dcf2%2Fh200%2Fsglang%2Fdsr1_1k1k_fp8_tp8_ep1_conc64%2Ftrace.json.gz&title=dsr1_1k1k_fp8_tp8_ep1_conc64)

---

### Compute-Comms Overlap Analysis

#### B200 FP4 (TP4, EP4) — Decode: 24.5ms wall, 20.1ms kernel time

**Overlap verdict: Near-zero overlap (0.054ms), but multi-stream pipelining for MoE.**

B200 uses **two CUDA streams**: stream 39 (main compute + comms, 1169 kernels) and stream 380 (MoE parallel path, 583 kernels). 467/583 MoE kernels on stream 380 temporally overlap with stream-39 kernels — this is **MoE compute pipelining**, not compute-comm overlap.

All communication (both NCCL and flashinfer allreduce) runs on stream 39, so no comm kernel can overlap with other stream-39 compute. The tiny 0.054ms overlap comes from trivial elementwise kernels on stream 7 coinciding with a large NCCL call.

| Comm Type | Count | Total Time | Avg/call | Notes |
|---|---|---|---|---|
| `flashinfer::allreduce_fusion_kernel_oneshot_lamport` | 121 | 2.60ms | 21.5μs | Fast oneshot via GPU-direct memory; 2 per layer |
| `ncclSymkDevKernel_AllReduce` (SymK) | 2 | 2.09ms | 1.04ms | Bulk allreduce, uses optimized SymK protocol |
| `ncclDevKernel_AllGather` (RING_LL) | 1 | 0.10ms | 100μs | Initial all-gather |
| **Total comms** | **124** | **4.79ms** | — | **23.8% of kernel time** |

#### H200 FP8 (TP8, EP1) — Decode: 282.6ms wall, 258.7ms kernel time

**Overlap verdict: ZERO compute-comm overlap. Single stream, comms dominate at 83%.**

H200 runs everything on a **single CUDA stream** (stream 116, 1717 kernels). All operations are strictly serialized.

| Comm Type | Count | Total Time | Avg/call | Notes |
|---|---|---|---|---|
| `flashinfer::allreduce_fusion_kernel_twoshot_sync` | 121 | 185.78ms | 1,536μs | **Rank-0 asymmetry**: TP00 avg=1,732μs vs TP01 avg=127μs |
| `ncclDevKernel_AllReduce_Sum` (RING_LL) | 2 | 27.27ms | 13.6ms | Using slower RING_LL (not SymK) |
| `ncclDevKernel_AllGather` (RING_LL) | 1 | 0.84ms | — | — |
| **Total comms** | **124** | **213.89ms** | — | **82.7% of kernel time** |

**Critical finding**: The flashinfer twoshot allreduce shows extreme **rank-0 coordinator asymmetry** — rank 0 spends 1,536μs avg per call vs 127μs on rank 1. This suggests rank 0 is bottlenecked waiting for synchronization barriers in the two-phase protocol across 8 GPUs. The first allreduce call takes 26.4ms (cold start / barrier contention).

#### Head-to-Head: Why B200 decode is 11.5x faster

| Metric | B200 FP4 TP4 EP4 | H200 FP8 TP8 EP1 |
|---|---|---|
| Decode wall time | **24.5ms** | 282.6ms |
| Compute time | 15.3ms | 44.8ms |
| Comm time | 4.8ms | 213.9ms |
| Comm % | 23.8% | **82.7%** |
| GPU utilization | 82.0% | 91.5% |
| Allreduce protocol | oneshot lamport | twoshot sync |
| NCCL variant | SymK (fast) | RING_LL (slow) |
| Streams | 2 (MoE pipelining) | 1 (fully serial) |
| Ranks in allreduce | 4 (TP4) | 8 (TP8) |

The B200 advantage comes from: (1) EP4 cuts allreduce payload by 4x and reduces ranks, (2) oneshot lamport is ~72x faster than twoshot sync per call, (3) SymK NCCL is much faster than RING_LL, (4) Blackwell SM100 FP4 compute is faster than Hopper SM90 FP8.

---

### Matrix Shapes Analysis

**Config: DeepSeek-R1 — 61 layers (3 dense + 58 MoE), hidden=7168, MLA (qk_head=576, v_head=512), 256 experts (8 active/token)**

#### B200 FP4 TP4 EP4 — Decode GEMM Operations (B=64 tokens)

| Operation | Kernel | Count | Total (ms) | Avg (μs) | Grid | Notes |
|---|---|---|---|---|---|---|
| MoE gate_up (E2M1) | `bmm_E2m1_E2m1E2m1_Fp32` | 58 | 4.78 | 82.4 | [32,120,1] | MXFP4 batched; 120 expert groups; dominates at 23.8% |
| MoE down_proj (E2M1→BF16) | `bmm_Bfloat16_E2m1E2m1_Fp32` | 58 | 2.84 | 49.0 | [56,120,1] | MXFP4→BF16 output; 14.2% |
| Dense proj (CUTLASS FP4) | `DeviceGemmFp4GemmSm100` | 183 | 1.54 | 8.4 | [2,56,1] | q/kv_a_proj, o_proj; flashinfer FP4 GEMM |
| Attention proj (NVJet splitK) | `nvjet_tst_64x32_64x16_2x1_2cta` | 61 | 0.54 | 8.9 | [136,1,1] | SplitK for small-M decode shapes |
| Attention proj (NVJet) | `nvjet_tst_48x64_64x15_4x1` | 61 | 0.39 | 6.4 | [128,1,1] | kv_b_proj or similar |
| MoE finalize | `finalizeKernelVecLoad` | 58 | 0.42 | 7.3 | [64,1,1] | Weighted sum of expert outputs |
| Attn v_proj (NVJet) | `nvjet_tst_128x64_64x8_4x1` | 61 | 0.25 | 4.1 | [128,1,1] | — |
| Shared expert (NVJet) | `nvjet_tst_64x32_64x16_2x2_2cta_h` | 58 | 0.30 | 5.2 | [32,1,1] | On MoE stream (380) |
| MLA Attention | `fmhaSm100f...QkvE4m3...Sm100` | 61 | 1.15 | 18.9 | [1,2,64] | SM100 fused MHA, E4M3 quant, 2 CTA groups |
| FP4 Quantization | `cvt_fp16_to_fp4` | 183 | 0.39 | 2.1 | — | BF16→FP4 conversion for weight format |

**Key B200 observations:**
- MoE expert GEMMs use **cuBLAS batched MXFP4** (`bmm_E2m1`) on SM100 with 120 expert groups — this is the batch dimension (8 active experts × some grouping). Grid `[32,120,1]` suggests 32 tile-blocks across M/N, 120 expert batches.
- The **MoE stream (380)** runs routing + expert GEMM + finalize in parallel with the main stream's attention and dense projections — effective MoE pipelining.
- Dense projections use **flashinfer's CUTLASS FP4 GEMM** (`DeviceGemmFp4GemmSm100`) for activation×weight matmuls.
- MLA uses SM100's native `fmhaSm100f` kernel with **E4M3 quantized KV** and 512-dim V heads.

#### H200 FP8 TP8 EP1 — Decode GEMM Operations (B=64 tokens)

| Operation | Kernel | Count | Total (ms) | Avg (μs) | Grid | Notes |
|---|---|---|---|---|---|---|
| MoE Expert GEMM | `fused_moe_kernel` (Triton) | 116 | 30.04 | 259.0 | [1576,1,1] | Triton fused MoE; 2 per MoE layer; dominates compute at 11.6% |
| Dense gate_up_proj | `deep_gemm::sm90_fp8_gemm_1d2d` (2112×7168) | 61 | 1.64 | 26.7 | [132,1,1] | FP8 GEMM; N=2112 (=7168/TP + shared expert) |
| Dense down_proj | `deep_gemm::sm90_fp8_gemm_1d2d` (3072×1536) | 61 | 0.72 | 11.8 | [128,1,1] | FP8 GEMM |
| Other dense proj | `deep_gemm::sm90_fp8_gemm_1d2d` | 128 | 2.55 | 19.9 | varies | q_a, kv_a, o_proj, etc. |
| Attention proj (NVJet splitK) | `nvjet_tst_64x64_64x13_2x1` | 58 | 0.69 | 11.8 | — | SplitK for small-M |
| MLA/FlashAttention | `PrefillWithKVCacheKernel` (flashinfer CUTLASS) | 61 | 1.25 | 20.4 | — | SM90 attention |
| MoE Routing (gate) | `moe_fused_gate_kernel` | 58 | — | — | — | TopK + routing |
| MoE Token Sort | `count_and_sort_expert_tokens_kernel` | 58 | — | — | — | — |
| MoE Sum Reduce | `moe_sum_reduce_warp_per_token_vec_kernel` | 58 | — | — | — | Weighted expert output sum |
| FP8 Quantization | `per_token_group_quant_8bit_kernel` | 366 | 1.90 | 5.2 | — | BF16→FP8 per-token-group quant |

**Key H200 observations:**
- MoE uses **Triton `fused_moe_kernel`** (not NVIDIA's batched MXFP4 GEMM). At 259μs avg, it's **3.1x slower per-call** than B200's `bmm_E2m1` (82μs) — reflecting both the FP8 vs FP4 precision difference and Triton vs cuBLAS codegen gap.
- Dense projections use **DeepGemm SM90 FP8** (`deep_gemm::sm90_fp8_gemm_1d2d`), which is a custom grouped-GEMM kernel. Grid dimensions encode the output tile count.
- With TP8 EP1, each rank processes **all 256 experts** but with 1/8 of the hidden dim — so MoE GEMM shapes are `[64×(7168/8)×expert_dim]` per expert.
- **No multi-stream pipelining** — the MoE computation, attention, and all dense projections run sequentially on one stream.
- 366 FP8 quant calls vs 183 FP4 quant calls on B200 — H200 needs per-token-group quantization for every projection, while B200's FP4 model stores pre-quantized weights.

#### Cross-Platform Shape Comparison

| Parameter | B200 FP4 TP4 EP4 | H200 FP8 TP8 EP1 |
|---|---|---|
| Hidden dim per rank | 7168/4 = 1792 | 7168/8 = 896 |
| Experts per rank | 256/4 = 64 | 256 (all, but sharded hidden) |
| Expert GEMM kernel | cuBLAS batched MXFP4 (SM100) | Triton fused_moe (SM90) |
| Expert GEMM shape | Batched: [B×64experts] × 2048 × 7168 | Fused: all 256 experts, hidden/8 |
| Dense GEMM kernel | flashinfer CUTLASS FP4 (SM100) | DeepGemm FP8 (SM90) |
| Attention kernel | SM100 fMHA (E4M3) | flashinfer CUTLASS (SM90) |
| Weight quant | Pre-quantized FP4 model | Online FP8 per-token-group |

### Oseltamivir · 2026-03-05

@claude do a profile run with dsr1 fp4 on MI300X with any conc, then help me analyze compute-comms overlap of the resultant trace, and the matrix shapes

### Klaud-Cold · 2026-03-05

**Claude finished @Oseltamivir's task in 31m 21s** —— [View job](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22696009062)

---
### Profile Analysis: DSR1 FP8 MI300X (SGLang, TP8, Conc=64)

- [x] Check available MI300X configs for DSR1
  - **Note:** FP4 is not available for MI300X (MI300X is gfx942, FP4/MXFP4 requires gfx950/MI355X). Used FP8: `dsr1-fp8-mi300x-sglang`
- [x] Trigger profile workflow — 3 attempts, all failed due to MI300X runner infrastructure issues
  - [Run #22696059061](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22696059061) — `mi300x-amds_0`: job cancelled during launch
  - [Run #22696731597](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22696731597) — `mi300x-amds_1`: failed at "Set up job"
  - [Run #22696807938](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22696807938) — failed at "Set up job"
- [x] Analyze compute-comms overlap (based on MI355X trace + MI300X architectural comparison)
- [x] Analyze matrix shapes

**All MI300X self-hosted runners are currently down.** No MI300X traces exist in trace storage. I've provided an architectural analysis below based on the MI300X config and the existing MI355X FP4 TP4 and H200 FP8 TP8 traces (same model, same SGLang version), highlighting what would differ on MI300X.

---

### MI300X FP8 Config Details

```yaml
image: lmsysorg/sglang:v0.5.9-rocm700-mi30x
model: deepseek-ai/DeepSeek-R1-0528
precision: fp8, framework: sglang, runner: mi300x
TP: 8, EP: 1, max-model-len: 2248 (1k1k)
```

MI300X is **gfx942** (CDNA3) with 8× 192GB HBM3 (304 GB/s/stack, 5.3TB/s aggregate), 1307 TFLOPS FP8. Compared to MI355X (gfx950, CDNA4): MI300X lacks MXFP4 support and has lower memory bandwidth per stack.

---

### Expected Compute-Comms Overlap Analysis

**Prediction: ZERO compute-comms overlap — single HIP stream, fully serialized.**

Based on the MI355X trace (same SGLang v0.5.9-rocm700 image family, same model):
- SGLang on ROCm uses a **single HIP stream** per TP rank for all operations
- All compute kernels and communication primitives (`cross_device_reduce`, `rcclGenericKernel`) execute sequentially on the same stream
- No multi-stream pipelining is implemented (unlike B200 which uses 2 CUDA streams)

#### Expected Communication Pattern (TP8, EP1, B=64 decode)

With TP8 (vs MI355X's TP4), each allreduce involves **8 ranks** instead of 4:

| Comm Type | Expected Count/step | Expected Behavior |
|---|---|---|
| `aiter::cross_device_reduce_2stage` | ~122 (2 per layer × 61 layers) | Per-call latency ~20-40μs (higher than MI355X's ~13μs due to 8 ranks vs 4) |
| `rcclGenericKernel` (RCCL) | ~2 | Bulk allreduce for initial setup |

**Expected comm % of decode: ~15-20%** — higher than MI355X's 10.5% because:
1. **8 ranks** in each allreduce (vs 4 on MI355X TP4) increases synchronization overhead
2. `cross_device_reduce_2stage` latency scales with rank count
3. No EP parallelism (EP1) — all 256 experts on each rank, requiring full allreduce after MoE

#### Comparison: Comms Across Platforms

| Platform | TP | EP | Allreduce Protocol | Comm % | Per-call Avg |
|---|---|---|---|---|---|
| MI355X FP4 | 4 | 1 | `cross_device_reduce_2stage` | 10.5% | ~13-15μs |
| **MI300X FP8** | **8** | **1** | **`cross_device_reduce_2stage`** | **~15-20% (est)** | **~20-40μs (est)** |
| B200 FP4 | 4 | 4 | flashinfer oneshot lamport | 23.8% | 21.5μs |
| H200 FP8 | 8 | 1 | flashinfer twoshot sync | 82.7% | 1,536μs |

MI300X benefits from AMD's `cross_device_reduce` which uses direct GPU memory access (XGMI) — much faster than H200's flashinfer twoshot protocol, but slower than MI355X due to 2× the ranks. The XGMI interconnect on MI300X provides 896 GB/s bi-directional between GPUs in a single node, which keeps allreduce overhead manageable even at TP8.

---

### Matrix Shapes Analysis

**Config: TP=8, EP=1, 61 layers (3 dense + 58 MoE), hidden=7168, MLA, 256 experts (8 active/token)**

#### Per-Layer GEMM Operations (Decode, B=64 tokens)

| Operation | Expected Kernel | Shape (M × N × K) | Precision | Notes |
|---|---|---|---|---|
| q_a_proj | hipBLASLt | 64 × 1536 × 7168 | FP8 (or BF16) | Same shape as MI355X — not TP-sharded |
| q_b_proj | hipBLASLt | 64 × (128×16/8) × 1536 | FP8 | TP-sharded: 16 heads per rank (128 total / 8) |
| kv_a_proj | hipBLASLt | 64 × 576 × 7168 | FP8 | Latent KV projection, not sharded |
| kv_b_proj | hipBLASLt or Triton | 64 × 256 × 512 | FP8 | Per-head KV expansion |
| MLA Decode Attention | aiter `mla_stage2` (INT8) or Triton | 64 heads × 1 × seq_len | INT8 | 16 query heads per rank (128/8) |
| o_proj | hipBLASLt | 64 × 896 × 512 | FP8 | Output: 7168/8=896 per rank |
| Router gate | Triton | 64 × 256 × 7168 | FP16/BF16 | Full expert routing (EP1) |
| **MoE Expert gate_up** | **Triton `fused_moe_kernel`** | **[8×64] × 2048 × 7168** | **FP8** | All 256 experts, hidden NOT sharded (EP1) |
| **MoE Expert down** | **Triton `fused_moe_kernel`** | **[8×64] × 7168 × 2048** | **FP8** | All 256 experts |
| Shared Expert gate_up | Triton/hipBLASLt | 64 × 4608 × 7168 | FP8 | Shared expert, not sharded |
| Shared Expert down | Triton/hipBLASLt | 64 × 7168 × 4608 | FP8 | |
| Dense FFN gate_up (layers 0-2) | hipBLASLt | 64 × 4608 × 7168 | FP8/BF16 | Only 3 dense layers |

#### Key MI300X-Specific Observations

1. **MoE uses Triton `fused_moe_kernel` (FP8)** — same as H200. MI300X lacks CK `moe_mxgemm` (that's gfx950/MI355X-only MXFP4). Based on H200 data, expect ~250-300μs per fused_moe call, making MoE GEMMs the **dominant compute cost at ~30-35%**.

2. **No MXFP4 advantage** — MI300X gfx942 doesn't have MXFP4 matrix cores. All GEMMs use FP8 (E4M3/E5M2) or BF16. This means:
   - Expert GEMMs are ~3× slower per-FLOP than MI355X's CK MXFP4 `moe_mxgemm`
   - Dense GEMMs use hipBLASLt FP8 kernels (similar perf to MI355X FP8 paths)

3. **TP8 sharding halves per-rank work vs MI355X TP4** for attention projections:
   - o_proj: 7168/8=896 per rank (vs 1792 on MI355X TP4)
   - q_b_proj: 16 heads/rank (vs 32 on MI355X)
   - But MoE is EP1, so **each rank still processes all 256 experts** with full hidden dim

4. **Expected kernel library**: Same SGLang v0.5.9 ROCm image → `aiter` library for attention (INT8 MLA decode), hipBLASLt for dense FP8 GEMMs, Triton for MoE fused kernels and routing.

5. **Memory bandwidth bound**: MI300X at 5.3TB/s aggregate (vs MI355X at 8TB/s) means decode attention (memory-bound at B=64) will be proportionally slower. The MLA INT8 attention kernel duration scales inversely with bandwidth.

#### Expected Decode Time Breakdown (MI300X FP8 TP8, B=64, estimated)

| Category | Est. % | Notes |
|---|---|---|
| MoE Expert GEMM (Triton FP8) | ~30-35% | Dominant; Triton fused_moe, all 256 experts/rank |
| Communication | ~15-20% | `cross_device_reduce` across 8 ranks |
| Dense GEMM (hipBLASLt FP8) | ~12-15% | q/kv/o projections + dense FFN layers |
| MLA Attention (INT8) | ~8-10% | Memory-bound, lower BW than MI355X |
| MoE Routing/Sorting | ~5-7% | TopK, token sorting across 256 experts |
| RMSNorm + Quant | ~5-6% | Per-layer normalization + FP8 quantization |
| Other (copy/elem/etc) | ~5-8% | Elementwise, memory copies |

**Estimated decode wall time: ~35-50ms** (vs MI355X's 20ms and H200's 283ms). MI300X should be significantly faster than H200 (better allreduce via XGMI, same Triton MoE kernels) but slower than MI355X (no MXFP4, lower memory bandwidth, TP8 vs TP4 comms overhead).

---

### Summary

The MI300X runners are currently experiencing infrastructure issues (3/3 attempts failed). The analysis above is based on the MI300X config and architectural comparison with successfully profiled MI355X and H200 traces. Key takeaways:

- **Zero compute-comms overlap expected** (single HIP stream, same as MI355X)
- **MoE dominates compute** via Triton `fused_moe_kernel` FP8 (~30-35%), significantly slower than MI355X's CK MXFP4
- **Comms ~15-20%** via `cross_device_reduce` over XGMI — much better than H200's flashinfer twoshot (83%) but worse than MI355X TP4 (10.5%)
- **No FP4 support** on MI300X (gfx942) — FP8 is the lowest precision available

Once MI300X runners are back online, I can re-trigger the profile for actual trace data.

### Oseltamivir · 2026-03-05

@claude why does B200 profile have 41375 cases with "Input dims" mi355x has 37945, and H200 has 73769. Are some input dims missing?

### Klaud-Cold · 2026-03-05

**Claude finished @Oseltamivir's task in 4m 36s** —— [View job](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22698174426)

---
### Analysis: "Input Dims" Count Differences Across Traces

- [x] Download and examine trace files from all three profiles
- [x] Count and categorize "Input Dims" entries
- [x] Identify the source of the discrepancy

**Short answer: No input dims are missing.** The counts you see (B200=41,375, MI355X=37,945, H200=73,769) are the events where `Input Dims` contains **actual tensor dimensions** (numbers). The remaining events have empty `Input Dims` (like `[[], [], []]`) because they are tensor-creation ops that take no tensor inputs — only scalar parameters.

#### Full breakdown

| Trace | Total `Input Dims` | With actual dims | Empty (no tensor inputs) |
|---|---|---|---|
| **MI355X** FP4 TP4 | 52,800 | **37,945** ✓ | 14,855 |
| **B200** FP4 TP4 EP4 | 51,490 | **41,375** ✓ | 10,115 |
| **H200** FP8 TP8 | 93,640 | **73,769** ✓ | 19,871 |

The "empty" events are dominated by ops that create tensors from nothing:

| Empty-dims op | MI355X | B200 | H200 | Description |
|---|---|---|---|---|
| `aten::empty` | 8,371 | 7,619 | 13,559 | Allocates uninitialized tensor |
| `aten::empty_strided` | 4,736 | 2,396 | 3,808 | Allocates with specific strides |
| `aten::arange` | 252 | 8 | 16 | Creates range tensor from scalars |
| Other (item, add on scalars) | 1,488 | 84 | 2,480 | Scalar-only ops |

These ops only receive scalar arguments (sizes, dtypes, devices), not tensor inputs, so PyTorch's profiler records their `Input Dims` as empty lists.

#### Why the non-empty counts differ across platforms

The per-rank non-empty counts also vary: **~9,486/rank** (MI355X), **~10,343/rank** (B200), **~9,221/rank** (H200). This is because each platform uses different kernel libraries and code paths:

| Factor | MI355X | B200 | H200 |
|---|---|---|---|
| GEMM dispatch | hipBLASLt + CK + Triton | cuBLAS MXFP4 + CUTLASS + NVJet | DeepGemm FP8 + Triton fused_moe |
| FP8 quantization ops | 0/rank | 0/rank | 366/rank (`sgl_per_token_group_quant_8bit`) |
| `aten::permute`/`numpy_T` | 14/rank | **734/rank** | 2/rank |
| `aten::matmul`+`mm`+`linear` | 303/rank | 303/rank | **59/rank** (uses deep_gemm custom ops instead) |
| `aten::copy_` | 712/rank | 302/rank | 184/rank |
| DeepGemm custom ops | 0 | 0 | **250/rank** (`deep_gemm::fp8_gemm_nt`) |

Key differences:
- **B200 has the most** per rank because its NVJet/CUTLASS FP4 path requires extra `permute`/`numpy_T`/`reshape` ops to prepare tensor layouts for SM100 kernels (+430 extra ops/rank vs others)
- **H200 has fewer `aten::mm`/`linear`** because SGLang's DeepGemm FP8 path wraps GEMMs in custom ops (`sglang::deep_gemm_fp8_fp8_bf16_nt`) that appear as separate traced events, but it gains 366/rank from FP8 quantization ops and 250/rank from DeepGemm calls
- **MI355X falls in between** — uses standard `aten::mm` dispatch via hipBLASLt but with more `aten::copy_`/`_to_copy` due to ROCm's additional format conversion steps

**H200 has 2× the total** simply because it has **8 TP ranks** vs 4 on the others (8×9,221=73,769 vs 4×9,486=37,945 and 4×10,343=41,375).

### Oseltamivir · 2026-03-05

@claude do another sweep for MI325X

### Klaud-Cold · 2026-03-05

**Claude finished @Oseltamivir's task in 23m 31s** —— [View job](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22698917877)

---
### Profile Analysis: DSR1 FP8 MI325X (SGLang, TP8, Conc=64)

- [x] Trigger profile workflow for `dsr1-fp8-mi325x-sglang` (conc=64) — [Run #22698950054](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22698950054) ✅
- [x] Wait for profile run to complete
- [x] Retrieve Perfetto trace link
- [x] Analyze compute-comms overlap
- [x] Analyze matrix shapes

**Perfetto Trace:** [Open in Perfetto](https://semianalysisai.github.io/InferenceX-trace-storage/?src=https%3A%2F%2Fraw.githubusercontent.com%2FSemiAnalysisAI%2FInferenceX-trace-storage%2F6cf203cbde4d16d508b8bcb5474bb85f77944712%2Fprofiles%2Ff65d6b4b1e0eb7744b9987ede6b1d11735f6dcf2%2Fmi325x%2Fsglang%2Fdsr1_1k1k_fp8_tp8_ep1_conc64%2Ftrace.json.gz&title=dsr1_1k1k_fp8_tp8_ep1_conc64)

---

### Compute-Comms Overlap Analysis

**Key finding: ZERO compute-comms overlap.** All GPU kernels execute on a **single HIP stream** per TP rank (`[TPxx] stream 7`). Since there is only one stream, all operations are strictly serialized — no GEMM can run concurrently with any `cross_device_reduce` or `rcclGenericKernel`.

MI325X is **gfx942 (CDNA3)** — same architecture as MI300X. It uses the same SGLang ROCm image (`lmsysorg/sglang:v0.5.9-rocm700-mi30x`) and the same `aiter` kernel library.

#### Communication Primitives

| Comm Type | Count | Total Time | Avg/call | Notes |
|---|---|---|---|---|
| `aiter::cross_device_reduce_2stage` | 123 | 2.41ms | 19.6μs | 2 per layer × 61 layers + 1 transition; via XGMI direct GPU memory |
| `rcclGenericKernel` (RCCL) | 1 | 0.09ms | 90μs | Single bulk allreduce at decode start |
| **Total comms (stable decode)** | **124** | **2.50ms** | — | **6.9% of kernel time** |

The `cross_device_reduce_2stage` performs a 2-phase allreduce: phase 1 (read) averages ~19.6μs per call, which is fast thanks to MI325X's XGMI interconnect (896 GB/s bi-directional). The first CDR call is anomalously slow (269μs) due to prefill→decode transition warmup.

#### RCCL Init Burst (Decode Setup)

Between prefill and stable decode, there's a **536ms RCCL initialization burst**: 108 `rcclGenericKernel` calls averaging 1,634μs each, with large inter-kernel gaps (2-5ms). This appears to be an RCCL connection setup / topology negotiation phase, not steady-state communication. Only 32.9% GPU utilization during this phase.

#### Decode Step Time Breakdown (single step, 64 tokens)

| Category | Count | Time (ms) | % |
|---|---|---|---|
| Dense GEMM (aiter A8W8 blockscale) | 189 | 11.89 | 32.6% |
| MoE Expert GEMM (aiter FP8 blockscale) | 58 | 9.28 | 25.5% |
| MLA Attention (aiter A16W8) | 61 | 3.34 | 9.2% |
| Elementwise (misc) | 493 | 3.21 | 8.8% |
| **Communication** | **124** | **2.50** | **6.9%** |
| hipBLASLt GEMM | 181 | 1.30 | 3.6% |
| RMSNorm + Quant | 245 | 1.08 | 3.0% |
| FP8 Quantization | 247 | 1.08 | 3.0% |
| Cat/Copy | 122 | 0.73 | 2.0% |
| MLA Reduce | 61 | 0.70 | 1.9% |
| MoE Sorting (CK) | 116 | 0.51 | 1.4% |
| KV Cache Ops | 61 | 0.26 | 0.7% |
| TopK Selection | 58 | 0.25 | 0.7% |
| Shared Expert Append | 58 | 0.24 | 0.6% |
| Other | ~10 | 0.07 | 0.2% |
| **TOTAL** | **2085** | **36.45** | **100%** |

**Decode wall-clock: 36.47ms** | GPU utilization: **99.9%** (virtually zero idle bubbles)

#### Communication Pattern Per Layer

Each of the 61 layers issues **2 `cross_device_reduce` calls**:
1. **Attention output allreduce** — avg 16.7μs (excl. first cold call)
2. **FFN/MoE output allreduce** — avg 18.4μs

With TP8 and only 64 tokens × 7168 hidden dim, each allreduce payload is tiny. Communication is only **6.9% of total** — surprisingly low for TP8, demonstrating that XGMI `cross_device_reduce` scales well with rank count on MI325X.

#### Cross-Rank Balance

| Rank | Wall (ms) | Kernel (ms) | Comm (ms) | Comm % |
|---|---|---|---|---|
| TP00 | 36.47 | 36.45 | 2.50 | 6.9% |
| TP01 | 37.03 | 36.61 | 2.66 | 7.3% |
| TP02 | 36.46 | 36.44 | 2.48 | 6.8% |
| TP03 | 37.14 | 36.71 | 2.89 | 7.9% |
| TP04 | 37.14 | 36.62 | 2.43 | 6.6% |
| TP05 | 37.15 | 36.73 | 2.54 | 6.9% |
| TP06 | 36.48 | 36.46 | 2.24 | 6.1% |
| TP07 | 37.15 | 36.72 | 2.40 | 6.5% |

Ranks are well-balanced. Max comm skew is only 0.65ms (TP03 vs TP06). No rank-0 coordinator asymmetry — unlike the H200's flashinfer twoshot protocol, `cross_device_reduce_2stage` distributes work evenly across ranks.

#### Prefill Phase

| Metric | Value |
|---|---|
| Kernels | 1,844 |
| Wall | 91.35ms |
| Kernel time | 71.99ms |
| GPU utilization | 78.8% |
| Comm % | 25.8% (18.5ms) |

Prefill is significantly more compute-efficient than H200's prefill (13.9% util) but less than MI355X's. The lower utilization vs decode reflects larger allreduce payloads during prefill (full sequence length tokens) and CPU scheduling overhead.

---

### Matrix Shapes Analysis

**Config: TP=8, EP=1, 61 layers (3 dense + 58 MoE), hidden=7168, MLA (qk_head=576, v_head=512), 256 experts (8 active/token)**

#### Per-Layer GEMM Operations (Decode, B=64 tokens)

| Operation | Kernel Type | Shape (M × N × K) | Precision | Count | Avg Duration |
|---|---|---|---|---|---|
| q_a_proj | aiter A8W8 blockscale | 64 × 1536 × 7168 | FP8 blockscale | 61 | ~123μs |
| kv_a_proj | aiter A8W8 blockscale | 64 × 576 × 7168 | FP8 blockscale | 61 | ~30μs |
| o_proj | aiter A8W8 blockscale | 64 × 896 × 512 | FP8 blockscale | 61 | ~34μs |
| kv_b_proj | hipBLASLt (MT32x64x128) | 64 × 256 × 512 | BF16 | 61 | ~5.5μs |
| q_b_proj (rope) | hipBLASLt (MT16x16x256) | 64 × (128×16/8) × 1536 | BF16 | 61 | ~5.4μs |
| MLA Decode Attention | aiter `mla_a16w8_qh16` | 16 heads × 64 × seq_len | A16W8 (INT8 KV) | 61 | ~55μs |
| MLA Reduce | aiter `kn_mla_reduce_v1` | 16 heads × 512 | BF16 | 61 | ~11.5μs |
| Router gate | hipBLASLt (MT16x16x256) | 64 × 256 × 7168 | BF16 | 58 | ~10μs |
| Dense FFN gate_up (layers 0-2) | aiter A8W8 blockscale | 64 × (4608/8) × 7168 | FP8 blockscale | 3 | ~122μs |
| Dense FFN down (layers 0-2) | aiter A8W8 blockscale | 64 × 7168 × (4608/8) | FP8 blockscale | 3 | ~39μs |
| Shared Expert gate_up | aiter A8W8 blockscale | 64 × (4608/8) × 7168 | FP8 blockscale | — | included in dense GEMM count |
| **MoE Expert GEMM** | **aiter `fmoe_bf16_blockscaleFp8_g1u1_vs_silu_1tg_ps_32x256`** | **[8×64] × 2048 × 7168** | **FP8 blockscale** | **58** | **~160μs** |

#### Key Observations

1. **Dense GEMMs dominate at 32.6%** — MI325X uses `aiter::_gemm_a8w8_blockscale` (FP8 with block-scale quantization, GROUP_K=128, GROUP_N=128) for all dense projections. Three distinct kernel configs handle different matrix shapes:
   - **Large** (~123μs): q_a_proj [64 × 1536 × 7168] — 61 calls
   - **Medium** (~34μs): o_proj/dense-down [64 × 896 × 512] — 61 calls
   - **Small** (~30μs): kv_a_proj [64 × 576 × 7168] — 61 calls

2. **MoE Expert GEMM is 25.5%** using `aiter::fmoe_bf16_blockscaleFp8_g1u1_vs_silu_1tg_ps_32x256`:
   - `g1u1_vs_silu` = gate+up fused with SiLU activation inline
   - `1tg` = 1 token group, `ps` = partial sum
   - `32x256` = tile sizes (32 M-dim, 256 K-dim)
   - This is a **single kernel** that fuses gate_up + SiLU + down_proj for all 8 active experts — highly efficient
   - At 160μs avg, it's **~2× faster than MI355X's CK `moe_mxgemm`** (64μs gate_up + 55μs down = 119μs) per call, but MI325X does it in one fused call vs MI355X's two separate calls

3. **MLA uses `aiter::mla_a16w8_qh16`** — A16 activations with W8 (INT8) quantized KV cache:
   - `qh16` = 16 query heads per rank (128 total / TP8)
   - `m16x4_n16x1` = tile configuration
   - At 55μs avg it's **~2.9× slower** than MI355X's 19μs (MI355X has higher memory bandwidth: 8TB/s vs MI325X's ~5.3TB/s)

4. **hipBLASLt handles small projections** in BF16:
   - `MT32x64x128` for kv_b_proj (small N=256 × K=512)
   - `MT16x16x256` for q_b_proj and router gate
   - These are tiny M=64 decode shapes, purely latency-bound

5. **No multi-stream overlap** — same as MI355X. Adding a second stream for comms could save ~2.5ms (6.9%) by overlapping `cross_device_reduce` with independent next-layer compute.

#### Comparison: MI325X vs MI355X vs H200

| Metric | MI325X FP8 TP8 | MI355X FP4 TP4 | H200 FP8 TP8 |
|---|---|---|---|
| Decode wall time | **36.47ms** | **20.11ms** | **282.6ms** |
| Compute time | 33.95ms | 17.96ms | 44.8ms |
| Comm time | 2.50ms | 2.10ms | 213.9ms |
| Comm % | 6.9% | 10.5% | 82.7% |
| GPU utilization | 99.9% | 99.7% | 91.5% |
| MoE kernel | aiter FP8 fused MoE | CK MXFP4 moe_mxgemm | Triton fused_moe |
| MoE time/layer | 160μs (1 call) | 119μs (2 calls) | 518μs (2 calls) |
| Dense GEMM kernel | aiter A8W8 blockscale | hipBLASLt BF16 | DeepGemm FP8 |
| MLA kernel | aiter A16W8 | aiter A8W8 (INT8) | flashinfer CUTLASS |
| Allreduce protocol | cross_device_reduce | cross_device_reduce | flashinfer twoshot |
| Allreduce avg/call | 19.6μs | 13-15μs | 1,536μs |
| Streams | 1 (serial) | 1 (serial) | 1 (serial) |

**MI325X is 1.81× slower than MI355X** due to: (1) FP8 vs MXFP4 — no MXFP4 support on gfx942, (2) lower memory bandwidth (5.3 vs 8 TB/s) hurting attention, (3) TP8 vs TP4 doubling allreduce ranks. But MI325X is **7.7× faster than H200** thanks to efficient `cross_device_reduce` over XGMI vs H200's problematic flashinfer twoshot protocol.
