source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/nemotron_parse/
lastmod: 2026-09-23

#

`vllm.model_executor.models.nemotron_parse`

[¶](https://docs.vllm.ai#vllm.model_executor.models.nemotron_parse)

Classes:

-
–[BartDecoderLayer](https://docs.vllm.ai#vllm.model_executor.models.nemotron_parse.BartDecoderLayer) -
–[BartScaledWordEmbedding](https://docs.vllm.ai#vllm.model_executor.models.nemotron_parse.BartScaledWordEmbedding)This module overrides VocabParallelEmbedding's

-
–[MBartDecoderNoPos](https://docs.vllm.ai#vllm.model_executor.models.nemotron_parse.MBartDecoderNoPos)Transformer decoder consisting of

*config.decoder_layers*layers. -
–[NemotronParseForConditionalGeneration](https://docs.vllm.ai#vllm.model_executor.models.nemotron_parse.NemotronParseForConditionalGeneration) -
–[NemotronParsePixelInputs](https://docs.vllm.ai#vllm.model_executor.models.nemotron_parse.NemotronParsePixelInputs)Dimensions:

-
–[RadioWithNeck](https://docs.vllm.ai#vllm.model_executor.models.nemotron_parse.RadioWithNeck)Vision encoder using RADIO model with custom neck.


##

`BartDecoderLayer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.nemotron_parse.BartDecoderLayer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.nemotron_parse.BartDecoderLayer.forward)Args:


Attributes:

-
–[self_attn_layer_norm](https://docs.vllm.ai#vllm.model_executor.models.nemotron_parse.BartDecoderLayer.self_attn_layer_norm)afeldman-nm: personally I would call this "cross-attention",


## Source code in `vllm/model_executor/models/nemotron_parse.py`


|
|

###

`self_attn_layer_norm = nn.LayerNorm(self.embed_dim)`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.nemotron_parse.BartDecoderLayer.self_attn_layer_norm)

afeldman-nm: personally I would call this "cross-attention", however I left the name as "encoder_attn" to maintain consistency with the name of the pretrained weights.

###

`forward(decoder_hidden_states, encoder_hidden_states=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.nemotron_parse.BartDecoderLayer.forward)

Parameters:

-

(`decoder_hidden_states`

[¶](https://docs.vllm.ai#vllm.model_executor.models.nemotron_parse.BartDecoderLayer.forward(decoder_hidden_states))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)torch.Tensor of

*decoder*input embeddings. -

(`encoder_hidden_states`

[¶](https://docs.vllm.ai#vllm.model_executor.models.nemotron_parse.BartDecoderLayer.forward(encoder_hidden_states))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –torch.Tensor of

*encoder*input embeddings.

Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Decoder layer output torch.Tensor


## Source code in `vllm/model_executor/models/nemotron_parse.py`


##

`BartScaledWordEmbedding`

[¶](https://docs.vllm.ai#vllm.model_executor.models.nemotron_parse.BartScaledWordEmbedding)

Bases: [VocabParallelEmbedding](https://docs.vllm.ai/layers/vocab_parallel_embedding/#vllm.model_executor.layers.vocab_parallel_embedding.VocabParallelEmbedding)

This module overrides VocabParallelEmbedding's forward by multiplying with embeddings scale.

## Source code in `vllm/model_executor/models/nemotron_parse.py`


##

`MBartDecoderNoPos`

[¶](https://docs.vllm.ai#vllm.model_executor.models.nemotron_parse.MBartDecoderNoPos)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Transformer decoder consisting of *config.decoder_layers* layers. Each layer is a [`BartDecoderLayer`

]

Parameters:

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.nemotron_parse.MBartDecoderNoPos.forward)Args:


## Source code in `vllm/model_executor/models/nemotron_parse.py`


|
|

###

`forward(decoder_input_ids, *, encoder_hidden_states, inputs_embeds=None, **kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.nemotron_parse.MBartDecoderNoPos.forward)

Parameters:

-

(`decoder_input_ids`

[¶](https://docs.vllm.ai#vllm.model_executor.models.nemotron_parse.MBartDecoderNoPos.forward(decoder_input_ids))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| NoneIndices of

*decoder*input sequence tokens in the vocabulary. Padding will be ignored by default should you provide it. -

(`encoder_hidden_states`

[¶](https://docs.vllm.ai#vllm.model_executor.models.nemotron_parse.MBartDecoderNoPos.forward(encoder_hidden_states))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| NoneTensor of encoder output embeddings


Returns: Decoder output torch.Tensor

## Source code in `vllm/model_executor/models/nemotron_parse.py`


##

`NemotronParseForConditionalGeneration`

[¶](https://docs.vllm.ai#vllm.model_executor.models.nemotron_parse.NemotronParseForConditionalGeneration)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)[SupportsMultiModal](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsMultiModal)

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.nemotron_parse.NemotronParseForConditionalGeneration.forward)Args:


## Source code in `vllm/model_executor/models/nemotron_parse.py`


|
|

###

`forward(input_ids, positions, encoder_outputs=None, **kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.nemotron_parse.NemotronParseForConditionalGeneration.forward)

Parameters:

-

(`input_ids`

[¶](https://docs.vllm.ai#vllm.model_executor.models.nemotron_parse.NemotronParseForConditionalGeneration.forward(input_ids))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| Nonetorch.Tensor of

*decoder*input token ids. -

(`positions`

[¶](https://docs.vllm.ai#vllm.model_executor.models.nemotron_parse.NemotronParseForConditionalGeneration.forward(positions))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)torch.Tensor of

*decoder*position indices. -

(`encoder_outputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.nemotron_parse.NemotronParseForConditionalGeneration.forward(encoder_outputs))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)] | None`None`

) –List of encoder output tensors (vision embeddings). During profiling, this may be None or empty.


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Output torch.Tensor


## Source code in `vllm/model_executor/models/nemotron_parse.py`


##

`NemotronParsePixelInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.nemotron_parse.NemotronParsePixelInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - b: Batch size - c: Number of channels (3) - h: Height - w: Width

## Source code in `vllm/model_executor/models/nemotron_parse.py`


##

`RadioWithNeck`

[¶](https://docs.vllm.ai#vllm.model_executor.models.nemotron_parse.RadioWithNeck)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Vision encoder using RADIO model with custom neck.

## Source code in `vllm/model_executor/models/nemotron_parse.py`


|
|