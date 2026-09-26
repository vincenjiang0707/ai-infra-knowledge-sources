source: https://github.com/ROCm/aiter/releases

# Releases: ROCm/aiter

## Release list

## AITER v0.1.22.post1

AITER v0.1.22.post1 - post release

Post release on top of the release/v0.1.22 release line.

Diff base: v0.1.22

## Wheels

Prebuilt manylinux_2_28 wheels, `GPU_ARCHS=gfx942;gfx950`

:

- ROCm 7.0 / 7.1 / 7.2 x cp310 / cp312 (6 wheels)

Wheel assets are uploaded after the release page is created.

## What's Changed

- [Release v0.1.22] Cherry-pick MXFP4 MoE OOB fix, MoE sorting and routing fixes, fp8 MQA logits split-k and DSv4 tunings (
[#5573](https://github.com/ROCm/aiter/pull/5573),[#5295](https://github.com/ROCm/aiter/pull/5295),[#5558](https://github.com/ROCm/aiter/pull/5558),[#5603](https://github.com/ROCm/aiter/pull/5603),[#5627](https://github.com/ROCm/aiter/pull/5627),[#5485](https://github.com/ROCm/aiter/pull/5485)) by[@vgokhale](https://github.com/vgokhale)in[#5638](https://github.com/ROCm/aiter/pull/5638)

**Full Changelog**: `v0.1.22...v0.1.22.post1`

## AITER v0.1.22

AITER v0.1.22 - bi-weekly release

Scheduled release from `release/v0.1.22`

.

Diff base: `v0.1.21`


## Wheels

Prebuilt manylinux_2_28 wheels, `GPU_ARCHS=gfx942;gfx950`

:

## What's Changed

## Changes

- [Triton/Gluon] Add config-aware repr to the rope and normalization kernels by
[@Boss2002n](https://github.com/Boss2002n)in[#5099](https://github.com/ROCm/aiter/pull/5099) - [Triton/Gluon] Add config-aware repr to the quant kernels by
[@Boss2002n](https://github.com/Boss2002n)in[#5100](https://github.com/ROCm/aiter/pull/5100) - [CI] CI: use app token for release refs by
[@gyohuangxin](https://github.com/gyohuangxin)in[#5198](https://github.com/ROCm/aiter/pull/5198) - [CI] CI: respect docker login input in release builds by
[@gyohuangxin](https://github.com/gyohuangxin)in[#5201](https://github.com/ROCm/aiter/pull/5201) - [Triton/Gluon] [HIP] [CK] Remove obsolete availability helpers by
[@coderfeli](https://github.com/coderfeli)in[#5116](https://github.com/ROCm/aiter/pull/5116) - [FlyDSL] Add FlyDSL Radix-Select TopK Path to the Existing Per-Row Decode Interface by
[@lirui927](https://github.com/lirui927)in[#5011](https://github.com/ROCm/aiter/pull/5011) - [CI] CI: set release publish repository context by
[@gyohuangxin](https://github.com/gyohuangxin)in[#5204](https://github.com/ROCm/aiter/pull/5204) - [HIP] Add fused SiTUv2 activation + per-token FP8 quant kernel by
[@XiaobingSuper](https://github.com/XiaobingSuper)in[#5081](https://github.com/ROCm/aiter/pull/5081) - [Docs] docs: update README by
[@shengnxu](https://github.com/shengnxu)in[#5073](https://github.com/ROCm/aiter/pull/5073) - [CK] [FlyDSL] Retune Kimi-K3 a16w4 MoE tile geometry by
[@amd-wsung102](https://github.com/amd-wsung102)in[#5118](https://github.com/ROCm/aiter/pull/5118) - [Config] tune a8w8 gemm with 64-step m for k3 by
[@gbyu-amd](https://github.com/gbyu-amd)in[#5197](https://github.com/ROCm/aiter/pull/5197) - [CI] CI: add extended test workflow by
[@gyohuangxin](https://github.com/gyohuangxin)in[#4458](https://github.com/ROCm/aiter/pull/4458) - [CI] Run extended test dispatch on internal runner by
[@gyohuangxin](https://github.com/gyohuangxin)in[#5205](https://github.com/ROCm/aiter/pull/5205) - Fix stale TopK availability checks by
[@vorapolsiloai](https://github.com/vorapolsiloai)in[#5210](https://github.com/ROCm/aiter/pull/5210) - [CI] Extended tests client_payload change by
[@leo-automation](https://github.com/leo-automation)in[#5209](https://github.com/ROCm/aiter/pull/5209) - [Triton/Gluon] Move the sage-attention launch params into the config tree by
[@Boss2002n](https://github.com/Boss2002n)in[#5106](https://github.com/ROCm/aiter/pull/5106) - [Triton/Gluon] moe_gemm_a4w4 num_warps 8 -> 4 for block_m != 16 tile by
[@nidal567](https://github.com/nidal567)in[#5189](https://github.com/ROCm/aiter/pull/5189) - [Docs] Update docs for the single nested config layout by
[@Boss2002n](https://github.com/Boss2002n)in[#5085](https://github.com/ROCm/aiter/pull/5085) - [skills] Add kernel PR validation and structural D9 scanning (supersedes
[#4870](https://github.com/ROCm/aiter/pull/4870)) by[@zhiding512](https://github.com/zhiding512)in[#5142](https://github.com/ROCm/aiter/pull/5142) - [AMD][DSV4] Fix(fmoe): fuse stage-1 fp8 quant on the heuristic FlyDSL fallback by
[@karverma-amd](https://github.com/karverma-amd)in[#4994](https://github.com/ROCm/aiter/pull/4994) - [Bugfix] Make
`_fold_seqlen_indptr`

cudagraph-safe (avoid scalar H2D copy) by[@micah-wil](https://github.com/micah-wil)in[#5202](https://github.com/ROCm/aiter/pull/5202) - [FlyDSL] Relax GDR decode test mismatch tolerance by
[@xytpai](https://github.com/xytpai)in[#5215](https://github.com/ROCm/aiter/pull/5215) - [HIP] Extend fused QK norm for MiniMax-M3 by
[@weitliao](https://github.com/weitliao)in[#5143](https://github.com/ROCm/aiter/pull/5143) - Revert "[AMD][DSV4] Fix(fmoe): fuse stage-1 fp8 quant on the heuristic FlyDSL fallback" by
[@valarLip](https://github.com/valarLip)in[#5227](https://github.com/ROCm/aiter/pull/5227) - [Triton/Gluon] [CI] Add fused KDA decode kernel (conv1d + recurrence + gated RMSNorm) by
[@mengfei-jiang](https://github.com/mengfei-jiang)in[#4712](https://github.com/ROCm/aiter/pull/4712) - [HIP] fix(mla/metadata): scale the auto KV-split count with the machine width by
[@whx-sjtu](https://github.com/whx-sjtu)in[#5212](https://github.com/ROCm/aiter/pull/5212) - [Triton/Gluon] Add
`repr`

to DiT fused kernels + Cover`round_intermediate`

in tests by[@brunomazzottiamd](https://github.com/brunomazzottiamd)in[#5154](https://github.com/ROCm/aiter/pull/5154) - [HIP] [FlyDSL] Refactor gfx950 A16W16 GEMM with centralized policy selection and tuning by
[@xytpai](https://github.com/xytpai)in[#5145](https://github.com/ROCm/aiter/pull/5145) - [Triton/Gluon] [GFX9] [GFX12] EP MOE changes by
[@k50112113](https://github.com/k50112113)in[#4500](https://github.com/ROCm/aiter/pull/4500) - [FlyDSL] [CI] FlyDSL FMHA forward-prefill A16W16 kernel for gfx1250 (
`fmha_fwd_prefill_m32x8`

) by[@ruanjm](https://github.com/ruanjm)in[#5168](https://github.com/ROCm/aiter/pull/5168) - [HIP] [Bugfix] Guard against negative expert ids in MoE sorting P0 by
[@xudonlyu](https://github.com/xudonlyu)in[#4839](https://github.com/ROCm/aiter/pull/4839) - [FlyDSL] perf(mqa-logits): build the FP4 prefill schedule in one kernel, not 25 torch ops by
[@valarLip](https://github.com/valarLip)in[#5276](https://github.com/ROCm/aiter/pull/5276) - [Config] configs: GLM-5.2 a8w8-bpreshuffle rows for the shapes a live engine dispatches by
[@ThomasNing](https://github.com/ThomasNing)in[#5281](https://github.com/ROCm/aiter/pull/5281) - [FlyDSL] Rewrite gfx950 HGEMM test to op_test standard by
[@xytpai](https://github.com/xytpai)in[#5287](https://github.com/ROCm/aiter/pull/5287) - [Config] tune(dsv4): gfx950 FP8 blockscale bpreshuffle for wq_b / wqkv_a by
[@lixiufei-leo](https://github.com/lixiufei-leo)in[#5283](https://github.com/ROCm/aiter/pull/5283) - [FlyDSL] [DSv4] Bound the FP4 MQA-logits store with a window-sized V# instead of a compare by
[@valarLip](https://github.com/valarLip)in[#5285](https://github.com/ROCm/aiter/pull/5285) - [Config] [AMD][DSV4] [tune][gfx950] wo_b/wq_b a8w8 blockscale bpreshuffle configs by
[@karverma-amd](https://github.com/karverma-amd)in[#5279](https://github.com/ROCm/aiter/pull/5279) - [Triton/Gluon] Add FP8 block-wise quantization kernels by
[@WuLei-AMD](https://github.com/WuLei-AMD)in[#5177](https://github.com/ROCm/aiter/pull/5177) - [Triton/Gluon] Add vocab-parallel cross-entropy kernel by
[@WuLei-AMD](https://github.com/WuLei-AMD)in[#5165](https://github.com/ROCm/aiter/pull/5165) - [FlyDSL] Remove the unused gfx1250 d192 FMHA sibling kernel by
[@coderfeli](https://github.com/coderfeli)in[#5306](https://github.com/ROCm/aiter/pull/5306) - [HIP] [CK] [MoE] Reject non-int32 index buffers in the topk kernels by
[@i-kosarev](https://github.com/i-kosarev)in[#5255](https://github.com/ROCm/aiter/pull/5255) - [FlyDSL] Migrate mixed MoE 2-stage LDS to fly shared storage by
[@xudoyuan](https://github.com/xudoyuan)in[#5317](https://github.com/ROCm/aiter/pull/5317) - review-pr: gates that can be checked, and 200 PRs of evidence about them by
[@zufayu](https://github.com/zufayu)in[#5289](https://github.com/ROCm/aiter/pull/5289) - [CI] fix auditwheel excludes: versioned ROCm SONAMEs were grafting ~890MB into the wheel by
[@amd-ruitang3](https://github.com/amd-ruitang3)in[#5318](https://github.com/ROCm/aiter/pull/5318) - [Triton/Gluon] Add MXFP8 convert and fast-transpose kernels by
[@WuLei-AMD](https://github.com/WuLei-AMD)in[#5203](https://github.com/ROCm/aiter/pull/5203) - [HIP] [JIT] [Build] Stop stamping torch-free modules with torch's pybind11 ABI identity by
[@amd-ruitang3](https://github.com/amd-ruitang3)in[#5312](https://github.com/ROCm/aiter/pull/5312) - fix(mega_moe): stop the reference clamping SwiGLU at swiglu_limit=0 by
[@JohnQinAMD](https://github.com/JohnQinAMD)in[#5271](https://github.com/ROCm/aiter/pull/5271) - [Triton/Gluon] chunk_kimi_delta_attn: accept a non-fp32 KDA state by
[@XiaobingSuper](https://github.com/XiaobingSuper)in[#5249](https://github.com/ROCm/aiter/pull/5249) - [Triton/Gluon] Fix ragged-K mask in batched A16WFP4 GEMM by
[@mjkvaak-amd](https://github.com/mjkvaak-amd)in[#4181](https://github.com/ROCm/aiter/pull/4181) - [Triton/Gluon] [FlyDSL] feat(flydsl): Add HSTU Forward kernel by
[@damien-lejeune](https://github.com/damien-lejeune)in[#4441](https://github.com/ROCm/aiter/pull/4441) - [FlyDSL] [JIT] refactor: move tuning config file for all2all by
[@JiaoliangYu](https://github.com/JiaoliangYu)in[#5129](https://github.com/ROCm/aiter/pull/5129) - [Triton/Gluon] [GFX950] Add MHA Gluon Kernel by
[@lucas-santos-amd](https://github.com/lucas-santos-amd)in[#4147](https://github.com/ROCm/aiter/pull/4147) - [FlyDSL] Tune the GLM-5.2 decode shapes for gfx950 by
[@kyle-256](https://github.com/kyle-256)in[#5328](https://github.com/ROCm/aiter/pull/5328) - [FlyDSL] fix(flydsl): zero GDR decode graph padding output by
[@junna2016](https://github.com/junna2016)in[#5324](https://github.com/ROCm/aiter/pull/5324) - [Triton/Gluon] [Conv2D] Add Conv2D configuration files for gfx1101 (RDNA3) and gfx1150 (RDNA3.5) by
[@Ragua1](https://github.com/Ragua1)in[#5246](https://github.com/ROCm/aiter/pull/5246) - [FlyDSL] feat(mega_moe): optimize fused stage1 and AOT bundles by
[@GwilliamHu](https://github.com/GwilliamHu)in[#5001](https://github.com/ROCm/aiter/pull/5001) - [FlyDSL] Revert " feat(mega_moe): optimize fused stage1 and AOT bundle… by
[@coderfeli](https://github.com/coderfeli)in[#5345](https://github.com/ROCm/aiter/pull/5345) - [FlyDSL] fix(flydsl): detach tensors before DLPack conversion by
[@xytpai](https://github.com/xytpai)in[#5327](https://github.com/ROCm/aiter/pull/5327) - [FlyDSL] [CI] [JIT] comm fused moe by
[@yifehuan](https://github.com/yifehuan)in[#4985](https://github.com/ROCm/aiter/pull/4985) - [Triton/Gluon] split K correct OOB afp4wfp4 by
[@afriedri](https://github.com/afriedri)in[#5261](https://github.com/ROCm/aiter/pull/5261) - [HIP] [OPUS] fix: single-source opus's half-precision dtype spellings by
[@zufayu](https://github.com/zufayu)in[#5329](https://github.com/ROCm/aiter/pull/5329) - [FlyDSL] Megamoe restore 5001 aot fix by
[@GwilliamHu](https://github.com/GwilliamHu)in[#5346](https://github.com/ROCm/aiter/pull/5346) - [HIP] Use designated initializers for FMHA forward arguments by
[@rocking5566](https://github.com/rocking5566)in[#5359](https://github.com/ROCm/aiter/pull/5359) - [ASM] [HIP] [OPUS] Add narrow-head (H<=32) gfx1250 MLA sparse-prefill kernels for DSv4 TP by
[@kaiyang-1](https://github.com/kaiyang-1)in[#5228](https://github.com/ROCm/aiter/pull/5228) - [Triton/Gluon] [CI] [Bugfix] Fix stale MHA config-utils import by
[@vorapolsiloai](https://github.com/vorapolsiloai)in ht...

[Read more](https://github.com/ROCm/aiter/releases/tag/v0.1.22)

## AITER v0.1.21.post2

AITER v0.1.21.post2 - post release

Post release on top of the `release/v0.1.21.post2`

release line.

Diff base: `v0.1.21.post1`


## Wheels

Prebuilt manylinux_2_28 wheels, `GPU_ARCHS=gfx942;gfx950`

:

## What's Changed

## Changes

- [Triton/Gluon] Add config-aware repr to the rope and normalization kernels by
[@Boss2002n](https://github.com/Boss2002n)in[#5099](https://github.com/ROCm/aiter/pull/5099) - [Triton/Gluon] Add config-aware repr to the quant kernels by
[@Boss2002n](https://github.com/Boss2002n)in[#5100](https://github.com/ROCm/aiter/pull/5100) - [CI] CI: use app token for release refs by
[@gyohuangxin](https://github.com/gyohuangxin)in[#5198](https://github.com/ROCm/aiter/pull/5198) - [CI] CI: respect docker login input in release builds by
[@gyohuangxin](https://github.com/gyohuangxin)in[#5201](https://github.com/ROCm/aiter/pull/5201) - [Triton/Gluon] [HIP] [CK] Remove obsolete availability helpers by
[@coderfeli](https://github.com/coderfeli)in[#5116](https://github.com/ROCm/aiter/pull/5116) - [FlyDSL] Add FlyDSL Radix-Select TopK Path to the Existing Per-Row Decode Interface by
[@lirui927](https://github.com/lirui927)in[#5011](https://github.com/ROCm/aiter/pull/5011) - [CI] CI: set release publish repository context by
[@gyohuangxin](https://github.com/gyohuangxin)in[#5204](https://github.com/ROCm/aiter/pull/5204) - [HIP] Add fused SiTUv2 activation + per-token FP8 quant kernel by
[@XiaobingSuper](https://github.com/XiaobingSuper)in[#5081](https://github.com/ROCm/aiter/pull/5081) - [Docs] docs: update README by
[@shengnxu](https://github.com/shengnxu)in[#5073](https://github.com/ROCm/aiter/pull/5073) - [CK] [FlyDSL] Retune Kimi-K3 a16w4 MoE tile geometry by
[@amd-wsung102](https://github.com/amd-wsung102)in[#5118](https://github.com/ROCm/aiter/pull/5118) - [Config] tune a8w8 gemm with 64-step m for k3 by
[@gbyu-amd](https://github.com/gbyu-amd)in[#5197](https://github.com/ROCm/aiter/pull/5197) - [CI] CI: add extended test workflow by
[@gyohuangxin](https://github.com/gyohuangxin)in[#4458](https://github.com/ROCm/aiter/pull/4458) - [CI] Run extended test dispatch on internal runner by
[@gyohuangxin](https://github.com/gyohuangxin)in[#5205](https://github.com/ROCm/aiter/pull/5205) - Fix stale TopK availability checks by
[@vorapolsiloai](https://github.com/vorapolsiloai)in[#5210](https://github.com/ROCm/aiter/pull/5210) - [CI] Extended tests client_payload change by
[@leo-automation](https://github.com/leo-automation)in[#5209](https://github.com/ROCm/aiter/pull/5209) - [Triton/Gluon] Move the sage-attention launch params into the config tree by
[@Boss2002n](https://github.com/Boss2002n)in[#5106](https://github.com/ROCm/aiter/pull/5106) - [Triton/Gluon] moe_gemm_a4w4 num_warps 8 -> 4 for block_m != 16 tile by
[@nidal567](https://github.com/nidal567)in[#5189](https://github.com/ROCm/aiter/pull/5189) - [Docs] Update docs for the single nested config layout by
[@Boss2002n](https://github.com/Boss2002n)in[#5085](https://github.com/ROCm/aiter/pull/5085) - [skills] Add kernel PR validation and structural D9 scanning (supersedes
[#4870](https://github.com/ROCm/aiter/pull/4870)) by[@zhiding512](https://github.com/zhiding512)in[#5142](https://github.com/ROCm/aiter/pull/5142) - [AMD][DSV4] Fix(fmoe): fuse stage-1 fp8 quant on the heuristic FlyDSL fallback by
[@karverma-amd](https://github.com/karverma-amd)in[#4994](https://github.com/ROCm/aiter/pull/4994) - [Bugfix] Make
`_fold_seqlen_indptr`

cudagraph-safe (avoid scalar H2D copy) by[@micah-wil](https://github.com/micah-wil)in[#5202](https://github.com/ROCm/aiter/pull/5202) - [FlyDSL] Relax GDR decode test mismatch tolerance by
[@xytpai](https://github.com/xytpai)in[#5215](https://github.com/ROCm/aiter/pull/5215) - [HIP] Extend fused QK norm for MiniMax-M3 by
[@weitliao](https://github.com/weitliao)in[#5143](https://github.com/ROCm/aiter/pull/5143) - Revert "[AMD][DSV4] Fix(fmoe): fuse stage-1 fp8 quant on the heuristic FlyDSL fallback" by
[@valarLip](https://github.com/valarLip)in[#5227](https://github.com/ROCm/aiter/pull/5227) - [Triton/Gluon] [CI] Add fused KDA decode kernel (conv1d + recurrence + gated RMSNorm) by
[@mengfei-jiang](https://github.com/mengfei-jiang)in[#4712](https://github.com/ROCm/aiter/pull/4712) - [HIP] fix(mla/metadata): scale the auto KV-split count with the machine width by
[@whx-sjtu](https://github.com/whx-sjtu)in[#5212](https://github.com/ROCm/aiter/pull/5212) - [Triton/Gluon] Add
`repr`

to DiT fused kernels + Cover`round_intermediate`

in tests by[@brunomazzottiamd](https://github.com/brunomazzottiamd)in[#5154](https://github.com/ROCm/aiter/pull/5154) - [HIP] [FlyDSL] Refactor gfx950 A16W16 GEMM with centralized policy selection and tuning by
[@xytpai](https://github.com/xytpai)in[#5145](https://github.com/ROCm/aiter/pull/5145) - [Triton/Gluon] [GFX9] [GFX12] EP MOE changes by
[@k50112113](https://github.com/k50112113)in[#4500](https://github.com/ROCm/aiter/pull/4500)

## New Contributors

[@amd-wsung102](https://github.com/amd-wsung102)made their first contribution in[#5118](https://github.com/ROCm/aiter/pull/5118)[@weitliao](https://github.com/weitliao)made their first contribution in[#5143](https://github.com/ROCm/aiter/pull/5143)[@whx-sjtu](https://github.com/whx-sjtu)made their first contribution in[#5212](https://github.com/ROCm/aiter/pull/5212)

**Full Changelog**: `v0.1.21.post1...v0.1.21.post2`

## AITER v0.1.21.post1

AITER v0.1.21.post1 - post release

Post release on top of the `release/v0.1.21`

release line.

Diff base: `v0.1.21`


## Wheels

Prebuilt manylinux_2_28 wheels, `GPU_ARCHS=gfx942;gfx950`

:

## AITER v0.1.21

AITER v0.1.21 - bi-weekly release

Scheduled release from `release/v0.1.21`

.

Diff base: `v0.1.20`


## Wheels

Prebuilt manylinux_2_28 wheels, `GPU_ARCHS=gfx942;gfx950`

:

## What's Changed

## Changes

- [CI] ci: skip moe 2stage test by
[@gyohuangxin](https://github.com/gyohuangxin)in[#4828](https://github.com/ROCm/aiter/pull/4828) - [TRITON/GLUON]: Add moe_a16w4 gfx1250 gluon kernel by
[@rahulbatra85](https://github.com/rahulbatra85)in[#4446](https://github.com/ROCm/aiter/pull/4446) - [Opus MoE] Unify A8W4 metadata and runtime dispatch by
[@yifehuan](https://github.com/yifehuan)in[#4755](https://github.com/ROCm/aiter/pull/4755) - [CI] ci: temporarily skip dependency check by
[@gyohuangxin](https://github.com/gyohuangxin)in[#4842](https://github.com/ROCm/aiter/pull/4842) - [Triton/Gluon] [GFX1250] Use new preshuffling API for a4w4 MoE by
[@farlukas](https://github.com/farlukas)in[#4826](https://github.com/ROCm/aiter/pull/4826) - [CI] ci: make Aiter S3 wheel manifest cache-safe by
[@gyohuangxin](https://github.com/gyohuangxin)in[#4807](https://github.com/ROCm/aiter/pull/4807) - [HIP] [module_fused_ar_mhc] detorch fused_ar_mhc_post + pybind by
[@amd-ruitang3](https://github.com/amd-ruitang3)in[#4832](https://github.com/ROCm/aiter/pull/4832) - Alizaidy/bf16 gemm tuning 081426 by
[@azaidy](https://github.com/azaidy)in[#4749](https://github.com/ROCm/aiter/pull/4749) - fix moe ut oom by
[@yadaish](https://github.com/yadaish)in[#4844](https://github.com/ROCm/aiter/pull/4844) - [CI] ci: centralize docker login config by
[@gyohuangxin](https://github.com/gyohuangxin)in[#4846](https://github.com/ROCm/aiter/pull/4846) - fix(rope): tolerate missing original_max_position_embeddings by
[@lizamd](https://github.com/lizamd)in[#4742](https://github.com/ROCm/aiter/pull/4742) - [cache] cover int32 slot_mapping in test_kvcache by
[@i-chaochen](https://github.com/i-chaochen)in[#4697](https://github.com/ROCm/aiter/pull/4697) - [Config] perf(configs): tune bf16 GEMM for gfx1250 DeepSeek-V4-Flash shapes by
[@yichiche](https://github.com/yichiche)in[#4804](https://github.com/ROCm/aiter/pull/4804) - [Triton/Gluon] tune chunked_pa_prefill params for gfx950 by
[@nidal567](https://github.com/nidal567)in[#4718](https://github.com/ROCm/aiter/pull/4718) - [gfx950] Retune the small-M tiles and wave counts in the A16W16 fallback config by
[@akii96](https://github.com/akii96)in[#4781](https://github.com/ROCm/aiter/pull/4781) - [HIP] [GFX950]Fix OPUS MHA TypeError Issue by
[@shay-li77](https://github.com/shay-li77)in[#4847](https://github.com/ROCm/aiter/pull/4847) - [HIP] fix(topk_per_row): support ROCm 10 by dropping hipcub::Traits dependency by
[@zufayu](https://github.com/zufayu)in[#4853](https://github.com/ROCm/aiter/pull/4853) - [HIP] fix(sampling): support ROCm 10 by dropping hipcub::Traits dependency by
[@fsx950223](https://github.com/fsx950223)in[#4843](https://github.com/ROCm/aiter/pull/4843) - [FlyDSL] moe gemm optimization by
[@yadaish](https://github.com/yadaish)in[#4730](https://github.com/ROCm/aiter/pull/4730) - [CI] fix: lazily dequantize moe reference weights by
[@gyohuangxin](https://github.com/gyohuangxin)in[#4829](https://github.com/ROCm/aiter/pull/4829) - [Triton/Gluon] [Config] Tune mla_decode_rope fp32 config for gfx950 by
[@nidal567](https://github.com/nidal567)in[#4632](https://github.com/ROCm/aiter/pull/4632) - [Triton][DSV4] Fix non-stage1 paged MQA logits for KV block size > 1 by
[@skysnow2001](https://github.com/skysnow2001)in[#4825](https://github.com/ROCm/aiter/pull/4825) - [Triton/Gluon] perf(mla): chunk the non-FP4 gather_kv_b_proj over KV by
[@zejunchen-zejun](https://github.com/zejunchen-zejun)in[#4776](https://github.com/ROCm/aiter/pull/4776) - [Config] [gemm][gfx950] Tune Kimi-K3 A4W4 and FP8 projections by
[@XiaobingSuper](https://github.com/XiaobingSuper)in[#4873](https://github.com/ROCm/aiter/pull/4873) - [CK] Pin composable_kernel to 15e12dd7 by
[@JiaLuo-CAN](https://github.com/JiaLuo-CAN)in[#4861](https://github.com/ROCm/aiter/pull/4861) - [FlyDSL] Dev/tiny kernel improve by
[@yadaish](https://github.com/yadaish)in[#4597](https://github.com/ROCm/aiter/pull/4597) - [Triton/Gluon] [FlyDSL] Gfx1250 flydsl batched gemm by
[@XingerZhu](https://github.com/XingerZhu)in[#4626](https://github.com/ROCm/aiter/pull/4626) - [Triton/Gluon] [HIP] [FlyDSL] Support prefill GDN K5 fp32 chunk states and AOT coverage by
[@huizzhan](https://github.com/huizzhan)in[#4732](https://github.com/ROCm/aiter/pull/4732) - [FlyDSL] Revert " Dev/tiny kernel improve" by
[@yadaish](https://github.com/yadaish)in[#4898](https://github.com/ROCm/aiter/pull/4898) - [ASM] [gfx1250] replace bf16 prefill mha kernel by
[@tingchen988](https://github.com/tingchen988)in[#4852](https://github.com/ROCm/aiter/pull/4852) - [CI] CI: enable GLM-5.2 and dynamic nodes in ATOM DI smoke by
[@JiaoliangYu](https://github.com/JiaoliangYu)in[#4895](https://github.com/ROCm/aiter/pull/4895) - [HIP] [kernel] mrope cache-quant: accept strided flash KV-cache view by
[@vorapolsiloai](https://github.com/vorapolsiloai)in[#4531](https://github.com/ROCm/aiter/pull/4531) - [FlyDSL] [CI] [feat] mega-moe stage2 for gfx1250 by
[@yanboshao](https://github.com/yanboshao)in[#4785](https://github.com/ROCm/aiter/pull/4785) - [FlyDSL] mxfp4 MoE stage2 optimization v2 by
[@binding7012](https://github.com/binding7012)in[#4879](https://github.com/ROCm/aiter/pull/4879) - [Triton/Gluon] [Config] Add gfx1250 A16W16 GEMM configs for FLUX.2 shapes by
[@sogalin](https://github.com/sogalin)in[#4851](https://github.com/ROCm/aiter/pull/4851) - [FlyDSL] [gfx1250] optimize a8w8 mx128 bpreshuffle gemm by
[@aoli26](https://github.com/aoli26)in[#4849](https://github.com/ROCm/aiter/pull/4849) - [Triton/Gluon] [Config] move mxfp4 preshuffled into right folders by
[@Boss2002n](https://github.com/Boss2002n)in[#4900](https://github.com/ROCm/aiter/pull/4900) - [Docs] Satya/copilot instr update by
[@Boss2002n](https://github.com/Boss2002n)in[#4913](https://github.com/ROCm/aiter/pull/4913) - Skip memory-heavy moe 2stage test cases by
[@gyohuangxin](https://github.com/gyohuangxin)in[#4901](https://github.com/ROCm/aiter/pull/4901) - [Triton/Gluon] Moe A8W4 tuning by
[@lburzawa](https://github.com/lburzawa)in[#4892](https://github.com/ROCm/aiter/pull/4892) - [Triton/Gluon] [GFX1250] add triton support for gfx1250 MoE a8w4 and a4w4 by
[@nsusanto](https://github.com/nsusanto)in[#4836](https://github.com/ROCm/aiter/pull/4836) - [FlyDSL] make tiny kernel great by
[@yadaish](https://github.com/yadaish)in[#4904](https://github.com/ROCm/aiter/pull/4904) - [FlyDSL] fix a4w4 moe prefill kernel by
[@yadaish](https://github.com/yadaish)in[#4911](https://github.com/ROCm/aiter/pull/4911) - [FlyDSL] [JIT] [AOT] [FHMoE] Support native-I384 DeepSeek V4 through M=2048 by
[@Fangzhou-Ai](https://github.com/Fangzhou-Ai)in[#4891](https://github.com/ROCm/aiter/pull/4891) - [Config] yadai tune a4w4 csv by
[@yadaish](https://github.com/yadaish)in[#4914](https://github.com/ROCm/aiter/pull/4914) - [HIP] Fix and opt inverse rope group quant on gfx1250 by
[@yzhou103](https://github.com/yzhou103)in[#4806](https://github.com/ROCm/aiter/pull/4806) - [Triton/Gluon] [GFX12] mxfp8 gemm by
[@k50112113](https://github.com/k50112113)in[#4773](https://github.com/ROCm/aiter/pull/4773) - [Config] feat(minimax-m3): add TP8 tuned AITER configs by
[@zcnrex](https://github.com/zcnrex)in[#4835](https://github.com/ROCm/aiter/pull/4835) - [HIP] [JIT] [Build] [detorch] gradlib gemm + moe_mxfp4_aux + mha_native_splitkv + custom_all_reduce_gfx1250 by
[@amd-ruitang3](https://github.com/amd-ruitang3)in[#4850](https://github.com/ROCm/aiter/pull/4850) - [Triton/Gluon] Fuse block-banking cat into attn_res_gate via close_block/WRITE_BLOCK… by
[@yanxuer-999](https://github.com/yanxuer-999)in[#4726](https://github.com/ROCm/aiter/pull/4726) - [CI] ci: install Mori for multi-GPU tests by
[@gyohuangxin](https://github.com/gyohuangxin)in[#4956](https://github.com/ROCm/aiter/pull/4956) - [CI] ci: fix Mori import smoke check quoting by
[@gyohuangxin](https://github.com/gyohuangxin)in[#4959](https://github.com/ROCm/aiter/pull/4959) - [HIP] [MLA PS] workload-aware KV-split count for auto mode by
[@zejunchen-zejun](https://github.com/zejunchen-zejun)in[#4899](https://github.com/ROCm/aiter/pull/4899) - [Triton/Gluon] Force fp4gemm preshuffle to triton on gfx1250 by
[@zufayu](https://github.com/zufayu)in[#4955](https://github.com/ROCm/aiter/pull/4955) - [HIP] [GFX950]OPUS MHA Support LSE by
[@shay-li77](https://github.com/shay-li77)in[#4877](https://github.com/ROCm/aiter/pull/4877) - [Triton/Gluon] [Config] Move GEMM-A8WFP4 configs to nested layout by
[@Boss2002n](https://github.com/Boss2002n)in[#4932](https://github.com/ROCm/aiter/pull/4932) - [Triton/Gluon] [Config] Move GEMM-AFP8WFP8_PRESHUFFLED configs to nested layout by
[@Boss2002n](https://github.com/Boss2002n)in[#4933](https://github.com/ROCm/aiter/pull/4933) - [Triton/Gluon] [Config] Move GEMM-A8W8_PER_TOKEN_SCALE configs to nested layout by
[@Boss2002n](https://github.com/Boss2002n)in[#4934](https://github.com/ROCm/aiter/pull/4934) - [Triton/Gluon] [Config] Satya/migrate configs gemm a8w8 blockscale by
[@Boss2002n](https://github.com/Boss2002n)in[#4927](https://github.com/ROCm/aiter/pull/4927) - [Triton/Gluon] [Config] Move FUSED-GEMM-A8W8_BLOCKSCALE-MUL_ADD configs to nested layout by
[@Boss2002n](https://github.com/Boss2002n)in[#4939](https://github.com/ROCm/aiter/pull/4939) - [Triton/Gluon] [Config] Move GEMM-A8W8 configs to nested layout by
[@Boss2002n](https://github.com/Boss2002n)in[#4935](https://github.com/ROCm/aiter/pull/4935) - [Triton/Gluon] [Config] Move GEMM-A16WFP4 and GEMM-A16WFP4_PRESHUFFLED configs to nested layout by
[@Boss2002n](https://github.com/Boss2002n)in[#4936](https://github.com/ROCm/aiter/pull/4936) - [Triton/Gluon] [Config] Move GEMM-A16W8_BLOCKSCALE family configs to nested layout by
[@Boss2002n](https://github.com/Boss2002n)in[#4931](https://github.com/ROCm/aiter/pull/4931) - [Triton/Gluon] [Config] Move GEMM-A16W16-gated configs to nested layout by
[@Boss2002n](https://github.com/Boss2002n)in[#4928](https://github.com/ROCm/aiter/pull/4928) - [Triton/Gluon] [Config] Move GEMM-A16W16-ATOMIC configs to nested layout by
[@Boss2002n](https://github.com/Boss2002n)in[#4929](https://github.com/ROCm/aiter/pull/4929) - [Triton/Gluon] [Config] Move GEMM-A16W16 configs to nested layout by
[@Boss2002n](https://github.com/Boss2002n)in[#4930](https://github.com/ROCm/aiter/pull/4930) - [Triton/Gluon] [Config] Move FUSED-GEMM-AFP4WFP4-MUL_ADD configs to nested layout by
[@Boss2002n](https://github.com/Boss2002n)in[#4937](https://github.com/ROCm/aiter/pull/4937) - [Triton/Gluon] [Config] Move FUSED-GEMM-AFP4WFP4-A16W16 family configs to nested layout by
[@Boss2002n](https://github.com/Boss2002n)in[#4938](https://github.com/ROCm/aiter/pull/4938) - [Triton/Gluon] [Config] Move FUSED...

[Read more](https://github.com/ROCm/aiter/releases/tag/v0.1.21)

## AITER v0.1.21.dev0 (gfx1250 preview)

# AITER v0.1.21.dev0 — gfx1250 / ROCm 7.14 (pre-release)

Development wheel of `amd-aiter`

for **gfx1250 only**, on **ROCm 7.14**.

Cross-compiled, marked **pre-release**. Not an official release artifact.

Pinned to aiter commit ** b12a1904** (

`main`

HEAD 2026-08-26, MHA v4 [#4967](https://github.com/ROCm/aiter/pull/4967)).


Note on the version number.An earlier attempt tagged this build`v0.1.20.dev1`

.

Two things were wrong with it: the base version (`0.1.20.devN`

sortsbefore`v0.1.20`

,

but this build is 94 commitsafterit), and the custom`.devN`

.

That tag had to be withdrawn: setuptools_scm >= 10 rejects tags with a custom`.devN`


distance (`ValueError: choosing custom numbers for the .devX distance is not supported`

),

and because the tag sat on`main`

HEAD it broke every from-source build of aiter at that

commit — including ROCm/ATOM's nightly Docker CI, which tracks HEAD.

`v0.1.21.dev0`

ends in`.dev0`

, which setuptools_scm supports, and it also orders

correctly (`0.1.20 < 0.1.21.dev0 < 0.1.21`

).

If you tag aiter, avoid custom`.devN`

— use`.dev0`

,`-rcN`

, or a plain version.

## Why this exists

gfx1250 is not in the official release matrix (`GPU_ARCHS=gfx942;gfx950`

), so no GA

wheel covers it. This is the second gfx1250 preview; see

[v0.1.20.dev0](https://github.com/ROCm/aiter/releases/tag/v0.1.20.dev0) for the

first one (pinned to `d9e5ef7`

, 2026-07-29).

## Required environment

```
SGLANG_USE_AITER_MOE_GU_ITLV=1
```


**This is mandatory.** It makes SGLang lay out the MoE `w13`

/`w2`

weights and scales

in the gate/up-interleaved (GUGU) form that the gfx1250 kernels expect

(`fp8.py: shuffle_weight(..., is_guinterleave=gu_intv)`

and `shuffle_scale(...)`

).

With `=0`

the weights are prepared SEPARATED (GGUU) and the run falls through to the

FlyDSL heuristic path — see [#4987](https://github.com/ROCm/aiter/issues/4987).

## Status on real gfx1250 hardware

| Item | Result |
|---|---|
| Server start (DeepSeek-V4-Flash, tp=1) | OK — ready in ~353 s |
FlyDSL `raw.ptr.buffer.load.lds` crash (
|
No longer hit |
| aiter/SGLang API mismatch | None |
| gsm8k completes | Yes |
gsm8k accuracy |
≈ 0.030 — see below |

⚠️ Open accuracy regression

`gsm8k accuracy ≈ 0.030`

against **0.925** on

[v0.1.20.dev0](https://github.com/ROCm/aiter/releases/tag/v0.1.20.dev0)

(`d9e5ef7`

), same model, same SGLang recipe.

**Root cause is not yet attributed.** It is not known whether this originates in aiter,

in SGLang, or in the interaction between the two. It is tracked separately and does not

block this packaging: the process no longer aborts, the server starts, and the benchmark

runs to completion — i.e. the gfx1250 build itself is functional.

**If you need known-good accuracy today, use v0.1.20.dev0.**

Use this build for bring-up, integration, and to pick up the 94 commits since v0.1.20.

## How this differs from official wheels

| Official (v0.1.20) | This build | |
|---|---|---|
| Assets | 6 (ROCm 7.0/7.1/7.2 × py3.10/3.12) | 1 (ROCm 7.14 × py3.12) |
`GPU_ARCHS` |
`gfx942;gfx950` |
`gfx1250` |
| Platform tag | `manylinux_2_27/2_28_x86_64` |
`linux_x86_64` (NOT manylinux) |
| Build image | `pytorch/manylinux2_28-builder` (glibc 2.28) |
Ubuntu 22.04 (glibc 2.35) |
`ENABLE_CK` |
1 | 0 |
| Source | unmodified | 1 patch applied (below) |

**Runtime requirements**

**glibc ≥ 2.35**— not manylinux-compatible; will fail`dlopen`

in older containers.

Verified against the Ubuntu 24.04 (glibc 2.39) MI455 image.**torch 2.11.0+rocm7.14.0****flydsl**—`pip install --no-deps`

does not pull it. Install the version matching

this build explicitly; a mismatched flydsl fails with a`RawPtrBufferLoadOp`

arity error.

**This wheel contains gfx1250 device code only.** It has no kernels for gfx942/gfx950 —

it does not replace the official wheels for those architectures. A single wheel cannot

serve both: `ENABLE_CK`

is a per-build switch (gfx1250 needs `0`

, CDNA needs `1`

, and

disabling CK excludes 70 modules), and module exclusion is per-build rather than per-arch.

## Patch required to build for gfx1250

`aiter-gfx1250-module-exclusion.patch`

— aiter's module selection ignores the target

architecture, so CDNA-only modules are attempted on gfx1250 and fail to compile:

`__builtin_amdgcn_mfma_*`

needs`gfx90a-insts`

`__builtin_amdgcn_raw_ptr_buffer_load_lds`

needs`vmem-to-lds-load-insts`

`-mwavefrontsize64`

is rejected (gfx12 is wave32-only)- some kernels fail via a wave32
`static_assert`

on`warp_size`

rather than a detectable

builtin (e.g.`module_dsv4_rotate_quant`

,`module_chunk_gdr_fwd_h`

)

**19 modules are excluded for gfx1250, including all mha_*.** The CK

`amd_tdm_store`

stray-brace fix needed for earlier commits is **not**required here.

## Known limitations on gfx1250

**No native MHA backend.**`mha_native`

needs MFMA and buffer-load-to-LDS, neither of

which exists on gfx1250. Route attention through Triton

(SGLang:`SGLANG_HACK_FLASHMLA_BACKEND=unified_kv_triton`

).**FlyDSL AOT does not target gfx1250.**`_CU_NUM_TO_ARCH`

maps only gfx942/gfx950;

MOE/GEMM/CHUNK_GDN_H default to gfx950. Expect first-run JIT rather than AOT cache hits.

The non-gfx1250 AOT cache and prebuilt ASM are stripped from this wheel.- Not validated by the 5-model GSM8K gate — no gfx1250 runner exists in the pool.

## vs v0.1.20

Cut from `main`

@ `b12a1904`

— **94 commits** since v0.1.20 (`fc2e5d57`

),

of which 12 touch gfx1250 and 25 touch MoE/FlyDSL.

### gfx1250

- [ASM] [HIP] [gfx1250] fix(asm gemm): add a_preshuffle=0 f4gemm & f8gemm, fix corner case support and enhance ut (
[#4748](https://github.com/ROCm/aiter/pull/4748)) - [Triton/Gluon] Force fp4gemm preshuffle to triton on gfx1250 (
[#4955](https://github.com/ROCm/aiter/pull/4955)) - [HIP] [JIT] [Build] [detorch] gradlib gemm + moe_mxfp4_aux + mha_native_splitkv + custom_all_reduce_gfx1250 (
[#4850](https://github.com/ROCm/aiter/pull/4850)) - [HIP] Fix and opt inverse rope group quant on gfx1250 (
[#4806](https://github.com/ROCm/aiter/pull/4806)) - [Triton/Gluon] [GFX1250] add triton support for gfx1250 MoE a8w4 and a4w4 (
[#4836](https://github.com/ROCm/aiter/pull/4836)) - [FlyDSL] [gfx1250] optimize a8w8 mx128 bpreshuffle gemm (
[#4849](https://github.com/ROCm/aiter/pull/4849)) - [Triton/Gluon] [Config] Add gfx1250 A16W16 GEMM configs for FLUX.2 shapes (
[#4851](https://github.com/ROCm/aiter/pull/4851)) - [FlyDSL] [CI] [feat] mega-moe stage2 for gfx1250 (
[#4785](https://github.com/ROCm/aiter/pull/4785)) - [Triton/Gluon] [FlyDSL] Gfx1250 flydsl batched gemm (
[#4626](https://github.com/ROCm/aiter/pull/4626)) - perf(configs): tune bf16 GEMM for gfx1250 DeepSeek-V4-Flash shapes (
[#4804](https://github.com/ROCm/aiter/pull/4804)) - [Triton/Gluon] [GFX1250] Use new preshuffling API for a4w4 MoE (
[#4826](https://github.com/ROCm/aiter/pull/4826)) - [TRITON/GLUON]: Add moe_a16w4 gfx1250 gluon kernel (
[#4446](https://github.com/ROCm/aiter/pull/4446))

### Other highlights

- [Triton/Gluon] [ASM] [HIP] MHA v4: support GQA, add gfx950 bf16, add gfx942 i8/fp8 (
[#4967](https://github.com/ROCm/aiter/pull/4967)) - [HIP] topk_gating: fix dropped and out-of-range top-k slots (
[#4965](https://github.com/ROCm/aiter/pull/4965)) - CI: skip MegaMoE v2 multi-GPU tests (
[#5003](https://github.com/ROCm/aiter/pull/5003)) - [Triton/Gluon] Remove legacy MOE code (
[#4833](https://github.com/ROCm/aiter/pull/4833)) - [AMD][DSV4] feat: MXFP8 activation passthrough in fused_moe (
[#4954](https://github.com/ROCm/aiter/pull/4954)) - [Triton] Move stray BATCHED_GEMM-A8W8 prequant configs to nested layout (
[#4982](https://github.com/ROCm/aiter/pull/4982)) - [Triton/Gluon] [GFX950][DSV4] Sparse MLA training backward (
[#4766](https://github.com/ROCm/aiter/pull/4766)) - fix a scale tdm inner oob (
[#4988](https://github.com/ROCm/aiter/pull/4988)) - [Config] Add tuned GEMM configs for Kimi-K3 BF16 MoE front shapes (
[#4834](https://github.com/ROCm/aiter/pull/4834)) - fix(flydsl): stabilize GDN prepare triangular solve (
[#4952](https://github.com/ROCm/aiter/pull/4952)) - fix(mha): select sink kernel when only sink_ptr is provided (
[#4976](https://github.com/ROCm/aiter/pull/4976)) - [Triton/Gluon] [Config] [gfx950] Tune batched_gemm_a8w8 per-token-group for large M (MLA absorb bmm) (
[#4453](https://github.com/ROCm/aiter/pull/4453)) - [Triton] Move BATCHED_GEMM-A8W8-A_PER_TOKEN_GROUP_PREQUANT_W_PER_BATCHED_TENSOR_QUANT configs to nested layout (
[#4943](https://github.com/ROCm/aiter/pull/4943)) - [Triton] Move BATCHED_GEMM-A8W8 configs to nested layout (
[#4944](https://github.com/ROCm/aiter/pull/4944)) - [Triton] Move BATCHED_GEMM-A16W16 configs to nested layout (
[#4946](https://github.com/ROCm/aiter/pull/4946)) - [Triton] Move BATCHED_GEMM-A16WFP4 configs to nested layout (
[#4945](https://github.com/ROCm/aiter/pull/4945)) - [Triton] Move BATCHED_GEMM-AFP4WFP4 configs to nested layout (
[#4942](https://github.com/ROCm/aiter/pull/4942)) - [Triton] Move FUSED-GEMM-A8W8_BLOCKSCALE-A16W16 configs to nested layout (
[#4940](https://github.com/ROCm/aiter/pull/4940))

*(full list: git log --oneline v0.1.20..b12a1904)*

## AITER v0.1.20

AITER v0.1.20 — bi-weekly release.

Cut from `release/v0.1.20`

@ `fc2e5d57`

and diffed against `v0.1.19`

. This is the scheduled release line, not a post-release hotfix.

## Wheels

Prebuilt manylinux_2_28 wheels, `GPU_ARCHS=gfx942;gfx950`

:

## Build runs

- ROCm 7.0 cp310:
[https://github.com/ROCm/aiter/actions/runs/32124560585](https://github.com/ROCm/aiter/actions/runs/32124560585) - ROCm 7.0 cp312:
[https://github.com/ROCm/aiter/actions/runs/32215589704](https://github.com/ROCm/aiter/actions/runs/32215589704) - ROCm 7.1 cp310:
[https://github.com/ROCm/aiter/actions/runs/32211815213](https://github.com/ROCm/aiter/actions/runs/32211815213) - ROCm 7.1 cp312:
[https://github.com/ROCm/aiter/actions/runs/32124599999](https://github.com/ROCm/aiter/actions/runs/32124599999) - ROCm 7.2 cp310/cp312:
[https://github.com/ROCm/aiter/actions/runs/32124600442](https://github.com/ROCm/aiter/actions/runs/32124600442)

## What's Changed

## Changes

- [Triton/Gluon] Streamline GEMM and MoE configs by
[@Boss2002n](https://github.com/Boss2002n)in[#4379](https://github.com/ROCm/aiter/pull/4379) - Fix: add missing end_sync barrier in fused allreduce+rmsnorm kernel by
[@yuzho-amd](https://github.com/yuzho-amd)in[#4346](https://github.com/ROCm/aiter/pull/4346) - docs(readme): announce Kimi-K3 support in News by
[@carlushuang](https://github.com/carlushuang)in[#4404](https://github.com/ROCm/aiter/pull/4404) - DeepSeek-V4 FP4: fused_compress FP4 scatter + rmsnorm_rope_rotate FP4 KV-cache kernel by
[@junhaha666](https://github.com/junhaha666)in[#4029](https://github.com/ROCm/aiter/pull/4029) - [module_pos_encoding] refactor and rm torch by
[@amd-ruitang3](https://github.com/amd-ruitang3)in[#4393](https://github.com/ROCm/aiter/pull/4393) - Correcting errors and discrepancies in the MLA v4 mi355 kernel design documents by
[@ruanjm](https://github.com/ruanjm)in[#4392](https://github.com/ROCm/aiter/pull/4392) - [FLYDSL] Support paged mqa logits fp4 varqlen kernel by
[@zhiding512](https://github.com/zhiding512)in[#4230](https://github.com/ROCm/aiter/pull/4230) - [CI] pin ruff and make its configuration explicit by
[@valarLip](https://github.com/valarLip)in[#4403](https://github.com/ROCm/aiter/pull/4403) - Fix Q UE8M0 quant and require fp32 LN params in fused DSv3.2 indexer kernel by
[@frida-andersson](https://github.com/frida-andersson)in[#3451](https://github.com/ROCm/aiter/pull/3451) - refactor(flydsl): vendor buffer_ops/vector into aiter by
[@Phil-amd](https://github.com/Phil-amd)in[#4402](https://github.com/ROCm/aiter/pull/4402) - [MLA][gluon] support nhead=96 for MLA by
[@yanxuer-999](https://github.com/yanxuer-999)in[#4412](https://github.com/ROCm/aiter/pull/4412) - fix(gemm_a8w8_blockscale): prevent scale OOB and support Triton 3.6 by
[@bingxche](https://github.com/bingxche)in[#4406](https://github.com/ROCm/aiter/pull/4406) - [tune] Kimi-K2.5/K2.6 fp4: port BM16 (flydsl_mxmoe_g*_a4w4) for decode gemm2 (+3~13% throughput) by
[@jiacao-amd](https://github.com/jiacao-amd)in[#4307](https://github.com/ROCm/aiter/pull/4307) - [module_quick_all_reduce] refactor and rm torch by
[@amd-ruitang3](https://github.com/amd-ruitang3)in[#4421](https://github.com/ROCm/aiter/pull/4421) - Enable stride aware indexing on top of strided blocks for block_size and heads (assumes contiguous head dim) of fused_qk_norm_rope_cache_pts_quant_shuffle() by
[@jhu960213](https://github.com/jhu960213)in[#4312](https://github.com/ROCm/aiter/pull/4312) - fix: synchronize custom collectives before return by
[@jpy794](https://github.com/jpy794)in[#4082](https://github.com/ROCm/aiter/pull/4082) - Fix fused_qk_rope_concat_and_cache_mla for DCP by
[@yitingw1](https://github.com/yitingw1)in[#4342](https://github.com/ROCm/aiter/pull/4342) - [gfx1250][FlyDSL] Refactor GEMMs with layout-based API by
[@aoli26](https://github.com/aoli26)in[#4374](https://github.com/ROCm/aiter/pull/4374) - fix(dsv4): use vec_size=32 for dim=1024 rotate-quant kernels by
[@XiaobingSuper](https://github.com/XiaobingSuper)in[#4438](https://github.com/ROCm/aiter/pull/4438) - fix(flydsl-aot): map Situv2 activation in MoE AOT parse_csv by
[@coderfeli](https://github.com/coderfeli)in[#4429](https://github.com/ROCm/aiter/pull/4429) - [Triton] [Gluon] [GFX12] DSV4 Pro EP tunning (=TP1 shape) by
[@k50112113](https://github.com/k50112113)in[#4253](https://github.com/ROCm/aiter/pull/4253) - fix(mla): refresh qh16 fp8 persistent decode HSACO for large page_id by
[@fangche123](https://github.com/fangche123)in[#4341](https://github.com/ROCm/aiter/pull/4341) - Fix large-token FlyDSL MoE launch and output limits by
[@XiaobingSuper](https://github.com/XiaobingSuper)in[#4417](https://github.com/ROCm/aiter/pull/4417) - [module_rmsnorm_quant] refactor and rm torch by
[@amd-ruitang3](https://github.com/amd-ruitang3)in[#4434](https://github.com/ROCm/aiter/pull/4434) - [MoE] Add swiglu_oai (OAI SwiGLU) for per-token fp8 CK XDL 2-stage MoE by
[@LJ-underdog](https://github.com/LJ-underdog)in[#3886](https://github.com/ROCm/aiter/pull/3886) - [CK][VSA] Add thin sparse attention operator by
[@LiuYinfeng01](https://github.com/LiuYinfeng01)in[#4373](https://github.com/ROCm/aiter/pull/4373) - feat(topksoftmax): add 640-expert top-8 asm kernels for gfx942/gfx950 by
[@junhaha666](https://github.com/junhaha666)in[#4454](https://github.com/ROCm/aiter/pull/4454) - [triton] Optimized Unified Attention for Gemma-4-31b by
[@a-sidorova](https://github.com/a-sidorova)in[#4044](https://github.com/ROCm/aiter/pull/4044) - ci: extend multi-gpu test timeout by
[@gyohuangxin](https://github.com/gyohuangxin)in[#4468](https://github.com/ROCm/aiter/pull/4468) - Fix for 32 bit GU offsets overflow by
[@JohnNikolay84](https://github.com/JohnNikolay84)in[#4449](https://github.com/ROCm/aiter/pull/4449) - Add inverse_rope_group_quant op for DeepSeek-V4 wo_a input by
[@yzhou103](https://github.com/yzhou103)in[#4428](https://github.com/ROCm/aiter/pull/4428) - moe rebase and refactor by
[@yadaish](https://github.com/yadaish)in[#4394](https://github.com/ROCm/aiter/pull/4394) - [opus_moe] production A8W4 MoE stage1 kernels by
[@yifehuan](https://github.com/yifehuan)in[#4464](https://github.com/ROCm/aiter/pull/4464) - [config] add k3 gemm&moe tuned configs by
[@gbyu-amd](https://github.com/gbyu-amd)in[#4435](https://github.com/ROCm/aiter/pull/4435) - [Feature][FlyDSL] Add fused heterogeneous MXFP4/FP8 shared-expert MoE (FHMoE) and share the mixed-MoE kernel builders by
[@Fangzhou-Ai](https://github.com/Fangzhou-Ai)in[#4269](https://github.com/ROCm/aiter/pull/4269) - Flydsl kernel cleanup by
[@coderfeli](https://github.com/coderfeli)in[#4501](https://github.com/ROCm/aiter/pull/4501) - Add an opt-in a4w4 SiTUv2 MoE path and fix three SiTUv2 tuner defects by
[@XiaobingSuper](https://github.com/XiaobingSuper)in[#4463](https://github.com/ROCm/aiter/pull/4463) - optimize ctypes marshalling by
[@amd-ruitang3](https://github.com/amd-ruitang3)in[#4465](https://github.com/ROCm/aiter/pull/4465) - CI: auto-update split test FILE_TIMES by @aiter-gh-app[bot] in
[#4518](https://github.com/ROCm/aiter/pull/4518) - fix(module_rmsnorm_quant): bound packed FP4 output stores by
[@gbyu-amd](https://github.com/gbyu-amd)in[#4467](https://github.com/ROCm/aiter/pull/4467) - [Perf][FlyDSL] Tune DeepSeek V4 fused MoE for C1/C2/C32/C64 decode by
[@Fangzhou-Ai](https://github.com/Fangzhou-Ai)in[#4314](https://github.com/ROCm/aiter/pull/4314) - [gfx1250][FlyDSL] Unify&Rename GEMM kernels and refactor LDS load by
[@aoli26](https://github.com/aoli26)in[#4527](https://github.com/ROCm/aiter/pull/4527) - chore(flydsl): bump flydsl dependency to 0.3.0 by
[@coderfeli](https://github.com/coderfeli)in[#4431](https://github.com/ROCm/aiter/pull/4431) - Fix LDS allocation for B-to-LDS FlyDSL Split-K HGEMM by
[@xytpai](https://github.com/xytpai)in[#4529](https://github.com/ROCm/aiter/pull/4529) - Flash attention sliding window tests by
[@micmelesse](https://github.com/micmelesse)in[#4003](https://github.com/ROCm/aiter/pull/4003) - gfx1250: fix the grouped-MoE expert scan above 512 experts, and compute SiTUv2 instead of SiLU by
[@XiaobingSuper](https://github.com/XiaobingSuper)in[#4482](https://github.com/ROCm/aiter/pull/4482) - ci: switch MI300X jobs to OCI runners by
[@gyohuangxin](https://github.com/gyohuangxin)in[#4520](https://github.com/ROCm/aiter/pull/4520) - [fmoe][gfx950]Flydsl mxmoe v2 by
[@charlieguo1106](https://github.com/charlieguo1106)in[#4179](https://github.com/ROCm/aiter/pull/4179) - [CI] Fix SGLang downstream setup and enable DSV3.2 accuracy by
[@bingxche](https://github.com/bingxche)in[#4516](https://github.com/ROCm/aiter/pull/4516) - [Bugfix][Triton] Fix int32 KV-offset overflow in _mla_gluon >2GB path by
[@peizhang56](https://github.com/peizhang56)in[#4474](https://github.com/ROCm/aiter/pull/4474) - [gfx1250] update asm f4gemm, add fp8 out support, enhance ut by
[@dbyoung18](https://github.com/dbyoung18)in[#4335](https://github.com/ROCm/aiter/pull/4335) - [PERF] Eliminate varlen prefill GDN D2H synchronization with reusable metadata by
[@yiijin](https://github.com/yiijin)in[#4532](https://github.com/ROCm/aiter/pull/4532) - fix mxmoe CI bug(flydsl0.2.4->0.3.0) by
[@charlieguo1106](https://github.com/charlieguo1106)in[#4553](https://github.com/ROCm/aiter/pull/4553) - [triton] fix transpose_scale in fused_rms_fp8_group_quant (was silently row-major) by
[@karverma-amd](https://github.com/karverma-amd)in[#4506](https://github.com/ROCm/aiter/pull/4506) - [TRITON][GLUON] Fixing Python 3.14 Compatibility Issue About
[@aggregate](https://github.com/aggregate)by[@cagrikymk](https://github.com/cagrikymk)in[#4508](https://github.com/ROCm/aiter/pull/4508) - [fix][flydsl] fix oob scale descriptor in ptpc fp8 gemm by
[@gbyu-amd](https://github.com/gbyu-amd)in[#4546](https://github.com/ROCm/aiter/pull/4546) - [gfx1250] Route the missing Kimi-K3 fused BF16 GEMM to Triton by
[@XiaobingSuper](https://github.com/XiaobingSuper)in[#4552](https://github.com/ROCm/aiter/pull/4552) - [dist] forward transpose_scale through fused AR+RMSNorm per-group quant by
[@yichiche](https://github.com/yichiche)in[#4478](https://github.com/ROCm/aiter/pull/4478) - fix(mla): refresh gfx950 MLA HSACO for large page_id KV addressing by
[@fangche123](https://github.com/fangche123)in[#4452](https://github.com/ROCm/aiter/pull/4452) - configs: add DSv3-MXFP4 E=33/topk9 fused-MoE shape (shared-expert fus… by
[@rbrugaro-amd](https://github.com/rbrugaro-amd)in[#3739](https://github.com/ROCm/aiter/pull/3739) - [Fix] Add assert for layernorm weight/input dtype mismatch by
[@yitingw1](https://github.com/yitingw1)in[#4567](https://github.com/ROCm/aiter/pull/4567) - [OpusMoe] optimize opus moe situv2 ability by
[@yifehuan](https://github.com/yifehuan)in[#4534](https://github.com/ROCm/aiter/pull/4534) - MXMoE kernels for Qwen3.5-397B TP2 decode by
[@zijiecode](https://github.com/zijiecode)in[#4513](https://github.com/ROCm/aiter/pull/4513) - MI350 MLA PS mode add ds32 opus kernel for nhead*qseqlen=128 case by
[@minmengdie](https://github.com/minmengdie)in[https://github.co](https://github.co)...

[Read more](https://github.com/ROCm/aiter/releases/tag/v0.1.20)

## v0.1.19.post2

enable v3 decode mla long context support

## v0.1.19.post1

For decode mla v3 long context support

## AITER v0.1.20.dev0

# AITER v0.1.20.dev0 — gfx1250 / ROCm 7.14 (pre-release)

Development wheel of `amd-aiter`

for **gfx1250** on **ROCm 7.14**.

Cross-compiled, validated on real gfx1250 hardware. Marked **pre-release**.

## What this is

A `.dev0`

snapshot pinned to aiter commit ** d9e5ef7** (PR

[#4406](https://github.com/ROCm/aiter/pull/4406)), the last

commit that runs DeepSeek-V4 on gfx1250

**without**the FlyDSL lowering crash

(

`raw.ptr.buffer.load.lds`

→ `LLVM ERROR: Do not know how to expand this operator's operand`

). Later commits re-introduce that crash on gfx1250.## Asset

| file | sha256 |
|---|---|
`amd_aiter-0.1.20.dev0+rocm7.14.0.gfx1250-cp312-cp312-linux_x86_64.whl` |
`8484202f16d13b267ff17d78db6c9936683fdce2f86c1840346f52308ce92b6f` |

- size 88 MB · Python 3.12 · torch
**2.11.0+rocm7.14.0**· flydsl**0.2.4**

## Validation (real gfx1250)

- SGLang · DeepSeek-V4-Flash · tp1 · attention-backend dsv4 · kv fp8_e4m3
**gsm8k 0.925**(Invalid 0.000, server exit 0); server log flydsl count = 0

## Install

```
pip install --force-reinstall --no-deps amd_aiter-0.1.20.dev0+rocm7.14.0.gfx1250-cp312-cp312-linux_x86_64.whl
pip install --force-reinstall --no-deps flydsl==0.2.4
# ensure no source-tree aiter (/app/aiter, /sgl-workspace/aiter) shadows the wheel
```

## Caveats

- Built on glibc 2.35 →
**not manylinux_2_28**; for gfx1250 self-use, not the

official 6-wheel matrix (which is gfx942;gfx950). - torch ABI must match the target container's torch exactly.