source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/siglip2navit/
lastmod: 2026-09-23

#

`vllm.model_executor.models.siglip2navit`

[¶](https://docs.vllm.ai#vllm.model_executor.models.siglip2navit)

Implementation of SiglipVisionModel intended to be only used within a vision language model.

Classes:

-
–[Siglip2Attention](https://docs.vllm.ai#vllm.model_executor.models.siglip2navit.Siglip2Attention)Multi-headed attention from 'Attention Is All You Need' paper.

-
–[Siglip2Encoder](https://docs.vllm.ai#vllm.model_executor.models.siglip2navit.Siglip2Encoder)Transformer encoder consisting of

`config.num_hidden_layers`

-
–[Siglip2EncoderLayer](https://docs.vllm.ai#vllm.model_executor.models.siglip2navit.Siglip2EncoderLayer) -
–[Siglip2VisionEmbeddings](https://docs.vllm.ai#vllm.model_executor.models.siglip2navit.Siglip2VisionEmbeddings) -
–[Siglip2VisionTransformer](https://docs.vllm.ai#vllm.model_executor.models.siglip2navit.Siglip2VisionTransformer)

##

`Siglip2Attention`

[¶](https://docs.vllm.ai#vllm.model_executor.models.siglip2navit.Siglip2Attention)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Multi-headed attention from 'Attention Is All You Need' paper.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.siglip2navit.Siglip2Attention.forward)Input shape: Batch x Time x Channel.


## Source code in `vllm/model_executor/models/siglip2navit.py`


|
|

###

`forward(hidden_states, cu_seqlens, position_embeddings=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.siglip2navit.Siglip2Attention.forward)

Input shape: Batch x Time x Channel.

## Source code in `vllm/model_executor/models/siglip2navit.py`


##

`Siglip2Encoder`

[¶](https://docs.vllm.ai#vllm.model_executor.models.siglip2navit.Siglip2Encoder)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Transformer encoder consisting of `config.num_hidden_layers`

self attention layers. Each layer is a [`Siglip2EncoderLayer`

].

Parameters:

-

(`config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.siglip2navit.Siglip2Encoder(config))`Siglip2VisionConfig`

) –PretrainedConfig


Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.siglip2navit.Siglip2Encoder.forward)Args:


## Source code in `vllm/model_executor/models/siglip2navit.py`


|
|

###

`forward(inputs_embeds, grid_thws)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.siglip2navit.Siglip2Encoder.forward)

inputs_embeds: Input tensor of shape (batch_size, sequence_length, hidden_size). Embedded representation of the input tokens. grid_thws: Grid tensor of shape (num_patches, 3) containing grid dimensions. Whether or not to return a [`~utils.ModelOutput`

] instead of a plain tuple.

## Source code in `vllm/model_executor/models/siglip2navit.py`


##

`Siglip2EncoderLayer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.siglip2navit.Siglip2EncoderLayer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.siglip2navit.Siglip2EncoderLayer.forward)Args:


## Source code in `vllm/model_executor/models/siglip2navit.py`


###

`forward(hidden_states, cu_seqlens, position_embeddings)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.siglip2navit.Siglip2EncoderLayer.forward)

Args: hidden_states: Input tensor of shape (batch, seq_len, embed_dim). cu_seqlens: Cumulative sequence lengths tensor. position_embeddings: Position embeddings tensor.

## Source code in `vllm/model_executor/models/siglip2navit.py`


##

`Siglip2VisionEmbeddings`

[¶](https://docs.vllm.ai#vllm.model_executor.models.siglip2navit.Siglip2VisionEmbeddings)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.siglip2navit.Siglip2VisionEmbeddings.forward)Args:


## Source code in `vllm/model_executor/models/siglip2navit.py`


|
|

###

`forward(pixel_values, grid_thws=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.siglip2navit.Siglip2VisionEmbeddings.forward)

pixel_values (`torch.FloatTensor`

): Pixel values of shape ( num_patches, num_channels * temporal_patch_size * patch_size * patch_size ) grid_thws: (`torch.LongTensor`

): grid shape (num_patches, 3)

## Source code in `vllm/model_executor/models/siglip2navit.py`


##

`Siglip2VisionTransformer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.siglip2navit.Siglip2VisionTransformer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.siglip2navit.Siglip2VisionTransformer.forward)spatial_shapes (

`torch.LongTensor`

of shape`(batch_size, 2)`

):

## Source code in `vllm/model_executor/models/siglip2navit.py`


###

`forward(pixel_values, grid_thws)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.siglip2navit.Siglip2VisionTransformer.forward)

spatial_shapes (`torch.LongTensor`

of shape `(batch_size, 2)`

): Tensor containing the spatial dimensions (height, width) of the input images.