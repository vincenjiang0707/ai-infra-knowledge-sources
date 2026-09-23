# DeepGEMM

source: https://github.com/flashinfer-ai/flashinfer/releases

# Releases: flashinfer-ai/flashinfer

## Release list

## Release v0.7.0

## What's Changed

- fix(sampling): reject unsafe multi-CTA top-k launches on low-SM GPUs by
[@bkryu](https://github.com/bkryu)in[#4595](https://github.com/flashinfer-ai/flashinfer/pull/4595) - feat(cake_kda): optimize small-BH recurrent-KDA prefill by
[@yyihuang](https://github.com/yyihuang)in[#4571](https://github.com/flashinfer-ai/flashinfer/pull/4571) - test: enable the unified MoE fuzzer by default and prune legacy UTs by
[@feih-nv](https://github.com/feih-nv)in[#4475](https://github.com/flashinfer-ai/flashinfer/pull/4475) - feat(gdn): add pooled state and state checkpointing and dtype support for feature parity by
[@guangyunh-nv](https://github.com/guangyunh-nv)in[#4436](https://github.com/flashinfer-ai/flashinfer/pull/4436) - feat(attention): add PrimTS Q64/KV256 and paged GQA block-sparse attention by
[@heyuhhh](https://github.com/heyuhhh)in[#4474](https://github.com/flashinfer-ai/flashinfer/pull/4474) - add backward-compatible aliases for bsa_attn_fwd and bsa_attn_blk64_fwd by
[@hsr1234563](https://github.com/hsr1234563)in[#4590](https://github.com/flashinfer-ai/flashinfer/pull/4590) - fix(moe): restore SM12x MoE kernels broken by self-resolved helper in borrowed dense methods by
[@lucifer1004](https://github.com/lucifer1004)in[#4602](https://github.com/flashinfer-ai/flashinfer/pull/4602) - Add
[@Anerudhan](https://github.com/Anerudhan)to CODEOWNERS for core review by[@aleozlx](https://github.com/aleozlx)in[#4622](https://github.com/flashinfer-ai/flashinfer/pull/4622) - fix(moe_ep): fix in_kernel_fc2_reduce livelock on zero-token launches (MXFP8 + NVFP4) by
[@mhoqueanik](https://github.com/mhoqueanik)in[#4531](https://github.com/flashinfer-ai/flashinfer/pull/4531) - feat(moe_ep): SM100 BF16 CuTeDSL MegaMoE kernel by
[@mhoqueanik](https://github.com/mhoqueanik)in[#4386](https://github.com/flashinfer-ai/flashinfer/pull/4386) - feat: CuTe DSL kernels for Rubin (SM107) and batched FP8 GEMM for Blackwell by
[@Vinnie6167](https://github.com/Vinnie6167)in[#4526](https://github.com/flashinfer-ai/flashinfer/pull/4526) - Add back TRTLLM Gen MoE split-K by
[@jiahanc](https://github.com/jiahanc)in[#4617](https://github.com/flashinfer-ai/flashinfer/pull/4617) - feat(kda): add CuTe DSL recurrent prefill backend by
[@Observer007](https://github.com/Observer007)in[#4605](https://github.com/flashinfer-ai/flashinfer/pull/4605) - feat(cake_backend): accelerate DeepSeek fused routing by
[@yyihuang](https://github.com/yyihuang)in[#4587](https://github.com/flashinfer-ai/flashinfer/pull/4587) - Stop legacy nightly release publishing by
[@dierksen](https://github.com/dierksen)in[#4623](https://github.com/flashinfer-ai/flashinfer/pull/4623) - feat(cake_backend): add Blackwell Router GEMM by
[@yyihuang](https://github.com/yyihuang)in[#4594](https://github.com/flashinfer-ai/flashinfer/pull/4594) - [feat]custom all reduce kernel by
[@qsang-nv](https://github.com/qsang-nv)in[#4393](https://github.com/flashinfer-ai/flashinfer/pull/4393) - fix(attention): handle extreme negative logits in masked softmax by
[@shoutoutuoadi325](https://github.com/shoutoutuoadi325)in[#4401](https://github.com/flashinfer-ai/flashinfer/pull/4401) - feat: trtllm-gen FMHA features for sm107 (spcompress, fp16softmax) by
[@jimmyzho](https://github.com/jimmyzho)in[#4596](https://github.com/flashinfer-ai/flashinfer/pull/4596) - feat(moe_ep): SM100 W4A8 (MXFP8xMXFP4) CuTeDSL split kernel backend with MXFP8 packed dispatch by
[@mhoqueanik](https://github.com/mhoqueanik)in[#4529](https://github.com/flashinfer-ai/flashinfer/pull/4529) - Add Qwen fused GDN decode step for sm120 by
[@nv-yunzheq](https://github.com/nv-yunzheq)in[#4481](https://github.com/flashinfer-ai/flashinfer/pull/4481) - feat: collect a union of TEST_PATH targets in unit CI by
[@kahyunnam](https://github.com/kahyunnam)in[#4641](https://github.com/flashinfer-ai/flashinfer/pull/4641) - fix(moe): correct unified fuzzer references by
[@feih-nv](https://github.com/feih-nv)in[#4639](https://github.com/flashinfer-ai/flashinfer/pull/4639) - [perf] split TRT-LLM Gen routing kernels to reduce compile time by
[@jiahanc](https://github.com/jiahanc)in[#4635](https://github.com/flashinfer-ai/flashinfer/pull/4635) - feat(moe): add SiTU-GLU activation to the CUTLASS fused-MoE backend by
[@xuanyu-mistral](https://github.com/xuanyu-mistral)in[#4460](https://github.com/flashinfer-ai/flashinfer/pull/4460) - feat(cake_mamba): add Blackwell selective state update backend by
[@yyihuang](https://github.com/yyihuang)in[#4616](https://github.com/flashinfer-ai/flashinfer/pull/4616) - ci: consolidate CUDA coverage and validate candidate images by
[@dierksen](https://github.com/dierksen)in[#4469](https://github.com/flashinfer-ai/flashinfer/pull/4469) - feat(kda): add SM120a CuTe DSL prefill backend by
[@JimpleMa](https://github.com/JimpleMa)in[#4633](https://github.com/flashinfer-ai/flashinfer/pull/4633) - feat(moe): standalone trtllm-gen routing op + decomposed tests/moe routing matrix by
[@aleozlx](https://github.com/aleozlx)in[#4082](https://github.com/flashinfer-ai/flashinfer/pull/4082) - feat(cake_vsa): add optimized SM100/SM103 block-sparse attention (VSA) by
[@yyihuang](https://github.com/yyihuang)in[#4593](https://github.com/flashinfer-ai/flashinfer/pull/4593) - feat(cake_kda): add paired recurrent training for SM100a and SM103a by
[@yyihuang](https://github.com/yyihuang)in[#4636](https://github.com/flashinfer-ai/flashinfer/pull/4636) - perf(gemm): optimize CuTe DSL W4A16 dense GEMM by
[@zianglih](https://github.com/zianglih)in[#4686](https://github.com/flashinfer-ai/flashinfer/pull/4686) - fix(sm120): align MXFP8 plain tactic and FP8 moe stage policy by
[@CarstyYou](https://github.com/CarstyYou)in[#4660](https://github.com/flashinfer-ai/flashinfer/pull/4660) - feat(moe): align unified MoE do_finalize behavior with flat API by
[@feih-nv](https://github.com/feih-nv)in[#4614](https://github.com/flashinfer-ai/flashinfer/pull/4614) - perf(gdn): reduce non-CP CuTeDSL launch overhead by
[@guangyunh-nv](https://github.com/guangyunh-nv)in[#4699](https://github.com/flashinfer-ai/flashinfer/pull/4699) - feat(cake_mamba): add Blackwell Mamba SSDCombined by
[@yyihuang](https://github.com/yyihuang)in[#4576](https://github.com/flashinfer-ai/flashinfer/pull/4576) - feat: SM120 NVFP4 SVDQuant Gemm in CuteDSL by
[@rosenrodt](https://github.com/rosenrodt)in[#4420](https://github.com/flashinfer-ai/flashinfer/pull/4420) - ci: disable sccache for cu134 nvcc by
[@dierksen](https://github.com/dierksen)in[#4682](https://github.com/flashinfer-ai/flashinfer/pull/4682) - Add paged MQA logits (attn_scores) kernels for Blackwell SM100 by
[@dhiraj113](https://github.com/dhiraj113)in[#4365](https://github.com/flashinfer-ai/flashinfer/pull/4365) - perf(sm120): optimize NVFP4 attention with N64 score-slot reuse by
[@tiffany940107](https://github.com/tiffany940107)in[#4502](https://github.com/flashinfer-ai/flashinfer/pull/4502) - feat(cake_msa): add Blackwell minimax sparse attention source kernels by
[@yyihuang](https://github.com/yyihuang)in[#4355](https://github.com/flashinfer-ai/flashinfer/pull/4355) - perf(cake_kda): further optimize recurrent-KDA prefill on Blackwell by
[@yyihuang](https://github.com/yyihuang)in[#4675](https://github.com/flashinfer-ai/flashinfer/pull/4675) - feat(moe): allow B12xMoEWrapper to share pre-allocated workspaces by
[@lucifer1004](https://github.com/lucifer1004)in[#4603](https://github.com/flashinfer-ai/flashinfer/pull/4603) - (perf) add fused_GDN_step support for Qwen 3.6 35B A3B on sm120 by
[@nv-yunzheq](https://github.com/nv-yunzheq)in[#4708](https://github.com/flashinfer-ai/flashinfer/pull/4708) - fix: SageAttention support block size doesn't divide sequence; support K-smoothing by
[@xrq-phys](https://github.com/xrq-phys)in[#4654](https://github.com/flashinfer-ai/flashinfer/pull/4654) - ci: coordinate CUDA dependency policy by
[@dierksen](https://github.com/dierksen)in[#4711](https://github.com/flashinfer-ai/flashinfer/pull/4711) - perf(msa): chunked top-k and in-kernel causal offsets for the SM12x indexer by
[@yichengj0](https://github.com/yichengj0)in[#4030](https://github.com/flashinfer-ai/flashinfer/pull/4030) - perf(cake_kda): add recurrence-piece persistent M128 prefill by
[@yyihuang](https://github.com/yyihuang)in[#4728](https://github.com/flashinfer-ai/flashinfer/pull/4728) - feat(moe): add remaining CUTLASS unified MoE runners by
[@feih-nv](https://github.com/feih-nv)in[#4610](https://github.com/flashinfer-ai/flashinfer/pull/4610) - fix: Correctly wire scale_qkvo to cute-dsl fmha backends by
[@xrq-phys](https://github.com/xrq-phys)in[#4665](https://github.com/flashinfer-ai/flashinfer/pull/4665) - fix(kda): fall back to Cake when CuTe DSL predates cutlass.experimental by
[@kahyunnam](https://github.com/kahyunnam)in[#4667](https://github.com/flashinfer-ai/flashinfer/pull/4667) - fix(ci): skip source-only CUDA config test in nightlies by
[@dierksen](https://github.com/dierksen)in[#4750](https://github.com/flashinfer-ai/flashinfer/pull/4750) - perf(activation): cap act_and_mul_kernel block size for ~17-19% speedup at large hidden dims by
[@yekerr](https://github.com/yekerr)in[#4733](https://github.com/flashinfer-ai/flashinfer/pull/4733) - fix(fmha): select CGA reduction for MLA H512 decode by
[@yihwang-nv](https://github.com/yihwang-nv)in[#4702](https://github.com/flashinfer-ai/flashinfer/pull/4702) - feat(norm): fused Add+RMSNorm+1x128 fp8 block-quant producer by
[@NVShreyas](https://github.com/NVShreyas)in[#4480](https://github.com/flashinfer-ai/flashinfer/pull/4480) - chore(aot): exclude single prefill/decode modules from jit-cache prebuilds by
[@bkryu](https://github.com/bkryu)in[#4760](https://github.com/flashinfer-ai/flashinfer/pull/4760) - build(jit): reduce JIT-cache wheel size by
[@dierksen](https://github.com/dierksen)in[#4757](https://github.com/flashinfer-ai/flashinfer/pull/4757) - feat(moe): add unified activation parity by
[@feih-nv](https://github.com/feih-nv)in[#4613](https://github.com/flashinfer-ai/flashinfer/pull/4613) - Support per-token NVFP4 ReLU2 MoE by
[@xuantengh](https://github.com/xuantengh)in[#4618](https://github.com/flashinfer-ai/flashinfer/pull/4618) - feat: CUB
`DeviceBatchedTopK`

top-k backend with variable-length support by[@NaderAlAwar](https://github.com/NaderAlAwar)in[#4442](https://github.com/flashinfer-ai/flashinfer/pull/4442) - feat(cake_fmha): add native Blackwell DCP speculative decode by
[@yyihuang](https://github.com/yyihuang)in[#4518](https://github.com/flashinfer-ai/flashinfer/pull/4518) - fix(cute_dsl): consult the arch gate in the GEMM and GDN dispatchers by
[@Vinnie6167](https://github.com/Vinnie6167)in[#4649](https://github.com/flashinfer-ai/flashinfer/pull/4649) - feat(cake_activation): add fused Blackwell SwiGLU MXFP8 quantization by
[@yyihuang](https://github.com/yyihuang)in[#4638](https://github.com/flashinfer-ai/flashinfer/pull/4638) - Adding var-window FMHA context support for PrimsTS. by
[@mingxu1067](https://github.com/mingxu1067)in[#4599](https://github.com/flashinfer-ai/flashinfer/pull/4599) - Add bias support to cublast gemm backend and as fallback backend for cutedsl gemm backend by
[@jiahanc](https://github.com/jiahanc)in[#4772](https://github.com/flashinfer-ai/flashinfer/pull/4772) - misc: multi-arch cubins (sm100, 103, 107) in a single artifact by
[@jimmyzho](https://github.com/jimmyzho)in[#4648](https://github.com/flashinfer-ai/flashinfer/pull/4648) - refactor(mla): isolate planned FA2, FA3, and CUTLASS backends by
[@saltyminty](https://github.com/saltyminty)in[#4697](https://github.com/flashinfer-ai/flashinfer/pull/4697) - Enable CuTe DSL MLA benchmarks for low head counts by
[@lunarz-dev](https://github.com/lunarz-dev)in[#4656](https://github.com/flashinfer-ai/flashinfer/pull/4656) - fix(gemm): never move the shared cuDNN GEMM workspace by
[@yanqinz2](https://github.com/yanqinz2)in[#4666](https://github.com/flashinfer-ai/flashinfer/pull/4666) - feat(cake_kda): add recurrent training template dispatch by
[@yyihuang](https://github.com/yyihuang)in[#4726](https://github.com/flashinfer-ai/flashinfer/pull/4726) - fix(norm): limit add RMSNorm FP4 launch config heuristics to SM100 and SM103 by
[@soodoshll](https://github.com/soodoshll)in[#4494](https://github.com/flashinfer-ai/flashinfer/pull/4494) - perf(cake_vsa): refresh Blackwell block-sparse WS kernel by
[@yyihuang](https://github.com/yyihuang)in[#4804](https://github.com/flashinfer-ai/flashinfer/pull/4804) - feat(decode): add prims-ts backend and is_causal to paged decode by
[@elwhyjay](https://github.com/elwhyjay)in[#4739](https://github.com/flashinfer-ai/flashinfer/pull/4739) - [Bugfix] Skip .item() readback for trtllm_ragged_attention_deepseek during CUDA graph capture (
[#4609](https://github.com/flashinfer-ai/flashinfer/issues/4609)) by[@zhang-keliang](https://github.com/zhang-keliang)in[#4703](https://github.com/flashinfer-ai/flashinfer/pull/4703) - feat(cake_comm): Add a Cake Black...

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