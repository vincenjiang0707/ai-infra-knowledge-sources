source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/idefics2_vision_model/
lastmod: 2026-09-24

#

`vllm.model_executor.models.idefics2_vision_model`

[¶](https://docs.vllm.ai#vllm.model_executor.models.idefics2_vision_model)

PyTorch Idefics2 model.

Classes:

-
–[Idefics2Encoder](https://docs.vllm.ai#vllm.model_executor.models.idefics2_vision_model.Idefics2Encoder)Transformer encoder consisting of

`config.num_hidden_layers`

self attention -
–[Idefics2EncoderLayer](https://docs.vllm.ai#vllm.model_executor.models.idefics2_vision_model.Idefics2EncoderLayer) -
–[Idefics2VisionAttention](https://docs.vllm.ai#vllm.model_executor.models.idefics2_vision_model.Idefics2VisionAttention)Multi-headed attention from 'Attention Is All You Need' paper.

-
–[Idefics2VisionEmbeddings](https://docs.vllm.ai#vllm.model_executor.models.idefics2_vision_model.Idefics2VisionEmbeddings)This is a modified version of `siglip.modelign_siglip.SiglipVisionEmbeddings


##

`Idefics2Encoder`

[¶](https://docs.vllm.ai#vllm.model_executor.models.idefics2_vision_model.Idefics2Encoder)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Transformer encoder consisting of `config.num_hidden_layers`

self attention layers. Each layer is a [`Idefics2EncoderLayer`

].

Parameters:

-

(`config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.idefics2_vision_model.Idefics2Encoder(config))`Idefics2Config`

) –Idefics2Config


Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.idefics2_vision_model.Idefics2Encoder.forward)Args:


## Source code in `vllm/model_executor/models/idefics2_vision_model.py`


###

`forward(inputs_embeds, attention_mask=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.idefics2_vision_model.Idefics2Encoder.forward)

inputs_embeds (torch.Tensor): Optionally, instead of passing `input_ids`

you can choose to directly pass an embedded representation. This is useful if you want more control over how to convert `input_ids`

indices into associated vectorsthan the model's internal embedding lookup matrix.

## Source code in `vllm/model_executor/models/idefics2_vision_model.py`


##

`Idefics2EncoderLayer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.idefics2_vision_model.Idefics2EncoderLayer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.idefics2_vision_model.Idefics2EncoderLayer.forward)Args:


## Source code in `vllm/model_executor/models/idefics2_vision_model.py`


###

`forward(hidden_states, attention_mask=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.idefics2_vision_model.Idefics2EncoderLayer.forward)

hidden_states (`torch.FloatTensor`

): Input to the layer of shape `(batch, seq_len, embed_dim)`

.

## Source code in `vllm/model_executor/models/idefics2_vision_model.py`


##

`Idefics2VisionAttention`

[¶](https://docs.vllm.ai#vllm.model_executor.models.idefics2_vision_model.Idefics2VisionAttention)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Multi-headed attention from 'Attention Is All You Need' paper.

## Source code in `vllm/model_executor/models/idefics2_vision_model.py`


|
|

##

`Idefics2VisionEmbeddings`

[¶](https://docs.vllm.ai#vllm.model_executor.models.idefics2_vision_model.Idefics2VisionEmbeddings)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

This is a modified version of `siglip.modelign_siglip.SiglipVisionEmbeddings`

to enable images of variable resolution.

The modifications are adapted from [Patch n' Pack: NaViT, a Vision Transformer for any Aspect Ratio and Resolution](https://arxiv.org/abs/2307.06304) which allows treating images in their native aspect ratio and without the need to resize them to the same fixed size. In particular, we start from the original pre-trained SigLIP model(which uses images of fixed-size square images) and adapt it by training on images of variable resolutions.

## Source code in `vllm/model_executor/models/idefics2_vision_model.py`


|
|