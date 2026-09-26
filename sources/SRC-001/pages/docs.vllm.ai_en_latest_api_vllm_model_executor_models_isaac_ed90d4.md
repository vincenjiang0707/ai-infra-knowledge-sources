source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/isaac/
lastmod: 2026-09-24

#

`vllm.model_executor.models.isaac`

[¶](https://docs.vllm.ai#vllm.model_executor.models.isaac)

Classes:

-
–[IsaacForConditionalGeneration](https://docs.vllm.ai#vllm.model_executor.models.isaac.IsaacForConditionalGeneration) -
–[IsaacImagePixelInputs](https://docs.vllm.ai#vllm.model_executor.models.isaac.IsaacImagePixelInputs)Schema for validating Isaac image inputs.

-
–[Siglip2VisionTransformer](https://docs.vllm.ai#vllm.model_executor.models.isaac.Siglip2VisionTransformer)

Functions:

-
–[create_cumulative_seq_lengths](https://docs.vllm.ai#vllm.model_executor.models.isaac.create_cumulative_seq_lengths)Create cumulative sequence lengths for variable-length attention.

-
–[create_pixel_shuffle_index_map](https://docs.vllm.ai#vllm.model_executor.models.isaac.create_pixel_shuffle_index_map)Build a gather-index map that tells us, for every

*output*token after -
–[pixel_shuffle_varlen](https://docs.vllm.ai#vllm.model_executor.models.isaac.pixel_shuffle_varlen)Apply pixel shuffle to a packed vision sequence without unpacking per image.


##

`IsaacForConditionalGeneration`

[¶](https://docs.vllm.ai#vllm.model_executor.models.isaac.IsaacForConditionalGeneration)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

, [SupportsMultiModal](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsMultiModal)

, [SupportsLoRA](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsLoRA)

, [SupportsPP](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsPP)[SupportsMRoPE](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsMRoPE)

Methods:

-
–[get_mm_mapping](https://docs.vllm.ai#vllm.model_executor.models.isaac.IsaacForConditionalGeneration.get_mm_mapping)Get the module prefix in multimodal models.


## Source code in `vllm/model_executor/models/isaac.py`


|
|

###

`get_mm_mapping()`

[¶](https://docs.vllm.ai#vllm.model_executor.models.isaac.IsaacForConditionalGeneration.get_mm_mapping)

Get the module prefix in multimodal models.

## Source code in `vllm/model_executor/models/isaac.py`


##

`IsaacImagePixelInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.isaac.IsaacImagePixelInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Schema for validating Isaac image inputs.

## Dimensions

- np: Number of patches
- d: Patch dimension
- ni: Number of images

## The schema enforces

- pixel_values must be 2D: (num_patches, patch_dim)
- image_grid_thw must be 2D: (num_images, 3) where 3 represents [T, H, W]

## Source code in `vllm/model_executor/models/isaac.py`


##

`Siglip2VisionTransformer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.isaac.Siglip2VisionTransformer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.isaac.Siglip2VisionTransformer.forward)spatial_shapes (

`torch.LongTensor`

of shape`(batch_size, 2)`

):

## Source code in `vllm/model_executor/models/isaac.py`


###

`forward(packed_seq_patches)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.isaac.Siglip2VisionTransformer.forward)

spatial_shapes (`torch.LongTensor`

of shape `(batch_size, 2)`

): Tensor containing the spatial dimensions (height, width) of the input images.

## Source code in `vllm/model_executor/models/isaac.py`


##

`create_cumulative_seq_lengths(seq_sizes, device)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.isaac.create_cumulative_seq_lengths)

Create cumulative sequence lengths for variable-length attention.

## Source code in `vllm/model_executor/models/isaac.py`


##

`create_pixel_shuffle_index_map(seq_sizes, token_grids, scale_factor=1, device=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.isaac.create_pixel_shuffle_index_map)

Build a gather-index map that tells us, for every *output* token after pixel-shuffle, which `scale_factor**2`

*input* tokens are being merged.

#### Args:[¶](https://docs.vllm.ai#vllm.model_executor.models.isaac.create_pixel_shuffle_index_map--args)

seq_sizes : (num_images,) - #patches in each image (row-major order) token_grids : (num_images,2) - (height, width) for every image scale_factor : spatial down-scale factor (≥2) device : (optional) overrides `seq_sizes.device`


#### Returns:[¶](https://docs.vllm.ai#vllm.model_executor.models.isaac.create_pixel_shuffle_index_map--returns)

gather_idx : (new_total_seq_len, scale_factor* 2) int64 tensor. gather_idx[i, j] is the flat* index into the

*original*packed sequence for the j-th sub-patch that forms the i-th output token.

## Source code in `vllm/model_executor/models/isaac.py`


##

`pixel_shuffle_varlen(x, token_grids, scale_factor=1)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.isaac.pixel_shuffle_varlen)

Apply pixel shuffle to a packed vision sequence without unpacking per image.

Parameters:

-

(`x`

[¶](https://docs.vllm.ai#vllm.model_executor.models.isaac.pixel_shuffle_varlen(x))``torch.Tensor``

) –Concatenated vision embeddings. Accepts

`(seq_len, hidden_size)`

or`(1, seq_len, hidden_size)`

shapes produced by stacking image patches. -

(`token_grids`

[¶](https://docs.vllm.ai#vllm.model_executor.models.isaac.pixel_shuffle_varlen(token_grids))``torch.Tensor``

) –Integer tensor of shape

`(num_images, 2)`

whose rows give the`(height, width)`

patch grid sizes corresponding to each image segment inside`x`

. -

(`scale_factor`

[¶](https://docs.vllm.ai#vllm.model_executor.models.isaac.pixel_shuffle_varlen(scale_factor))``int`, *optional*, defaults to 1`

, default:`1`

) –Spatial down-sampling factor specific to pixel shuffle. Values greater than one merge

`scale_factor**2`

neighboring patches into a single embedding channel-group.

Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`torch.Tensor`

: Pixel-shuffled embeddings with shape matching the input -
(`convention`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`(seq_len, hidden_size * scale_factor**2)`

when the input -

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)was 2D, or

`(1, seq_len, hidden_size * scale_factor**2)`

if the -

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)singleton batch dimension was present.


Raises:

-

–[ValueError](https://docs.python.org/3/builtins/exceptions.html#ValueError)If more than one batch item is provided.