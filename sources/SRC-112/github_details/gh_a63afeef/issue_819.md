# [Issue #819] test claude profile compare / 测试 Claude profile 对比

source: https://github.com/SemiAnalysisAI/InferenceX/issues/819
state: open | updated: 2026-07-04T05:12:31Z
labels: 

## 正文

@claude do a profile run with dsr1 fp8 on b200 with conc 4, and for 1 decode step & dsr1 fp8 on mi300 with conc 4, and for 1 decode step


compare the 2 different traces & breakdown where the time went kernel by kernel, wall clock time & %, how long did MoE take, etc?

## 中文说明
请求对 DeepSeek-R1 FP8 B200（conc 4，1 个解码步骤）和 DeepSeek-R1 FP8 MI300（conc 4，1 个解码步骤）分别进行 profile 运行，然后对比两个 trace 的逐内核耗时分解（wall clock 时间和百分比），包括 MoE 耗时等。


## 评论 (1)

### Klaud-Cold · 2026-02-26

**Claude finished @functionstackx's task in 216m 2s** —— [View job](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22463851238)

---
## DSR1 FP8 Profile Comparison: B200 vs MI300X (conc=4)

### Setup
| | B200 (NVIDIA) | MI300X (AMD) |
|---|---|---|
| **Model** | DeepSeek-R1-0528 (671B MoE) | DeepSeek-R1-0528 (671B MoE) |
| **Precision** | FP8 | FP8 |
| **Framework** | SGLang v0.5.6 | SGLang v0.5.8 |
| **TP** | 8 | 8 |
| **Concurrency** | 4 | 4 |
| **Runner** | b200-dgxc-slurm_8 | mi300x-amds_3 |
| **Decode steps captured** | 8 | 8 |

### Profile Runs
- **B200**: [Run #22](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22466066057) (success)
- **MI300X**: [Run #21](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22463891499) (profiling succeeded; storage push failed due to trace >100MB)
- **B200 Perfetto trace**: [View in Perfetto](https://semianalysisai.github.io/InferenceX-trace-storage/?src=https%3A%2F%2Fraw.githubusercontent.com%2FSemiAnalysisAI%2FInferenceX-trace-storage%2F8345d9a92dd9c4a033435330ce7d5c0560b3bd46%2Fprofiles%2F3450ced072e78b6d7acca6c7e07a83150f9f23f7%2Fb200%2Fsglang%2Fdsr1_1k1k_fp8_tp8_ep1_conc4%2Ftrace.json.gz&title=dsr1_1k1k_fp8_tp8_ep1_conc4)
- MI300X trace available as [artifact from run #21](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22463891499) (too large for Perfetto relay)

---

### Per-Decode-Step Comparison

| Category | B200 (ms) | B200 % | MI300X (ms) | MI300X % | Ratio | Winner |
|---|---:|---:|---:|---:|---:|---|
| **AllReduce / Communication** | 156.70 | 69.7% | 214.89 | 73.1% | 0.73x | B200 |
| **MoE (Experts + Routing)** | 32.60 | 14.5% | 29.27 | 10.0% | 1.11x | MI300X |
| **GEMM (non-MoE)** | 23.39 | 10.4% | 29.14 | 9.9% | 0.80x | B200 |
| **Quantization / Dequant** | 5.25 | 2.3% | 3.39 | 1.2% | 1.55x | MI300X |
| **Attention (MLA/MHA)** | 3.91 | 1.7% | 3.57 | 1.2% | 1.10x | MI300X |
| **Elementwise / Memory** | 1.76 | 0.8% | 6.42 | 2.2% | 0.27x | B200 |
| **RMSNorm / LayerNorm** | 0.00 | 0.0% | 4.24 | 1.4% | — | B200 |
| **Other** | 1.09 | 0.5% | 2.91 | 1.0% | 0.37x | B200 |
| **TOTAL** | **224.70** | **100%** | **293.83** | **100%** | **0.76x** | **B200** |

### Key Findings

**B200 is 1.3x faster per decode step** (224.70 ms vs 293.83 ms).

Both platforms are **heavily communication-bound** (~70-73% of step time in AllReduce):

1. **AllReduce dominates on both**: B200 spends 156.70 ms (69.7%) and MI300X spends 214.89 ms (73.1%). B200's AllReduce is **1.4x faster** — the single biggest performance differentiator.
   - B200 uses `flashinfer::allreduce_fusion_kernel_twoshot` (135.35 ms/step) + NCCL (15.65 ms/step) + `cross_device_reduce_1stage` (4.23 ms/step)
   - MI300X uses `aiter::cross_device_reduce_2stage` (213.46 ms/step) — nearly all in one kernel

2. **MoE is slightly faster on MI300X** (29.27 ms vs 32.60 ms, MI300X wins by ~10%). AMD's AITER `fmoe_bf16_blockscaleFp8` fused kernel (26.35 ms/step) is efficient. NVIDIA uses separate `bmm_*` batch GEMMs + `moe::dev::finalize` + `moe::dev::activation` kernels.

3. **Non-MoE GEMM is faster on B200** (23.39 ms vs 29.14 ms, B200 wins by 20%). NVIDIA's `gemm_Bfloat16_E4m3E4m3` cutlass kernels outperform AMD's `gemm_a8w8_blockscale` kernels.

4. **Quantization faster on MI300X** (3.39 ms vs 5.25 ms) — AITER's fused quant kernel handles it in fewer calls.

5. **Attention roughly equal** (3.91 ms B200 vs 3.57 ms MI300X) — both use efficient fused attention (SM100a on B200, AITER fmha on MI300X).

### MoE Deep Dive

| | B200 | MI300X |
|---|---|---|
| MoE time per step | 32.60 ms | 29.27 ms |
| MoE % of total step | 14.5% | 10.0% |
| Top MoE kernel | `bmm_E4m3_*` (14.45 ms) | `fmoe_bf16_blockscaleFp8_*` (26.35 ms) |
| MoE approach | Separate bmm + finalize + activation | Single fused kernel (AITER) |

### Top 5 Kernels per Platform

**B200:**
| Kernel | Per-step | % |
|---|---:|---:|
| `flashinfer::allreduce_fusion_kernel_twoshot` | 135.35 ms | 60.2% |
| `ncclDevKernel_AllReduce_Sum_bf16_RING_LL` | 15.65 ms | 7.0% |
| `gemm_Bfloat16_E4m3E4m3_*_t128x16x128` | 14.96 ms | 6.7% |
| `bmm_E4m3_E4m3E4m3_*_t128x16x128` | 14.45 ms | 6.4% |
| `bmm_Bfloat16_E4m3E4m3_*_t128x16x128` | 11.82 ms | 5.3% |

**MI300X:**
| Kernel | Per-step | % |
|---|---:|---:|
| `aiter::cross_device_reduce_2stage` | 213.46 ms | 72.6% |
| `aiter::fmoe_bf16_blockscaleFp8_g1u1_vs_silu` | 26.35 ms | 9.0% |
| `gemm_a8w8_blockscale_*_M128_N128` (variant 1) | 8.11 ms | 2.8% |
| `gemm_a8w8_blockscale_*_M128_N128` (variant 2) | 7.00 ms | 2.4% |
| `gemm_a8w8_blockscale_*_M128_N128` (variant 3) | 3.63 ms | 1.2% |

### Summary
At conc=4 with TP=8 FP8, **communication (AllReduce) accounts for 70-73% of decode step time on both platforms**. The biggest optimization opportunity is reducing AllReduce latency. B200 has a 1.4x advantage here, which drives its overall 1.3x lead. Compute-wise, the platforms are competitive — MI300X's fused MoE kernel is actually slightly faster, while B200's cutlass GEMMs are faster for non-MoE projections.
