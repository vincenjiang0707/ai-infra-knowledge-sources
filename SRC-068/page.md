# FlashInfer

source: https://github.com/Dao-AILab/flash-attention/releases

# Releases: Dao-AILab/flash-attention

Releases · Dao-AILab/flash-attention

## Release list

## fa4-v4.0.0.beta31

## What's Changed

- Add an Attention Sink to Flash MLA for SM100 by
[@floatingtrees](https://github.com/floatingtrees)in[#2768](https://github.com/Dao-AILab/flash-attention/pull/2768) - [CuTe, SM100] Stop the non-causal hdim 128 softmax warps spilling by
[@dawnop](https://github.com/dawnop)in[#2869](https://github.com/Dao-AILab/flash-attention/pull/2869) - [CuTe, SM100] hd256 2-CTA: support seqused_q/seqused_k and the decoder paged-KV shape by
[@kzos](https://github.com/kzos)in[#2810](https://github.com/Dao-AILab/flash-attention/pull/2810) - [CuTe, SM100] Preserve hd256 output alignment for vectorized stores by
[@drisspg](https://github.com/drisspg)in[#2880](https://github.com/Dao-AILab/flash-attention/pull/2880) - One more deprecation; by
[@drisspg](https://github.com/drisspg)in[#2867](https://github.com/Dao-AILab/flash-attention/pull/2867) - [CuTe, SM100, HD256] optimize SM100 HD256 varlen scheduling and epilogues by
[@catwinee](https://github.com/catwinee)in[#2807](https://github.com/Dao-AILab/flash-attention/pull/2807) - [CuTe, SM90] Fix swapped backward MMA layout and use 2-stage hdim256 config by
[@SuperGoodGame](https://github.com/SuperGoodGame)in[#2888](https://github.com/Dao-AILab/flash-attention/pull/2888) - [CuTe, Bwd] Return zero gradients for empty Q/K workloads by
[@guoriyue](https://github.com/guoriyue)in[#2776](https://github.com/Dao-AILab/flash-attention/pull/2776) - [CuTe, Fwd] Fix PackGQA predication for padded head dimensions by
[@guoriyue](https://github.com/guoriyue)in[#2775](https://github.com/Dao-AILab/flash-attention/pull/2775)

## New Contributors

[@floatingtrees](https://github.com/floatingtrees)made their first contribution in[#2768](https://github.com/Dao-AILab/flash-attention/pull/2768)[@dawnop](https://github.com/dawnop)made their first contribution in[#2869](https://github.com/Dao-AILab/flash-attention/pull/2869)[@kzos](https://github.com/kzos)made their first contribution in[#2810](https://github.com/Dao-AILab/flash-attention/pull/2810)[@catwinee](https://github.com/catwinee)made their first contribution in[#2807](https://github.com/Dao-AILab/flash-attention/pull/2807)[@SuperGoodGame](https://github.com/SuperGoodGame)made their first contribution in[#2888](https://github.com/Dao-AILab/flash-attention/pull/2888)

**Full Changelog**: `fa4-v4.0.0.beta30...fa4-v4.0.0.beta31`

## fa4-v4.0.0.beta30

## What's Changed

- [CuTe, SM80/SM120] Guard invalid varlen forward tiles by
[@eamonn-zh](https://github.com/eamonn-zh)in[#2763](https://github.com/Dao-AILab/flash-attention/pull/2763) - [CuTe] Include callable defaults in JIT cache hashes by
[@guoriyue](https://github.com/guoriyue)in[#2773](https://github.com/Dao-AILab/flash-attention/pull/2773) - [CuTe,Bwd,Sm100] Support head_dim not a multiple of 32 in backward by
[@KaijingOfficial](https://github.com/KaijingOfficial)in[#2698](https://github.com/Dao-AILab/flash-attention/pull/2698) - [CuTe] Speed up SM100 hdim-64 bwd: dedicated P/dS TMEM slots + per-warp signaling by
[@jack-carlisle-2025](https://github.com/jack-carlisle-2025)in[#2804](https://github.com/Dao-AILab/flash-attention/pull/2804) - cute: don't widen intentionally-empty offset windows to full attention by
[@cora-codes](https://github.com/cora-codes)in[#2490](https://github.com/Dao-AILab/flash-attention/pull/2490) - Fix
`seqlen_k_loaded`

treating a window bound of 0 as unbounded (sliding window) by[@lollinng](https://github.com/lollinng)in[#2624](https://github.com/Dao-AILab/flash-attention/pull/2624) - Fix SM90 bwd crash for head_dim in (128, 192] by
[@cora-codes](https://github.com/cora-codes)in[#2482](https://github.com/Dao-AILab/flash-attention/pull/2482)

## New Contributors

[@guoriyue](https://github.com/guoriyue)made their first contribution in[#2773](https://github.com/Dao-AILab/flash-attention/pull/2773)[@KaijingOfficial](https://github.com/KaijingOfficial)made their first contribution in[#2698](https://github.com/Dao-AILab/flash-attention/pull/2698)[@jack-carlisle-2025](https://github.com/jack-carlisle-2025)made their first contribution in[#2804](https://github.com/Dao-AILab/flash-attention/pull/2804)[@cora-codes](https://github.com/cora-codes)made their first contribution in[#2490](https://github.com/Dao-AILab/flash-attention/pull/2490)[@lollinng](https://github.com/lollinng)made their first contribution in[#2624](https://github.com/Dao-AILab/flash-attention/pull/2624)

**Full Changelog**: `fa4-v4.0.0.beta29...fa4-v4.0.0.beta30`

## fa4-v4.0.0.beta29

## fa4-v4.0.0.beta28

## fa4-v4.0.0.beta27

## fa4-v4.0.0.beta26

## What's Changed

- [CuTe,Bwd,Sm90] Fix: wait for bwd_preprocess on the block-sparse path, matching the dense path by
[@Fugoes](https://github.com/Fugoes)in[#2756](https://github.com/Dao-AILab/flash-attention/pull/2756) - [Cute, bwd, sm90/100/110] Support learnable sink in backward by
[@henrylhtsang](https://github.com/henrylhtsang)in[#2706](https://github.com/Dao-AILab/flash-attention/pull/2706) - [CuTe, FA4] Preserve first-tile flag during scheduler reconstruction by
[@dongxiao92](https://github.com/dongxiao92)in[#2705](https://github.com/Dao-AILab/flash-attention/pull/2705) - Fix duplicated word in layer norm comment by
[@cupkk](https://github.com/cupkk)in[#2744](https://github.com/Dao-AILab/flash-attention/pull/2744) - [CuTe, SM100] Fix deadlock in varlen + block-sparse + SplitKV forward by
[@JiaxuanBai](https://github.com/JiaxuanBai)in[#2761](https://github.com/Dao-AILab/flash-attention/pull/2761) - [CuTe, Fwd] Fix forward compile key churn when max_seqlen is a tensor by
[@eamonn-zh](https://github.com/eamonn-zh)in[#2762](https://github.com/Dao-AILab/flash-attention/pull/2762) - [CuTe] Fix forward dynamic-shape correctness by
[@drisspg](https://github.com/drisspg)in[#2745](https://github.com/Dao-AILab/flash-attention/pull/2745) - Fix CLC fuzz scheduler expectations by
[@JiaxuanBai](https://github.com/JiaxuanBai)in[#2766](https://github.com/Dao-AILab/flash-attention/pull/2766) - Fix removed Quack packed subtraction API by
[@JiaxuanBai](https://github.com/JiaxuanBai)in[#2787](https://github.com/Dao-AILab/flash-attention/pull/2787)

## New Contributors

[@Fugoes](https://github.com/Fugoes)made their first contribution in[#2756](https://github.com/Dao-AILab/flash-attention/pull/2756)[@dongxiao92](https://github.com/dongxiao92)made their first contribution in[#2705](https://github.com/Dao-AILab/flash-attention/pull/2705)[@cupkk](https://github.com/cupkk)made their first contribution in[#2744](https://github.com/Dao-AILab/flash-attention/pull/2744)[@JiaxuanBai](https://github.com/JiaxuanBai)made their first contribution in[#2761](https://github.com/Dao-AILab/flash-attention/pull/2761)[@eamonn-zh](https://github.com/eamonn-zh)made their first contribution in[#2762](https://github.com/Dao-AILab/flash-attention/pull/2762)

**Full Changelog**: `fa4-v4.0.0.beta25...fa4-v4.0.0.beta26`

## fa4-v4.0.0.beta25

## What's Changed

- Remove SM100 Functions from Hopper Flash Attention 3 by
[@ankutalev](https://github.com/ankutalev)in[#2746](https://github.com/Dao-AILab/flash-attention/pull/2746) - [CuTe,Sm100] Varlen Dynamic Persistent scheduler and metadata by
[@reubenconducts](https://github.com/reubenconducts)in[#2559](https://github.com/Dao-AILab/flash-attention/pull/2559) - [AI] Add doc on debug methodology by
[@jayhshah](https://github.com/jayhshah)in[#2753](https://github.com/Dao-AILab/flash-attention/pull/2753) - [ROCm] Fix CK varlen_fwd binding argument mismatch by
[@hyoon1](https://github.com/hyoon1)in[#2742](https://github.com/Dao-AILab/flash-attention/pull/2742) - [CuTe, SM100] Sparse MLA bwd: don't scatter dK/dV at -1 sentinel indices by
[@abcdabcd987](https://github.com/abcdabcd987)in[#2755](https://github.com/Dao-AILab/flash-attention/pull/2755)

## New Contributors

[@hyoon1](https://github.com/hyoon1)made their first contribution in[#2742](https://github.com/Dao-AILab/flash-attention/pull/2742)[@abcdabcd987](https://github.com/abcdabcd987)made their first contribution in[#2755](https://github.com/Dao-AILab/flash-attention/pull/2755)

**Full Changelog**: `fa4-v4.0.0.beta24...fa4-v4.0.0.beta25`

## fa4-v4.0.0.beta24

## What's Changed

- [CuTe, Flex] Allow score mod use in varlen backward by
[@reubenconducts](https://github.com/reubenconducts)in[#2547](https://github.com/Dao-AILab/flash-attention/pull/2547) - Expand FLASHATTENTION_DISABLE_DROPOUT to not bring in unneeded headers by
[@janeyx99](https://github.com/janeyx99)in[#2669](https://github.com/Dao-AILab/flash-attention/pull/2669) - add linearize scheduling to combine kernel for full cudagraph by
[@liangel-02](https://github.com/liangel-02)in[#2692](https://github.com/Dao-AILab/flash-attention/pull/2692) - Numeric tweaks to fp8 by
[@drisspg](https://github.com/drisspg)in[#2731](https://github.com/Dao-AILab/flash-attention/pull/2731)

**Full Changelog**: `fa4-v4.0.0.beta23...fa4-v4.0.0.beta24`

## fa4-v4.0.0.beta23

## What's Changed

- Add paged-KV block_table bounds check in mha_fwd_kvcache by
[@yunweili3](https://github.com/yunweili3)in[#2711](https://github.com/Dao-AILab/flash-attention/pull/2711) - [CuTe, SM100] Fix FP8 e4m3 accuracy: make max_offset dtype-aware to avoid P saturation by
[@yunweili3](https://github.com/yunweili3)in[#2717](https://github.com/Dao-AILab/flash-attention/pull/2717)

**Full Changelog**: `fa4-v4.0.0.beta22...fa4-v4.0.0.beta23`

## fa4-v4.0.0.beta22

## What's Changed

- add tcgen.ld.red support to sm103a arch by
[@drisspg](https://github.com/drisspg)in[#2696](https://github.com/Dao-AILab/flash-attention/pull/2696) - [CuTe, Bwd] Fix backward compile key churn due to pickling, max_seqlen is a tensor by
[@michaelxu-msft](https://github.com/michaelxu-msft)in[#2507](https://github.com/Dao-AILab/flash-attention/pull/2507) - hopper/setup.py: harden tarfile extraction against path traversal and symlink escape by
[@aryanputta](https://github.com/aryanputta)in[#2702](https://github.com/Dao-AILab/flash-attention/pull/2702) - Enable 2CTA for SM100 block-sparse backward by
[@drisspg](https://github.com/drisspg)in[#2661](https://github.com/Dao-AILab/flash-attention/pull/2661)

## New Contributors

[@michaelxu-msft](https://github.com/michaelxu-msft)made their first contribution in[#2507](https://github.com/Dao-AILab/flash-attention/pull/2507)

**Full Changelog**: `fa4-v4.0.0.beta21...fa4-v4.0.0.beta22`