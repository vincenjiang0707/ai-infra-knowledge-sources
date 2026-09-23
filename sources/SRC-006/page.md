# SGLang 学习资

source: https://github.com/sgl-project/sglang/releases

# Releases: sgl-project/sglang

## Release list

## v0.5.20

# Highlights

*713 PRs from 237 contributors.*

**New models in this release** (see the [cookbook](https://docs.sglang.io/cookbook) for all supported models):

| Model | Type | PRs | Cookbook |
|---|---|---|---|
| GLM-5.3-Flash | Autoregressive |
|

[link](https://docs.sglang.io/cookbook/autoregressive/GLM/GLM-5.3-Flash)[#36805](https://github.com/sgl-project/sglang/pull/36805)[link](https://docs.sglang.io/cookbook/autoregressive/Tencent/Hy4-Preview)[#37500](https://github.com/sgl-project/sglang/pull/37500)[link](https://docs.sglang.io/cookbook/autoregressive/Qwen/Qwen3.8-Flash-Next)[#37654](https://github.com/sgl-project/sglang/pull/37654),[#38033](https://github.com/sgl-project/sglang/pull/38033)[link](https://docs.sglang.io/cookbook/autoregressive/IFM/K2-Horizon)[#32151](https://github.com/sgl-project/sglang/pull/32151)[#36606](https://github.com/sgl-project/sglang/pull/36606)[link](https://docs.sglang.io/cookbook/diffusion/SenseNova/SenseNova-U1.5-8B-MoT)[#37480](https://github.com/sgl-project/sglang/pull/37480)[link](https://docs.sglang.io/cookbook/diffusion/MiniMax/MiniMax-H3)[#37903](https://github.com/sgl-project/sglang/pull/37903)[link](https://docs.sglang.io/cookbook/diffusion/MiniMax/MiniMax-H3)**Sampling masks for RL rollouts.** With `return_sampling_mask`

, each decode step returns the exact token support the sampler drew from and the log-probability of the sampled token under it, so a trainer can replay the rollout without reconstructing top-k or top-p ([#36630](https://github.com/sgl-project/sglang/pull/36630)). Masks now run under overlap scheduling: on Qwen3-8B, decode throughput is 17% higher at batch 1 and 52% higher at batch 64 than the previous implementation. Capacity is set by `--sampling-mask-max-tokens`

(default 4096) ([#36631](https://github.com/sgl-project/sglang/pull/36631)). `DisallowedTokensLogitsProcessor`

is supported alongside masks ([#38279](https://github.com/sgl-project/sglang/pull/38279)).

**Unified radix tree.** Branching-point caching for the SWA component keeps the sliding-window state at the point where requests fork from a shared prefix, so branches reuse it instead of recomputing. On DeepSeek-V4-Flash with a shared system prompt, token hit rate rises from 43.8% to 60.8% and mean TTFT falls from 1.57 s to 1.07 s ([#34565](https://github.com/sgl-project/sglang/pull/34565)). An opt-in external linker lets the tree address a shared global memory pool through Mooncake or UMBP ([#37381](https://github.com/sgl-project/sglang/pull/37381)).

**DSpark under PD with decode context parallelism.** A DCP1 prefill can now transfer its DSpark draft KV to a DCP-N decode, so hybrid models such as Kimi-Linear run DSpark in disaggregated, context-parallel serving. Verified on 8x B300 over NIXL and Mooncake up to 256K input ([#37709](https://github.com/sgl-project/sglang/pull/37709)).

**Responses API storage is opt-in.** `/v1/responses`

no longer retains results in memory unless the server starts with `--enable-response-store`

. Without it, retrieval, `previous_response_id`

chaining, and background requests return 400; PD deployments cannot enable it ([#39122](https://github.com/sgl-project/sglang/pull/39122)).

**SGLang Simulator.** A CPU-only simulator runs the real scheduler, radix cache, and hierarchical cache with a latency predictor in place of the model forward. Against measured serving traces it predicts TTFT within about 6% on most traces (up to 10% on the longest 32K to 128K ones) and prefix reuse within 0.05 percentage points, for cache and scheduling studies without GPUs ([#33824](https://github.com/sgl-project/sglang/pull/33824)).

**Prefill context parallelism v1 removed.** The strategy-based implementation is now the only prefill CP path; the v1 runtime and its CLI options are gone. Prefill CP on HIP, NPU, and MUSA is rejected until those platforms are ported ([#36228](https://github.com/sgl-project/sglang/pull/36228)).

**Faster model loading on ROCm.** Large pageable host-to-device copies are staged rather than pinned in place, which stops the driver from suspending GPU queues on every eviction. GLM-5.2 at TP4 on 4x MI355X loads in 40.4 s instead of 505.7 s ([#37720](https://github.com/sgl-project/sglang/pull/37720)).

**Intel XPU joins the release images.** Every tagged release now builds and publishes `lmsysorg/sglang:vX.Y.Z-xpu`

from the XPU Dockerfile, so Intel GPU users get a versioned image instead of relying on nightly builds ([#37340](https://github.com/sgl-project/sglang/pull/37340)).

**DeepSeek-V4 on Blackwell.** TRT-LLM attention kernels now cover DeepSeek-V4's CSA and HCA layers on SM100 and SM103: about 1.2x faster prefill and 1.45x faster decode than FlashMLA at the kernel level on B200 ([#30805](https://github.com/sgl-project/sglang/pull/30805)). FlashInfer MegaMoE is available as `--moe-runner-backend flashinfer_megamoe`

; on DeepSeek-V4-Flash NVFP4 at TP4/DP4 it adds up to 11.9% prefill throughput at 8192 tokens per rank, with decode within 2% of the trtllm runner at saturation ([#31470](https://github.com/sgl-project/sglang/pull/31470)).

**DeepSeek-V4 on RTX PRO 6000.** On SM120 the sparse-MLA indexer now runs on DeepGEMM's paged-MQA kernel and the DeepGEMM FP4 MoE backend is enabled, replacing the torch fallback that was the only working path. On 4x RTX PRO 6000, DeepSeek-V4-Flash decode TPOT drops from 36.1 to 10.5 ms at batch 1 and TTFT falls 20% from 8K to 128K input. Opt-in through the environment flags in the PR ([#29927](https://github.com/sgl-project/sglang/pull/29927)).

**Dependencies and images.** The CUDA 12 lane is retired; v0.5.19 was the last release with `-cu12x`

wheels and images ([#38404](https://github.com/sgl-project/sglang/pull/38404)). sglang-kernel moves to 0.4.7 ([#39346](https://github.com/sgl-project/sglang/pull/39346)) and sgl-deep-gemm to 0.2.0 ([#39371](https://github.com/sgl-project/sglang/pull/39371)). New images: ROCm 10 for MI30x and MI35x with a matching kernel wheel ([#38763](https://github.com/sgl-project/sglang/pull/38763)), gfx1151 for Strix Halo / Ryzen AI MAX+ ([#33939](https://github.com/sgl-project/sglang/pull/33939)), and Moore Threads MUSA ([#36709](https://github.com/sgl-project/sglang/pull/36709)). ROCm 7.0 CI, images, and kernel wheel are retired ([#38632](https://github.com/sgl-project/sglang/pull/38632), [#38767](https://github.com/sgl-project/sglang/pull/38767)).

*Full release notes by category below; breaking changes are at the end.*

## Speculative Decoding

- [Speculative Decoding] Add native UNO serving support:
[#37667](https://github.com/sgl-project/sglang/pull/37667) - feat: add optimized Domino rollout to DFlash V2:
[#36899](https://github.com/sgl-project/sglang/pull/36899) - feat: support TP>1 Domino rollout for DFlash V2:
[#37069](https://github.com/sgl-project/sglang/pull/37069) - [Spec] Stage Inkling MTP draft metadata before verify:
[#38169](https://github.com/sgl-project/sglang/pull/38169) - [Spec] Allow speculative workers to stage prefill shared reads:
[#38554](https://github.com/sgl-project/sglang/pull/38554) - [Spec] Support large MTP batches in short-convolution metadata:
[#38558](https://github.com/sgl-project/sglang/pull/38558) - [EAGLE] Prune draft-extend logits to selected rows (+2.5% output tokens/s/GPU at 102K context per rank):
[#35546](https://github.com/sgl-project/sglang/pull/35546) - [KDA] Support ReplaySSM ring-write in the fused chain-verify kernel:
[#36821](https://github.com/sgl-project/sglang/pull/36821) - [GDN] Amortize ReplaySSM checkpoint materialization:
[#35544](https://github.com/sgl-project/sglang/pull/35544) - perf(gdn): select ReplaySSM verify loop unrolling by shape:
[#36970](https://github.com/sgl-project/sglang/pull/36970) - Allow custom policy for adaptive speculative decoding:
[#37274](https://github.com/sgl-project/sglang/pull/37274) - Support speculative decoding with unified SWA memory:
[#36403](https://github.com/sgl-project/sglang/pull/36403) - Improve CUDA graph and speculative execution output handling:
[#37329](https://github.com/sgl-project/sglang/pull/37329) - Fix DSpark CUDA graph replay with MegaMoE TP attention:
[#34919](https://github.com/sgl-project/sglang/pull/34919) - [Fix][Mamba] Clear deferred init metadata before speculative decode:
[#37165](https://github.com/sgl-project/sglang/pull/37165) - [Fix] Track DFlash Mamba state at checkpoint boundaries:
[#37818](https://github.com/sgl-project/sglang/pull/37818) - [Fix] Load Qwen3.5 MTP embedding under PP:
[#37471](https://github.com/sgl-project/sglang/pull/37471) - fix: stop shadowing the DSpark shared-experts fusion guard:
[#39366](https://github.com/sgl-project/sglang/pull/39366) - [Profiler] Label draft-runner steps DRAFT and target verify VERIFY in step spans:
[#38630](https://github.com/sgl-project/sglang/pull/38630)

## Piecewise & Breakable CUDA Graph

- [Memory] Size the CUDA graph pool from warmup measurements and fix graph-pool borrowing:
[#36911](https://github.com/sgl-project/sglang/pull/36911) - [Memory] Retire graph borrow pool before updating static runs:
[#37966](https://github.com/sgl-project/sglang/pull/37966) - [Memory] Reuse output storage across full prefill CUDA graphs:
[#38038](https://github.com/sgl-project/sglang/pull/38038) - [Unified Memory] Enable prefill cuda-graph capture:
[#37418](https://github.com/sgl-project/sglang/pull/37418) - Decouple ragged CUDA graph request and token capacities:
[#37300](https://github.com/sgl-project/sglang/pull/37300)...

[Read more](https://github.com/sgl-project/sglang/releases/tag/v0.5.20)

## v0.5.19

# Highlights

*786 PRs from 214 contributors.*

**New models in this release** (see the [cookbook](https://docs.sglang.io/cookbook) for all supported models):

| Model | Type | PRs | Cookbook |
|---|---|---|---|
| Qwen3.8 (2.4T-A95B) | Autoregressive |
|

[link](https://docs.sglang.io/cookbook/autoregressive/Qwen/Qwen3.8)[#34859](https://github.com/sgl-project/sglang/pull/34859)[link](https://docs.sglang.io/cookbook/autoregressive/Qwen/Qwen3.8-27B)[#33829](https://github.com/sgl-project/sglang/pull/33829)⭐[link](https://docs.sglang.io/cookbook/autoregressive/RedNote/Dots3-Note)[#33561](https://github.com/sgl-project/sglang/pull/33561)[link](https://docs.sglang.io/cookbook/autoregressive/InclusionAI/Ling-3.0-flash)[#33561](https://github.com/sgl-project/sglang/pull/33561)[link](https://docs.sglang.io/cookbook/autoregressive/InclusionAI/Ling-3.0-tiny)[#35963](https://github.com/sgl-project/sglang/pull/35963)⭐[#30360](https://github.com/sgl-project/sglang/pull/30360)[#36286](https://github.com/sgl-project/sglang/pull/36286)[link](https://docs.sglang.io/cookbook/autoregressive/IBM/Granite-4.2)[#35829](https://github.com/sgl-project/sglang/pull/35829)**Cookbook updates:**

- GLM-5.3 deployment guide:
[link](https://docs.sglang.io/cookbook/autoregressive/GLM/GLM-5.3) - PaddleOCR-VL deployment guide:
[link](https://docs.sglang.io/cookbook/autoregressive/Baidu/PaddleOCR-VL) - Kimi-K3 on Ascend A3:
[#35508](https://github.com/sgl-project/sglang/pull/35508) - Kimi-K2.7-Code-MXFP4 on MI355X:
[#36246](https://github.com/sgl-project/sglang/pull/36246) - Qwen3.5 MXFP4 on MI355X with an FP8 KV cache or a HiCache host-memory tier:
[#35445](https://github.com/sgl-project/sglang/pull/35445),[#36245](https://github.com/sgl-project/sglang/pull/36245) - MiniMax-H3 on a 24 GB GPU or DGX Spark, with a consumer-GPU tuning guide:
[#36169](https://github.com/sgl-project/sglang/pull/36169),[#35816](https://github.com/sgl-project/sglang/pull/35816) - Ling-3.0-flash on DGX Spark:
[#36364](https://github.com/sgl-project/sglang/pull/36364) - Qwen3.8-27B on RTX 5090, RTX PRO 6000, and DGX Spark, re-measured:
[#35825](https://github.com/sgl-project/sglang/pull/35825)

**Beam search.** SGLang can now do beam search. Pass `beam_width`

in your request and you get back the `n`

best sequences instead of a single sample. It works out of the box next to regular requests, though it does not yet mix with speculative decoding, disaggregation, DP attention, or HiCache ([#31626](https://github.com/sgl-project/sglang/pull/31626)).

**DeepEP v2.** DeepEP's new ElasticBuffer engine is available as `--moe-a2a-backend deepep_v2`

for DeepSeek-V3/V4 and Qwen3-MoE in FP8. Its buffers have a fixed size, so decode can run under CUDA graphs even across nodes. Performance is on par with the classic backend ([#35634](https://github.com/sgl-project/sglang/pull/35634), [#34923](https://github.com/sgl-project/sglang/pull/34923)).

**LayerNorm sequence parallelism.** With `--enable-layernorm-sp`

, each tensor-parallel rank normalizes only its own share of the prefill tokens instead of all of them. That takes 3.5% off Qwen3-8B prefill on H100 and 5.6% on B200, and the saving grows with the TP degree. Dense Qwen3 models only for now ([#30915](https://github.com/sgl-project/sglang/pull/30915)).

**W4A8 MoE on Hopper.** If you serve MXFP4 experts on Hopper, you can now quantize the activations to FP8 as well with `--flashinfer-mxfp4-moe-precision fp8`

. DeepSeek-V4-Flash gains about 12% output throughput with no change in GSM8K accuracy. Needs FlashInfer 0.6.18 ([#34967](https://github.com/sgl-project/sglang/pull/34967)).

**DCP on the default Blackwell MLA backend.** Decode context parallelism now runs on `trtllm_mla`

, not just CuTe DSL and Tokenspeed. It pays off at long context: at 128K input, plain TP stops scaling around 680 tokens per second on eight B200s, while DCP keeps going as concurrency grows ([#33926](https://github.com/sgl-project/sglang/pull/33926)).

**Faster speculative kernels.** DSA prefill top-k moves to the v2 kernel, 1.3 to 1.8 times faster on B200 ([#35175](https://github.com/sgl-project/sglang/pull/35175)). KDA models get an opt-in fused accept path, `SGLANG_OPT_KDA_FUSED_ACCEPT_STATE=1`

, that cuts MTP verify-and-commit time by 45% to 63% on Kimi-Linear shapes with bit-identical output ([#33722](https://github.com/sgl-project/sglang/pull/33722)).

**Unified radix tree by default.** The unified tree is now the cache for every model, not just hybrid ones ([#35081](https://github.com/sgl-project/sglang/pull/35081), see Breaking Changes). It also picked up three things this cycle: PD decode workers can reuse cached prefixes for SWA hybrid models like gpt-oss ([#27770](https://github.com/sgl-project/sglang/pull/27770)), you can attach or detach L3 storage on a running server ([#35269](https://github.com/sgl-project/sglang/pull/35269)), and pipeline parallelism with HiCache L3 stays consistent across ranks ([#27010](https://github.com/sgl-project/sglang/pull/27010)).

**Lean attention on AMD.** Long or uneven decode batches used to leave many compute units idle on MI300X and MI355X. The new persistent Lean kernel spreads the work across all of them, for up to 1.52x more throughput and up to 3.62x lower inter-token latency on MI355X. It turns on by itself where it helps, and `SGLANG_DISABLE_LEAN_ATTENTION=1`

turns it off ([#33576](https://github.com/sgl-project/sglang/pull/33576)).

**DSA models on ROCm.** Disaggregated GLM-5.2 serving now uses the fused top-k seed remap, which brings decode TPOT from 23 ms down to 8 ms on eight MI355Xs ([#36714](https://github.com/sgl-project/sglang/pull/36714)). DeepSeek-V4 gets the v2 top-k kernel, up to three times faster ([#36684](https://github.com/sgl-project/sglang/pull/36684)), and a shared-experts gate fix gives GLM-5.2 up to 16% better TPOT ([#36124](https://github.com/sgl-project/sglang/pull/36124)).

**Dependencies.** FlashInfer moves to 0.6.18 ([#36954](https://github.com/sgl-project/sglang/pull/36954)), sgl-deep-ep to 0.1.2 ([#35450](https://github.com/sgl-project/sglang/pull/35450)), sgl-deep-gemm to 0.1.7 ([#37279](https://github.com/sgl-project/sglang/pull/37279)), and mooncake to 0.3.13 ([#36493](https://github.com/sgl-project/sglang/pull/36493)). There is a new CUDA 13.4 preview image for Rubin ([#36233](https://github.com/sgl-project/sglang/pull/36233)) and new ROCm 10 images for gfx942, gfx950, and gfx1250 ([#36434](https://github.com/sgl-project/sglang/pull/36434), [#36871](https://github.com/sgl-project/sglang/pull/36871)).

*Full release notes by category below; breaking changes and known issues are at the end.*

## Rust Server

- [Feature] Add process-local in-memory KV indexer and Router integration:
[#33370](https://github.com/sgl-project/sglang/pull/33370) - [Rust Server] Add e2e latency metadata and fix Sarashina import:
[#35125](https://github.com/sgl-project/sglang/pull/35125) - [Rust] Derive server address and accept signed env values:
[#37221](https://github.com/sgl-project/sglang/pull/37221) - [Rust] Keep sampling and scheduler wire schemas in sync:
[#37222](https://github.com/sgl-project/sglang/pull/37222) - Add configurable HTTP/2 connection window:
[#36920](https://github.com/sgl-project/sglang/pull/36920) - fix(gateway): bump wfaas to 1.0.2 so ContinueNextStep unblocks dependents:
[#37249](https://github.com/sgl-project/sglang/pull/37249)

## Speculative Decoding

- [KDA] Fused-accept state advance for FlashInfer KDA MTP verify:
[#33722](https://github.com/sgl-project/sglang/pull/33722)⭐ - [Spec] DFlash2: local convolution + candidate selector (3.43x over no-spec at batch 1 and about 24% over DFlash at concurrency 64):
[#35371](https://github.com/sgl-project/sglang/pull/35371) - [Spec] Support quantized target lm_head in the DFlash2 selector:
[#35496](https://github.com/sgl-project/sglang/pull/35496) - [Spec] Add LFM2 and LFM2-MoE DSpark speculative decoding support (1.05 to 2.42x faster decoding on LFM2.5 targets, 1xH100):
[#31041](https://github.com/sgl-project/sglang/pull/31041) - [Model] Support Nemotron 3.5 Lightning speculative decoding (GSM8K 94.6% to 95.8% across MTP, DFlash, and DSpark on GB300):
[#36186](https://github.com/sgl-project/sglang/pull/36186) - [Spec][LoRA] Support multi-adapter LoRA with EAGLE/NEXTN/DFLASH/DSPARK speculative decoding:
[#34337](https://github.com/sgl-project/sglang/pull/34337) - [Spec][DSA] Add --speculative-dsa-topk-backend:
[#36313](https://github.com/sgl-project/sglang/pull/36313) - [2/N][Mixed] Mixed chunk prefill with spec enabled:
[#36933](https://github.com/sgl-project/sglang/pull/36933) - Support custom draft worker classes in DSpark:
[#35397](https://github.com/sgl-project/sglang/pull/35397) - Make draft attention backends extensible:
[#35932](https://github.com/sgl-project/sglang/pull/35932) - [Memory] Borrow CUDA graph pool storage for EAGLE sampling:
[#35375](https://github.com/sgl-project/sglang/pull/35375) - [Spec] Fix Dspark and Dflash state divergence across TP rank:
[#33614](https://github.com/sgl-project/sglang/pull/33614) - [Fix][Spec] fix startup crash and reduce CUDA graph memory usage for speculative adaptive:
[#35275](https://github.com/sgl-project/sglang/pull/35275) - Fix DSV4 DSpark sample-from-anchor initialization:
[#36419](https://github.com/sgl-project/sglang/pull/36419) - [Fix] Drop the duplicated DSpark draft sample_block call:
[#36934](https://github.com/sgl-project/sglang/pull/36934) - fix(gemma4): quantize MTP bridge projections (Gemma-4 FP8 MTP acce...

[Read more](https://github.com/sgl-project/sglang/releases/tag/v0.5.19)

## v0.5.18

# Highlights

*710 PRs from 212 contributors.*

**New models in this release** (see the [cookbook](https://docs.sglang.io/cookbook) for all supported models):

| Model | Type | PRs | Cookbook |
|---|---|---|---|
| Muse Glimmer | Autoregressive (Multimodal) |
|

[link](https://docs.sglang.io/cookbook/autoregressive/Meta/MuseGlimmer)[#33691](https://github.com/sgl-project/sglang/pull/33691)[link](https://docs.sglang.io/cookbook/autoregressive/InternLM/Intern-S2-Mobius)[#32921](https://github.com/sgl-project/sglang/pull/32921)[link](https://docs.sglang.io/cookbook/diffusion/SANA-Video/SANA-Video)[#32341](https://github.com/sgl-project/sglang/pull/32341)[link](https://docs.sglang.io/cookbook/diffusion/LingBot-Video/LingBot-Video-MoE)[#34471](https://github.com/sgl-project/sglang/pull/34471)[link](https://docs.sglang.io/cookbook/diffusion/LTX/LTX2.5)[#31590](https://github.com/sgl-project/sglang/pull/31590)[link](https://docs.sglang.io/cookbook/diffusion/Cosmos/Cosmos3)[#23274](https://github.com/sgl-project/sglang/pull/23274)Plus cookbook recipes for the [Qwen3.8 family](https://docs.sglang.io/cookbook/autoregressive/Qwen/Qwen3.8), [Ling-3.0](https://docs.sglang.io/cookbook/autoregressive/InclusionAI/Ling-3.0-flash), [Nemotron 3.5 Lightning](https://docs.sglang.io/cookbook/autoregressive/NVIDIA/Nemotron3.5-Lightning), [Dots3-Note](https://docs.sglang.io/cookbook/autoregressive/RedNote/Dots3-Note), and DeepSeek-V4-Pro-0813 ([#34809](https://github.com/sgl-project/sglang/pull/34809)).

**Overlapped checkpoint staging at startup**: Checkpoint pages now stage from storage while CUDA graphs capture. Qwen3-32B on H100 starts **8.6-11.7% faster** than serial with prefetch, and **2.38x faster (35.6s vs 84.8s)** than the plain default. Opt in with `--startup-weight-load-mode overlap`

([#32017](https://github.com/sgl-project/sglang/pull/32017)).

**TP LMHead with All-to-All**: The TP LMHead's allgather + scatter becomes a single all-to-all for pure-DP dp-attention. On DeepSeek-V4-Pro B200 decode, LMHead time drops **320us to 169us** and TPOT improves 36.97ms to 35.67ms ([#32313](https://github.com/sgl-project/sglang/pull/32313)).

**FlashInfer MNNVL for pure allreduce**: Non-fused allreduce sites now reuse the FlashInfer MNNVL workspace instead of falling back to NCCL. DeepSeek-V4-Flash TP4 decode on Blackwell gains **up to +6.9% at small batches**. Auto-enabled for DeepSeek-V3/V3.2/V4; elsewhere `--enable-flashinfer-pure-allreduce`

([#30700](https://github.com/sgl-project/sglang/pull/30700)).

**NVFP4 checkpoints run on AMD**: `--quantization quark_mxfp4`

dequantizes ModelOpt and Quark NVFP4 weights and requantizes to MXFP4 at load, never holding a full-precision copy. 97.5-100.2% GSM8K recovery vs the NVFP4 reference across MiniMax-M2.7, GLM-5.1, Kimi-K2.6, Qwen3.5-397B, and DeepSeek-R1 ([#29328](https://github.com/sgl-project/sglang/pull/29328)).

**Kimi K3 tuned for MI355X**: a grouped-head MLA verify kernel replaces the MHA-shaped split-KV path that re-read the shared latent once per head, for **1.37-1.77x throughput and 1.45-2.42x ITL** at concurrency 2-32; the AITER MLA prefill kernel now accepts K3's 12-head shape (TTFT up to -14.9%); a gfx950-tuned decode stage-1 geometry adds **46-73% ITL** at 68k input, opt-in via `SGLANG_MLA_DECODE_TUNE=1`

. GSM8K holds at 0.951-0.957 ([#33981](https://github.com/sgl-project/sglang/pull/33981), [#34261](https://github.com/sgl-project/sglang/pull/34261), [#34837](https://github.com/sgl-project/sglang/pull/34837), [#34580](https://github.com/sgl-project/sglang/pull/34580)).

**One compiled-kernel cache directory**: Triton, FlashInfer, Inductor, DeepGEMM, and CUDA driver caches all move under `SGLANG_CACHE_DIR`

. The first launch after upgrading recompiles once; see Breaking Changes ([#32434](https://github.com/sgl-project/sglang/pull/32434)).

**Dependencies**: torch 2.13.0 with triton 3.7.1 ([#28836](https://github.com/sgl-project/sglang/pull/28836)), flashinfer 0.6.17 ([#33997](https://github.com/sgl-project/sglang/pull/33997)), CuTeDSL 4.6.2, fixing an FA4 startup regression on Blackwell ([#34372](https://github.com/sgl-project/sglang/pull/34372)), DeepEP now installed from released `sgl-deep-ep`

wheels ([#33932](https://github.com/sgl-project/sglang/pull/33932)), and sgl-kernel 0.4.6.post1 ([#33842](https://github.com/sgl-project/sglang/pull/33842)).

*Full release notes by category below; breaking changes and known issues are at the end.*

## Rust Server

- [mm] rust-server: native multimodal processing for Qwen VL (integrate sglang-mm, e2e):
[#32365](https://github.com/sgl-project/sglang/pull/32365) - refactor error responses into shared utils::response helpers:
[#33894](https://github.com/sgl-project/sglang/pull/33894) - move the PD bootstrap registry under api_server::disaggregation:
[#33895](https://github.com/sgl-project/sglang/pull/33895) - Build Rust extensions on demand in source checkouts:
[#34994](https://github.com/sgl-project/sglang/pull/34994)

## Speculative Decoding

- [spec decoding] support inkling dspark:
[#31847](https://github.com/sgl-project/sglang/pull/31847) - [Spec] Support logprobs with DSpark speculative decoding:
[#34696](https://github.com/sgl-project/sglang/pull/34696) - [Spec] Support output logprobs with DSpark:
[#34478](https://github.com/sgl-project/sglang/pull/34478) - [Spec] Support logprobs with DFlash:
[#33459](https://github.com/sgl-project/sglang/pull/33459) - [Spec] Wire DFLASH aux-hidden capture into the Qwen3.5 text-only wrapper:
[#34771](https://github.com/sgl-project/sglang/pull/34771) - [Spec] Support mamba-radix-cache-strategy extra_buffer_lazy with DFLASH:
[#34763](https://github.com/sgl-project/sglang/pull/34763) - [Spec] Support MegaMoE for DSpark under dp attention:
[#34844](https://github.com/sgl-project/sglang/pull/34844) - [unified memory] Support DSPARK speculative decoding + fix two NaN root causes (page hand-out zeroing, CuTe int32 slot-stride wrap):
[#33974](https://github.com/sgl-project/sglang/pull/33974) - [GDN] Honor configured linear-attn verify backend in the kernel dispatcher:
[#34592](https://github.com/sgl-project/sglang/pull/34592) - [Spec] Relay ngram accept tokens through the FutureMap:
[#35198](https://github.com/sgl-project/sglang/pull/35198) - [Spec] Reduce host-side overhead in ngram draft prep:
[#35207](https://github.com/sgl-project/sglang/pull/35207) - [Spec] Point multi-layer eagle's last shared-read runner at the draft runner:
[#35057](https://github.com/sgl-project/sglang/pull/35057) - Fix DFlash sliding attention causality defaults:
[#34524](https://github.com/sgl-project/sglang/pull/34524) - [Spec] Budget the DFLASH draft KV pool from its own attention geometry:
[#34234](https://github.com/sgl-project/sglang/pull/34234) - fix(dflash): account for DCP in draft KV pool sizing:
[#33912](https://github.com/sgl-project/sglang/pull/33912) - [DSV4] Fix silent KV corruption when speculative draft tokens > 4:
[#34189](https://github.com/sgl-project/sglang/pull/34189) - [Fix] Speculative decoding crashes with DP-Attention:
[#33892](https://github.com/sgl-project/sglang/pull/33892) - [bugfix] Stop/EOS inside a spec accept run beats the max_new_tokens finish:
[#33758](https://github.com/sgl-project/sglang/pull/33758) - [DSpark] Fix EP1 decode performance regression:
[#34759](https://github.com/sgl-project/sglang/pull/34759) - [Fix: RL] Snapshot async state-capture outputs before overlap:
[#34319](https://github.com/sgl-project/sglang/pull/34319)

## Piecewise & Breakable CUDA Graph

- [BCG][5/N] MLA Fully Support:
[#33661](https://github.com/sgl-project/sglang/pull/33661) - [BCG][6/N] Allow prefill breakable CUDA graph for the Kimi archs:
[#34245](https://github.com/sgl-project/sglang/pull/34245) - fix: always capture default prefill CUDA graph:
[#33352](https://github.com/sgl-project/sglang/pull/33352) - Fix padded positions in breakable CUDA Graph attention:
[#33253](https://github.com/sgl-project/sglang/pull/33253) - fix: avoid piecewise prefill graph for trtllm_mla:
[#32785](https://github.com/sgl-project/sglang/pull/32785) - Reenable breakable CUDA graph for NemotronH:
[#34538](https://github.com/sgl-project/sglang/pull/34538) - Fix prefill CP graph overflow with larger bucket search:
[#33906](https://github.com/sgl-project/sglang/pull/33906) - Fix stale track rows corrupting conv checkpoints under the prefill graph:
[#34184](https://github.com/sgl-project/sglang/pull/34184) - Fix sconv track refresh on graph capture:
[#35042](https://github.com/sgl-project/sglang/pull/35042) - Increase post-capture decode memory reserve:
[#34996](https://github.com/sgl-project/sglang/pull/34996)

## Attention Backends

- feat(attention): add architecture-owned SM12x FA4 kernels:
[#32991](https://github.com/sgl-project/sglang/pull/32991) - fix: support FA4 backend for GLM4.7-flash:
[#33436](https://github.com/sgl-project/sglang/pull/33436) - feat: Add flashinfer mHC fusion for DSV4:
[#33616](https://github.com/sgl-project/sglang/pull/33616) - [DSV4] Turn on mhc post pre fusion by default:
[#35214](https://github.com/sgl-project/sglang/pull/35214) - [SM12x] Default the fused MHC post+pre path on:
[#34019](https://github.com/sgl-project/sglang/pull/34019) - [trtllm_mha] perf: Stop allocating per-layer scratch inside the decode CUDA graph:
[#33063](https://github.com/sgl-project/sglang/pull/33063) - Select DeepGEMM standard layouts by memory budget:
[#33474](https://github.com/sgl-project/sglang/pull/33474) - [NVIDIA] Enable CuTe DSL BF16 GEMM on SM107:
[#33617](https://github.com/sgl-project/sglang/pull/33617) - add flashinfer cute-dsl backend for...

[Read more](https://github.com/sgl-project/sglang/releases/tag/v0.5.18)

## v0.5.17

# Highlights

*582 PRs from 194 contributors.*

**Kimi K3 day-0 support**: A 2.8T-parameter multimodal LatentMoE (896 experts, top-16, routed in a 3584-dim latent space) with a 1M-token context, 69 KDA linear-attention layers interleaved with 24 MLA layers, and a MoonViT3d vision tower, shipping as a native MXFP4 checkpoint. SGLang serves it from day 0 with DCP, DSpark speculative decoding, chunked-prefill PP with TP decode, KDA-aware prefix caching, HiCache L2 over DCP, LoRA on the quantized weights, and reasoning, tool-call and OpenAI-compatible serving, verified on NVIDIA GB300 and AMD MI35x ([#32541](https://github.com/sgl-project/sglang/pull/32541), [#32828](https://github.com/sgl-project/sglang/pull/32828), [#32890](https://github.com/sgl-project/sglang/pull/32890), [#33025](https://github.com/sgl-project/sglang/pull/33025), [#33112](https://github.com/sgl-project/sglang/pull/33112), [blog](https://www.lmsys.org/blog/2026-07-27-kimi-k3-day0-support), [cookbook](https://docs.sglang.io/cookbook/autoregressive/Moonshotai/Kimi-K3), [roadmap](https://github.com/sgl-project/sglang/issues/32607)).

**MiniMax-H3 day-0 support**: MiniMax's video generation model that produces a video and a synchronized stereo audio track in one request, served natively on SGLang-Diffusion across all three public task profiles: text-to-video-and-audio (`t2va`

), first/last-frame conditioning (`fl2va`

), and image/video/audio reference conditioning (`ref2va`

, which also covers video-to-video). Verified on B200 (TP2 + Ulysses4), H100 (TP2 + Ulysses2), AMD MI300X and MI355X (Ulysses1/2/4/8), and 2x RTX 5090 with layerwise offload ([#33275](https://github.com/sgl-project/sglang/pull/33275), [cookbook](https://docs.sglang.io/cookbook/diffusion/MiniMax/MiniMax-H3)).

**Other new models added**: [EmbeddingGemma](https://docs.sglang.io/cookbook/autoregressive/Google/EmbeddingGemma) and [LFM2.5](https://docs.sglang.io/cookbook/autoregressive/LiquidAI/LFM2.5) embedding models, nvidia/MiniMax-M3-NVFP4, plus cookbook recipes for Poolside's [Laguna-S-2.1](https://docs.sglang.io/cookbook/autoregressive/Poolside/Laguna-S-2.1) family and [Inkling-Small](https://docs.sglang.io/cookbook/autoregressive/ThinkingMachines/Inkling-Small).

**Initial support for the Rust frontend**: Migrates the front half of the server, everything from network ingress up to the point a tokenized request is handed to the GPU scheduler, from Python to a multi-threaded Rust implementation ([#29799](https://github.com/sgl-project/sglang/pull/29799)).

**DCP communication backends and q-replicate (Helix)**: The DeepSeek-MLA decode context-parallel path gains pluggable comm backends. `a2a`

exchanges packed attention output plus fp32 LSE in a single NCCL collective per layer, with fp8 KV carried as uint8 byte transport; `fi_a2a`

delegates the cross-rank exchange to the FlashInfer MNNVL kernel on GB200. `--dcp-replicate-q-proj`

projects full-head Q locally and skips the per-layer Q head-dim all-gather. Select with `--dcp-comm-backend {ag_rs, a2a, fi_a2a}`

([#21637](https://github.com/sgl-project/sglang/pull/21637)).

**DWDP for MoE prefill**: A new prefill parallelism strategy that prefetches peer expert weights over NVLink P2P and computes all experts locally, removing EP all-to-all token dispatch. On 4x B200 with gpt-oss-120b, prefill-only, DWDP4 reaches **1.92x over DEP4** at MNT 32K / ISL 32K, and **506K vs 329K tok/s (1.54x)** at saturation (CONC=128, ISL=8K). Enable with `--dwdp-size`

; the authors mark it early-development ([#29778](https://github.com/sgl-project/sglang/pull/29778)).

**Session-reference-aware Unified Radix Cache**: For agentic and RL-rollout workloads, requests can carry a stable `session_id`

so eviction knows which prefixes an active session still references, instead of evicting purely by cache policy. Release the references with `/close_session`

. Opt in with `--enable-session-radix-cache`

([#29173](https://github.com/sgl-project/sglang/pull/29173)).

**SM90 FP8 MegaMoE for DeepSeek-V4**: Adds the DeepGEMM MegaMoE A2A path on SM90 for DeepSeek-V4-Flash/Pro FP8, including the pre-dispatch JIT kernel and FP8 expert weight preparation. Guarded behind `SGLANG_OPT_USE_DEEPGEMM_MEGA_MOE=1`

([#29016](https://github.com/sgl-project/sglang/pull/29016)).

**Faster large-MoE model loading**: Oversized or non-contiguous CPU weight views were driving pathological H2D transfers, with DeepSeek-V4-Pro TP8 spending 27 to 32 minutes in H2D on some ranks. Copying those views into contiguous storage before H2D cuts full model loading from about **35 minutes to 6m20s (5.6x)**, and GPT-OSS-20B BF16 from **545s to 70s (7.8x)**, with Qwen3.5-397B measured at 1.93x to 2.3x. Opt in with `SGLANG_MOE_COPY_WEIGHT_VIEWS_BEFORE_H2D`

, off by default ([#32315](https://github.com/sgl-project/sglang/pull/32315)).

**Lower DeepSeek-V4 memory on AMD**: Removing unnecessary expert padding drops MI355X FP4 MoE model weights from **159.07 GB to 112.36 GB**, and bringing the HIP compress-state pool into the memory_saver KV_CACHE region lets colocated RL reclaim it, cutting the measured training-phase footprint from about **143 GiB to 87 GiB per GPU** ([#31450](https://github.com/sgl-project/sglang/pull/31450), [#31747](https://github.com/sgl-project/sglang/pull/31747)).

**Faster engine recovery**: Large-model restarts cost 3 to 6+ minutes today, about 6.5 minutes for Qwen3-235B FP8 on 4 GPUs, because weights reload from storage and CUDA graphs recapture. A weight-cache daemon holds weights per GPU so a restarting engine can recover from cache instead ([#27139](https://github.com/sgl-project/sglang/pull/27139)).

**Lower host overhead in hybrid-linear MTP decode**: Under spec-v2 overlap scheduling each decode step runs draft, verify and extend CUDA graphs, and the eager seams between them become GPU idle time at low concurrency. This trims that host work so the host stays off the critical path ([#32219](https://github.com/sgl-project/sglang/pull/32219)).

**Dependencies**: flashinfer 0.6.15.post1 ([#31927](https://github.com/sgl-project/sglang/pull/31927)), sgl-deep-gemm 0.1.5.post1 ([#32345](https://github.com/sgl-project/sglang/pull/32345), [#33143](https://github.com/sgl-project/sglang/pull/33143)), helion 1.4 ([#32562](https://github.com/sgl-project/sglang/pull/32562)), mooncake 0.3.12.post1 ([#32302](https://github.com/sgl-project/sglang/pull/32302)), dynamo-tokenizers 1.7.0 ([#32981](https://github.com/sgl-project/sglang/pull/32981)). PyTorch stays at 2.11.0 and the CUDA base image at 13.0.1.

*Full release notes by category below; breaking changes and known issues are at the end.*

## New Model Support

| Model | Type | PRs | Cookbook |
|---|---|---|---|
| Kimi K3 | Autoregressive (Multimodal) |
|

[link](https://docs.sglang.io/cookbook/autoregressive/Moonshotai/Kimi-K3)[#33275](https://github.com/sgl-project/sglang/pull/33275)[link](https://docs.sglang.io/cookbook/diffusion/MiniMax/MiniMax-H3)[#31989](https://github.com/sgl-project/sglang/pull/31989)[#32375](https://github.com/sgl-project/sglang/pull/32375),[#32383](https://github.com/sgl-project/sglang/pull/32383)[link](https://docs.sglang.io/cookbook/autoregressive/Google/EmbeddingGemma)[#28691](https://github.com/sgl-project/sglang/pull/28691)[link](https://docs.sglang.io/cookbook/autoregressive/LiquidAI/LFM2.5)## Kimi K3

- [Kimi] Support kimi-k3:
[#32541](https://github.com/sgl-project/sglang/pull/32541)⭐ - [Kimi] Support DCP + DSpark (ported from kimi-k3 branch):
[#32828](https://github.com/sgl-project/sglang/pull/32828) - [Kimi K3] Add reasoning, tool-call, and OpenAI serving support:
[#33025](https://github.com/sgl-project/sglang/pull/33025) - feat(kernels): port standalone Kimi K3 kernels:
[#32890](https://github.com/sgl-project/sglang/pull/32890) - [Feat] DCP + HiCache L2 Support (ported from kimi-k3):
[#33112](https://github.com/sgl-project/sglang/pull/33112) - Replace Kimi K3 DeepGEMM patch with 0.1.5.post1:
[#33143](https://github.com/sgl-project/sglang/pull/33143) - docker: add Kimi K3 images:
[#32760](https://github.com/sgl-project/sglang/pull/32760)

## Rust Server

A native Rust serving layer: tokenizer manager, ingress validation and egress, an OpenAI-compatible API server, and PD disaggregation support, shipped as prebuilt release artifacts.

- support rust sglang server:
[#29799](https://github.com/sgl-project/sglang/pull/29799) - create rust workspace:
[#32014](https://github.com/sgl-project/sglang/pull/32014) - init sglang rust server project:
[#32256](https://github.com/sgl-project/sglang/pull/32256) - add the rust server tokenizer, detokenizer, and egress modules:
[#32872](https://github.com/sgl-project/sglang/pull/32872) - add the rust server ingress request validation and api server common types:
[#32873](https://github.com/sgl-project/sglang/pull/32873) - add the rust server ingress tests, guard, and submit modules:
[#32874](https://github.com/sgl-project/sglang/pull/32874) - add the rust server api frame codec and http server entry:
[#32875](https://github.com/sgl-project/sglang/pull/32875) - add the rust server native api handlers and runtime threads:
[#32876](https://github.com/sgl-project/sglang/pull/32876) - wire the rust server modules into lib, runtime, and tokenizer manager:
[#32877](https://github.com/sgl-project/sglang/pull/32877) - sglang rust server tokenizer manager, ring and runtime:
[#32358](https://github.com/sgl-project/sglang/pull/32358) - feat: rust sglang server openai apis: [
[#33103](https://github.com/sgl-project/sglang/pull/33103)]([https://github.com/sgl-proj](https://github.com/sgl-proj)...

[Read more](https://github.com/sgl-project/sglang/releases/tag/v0.5.17)

## v0.5.16

# Highlights

*574 PRs from 169 contributors.*

**DSpark: confidence-driven speculative decoding**: A new speculative algorithm. It drafts semi-autoregressively in blocks, then sizes each verify window from the draft's own confidence instead of a fixed draft length. Reaches **383.7 tok/s at accept length ~5** on DeepSeek-V4-Pro, TP8 on B300 (bs=1). Enable with `--speculative-algorithm DSPARK`

and `SGLANG_RAGGED_VERIFY_MODE=compact`

; tune the block with `--speculative-dspark-block-size`

([#30261](https://github.com/sgl-project/sglang/pull/30261), [#31434](https://github.com/sgl-project/sglang/pull/31434), [blog](https://www.lmsys.org/blog/2026-07-06-dspark-sglang)).

**Inkling support**: A 975B-parameter multimodal MoE with a 1M-token context. It mixes sliding-window, full and Mamba2 linear attention, and adds an NVFP4 MoE, optional vision/audio towers and native MTP. On Blackwell it reaches up to **71.7k tok/s input** and **171.0 tok/s per-user decode**. Verified on Blackwell TP4/TP8, H200 and AMD MI350X / MI355X ([#31681](https://github.com/sgl-project/sglang/pull/31681), [blog](https://www.lmsys.org/blog/2026-07-15-inkling-day0-support), [cookbook](https://docs.sglang.io/cookbook/autoregressive/ThinkingMachines/Inkling)).

**Other new models added**: [LongCat 2.0 FP8](https://docs.sglang.io/cookbook/autoregressive/Meituan/LongCat-2.0), JetBrains Mellum v2, [Pi0.5](https://docs.sglang.io/cookbook/vla/OpenPI/Pi0.5), plus diffusion support for [LongLive 2.0](https://docs.sglang.io/cookbook/diffusion/LongLive/LongLive-2.0).

**UnifiedRadixTree is now the default** for SWA, Mamba and DSA models. Replay SSM and Mamba int8 checkpoints are synced onto it, and a cache hit now resets only the state it used ([#30468](https://github.com/sgl-project/sglang/pull/30468), [#30636](https://github.com/sgl-project/sglang/pull/30636), [#30626](https://github.com/sgl-project/sglang/pull/30626), [#31643](https://github.com/sgl-project/sglang/pull/31643)).

**GLM-5.2 DSA cache layer split under prefill CP**: KV and indexer cache layers are sharded across CP ranks. Each rank owns a disjoint layer range instead of all layers. That cuts per-rank KV memory by **~74%** (0.77 to 0.20 GB/rank) at 8192 tokens on GLM-5.2-FP8, 78 layers, cp_size=4. Enable with `--enable-dsa-cache-layer-split`

, which needs `--enable-prefill-cp --cp-strategy interleave`

([#29421](https://github.com/sgl-project/sglang/pull/29421)).

**ReplaySSM Ring Spec-Verify (GDN)**: Drops the per-draft SSM snapshot. Speculative scratch goes from **11.5 GB to 1.8 GB per GPU (6.4x smaller)** on Qwen3.5-35B-A3B at TP1, at accuracy and throughput parity. Opt in with `--enable-gdn-replayssm-spec`

(default off; GDN with a linear draft chain only, `--speculative-eagle-topk`

in {None, 1}), and tune the ring via `--linear-replayssm-cache-len`

([#28695](https://github.com/sgl-project/sglang/pull/28695)).

**Linear attention on Blackwell (SM100)**: The first correct KDA MTP path. Its `recurrent_kda`

decode kernel runs at **29.6 us vs 36.8 us** for Triton (ncu, B=64). The full decode path reaches parity by B=128 and **1.35x at B=256**, and is slower below that ([#30113](https://github.com/sgl-project/sglang/pull/30113)). Separately, GDN/KDA CuteDSL prefill fuses state I/O into the chunk-h kernel ([#30169](https://github.com/sgl-project/sglang/pull/30169)).

**QServe and FBGEMM FP8 quantization are removed**: the experimental QServe (QoQ) W4A8 and FBGEMM FP8 paths are gone. `--fp4-gemm-backend cutlass`

goes too, along with the in-tree NVFP4 JIT kernels, so NVFP4 GEMM now requires FlashInfer ([#31109](https://github.com/sgl-project/sglang/pull/31109), [#30448](https://github.com/sgl-project/sglang/pull/30448)).

**Dependencies**: flashinfer 0.6.14 ([#29910](https://github.com/sgl-project/sglang/pull/29910)), CuTe DSL 4.6.0 ([#31714](https://github.com/sgl-project/sglang/pull/31714)), sgl-kernel 0.4.5 ([#31496](https://github.com/sgl-project/sglang/pull/31496)), llguidance 1.7.6 ([#31484](https://github.com/sgl-project/sglang/pull/31484)).

## Breaking Changes & Upgrade Notes

**The experimental QServe (QoQ) W4A8 and FBGEMM FP8 quantization paths are removed**(per[#28543](https://github.com/sgl-project/sglang/issues/28543)):[#31109](https://github.com/sgl-project/sglang/pull/31109)**CUTLASS FP8 blockwise deleted for SM90 / SM100**, SM120 moved to JIT:[#30438](https://github.com/sgl-project/sglang/pull/30438)along with the in-tree NVFP4 JIT kernels, so NVFP4 GEMM now requires FlashInfer. Use`--fp4-gemm-backend cutlass`

is removed`auto`

, which picks`flashinfer_cutedsl`

on SM100 and`flashinfer_cutlass`

on SM120:[#30448](https://github.com/sgl-project/sglang/pull/30448)for SWA, Mamba and DSA models. A behavior change on those architectures:`UnifiedRadixTree`

is now the default[#30468](https://github.com/sgl-project/sglang/pull/30468)**Chunked input-logprob processing is now on by default**to cap peak memory:[#31498](https://github.com/sgl-project/sglang/pull/31498)**FA3 sparse mask kernels are off by default**:[#30356](https://github.com/sgl-project/sglang/pull/30356)**Legacy Sphinx**; the Mintlify cutover is complete:`docs/`

removed[#28964](https://github.com/sgl-project/sglang/pull/28964): kernels are relocated verbatim and only import paths change; public wrappers keep defaulting to the AOT`sglang.kernels`

namespace`sgl_kernel`

backend, so code reaching past them to internal paths must update (RFC[#29630](https://github.com/sgl-project/sglang/issues/29630)):[#30044](https://github.com/sgl-project/sglang/pull/30044),[#31582](https://github.com/sgl-project/sglang/pull/31582)across spec-decoding runners:`num_tokens_per_bs`

renamed to`num_tokens_per_req`

[#30977](https://github.com/sgl-project/sglang/pull/30977)with no deprecated alias, so existing launch commands fail with`--enable-deepep-waterfill`

is renamed to`--enable-waterfill`

`unrecognized arguments`

:[#27350](https://github.com/sgl-project/sglang/pull/27350)with no deprecated alias:`--optimistic-prefill-retries`

is renamed to`--optimistic-prefill-attempts`

[#30951](https://github.com/sgl-project/sglang/pull/30951)**The SGLang-Diffusion post-training rollout endpoint now returns**instead of JSON, with tensors as raw msgpack bytes rather than base64 (`application/msgpack`

`tensor_to_base64`

/`base64_to_tensor`

become`tensor_to_bytes`

/`bytes_to_tensor`

), so RL rollout consumers must be upgraded in lockstep with the server:[#31565](https://github.com/sgl-project/sglang/pull/31565)

## Known Issues

**Temperature-0 nondeterminism under DP attention with breakable prefill CUDA graph.**On the DSV4-Flash FP4 recipe, the idle-rank dummy extend introduced by[#30898](https://github.com/sgl-project/sglang/pull/30898)perturbs real requests' logits, so identical temperature-0 requests can diverge. The guarding determinism test is disabled as a stopgap rather than fixed ([#31125](https://github.com/sgl-project/sglang/pull/31125)); not enabling breakable prefill CUDA graph avoids the path.- A bump to
**flashinfer 0.6.15**was landed and reverted this cycle; this release pins**0.6.14**([#31502](https://github.com/sgl-project/sglang/pull/31502),[#31625](https://github.com/sgl-project/sglang/pull/31625)). **Mamba track-boundary seqlen under the overlap scheduler**was fixed and then reverted ([#31369](https://github.com/sgl-project/sglang/pull/31369),[#31622](https://github.com/sgl-project/sglang/pull/31622)). The underlying issue is still open.**CPU AMX optimizations for diffusion**were reverted ([#28527](https://github.com/sgl-project/sglang/pull/28527),[#30716](https://github.com/sgl-project/sglang/pull/30716)).**GB300 CI jobs were temporarily disabled**for runner availability during this cycle ([#31764](https://github.com/sgl-project/sglang/pull/31764)), so GB300 coverage rests on the cookbook's manual end-to-end validation.

*Full release notes by category below.*

## New Model Support

| Model | Type | PRs | Cookbook |
|---|---|---|---|
Inkling |
autoregressive |
|

[link](https://docs.sglang.io/cookbook/autoregressive/ThinkingMachines/Inkling)**LongCat 2.0**[#30275](https://github.com/sgl-project/sglang/pull/30275),[#30320](https://github.com/sgl-project/sglang/pull/30320)[link](https://docs.sglang.io/cookbook/autoregressive/Meituan/LongCat-2.0)**JetBrains Mellum v2**[#27375](https://github.com/sgl-project/sglang/pull/27375)**Pi0.5**[#30633](https://github.com/sgl-project/sglang/pull/30633)[link](https://docs.sglang.io/cookbook/vla/OpenPI/Pi0.5)**LongLive 2.0**[#27639](https://github.com/sgl-project/sglang/pull/27639)[link](https://docs.sglang.io/cookbook/diffusion/LongLive/LongLive-2.0)Landed this cycle but not yet usable end-to-end: **MiniMax-M3** completes its four-part landing ([#28715](https://github.com/sgl-project/sglang/pull/28715), begun in v0.5.14) but its [cookbook](https://docs.sglang.io/cookbook/autoregressive/MiniMax/MiniMax-M3) still points at a dev image ([#31819](https://github.com/sgl-project/sglang/pull/31819)).

## Inkling

- Add Inkling model support:
[#31681](https://github.com/sgl-project/sglang/pull/31681)⭐ - Add Inkling cookbook:
[#31360](https://github.com/sgl-project/sglang/pull/31360) - [Docs] Inkling cookbook: mark B300/GB300 recipes verified, tune B300 MTP mem fractions:
[#31550](https://github.com/sgl-project/sglang/pull/31550) - [Cookbook] Inkling: add measured accuracy numbers to benchmark cards:
[#31823](https://github.com/sgl-project/sglang/pull/31823) - [Docs] Inkling cookbook: LoRA cells require --disable-prefill-cuda-graph:
[#31418](https://github.com/sgl-project/sglang/pull/31418) - Fix dropped Inkling reasoning at stream end:
[#31787](https://github.com/sgl-project/sglang/pull/31787) - [Spec] fix inkling multi lay...

[Read more](https://github.com/sgl-project/sglang/releases/tag/v0.5.16)

## v0.5.15.post1

v0.5.15.post1 includes a few patches, mostly for GLM 5.2

[#30454](https://github.com/sgl-project/sglang/pull/30454)[#30627](https://github.com/sgl-project/sglang/pull/30627): Fix DSA model launching on non Cuda/HIP devices[#30858](https://github.com/sgl-project/sglang/pull/30858): Fix flashinfer dependency on Cuda 12 images[#31001](https://github.com/sgl-project/sglang/pull/31001): Fix NaN outputs caused by flashinfer trtllm FP4 MoE kernels on long input[#30839](https://github.com/sgl-project/sglang/pull/30839): Fix GLM 5.2 IndexShare on PD disaggregation setting[#30992](https://github.com/sgl-project/sglang/pull/30992): Fix GLM 5.2 IndexShare on Context Parallel setting

## v0.5.15

# Highlights

**GLM-5.2 NVFP4, tuned for production**: We took time this cycle to tune GLM-5.2 NVFP4 on Blackwell for optimized production serving. It now runs at **500+ tok/s/user on 8x B300, 450 on 4x GB300** (bs=1). Run GLM-5.2 with our [cookbook](https://docs.sglang.io/cookbook/autoregressive/GLM/GLM-5.2).

**Spec V2 by default**: zero-overhead scheduling via CUDA-graphable DSA draft-extend, dropped D2H/H2D syncs, fused metadata ops. +11% end-to-end TPS ([#29413](https://github.com/sgl-project/sglang/pull/29413),[#29343](https://github.com/sgl-project/sglang/pull/29343),[#29166](https://github.com/sgl-project/sglang/pull/29166),[#29077](https://github.com/sgl-project/sglang/pull/29077)).**IndexShare MTP**: reuses the indexer top-k across draft steps, up to 1.9x lower draft-step cost at long context ([#29959](https://github.com/sgl-project/sglang/pull/29959),[#29787](https://github.com/sgl-project/sglang/pull/29787),[#29654](https://github.com/sgl-project/sglang/pull/29654)).**TopK V2**: fuses top-k selection with the page-table transform, runtime k up to 2048 ([#30274](https://github.com/sgl-project/sglang/pull/30274),[#26788](https://github.com/sgl-project/sglang/pull/26788)).**Indexer prologue fusion**: 12 kernels to 4, ~8% faster decode at bs=1 ([#27705](https://github.com/sgl-project/sglang/pull/27705)).**GEMM**: shape-specialized JIT router GEMM + CuteDSL BF16 GEMM for Blackwell ([#21531](https://github.com/sgl-project/sglang/pull/21531),[#30117](https://github.com/sgl-project/sglang/pull/30117)).**FlashInfer autotune**: now covers draft-model graphs ([#29595](https://github.com/sgl-project/sglang/pull/29595)).

**New Model Support**: [Hunyuan 3 (Hy3)](https://docs.sglang.io/cookbook/autoregressive/Tencent/Hy3), Hierarchical Reasoning Model (HRM-Text), NVIDIA LocateAnything-3B, [Baidu Unlimited-OCR](https://docs.sglang.io/cookbook/autoregressive/Baidu/Unlimited-OCR), [JoyEcho](https://docs.sglang.io/cookbook/diffusion/JoyEcho/JoyEcho) multi-shot A/V, plus [Qwen3.6](https://docs.sglang.io/cookbook/autoregressive/Qwen/Qwen3.6) NVFP4 support.

**Native web search (Exa)**: Built-in `web_search`

support backed by Exa ([#29342](https://github.com/sgl-project/sglang/pull/29342)).

**Breakable CUDA Graph on by default**: Breakable CUDA Graph is now the default capture path, reducing per-step kernel-launch overhead ([#29458](https://github.com/sgl-project/sglang/pull/29458)); full CUDA Graph support for the prefill phase lands as experimental ([#27988](https://github.com/sgl-project/sglang/pull/27988)).

**Linear-attention kernels (KDA / GDN)**: New FlashKDA prefill backend for safe-gate KDA linear attention ([#29472](https://github.com/sgl-project/sglang/pull/29472)), plus ReplaySSM buffered output-only decode for linear attention ([#28451](https://github.com/sgl-project/sglang/pull/28451)).

**FlashInfer A2A for routed MoE**: Adds FlashInfer all-to-all with the `flashinfer_trtllm_routed`

MoE runner ([#22394](https://github.com/sgl-project/sglang/pull/22394)).

**DeepSeek-V4 Optimization**:

- Optimizes C128 state-pool allocation using the request state pool (
[#28612](https://github.com/sgl-project/sglang/pull/28612)). - FlashMLA sparse prefill is now enabled by default for DeepSeek-V4, reaching >10% throghput gain on long context. (
[#29775](https://github.com/sgl-project/sglang/pull/29775)). - Non paged indexer support for long context prefill, with >5% e2e throughput gain.(
[#29619](https://github.com/sgl-project/sglang/pull/29619)).

**Decode Context Parallelism**: decode context parallelism lands for MLA models, including DeepSeek V3 and Kimi K2 series ([#14194](https://github.com/sgl-project/sglang/pull/14194)).

**Dependency upgrades**: `transformers`

bumped to 5.12.1 ([#29393](https://github.com/sgl-project/sglang/pull/29393)); `tvm-ffi`

/ `sgl-deep-gemm`

/ `tilelang`

upgraded ([#29554](https://github.com/sgl-project/sglang/pull/29554)).

and . See the [DeepSeek-V4 cookbook](https://docs.sglang.io/cookbook/autoregressive/DeepSeek/DeepSeek-V4).

*Full release notes by category below.*

## New Model Support

- Hunyuan 3 (Hy3):
[#30201](https://github.com/sgl-project/sglang/pull/30201)([cookbook](https://docs.sglang.io/cookbook/autoregressive/Tencent/Hy3)) - Hierarchical Reasoning Model (HRM-Text):
[#27887](https://github.com/sgl-project/sglang/pull/27887) - NVIDIA LocateAnything-3B:
[#28958](https://github.com/sgl-project/sglang/pull/28958) - Baidu Unlimited-OCR:
[#29186](https://github.com/sgl-project/sglang/pull/29186)([cookbook](https://docs.sglang.io/cookbook/autoregressive/Baidu/Unlimited-OCR)) - JoyEcho multi-shot A/V:
[#27420](https://github.com/sgl-project/sglang/pull/27420)([cookbook](https://docs.sglang.io/cookbook/diffusion/JoyEcho/JoyEcho)) - Qwen3.6 ModelOpt mixed NVFP4:
[#27906](https://github.com/sgl-project/sglang/pull/27906),[#29905](https://github.com/sgl-project/sglang/pull/29905)([cookbook](https://docs.sglang.io/cookbook/autoregressive/Qwen/Qwen3.6)) ⭐

## GLM-5.2

- [BCG][GLM5] perf: BCG support and prefill enhancements:
[#27053](https://github.com/sgl-project/sglang/pull/27053)⭐ - [CI] Add GLM52 NVFP4 MTP B200 tests:
[#30021](https://github.com/sgl-project/sglang/pull/30021) - [cookbook] GLM-5.2 NVFP4 B300: TP8 recipe + 3 strategies:
[#29557](https://github.com/sgl-project/sglang/pull/29557) - [Cookbook] GLM-5.2: tune GB300 NVFP4 recipes + fill benchmarks:
[#29486](https://github.com/sgl-project/sglang/pull/29486) - [cookbook] drop redundant serve flags (GLM-5.2) + fix M3 page-size note:
[#28731](https://github.com/sgl-project/sglang/pull/28731) - [Docs] Add NVFP4 quantization to GLM-5.2 cookbook:
[#29380](https://github.com/sgl-project/sglang/pull/29380) - [DSA][GLM5.2] Index Share for MHA:
[#29959](https://github.com/sgl-project/sglang/pull/29959) - [GLM-5] Tune the threshold of router GEMM:
[#29470](https://github.com/sgl-project/sglang/pull/29470) - [Spec] Anchor GLM-5.2 MTP IndexShare topk on the draft-extend step:
[#29787](https://github.com/sgl-project/sglang/pull/29787) - Bypass legacy GLM DSA layer types validation:
[#29454](https://github.com/sgl-project/sglang/pull/29454) - docs: add B200 NVFP4 recipes + benchmarks to GLM-5.2 cookbook:
[#29674](https://github.com/sgl-project/sglang/pull/29674) - docs: add PD disaggregation to GLM-5.2 cookbook playground:
[#29544](https://github.com/sgl-project/sglang/pull/29544) - docs(cookbook): add AMD MI300X/MI325X/MI355X support for GLM-5.2:
[#28471](https://github.com/sgl-project/sglang/pull/28471) - Fuse the DSA (V3.2, GLM-5.x) indexer Q/K paths into single kernels:
[#27705](https://github.com/sgl-project/sglang/pull/27705)⭐ - glm5.2 on ascend doc (new version):
[#29828](https://github.com/sgl-project/sglang/pull/29828) - Support JIT fused A GEMM (MLA down projection) and support GLM-5 hidden size, SM120:
[#27397](https://github.com/sgl-project/sglang/pull/27397) - Update GLM-5.2 B300 and GB300 NVFP4 cookbook settings:
[#29466](https://github.com/sgl-project/sglang/pull/29466) - Update GLM tests to 5.2 and delete redundant tests:
[#29686](https://github.com/sgl-project/sglang/pull/29686) - [AMD] [GLM5] Guard cuda_runtime.h for ROCm in fused_metadata_copy:
[#29373](https://github.com/sgl-project/sglang/pull/29373) - [AMD] [GLM5] Mark EAGLE verified on MI300X/MI325X (gfx942) in GLM-5.1 cookbook:
[#29313](https://github.com/sgl-project/sglang/pull/29313) - [AMD] [GLM5] GLM-5.1 MXFP4 (MI355X) + enable EAGLE for gfx950 in cookbook:
[#29194](https://github.com/sgl-project/sglang/pull/29194) - [AMD] [GLM5] Add opt-in Triton fp8 sparse-MLA prefill kernel for gfx950:
[#28975](https://github.com/sgl-project/sglang/pull/28975) - [AMD] [GLM5] skip redundant -inf pre-fill of HIP indexer MQA-logits:
[#28757](https://github.com/sgl-project/sglang/pull/28757)

## DeepSeek V4

- [DeepSeek V4] Enable FlashMLA sparse prefill by default:
[#29775](https://github.com/sgl-project/sglang/pull/29775)⭐ - [DeepSeek-V4] Add an opt-in non-paged indexer for long-context prefill:
[#29619](https://github.com/sgl-project/sglang/pull/29619)⭐ - [DSA] Fold page-table into fused top-k v2 (decode): drop page_size=1 expansion:
[#30274](https://github.com/sgl-project/sglang/pull/30274) - [JIT Kernel] DeepSeek-V4 DSA indexer: faster top-k + page-table transform (runtime k <= 2048):
[#26788](https://github.com/sgl-project/sglang/pull/26788)⭐ - [Cherry-pick to release/v0.5.15] [DSA] Fix IMA in fused top-k v2: write all output slots on tie overflow (
[#30512](https://github.com/sgl-project/sglang/pull/30512)):[#30559](https://github.com/sgl-project/sglang/pull/30559) - [Cherry-pick to release/v0.5.15] [DSV4] perf: Make FP8 quant output tensor contiguous (
[#27926](https://github.com/sgl-project/sglang/pull/27926)):[#30449](https://github.com/sgl-project/sglang/pull/30449) - [Cherry-pick to release/v0.5.15] [DeepSeek-V4] Enable non-paged indexer by default for large prefill chunks (
[#30140](https://github.com/sgl-project/sglang/pull/30140)):[#30436](https://github.com/sgl-project/sglang/pull/30436) - [Cherry-pick to release/v0.5.15] [DSA] Re-enable fused top-k v2 for MTP: clamp padded-row seq_lens to >= 0 (
[#30378](https://github.com/sgl-project/sglang/pull/30378)):[#30427](https://github.com/sgl-project/sglang/pull/30427) - [AMD] Improve performance of DSV4 in high concurrency:
[#28938](https://github.com/sgl-project/sglang/pull/28938) - [AMD] DSV4 aiter reduce-scatter decode:
[#29103](https://github.com/sgl-project/sglang/pull/29103) - [AMD][DSV4] Remove per-batch D2H syncs in MTP to avoid bubbles between 2 batches:
[#29420](https://github.com/sgl-project/sglang/pull/29420) - [AMD][DeepSeek V4] Fix default FlashMLA sparse prefill off on ROCm/HIP:
[#29982](https://github.com/sgl-project/sglang/pull/29982) - [AMD] Fix DeepSeek V4 MTP accuracy issue:
[#30333](https://github.com/sgl-project/sglang/pull/30333) - [AMD] Fix dsv4 indexer dtype dispatch on gfx950:
[#29479](https://github.com/sgl-project/sglang/pull/29479) - [AMD] Cap DSV4 Flash max_total_num_tokens:
[#30313](https://github.com/sgl-project/sglang/pull/30313) - [AMD] Fix DeepSeekV4 serve...

[Read more](https://github.com/sgl-project/sglang/releases/tag/v0.5.15)

## v0.5.14

# Highlights

New Model Support: [GLM-5.2](https://docs.sglang.io/cookbook/autoregressive/GLM/GLM-5.2), [LiquidAI LFM2.5](https://docs.sglang.io/cookbook/autoregressive/LiquidAI/LFM2.5), [Kimi-K2.7-Code](https://docs.sglang.io/cookbook/autoregressive/Moonshotai/Kimi-K2.7-Code), [Poolside Laguna-M.1](https://docs.sglang.io/cookbook/autoregressive/Poolside/Laguna-M.1), [DiffusionGemma](https://docs.sglang.io/cookbook/autoregressive/Google/DiffusionGemma), Zyphra ZAYA1, MiMo-V2-ASR

**DeepSeek-V4 on GB300 since Day 0**: 5x higher throughput at the same interactivity, serving DeepSeek-V4 on NVIDIA GB300 with SGLang ([blog](https://pytorch.org/blog/serving-deepseek-v4-on-gb300-with-sglang-5x-higher-throughput-at-the-same-interactivity-since-day-0/)).

**Waterfill & LPLB MoE load balancing**: Two dispatch-time load-balancing methods for DeepEP expert parallelism: Waterfill for shared-expert dispatch and LPLB for redundant expert replicas, improving throughput for DeepSeek-V3/R1 and DeepSeek-V4 ([blog](https://www.lmsys.org/blog/2026-06-26-waterfill-lplb)).

**KDA CuteDSL prefill kernel on Blackwell (SM100)**: New CuteDSL prefill kernel for Kimi-Linear (KDA), 1.08-1.52x faster than the Triton path via a reusable scratch workspace, plus a cuda-graph padding fix ([#27488](https://github.com/sgl-project/sglang/pull/27488)); see the [Kimi-Linear cookbook](https://docs.sglang.io/cookbook/autoregressive/Moonshotai/Kimi-Linear).

**Linear-attention prefix-cache memory savings**: An int8 checkpoint pool stores recurrent states compactly in the Mamba radix cache, substantially increasing prefix-cache capacity for KDA / GDN models ([#28185](https://github.com/sgl-project/sglang/pull/28185)); the speculative conv-window intermediate cache is deduplicated with a sliding-window layout, halving its footprint with no numerical change ([#28302](https://github.com/sgl-project/sglang/pull/28302)).

**LPLB: linear-programming load balancer for MoE expert parallelism**: Balances token routing across redundant expert replicas by solving a per-layer LP; opt-in via `--ep-dispatch-algorithm=lp`

, default behavior unchanged ([#24515](https://github.com/sgl-project/sglang/pull/24515)).

**MSCCL++ integration & MNNVL allreduce fusion**: MSCCL++ migrates to the upstream `mscclpp`

Python package (Executor + DSL compiler) with auto-tuned collectives for TP=8 single-node and TP=16 two-node ([#22734](https://github.com/sgl-project/sglang/pull/22734)); FlashInfer fused allreduce + residual + RMSNorm re-enables an MNNVL backend behind `--flashinfer-allreduce-fusion-backend`

(`auto`

/ `trtllm`

/ `mnnvl`

), fixing the piecewise-CUDA-graph interaction ([#23402](https://github.com/sgl-project/sglang/pull/23402)).

**Nemotron DP attention + MTP**: Data-parallel attention for the hybrid Nemotron-H (Mamba2 + full attention + MoE), plus MTP support ([#24955](https://github.com/sgl-project/sglang/pull/24955)); see the [Nemotron 3 Ultra cookbook](https://docs.sglang.io/cookbook/autoregressive/NVIDIA/Nemotron3-Ultra).

**AMD: breakable CUDA graph on ROCm/HIP**: The breakable CUDA graph execution path now runs on AMD GPUs ([#28173](https://github.com/sgl-project/sglang/pull/28173)).

**NVFP4 MoE for DeepSeek-V4**: Adds an NVFP4 MoE quantization path for DeepSeek-V4 on Blackwell for higher MoE throughput; enable with `--moe-runner-backend flashinfer_trtllm_routed`

([#25820](https://github.com/sgl-project/sglang/pull/25820)); see the [DeepSeek-V4 cookbook](https://docs.sglang.io/cookbook/autoregressive/DeepSeek/DeepSeek-V4).

**DeepSeek-V4 decode & quantization optimizations**: FP8 group quantization now emits power-of-two (UE8M0) scales directly from the per-token group-quant kernel, dropping a separate rounding pass ([#26766](https://github.com/sgl-project/sglang/pull/26766)); MLA decode q-heads are padded to 64 under attention-TP so FlashMLA dispatches the ~2x cheaper head64 kernel instead of head128 ([#27954](https://github.com/sgl-project/sglang/pull/27954)); the MHC prenorm kernel is prewarmed at startup to remove the first-run JIT slowdown on a fresh server ([#27986](https://github.com/sgl-project/sglang/pull/27986)); and BF16 mixed-dtype compression states are supported on the C4 / C128 paths ([#27277](https://github.com/sgl-project/sglang/pull/27277)); see the [DeepSeek-V4 cookbook](https://docs.sglang.io/cookbook/autoregressive/DeepSeek/DeepSeek-V4).

Full release notes by category below.

## New Model Support

- GLM-5.2:
[#28437](https://github.com/sgl-project/sglang/pull/28437)([cookbook](https://docs.sglang.io/cookbook/autoregressive/GLM/GLM-5.2)) - LiquidAI LFM2.5:
[#27409](https://github.com/sgl-project/sglang/pull/27409)([cookbook](https://docs.sglang.io/cookbook/autoregressive/LiquidAI/LFM2.5)) - Kimi-K2.7-Code:
[#28064](https://github.com/sgl-project/sglang/pull/28064)([cookbook](https://docs.sglang.io/cookbook/autoregressive/Moonshotai/Kimi-K2.7-Code)) - Poolside Laguna-M.1:
[#28661](https://github.com/sgl-project/sglang/pull/28661),[#28400](https://github.com/sgl-project/sglang/pull/28400)([cookbook](https://docs.sglang.io/cookbook/autoregressive/Poolside/Laguna-M.1)) - DiffusionGemma:
[#27824](https://github.com/sgl-project/sglang/pull/27824)([cookbook](https://docs.sglang.io/cookbook/autoregressive/Google/DiffusionGemma)) - Zyphra ZAYA1:
[#26347](https://github.com/sgl-project/sglang/pull/26347)(cookbook wip) - MiMo-V2-ASR:
[#26278](https://github.com/sgl-project/sglang/pull/26278)(cookbook wip)

## DeepSeek V4

- [NVIDIA] Support NVFP4 MoE for DeepSeek-V4:
[#25820](https://github.com/sgl-project/sglang/pull/25820) - [DeepSeek-V4] Fuse UE8M0 scale rounding into FP8 group quantization:
[#26766](https://github.com/sgl-project/sglang/pull/26766) - [NPU] Add Ascend NPU support for DeepSeek-V4:
[#25144](https://github.com/sgl-project/sglang/pull/25144) - Deepseek v4: support mixed dtype compression states:
[#27277](https://github.com/sgl-project/sglang/pull/27277) - [AMD] Feat: Add prefill context parallel support for deepseek v4 unified kv attention:
[#27928](https://github.com/sgl-project/sglang/pull/27928) - DeepSeek-V4 Online Compress support MTP:
[#26471](https://github.com/sgl-project/sglang/pull/26471) - [dsv4] Pad MLA decode q-heads to 64 (not full n_heads) for FlashMLA head64 kernel:
[#27954](https://github.com/sgl-project/sglang/pull/27954) - [dsv4] Prewarm MHC prenorm kernel at startup:
[#27986](https://github.com/sgl-project/sglang/pull/27986) - [LoRA] Support DSA indexer LoRA targets for GLM-5.1 / DeepSeek-V3.2-family models:
[#28110](https://github.com/sgl-project/sglang/pull/28110) - Add DeepSeek V4 MTP acceptance length checks:
[#28098](https://github.com/sgl-project/sglang/pull/28098)

## Speculative Decoding

- [Spec] Add sync-free
`fast_prefill_plan`

for EAGLE draft-extend CUDA graph:[#28854](https://github.com/sgl-project/sglang/pull/28854) - [Spec] Support FlashInfer CUDA graph for EAGLE draft-extend:
[#28782](https://github.com/sgl-project/sglang/pull/28782) - [mtp] add rejection sampling for speculative decoding:
[#26312](https://github.com/sgl-project/sglang/pull/26312) - [NPU] Add MTP support for GLM-4.7-Flash:
[#28516](https://github.com/sgl-project/sglang/pull/28516) - Dflash add sliding window attention draft layer support:
[#27469](https://github.com/sgl-project/sglang/pull/27469) - Support Nemotron DP attention and MTP:
[#24955](https://github.com/sgl-project/sglang/pull/24955) - [Feature] [Ngram spec] Support ngram spec v2:
[#17260](https://github.com/sgl-project/sglang/pull/17260)

## Piecewise & Breakable CUDA Graph

- [AMD] Make breakable CUDA graph run on ROCm/HIP:
[#28173](https://github.com/sgl-project/sglang/pull/28173) - Dflash piecewise cuda graphs support:
[#27468](https://github.com/sgl-project/sglang/pull/27468)

## Attention Backends

- [Cookbook] Nemotron3-Ultra: Add mamba-backend and SSM dtype flags:
[#28675](https://github.com/sgl-project/sglang/pull/28675) - [Mamba][GDN] Deduplicate spec conv-window intermediate cache via sliding window layout:
[#28302](https://github.com/sgl-project/sglang/pull/28302) - [GDN][KDA][mem_cache] int8 checkpoint pool for the linear-attn prefix cache:
[#28185](https://github.com/sgl-project/sglang/pull/28185) - [diffusion] feat: use LocalAttention for mistral3 encoder:
[#28176](https://github.com/sgl-project/sglang/pull/28176) - [NPU] Add Gemma4 Sliding Window Attention support on Ascend backend:
[#26147](https://github.com/sgl-project/sglang/pull/26147) - [AMD] Fuse sigmoid + mul attention output gate into single Triton kernel:
[#27630](https://github.com/sgl-project/sglang/pull/27630) - [AMD] Enable fused GDN QKV split Triton kernel on HIP:
[#27583](https://github.com/sgl-project/sglang/pull/27583) - [KDA] Add CuteDSL Prefill Kernel on SM100:
[#27488](https://github.com/sgl-project/sglang/pull/27488) - [AMD] Add unified kv attention support in dpsk-v4:
[#27380](https://github.com/sgl-project/sglang/pull/27380)

## MoE & Expert Parallelism

- Add GB10 FP8 fused MoE Triton config:
[#25665](https://github.com/sgl-project/sglang/pull/25665) - Support asymmetric compressed-tensors MoE:
[#27690](https://github.com/sgl-project/sglang/pull/27690) - LPLB: linear-programming load balancer for MoE expert parallelism:
[#24515](https://github.com/sgl-project/sglang/pull/24515) - [AMD] Fuse sigmoid + mul into single Triton kernel for shared expert gating:
[#27636](https://github.com/sgl-project/sglang/pull/27636) - [quantization] NVFP4 MoE: split fused w13 gate/up global scales:
[#27588](https://github.com/sgl-project/sglang/pull/27588) - [Apple Silicon] [MLX] Fuse SwiGLU activation into gate gather_qmv for SwitchGLU MoE blocks:
[#26188](https://github.com/sgl-project/sglang/pull/26188) - [DeepSeek V3] Defer moe finalize and fused it with main stream add:
[#27720](https://github.com/sgl-project/sglang/pull/27720)

## Quantization

- ✨ [llm][npu][quant] Add W8A8 MXFP8 quantization support for...

[Read more](https://github.com/sgl-project/sglang/releases/tag/v0.5.14)

## v0.5.13

## Highlights

**New Model Support**:

**Autoregressive**:[Nemotron 3 Ultra](https://docs.sglang.io/cookbook/autoregressive/NVIDIA/Nemotron3-Ultra)(Day-0,[blog](https://www.lmsys.org/blog/2026-06-04-nvidia-run-nemotron-3-ultra/)),[Step-3.7-Flash](https://docs.sglang.io/cookbook/autoregressive/StepFun/Step-3.7-Flash), Command A+**Diffusion**:[Cosmos3](https://docs.sglang.io/cookbook/diffusion/Cosmos/Cosmos3),[LingBot-World](https://docs.sglang.io/cookbook/diffusion/LingBot-World/LingBot-World),[SANA-WM](https://docs.sglang.io/cookbook/diffusion/SANA-WM/SANA-WM),[Ernie-Image](https://docs.sglang.io/cookbook/diffusion/Ernie-Image/Ernie-Image),[FLUX.2-Klein 4B/9B](https://docs.sglang.io/cookbook/diffusion/FLUX/FLUX),[Ideogram 4](https://docs.sglang.io/cookbook/diffusion/Ideogram/Ideogram4)

**Spec V2 is now the default speculative-decoding path**: Tree drafting with topk > 1 is production-ready across the triton / FA3 / MLA / aiter backends, including `page_size > 1`

and Mamba/hybrid-linear models ([#26997](https://github.com/sgl-project/sglang/pull/26997), [#26972](https://github.com/sgl-project/sglang/pull/26972), [#27463](https://github.com/sgl-project/sglang/pull/27463)). Spec V1 is deprecated, with EAGLE/MTP now running on the unified V2 worker ([#25464](https://github.com/sgl-project/sglang/pull/25464)), and topk = 1 drafting is faster ([#26397](https://github.com/sgl-project/sglang/pull/26397), [#26424](https://github.com/sgl-project/sglang/pull/26424)).

**Lower per-step scheduler overhead**: Unified async value passing through FutureMap plus moving prefill input transfer onto the forward stream reduced per-step launch overhead and improved stability under high concurrency ([#25945](https://github.com/sgl-project/sglang/pull/25945), [#25879](https://github.com/sgl-project/sglang/pull/25879), [#26380](https://github.com/sgl-project/sglang/pull/26380)).

**Piecewise & Breakable CUDA Graph coverage**: Piecewise (PCG) and Breakable (BCG) CUDA Graph capture more of the model to cut per-step kernel-launch overhead, now extended to DSA models, Kimi-K2.5, and DeepSeek V4: [#23351](https://github.com/sgl-project/sglang/pull/23351), [#26382](https://github.com/sgl-project/sglang/pull/26382), [#25195](https://github.com/sgl-project/sglang/pull/25195).

**Faster Qwen 3.5 on Blackwell**: New FlashInfer Gated DeltaNet (GDN) kernels and a CuTeDSL GDN prefill kernel speed up Qwen 3.5 on Blackwell GPUs: [#22921](https://github.com/sgl-project/sglang/pull/22921), [#23273](https://github.com/sgl-project/sglang/pull/23273), [#26200](https://github.com/sgl-project/sglang/pull/26200).

**HiCache for hybrid models by default**: HybridModel (SWA/Mamba) launches HiCache through UnifiedTree by default, bringing hierarchical KV-cache offload to sliding-window and Mamba hybrids out of the box: [#27759](https://github.com/sgl-project/sglang/pull/27759).

**Heterogeneous CPU + GPU EPD disaggregation (with Intel)**: Offload VLM vision encoding onto Intel Xeon CPUs alongside GPUs, with up to ~1.3x P99 TTFT and request-throughput gains under load. ([blog](https://www.lmsys.org/blog/2026-06-01-hetero-epd/))

**MoRI on AMD Instinct MI355X (with AMD)**: Cost-competitive DeepSeek-R1 disaggregated inference via AMD's MoRI communication library, $0.169 per million tokens at 129 tok/s/user. ([blog](https://www.lmsys.org/blog/2026-05-28-mori/))

**DeepSeek V4 — context parallelism & sparse-attention kernels**: Building on the v0.5.12 Day-0 path, v0.5.13 extends DeepSeek-V4 to context-parallel serving and adds its sparse-attention kernels:

- Context Parallel + MTP:
[#24934](https://github.com/sgl-project/sglang/pull/24934) - Context Parallel + fused MoE kernel (non-DeepEP):
[#24947](https://github.com/sgl-project/sglang/pull/24947) - Sparse FlashMLA via
`flash_mla_sparse_fwd`

:[#25418](https://github.com/sgl-project/sglang/pull/25418) - FP4 indexer support:
[#26209](https://github.com/sgl-project/sglang/pull/26209) - SM120 support:
[#24692](https://github.com/sgl-project/sglang/pull/24692) - DeepEP waterfill load balancing:
[#25391](https://github.com/sgl-project/sglang/pull/25391) - MHC kernel warmup:
[#25810](https://github.com/sgl-project/sglang/pull/25810) - Breakable CUDA Graph for DeepSeek V4:
[#25195](https://github.com/sgl-project/sglang/pull/25195) - Backed by sgl-kernel 0.4.3 exposing
`sgl_kernel.flashmla`

:[#26421](https://github.com/sgl-project/sglang/pull/26421),[#26132](https://github.com/sgl-project/sglang/pull/26132)

See the [DeepSeek-V4 cookbook](https://docs.sglang.io/cookbook/autoregressive/DeepSeek/DeepSeek-V4) for tuned deployment commands.

**SGLang-Diffusion — realtime & progressive resolution**: OpenAI-style realtime video generation with msgpack frame streaming and a standalone browser WebUI ([#26954](https://github.com/sgl-project/sglang/pull/26954), [#26959](https://github.com/sgl-project/sglang/pull/26959)), continuous camera controls + super-resolution controls ([#27026](https://github.com/sgl-project/sglang/pull/27026), [#27297](https://github.com/sgl-project/sglang/pull/27297)), and progressive-resolution growing across FLUX / FLUX.2 / Qwen-Image / Wan / Z-Image ([#27524](https://github.com/sgl-project/sglang/pull/27524)).

*Full release notes by category below.*

## New Model Support

- Nemotron 3 Ultra (Day-0, kernel optimizations):
[#26733](https://github.com/sgl-project/sglang/pull/26733)(see[cookbook](https://docs.sglang.io/cookbook/autoregressive/NVIDIA/Nemotron3-Ultra)) - Step-3.7-Flash:
[#26565](https://github.com/sgl-project/sglang/pull/26565)(see[cookbook](https://docs.sglang.io/cookbook/autoregressive/StepFun/Step-3.7-Flash)) - Cosmos3-Nano / Cosmos3-Super — T2V / I2V / T2I (Diffusion):
[#24994](https://github.com/sgl-project/sglang/pull/24994),[#26492](https://github.com/sgl-project/sglang/pull/26492),[#26926](https://github.com/sgl-project/sglang/pull/26926),[#26950](https://github.com/sgl-project/sglang/pull/26950)(see[cookbook](https://docs.sglang.io/cookbook/diffusion/Cosmos/Cosmos3)) - Ernie-Image (Diffusion):
[#22439](https://github.com/sgl-project/sglang/pull/22439),[#27195](https://github.com/sgl-project/sglang/pull/27195)(see[cookbook](https://docs.sglang.io/cookbook/diffusion/Ernie-Image/Ernie-Image)) - LingBot-World — realtime / causal-DMD generation (Diffusion):
[#26954](https://github.com/sgl-project/sglang/pull/26954)(see[cookbook](https://docs.sglang.io/cookbook/diffusion/LingBot-World/LingBot-World)) - SANA-WM — streaming + realtime (Diffusion):
[#27531](https://github.com/sgl-project/sglang/pull/27531)(see[cookbook](https://docs.sglang.io/cookbook/diffusion/SANA-WM/SANA-WM)) - FLUX.2-Klein 4B / 9B (Diffusion):
[#25661](https://github.com/sgl-project/sglang/pull/25661)(see[cookbook](https://docs.sglang.io/cookbook/diffusion/FLUX/FLUX)) - Ideogram 4 — FP8 / NVFP4 with tensor parallelism (Diffusion):
[#27279](https://github.com/sgl-project/sglang/pull/27279),[#27379](https://github.com/sgl-project/sglang/pull/27379),[#27393](https://github.com/sgl-project/sglang/pull/27393)(see[cookbook](https://docs.sglang.io/cookbook/diffusion/Ideogram/Ideogram4)) - Command A+ (Cohere 2 family):
[#26106](https://github.com/sgl-project/sglang/pull/26106),[#27401](https://github.com/sgl-project/sglang/pull/27401)(cookbook page pending)

## DeepSeek V4

- Context Parallel + MTP:
[#24934](https://github.com/sgl-project/sglang/pull/24934) - Context Parallel + fused MoE kernel (non-DeepEP):
[#24947](https://github.com/sgl-project/sglang/pull/24947) - MHC kernel warmup:
[#25810](https://github.com/sgl-project/sglang/pull/25810) - SM120 support:
[#24692](https://github.com/sgl-project/sglang/pull/24692) - FP4 indexer support:
[#26209](https://github.com/sgl-project/sglang/pull/26209) - Integrate
`flash_mla_sparse_fwd`

kernel:[#25418](https://github.com/sgl-project/sglang/pull/25418) - DeepEP waterfill support:
[#25391](https://github.com/sgl-project/sglang/pull/25391) - Breakable CUDA Graph for DeepSeek V4:
[#25195](https://github.com/sgl-project/sglang/pull/25195)

## Speculative Decoding

- Spec V2 is now the default speculative-decoding path
- Tree speculative drafting (topk > 1) on Spec V2 —
`page_size > 1`

and Mamba/hybrid-linear, validated across triton / FA3 / MLA / aiter:[#26997](https://github.com/sgl-project/sglang/pull/26997),[#26972](https://github.com/sgl-project/sglang/pull/26972),[#27463](https://github.com/sgl-project/sglang/pull/27463) - Spec V1 deprecated; EAGLE/MTP run on the unified V2 worker:
[#25464](https://github.com/sgl-project/sglang/pull/25464) - Spec V2 extended to the FlashMLA backend:
[#24640](https://github.com/sgl-project/sglang/pull/24640) - Adaptive speculative decoding: batch-size-aware
`num_steps`

+ observability metrics:[#24055](https://github.com/sgl-project/sglang/pull/24055),[#25940](https://github.com/sgl-project/sglang/pull/25940) - Faster topk = 1 drafting (skip full-vocab softmax + redundant cat/topk/sort/gather ops):
[#26397](https://github.com/sgl-project/sglang/pull/26397),[#26424](https://github.com/sgl-project/sglang/pull/26424) - Draft-extend CUDA Graph for the trtllm
`mha`

attention backend:[#25002](https://github.com/sgl-project/sglang/pull/25002)

## Piecewise & Breakable CUDA Graph

- PCG support for DSA models:
[#23351](https://github.com/sgl-project/sglang/pull/23351) - PCG support for Kimi-K2.5:
[#26382](https://github.com/sgl-project/sglang/pull/26382) - BCG support for DeepSeek V4:
[#25195](https://github.com/sgl-project/sglang/pull/25195)

## Context Parallelism

## Attention Backends

- CuTeDSL MLA attention kernels from FlashInfer:
[#24737](https://github.com/sgl-project/sglang/pull/24737) - Qwen 3.5: Flash...

[Read more](https://github.com/sgl-project/sglang/releases/tag/v0.5.13)

## v0.5.12.post1

v0.5.12.post1 is a stability patch on top of v0.5.12. It cherry-picks 12 fixes — primarily for DeepSeek V4 — onto the release branch.

# Bug Fixes

## DeepSeek V4

- DSV4-Pro emits garbled text during single-token decode on B200/B300 (fix
`deep_gemm`

UE8M0 scale-packing path by ceiling activation scales before packing):[#25733](https://github.com/sgl-project/sglang/pull/25733) - DSV4 + EAGLE/MTP in disaggregation decode crashes around 2000 requests with a SWA allocator assertion (recycled KV pages kept stale sliding-window mappings):
[#25805](https://github.com/sgl-project/sglang/pull/25805) - DSV4 NSA prefill context-parallel (
`--enable-nsa-prefill-context-parallel --nsa-prefill-cp-mode round-robin-split`

) in`--disaggregation-mode prefill`

: scheduler crash at startup:[#25396](https://github.com/sgl-project/sglang/pull/25396) - DSV4 HiSparse +
`SGLANG_OPT_USE_COMPRESSOR_V2=1`

: GSM8K accuracy restored from 0.825 → 0.960:[#25646](https://github.com/sgl-project/sglang/pull/25646) - DSV4 PD disaggregation now works with pipeline parallelism > 1 (removed stale
`pp_size=1`

assertion):[#25771](https://github.com/sgl-project/sglang/pull/25771) - DSV4-Flash with
`--load-format dummy`

+ FlashInfer mxfp4 hits CUDA illegal memory access during CUDA-graph capture (the integer`HashTopK.tid2eid`

lookup table was left uninitialized by dummy load):[#25892](https://github.com/sgl-project/sglang/pull/25892) - DSV4 HiCache +
`SGLANG_OPT_CACHE_SWA_TRANSLATION=1`

returns stale translation indices after a cache rebuild, causing OOB writes / wrong outputs:[#25889](https://github.com/sgl-project/sglang/pull/25889)

## Disaggregation

- [PD][NIXL] Always send aux on
`is_last`

; only expect state when truthy:[#25699](https://github.com/sgl-project/sglang/pull/25699)

## Other

- Fix missing
`group`

arg in`get_dp_buffer`

:[#25585](https://github.com/sgl-project/sglang/pull/25585)

# Performance

- DSV4: warm MHC token-count buckets at startup (gated to
`SGLANG_OPT_DEEPGEMM_HC_PRENORM=1`

+`SGLANG_OPT_USE_TILELANG_MHC_PRE=1`

+ hybrid SWA) to eliminate 20–40s cold-bucket forward stalls:[#25810](https://github.com/sgl-project/sglang/pull/25810) - DSV4-Pro: precompile a DeepGEMM branch for
`_dispatch_bf16_fp32_backend`

to cut runtime JIT compile cost:[#25860](https://github.com/sgl-project/sglang/pull/25860)

# Dependencies

- Use
`[cu13]`

extra for`nvidia-cutlass-dsl`

(default to CUDA 13; required for sm_103 / B300):[#25576](https://github.com/sgl-project/sglang/pull/25576)

**All PRs included in this release**: `v0.5.12...v0.5.12.post1`

**Full Changelog**: `v0.5.12...v0.5.12.post1`