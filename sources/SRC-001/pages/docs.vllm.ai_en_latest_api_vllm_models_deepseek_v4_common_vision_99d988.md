source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v4/common/vision/
lastmod: 2026-09-23

#

`vllm.models.deepseek_v4.common.vision`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.vision)

DeepSeek-V4 vision tower (ViT + aligner) with TP-sharded linears.

Ported from the official reference implementation (deepseek-ai/DeepSeek-V4-Flash-Vision-Exp). Weight names match the HF checkpoint so no renaming is needed at load time. Attention and MLP weights are tensor-parallel sharded (replicated when the vision head count is not divisible by TP size, or under `--mm-encoder-tp-mode data`

); the patch embed and norms are replicated, so the residual stream is full-width on every rank.

Classes:

-
–[DeepseekV4Aligner](https://docs.vllm.ai#vllm.models.deepseek_v4.common.vision.DeepseekV4Aligner)Spatial merge (downsample_ratio x downsample_ratio) + MLP projector.

-
–[DeepseekV4ViT](https://docs.vllm.ai#vllm.models.deepseek_v4.common.vision.DeepseekV4ViT)DeepSeek-V4 ViT: full bidirectional attention per image, 2D RoPE.


Functions:

-
–[build_packed_merge_metadata](https://docs.vllm.ai#vllm.models.deepseek_v4.common.vision.build_packed_merge_metadata)Gather indices/mask for

`DeepseekV4Aligner.forward_packed`

. -
–[build_packed_vit_metadata](https://docs.vllm.ai#vllm.models.deepseek_v4.common.vision.build_packed_vit_metadata)Precompute packed-batch ViT metadata for

`DeepseekV4ViT.forward_packed`

. -
–[run_dp_sharded_vision_tower](https://docs.vllm.ai#vllm.models.deepseek_v4.common.vision.run_dp_sharded_vision_tower)Run the ViT + aligner with images sharded across TP ranks.


##

`DeepseekV4Aligner`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.vision.DeepseekV4Aligner)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Spatial merge (downsample_ratio x downsample_ratio) + MLP projector.

Methods:

-
–[forward_packed](https://docs.vllm.ai#vllm.models.deepseek_v4.common.vision.DeepseekV4Aligner.forward_packed)Packed multi-image path for encoder CUDA graphs.


## Source code in `vllm/models/deepseek_v4/common/vision.py`


###

`forward_packed(x, merge_idx, merge_mask)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.vision.DeepseekV4Aligner.forward_packed)

Packed multi-image path for encoder CUDA graphs.

`merge_idx`

/`merge_mask`

come from `build_packed_merge_metadata`

; gather+mask reproduces the eager `F.pad`

+ `F.unfold`

merge exactly (unfold rows are channel-major, so the gathered patch rows are transposed before flattening).

## Source code in `vllm/models/deepseek_v4/common/vision.py`


##

`DeepseekV4ViT`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.vision.DeepseekV4ViT)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

DeepSeek-V4 ViT: full bidirectional attention per image, 2D RoPE.

Methods:

-
–[forward_packed](https://docs.vllm.ai#vllm.models.deepseek_v4.common.vision.DeepseekV4ViT.forward_packed)Varlen path for encoder CUDA graphs: multiple images packed along


## Source code in `vllm/models/deepseek_v4/common/vision.py`


###

`forward_packed(patches, cos, sin, cu_seqlens, max_seqlen)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.vision.DeepseekV4ViT.forward_packed)

Varlen path for encoder CUDA graphs: multiple images packed along rows, per-image attention via `cu_seqlens`

, RoPE tables precomputed on device. Pure-tensor (no host reads, no H2D), safe to capture.

## Source code in `vllm/models/deepseek_v4/common/vision.py`


##

`build_packed_merge_metadata(grids, downsample_ratio, *, device, dtype)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.vision.build_packed_merge_metadata)

Gather indices/mask for `DeepseekV4Aligner.forward_packed`

.

For each aligner output row, the `r x r`

source patch rows in the packed ViT output; positions past the image edge (the eager path pads them with zeros) get mask 0 and a clamped in-range index.

## Source code in `vllm/models/deepseek_v4/common/vision.py`


##

`build_packed_vit_metadata(grids, *, rope_dim, rope_theta, device, max_seqlen_override=None, cached=True)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.vision.build_packed_vit_metadata)

Precompute packed-batch ViT metadata for `DeepseekV4ViT.forward_packed`

.

Parameters:

-

(`grids`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.vision.build_packed_vit_metadata(grids))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]] |[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int)]]`[n_vit_h, n_vit_w]`

per image, in packing order. -

(`rope_dim`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.vision.build_packed_vit_metadata(rope_dim))

) –[int](https://docs.python.org/3/builtins/functions.html#int)RoPE embedding dimension of the ViT.

-

(`rope_theta`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.vision.build_packed_vit_metadata(rope_theta))

) –[float](https://docs.python.org/3/builtins/functions.html#float)RoPE base frequency of the ViT.

-

(`device`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.vision.build_packed_vit_metadata(device))

) –[device](https://pytorch.org/docs/stable/tensor_attributes.html#torch.device)Device for the returned tensors (except

`max_seqlen`

, which stays on the host). -

(`max_seqlen_override`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.vision.build_packed_vit_metadata(max_seqlen_override))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –Worst-case value baked in at CUDA graph capture (the attention wrapper reads

`max_seqlen`

on the host, so the capture-time value becomes a graph constant). -

(`cached`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.vision.build_packed_vit_metadata(cached))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –Use the shared

`lru_cache`

for RoPE tables. Capture-time dummy grids pass`False`

to avoid evicting real entries.

## Source code in `vllm/models/deepseek_v4/common/vision.py`


##

`run_dp_sharded_vision_tower(vision_model, aligner, patches, vit_grid)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.vision.run_dp_sharded_vision_tower)

Run the ViT + aligner with images sharded across TP ranks.

Every rank holds the full tower weights (`--mm-encoder-tp-mode data`

) and receives the full `patches`

batch. Images are assigned to ranks by patch count (greedy load balancing), each rank encodes only its share, and per-image embeddings are exchanged with one padded all-gather and returned in the original image order.

Parameters:

-

(`vision_model`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.vision.run_dp_sharded_vision_tower(vision_model))

) –[DeepseekV4ViT](https://docs.vllm.ai#vllm.models.deepseek_v4.common.vision.DeepseekV4ViT)The (weight-replicated) ViT tower.

-

(`aligner`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.vision.run_dp_sharded_vision_tower(aligner))

) –[DeepseekV4Aligner](https://docs.vllm.ai#vllm.models.deepseek_v4.common.vision.DeepseekV4Aligner)The (weight-replicated) spatial-merge projector.

-

(`patches`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.vision.run_dp_sharded_vision_tower(patches))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`(sum(n_vit_h * n_vit_w), 3, p, p)`

patches of all images. -

(`vit_grid`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.vision.run_dp_sharded_vision_tower(vit_grid))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]]`[n_vit_h, n_vit_w]`

per image.

Returns:

## Source code in `vllm/models/deepseek_v4/common/vision.py`


|
|