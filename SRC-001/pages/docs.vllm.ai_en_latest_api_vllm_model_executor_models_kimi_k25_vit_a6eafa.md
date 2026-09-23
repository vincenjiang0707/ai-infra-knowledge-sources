source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/kimi_k25_vit/
lastmod: 2026-09-23

#

`vllm.model_executor.models.kimi_k25_vit`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit)

Vision tower implementation for Kimi-K2.5 model.

This module provides the vision encoder components for Kimi-K2.5, including 3D patch embedding, RoPE position embedding, and temporal pooling for video chunks.

Classes:

-
–[KimiK25MultiModalProjector](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.KimiK25MultiModalProjector)Multi-modal projector with patch merging for Kimi-K2.5.

-
–[Learnable2DInterpPosEmbDivided_fixed](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.Learnable2DInterpPosEmbDivided_fixed)2D learnable position embedding with temporal extension.

-
–[MLP2](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.MLP2)Two-layer MLP with tensor parallel support.

-
–[MoonViT3dEncoder](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.MoonViT3dEncoder)Full encoder stack for MoonViT 3D.

-
–[MoonViT3dPretrainedModel](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.MoonViT3dPretrainedModel)Main vision tower model.

-
–[MoonViTEncoderLayer](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.MoonViTEncoderLayer)Single encoder layer for MoonViT with TP/DP support.

-
–[MoonVision3dPatchEmbed](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.MoonVision3dPatchEmbed)3D patch embedding for vision tower.

-
–[Rope2DPosEmbRepeated](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.Rope2DPosEmbRepeated)2D rotary position embedding with multi-resolution support.


Functions:

-
–[build_image_merge_gather_idx](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.build_image_merge_gather_idx)Build packed spatial-merge indices for image-only CUDA graphs.

-
–[get_1d_sincos_pos_embed](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.get_1d_sincos_pos_embed)Generate 1D sincos positional embedding.

-
–[get_1d_sincos_pos_embed_from_grid](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.get_1d_sincos_pos_embed_from_grid)Generate 1D sincos positional embedding from grid positions.

-
–[mm_projector_forward](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.mm_projector_forward)Apply MM projector to vision tower outputs.

-
–[tpool_patch_merger](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.tpool_patch_merger)Temporal pooling patch merger.

-
–[tpool_patch_merger_packed](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.tpool_patch_merger_packed)Apply the image-only spatial merge using precomputed tensor indices.

-
–[vision_tower_forward](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.vision_tower_forward)DP-sharded vision tower forward with mrope.


##

`KimiK25MultiModalProjector`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.KimiK25MultiModalProjector)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Multi-modal projector with patch merging for Kimi-K2.5.

## Source code in `vllm/model_executor/models/kimi_k25_vit.py`


##

`Learnable2DInterpPosEmbDivided_fixed`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.Learnable2DInterpPosEmbDivided_fixed)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

2D learnable position embedding with temporal extension.

## Source code in `vllm/model_executor/models/kimi_k25_vit.py`


##

`MLP2`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.MLP2)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Two-layer MLP with tensor parallel support.

## Source code in `vllm/model_executor/models/kimi_k25_vit.py`


##

`MoonViT3dEncoder`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.MoonViT3dEncoder)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Full encoder stack for MoonViT 3D.

## Source code in `vllm/model_executor/models/kimi_k25_vit.py`


|
|

##

`MoonViT3dPretrainedModel`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.MoonViT3dPretrainedModel)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Main vision tower model.

Uses KimiK25VisionConfig directly from transformers_utils/configs/kimi_k25.py.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.MoonViT3dPretrainedModel.forward)Args:

-
–[prepare_encoder_cudagraph_metadata](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.MoonViT3dPretrainedModel.prepare_encoder_cudagraph_metadata)Precompute fixed-buffer metadata for image encoder CUDA graphs.


## Source code in `vllm/model_executor/models/kimi_k25_vit.py`


|
|

###

`forward(pixel_values, grid_thws, *, encoder_metadata=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.MoonViT3dPretrainedModel.forward)

Parameters:

-

(`pixel_values`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.MoonViT3dPretrainedModel.forward(pixel_values))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The input pixel values.

-

(`grid_thws`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.MoonViT3dPretrainedModel.forward(grid_thws))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Temporal, height and width.


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)torch.Tensor: The output tokens.


## Source code in `vllm/model_executor/models/kimi_k25_vit.py`


###

`prepare_encoder_cudagraph_metadata(grid_thw_list, *, max_batch_size, max_seqlen_override=None, device)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.MoonViT3dPretrainedModel.prepare_encoder_cudagraph_metadata)

Precompute fixed-buffer metadata for image encoder CUDA graphs.

## Source code in `vllm/model_executor/models/kimi_k25_vit.py`


##

`MoonViTEncoderLayer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.MoonViTEncoderLayer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Single encoder layer for MoonViT with TP/DP support.

Methods:

-
–[attention_qkvpacked](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.MoonViTEncoderLayer.attention_qkvpacked)Compute self-attention with packed QKV.


## Source code in `vllm/model_executor/models/kimi_k25_vit.py`


|
|

###

`attention_qkvpacked(x, cu_seqlens, rope_freqs_cis, max_seqlen=None, sequence_lengths=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.MoonViTEncoderLayer.attention_qkvpacked)

Compute self-attention with packed QKV.

Parameters:

-

(`x`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.MoonViTEncoderLayer.attention_qkvpacked(x))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(seqlen, hidden_dim)

-

(`cu_seqlens`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.MoonViTEncoderLayer.attention_qkvpacked(cu_seqlens))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)cumulative sequence lengths

-

(`rope_freqs_cis`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.MoonViTEncoderLayer.attention_qkvpacked(rope_freqs_cis))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)rotary embedding frequencies

-

(`max_seqlen`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.MoonViTEncoderLayer.attention_qkvpacked(max_seqlen))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –longest sequence in the batch

-

(`sequence_lengths`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.MoonViTEncoderLayer.attention_qkvpacked(sequence_lengths))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –per-sequence lengths


## Source code in `vllm/model_executor/models/kimi_k25_vit.py`


##

`MoonVision3dPatchEmbed`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.MoonVision3dPatchEmbed)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

3D patch embedding for vision tower.

## Source code in `vllm/model_executor/models/kimi_k25_vit.py`


##

`Rope2DPosEmbRepeated`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.Rope2DPosEmbRepeated)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

2D rotary position embedding with multi-resolution support.

Methods:

-
–[get_freqs_cis](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.Rope2DPosEmbRepeated.get_freqs_cis)Args:


## Source code in `vllm/model_executor/models/kimi_k25_vit.py`


###

`_precompute_freqs_cis(device)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.Rope2DPosEmbRepeated._precompute_freqs_cis)

Calculate the cis(freqs) for each position in the 2D grid.

## Source code in `vllm/model_executor/models/kimi_k25_vit.py`


###

`get_freqs_cis(grid_thws, device)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.Rope2DPosEmbRepeated.get_freqs_cis)

Parameters:

Returns:

-
(`freqs_cis`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)tensor of shape (sum(t * height * width), dim//2)


## Source code in `vllm/model_executor/models/kimi_k25_vit.py`


##

`build_image_merge_gather_idx(grid_thws, merge_kernel_size)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.build_image_merge_gather_idx)

Build packed spatial-merge indices for image-only CUDA graphs.

## Source code in `vllm/model_executor/models/kimi_k25_vit.py`


##

`get_1d_sincos_pos_embed(embed_dim, t_size, cls_token=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.get_1d_sincos_pos_embed)

Generate 1D sincos positional embedding.

## Source code in `vllm/model_executor/models/kimi_k25_vit.py`


##

`get_1d_sincos_pos_embed_from_grid(embed_dim, pos)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.get_1d_sincos_pos_embed_from_grid)

Generate 1D sincos positional embedding from grid positions.

## Source code in `vllm/model_executor/models/kimi_k25_vit.py`


##

`mm_projector_forward(mm_projector, vt_output)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.mm_projector_forward)

Apply MM projector to vision tower outputs.

## Source code in `vllm/model_executor/models/kimi_k25_vit.py`


##

`tpool_patch_merger(x, grid_thws, merge_kernel_size=(2, 2))`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.tpool_patch_merger)

Temporal pooling patch merger.

## Source code in `vllm/model_executor/models/kimi_k25_vit.py`


##

`tpool_patch_merger_packed(x, merge_gather_idx)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.tpool_patch_merger_packed)

Apply the image-only spatial merge using precomputed tensor indices.

##

`vision_tower_forward(vision_tower, pixel_values, grid_thw, mm_projector, use_data_parallel)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.kimi_k25_vit.vision_tower_forward)

DP-sharded vision tower forward with mrope.

Uses vLLM's standard data parallelism utility to shard the batch across available GPUs, enabling parallel processing of vision features.