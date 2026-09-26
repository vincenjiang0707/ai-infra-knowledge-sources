source: https://docs.vllm.ai/en/latest/api/vllm/models/dots3_note/nvidia/vision/
lastmod: 2026-09-24

#

`vllm.models.dots3_note.nvidia.vision`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.vision)

Classes:

-
–[MoESwiGLUFFN](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.vision.MoESwiGLUFFN)MoE FFN with per-expert SwiGLU experts, sigmoid/softmax gating, top-k routing.

-
–[MoESwiGLUFFNFP8](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.vision.MoESwiGLUFFNFP8)NOTE vision MoE using the checkpoint's local block-FP8 semantics.

-
–[PatchMergerAdapter](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.vision.PatchMergerAdapter)Cybertron

`PatchMerger`

(`pool_kind='patch_merger', proj_kind='identity'`

). -
–[PixelShuffleAdapter](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.vision.PixelShuffleAdapter)Legacy adapter: NHWC pixel-shuffle spatial merge + LayerNorm + 2-layer MLP.


##

`MoESwiGLUFFN`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.vision.MoESwiGLUFFN)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

MoE FFN with per-expert SwiGLU experts, sigmoid/softmax gating, top-k routing.

## Source code in `vllm/models/dots3_note/nvidia/vision.py`


|
|

##

`MoESwiGLUFFNFP8`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.vision.MoESwiGLUFFNFP8)

Bases: [MoESwiGLUFFN](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.vision.MoESwiGLUFFN)

NOTE vision MoE using the checkpoint's local block-FP8 semantics.

## Source code in `vllm/models/dots3_note/nvidia/vision.py`


##

`PatchMergerAdapter`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.vision.PatchMergerAdapter)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Cybertron `PatchMerger`

(`pool_kind='patch_merger', proj_kind='identity'`

).

Assumes the encoder output is already laid out in `merge_size`

x`merge_size`

groups (qwen `pre_pixel_shuffle`

preprocessor + RoPE grouped accordingly), so merging is a simple `view(-1, merge**2 * in_dim)`

of consecutive tokens. State-dict layout matches cybertron's `PatchMerger`

(`ln_q`

over the per-token dim, `mlp.0`

/ `mlp.2`

Linear).

## Source code in `vllm/models/dots3_note/nvidia/vision.py`


##

`PixelShuffleAdapter`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.vision.PixelShuffleAdapter)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Legacy adapter: NHWC pixel-shuffle spatial merge + LayerNorm + 2-layer MLP.

Mirrors `cybertron`

`FCAdapter(pool_kind='pixel_shuffle', proj_kind='mlp2x_ln_gelu')`

. State-dict keys: `proj.0`

(LayerNorm of in_dim*merge**2), `proj.1`

/ `proj.3`

(Linear).