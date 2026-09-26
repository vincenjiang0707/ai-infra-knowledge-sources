source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/lfm2_siglip2/
lastmod: 2026-09-24

#

`vllm.model_executor.models.lfm2_siglip2`

[¶](https://docs.vllm.ai#vllm.model_executor.models.lfm2_siglip2)

Implementation of Siglip2VisionModel intended to be only used within a vision language model.

Classes:

-
–[Siglip2Attention](https://docs.vllm.ai#vllm.model_executor.models.lfm2_siglip2.Siglip2Attention)Multi-headed attention from 'Attention Is All You Need' paper.

-
–[Siglip2Encoder](https://docs.vllm.ai#vllm.model_executor.models.lfm2_siglip2.Siglip2Encoder)Transformer encoder consisting of

`config.num_hidden_layers`

-
–[Siglip2EncoderLayer](https://docs.vllm.ai#vllm.model_executor.models.lfm2_siglip2.Siglip2EncoderLayer) -
–[Siglip2Model](https://docs.vllm.ai#vllm.model_executor.models.lfm2_siglip2.Siglip2Model) -
–[Siglip2VisionEmbeddings](https://docs.vllm.ai#vllm.model_executor.models.lfm2_siglip2.Siglip2VisionEmbeddings) -
–[Siglip2VisionTransformer](https://docs.vllm.ai#vllm.model_executor.models.lfm2_siglip2.Siglip2VisionTransformer)

##

`Siglip2Attention`

[¶](https://docs.vllm.ai#vllm.model_executor.models.lfm2_siglip2.Siglip2Attention)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Multi-headed attention from 'Attention Is All You Need' paper.

## Source code in `vllm/model_executor/models/lfm2_siglip2.py`


|
|

##

`Siglip2Encoder`

[¶](https://docs.vllm.ai#vllm.model_executor.models.lfm2_siglip2.Siglip2Encoder)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Transformer encoder consisting of `config.num_hidden_layers`

self attention layers. Each layer is a [`Siglip2EncoderLayer`

].

Parameters:

-

(`config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.lfm2_siglip2.Siglip2Encoder(config))`Siglip2VisionConfig`

) –PreTrainedConfig


## Source code in `vllm/model_executor/models/lfm2_siglip2.py`


##

`Siglip2EncoderLayer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.lfm2_siglip2.Siglip2EncoderLayer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.lfm2_siglip2.Siglip2EncoderLayer.forward)Args:


## Source code in `vllm/model_executor/models/lfm2_siglip2.py`


###

`forward(hidden_states, cu_seqlens, max_seqlen)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.lfm2_siglip2.Siglip2EncoderLayer.forward)

Args: hidden_states: Input tensor of shape (batch, seq_len, embed_dim). cu_seqlens: Cumulative sequence lengths tensor. max_seqlen: Maximum sequence length.

## Source code in `vllm/model_executor/models/lfm2_siglip2.py`


##

`Siglip2Model`

[¶](https://docs.vllm.ai#vllm.model_executor.models.lfm2_siglip2.Siglip2Model)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.lfm2_siglip2.Siglip2Model.forward)Forward pass through the vision model.


## Source code in `vllm/model_executor/models/lfm2_siglip2.py`


|
|

###

`forward(pixel_values_packed, spatial_shapes, cu_seqlens, max_seqlen, select_layers=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.lfm2_siglip2.Siglip2Model.forward)

Forward pass through the vision model.

Parameters:

-

(`pixel_values_packed`

[¶](https://docs.vllm.ai#vllm.model_executor.models.lfm2_siglip2.Siglip2Model.forward(pixel_values_packed))`FloatTensor`

) –Packed pixel values for all images.

-

(`spatial_shapes`

[¶](https://docs.vllm.ai#vllm.model_executor.models.lfm2_siglip2.Siglip2Model.forward(spatial_shapes))`LongTensor`

) –Per-image spatial dimensions.

-

(`cu_seqlens`

[¶](https://docs.vllm.ai#vllm.model_executor.models.lfm2_siglip2.Siglip2Model.forward(cu_seqlens))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Cumulative sequence lengths of the packed images.

-

(`max_seqlen`

[¶](https://docs.vllm.ai#vllm.model_executor.models.lfm2_siglip2.Siglip2Model.forward(max_seqlen))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Longest image sequence in the batch.

-

(`select_layers`

[¶](https://docs.vllm.ai#vllm.model_executor.models.lfm2_siglip2.Siglip2Model.forward(select_layers))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | None`None`

) –Layer indices to select hidden states from. Supports negative indices (e.g., [-2] for second-to-last). If None, returns the last layer output with post_layernorm. Multiple layers can be selected and will be concatenated.


## Source code in `vllm/model_executor/models/lfm2_siglip2.py`


##

`Siglip2VisionEmbeddings`

[¶](https://docs.vllm.ai#vllm.model_executor.models.lfm2_siglip2.Siglip2VisionEmbeddings)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.lfm2_siglip2.Siglip2VisionEmbeddings.forward)Embed patchified pixel values in packed (unpadded) form.

-
–[resize_positional_embeddings_packed](https://docs.vllm.ai#vllm.model_executor.models.lfm2_siglip2.Siglip2VisionEmbeddings.resize_positional_embeddings_packed)Resize positional embeddings per image and return a packed tensor.


## Source code in `vllm/model_executor/models/lfm2_siglip2.py`


|
|

###

`forward(pixel_values_packed, spatial_shapes)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.lfm2_siglip2.Siglip2VisionEmbeddings.forward)

Embed patchified pixel values in packed (unpadded) form.

Parameters:

-

(`pixel_values_packed`

[¶](https://docs.vllm.ai#vllm.model_executor.models.lfm2_siglip2.Siglip2VisionEmbeddings.forward(pixel_values_packed))`FloatTensor`

) –(1, total_tokens, patch_dim) or (total_tokens, patch_dim), packed in tile order.

-

(`spatial_shapes`

[¶](https://docs.vllm.ai#vllm.model_executor.models.lfm2_siglip2.Siglip2VisionEmbeddings.forward(spatial_shapes))`LongTensor`

) –(num_tiles, 2) on CPU (height, width) per tile.


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(1, total_tokens, embed_dim) packed embeddings.


## Source code in `vllm/model_executor/models/lfm2_siglip2.py`


###

`resize_positional_embeddings_packed(positional_embeddings, spatial_shapes, lengths_list)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.lfm2_siglip2.Siglip2VisionEmbeddings.resize_positional_embeddings_packed)

Resize positional embeddings per image and return a packed tensor.

Parameters:

-

(`positional_embeddings`

[¶](https://docs.vllm.ai#vllm.model_executor.models.lfm2_siglip2.Siglip2VisionEmbeddings.resize_positional_embeddings_packed(positional_embeddings))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(height, width, embed_dim) base grid.

-

(`spatial_shapes`

[¶](https://docs.vllm.ai#vllm.model_executor.models.lfm2_siglip2.Siglip2VisionEmbeddings.resize_positional_embeddings_packed(spatial_shapes))`LongTensor`

) –(batch_size, 2) on CPU, (height, width) per image.

-

(`lengths_list`

[¶](https://docs.vllm.ai#vllm.model_executor.models.lfm2_siglip2.Siglip2VisionEmbeddings.resize_positional_embeddings_packed(lengths_list))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]flattened token length per image (height * width).


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(total_tokens, embed_dim) packed positional embeddings, concatenated

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)in the same order as

`lengths_list`

.

## Source code in `vllm/model_executor/models/lfm2_siglip2.py`


##

`Siglip2VisionTransformer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.lfm2_siglip2.Siglip2VisionTransformer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.lfm2_siglip2.Siglip2VisionTransformer.forward)spatial_shapes (

`torch.LongTensor`

of shape`(batch_size, 2)`

):

## Source code in `vllm/model_executor/models/lfm2_siglip2.py`


###

`forward(pixel_values_packed, spatial_shapes, cu_seqlens, max_seqlen, select_layers=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.lfm2_siglip2.Siglip2VisionTransformer.forward)

spatial_shapes (`torch.LongTensor`

of shape `(batch_size, 2)`

): Tensor containing the spatial dimensions (height, width) of the input images. select_layers (`list[int]`

or `None`

, defaults to `None`

): Layer indices to select hidden states from. Supports negative indices (e.g., -1 for last layer, -2 for second-to-last). If None, returns the last layer output.