source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/moonvit/
lastmod: 2026-09-24

#

`vllm.model_executor.models.moonvit`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit)

Classes:

-
–[Learnable2DInterpPosEmb](https://docs.vllm.ai#vllm.model_executor.models.moonvit.Learnable2DInterpPosEmb) -
–[MLP2](https://docs.vllm.ai#vllm.model_executor.models.moonvit.MLP2)Args:

-
–[MoonVisionPatchEmbed](https://docs.vllm.ai#vllm.model_executor.models.moonvit.MoonVisionPatchEmbed) -
–[MoonVitEncoderLayer](https://docs.vllm.ai#vllm.model_executor.models.moonvit.MoonVitEncoderLayer) -
–[MoonVitPretrainedModel](https://docs.vllm.ai#vllm.model_executor.models.moonvit.MoonVitPretrainedModel) -
–[Rope2DPosEmb](https://docs.vllm.ai#vllm.model_executor.models.moonvit.Rope2DPosEmb)2D rotary position embedding with multi-resolution support.


Functions:

-
–[apply_rope](https://docs.vllm.ai#vllm.model_executor.models.moonvit.apply_rope)Args: (The leading dimensions of all inputs should be the same)

-
–[patch_merger_packed](https://docs.vllm.ai#vllm.model_executor.models.moonvit.patch_merger_packed)CUDA-graph-safe equivalent of :func:

`patch_merger`

.

##

`Learnable2DInterpPosEmb`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.Learnable2DInterpPosEmb)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[get_pos_embeds](https://docs.vllm.ai#vllm.model_executor.models.moonvit.Learnable2DInterpPosEmb.get_pos_embeds)Build packed per-token positional embeddings for a list of grids.


## Source code in `vllm/model_executor/models/moonvit.py`


###

`get_pos_embeds(grid_hws_list)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.Learnable2DInterpPosEmb.get_pos_embeds)

Build packed per-token positional embeddings for a list of grids.

Returns a tensor of shape `(sum(h * w), dim)`

formed by interpolating the learned `(height, width, dim)`

weight to each `(h, w)`

grid and concatenating the flattened results in the same order as `grid_hws_list`

. Lives outside the captured CUDA graph so the per-grid Python iteration is safe.

## Source code in `vllm/model_executor/models/moonvit.py`


##

`MLP2`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.MLP2)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Args: dims: [in_dim, hidden_dim, out_dim] bias: whether to use bias in linear layer.

## Source code in `vllm/model_executor/models/moonvit.py`


##

`MoonVisionPatchEmbed`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.MoonVisionPatchEmbed)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.moonvit.MoonVisionPatchEmbed.forward)Args:


## Source code in `vllm/model_executor/models/moonvit.py`


###

`forward(x, grid_hw=None, *, pos_embeds=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.MoonVisionPatchEmbed.forward)

Parameters:

-

(`x`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.MoonVisionPatchEmbed.forward(x))`(L, Channels)`

) –input tensor

-

(`grid_hw`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.MoonVisionPatchEmbed.forward(grid_hw))`(N, 2)`

, default:`None`

) –grid height and width

-

(`pos_embeds`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.MoonVisionPatchEmbed.forward(pos_embeds))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –precomputed positional embeddings of shape

`(L, Cout)`

. When provided,`grid_hw`

is unused and the CUDA-graph-incompatible interpolation in`self.pos_emb`

is skipped.

Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(L, Cout) tensor


## Source code in `vllm/model_executor/models/moonvit.py`


##

`MoonVitEncoderLayer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.MoonVitEncoderLayer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[attention_qkvpacked](https://docs.vllm.ai#vllm.model_executor.models.moonvit.MoonVitEncoderLayer.attention_qkvpacked)Args:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.moonvit.MoonVitEncoderLayer.forward)Args:


## Source code in `vllm/model_executor/models/moonvit.py`


|
|

###

`attention_qkvpacked(x, cu_seqlens, rope_freqs_cis=None, max_seqlen=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.MoonVitEncoderLayer.attention_qkvpacked)

Args: x (torch.Tensor): (seqlen, hidden_dim) cu_seqlens (torch.Tensor): max_seqlen: Optional precomputed scalar tensor. When omitted it is derived from `cu_seqlens`

, which produces a GPU scalar that breaks CUDA graph capture.

## Source code in `vllm/model_executor/models/moonvit.py`


###

`forward(hidden_states, cu_seqlens, rope_freqs_cis=None, max_seqlen=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.MoonVitEncoderLayer.forward)

Parameters:

-

(`hidden_states`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.MoonVitEncoderLayer.forward(hidden_states))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)non-packed (B, N, D) or packed (L, D). if non-packed, seqlens should be None, if packed, seqlens should be set

-

(`max_seqlen`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.MoonVitEncoderLayer.forward(max_seqlen))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –optional precomputed max-sequence-length scalar.


Returns:

-
(`output`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)same shape of input, non-packed (B, N, D) for non-packed input, (L, D) for packed input


## Source code in `vllm/model_executor/models/moonvit.py`


##

`MoonVitPretrainedModel`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.MoonVitPretrainedModel)

Bases: `PreTrainedModel`


Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.moonvit.MoonVitPretrainedModel.forward)Args:

-
–[prepare_encoder_metadata](https://docs.vllm.ai#vllm.model_executor.models.moonvit.MoonVitPretrainedModel.prepare_encoder_metadata)Precompute every grid-dependent input the encoder needs.


## Source code in `vllm/model_executor/models/moonvit.py`


|
|

###

`forward(pixel_values, grid_hw, *, encoder_metadata=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.MoonVitPretrainedModel.forward)

Args: pixel_values (torch.Tensor): The input pixel values. grid_hw (torch.Tensor): The grid height and width. encoder_metadata: Optional precomputed metadata produced by :meth:`prepare_encoder_metadata`

. When provided every `.tolist()`

call in the forward path is skipped, the returned tensor is the packed `(sum(new_h*new_w), kh*kw, hidden_size)`

form (suitable for CUDA graph capture/replay), and `grid_hw`

is unused. When `None`

the legacy path runs and returns a list of per-image tensors.

## Source code in `vllm/model_executor/models/moonvit.py`


###

`prepare_encoder_metadata(grid_hws_list, *, max_batch_size=None, max_seqlen_override=None, device=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.MoonVitPretrainedModel.prepare_encoder_metadata)

Precompute every grid-dependent input the encoder needs.

Used by the CUDA graph capture and replay paths to precompute every grid-dependent input outside the captured graph, so per-grid Python iteration and `.tolist()`

round-trips are fine; the values are then copied into fixed-shape buffers for replay.

Parameters:

-

(`grid_hws_list`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.MoonVitPretrainedModel.prepare_encoder_metadata(grid_hws_list))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]] |[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int)]]List of

`(h, w)`

patch-grid sizes per image. -

(`max_batch_size`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.MoonVitPretrainedModel.prepare_encoder_metadata(max_batch_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –When set,

`cu_seqlens`

is right-padded with its last value so the buffer covers up to this many sequences. Required at CUDA graph capture/replay so the buffer shape matches what was recorded; padding entries are zero-length sequences and are ignored by varlen attention. -

(`max_seqlen_override`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.MoonVitPretrainedModel.prepare_encoder_metadata(max_seqlen_override))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –Override the per-replay max sequence length scalar. At capture this must be a safe upper bound (worst case: a single image consuming the full token budget) because the value is baked into the captured graph.

-

(`device`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.MoonVitPretrainedModel.prepare_encoder_metadata(device))

, default:[device](https://pytorch.org/docs/stable/tensor_attributes.html#torch.device)| None`None`

) –Device for the metadata tensors. Defaults to the model's parameter device.


## Source code in `vllm/model_executor/models/moonvit.py`


|
|

##

`Rope2DPosEmb`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.Rope2DPosEmb)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

2D rotary position embedding with multi-resolution support.

This class is intended to be used in the following way: 1. Before training, create an instance of Rope2DPosEmb. This instance will hold the precomputed cis. 2. Before each forward pass, call `get_freqs_cis_by_*`

to get the `freqs_cis`

tensor for this iteration. 3. During the forward pass, pass the `freqs_cis`

tensor to each attention layer, and call `apply`

just before each attention operation. The rope is shared across all attention layers and all heads.

Refs: - RoFormer: https://arxiv.org/abs/2104.09864 - VisionLLaMA: https://arxiv.org/abs/2403.00522 - https://github.com/Meituan-AutoML/VisionLLaMA/blob/main/dit/models.py

Parameters:

-

(`dim`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.Rope2DPosEmb(dim))

) –[int](https://docs.python.org/3/builtins/functions.html#int)usually the multi-head attention dimension, should be divisible by 4 (TODO: relax this constraint if needed)

-

(`max_height`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.Rope2DPosEmb(max_height))

) –[int](https://docs.python.org/3/builtins/functions.html#int)the maximum height of the 2D grid

-

(`max_width`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.Rope2DPosEmb(max_width))

) –[int](https://docs.python.org/3/builtins/functions.html#int)the maximum width of the 2D grid

-

(`theta_base`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.Rope2DPosEmb(theta_base))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)`10000`

) –the base of the theta

-

(`device`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.Rope2DPosEmb(device))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`device_type`

) –the device to store the precomputed cis


Methods:

-
–[get_freqs_cis_by_idx](https://docs.vllm.ai#vllm.model_executor.models.moonvit.Rope2DPosEmb.get_freqs_cis_by_idx)Args:

-
–[get_freqs_cis_by_seqlens](https://docs.vllm.ai#vllm.model_executor.models.moonvit.Rope2DPosEmb.get_freqs_cis_by_seqlens)Args:

-
–[get_freqs_cis_by_seqlens_list](https://docs.vllm.ai#vllm.model_executor.models.moonvit.Rope2DPosEmb.get_freqs_cis_by_seqlens_list)List-based variant of :meth:

`get_freqs_cis_by_seqlens`

.

Attributes:

-
([precomputed_freqs_cis](https://docs.vllm.ai#vllm.model_executor.models.moonvit.Rope2DPosEmb.precomputed_freqs_cis)

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Calculate the cis(freqs) for each position in the 2D grid.


## Source code in `vllm/model_executor/models/moonvit.py`


|
|

###

`precomputed_freqs_cis`

`cached`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.Rope2DPosEmb.precomputed_freqs_cis)

Calculate the cis(freqs) for each position in the 2D grid.

## complex tensor of shape (max_height, max_width, dim//2) and value:

height axis: ret[h, w, 2*i] = cis(h * theta_base**(-4*i/dim)) weight axis: ret[h, w, 2*i+1] = cis(w * theta_base**(-4*i/dim)) with (i in [0, dim//4)) note: `cis`

is a mathematical notation defined by cis x = cos x + i sin x,

###

`get_freqs_cis_by_idx(pos_idx, pos_idx_mask)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.Rope2DPosEmb.get_freqs_cis_by_idx)

Parameters:

-

(`pos_idx`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.Rope2DPosEmb.get_freqs_cis_by_idx(pos_idx))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)tensor of shape (..., 2), It contains the (h, w) position indices of each 2D token.

-

(`pos_idx_mask`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.Rope2DPosEmb.get_freqs_cis_by_idx(pos_idx_mask))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)a mask of shape (...), the leading dimensions should be the same as pos_idx. Rope will only be applied to the tokens with True mask.

`freqs_cis`

for the tokens with False mask with be ones.

## Return

freqs_cis: tensor of shape (..., dim//2)

## Source code in `vllm/model_executor/models/moonvit.py`


###

`get_freqs_cis_by_seqlens(grid_hws)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.Rope2DPosEmb.get_freqs_cis_by_seqlens)

Parameters:

Returns:

-
(`freqs_cis`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)tensor of shape (sum(t * height * width), dim//2)


## Source code in `vllm/model_executor/models/moonvit.py`


###

`get_freqs_cis_by_seqlens_list(grid_hws_list)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.Rope2DPosEmb.get_freqs_cis_by_seqlens_list)

List-based variant of :meth:`get_freqs_cis_by_seqlens`

.

Accepts a Python list of `(h, w)`

pairs so callers that already operate outside the captured CUDA graph can avoid materializing a tensor + `.tolist()`

round-trip.

## Source code in `vllm/model_executor/models/moonvit.py`


##

`_build_merge_gather_idx(grid_hws_list, merge_kernel_size)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit._build_merge_gather_idx)

Build the per-token gather indices used by :func:`patch_merger_packed`

.

For each item with grid (h, w) and merge kernel (kh, kw), the output block at position (nh, nw) gathers the kh*kw input tokens at rows (nh*kh + ih, nw*kw + iw) of that item, in (ih, iw) row-major order.

## Source code in `vllm/model_executor/models/moonvit.py`


##

`apply_rope(xq, xk, freqs_cis)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.apply_rope)

(The leading dimensions of all inputs should be the same)

-

(`xq`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.apply_rope(xq))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)query, tensor of shape (..., num_heads, head_dim)

-

(`xk`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.apply_rope(xk))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)key, tensor of shape (..., num_heads, head_dim)

-

(`freqs_cis`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.apply_rope(freqs_cis))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)tensor of shape (..., head_dim/2), dtype=torch.complex64. It contains the precomputed cis(freqs) for each position in the 2D grid.


Returns:

## Source code in `vllm/model_executor/models/moonvit.py`


##

`patch_merger_packed(x, gather_idx, merge_kernel_size)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.moonvit.patch_merger_packed)

CUDA-graph-safe equivalent of :func:`patch_merger`

.

Uses a precomputed index tensor to gather the per-token reshape + permute that `patch_merger`

does inside a Python loop. The output is the concatenated 3D tensor `(sum(new_h * new_w), kh * kw, d_model)`

, matching what `torch.cat(patch_merger(...))`

would produce.