source: https://github.com/flashinfer-ai/flashinfer/releases

# Releases: flashinfer-ai/flashinfer

## Release list

## Release v0.7.0

*These highlights are also published at flashinfer.ai/releases.*

### v0.7.0 Highlights

FlashInfer 0.7.0 makes the unified mixture-of-experts (MoE) API official, brings TRT-LLM Gen MoE kernels into readable Python source with PrimTS, and introduces Autotuner v2 and a formal experimental-API policy. It also expands sparse and linear attention, expert-parallel serving, and diffusion workloads across Blackwell GPUs.

Read the [v0.7 overview](https://flashinfer.ai/2026/09/22/flashinfer-v07.html) and the accompanying deep dives on [MegaMoE](https://flashinfer.ai/2026/09/22/mega-moe.html), [Autotuner v2](https://flashinfer.ai/2026/09/22/autotuner-v2.html), and the [experimental path](https://flashinfer.ai/2026/09/22/experimental-path.html).

**Unified MoE API is official**

`MoELayer`

is now an official FlashInfer API, with the lower-level kernel entry points supported alongside it. `QuantConfig`

gives weights, activations, and output explicit `QuantFormat`

fields: `QuantConfig(weight=QuantFormat.MXFP4)`

selects MXFP4 weights with BF16 activations, while adding `activation=QuantFormat.MXFP8`

selects W4A8. Backend coverage expands with quantization-specific CUTLASS runners, cuTile BF16 and NVFP4 MoE, and CuTe-DSL BF16 MoE on Hopper.

**TRT-LLM Gen MoE kernels as Python source with PrimTS**

The experimental PrimTS MoE backend exposes kernels built with the CUTLASS DSL Primitives and Task Scheduling APIs, making the expert GEMMs available as readable Python source. It supports BF16, per-tensor and block-scaled FP8, and NVFP4/MXFP4 combinations, while reusing TRT-LLM Gen routing and finalization. Accuracy qualification targets B200; B300 qualification is still pending, and supported configurations have backend-specific restrictions. PrimTS attention also gains paged block-sparse attention, variable-window attention, and a unified `plan()`

/`run()`

contract for reusable wrappers.

**Autotuner v2 tunes the way you serve**

`autotune_v2()`

lets applications measure candidates in eager or CUDA-graph execution and persist the results in an environment-specific cache managed by FlashInfer. Atomic cache entries support concurrent rank writes, and `autotune_v2_reload()`

lets homogeneous ranks converge on shared results. In the [reported vLLM validation](https://github.com/flashinfer-ai/flashinfer/issues/3920#issuecomment-5590875709), Qwen3-8B-FP8 at TP2 on B200 reduced its tuning window from 128 seconds on a cold start to 1 second on restart with the same cache; total startup was 410.7 seconds and 165.3 seconds, respectively. Applications opt in through the new API; `autotune()`

remains available.

**Experimental APIs and backends have an explicit opt-in path**

Experimental APIs are marked with `@flashinfer_experimental_api`

, and experimental backends have a dedicated `flashinfer.experimental`

namespace. Calling an experimental API or explicitly selecting a marked backend emits a warning; automatic selection includes marked experimental backends only when `FLASHINFER_ALLOW_EXPERIMENTAL_AUTO_BACKENDS=1`

is set. The policy defines admission and graduation criteria and keeps experimental implementations JIT-only, outside prebuilt packages.

**Expert-parallel MoE expands across Blackwell**

`moe_ep`

adds an unquantized BF16 MegaMoE backend and a W4A8 split backend on B200, with MXFP8-packed dispatch for the latter. RTX PRO 6000 and DGX Spark gain an MXFP8 MegaMoE backend with functional correctness validated and performance tuning ongoing. The NCCL-EP split path supports CUDA-graph capture through a reusable handle with per-step `update()`

, validated through vLLM on four B200 GPUs.

**DeepSeek-V4 and MiniMax-M3 sparse attention**

Blackwell gains paged FP8/MXFP4 indexer logits and more top-K choices, including a CUB backend with variable-length support. DeepSeek-V4 Flash sparse MLA supports an NVFP4 KV cache on SM120/SM121 through `kv_cache_format="nvfp4"`

. MiniMax-M3 sparse attention gains source-distributed CAKE-generated kernels on SM100/SM103; the B200 kernel benchmark reports a 2.45× geometric-mean speedup over the MiniMax baseline across 11 comparable prefill, decode, speculative, and boundary cases.

**Linear attention for Kimi K3, Qwen 3.6, and Nemotron-H**

Kimi K3 gains a speculative-verification entry point compatible with vLLM's recurrent verifier, plus CuTe-DSL recurrent prefill on B200/B300 and SM120. The experimental `RecurrentKDAPrefillWrapper`

supports planning and graph-safe prefix checkpoints. Qwen 3.6 gains experimental fused GDN decode steps on SM120 that combine projection, convolution, gating, and recurrent state updates. Nemotron-H gains source-built Mamba SSD-combined and selective-state-update backends on B200/GB300.

**Diffusion and video attention on Blackwell**

Video Sparse Attention gains generated SM100/SM103 kernels, and the block-64 path adds a native CuTe-DSL implementation with Sage FP8 support. SM120 gains a generated Sage block-sparse backend and an optimized NVFP4 attention path for Cosmos workloads. MiniMax-H3 gains a prepared MXFP8 pre-attention pipeline on B200/B300, while PrimTS block-sparse attention adds proxy compensation for Sol-Attn workloads.

**Communication for PCIe and NVLink deployments**

`PcieIpcAllReduceWorkspace`

adds an intra-node CUDA-IPC all-reduce for two, four, or eight ranks on PCIe machines without NVLink. Blackwell fused all-gather matmul gains a `backend="cake"`

option and a prepared callable for packed-QKV workloads, with tensor parallelism up to eight GPUs.

**Notice: packaging and dependencies**

`flashinfer-jit-cache`

is now a small shim that depends on architecture-specific provider wheels. The usual installation command installs the provider set for the selected CUDA and CPU platform; to reduce image size, install only the provider needed for your GPU. If you mirror or vendor wheels, include the provider wheels as well as the shim, and keep their CUDA-specific versions aligned.

| Dependency | 0.6.18.post1 | 0.7.0 |
|---|---|---|
`nvidia-cudnn-frontend` |
`>=1.25.0` |
`>=1.29.0` |
`apache-tvm-ffi` |
`>=0.1.6,!=0.1.8,!=0.1.8.post0,<0.2` |
`>=0.1.11,<0.2` |
| NCCL-EP Python packages | `nccl4py>=0.3.1` |
`nccl4py>=0.4.1` and `nccl-extensions>=0.1.0` |
`nvidia-cutlass-dsl` through `[cu12]` / `[cu13]` |
`>=4.6.2a0` |
`>=4.7.0a0` |

The base `nvidia-cutlass-dsl`

requirement remains `>=4.6.2a0`

; the CUDA extras have the higher floor. Environments pinned to CUTLASS DSL 4.6.2 need compatible dependency pins before installing those extras.

**Notice: small-batch FP8 groupwise GEMM**


⚠️ The CUTLASS`gemm_fp8_nt_groupwise`

path on SM100/SM103 can intermittently produce incorrect output for`M <= 32`

with`scale_granularity_mnk=(1, 128, 128)`

. This pre-existing issue remains in 0.7.0; see[#4396]for the investigation. Validate affected workloads before deployment. A different backend requires its own supported shapes and scale layout; there is no documented switch to disable only this CUTLASS fast path.

**Notice: API removals and behavior changes**

Update callers of the removed APIs before upgrading:

| Removed | Replacement |
|---|---|
`comm.trtllm_custom_all_reduce` |
`comm.trtllm_allreduce_fusion` |
`comm.trtllm_create_ipc_workspace_for_all_reduce` |
`comm.trtllm_create_ipc_workspace_for_all_reduce_fusion` |
`BatchDecodeMlaWithPagedKVCacheWrapper` |
`mla.BatchMLAPagedAttentionWrapper` |
No-op `end_forward()` methods on dec... |

[Read more](https://github.com/flashinfer-ai/flashinfer/releases/tag/v0.7.0)

## Release v0.7.0rc4

## Release v0.7.0rc3

## Release v0.6.18.post1

**Full Changelog**: `v0.6.18...v0.6.18.post1`

## Release v0.6.18

*These highlights are also published at flashinfer.ai/releases.*

### v0.6.18 Highlights

This release completes NVIDIA Rubin (SM107) support, brings whole-layer expert-parallel MoE to Hopper, adds decode paths for DeepSeek-V4 sparse attention and Kimi K3 linear attention, and broadens low-precision MoE coverage with MXFP4 on Blackwell RTX PRO and DGX Spark and weight-only W4A16 on B200 and B300.

**SM107 (Rubin) support**

FlashInfer 0.6.18 completes support for NVIDIA Rubin (SM107), begun in 0.6.16. Rubin devices now dispatch through the same unified APIs as Blackwell — attention, GEMM, MoE, and quantization.

Attention gains trtllm-gen FMHA for SM107, including sparse compression and FP16 softmax. The PrimTS attention path accepts Rubin as well. On the GEMM side, batched and low-latency GEMM both run on Rubin, and CUTLASS NVFP4 SVDQuant is enabled. A CuTe-DSL kernel family specialized for Rubin ships alongside them. trtllm-gen MoE now selects valid tactics on Rubin, and router GEMM and topk_varlen accept SM107.

**Expert-parallel MoE runs whole-layer on Hopper**

The `moe_ep`

mega-kernel stack was Blackwell-only. Two Hopper FP8 backends, `Sm90PullFp8MegaMoeConfig`

and `Sm90PushFp8MegaMoeConfig`

, now let Hopper deployments run dispatch, FC1, SwiGLU, FC2, and combine as one fused layer behind the existing `MoEEpLayer`

, instead of composing an NCCL all-to-all with a local fused-MoE operator. The pull backend reaches 562 TFLOPS/rank at a 384-expert DeepSeek-class geometry. The push backend supports CUDA Graph capture, and its opt-in fused FC1 epilogue drops an approximately 1 GiB per-rank activation buffer at the DeepSeek-V3 EP8 shape. Its grouped GEMM requires CUDA Toolkit 12.8 or newer.

**HCA decode backend and top-K selection for DeepSeek-V4**

Sparse attention picks the top-K KV positions per request on every decode step, then attends over the compressed cache; both halves now have dedicated paths. FP8 Heavily Compressed Attention (HCA) arrives for SM100/SM103 via `trtllm_batch_decode_sparse_mla_dsv4(..., backend="cute-dsl")`

, taking arbitrary sliding-window row order including ring rotation and wraparound while keeping the compressed cache paged. The new `flashinfer.top_k_varlen`

handles ragged batches through a Blackwell radix kernel, a guess-verify-refine kernel that warm-starts from the previous step's indices, and a CUTLASS fallback for any GPU. SM120/121 also picks up top-k 192 and 256.

**Kimi K3 decode fuses into one Blackwell kernel**

`flashinfer.fused_kda_decode`

folds Kimi K3's width-four depthwise causal convolution, SiLU, recurrent Kimi Delta Attention update, and gated RMSNorm into a single SM100 launch, covering the production head_dim 128 shapes at 12, 24, 48, and 96 heads and updating the convolution cache and FP32 state in place. On B200 under CUDA Graphs it is 1.33x the vLLM fused kernel at one row (table geomean 1.13x). A T=1 fast path inside `recurrent_kda`

and shared SM100-family recurrent kernels round out the KDA stack.

**MXFP4 MoE and video sparse attention on Blackwell RTX PRO**

MXFP4 checkpoints run natively on SM120/121: `b12x_fused_moe`

and `B12xMoEWrapper`

accept `quant_mode="mxfp4"`

across the existing fused schedules including CUDA Graph reuse, the b12x dense GEMM gains the matching path, and on an RTX PRO 6000 Blackwell Server Edition MXFP4 tracks NVFP4 against a strict quantized reference. Video Sparse Attention, until now datacenter-Blackwell only, reaches these parts through a `vsa_sm120_blk64`

backend on `BlockSparseAttentionWrapper`

. Gemma 4 gains asymmetric VO-split NVFP4 paged prefill on SM120/121.

**W4A16 MoE and dense GEMM extend to B200 and B300**

Weight-only NVFP4 against BF16 activations, which 0.6.14 shipped for SM12x, now runs on the SM100 family: `CuteDslMoEWrapper`

and `cute_dsl_fused_moe_nvfp4`

accept `quant_mode="w4a16"`

, decoding weights to BF16 inside the kernel so no separate activation-quantization or repack launch is needed, and `mm_bf16_fp4`

gains a dedicated SM100/SM103 kernel. Consuming BF16 directly pays off where MoE decode is memory-bound: at a DeepSeek EP8 shape on B200, W4A16 is 1.50x the W4A4 baseline at one token; W4A4 still wins large-batch prefill. GeGLU-tanh and SiTU are supported.

**Unified MoE API adds shared experts, MXINT4, and CUTLASS runners**

Shared experts now work through the unified API rather than low-level kernel entry points, via `ExpertConfig.num_fused_shared_experts`

on the block-FP8 and FP4 runners, completing in the unified API what 0.6.15 and 0.6.17 added for FP8 and FP4. The API also gains MXINT4, CUTLASS BF16 and W4A16 runners on SM90, packed per-tensor FP8 routing, BF16 `FromLogits`

routing, and `TopKSigmoid`

.

**Fused MNNVL all-reduce tail for tensor-parallel MoE**

`allreduce_fusion`

gains a BF16 Blackwell CuTe-DSL backend for the latency-critical tail of tensor-parallel MoE layers, fusing all-reduce, residual add, and RMSNorm, optionally preceded by MoE finalize and shared-expert add, over MNNVL/NVLink multicast. One backend spans decode to prefill by switching protocol with token count, with initial profiles targeting GB300 on TP8 and TP16.

**Smaller JIT-cache wheels; SM75 and single-request FA2 are JIT-only**

The `flashinfer-jit-cache`

wheels no longer ship precompiled kernels for SM75 (Turing). Those GPUs still run; the kernels compile on first use. CUDA 13 AArch64 wheels also drop native SM121a cubins (DGX Spark keeps running via SM120 family cubins), and the single-request `single_decode_with_kv_cache`

/ `single_prefill_with_kv_cache`

FA2 modules are no longer AOT-prebuilt — those APIs still JIT. Fatbins use size-oriented compression.

| 0.6.17 | 0.6.18 | |
|---|---|---|
| cu129 x86_64 | 1.94 GB | 1.02 GB |
| cu130 x86_64 | 1.51 GB | 1.02 GB |
| cu130 aarch64 | 1.69 GB | 1.13 GB |

## What's Changed

- test(moe): add tests for trtllm-gen fused MoE with GeGLU activation by
[@Aneureka](https://github.com/Aneureka)in[#4265](https://github.com/flashinfer-ai/flashinfer/pull/4265) - perf: optimize trtllm_fmha_v2 fp8 causal attention q-tile scheduling & decoding for uniform seqlen by
[@akhilg-nv](https://github.com/akhilg-nv)in[#3575](https://github.com/flashinfer-ai/flashinfer/pull/3575) - docs: improve Ulysses communicator and MoE EP docs by
[@kangbintNV](https://github.com/kangbintNV)in[#4240](https://github.com/flashinfer-ai/flashinfer/pull/4240) - fix(docker): stop pip from swapping the +cuXXX torch in CI image by
[@bkryu](https://github.com/bkryu)in[#4284](https://github.com/flashinfer-ai/flashinfer/pull/4284) - fix: skip LogitsTransform on lanes beyond the split-KV chunk boundary in FA2 kernels by
[@yichengj0](https://github.com/yichengj0)in[#3890](https://github.com/flashinfer-ai/flashinfer/pull/3890) - fix(test): repair main CI regressions from
[#4280](https://github.com/flashinfer-ai/flashinfer/pull/4280)(artifacts Rubin pins + CuTe-DSL MoE device guard) by[@bkryu](https://github.com/bkryu)in[#4301](https://github.com/flashinfer-ai/flashinfer/pull/4301) - fix: preserve DeepSeek no-group sigmoid routing weights by
[@alexeldeib](https://github.com/alexeldeib)in[#3875](https://github.com/flashinfer-ai/flashinfer/pull/3875) - fix(gdn): use block-end decay for SM100 state updates by
[@guangyunh-nv](https://github.com/guangyunh-nv)in[#4311](https://github.com/flashinfer-ai/flashinfer/pull/4311) - feat(cake_kda): add optimized B200 recurrent prefill backend by
[@yyihuang](https://github.com/yyihuang)in[#4262](https://github.com/flashinfer-ai/flashinfer/pull/4262) - feat(cake_kda): add optimized B200 recurrent decode backend by
[@yyihuang](https://github.com/yyihuang)in[#4279](https://github.com/flashinfer-ai/flashinfer/pull/4279) - test: Add sharding support to scripts/task_run_unit_tests.sh by
[@righthandabacus](https://github.com/righthandabacus)in[#4141](https://github.com/flashinfer-ai/flashinfer/pull/4141) - test(msa_ops): fix stale split-K heuristic expectation on high-SM GPUs by
[@jimmyzho](https://github.com/jimmyzho)in[#4303](https://github.com/flashinfer-ai/flashinfer/pull/4303) - perf(moe): sync SM12x NVFP4 fused-MoE kernels to b12x HEAD by
[@yichengj0](https://github.com/yichengj0)in[#4285](https://github.com/flashinfer-ai/flashinfer/pull/4285) - feat(moe): sync SM12x W4A16 fused MoE family to b12x HEAD by
[@yichengj0](https://github.com/yichengj0)in[#4255](https://github.com/flashinfer-ai/flashinfer/pull/4255) - fix: support fp8 e5m2 output in rmsnorm_quant and fused_add_rmsnorm_quant by
[@elwhyjay](https://github.com/elwhyjay)in[#4202](https://github.com/flashinfer-ai/flashinfer/pull/4202) - feat(moe): add packed per-tensor FP8 and BF16 FromLogits routing to unified MoE API by
[@feih-nv](https://github.com/feih-nv)in[#4227](https://github.com/flashinfer-ai/flashinfer/pull/4227) - perf: remove dead cudaGetDeviceProperties in sm120 groupwise GEMM by
[@aws-jiadingg](https://github.com/aws-jiadingg)in[https://github.com/flashinfer-ai/fla](https://github.com/flashinfer-ai/fla)...

[Read more](https://github.com/flashinfer-ai/flashinfer/releases/tag/v0.6.18)

## Nightly Release v0.6.18-20260819

Automated nightly build for version 0.6.18 (dev20260819)

## Nightly Release v0.6.18-20260818

Automated nightly build for version 0.6.18 (dev20260818)

## Nightly Release v0.6.18-20260817

Automated nightly build for version 0.6.18 (dev20260817)

## Nightly Release v0.6.18-20260816

Automated nightly build for version 0.6.18 (dev20260816)

## Nightly Release v0.6.18-20260814

Automated nightly build for version 0.6.18 (dev20260814)