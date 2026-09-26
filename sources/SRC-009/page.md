source: https://github.com/vllm-project/vllm-ascend/releases

# Releases: vllm-project/vllm-ascend

## Release list

## v0.23.0.post1

## v0.23.0.post1 - 2026.09.21

This is the first post release of vLLM Ascend v0.23.0. It includes the fixes, dependency updates, CI changes, and documentation updates merged into the v0.23.0 release branch after the v0.23.0 tag. Please follow the [official documentation](https://docs.vllm.ai/projects/ascend/en/v0.23.0/) to get started.

### Bug Fixes

- Fixed stale KV-cache writes during DP-aligned dummy runs by invalidating per-KV-group slot mappings before attention metadata construction.
[#15362](https://github.com/vllm-project/vllm-ascend/pull/15362) - Fixed MTP overlay prefix-cache precision on Atlas 300I DUO and kept W8A8 MXFP8 transformed buffers stable across RL weight reloads in ACL Graph mode.
[#14336](https://github.com/vllm-project/vllm-ascend/pull/14336)[#13905](https://github.com/vllm-project/vllm-ascend/pull/13905)

### Other Changes

- Pinned the KV Pool dependencies to
`memfabric_hybrid==1.2.0`

and`memcache_hybrid==1.2.0`

.[#14352](https://github.com/vllm-project/vllm-ascend/pull/14352) - Consolidated installation guidance, GLM-5/5.2 and Kimi-K3 deployment instructions, PD and 310P notes, release metadata, navigation titles, English comments, and Chinese translations.
[#15449](https://github.com/vllm-project/vllm-ascend/pull/15449)[#14242](https://github.com/vllm-project/vllm-ascend/pull/14242)[#14338](https://github.com/vllm-project/vllm-ascend/pull/14338)[#14634](https://github.com/vllm-project/vllm-ascend/pull/14634)[#14698](https://github.com/vllm-project/vllm-ascend/pull/14698)[#14713](https://github.com/vllm-project/vllm-ascend/pull/14713)[#14906](https://github.com/vllm-project/vllm-ascend/pull/14906)[#15998](https://github.com/vllm-project/vllm-ascend/pull/15998)[#16106](https://github.com/vllm-project/vllm-ascend/pull/16106)[#14382](https://github.com/vllm-project/vllm-ascend/pull/14382)[#14387](https://github.com/vllm-project/vllm-ascend/pull/14387)[#14436](https://github.com/vllm-project/vllm-ascend/pull/14436)[#14579](https://github.com/vllm-project/vllm-ascend/pull/14579)[#14684](https://github.com/vllm-project/vllm-ascend/pull/14684)[#15534](https://github.com/vllm-project/vllm-ascend/pull/15534)[#16202](https://github.com/vllm-project/vllm-ascend/pull/16202) - Added release-branch nightly and weekly model configurations and installed
`concurrent-log-handler`

in release images.[#14559](https://github.com/vllm-project/vllm-ascend/pull/14559)[#14645](https://github.com/vllm-project/vllm-ascend/pull/14645)[#14739](https://github.com/vllm-project/vllm-ascend/pull/14739)[#16191](https://github.com/vllm-project/vllm-ascend/pull/16191)

## v0.26.0rc1

## v0.26.0rc1 - 2026.09.03

This is the first release candidate of v0.26.0 for vLLM Ascend, aligned with upstream vLLM v0.26.0. This release is a model‑restricted version. Fully validated models include Kimi K3, GLM‑5.2, DeepSeek V4 Flash 0731, DeepSeek V4 Pro 0813. Availability is not guaranteed for other models. For the full test report, see: [v0.26.0rc1 Test Conclusion](https://github.com/vllm-project/vllm-ascend/blob/releases/v0.26.0rc/tests/vllm_ascend_v0.26.0rc1_test_conclusion.md). Please follow the [official documentation](https://docs.vllm.ai/projects/ascend/en/v0.26.0rc1/) to get started.

### Highlights

**Kimi K3 on Ascend**: Added end-to-end Kimi K3 support, including MLA DSpark speculative decoding, no-RoPE MLAPO on Ascend 950, fused QKV projections, fused norm gate and attention residual, and projector rotation.[#12950](https://github.com/vllm-project/vllm-ascend/pull/12950)[#13277](https://github.com/vllm-project/vllm-ascend/pull/13277)[#13507](https://github.com/vllm-project/vllm-ascend/pull/13507)[#13989](https://github.com/vllm-project/vllm-ascend/pull/13989)[#13509](https://github.com/vllm-project/vllm-ascend/pull/13509)[#14231](https://github.com/vllm-project/vllm-ascend/pull/14231)**GLM-5.2 / DeepSeek V4 Flash 0731 / DeepSeek V4 Pro 0813 accuracy and performance**: Resolved GLM-5.2 DSpark acceptance regressions and DeepSeek V4 Flash-0731 / Pro-0813 accuracy issues (reasoning-effort alignment, routed SwiGLU limit, and frontend behavior), and reused DSV4 compressor metadata across layers for better performance.[#12262](https://github.com/vllm-project/vllm-ascend/pull/12262)[#13531](https://github.com/vllm-project/vllm-ascend/pull/13531)[#13993](https://github.com/vllm-project/vllm-ascend/pull/13993)[#14074](https://github.com/vllm-project/vllm-ascend/pull/14074)[#14397](https://github.com/vllm-project/vllm-ascend/pull/14397)[#14624](https://github.com/vllm-project/vllm-ascend/pull/14624)[#14994](https://github.com/vllm-project/vllm-ascend/pull/14994)**DeepSeek V4 DSpark**: Refactored DSv4 DSpark speculative decoding with aligned SP handling and QuaRot weight support for Qwen3 DSpark.[#11431](https://github.com/vllm-project/vllm-ascend/pull/11431)[#12662](https://github.com/vllm-project/vllm-ascend/pull/12662)**Sparse-attention context parallelism**: Added SFA DCP with a replicated indexer, compact KV gather, and C8 support. Enabled P/D disaggregation for DCP with replicate-indexer.[#11443](https://github.com/vllm-project/vllm-ascend/pull/11443)[#11870](https://github.com/vllm-project/vllm-ascend/pull/11870)[#11980](https://github.com/vllm-project/vllm-ascend/pull/11980)[#11696](https://github.com/vllm-project/vllm-ascend/pull/11696)**Deprecation cleanup**: Removed layer sharding, FlashComm2, multistream overlap gate, dynamic-batch SLO, weight prefetch, matmul all-reduce fusions, and kv offload in KV Pool to streamline the codebase.[#11953](https://github.com/vllm-project/vllm-ascend/pull/11953)[#12117](https://github.com/vllm-project/vllm-ascend/pull/12117)[#11956](https://github.com/vllm-project/vllm-ascend/pull/11956)[#11933](https://github.com/vllm-project/vllm-ascend/pull/11933)[#11949](https://github.com/vllm-project/vllm-ascend/pull/11949)[#12119](https://github.com/vllm-project/vllm-ascend/pull/12119)[#11904](https://github.com/vllm-project/vllm-ascend/pull/11904)

### Features

- Added LoRA with unquantized MoE models and AlltoAll + EP + LoRA support.
[#10977](https://github.com/vllm-project/vllm-ascend/pull/10977)[#12451](https://github.com/vllm-project/vllm-ascend/pull/12451) - Added Gemma4 E2B and E4B model support with graph execution on A2/A3 and ModelSlim quantization.
[#11536](https://github.com/vllm-project/vllm-ascend/pull/11536)[#11575](https://github.com/vllm-project/vllm-ascend/pull/11575)[#11791](https://github.com/vllm-project/vllm-ascend/pull/11791) - Added Step3.5/3.7 Flash support for Ascend 950.
[#10556](https://github.com/vllm-project/vllm-ascend/pull/10556) - Added KV sliding window for Eagle3 and DFlash.
[#10023](https://github.com/vllm-project/vllm-ascend/pull/10023) - Added ShortRequestFirst scheduling and batch job aware scheduler.
[#11576](https://github.com/vllm-project/vllm-ascend/pull/11576)[#12240](https://github.com/vllm-project/vllm-ascend/pull/12240)[#12719](https://github.com/vllm-project/vllm-ascend/pull/12719) - Added NZ static buffers for prefetch offload.
[#11945](https://github.com/vllm-project/vllm-ascend/pull/11945) - Added update config and reload weights to NPU Worker.
[#10126](https://github.com/vllm-project/vllm-ascend/pull/10126) - Added SFA C8 support: unified packed KV cache layout on A3, and DCP replicated indexer for sparse‑attention paths.
[#11228](https://github.com/vllm-project/vllm-ascend/pull/11228)[#11870](https://github.com/vllm-project/vllm-ascend/pull/11870)

### Hardware and Operator Support

- Expanded Ascend 950 supports: MXFP quant for token dispatch, and CPU binding with topo clusters.
[#11614](https://github.com/vllm-project/vllm-ascend/pull/11614)[#11717](https://github.com/vllm-project/vllm-ascend/pull/11717) - Expanded Atlas 300I DUO support: disabled npugraph_ex by default, added Qwen3.5-Dense documentation, and fixed 310P spec decoding accuracy.
[#10874](https://github.com/vllm-project/vllm-ascend/pull/10874)[#12077](https://github.com/vllm-project/vllm-ascend/pull/12077)[#11918](https://github.com/vllm-project/vllm-ascend/pull/11918) - Added operator supports: KV quant sparse flash attention, and Triton SwiGLuStep kernel (replaced AscendC‑based fused_gdn_gating).
[#11626](https://github.com/vllm-project/vllm-ascend/pull/11626)[#11467](https://github.com/vllm-project/vllm-ascend/pull/11467)[#12035](https://github.com/vllm-project/vllm-ascend/pull/12035)

### Performance

Unless stated otherwise, these optimizations are selected automatically for the targeted path and need no additional configuration.

- Optimized PCP FA restore and output merge to reduce overhead.
[#11586](https://github.com/vllm-project/vllm-ascend/pull/11586) - Vectorized local sequence-length computation in SFA metadata to remove per-request NPU-to-CPU synchronization.
[#11762](https://github.com/vllm-project/vllm-ascend/pull/11762) - Avoided H2D synchronization in context-parallel speculative-proposer metadata.
[#11496](https://github.com/vllm-project/vllm-ascend/pull/11496) - Optimized DSA-CP local token metadata with a fused Triton kernel and caching.
[#12193](https://github.com/vllm-project/vllm-ascend/pull/12193) - Split mixed ChunkedPrefill into separate decode and prefill attention calls.
[#11948](https://github.com/vllm-project/vllm-ascend/pull/11948) - Optimized AscendStore key construction and miss-path handling.
[#12814](https://github.com/vllm-project/vllm-ascend/pull/12814) - Removed D2H sync in QLIMetadata builder for DSA-CP.
[#12536](https://github.com/vllm-project/vllm-ascend/pull/12536) - Bound Mooncake receiver threads to KV cache device.
[#12126](https://github.com/vllm-project/vllm-ascend/pull/12126) - Sharded DeepSeek V4 DSpark main projection across TP ranks for better parallelism.
[#15144](https://github.com/vllm-project/vllm-ascend/pull/15144) - Reused DeepSeek V4 compressor metadata across layers to avoid redundant computation.
[#14994](https://github.com/vllm-project/vllm-ascend/pull/14994)

### Dependencies

**Upstream vLLM**: v0.26.0.**Python**: >= 3.10, < 3.13.**CANN**: 9.1.0.**PyTorch / torch_npu**: 2.10.0 / 2.10.0.post4.**Triton Ascend**: 3.2.2 for A2, A3, and Ascend 950; Triton Ascend is not supported on Atlas 300I DUO.**Mooncake**: 0.3.11.post1 in the release images.

### Deprecation and Breaking Changes

- Removed layer sharding.
[#11953](https://github.com/vllm-project/vllm-ascend/pull/11953) - Removed FlashComm2 optimization techniques.
[#12117](https://github.com/vllm-project/vllm-ascend/pull/12117) - Removed multistream overlap gate.
[#11956](https://github.com/vllm-project/vllm-ascend/pull/11956) - Removed dynamic-batch SLO.
[#11933](https://github.com/vllm-project/vllm-ascend/pull/11933) - Removed weight prefetch config.
[#11949](https://github.com/vllm-project/vllm-ascend/pull/11949) - Removed matmul all-reduce and matmul all-reduce RMSNorm fusions.
[#12119](https://github.com/vllm-project/vllm-ascend/pull/12119) - Removed KV offload in KV Pool.
[#11904](https://github.com/vllm-project/vllm-ascend/pull/11904) - Removed
`dp_allreduce_on_npu`

additional config option.[#12496](https://github.com/vllm-project/vllm-ascend/pull/12496) - Removed PCP from MRV1; use MRV2 for prefill context parallelism.
[#12592](https://github.com/vllm-project/vllm-ascend/pull/12592) - Removed custom top-k top-p AscendC implementation in favor of CANN operator.
[#12232](https://github.com/vllm-project/vllm-ascend/pull/12232) - Refactored hamming ops and removed sparse action.
[#12049](https://github.com/vllm-project/vllm-ascend/pull/12049) - Deprecated
`ASCEND_BUFFER_POOL`

environment variable; use`ASCEND_ENABLE_USE_FABRIC_MEM=1`

or`HCCL_INTRA_ROCE_ENABLE=1`

.[#13856](https://github.com/vllm-project/vllm-ascend/pull/13856)

### Ready to Deprecate

The following features are deprecated or subject to change:

- Added deprecation warnings for W4A8 linear, W4A8 MoE per-group, and W8A8 PDMix MoE quantization. These quantization paths will be removed in a future release.
[#13850](https://github.com/vllm-project/vllm-ascend/pull/13850) - The
`mega_moe_max_tokens`

and`enable_fused_mc2`

configurations in`additional-config`

will be moved into a new dedicated dict for centralized maintenance in the next release. - DeepSeek-V3, DeepSeek-V3.1, and DeepSeek-R1 model support will be removed in v0.28.0.
- The
`reduce sampling`

feature is experimental and will be deprecated in future releases. We will follow the upstream vLLM community for the`batch-sharded sampling`

feature.

### Documentation...

[Read more](https://github.com/vllm-project/vllm-ascend/releases/tag/v0.26.0rc1)

## v0.23.0

## v0.23.0 - 2026.08.16

We're excited to announce the official vLLM Ascend v0.23.0 release, aligned with upstream vLLM v0.23.0. This note summarizes the cumulative user-facing changes since the previous official release, v0.18.0, including the v0.19.1rc1, v0.20.2rc1, v0.21.0rc1, v0.22.1rc1, and v0.23.0rc1 development cycles. Please follow the [official documentation](https://docs.vllm.ai/projects/ascend/en/v0.23.0/) to get started.

PR references marked with **†** were merged into the v0.23.0 release branch after v0.23.0rc1.

### Highlights

**Ascend 950 and DeepSeek V4**: Added end-to-end DeepSeek V4 support on Ascend 950, including DSA attention, MTP, piecewise graph execution, distributed inference, sparse attention, CPU binding, and MXFP quantization and communication paths.[#9757](https://github.com/vllm-project/vllm-ascend/pull/9757)[#9935](https://github.com/vllm-project/vllm-ascend/pull/9935)[#10236](https://github.com/vllm-project/vllm-ascend/pull/10236)[#11014](https://github.com/vllm-project/vllm-ascend/pull/11014)**Model and hardware coverage**: Expanded support and deployment guidance for GLM-5.2, GLM-4.7-Flash, Qwen3.5/Qwen3.6, Qwen3-ASR, Qwen3-Omni, Bailing MoE, Gemma4, Step3, and MiniMax 2.x models across A2, A3, Ascend 950, and Atlas 300I DUO. GLM-5.2 supports long-sequence inference up to 1M tokens on Atlas 800 A3.[#8657](https://github.com/vllm-project/vllm-ascend/pull/8657)[#9560](https://github.com/vllm-project/vllm-ascend/pull/9560)[#10441](https://github.com/vllm-project/vllm-ascend/pull/10441)[#10697](https://github.com/vllm-project/vllm-ascend/pull/10697)[#11091](https://github.com/vllm-project/vllm-ascend/pull/11091)[#11264](https://github.com/vllm-project/vllm-ascend/pull/11264)[#12115](https://github.com/vllm-project/vllm-ascend/pull/12115)**Context parallelism and sparse attention**: Added SFA DCP with a replicated indexer, compact KV gather, C8 support, and device-side metadata paths for long-context and P/D-disaggregated deployments.[#9638](https://github.com/vllm-project/vllm-ascend/pull/9638)[#9809](https://github.com/vllm-project/vllm-ascend/pull/9809)[#11819](https://github.com/vllm-project/vllm-ascend/pull/11819)[#11871](https://github.com/vllm-project/vllm-ascend/pull/11871)[#11981](https://github.com/vllm-project/vllm-ascend/pull/11981)**KV-cache lifecycle and offload**: Added hybrid/Mamba attention prefix caching; CPU and SSD offload in AscendStore that covers all backends.[#8743](https://github.com/vllm-project/vllm-ascend/pull/8743)[#9533](https://github.com/vllm-project/vllm-ascend/pull/9533)[#9731](https://github.com/vllm-project/vllm-ascend/pull/9731)[#10393](https://github.com/vllm-project/vllm-ascend/pull/10393)**Graph and speculative execution**: Added`FULL_AND_PIECEWISE`

graph mode, which is enabled by default and requires no manual configuration; DFlash`FULL_DECODE_ONLY`

; zero-bubble async scheduling; P-Eagle and PARD; and expanded MTP/Eagle3 support.[#7640](https://github.com/vllm-project/vllm-ascend/pull/7640)[#8118](https://github.com/vllm-project/vllm-ascend/pull/8118)[#9572](https://github.com/vllm-project/vllm-ascend/pull/9572)[#10042](https://github.com/vllm-project/vllm-ascend/pull/10042)[#10566](https://github.com/vllm-project/vllm-ascend/pull/10566)

### Features

- Added multimodal DFlash, FlashComm support for Qwen VL/MoE models, and PCP-aware multimodal reasoning.
[#7486](https://github.com/vllm-project/vllm-ascend/pull/7486)[#7897](https://github.com/vllm-project/vllm-ascend/pull/7897)[#8038](https://github.com/vllm-project/vllm-ascend/pull/8038)[#9340](https://github.com/vllm-project/vllm-ascend/pull/9340) - Added HCCL weight transfer for reinforcement-learning workloads and D2D NetLoader support for speculative draft models.
[#9152](https://github.com/vllm-project/vllm-ascend/pull/9152)[#9893](https://github.com/vllm-project/vllm-ascend/pull/9893) - Expanded Model Runner V2 with initial MoE and Eagle support.
[#7885](https://github.com/vllm-project/vllm-ascend/pull/7885)[#7922](https://github.com/vllm-project/vllm-ascend/pull/7922) - Expanded EPLB with additional observability and dynamic load-balancer examples.
[#9536](https://github.com/vllm-project/vllm-ascend/pull/9536)[#10627](https://github.com/vllm-project/vllm-ascend/pull/10627) - Extended C8 INT8 KV cache to sparse-attention paths with packed layouts and a DCP replicated indexer, and added W8A8FP8 and W4A16 MXFP quantization paths for Ascend 950.
[#10236](https://github.com/vllm-project/vllm-ascend/pull/10236)[#11014](https://github.com/vllm-project/vllm-ascend/pull/11014)[#11846](https://github.com/vllm-project/vllm-ascend/pull/11846)[#11871](https://github.com/vllm-project/vllm-ascend/pull/11871)

### Hardware and Operator Support

- Added and optimized recurrent GDN, causal Conv1D, sparse-attention, LightningIndexer, compressor, and fused quantization operators.
[#7798](https://github.com/vllm-project/vllm-ascend/pull/7798)[#7926](https://github.com/vllm-project/vllm-ascend/pull/7926)[#9382](https://github.com/vllm-project/vllm-ascend/pull/9382)[#9491](https://github.com/vllm-project/vllm-ascend/pull/9491)[#9825](https://github.com/vllm-project/vllm-ascend/pull/9825)[#10730](https://github.com/vllm-project/vllm-ascend/pull/10730) - Expanded Atlas 300I DUO support for Qwen3.5, Qwen3.6, Qwen3-ASR, Qwen3-VL, quantized MoE paths, MTP, and graph execution.
[#7674](https://github.com/vllm-project/vllm-ascend/pull/7674)[#7725](https://github.com/vllm-project/vllm-ascend/pull/7725)[#10309](https://github.com/vllm-project/vllm-ascend/pull/10309)[#12115](https://github.com/vllm-project/vllm-ascend/pull/12115)[#13262](https://github.com/vllm-project/vllm-ascend/pull/13262)† - Added Python 3.12 support and moved release images to Python 3.12.
[#9558](https://github.com/vllm-project/vllm-ascend/pull/9558)

### Performance

Unless stated otherwise, these optimizations are selected automatically for the targeted path and need no additional configuration.

- Replaced
`npu_fusion_attention`

with`_npu_flash_attention_unpad`

for supported A2/A3 attention workloads. It is selected automatically; no manual setting is needed.[#8671](https://github.com/vllm-project/vllm-ascend/pull/8671) - Avoided projecting unused tail KV tokens during MLA prefill with PCP. Enable PCP with
`--prefill-context-parallel-size`

; the optimization then applies automatically.[#8787](https://github.com/vllm-project/vllm-ascend/pull/8787) - Reduced scheduler issuance bubbles for workloads using asynchronous scheduling. Enable it with
`--async-scheduling`

.[#8766](https://github.com/vllm-project/vllm-ascend/pull/8766) - Added zero-bubble scheduling for asynchronous speculative decoding. Enable it with
`--async-scheduling`

together with a speculative decoding configuration.[#7640](https://github.com/vllm-project/vllm-ascend/pull/7640) - Batched KV-cache offload copies with
`aclrtMemcpyBatchAsync`

for CPU-offload workloads. Configure KV cache CPU offload as documented; batching is automatic within that path.[#7819](https://github.com/vllm-project/vllm-ascend/pull/7819) - Reduced PCP/DCP KV-cache all-gather traffic by selecting the required blocks before communication. Enable PCP or DCP with
`--prefill-context-parallel-size`

or`--decode-context-parallel-size`

; no separate optimization switch is needed.[#8050](https://github.com/vllm-project/vllm-ascend/pull/8050) - Optimized
`split_qkv_tp_rmsnorm_rope`

kernels for supported quantized model paths. Kernel selection is automatic; no manual setting is needed.[#8059](https://github.com/vllm-project/vllm-ascend/pull/8059)[#9830](https://github.com/vllm-project/vllm-ascend/pull/9830) - Removed prefill host-device synchronization in Qwen3-Next and Qwen3.5 paths. It applies automatically to those models.
[#7967](https://github.com/vllm-project/vllm-ascend/pull/7967) - Reduced SFA prefill KV all-gather communication for PCP/DCP. Enable the corresponding context-parallel mode; the optimized communication path is automatic.
[#8043](https://github.com/vllm-project/vllm-ascend/pull/8043) - Added a Triton penalty kernel for requests using repetition, frequency, or presence penalties. It is selected automatically when penalties are requested.
[#7569](https://github.com/vllm-project/vllm-ascend/pull/7569) - Optimized Model Runner V2 temperature and top-k log-softmax kernels. They are selected automatically for sampling workloads on Model Runner V2.
[#8083](https://github.com/vllm-project/vllm-ascend/pull/8083) - Optimized the Model Runner V2 min-p kernel. It applies automatically when min-p sampling is requested.
[#8243](https://github.com/vllm-project/vllm-ascend/pull/8243)[#7767](https://github.com/vllm-project/vllm-ascend/pull/7767) - Added a Model Runner V2 Triton kernel for bad-word filtering. It applies automatically when
`bad_words`

is supplied.[#8030](https://github.com/vllm-project/vllm-ascend/pull/8030) - Optimized the Model Runner V2 bincount kernel. It is selected automatically for sampling paths that require token counts.
[#7757](https://github.com/vllm-project/vllm-ascend/pull/7757) - Optimized the Model Runner V2 ranks kernel. It is selected automatically for the corresponding sampling path.
[#7767](https://github.com/vllm-project/vllm-ascend/pull/7767) - Reduced avoidable Triton recompilation caused by runtime function parameters. The cache-friendly path is automatic; no manual setting is needed.
[#7481](https://github.com/vllm-project/vllm-ascend/pull/7481)[#7483](https://github.com/vllm-project/vllm-ascend/pull/7483) - Reused equivalent HCCL process groups to reduce distributed initialization overhead. Reuse is automatic for matching groups.
[#7654](https://github.com/vllm-project/vllm-ascend/pull/7654) - Deferred CPU binding until worker warmup completes to avoid interfering with initialization. CPU binding is enabled by default on supported ARM servers; no manual setting is needed unless it was explicitly dis...

[Read more](https://github.com/vllm-project/vllm-ascend/releases/tag/v0.23.0)

## v0.23.0rc1

## v0.23.0rc1 - 2026.07.20

We're excited to announce v0.23.0rc1, the first release candidate for the vLLM Ascend v0.23.0 release line. This release aligns the plugin with upstream vLLM v0.23.0 and expands model, context-parallel, KV-cache offload, and Ascend 950 support. Please follow the [official documentation](https://docs.vllm.ai/projects/ascend/en/v0.23.0rc1/) to get started.

### Highlights

**Expanded model support**: Added GLM-5.2 support on A2 and A3, and Ascend 310P support for Qwen3-ASR-1.7B, Qwen3.5, and Qwen3.6.[#10441](https://github.com/vllm-project/vllm-ascend/pull/10441)[#11264](https://github.com/vllm-project/vllm-ascend/pull/11264)[#10257](https://github.com/vllm-project/vllm-ascend/pull/10257)[#12115](https://github.com/vllm-project/vllm-ascend/pull/12115)**Sparse attention and context parallelism**: Added SFA DCP with a replicated indexer, compact KV gather, and C8 support.[#11819](https://github.com/vllm-project/vllm-ascend/pull/11819)[#11981](https://github.com/vllm-project/vllm-ascend/pull/11981)[#11846](https://github.com/vllm-project/vllm-ascend/pull/11846)[#11871](https://github.com/vllm-project/vllm-ascend/pull/11871)**KV-cache lifecycle and offload**: Added recompute KV-cache offload for P/D decoder nodes, AscendStore coordination, and layerwise KV Pooling with a Memcache backend.[#10742](https://github.com/vllm-project/vllm-ascend/pull/10742)[#10393](https://github.com/vllm-project/vllm-ascend/pull/10393)[#11585](https://github.com/vllm-project/vllm-ascend/pull/11585)**Ascend 950 quantization and communication**: Added W4A16 MXFP4, all-gather EP MXFP4, and low-accuracy token-dispatch paths.[#11014](https://github.com/vllm-project/vllm-ascend/pull/11014)[#11287](https://github.com/vllm-project/vllm-ascend/pull/11287)[#11718](https://github.com/vllm-project/vllm-ascend/pull/11718)[#11766](https://github.com/vllm-project/vllm-ascend/pull/11766)

### Features

- Added DeepSeek V4 MTP graph support.
[#11062](https://github.com/vllm-project/vllm-ascend/pull/11062) - Added Virtual Width Network Eagle3 and Eagle3 support with chunked pipeline parallelism.
[#10042](https://github.com/vllm-project/vllm-ascend/pull/10042)[#10566](https://github.com/vllm-project/vllm-ascend/pull/10566)

### Experimental Features or Optimizations

- Added experimental Step3P7 and Step3P5 support, including Step3P5 MTP.
[#10697](https://github.com/vllm-project/vllm-ascend/pull/10697) - Added experimental Gemma4 support on A2 and Ascend 950.
[#11091](https://github.com/vllm-project/vllm-ascend/pull/11091)[#10643](https://github.com/vllm-project/vllm-ascend/pull/10643) - Improved the DeepSeek V4 prefix-cache hit rate.
[#11107](https://github.com/vllm-project/vllm-ascend/pull/11107)

### Performance

- Optimized SFA DSA-CP output merge with All-to-All communication and PCP FlashAttention restore/output merge.
[#12137](https://github.com/vllm-project/vllm-ascend/pull/12137)[#11842](https://github.com/vllm-project/vllm-ascend/pull/11842) - Avoided H2D synchronization in context-parallel speculative decoding metadata and snapshotted query locations before asynchronous H2D copies.
[#11862](https://github.com/vllm-project/vllm-ascend/pull/11862)[#12071](https://github.com/vllm-project/vllm-ascend/pull/12071) - Parallelized KV-cache receive with a thread pool and enabled asynchronous all-gather for DSA-CP output-projection TP weights.
[#10548](https://github.com/vllm-project/vllm-ascend/pull/10548)[#10694](https://github.com/vllm-project/vllm-ascend/pull/10694) - Vectorized local sequence-length computation in SFA metadata.
[#11816](https://github.com/vllm-project/vllm-ascend/pull/11816)

### Stability and Bug Fixes

- Fixed GLM-5.1 IndexCache weight loading and a GLM-4.7-Flash
`IndexError`

on the first request with MTP and layerwise MemCache.[#11363](https://github.com/vllm-project/vllm-ascend/pull/11363)[#11829](https://github.com/vllm-project/vllm-ascend/pull/11829) - Fixed Qwen3.5 GDN accuracy regressions across PCP, MTP, and DCP graph replay, including a mixed-length PCP out-of-bounds crash, while restoring the previous model-runner dispatch behavior.
[#11195](https://github.com/vllm-project/vllm-ascend/pull/11195)[#11893](https://github.com/vllm-project/vllm-ascend/pull/11893)[#12027](https://github.com/vllm-project/vllm-ascend/pull/12027)[#12283](https://github.com/vllm-project/vllm-ascend/pull/12283) - Fixed Qwen3.5 speculative-decoding accuracy, garbled output, and out-of-bounds failures on Ascend 310P with MTP/EAGLE and full-graph execution.
[#11337](https://github.com/vllm-project/vllm-ascend/pull/11337)[#11408](https://github.com/vllm-project/vllm-ascend/pull/11408)[#11920](https://github.com/vllm-project/vllm-ascend/pull/11920) - Fixed Qwen MoE routing overflow and shared-expert gate matrix-multiplication failures on Ascend 310P.
[#11391](https://github.com/vllm-project/vllm-ascend/pull/11391)[#11730](https://github.com/vllm-project/vllm-ascend/pull/11730) - Fixed Qwen3-Omni ModelSlim W8A8 checkpoint loading failures caused by mismatched weight names and unquantized embedding metadata.
[#12321](https://github.com/vllm-project/vllm-ascend/pull/12321) - Fixed Qwen3-VL rotary-embedding copy races on Ascend 310P and restored the device-specific VisionTransformer patch.
[#11679](https://github.com/vllm-project/vllm-ascend/pull/11679)[#12132](https://github.com/vllm-project/vllm-ascend/pull/12132) - Fixed the DeepSeek-R1-0528 W8A8 shared-expert no-clamp accuracy path without regressing the clamped DeepSeek V4 path.
[#11775](https://github.com/vllm-project/vllm-ascend/pull/11775) - Fixed DeepSeek V4 Flash W4A8-MXFP4 all-gather EP inference on Ascend 950 by preserving routing-weight precision.
[#11498](https://github.com/vllm-project/vllm-ascend/issues/11498)[#11663](https://github.com/vllm-project/vllm-ascend/pull/11663)[#11718](https://github.com/vllm-project/vllm-ascend/pull/11718) - Fixed malformed streamed tool-call arguments and TP8+EP startup compatibility for MiniMax-M2 and MiniMax-M2.5.
[#11505](https://github.com/vllm-project/vllm-ascend/pull/11505) - Fixed silent prefix-cache output corruption and block-table overflow for Qwen3-Next, Qwen3.5, and other hybrid Mamba models using MTP/EAGLE, plus a 310P Mamba align-postprocess hang.
[#11353](https://github.com/vllm-project/vllm-ascend/pull/11353)[#11659](https://github.com/vllm-project/vllm-ascend/pull/11659)[#12038](https://github.com/vllm-project/vllm-ascend/pull/12038) - Fixed Mooncake KV-transfer grouping for Kimi-K2.7 Code with Kimi-K2.5-DFlash when P/D nodes use unequal TP sizes and target/draft models have different global KV-head counts.
[#11887](https://github.com/vllm-project/vllm-ascend/pull/11887) - Fixed the AscendStore parent-block hash chain when a KV block group is only partially missing.
[#12252](https://github.com/vllm-project/vllm-ascend/pull/12252) - Disabled shared-expert multistream overlap when fused MC2 is enabled to avoid an unsupported configuration.
[#12245](https://github.com/vllm-project/vllm-ascend/pull/12245) - Fixed DCP/DP service hangs and restricted the recompute scheduler to decode nodes.
[#12034](https://github.com/vllm-project/vllm-ascend/pull/12034)[#11490](https://github.com/vllm-project/vllm-ascend/pull/11490) - Delayed AscendStore initialization until the first real decode request.
[#11673](https://github.com/vllm-project/vllm-ascend/pull/11673) - Fixed low MTP acceptance rates for SFA with DSA-CP and multiple speculative tokens.
[#10878](https://github.com/vllm-project/vllm-ascend/pull/10878)

### Dependencies

**Upstream vLLM**: v0.23.0.**Python**: >= 3.10, < 3.13.**CANN**: 9.0.1 for A2, A3, and Ascend 950; refer to the 310P installation guide for its platform-specific CANN package.**PyTorch / torch_npu**: 2.10.0 / 2.10.0.post2.**Triton Ascend**: 3.2.1.**Mooncake**: 0.3.11.post1 in the release images.

### Ready to Deprecate

The following features and optimizations are planned for deprecation in a future release:

- Layer sharding.
- FlashComm2.
- The FlashComm3 multistream-overlap gate.
- Hamming sparse.
- Asynchronous exponential overlap.
- Matmul all-reduce and matmul all-reduce RMSNorm fusions.
- Weight prefetch.
- Dynamic-batch SLO.
- KV offload in KV Pool.
- Fused MC2 mode 2 (
`enable_fused_mc2=2`

). - Paged attention and
`pa_shape_list`

. - Selected plugin environment variables; their configuration will be migrated to equivalent
`--additional-config`

options.

### Known Issues

- The combination of pipeline parallelism (PP) and prefill context parallelism (PCP) is not supported in v0.23.0. Support for this combination is deferred to a later release.
- The former
`enable_sparse_c8`

option has been split into`enable_sparse_sfa_c8`

and`enable_sparse_li_c8`

. Existing`--additional-config`

settings must use one or both new options depending on whether Sparse Flash Attention C8, LightningIndexer C8, or both are required.[#12351](https://github.com/vllm-project/vllm-ascend/pull/12351) - The load-balance proxy can swallow decode errors and return an empty HTTP 200 response.
[#12166](https://github.com/vllm-project/vllm-ascend/issues/12166) - Qwen3-30B-A3B floating-point serving can show a 1-2 ms TPOT regression at batch size 1 in the reported TP4 full-graph configuration.
[#12337](https://github.com/vllm-project/vllm-ascend/issues/12337) - In the reported DeepSeek V4 Flash W8A8 MTP P/D-disaggregated deployment, the second aisbench round can cause a worker process from another card to appear on an NPU device.
[#12338](https://github.com/vllm-project/vllm-ascend/issues/12338) - On Ascend 950, Qwen3.5-397B-W8A8-MXFP8-FULL_QUANT in a P/D-disaggregated deployment without MTP can alternate between correct and incorrect outputs.
[#12339](https://github.com/vllm-project/vllm-ascend/issues/12339) - DeepSeek V4 Pro on A3 and A5 can show continuously increasing memory usage in bo...

[Read more](https://github.com/vllm-project/vllm-ascend/releases/tag/v0.23.0rc1)

## v0.22.1rc1

We're excited to announce the release of v0.22.1rc1 for vLLM Ascend. This is the first release candidate for the v0.22.1 release line, building on v0.21.0rc1 and aligning the plugin with upstream vLLM v0.22.1. Please follow the [official doc](https://docs.vllm.ai/projects/ascend/en/releases-v0.22.1rc) to get started.

### Highlights

**Mooncake Connector for DeepSeek V4 / Hybrid KV Cache**: Mooncake connector now supports DeepSeek V4 and hybrid KV cache disaggregated prefill scenarios with correct block stride handling, compressed KV transfer calculation, and hybrid Mamba token alignment.[#10342](https://github.com/vllm-project/vllm-ascend/pull/10342)**HCCL Weight Transfer for RL Workloads**: Added an HCCL-based weight transfer backend for Ascend NPU so trainer and inference workers can synchronize weights in RL pipelines without a CUDA/NCCL dependency.[#9152](https://github.com/vllm-project/vllm-ascend/pull/9152)**Ascend 950 Expansion**: Extended Ascend 950 support with W8A8/W4A8 dynamic quantization and platform-specific CPU binding support.[#10236](https://github.com/vllm-project/vllm-ascend/pull/10236)[#10483](https://github.com/vllm-project/vllm-ascend/pull/10483)

### Features

- Added multimodal input support for DFlash workloads.
[#9340](https://github.com/vllm-project/vllm-ascend/pull/9340) - P-Eagle and PARD are now stable parallel speculative decoding methods and have passed validation testing.
- Added KV consumer partial-group caching for hybrid Mamba models.
[#10009](https://github.com/vllm-project/vllm-ascend/pull/10009) - Added MiniMax M2 C8 cache-scale support in GQA
`load_weights`

.[#10461](https://github.com/vllm-project/vllm-ascend/pull/10461) - [Experimental] Added SSD support for multiple DP ranks on the same machine to avoid local-rank path collisions in Mooncake offload directories.
[#10477](https://github.com/vllm-project/vllm-ascend/pull/10477)

### Hardware and Operator Support

- Added W8A8/W4A8 dynamic quantization support for Ascend 950.
[#10236](https://github.com/vllm-project/vllm-ascend/pull/10236) - Added Ascend 950 CPU binding support for Ascend 950 server topology and process layout.
[#10483](https://github.com/vllm-project/vllm-ascend/pull/10483)

### Performance

- Optimized
`split_qkv_tp_rmsnorm_rope`

with grid-stride loading and host-side reciprocal precomputation; the PR reports about a 5x kernel speedup on the tested MiniMax-M2.5 W8A8 QuaRot prefill workload.[#9830](https://github.com/vllm-project/vllm-ascend/pull/9830) - Reused prebuilt chunk host metadata for Ascend chunk ops to reduce host-device synchronization overhead on Qwen3.5 workloads.
[#9310](https://github.com/vllm-project/vllm-ascend/pull/9310) - Skipped
`compute_slot_mapping`

for Mamba groups to reduce unnecessary work in hybrid cache paths.[#10492](https://github.com/vllm-project/vllm-ascend/pull/10492) - Enabled multistream DSV4 DSA overlap and removed redundant DSA v1 code paths.
[#10518](https://github.com/vllm-project/vllm-ascend/pull/10518)

### Documentation

- Refreshed the context parallel, EPLB, and speculative decoding documentation.
[#10332](https://github.com/vllm-project/vllm-ascend/pull/10332) - Added Kimi 2.6 and GLM5.2 documentation.
[#9969](https://github.com/vllm-project/vllm-ascend/pull/9969)[#10544](https://github.com/vllm-project/vllm-ascend/pull/10544)

### Known Issues

- MiniMax 2.7 dual-node 16-card deployments may hang or crash after 10-20 minutes under load.
[#10591](https://github.com/vllm-project/vllm-ascend/issues/10591) - Llama LoRA can still hit an einsum tensor-dimension mismatch on Ascend.
[#10577](https://github.com/vllm-project/vllm-ascend/issues/10577) - Qwen3.x with PD disaggregation plus MTP could still show precision issues because former KVCache blocks may remain dirty.
[#10961](https://github.com/vllm-project/vllm-ascend/issues/10961) - In A3 four-machine 2P1D deployments, Kimi-K2.6 can trigger
`Error in KVCacheTransferThread. error=unhashable type: 'list'`

on the D node under concurrent`terminal-bench2`

testing.[#10962](https://github.com/vllm-project/vllm-ascend/issues/10962) - With CANN 9.0.0, GLM5.1 1P1D four-machine deployments may hang during 140K-context performance tests, and Kimi-K2.5 with MC2 enabled may hit OOM on single-node A3.
[#10963](https://github.com/vllm-project/vllm-ascend/issues/10963) - Multi-level pooling remains an experimental feature and still has known issues, including DeepSeek-V4-Flash startup failures with Layerwise masks and service hangs in some Mooncake SSD scenarios.
[#10964](https://github.com/vllm-project/vllm-ascend/issues/10964)

## New Contributors

[@Lin-Qingyang-Alec](https://github.com/Lin-Qingyang-Alec)made their first contribution in[#8799](https://github.com/vllm-project/vllm-ascend/pull/8799)[@Maybe2191](https://github.com/Maybe2191)made their first contribution in[#8706](https://github.com/vllm-project/vllm-ascend/pull/8706)[@ChefWu551](https://github.com/ChefWu551)made their first contribution in[#8398](https://github.com/vllm-project/vllm-ascend/pull/8398)[@AlanisZomeg](https://github.com/AlanisZomeg)made their first contribution in[#9018](https://github.com/vllm-project/vllm-ascend/pull/9018)[@ccc000-cell](https://github.com/ccc000-cell)made their first contribution in[#8928](https://github.com/vllm-project/vllm-ascend/pull/8928)[@vvaen](https://github.com/vvaen)made their first contribution in[#8508](https://github.com/vllm-project/vllm-ascend/pull/8508)[@quancs](https://github.com/quancs)made their first contribution in[#9049](https://github.com/vllm-project/vllm-ascend/pull/9049)[@ZeroFadeAway](https://github.com/ZeroFadeAway)made their first contribution in[#9218](https://github.com/vllm-project/vllm-ascend/pull/9218)[@mccube2000](https://github.com/mccube2000)made their first contribution in[#9298](https://github.com/vllm-project/vllm-ascend/pull/9298)[@yuhongming-2026](https://github.com/yuhongming-2026)made their first contribution in[#7886](https://github.com/vllm-project/vllm-ascend/pull/7886)[@lihaofei-2026](https://github.com/lihaofei-2026)made their first contribution in[#8537](https://github.com/vllm-project/vllm-ascend/pull/8537)[@panther-zhu](https://github.com/panther-zhu)made their first contribution in[#9389](https://github.com/vllm-project/vllm-ascend/pull/9389)[@nanxingMy](https://github.com/nanxingMy)made their first contribution in[#9381](https://github.com/vllm-project/vllm-ascend/pull/9381)[@Shelleyaaa](https://github.com/Shelleyaaa)made their first contribution in[#9433](https://github.com/vllm-project/vllm-ascend/pull/9433)[@MosCloud](https://github.com/MosCloud)made their first contribution in[#9450](https://github.com/vllm-project/vllm-ascend/pull/9450)[@zhao-stack](https://github.com/zhao-stack)made their first contribution in[#9238](https://github.com/vllm-project/vllm-ascend/pull/9238)[@internel-error](https://github.com/internel-error)made their first contribution in[#9616](https://github.com/vllm-project/vllm-ascend/pull/9616)[@ZRICHARD9527](https://github.com/ZRICHARD9527)made their first contribution in[#9201](https://github.com/vllm-project/vllm-ascend/pull/9201)[@CXY-Katrina](https://github.com/CXY-Katrina)made their first contribution in[#9525](https://github.com/vllm-project/vllm-ascend/pull/9525)[@xszbuaa](https://github.com/xszbuaa)made their first contribution in[#9344](https://github.com/vllm-project/vllm-ascend/pull/9344)[@ningjingbengxiaohai](https://github.com/ningjingbengxiaohai)made their first contribution in[#9692](https://github.com/vllm-project/vllm-ascend/pull/9692)[@Biuapha](https://github.com/Biuapha)made their first contribution in[#9765](https://github.com/vllm-project/vllm-ascend/pull/9765)[@jyoung6652](https://github.com/jyoung6652)made their first contribution in[#9189](https://github.com/vllm-project/vllm-ascend/pull/9189)[@KaiMa-endeavour](https://github.com/KaiMa-endeavour)made their first contribution in[#9663](https://github.com/vllm-project/vllm-ascend/pull/9663)[@ztzx3156](https://github.com/ztzx3156)made their first contribution in[#9721](https://github.com/vllm-project/vllm-ascend/pull/9721)[@Bybbbb11](https://github.com/Bybbbb11)made their first contribution in[#9382](https://github.com/vllm-project/vllm-ascend/pull/9382)[@1-Y-C](https://github.com/1-Y-C)made their first contribution in[#9601](https://github.com/vllm-project/vllm-ascend/pull/9601)[@yilunh998](https://github.com/yilunh998)made their first contribution in[#9893](https://github.com/vllm-project/vllm-ascend/pull/9893)- @nomewang made their first contribution in
[#9757](https://github.com/vllm-project/vllm-ascend/pull/9757) [@cfq0](https://github.com/cfq0)made their first contribution in[#9638](https://github.com/vllm-project/vllm-ascend/pull/9638)[@ljy19911228](https://github.com/ljy19911228)made their first contribution in[#9481](https://github.com/vllm-project/vllm-ascend/pull/9481)[@muziyuhui666](https://github.com/muziyuhui666)made their first contribution in[#9972](https://github.com/vllm-project/vllm-ascend/pull/9972)[@Fishermanykx](https://github.com/Fishermanykx)made their first contribution in[#9908](https://github.com/vllm-project/vllm-ascend/pull/9908)[@nofushanquan](https://github.com/nofushanquan)made their first contribution in[#9835](https://github.com/vllm-project/vllm-ascend/pull/9835)[@zouzy5137](https://github.com/zouzy5137)made their first contribution in[#10004](https://github.com/vllm-project/vllm-ascend/pull/10004)[@goodgoodname](https://github.com/goodgoodname)made their first contribution in[#10032](https://github.com/vllm-project/vllm-ascend/pull/10032)[@robellliu-dev](https://github.com/robellliu-dev)made their first contribution in[#9801](https://github.com/vllm-project/vllm-ascend/pull/9801)[@baolongsun](https://github.com/baolongsun)made their first contribution in[#10266](https://github.com/vllm-project/vllm-ascend/pull/10266)[@evan-ai-arg](https://github.com/evan-ai-arg)made their first contribution in[#9476](https://github.com/vllm-project/vllm-ascend/pull/9476)[@luobicangqiong](https://github.com/luobicangqiong)made their first contribution in[#10248](https://github.com/vllm-project/vllm-ascend/pull/10248)[@2416602906](https://github.com/2416602906)made their first contribution in[#10178](https://github.com/vllm-project/vllm-ascend/pull/10178)[@lHrHenry233](https://github.com/lHrHenry233)made their first contribution in[#10009](https://github.com/vllm-project/vllm-ascend/pull/10009)[@He1pa](https://github.com/He1pa)made their first contribution in[#9830](https://github.com/vllm-project/vllm-ascend/pull/9830)

**Full Changelog**: `v0.19.1rc1...v0.22.1rc1`

## v0.21.0rc1

We're excited to announce the release of v0.21.0rc1 for vLLM Ascend. This is the first release candidate for the v0.21.0 release line, building on v0.20.2rc1. Please follow the [official doc](https://docs.vllm.ai/projects/ascend/en/latest) to get started.

### Highlights

**DeepSeek-V4 for Ascend 950**: Full end-to-end support for DeepSeek-V4 on Ascend 950, including piecewise graph mode, DSA attention, KV cache management, and MTP.[#9757](https://github.com/vllm-project/vllm-ascend/pull/9757)[#9935](https://github.com/vllm-project/vllm-ascend/pull/9935)**Hybrid & Mamba Align Prefix Cache**: New alignment-based prefix caching mechanism for Hybrid and Mamba architectures, improving cache hit rates across related sequences.[#9533](https://github.com/vllm-project/vllm-ascend/pull/9533)**FULL_AND_PIECEWISE Graph Mode**: Introduced a hybrid graph compilation mode combining full-graph and piecewise strategies.**Requires HDK 25.5.1+ / CANN 8.5.0+**to remove the old stream-budget limitation, enabling up to ~32K graphs on A3 and ~64K on Ascend 950.[#9572](https://github.com/vllm-project/vllm-ascend/pull/9572)[#9962](https://github.com/vllm-project/vllm-ascend/pull/9962)**Python 3.12 Support**: Dockerfiles and setup.py now officially support Python 3.12, and all base images have been upgraded from`py3.11`

to`py3.12`

.[#9558](https://github.com/vllm-project/vllm-ascend/pull/9558)

### Features

- Added end-to-end support for DeepSeek-V4 on Ascend 950, including piecewise graph mode, DSA attention backend, KV cache management, distributed inference (with PP fixes), and MTP.
[#9757](https://github.com/vllm-project/vllm-ascend/pull/9757)[#9473](https://github.com/vllm-project/vllm-ascend/pull/9473)[#9935](https://github.com/vllm-project/vllm-ascend/pull/9935) - Added Hybrid & Mamba Align Prefix Cache for improved prefix cache reuse in Hybrid and Mamba architectures.
[#9533](https://github.com/vllm-project/vllm-ascend/pull/9533) - Added layerwise KV cache event callbacks for finer per-layer observability and control.
[#9468](https://github.com/vllm-project/vllm-ascend/pull/9468) - Added GLM4.7-Flash model support with Flash Attention backend.
[#9560](https://github.com/vllm-project/vllm-ascend/pull/9560) - Added
`FULL_AND_PIECEWISE`

graph mode, a hybrid compilation strategy mixing full-graph and piecewise approaches.**Requires HDK 25.5.1+ / CANN 8.5.0+**to remove the old stream-budget limitation, enabling significantly more graph captures — approximately 32K on A3 and 64K on Ascend 950. Legacy capture-size pruning has been cleaned up accordingly.[#9572](https://github.com/vllm-project/vllm-ascend/pull/9572)[#9962](https://github.com/vllm-project/vllm-ascend/pull/9962) - Added W4A8 MXFP4 quantization support for Ascend 950.
[#8265](https://github.com/vllm-project/vllm-ascend/pull/8265) - Added MXFP8 FlashCommV3 support on Ascend 950.
[#9671](https://github.com/vllm-project/vllm-ascend/pull/9671) - Added NZ layout support for W4A8 MoE compressed tensors and C8 quantization (GQA).
[#9625](https://github.com/vllm-project/vllm-ascend/pull/9625)[#9721](https://github.com/vllm-project/vllm-ascend/pull/9721) - Added Mooncake Connector hybrid PCP/DCP support for QWen3.5.
[#9809](https://github.com/vllm-project/vllm-ascend/pull/9809) - Added D2D NetLoader weight loading for draft models in speculative decoding.
[#9893](https://github.com/vllm-project/vllm-ascend/pull/9893) - Added Mooncake Connector hybrid attention support.
[#8850](https://github.com/vllm-project/vllm-ascend/pull/8850) - Added Mooncake KV pool usage optimization.
[#7820](https://github.com/vllm-project/vllm-ascend/pull/7820) - Added KV Pool support for loading failure block IDs without hybrid recompute.
[#9701](https://github.com/vllm-project/vllm-ascend/pull/9701) - Added NPU storage metadata debug helpers for improved troubleshooting.
[#9189](https://github.com/vllm-project/vllm-ascend/pull/9189) - Added torch reserved/allocated memory profiling in
`execute_model()`

.[#9765](https://github.com/vllm-project/vllm-ascend/pull/9765) - Added EPLB experts hotness metrics and EPLB time consumption data exposure.
[#9536](https://github.com/vllm-project/vllm-ascend/pull/9536) - Added
`group_name`

parameter when creating HCCL config for better group management.[#9667](https://github.com/vllm-project/vllm-ascend/pull/9667) - Enabled prefix caching with PCP/DCP, allowing KV cache reuse across prefill and decode in disaggregated deployments.
[#9638](https://github.com/vllm-project/vllm-ascend/pull/9638) - Added simple yet general CPU KV Cache Offloading support.
[#8743](https://github.com/vllm-project/vllm-ascend/pull/8743) - Added Mooncake SSD offload with embedded client for large-scale KV cache storage.
[#9731](https://github.com/vllm-project/vllm-ascend/pull/9731) - Re-added code start compilation caching for npugraph_ex (previously reverted), improving warmup time.
[#9914](https://github.com/vllm-project/vllm-ascend/pull/9914) - Added ACL graph memory estimation before KV cache allocation to prevent OOM during graph capture.
[#9865](https://github.com/vllm-project/vllm-ascend/pull/9865) - Added DeepSeek-V4 compressor block size [32,64,128] support to improve automatic prefix cache hit rate.
[#10354](https://github.com/vllm-project/vllm-ascend/pull/10354) - Added batch_invariant_ops setup for reinforcement learning scenarios.
[#10034](https://github.com/vllm-project/vllm-ascend/pull/10034) - Adapted load balance proxy example to shared scheduler workers.
[#9645](https://github.com/vllm-project/vllm-ascend/pull/9645) - [310P] Added Qwen3.5 MTP and graph mode support.
[#10309](https://github.com/vllm-project/vllm-ascend/pull/10309)

### Hardware and Operator Support

- Added custom GDN operator support for Ascend 950 with a new fused GDN gating AscendC operator (
`fused_gdn_gating`

).[#9382](https://github.com/vllm-project/vllm-ascend/pull/9382)[#9601](https://github.com/vllm-project/vllm-ascend/pull/9601) - Added A2/A3 and Ascend 950 compressor operator paths.
[#9350](https://github.com/vllm-project/vllm-ascend/pull/9350) - Adapted GDN and Conv1D operators for the Ascend 950 platform.
[#9224](https://github.com/vllm-project/vllm-ascend/pull/9224) - Added Ascend 950 Dockerfiles and disaggregated PD endpoint configuration documentation.
[#9723](https://github.com/vllm-project/vllm-ascend/pull/9723)[#9690](https://github.com/vllm-project/vllm-ascend/pull/9690) - Removed unused MC2 prefill custom ops to streamline the operator surface.
[#9919](https://github.com/vllm-project/vllm-ascend/pull/9919) - Added Sparse Flash Attention support on Ascend 950 devices.
[#9825](https://github.com/vllm-project/vllm-ascend/pull/9825) - Added LightningIndexer and SparseFlashAttention ACLNN ops for improved sparse attention performance.
[#9491](https://github.com/vllm-project/vllm-ascend/pull/9491) - Added Rehash for AscendStore grouped keys to support DeepSeek V4 and compressed layouts.
[#9789](https://github.com/vllm-project/vllm-ascend/pull/9789)

### Performance

- Optimized 310P MoE routing path for improved throughput.
[#9105](https://github.com/vllm-project/vllm-ascend/pull/9105) - Added NZ format support for W4A8 MoE compressed tensors, delivering better memory access patterns.
[#9625](https://github.com/vllm-project/vllm-ascend/pull/9625) - Added irregular mask build optimization for PCP/DCP with speculative decoding, improving efficiency.
[#9678](https://github.com/vllm-project/vllm-ascend/pull/9678) - Reconstructed reduce sampling to eliminate patch behaviors and support both DFlash and MTP.
[#9735](https://github.com/vllm-project/vllm-ascend/pull/9735)

### Stability and Bug Fixes

- Fixed speculative decoding MLA shape mismatch with Eagle3 and added DeepSeek V2 Eagle3 support.
[#9703](https://github.com/vllm-project/vllm-ascend/pull/9703) - Fixed draft
`lm_head`

preservation for DFlash with reduced (draft-to-target) vocabulary.[#9795](https://github.com/vllm-project/vllm-ascend/pull/9795) - Fixed a draft model index-out-of-range error caused by
`token_indices_to_sample`

on Ascend 950.[#9867](https://github.com/vllm-project/vllm-ascend/pull/9867) - Added validation of DCP for draft models to catch configuration mismatches early.
[#9717](https://github.com/vllm-project/vllm-ascend/pull/9717) - Fixed multiple DeepSeek V4 PP issues.
[#9473](https://github.com/vllm-project/vllm-ascend/pull/9473) - Fixed DSA compressed idle dummy graph out-of-bounds issue.
[#9818](https://github.com/vllm-project/vllm-ascend/pull/9818) - Fixed HMA support in AscendMultiConnector.
[#9782](https://github.com/vllm-project/vllm-ascend/pull/9782) - Patched GLM47 inline zero-argument streaming tool calls.
[#9901](https://github.com/vllm-project/vllm-ascend/pull/9901) - Patched GLM tool-call final chunks for correct streaming termination.
[#9787](https://github.com/vllm-project/vllm-ascend/pull/9787) - Fixed empty
`tool_calls`

being emitted in OpenAI-format chat responses.[#9791](https://github.com/vllm-project/vllm-ascend/pull/9791) - Backported MiniMax M2 tool call streaming support.
[#9742](https://github.com/vllm-project/vllm-ascend/pull/9742) - Repaired 310P Qwen3.5 ACLGraph precision.
[#9727](https://github.com/vllm-project/vllm-ascend/pull/9727) - Fixed precision of the
`causal_conv1d_v310`

operator on 310P.[#9720](https://github.com/vllm-project/vllm-ascend/pull/9720) - Fixed ACL dtype mapping table for correct dtype conversions.
[#9826](https://github.com/vllm-project/vllm-ascend/pull/9826) - Chunked
`wq_b`

matmul to work around the NPU 65536 dimension limit.[#9780](https://github.com/vllm-project/vllm-ascend/pull/9780) - Optimized router experts in eager mode and fixed communication handling.
[#9728](https://github.com/vllm-project/vllm-ascend/pull/9728) - Lazy initialization of KV store on
`put`

to avoid early resource allocation. [[#9771](https://github.com/vllm-project/vllm-ascend/pull/9771)]([#9771](https://github.com/vllm-project/vllm-ascend/pull/9771)...

[Read more](https://github.com/vllm-project/vllm-ascend/releases/tag/v0.21.0rc1)

## v0.20.2rc1

We're excited to announce the release of v0.20.2rc1 for vLLM Ascend. This is the first release candidate for the v0.20.2 release line. Please follow the [official doc](https://docs.vllm.ai/projects/ascend/en/latest) to get started.

### Highlights

**DeepSeek V4 Support**: Added end-to-end support for DeepSeek V4, including the model architecture, DSA attention backend, KV cache management, distributed inference, tool-call parser, MTP support, KV Pool adaptation, and custom operator enablement.[#9270](https://github.com/vllm-project/vllm-ascend/pull/9270)[#9385](https://github.com/vllm-project/vllm-ascend/pull/9385)[#9228](https://github.com/vllm-project/vllm-ascend/pull/9228)**A5 and XLite Quantization Expansion**: Added MXFP4 flatquant with row parallelism for Ascend A5 and expanded XLite support to GLM-4.7 W8A8 quantization.[#9391](https://github.com/vllm-project/vllm-ascend/pull/9391)[#9415](https://github.com/vllm-project/vllm-ascend/pull/9415)

### Features

- Added Flash Attention 3 support for training-inference consistency. The backend is ready in vLLM Ascend and will become directly usable once the FA3 package is publicly available.
[#9060](https://github.com/vllm-project/vllm-ascend/pull/9060) - Added DeepSeek PCP/DCP adaptation to improve support for disaggregated deployments.
[#9058](https://github.com/vllm-project/vllm-ascend/pull/9058) - Added a dedicated
`additional_config.enable_dsa_cp`

switch to decouple DSA-CP from FC1. DSA-CP now requires both FC1 and DSA-CP to be explicitly enabled, allowing FC1 to stay enabled while DSA-CP is disabled when needed.[#9878](https://github.com/vllm-project/vllm-ascend/pull/9878) - Added merged graph support for DFlash workloads.
[#9074](https://github.com/vllm-project/vllm-ascend/pull/9074) - Added LoRA support for Qwen3.5 dense models.
[#9023](https://github.com/vllm-project/vllm-ascend/pull/9023) - Added KV pool adaptation for DeepSeek V4 and separated MTP-layer KV cache sharding for DeepSeek V4 speculative decoding.
[#9385](https://github.com/vllm-project/vllm-ascend/pull/9385)[#9367](https://github.com/vllm-project/vllm-ascend/pull/9367)

### Hardware and Operator Support

- Added DeepSeek V4 custom operators required for the new model path, registered the operators for Ascend 910B, and switched the DeepSeek V4
`hc_pre`

path to a fused operator.[#9228](https://github.com/vllm-project/vllm-ascend/pull/9228)[#9339](https://github.com/vllm-project/vllm-ascend/pull/9339)[#9396](https://github.com/vllm-project/vllm-ascend/pull/9396) - Enabled MXFP4 flatquant and row parallel support on Ascend A5.
[#9391](https://github.com/vllm-project/vllm-ascend/pull/9391) - Enabled MC2 dispatch and combine support for MXFP4/MXFP8 quantization on Ascend A5.
[#9365](https://github.com/vllm-project/vllm-ascend/pull/9365)[#9328](https://github.com/vllm-project/vllm-ascend/pull/9328) - Improved 310P support by optimizing fused operators for Qwen3.5 Dense ACLGraph and simplifying the 310P RMSNormGated path.
[#9104](https://github.com/vllm-project/vllm-ascend/pull/9104)[#9489](https://github.com/vllm-project/vllm-ascend/pull/9489)

### Performance

- Added DeepSeek V4 DSA multistream overlap optimizations across compressor, indexer-select, CV parallel, and pure-prefill compute-communication overlap paths.
[#9450](https://github.com/vllm-project/vllm-ascend/pull/9450)[#9441](https://github.com/vllm-project/vllm-ascend/pull/9441)[#9433](https://github.com/vllm-project/vllm-ascend/pull/9433)[#9504](https://github.com/vllm-project/vllm-ascend/pull/9504) - Reused DSA
`topk_indices`

across decode steps with IndexCache to reduce repeated DeepSeek V4 index computation.[#9390](https://github.com/vllm-project/vllm-ascend/pull/9390) - Fixed the missing enablement for
`cv_indexer_qkv_prepare`

multistream parallelism in the new overlap path.[#9530](https://github.com/vllm-project/vllm-ascend/pull/9530) - Reduced host-device synchronization overhead by removing the sync point in PIECEWISE mode.
[#9025](https://github.com/vllm-project/vllm-ascend/pull/9025) - Optimized shared expert overlap timing in FusedMoE.
[#9413](https://github.com/vllm-project/vllm-ascend/pull/9413) - [Experimental] Added reduce sampling with
`enable_reduce_sample`

to lower Tensor Parallel communication overhead in distributed greedy, top-k/top-p, and rejection sampling paths.[#8308](https://github.com/vllm-project/vllm-ascend/pull/8308)

### Stability and Bug Fixes

- Fixed DeepSeek V4 MTP, serial inference, FlashComm, A2 tensor-output all-reduce, and P/D disaggregation KV cache edge cases.
[#9456](https://github.com/vllm-project/vllm-ascend/pull/9456)[#9487](https://github.com/vllm-project/vllm-ascend/pull/9487)[#9488](https://github.com/vllm-project/vllm-ascend/pull/9488)[#9389](https://github.com/vllm-project/vllm-ascend/pull/9389)[#9500](https://github.com/vllm-project/vllm-ascend/pull/9500) - Fixed DeepSeek V4
`hc_pre`

behavior and added a 4-card E2E regression test.[#9452](https://github.com/vllm-project/vllm-ascend/pull/9452)

### Dependencies

- Upgraded the matched upstream vLLM baseline to v0.20.2.
[#9270](https://github.com/vllm-project/vllm-ascend/pull/9270) - Upgraded CANN to 9.0.0 and triton-ascend to 3.2.1.
[#9085](https://github.com/vllm-project/vllm-ascend/pull/9085) - Upgraded PyTorch and torch-npu to 2.10.0.
[#9128](https://github.com/vllm-project/vllm-ascend/pull/9128)

### Breaking Changes and Migration Notes

- Migrated a set of runtime options from environment variables to
`AscendConfig`

, including the FC1/FlashComm1 switch from`VLLM_ASCEND_ENABLE_FLASHCOMM1`

to`additional_config.enable_flashcomm1`

. Please review configuration code and deployment manifests when upgrading.[#9064](https://github.com/vllm-project/vllm-ascend/pull/9064) - Disabled SwiGLU clamp by default, which may slightly change behavior for workloads that previously relied on the old default.
[#9438](https://github.com/vllm-project/vllm-ascend/pull/9438)

### Documentation

- Refreshed deployment and feature documentation for the current main branch release line.
[#9309](https://github.com/vllm-project/vllm-ascend/pull/9309)[#8968](https://github.com/vllm-project/vllm-ascend/pull/8968) - Added documentation for the
`enable_dsa_cp`

additional configuration option for DeepSeek V3.2 and GLM5.[#9910](https://github.com/vllm-project/vllm-ascend/pull/9910)

### Known Issues

- GLM5/GLM5.1 W4A8 deployments have known issues in some advanced configurations.
[#9395](https://github.com/vllm-project/vllm-ascend/issues/9395) - Qwen3.6-35B-A3B may shut down when MTP/speculative decoding is enabled, with
`numAcceptedTokens[0]=4 exceeds varlen segment length=3`

reported during shape/dtype processing.[#9956](https://github.com/vllm-project/vllm-ascend/issues/9956) - GLM-5.1 can hang on the P node in 200K long-sequence 1P1D agent workloads after long-running service, with
`MoeDistributeDispatchV2`

/`aclnnMoeDistributeDispatchV4`

reporting an AICore timeout.[#9958](https://github.com/vllm-project/vllm-ascend/issues/9958) - GLM5 W4A8 deployments can see a significantly lower speculative decoding acceptance rate when MTP3 is used together with FlashComm.
[#9803](https://github.com/vllm-project/vllm-ascend/issues/9803) - MiniMax-M2.7 W8A8/QuaRot can show lower-than-expected GPQA accuracy in long-sequence deployments when PCP/DCP is combined with Eagle3 speculative decoding.
[#9959](https://github.com/vllm-project/vllm-ascend/issues/9959) - KV Pool feature for DeepSeek V4 now faces several known issues affects user-friendliness and performance, including special startup parameter requirements, special key storing behaviors, etc. For details, please refer to issue
[#9975](https://github.com/vllm-project/vllm-ascend/issues/9975).

## v0.19.1rc1

This is the first release candidate of v0.19.1 for vLLM Ascend, based on vLLM v0.19.1. This release includes significant performance optimizations, new model support, hardware expansion, and important bug fixes.

Please follow the [official doc](https://docs.vllm.ai/projects/ascend/en/latest) to get started.

### Highlights

**DFlash Attention Backend**: Added DFlash attention backend with FULL_DECODE_ONLY support for improved inference performance ([#8118](https://github.com/vllm-project/vllm-ascend/pull/8118),[#8516](https://github.com/vllm-project/vllm-ascend/pull/8516),[#8627](https://github.com/vllm-project/vllm-ascend/pull/8627))**Zero Bubble Async Scheduling**: Implemented zero bubble optimization for async scheduling and speculative decoding, significantly reducing scheduling overhead ([#7640](https://github.com/vllm-project/vllm-ascend/pull/7640))**A2/A3 Attention Operator Upgrade**: Replaced npu_fusion_attention with _npu_flash_attention_unpad operator for better performance on A2 and A3 hardware ([#8671](https://github.com/vllm-project/vllm-ascend/pull/8671))**Eagle3 + MiniMax-M2.5 Support**: Applied Eagle3 speculative decoding to MiniMax-M2.5 model for faster inference ([#7619](https://github.com/vllm-project/vllm-ascend/pull/7619))**C8 INT8 KV Cache for GQA**: Added C8 (INT8 KV cache) support for GQA attention models, including DeepSeek-V3.1 with PD disaggregation ([#7474](https://github.com/vllm-project/vllm-ascend/pull/7474),[#7222](https://github.com/vllm-project/vllm-ascend/pull/7222))**Bailing Model Support**: Full support for Bailing MoE model including linear adaptation and ModelSlim quantization ([#8657](https://github.com/vllm-project/vllm-ascend/pull/8657),[#8709](https://github.com/vllm-project/vllm-ascend/pull/8709))

### Features

**Flash Comm V1 for Qwen3-VL**: Support Flash Comm V1 for Qwen3-VL multimodal models ([#7897](https://github.com/vllm-project/vllm-ascend/pull/7897))**Eagle + PCP + Full Graph Mode**: Support Eagle combined with PCP and full graph mode ([#7924](https://github.com/vllm-project/vllm-ascend/pull/7924))**Multimodal Reasoning with PCP**: Support multimodal reasoning when prefill context parallel feature is enabled ([#8038](https://github.com/vllm-project/vllm-ascend/pull/8038))**Dynamic Chunk for PP**: Support Dynamic Chunk for Chunked Pipeline Parallelism ([#7896](https://github.com/vllm-project/vllm-ascend/pull/7896))**Hamming-based Sparse Attention**: Added Hamming-based sparse attention inference framework and operators ([#8564](https://github.com/vllm-project/vllm-ascend/pull/8564),[#8346](https://github.com/vllm-project/vllm-ascend/pull/8346))**Optimized Causal Conv1d Operator**: Added optimized causal conv1d operator ([#8215](https://github.com/vllm-project/vllm-ascend/pull/8215))**Recurrent AscendC Operators**: Added recurrent AscendC operators for specific model architectures ([#8055](https://github.com/vllm-project/vllm-ascend/pull/8055))**GLM4.7 C8 Support**: Support GLM4.7 with C8 (INT8 KV cache) scenarios ([#8174](https://github.com/vllm-project/vllm-ascend/pull/8174))**Minitron-8B-Base Support**: Verified and supported nvidia/Minitron-8B-Base model ([#8157](https://github.com/vllm-project/vllm-ascend/pull/8157))**Bailing Model Support**: Full support for Bailing MoE model with linear adaptation and ModelSlim quantization configuration ([#8657](https://github.com/vllm-project/vllm-ascend/pull/8657),[#8709](https://github.com/vllm-project/vllm-ascend/pull/8709))**Qwen3.5 MoE Flash Comm**: Support Flash Comm for Qwen3.5 MoE models ([#7486](https://github.com/vllm-project/vllm-ascend/pull/7486))**Initial MoE Support for MRv2**: Add initial MoE models support for Model Runner V2 ([#7922](https://github.com/vllm-project/vllm-ascend/pull/7922))**Xlite Backend Expansion**:**EPLB Enhancements**:**Eagle Improvements for model_runner_v2**:**MTP Merged Graph**: Support merged graph for MTP (Multi-Token Prediction) ([#6860](https://github.com/vllm-project/vllm-ascend/pull/6860))**Unified MoE Expert Placement**: Support unified placement for shared & router experts ([#7188](https://github.com/vllm-project/vllm-ascend/pull/7188))**Dispatch V2 Hierarchy Communication**: Support dispatch_v2/combine_v2 hierarchy communication for better MoE performance ([#7583](https://github.com/vllm-project/vllm-ascend/pull/7583))**Xmask for Dispatch FFN Combine**: Add xmask feature for dispatch_ffn_combine operator (w8a8 branch) ([#8560](https://github.com/vllm-project/vllm-ascend/pull/8560))**Fused W4A8 Kernel**: Fuse W4A8 dispatch + FFN + combine into a single fused kernel ([#7779](https://github.com/vllm-project/vllm-ascend/pull/7779))**KV Cache Memory Accounting**: Account for graph capture memory in KV cache planning ([#8289](https://github.com/vllm-project/vllm-ascend/pull/8289))**Qwen3-Next Hybrid Attention**: Support Qwen3-next hybrid attention in piecewise & full_decode_only modes ([#7422](https://github.com/vllm-project/vllm-ascend/pull/7422))**GDN Optimization**: Optimize GDN non-spec prefill fallback metadata ([#7756](https://github.com/vllm-project/vllm-ascend/pull/7756))**Qwen3-VL Support**: Support kv_rmsnorm_mrope for Qwen3-VL ([#7762](https://github.com/vllm-project/vllm-ascend/pull/7762))**Mamba Prefix Caching**: Layerwise connector supports Mamba prefill prefix caching ([#7814](https://github.com/vllm-project/vllm-ascend/pull/7814))**Yuanrong KV Pool Backend**: Add Yuanrong backend support to KV Pool ([#6869](https://github.com/vllm-project/vllm-ascend/pull/6869))

### Hardware and Operator Support

**310P Enhancements**:

### Performance

**A2/A3 Attention**: Replace npu_fusion_attention with _npu_flash_attention_unpad operator for better performance ([#8671](https://github.com/vllm-project/vllm-ascend/pull/8671))**MLA PCP Prefill Optimization**: Optimize MLA PCP prefill attention by avoiding projecting unnecessary tail KV tokens ([#8787](https://github.com/vllm-project/vllm-ascend/pull/8787))**Async Scheduling Optimization**:**KV Cache Optimization**:**Operator Optimizations**:**Triton Kernel Optimizations (model_runner_v2)**:- Optimize _temperature_kernel and _topk_log_softmax_kernel (
[#8083](https://github.com/vllm-project/vllm-ascend/pull/8083)) - Optimize _min_p_kernel performance (
[#8243](https://github.com/vllm-project/vllm-ascend/pull/8243),[#7767](https://github.com/vllm-project/vllm-ascend/pull/7767)) - Add bad-words-kernel triton kernel (
[#8030](https://github.com/vllm-project/vllm-ascend/pull/8030)) - Optimize bincount_kernel performance (
[#7757](https://github.com/vllm-project/vllm-ascend/pull/7757)) - Optimize _ranks_kernel performance (
[#7767](https://github.com/vllm-project/vllm-ascend/pull/7767)) - Optimize triton recompilation triggered by function parameters (
[#7480](https://github.com/vllm-project/vllm-ascend/pull/7480),[#7481](https://github.com/vllm-project/vllm-ascend/pull/7481),[#7483](https://github.com/vllm-project/vllm-ascend/pull/7483))

- Optimize _temperature_kernel and _topk_log_softmax_kernel (
**HCCL Process Group Reuse**: Reuse equivalent HCCL process groups on Ascend ([#7654](https://github.com/vllm-project/vllm-ascend/pull/7654))**CPU Binding Defer**: Defer CPU binding until worker warmup completes ([#7829](https://github.com/vllm-project/vllm-ascend/pull/7829))**Conv3d to Linear Conversion**: Convert conv3d to linear when kernel size equ...

[Read more](https://github.com/vllm-project/vllm-ascend/releases/tag/v0.19.1rc1)

## v0.18.0

We're excited to announce the release of v0.18.0 for vLLM Ascend. This is the official release for v0.18.0. Please follow the [official doc](https://docs.vllm.ai/projects/ascend/en/v0.18.0) to get started.

### Highlights

**Model Support**

**Kimi-K2.x Model Support**: [Experimental]Added support for Kimi-K2.x models.[@aipaes](https://github.com/aipaes)[@dragondream-chen](https://github.com/dragondream-chen)[@SparrowMu](https://github.com/SparrowMu)[@LoganJane](https://github.com/LoganJane)[#6755](https://github.com/vllm-project/vllm-ascend/pull/6755)**Minimax-m2.x Model Support**: [Experimental]Added support for Minimax-m2.x models with eagle3.[@SparrowMu](https://github.com/SparrowMu)[@GDzhu01](https://github.com/GDzhu01)[#7105](https://github.com/vllm-project/vllm-ascend/pull/7105)[#7714](https://github.com/vllm-project/vllm-ascend/pull/7714)**GLM5 Support**: [Experimental]Added support for GLM5 models without any code modification!**Qwen3.x Support**: [Experimental]Added support for Qwen3.x models without any code modification!**DeepseekOCR Support**: [Experimental]Added support for DeepseekOCR model and optimize`RelPosAttention`

and`CustomQwen2Decoder`

.[@Wangbei25](https://github.com/Wangbei25)[#7737](https://github.com/vllm-project/vllm-ascend/pull/7737)

**Core Features**

**EPLB (Expert Parallelism Load Balance)**: EPLB is more stable with many bug fixes, and has better performance now. EPLB now works in most cases and is recommended for use.[#6528](https://github.com/vllm-project/vllm-ascend/pull/6528)[#7344](https://github.com/vllm-project/vllm-ascend/pull/7344)[#7890](https://github.com/vllm-project/vllm-ascend/pull/7890)[#6477](https://github.com/vllm-project/vllm-ascend/pull/6477)**ACLGraph Enhancement**: ACLGraph now support capturing a single merged graph for multi-step drafts, which greatly reduce host bound in multi-step spec decoding case![#5553](https://github.com/vllm-project/vllm-ascend/pull/5553)[#5940](https://github.com/vllm-project/vllm-ascend/pull/5940)**KV Pooling**: Enhanced KV pool with Mooncake connector now support sparse attention, and LMCacheAscendConnector is added as a new KV cache pooling solution for Ascend, and support FabricMem Mode for HIXL interconnect, support yuanrong as a backend for AscendStoreConnector, and now MooncakeLayerwiseConnector can be activated together with KV Pooling. Compared with previous versions, KV Pooling has a huge performance optimization on TTFT![#6339](https://github.com/vllm-project/vllm-ascend/pull/6339)[#6882](https://github.com/vllm-project/vllm-ascend/pull/6882)[#6806](https://github.com/vllm-project/vllm-ascend/pull/6806)[#6869](https://github.com/vllm-project/vllm-ascend/pull/6869)[#7032](https://github.com/vllm-project/vllm-ascend/pull/7032)**PD disaggregation**: Mooncake layerwise connector now support hybrid attention manager and PCP feature.[#7022](https://github.com/vllm-project/vllm-ascend/pull/7022)[#6627](https://github.com/vllm-project/vllm-ascend/pull/6627)**NPU Graph EX (npugraph_ex) Enabled by Default**: The npugraph_ex feature is now enabled by default, providing better graph optimization with integrated inductor pass and MatmulAllReduceAddRMSNorm fusion.[#6354](https://github.com/vllm-project/vllm-ascend/pull/6354)[#6664](https://github.com/vllm-project/vllm-ascend/pull/6664)[#6006](https://github.com/vllm-project/vllm-ascend/pull/6006)**RL(Reinforcement learning)**: [Experimental]RL enhanced with implemented batch invariant feature with AscendC and triton op, and added routing replay feature.[#6590](https://github.com/vllm-project/vllm-ascend/pull/6590)[#6696](https://github.com/vllm-project/vllm-ascend/pull/6696)**CPU Binding Enabled by Default**: Enabled ARM-only CPU binding with global-slicing A3 policy, improving inference throughput in hostbound scenarios.[#6686](https://github.com/vllm-project/vllm-ascend/pull/6686)

### Features

- Prefix cache is now supported in hybrid model.
[#7103](https://github.com/vllm-project/vllm-ascend/pull/7103) - Flash Comm V1 now supports VL models with MLA, removing a previous limitation for multimodal serving.
[#7390](https://github.com/vllm-project/vllm-ascend/pull/7390) - VL MoE models now support SP, and
`sp_threshold`

is removed in favor of`sp_min_token_num`

from vLLM.[#7044](https://github.com/vllm-project/vllm-ascend/pull/7044) - [Experimental]Pipeline Parallel now supports async scheduling, improving throughput for PP deployments.
[#7136](https://github.com/vllm-project/vllm-ascend/pull/7136) - Eagle3 now supports QuaRot quantization without embedding.
[#7038](https://github.com/vllm-project/vllm-ascend/pull/7038) - Refactoring eagle3/mtp, eagle3 and mtp are now using the same proposer.
[#6349](https://github.com/vllm-project/vllm-ascend/pull/6349)[#7033](https://github.com/vllm-project/vllm-ascend/pull/7033)

### Hardware and Operator Support

**First time support 310P, with huge performance optimization!**:**Custom Operators**: Added multiple custom operators including:- Added AscendC casual_conv1d_fn operator for Qwen3-Next.
[#6661](https://github.com/vllm-project/vllm-ascend/pull/6661) - Added Ascend Ops recurrent_gated_delta_rule operator.
[#6725](https://github.com/vllm-project/vllm-ascend/pull/6725) - Added GMM custom operator for MoE models.
[#7010](https://github.com/vllm-project/vllm-ascend/pull/7010) - Optimize split_qkv_rmsnorm_rope operator.
[#6827](https://github.com/vllm-project/vllm-ascend/pull/6827) - Triton rope now supports index_selecting from cos_sin_cache.
[#5450](https://github.com/vllm-project/vllm-ascend/pull/5450) - Added AscendC fused op transpose_kv_cache_by_block to speed up GQA transfer.
[#6366](https://github.com/vllm-project/vllm-ascend/pull/6366) - Optimized
`DispatchFFNCombine`

kernel performance and resolved vector error caused by unaligned UB access.[#6468](https://github.com/vllm-project/vllm-ascend/pull/6468)[#6707](https://github.com/vllm-project/vllm-ascend/pull/6707) - Refactor and optimize CausalConv1d.
[#7495](https://github.com/vllm-project/vllm-ascend/pull/7495)

- Added AscendC casual_conv1d_fn operator for Qwen3-Next.

### Performance

**Initialize Performance**: Optimized Triton operator recompilation to reduce redundant rebuilds and unnecessary recompilation triggered by function parameter optimization.[#7647](https://github.com/vllm-project/vllm-ascend/pull/7647)[#7645](https://github.com/vllm-project/vllm-ascend/pull/7645)**Qwen3.x Performance**: [Experimental]Optimized the Qwen3.x and Qwen3-Next performance by supporting full graph mode, PD disaggregation, mamba prefill prefix-caching and flashcomm1, prebuilding chunk metadata to reducing host-device synchronization overhead, and multiple op performance optimization including`chunk_gated_delta_rule`

,`chunk_fwd_kernel_o`

,`solve_tril`

,`recompute_w_u_fwd_kernel`

,`split_qkv_rmsnorm_mrope`

, etc.[@LoganJane](https://github.com/LoganJane)[@shaopeng-666](https://github.com/shaopeng-666)[@ppppeng](https://github.com/ppppeng)[@SunnyLee151064](https://github.com/SunnyLee151064)[@hust17yixuan](https://github.com/hust17yixuan)[@Toneymiller](https://github.com/Toneymiller)[@linfeng-yuan](https://github.com/linfeng-yuan)[#7487](https://github.com/vllm-project/vllm-ascend/pull/7487)[#6830](https://github.com/vllm-project/vllm-ascend/pull/6830)[#7506](https://github.com/vllm-project/vllm-ascend/pull/7506)[#7796](https://github.com/vllm-project/vllm-ascend/pull/7796)[#7527](https://github.com/vllm-project/vllm-ascend/pull/7527)[#7529](https://github.com/vllm-project/vllm-ascend/pull/7529)[#7495](https://github.com/vllm-project/vllm-ascend/pull/7495)[#7368](https://github.com/vllm-project/vllm-ascend/pull/7368)**Kimi-K2.x Performance**: [Experimental]Optimized the Kimi-K2.x performance by supporting eagle3 and flashcomm1, and reducing d2h overhead.[@aipaes](https://github.com/aipaes)[@dragondream-chen](https://github.com/dragondream-chen)[@SparrowMu](https://github.com/SparrowMu)[@LoganJane](https://github.com/LoganJane)[@GDzhu01](https://github.com/GDzhu01)[@Yaphets24](https://github.com/Yaphets24)[@hust17yixuan](https://github.com/hust17yixuan)[#7342](https://github.com/vllm-project/vllm-ascend/pull/7342)[#7390](https://github.com/vllm-project/vllm-ascend/pull/7390)[#7521](https://github.com/vllm-project/vllm-ascend/pull/7521)**Qwen3-VL Performance**: Qwen3-VL gets stronger multimodal operator enablement with Flash Comm V1 and`qkv_rmsnorm_mrope`

support, and enable 2.7x faster for convolution computation with aclnn BatchMatMulV2, support EAGLE speculative decoding.[#7893](https://github.com/vllm-project/vllm-ascend/pull/7893)[#7852](https://github.com/vllm-project/vllm-ascend/pull/7852)[#7017](https://github.com/vllm-project/vllm-ascend/pull/7017)[#6327](https://github.com/vllm-project/vllm-ascend/pull/6327)**Qwen3-Omni Performance**: Qwen3-Omni quantization adaptation and optimization is now available.[#6828](https://github.com/vllm-project/vllm-ascend/pull/6828)**DeepSeek-V3.2/GLM5 Performance**: Performance optimizations, support W8A8C8 quantization, and optimized KV cache usage.[@yydyzr](https://github.com/yydyzr)[@ZYang6263](https://github.com/ZYang6263)[@rjg-lyh](https://github.com/rjg-lyh)[@Nagisa125](https://github.com/Nagisa125)[#7029](https://github.com/vllm-project/vllm-ascend/pull/7029)[#6610](https://github.com/vllm-project/vllm-ascend/pull/6610)**GLM4.7-Flash Performance**: Added W8A8 quantization support for GLM4.7-Flash.[@aipaes](https://github.com/aipaes)[#6492](https://github.com/vllm-project/vllm-ascend/pull/6492)

### Dependencies

**vLLM**: Upgraded to 0.18.0 and dropped 0.17.0 support.**CANN**: Upgraded to 8.5.1.**PS:**AscendStoreConnector with FabricMem mode, 310P device supporting and Qwen3-Omni model need upgrades CANN version to 9.0.0, if you need these features, please upgrade manually.**torch-npu**: Upgraded to 2.9.0.post1+git4c901a4 because of some known issue. This version can't install by default, pleas...

[Read more](https://github.com/vllm-project/vllm-ascend/releases/tag/v0.18.0)

## v0.13.0rc3

## What's Changed

- [Doc][Misc] Update release notes and FAQ links for v0.13.0 by
[@wangxiyuan](https://github.com/wangxiyuan)in[#6585](https://github.com/vllm-project/vllm-ascend/pull/6585) - [BugFix][v0.13.0] fix a bug that patch from PR
[#5786](https://github.com/vllm-project/vllm-ascend/pull/5786)does not take effect by[@Angazenn](https://github.com/Angazenn)in[#6615](https://github.com/vllm-project/vllm-ascend/pull/6615) - [v0.13.0][Ops] Make triton rope support index_selecting from cos_sin_cache by
[@Angazenn](https://github.com/Angazenn)in[#6602](https://github.com/vllm-project/vllm-ascend/pull/6602) - [0.13.0][bugfix]fix profiler initialization bug with calling stack by
[@linfeng-yuan](https://github.com/linfeng-yuan)in[#6714](https://github.com/vllm-project/vllm-ascend/pull/6714) - [0.13.0] modify release note & supported matrix by
[@zzzzwwjj](https://github.com/zzzzwwjj)in[#6751](https://github.com/vllm-project/vllm-ascend/pull/6751) - [v0.13.0][Fusion]add checks to skip fusion where split_rmsnorm_rope is not supported by
[@Angazenn](https://github.com/Angazenn)in[#6749](https://github.com/vllm-project/vllm-ascend/pull/6749) - [DOC] add request forwarding (cherry-pick from
[#6780](https://github.com/vllm-project/vllm-ascend/pull/6780)) by[@starmountain1997](https://github.com/starmountain1997)in[#6788](https://github.com/vllm-project/vllm-ascend/pull/6788) - [Bugfix] Fix vllm-ascend 0.13.0 error:
`TypeError: apply_token_bitmask_inplace_cpu(): incompatible function arguments`

by[@wjunLu](https://github.com/wjunLu)in[#6823](https://github.com/vllm-project/vllm-ascend/pull/6823) - [Bugfix] mtp forces eager mode by
[@zhenwenqi2024](https://github.com/zhenwenqi2024)in[#6760](https://github.com/vllm-project/vllm-ascend/pull/6760) - [DOC] add layer_sharding and fix link by
[@starmountain1997](https://github.com/starmountain1997)in[#6808](https://github.com/vllm-project/vllm-ascend/pull/6808) - [v0.13.0][CI] Upgrade to CANN 8.5.1 by
[@wxsIcey](https://github.com/wxsIcey)in[#6865](https://github.com/vllm-project/vllm-ascend/pull/6865) - [Bugfix] Resolve operator name collision for DeepSeekV3.2 in RL scena… by
[@Mind-s](https://github.com/Mind-s)in[#7034](https://github.com/vllm-project/vllm-ascend/pull/7034) - [doc] Added Ascend PyTorch Profiler section by
[@herizhen](https://github.com/herizhen)in[#6905](https://github.com/vllm-project/vllm-ascend/pull/6905) - [0.13.0][cherry-pick][Bugfix][csrc] Add compile-time Ascend950/910_95 compatibility for custom ops between CANN8.5 and 9.0 by
[@zjchenn](https://github.com/zjchenn)in[#7116](https://github.com/vllm-project/vllm-ascend/pull/7116) - [0.13.0][cherry-pick][Bugfix][Triton] Centralize Ascend extension op dispatch in triton_utils by
[@zjchenn](https://github.com/zjchenn)in[#7112](https://github.com/vllm-project/vllm-ascend/pull/7112) - [Doc][Misc][v0.13.0] Updated the document configuration for DeepSeek-V3.2 by
[@Nagisa125](https://github.com/Nagisa125)in[#7957](https://github.com/vllm-project/vllm-ascend/pull/7957) - [CI] Fix Releases/v0.13.0 CI tests by
[@wjunLu](https://github.com/wjunLu)in[#7952](https://github.com/vllm-project/vllm-ascend/pull/7952) - [BugFix]Fix compilation errors for operators dispatch_gmm_combine_decode/moe_combine_normal/moe_dispatch_normal by
[@wangyibo1005](https://github.com/wangyibo1005)in[#7840](https://github.com/vllm-project/vllm-ascend/pull/7840) - [v0.13.0][Feature] Add DeepSeek v4 initial support by
[@wangxiyuan](https://github.com/wangxiyuan)in[#8648](https://github.com/vllm-project/vllm-ascend/pull/8648)

## New Contributors

**Full Changelog**: `v0.13.0...v0.13.0rc3`