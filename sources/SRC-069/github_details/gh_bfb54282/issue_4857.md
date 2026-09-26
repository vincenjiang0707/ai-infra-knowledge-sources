# [Issue #4857] cuTile MoE progress tracker

source: https://github.com/flashinfer-ai/flashinfer/issues/4857
state: open | updated: 2026-09-22T23:54:40Z
labels: op: moe

## 正文

Current issue tracks progress on the cuTile fused MoE implementation that started with #4646 

We expect cuTile can provide maintainability, as well as easy debugging and development experience for a "catch all" MoE implementation.

Here we track the MoE support across all target architectures, precision combinations, and activations through FlashInfer's unified MoE API.

The end goal is support for all SKUs, all relevant data types (including mixed weight/input precision) and activation parity with the CUTLASS and TRTLLM-gen fused MoE backends.

## PRs

PR #4646 provides:

- [x] BF16 on SM89, SM90, SM120, and SM121 with SwiGLU and ReLU²
- [x] NVFP4 W4A4 on SM120 and SM121 with SwiGLU and ReLU²
- [x] Unified MoE integration, autotuning, CUDA Graph support, tests, documentation, and benchmarks

PR #4888 adds support for all activations listed below

PR #5099 adds support for MXFP4 W4A4 and W4A16  (NVFP4, MXFP4).

PR #5332 adds support for per-tensor scaled FP8 and MXFP8 (W4A8, W8A8, W8A16)

## Target Architecture coverage

- [ ] SM80
- [ ] SM86
- [x] SM89
- [x] SM90
- [ ] SM100
- [ ] SM103
- [ ] SM107
- [ ] SM110
- [x] SM120
- [x] SM121

An architecture is complete when all hardware-applicable precision and activation combinations are tested. Hardware or cuTile-toolchain limitations should be recorded explicitly as N/A.

## Target Precision coverage

Support same-precision execution and higher-precision activations:

- [x] BF16 weights: W16A16
- [x] NVFP4 weights: 
  - [x] W4A4, NVFP4_NVFP4
  - [x] W4A16, NVFP4_BF16
- [x] MXFP4 weights: 
  - [x] W4A4,  MXFP4_MXFP4
  - [x] W4A8,  MXFP4_MXFP8
  - [x] W4A16 MXFP4_BF16
- [x] MXFP8 weights:
  - [x] W8A8 MXFP8_MXFP8
  - [x] W8A16 MXFP8_BF16
- [x] Per-tensor-scaled FP8 weights: W8A8, W8A16
  - [x] W8A8 FP8_FP8
  - [x] W8A16 FP8_BF16
- [ ] DeepSeek-style block-scaled FP8 weights: W8A8, W8A16

For W4A8, track each applicable activation scaling format—per-tensor FP8, block-scaled FP8, and MXFP8—separately. Every combination must define its packing, scale, accumulation, and output contracts.

## Target Activation coverage

- [x] SwiGLU, including parameterized/OAI semantics
- [x] SwiGLU-step
- [x] GeGLU
- [x] GeGLU-tanh
- [x] SiTU
- [x] ReLU²
- [x] GELU
- [x] ReLU
- [x] SiLU
- [x] Identity

## Expert parallelism

Expert parallelism is the final milestone, after single-rank coverage is stable.

- [ ] Local expert ranges and correct routing semantics
- [ ] Multi-GPU correctness and CUDA Graph support
- [ ] Representative EP performance characterization

## 评论 (6)

### elwhyjay · 2026-09-03

Hi @bkryu . This looks really interesting! I'd like to work on NVFP4 weights if it's still available.

### bkryu · 2026-09-04

Hi @elwhyjay, thanks for checking in with this. I actually have a branch https://github.com/flashinfer-ai/flashinfer/compare/main...bkryu:flashinfer:cutile_moe_fp4_matrix that adds support for `W4A4-MXFP4`, `W4A16-MXFP4_BF16`, and `W4A16-NVFP4_BF16`. It is currently blocked by https://github.com/flashinfer-ai/flashinfer/pull/4952 but I expect to get a PR opened from a branch soon.  Note that `W4A4-NVFP4` is already supported.

The current issue was created mostly to share a plan that we are working on a catch-all cuTile MoE. The basic goal for the cuTile MoE is to support "all precisions, all activations, on all GPUs", which pertains to functional support so it is doable. 

The bigger ambition is to make cuTile MoE actually be performance-competitive anywhere so it gets very widely adopted. The avenue I have not yet explored very deeply is performance. https://github.com/flashinfer-ai/flashinfer/pull/4646 shows in its description that the cuTile MoE can be competitive against our own CUTLASS MoE in select cases. Some things I haven't explored in the SM120/121 space is:
- I have not tested performance on Spark. 
- How does performance compare to the b12x MoE's W4A4 that exists in FlashInfer on SM120/121
- Can we push performance even further? Ideas I have but have not yet explored:
  - For W4A4, the kernel sequence goes input quantization -> grouped GEMM 1 -> act+quant -> grouped GEMM 2 -> Combine (non-gated activation fuses grouped GEMM 1 & act+quant into a single kernel). Are there any other fusion opportunities? What if we fuse the input quantization to grouped GEMM 1? Is fusing better than not fusing? I have seen during development that not fusing can be more performant in some cases.
  - I don't think the grouped GEMMs have explored optimizations like split-K or split AB.
  - Where is the cuTile MoE performance strong and where is it weak?

Once I merge the W4A16 support, I will likely move on to further functional support on variants so would be great if somebody who is interested in cuTile and performance tuning could look into it. It could be a fun (also difficult) experience because it will need a lot of experimenting of _what optimization works for which problem size regime, and etc._ while making sure we don't have to autotune over hundreds of kernel configs. 

I rambled a bit, but @elwhyjay  please let me know if you are interested in tuning performance while I expand support. 

### faradawn · 2026-09-04

Hi @elwhyjay , based on your other PRs, you seem to have an SM120 device. Can I look at the Spark (SM121) performance of the cuTile MoE? I expect the performance profiles and required tuning to be different

### elwhyjay · 2026-09-05

Hi @bkryu, thank you for the detailed write-up. Yes, I am interested in the performance side. I will wait until that PR lands and then start from there.


### elwhyjay · 2026-09-05

Hi @faradawn, sure, please go ahead with Spark. I only have SM120 hardware.

Since GB10 uses the same Blackwell SM as RTX PRO 6000, I think the kernel-level work (quantization fusion, split-K, the large-token regime) applies to both, so I can drive that on SM120. The config/heuristic side will differ because of the SM count and memory bandwidth, and the SM121 entries in `runners.py` are currently copies of SM120, so Spark-specific tuning there would be a good place for you to start.

Let us use the #4646 testlist for both so the numbers stay comparable.

### bkryu · 2026-09-08

Current status: 
1. Waiting for https://github.com/flashinfer-ai/flashinfer/pull/4952 to be merged.
  a. PR enables expression of more flexible data types. 
2. https://github.com/bkryu/flashinfer/tree/cutile_moe_fp4_matrix adds support for `[weight, actvation] = [mxfp4, mxfp4], [mxfp4, bf16], and [nvfp4, bf16]` support, which completes the [fp4, bf16] matrix.
