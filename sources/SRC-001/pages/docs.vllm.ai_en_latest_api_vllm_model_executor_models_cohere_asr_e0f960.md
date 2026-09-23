source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/cohere_asr/
lastmod: 2026-09-23

#

`vllm.model_executor.models.cohere_asr`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr)

Classes:

-
–[CausalConv1D](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.CausalConv1D)A causal version of nn.Conv1d where each step would

-
–[CohereASRMultiHeadAttention](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.CohereASRMultiHeadAttention)Multi-Head Attention layer of Transformer.

-
–[ConformerConvolution](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.ConformerConvolution)The convolution module for the Conformer model.

-
–[ConformerEncoder](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.ConformerEncoder)The encoder for ASR model of Conformer.

-
–[ConformerFeedForward](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.ConformerFeedForward)feed-forward module of Conformer model.

-
–[ConformerLayer](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.ConformerLayer)A single block of the Conformer encoder.

-
–[ConvSubsampling](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.ConvSubsampling) -
–[FixedPositionalEncoding](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.FixedPositionalEncoding)Fixed positional encoding (embedding layer) from sine and cosine functions

-
–[MaskedConvSequential](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.MaskedConvSequential) -
–[PositionalEncoding](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.PositionalEncoding)Fixed sinusoidal positional encoding.

-
–[RelPositionMultiHeadAttention](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.RelPositionMultiHeadAttention)Multi-Head Attention layer of Transformer-XL with

-
–[RelPositionalEncoding](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.RelPositionalEncoding)Relative positional encoding for TransformerXL's layers

-
–[Swish](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.Swish)Swish activation function introduced in 'https://arxiv.org/abs/1710.05941'


##

`CausalConv1D`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.CausalConv1D)

Bases: [Conv1d](https://pytorch.org/docs/stable/generated/torch.nn.Conv1d.html#torch.nn.Conv1d)

A causal version of nn.Conv1d where each step would have limited access to locations on its right or left. All arguments are the same as nn.Conv1d except padding.

If padding is set None, then paddings are set automatically to make it a causal convolution where each location would not see any steps on its right.

If padding is set as a list (size of 2), then padding[0] would be used as left padding and padding[1] as right padding. It would make it possible to control the number of steps to be accessible on the right and left. This mode is not supported when stride > 1. padding[0]+padding[1] should be equal to (kernel_size - 1).

## Source code in `vllm/model_executor/models/cohere_asr.py`


##

`CohereASRMultiHeadAttention`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.CohereASRMultiHeadAttention)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Multi-Head Attention layer of Transformer.

Parameters:

-

(`n_head`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.CohereASRMultiHeadAttention(n_head))

) –[int](https://docs.python.org/3/builtins/functions.html#int)number of heads

-

(`n_feat`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.CohereASRMultiHeadAttention(n_feat))

) –[int](https://docs.python.org/3/builtins/functions.html#int)size of the features

-

(`use_bias`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.CohereASRMultiHeadAttention(use_bias))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –whether to remove bias in linear and conv layers


Methods:

-
–[__init__](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.CohereASRMultiHeadAttention.__init__)Construct an MultiHeadedAttention object.

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.CohereASRMultiHeadAttention.forward)Compute 'Scaled Dot Product Attention'.

-
–[forward_attention](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.CohereASRMultiHeadAttention.forward_attention)Compute attention context vector.

-
–[forward_qkv](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.CohereASRMultiHeadAttention.forward_qkv)Transforms query, key and value.


## Source code in `vllm/model_executor/models/cohere_asr.py`


|
|

###

`__init__(n_head, n_feat, use_bias=True)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.CohereASRMultiHeadAttention.__init__)

Construct an MultiHeadedAttention object.

## Source code in `vllm/model_executor/models/cohere_asr.py`


###

`forward(query, key, value, mask, pos_emb=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.CohereASRMultiHeadAttention.forward)

Compute 'Scaled Dot Product Attention'.

Parameters:

-

(`query`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.CohereASRMultiHeadAttention.forward(query))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(batch, time1, size)

-

(`key`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.CohereASRMultiHeadAttention.forward(key))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(batch, time2, size)

-

(`value`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.CohereASRMultiHeadAttention.forward(value))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(batch, time2, size)

-

(`mask`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.CohereASRMultiHeadAttention.forward(mask))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(batch, time1, time2)

-

(`pos_emb`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.CohereASRMultiHeadAttention.forward(pos_emb))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`None`

) –optional relative position embeddings


Returns:

-
(`output`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)transformed

`value`

(batch, time1, d_model) weighted by the query dot key attention

## Source code in `vllm/model_executor/models/cohere_asr.py`


###

`forward_attention(value, scores, mask)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.CohereASRMultiHeadAttention.forward_attention)

Compute attention context vector.

Parameters:

-

(`value`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.CohereASRMultiHeadAttention.forward_attention(value))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(batch, time2, size)

-

(`scores`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.CohereASRMultiHeadAttention.forward_attention(scores))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(batch, time1, time2)

-

(`mask`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.CohereASRMultiHeadAttention.forward_attention(mask))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(batch, time1, time2)


returns: value (torch.Tensor): transformed `value`

(batch, time2, d_model) weighted by the attention scores

## Source code in `vllm/model_executor/models/cohere_asr.py`


###

`forward_qkv(query, key, value)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.CohereASRMultiHeadAttention.forward_qkv)

Transforms query, key and value.

Parameters:

-

(`query`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.CohereASRMultiHeadAttention.forward_qkv(query))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(batch, time1, size)

-

(`key`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.CohereASRMultiHeadAttention.forward_qkv(key))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(batch, time2, size)

-

(`value`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.CohereASRMultiHeadAttention.forward_qkv(value))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(batch, time2, size)


returns: q (torch.Tensor): (batch, head, time1, size) k (torch.Tensor): (batch, head, time2, size) v (torch.Tensor): (batch, head, time2, size)

## Source code in `vllm/model_executor/models/cohere_asr.py`


##

`ConformerConvolution`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.ConformerConvolution)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

The convolution module for the Conformer model.

Parameters:

-

(`d_model`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.ConformerConvolution(d_model))

) –[int](https://docs.python.org/3/builtins/functions.html#int)hidden dimension

-

(`kernel_size`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.ConformerConvolution(kernel_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)kernel size for depthwise convolution

-

(`pointwise_activation`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.ConformerConvolution(pointwise_activation))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'glu_'`

) –name of the activation function to be used for the pointwise conv. Note that Conformer uses a special key

`glu_`

which is treated as the original default from the paper. -

(`use_bias`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.ConformerConvolution(use_bias))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –Use bias in all Linear and Conv1d layers to improve activation flow and stabilize training of huge models. Defaults to True


## Source code in `vllm/model_executor/models/cohere_asr.py`


|
|

##

`ConformerEncoder`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.ConformerEncoder)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

The encoder for ASR model of Conformer. Based on this paper: 'Conformer: Convolution-augmented Transformer for Speech Recognition' by Anmol Gulati et al. https://arxiv.org/abs/2005.08100

Methods:

-
–[set_max_audio_length](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.ConformerEncoder.set_max_audio_length)Sets maximum input length.


## Source code in `vllm/model_executor/models/cohere_asr.py`


|
|

###

`set_max_audio_length(max_audio_length)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.ConformerEncoder.set_max_audio_length)

Sets maximum input length. Pre-calculates internal seq_range mask.

Parameters:

## Source code in `vllm/model_executor/models/cohere_asr.py`


##

`ConformerFeedForward`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.ConformerFeedForward)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

feed-forward module of Conformer model. use_bias (bool): Apply bias to all Linear and Conv1d layers to improve activation flow and stabilize training of huge models.

## Source code in `vllm/model_executor/models/cohere_asr.py`


##

`ConformerLayer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.ConformerLayer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

A single block of the Conformer encoder.

Parameters:

-

(`d_model`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.ConformerLayer(d_model))

) –[int](https://docs.python.org/3/builtins/functions.html#int)input dimension of MultiheadAttentionMechanism and PositionwiseFeedForward

-

(`d_ff`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.ConformerLayer(d_ff))

) –[int](https://docs.python.org/3/builtins/functions.html#int)hidden dimension of PositionwiseFeedForward

-

(`self_attention_model`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.ConformerLayer(self_attention_model))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'rel_pos'`

) –type of the attention layer and positional encoding

-

(`n_heads`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.ConformerLayer(n_heads))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`4`

) –number of heads for multi-head attention

-

(`conv_kernel_size`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.ConformerLayer(conv_kernel_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`31`

) –kernel size for depthwise convolution in convolution module

-

(`use_bias`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.ConformerLayer(use_bias))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –Apply bias to all Linear and Conv1d layers from each ConformerLayer to improve activation flow and stabilize training of huge models. Defaults to True.


Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.ConformerLayer.forward)Args:


## Source code in `vllm/model_executor/models/cohere_asr.py`


|
|

###

`forward(x, att_mask=None, pos_emb=None, pad_mask=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.ConformerLayer.forward)

Parameters:

-

(`x`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.ConformerLayer.forward(x))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)input signals (B, T, d_model)

-

(`att_mask`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.ConformerLayer.forward(att_mask))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`None`

) –attention masks(B, T, T)

-

(`pos_emb`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.ConformerLayer.forward(pos_emb))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`None`

) –(L, 1, d_model)

-

(`pad_mask`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.ConformerLayer.forward(pad_mask))

, default:[tensor](https://pytorch.org/docs/stable/generated/torch.tensor.html#torch.tensor)`None`

) –padding mask


Returns: x (torch.Tensor): (B, T, d_model)

## Source code in `vllm/model_executor/models/cohere_asr.py`


##

`ConvSubsampling`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.ConvSubsampling)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[calc_length](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.ConvSubsampling.calc_length)Calculates the output length of a Tensor passed


## Source code in `vllm/model_executor/models/cohere_asr.py`


|
|

###

`calc_length(lengths, all_paddings, kernel_size, stride, ceil_mode, repeat_num=1)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.ConvSubsampling.calc_length)

Calculates the output length of a Tensor passed through a convolution or max pooling layer

## Source code in `vllm/model_executor/models/cohere_asr.py`


##

`FixedPositionalEncoding`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.FixedPositionalEncoding)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Fixed positional encoding (embedding layer) from sine and cosine functions of different frequencies according to https://arxiv.org/abs/1706.03762

Parameters:

-

(`hidden_size`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.FixedPositionalEncoding(hidden_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)size of the embeddings in the model, also known as d_model

-

(`max_sequence_length`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.FixedPositionalEncoding(max_sequence_length))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`512`

) –maximum allowed length of the input sequence


## Source code in `vllm/model_executor/models/cohere_asr.py`


###

`_build_pos_enc(hidden_size, max_sequence_length)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.FixedPositionalEncoding._build_pos_enc)

Builds/replaces pre-computed positional encoding.

## Source code in `vllm/model_executor/models/cohere_asr.py`


##

`MaskedConvSequential`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.MaskedConvSequential)

Bases: [Sequential](https://pytorch.org/docs/stable/generated/torch.nn.Sequential.html#torch.nn.Sequential)

Methods:

-
–[apply_channel_mask](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.MaskedConvSequential.apply_channel_mask)Apply mask in-place via broadcasting.

-
–[calculate_conv_output_size](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.MaskedConvSequential.calculate_conv_output_size)Calculate exact output size after convolution.


## Source code in `vllm/model_executor/models/cohere_asr.py`


###

`_create_mask(tensor, lengths)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.MaskedConvSequential._create_mask)

Create broadcastable mask from per-sample lengths.

Returns a (B, 1, T, 1) mask that broadcasts over channels and features without materializing a full (B, C, T, F) tensor.

## Source code in `vllm/model_executor/models/cohere_asr.py`


###

`apply_channel_mask(tensor, mask)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.MaskedConvSequential.apply_channel_mask)

Apply mask in-place via broadcasting.

tensor: (B, C, T, F), mask: (B, 1, T, 1)

###

`calculate_conv_output_size(input_size, kernel_size, stride, padding)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.MaskedConvSequential.calculate_conv_output_size)

Calculate exact output size after convolution.

## Source code in `vllm/model_executor/models/cohere_asr.py`


##

`PositionalEncoding`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.PositionalEncoding)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Fixed sinusoidal positional encoding.

Parameters:

-

(`d_model`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.PositionalEncoding(d_model))

) –[int](https://docs.python.org/3/builtins/functions.html#int)embedding dim

-

(`max_len`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.PositionalEncoding(max_len))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`5000`

) –maximum input length

-

(`xscale`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.PositionalEncoding(xscale))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`None`

) –whether to scale the input by sqrt(d_model)


Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.PositionalEncoding.forward)Adds positional encoding.


## Source code in `vllm/model_executor/models/cohere_asr.py`


###

`forward(x, cache_len=0)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.PositionalEncoding.forward)

Adds positional encoding.

Parameters:

-

(`x`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.PositionalEncoding.forward(x))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input. Its shape is (batch, time, feature_size)

-

(`cache_len`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.PositionalEncoding.forward(cache_len))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –the size of the cache which is used to shift positions


Returns: x+pos_emb (torch.Tensor): Its shape is (batch, time, feature_size) pos_emb (torch.Tensor): Its shape is (1, time, feature_size)

## Source code in `vllm/model_executor/models/cohere_asr.py`


##

`RelPositionMultiHeadAttention`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.RelPositionMultiHeadAttention)

Bases: [CohereASRMultiHeadAttention](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.CohereASRMultiHeadAttention)

Multi-Head Attention layer of Transformer-XL with support of relative positional encoding. Paper: https://arxiv.org/abs/1901.02860 Args: n_head (int): number of heads n_feat (int): size of the features use_bias (bool): whether to apply bias in linear and conv layers of MultiHeadAttention

Methods:

-
–[__init__](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.RelPositionMultiHeadAttention.__init__)Construct an RelPositionMultiHeadedAttention object.

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.RelPositionMultiHeadAttention.forward)Compute 'Scaled Dot Product Attention' with rel. positional encoding.

-
–[rel_shift](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.RelPositionMultiHeadAttention.rel_shift)Compute relative positional encoding.


## Source code in `vllm/model_executor/models/cohere_asr.py`


|
|

###

`__init__(n_head, n_feat, pos_bias_u, pos_bias_v, use_bias=True)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.RelPositionMultiHeadAttention.__init__)

Construct an RelPositionMultiHeadedAttention object.

## Source code in `vllm/model_executor/models/cohere_asr.py`


###

`forward(query, key, value, mask, pos_emb=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.RelPositionMultiHeadAttention.forward)

Compute 'Scaled Dot Product Attention' with rel. positional encoding.

Parameters:

-

(`query`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.RelPositionMultiHeadAttention.forward(query))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(batch, time1, size)

-

(`key`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.RelPositionMultiHeadAttention.forward(key))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(batch, time2, size)

-

(`value`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.RelPositionMultiHeadAttention.forward(value))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(batch, time2, size)

-

(`mask`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.RelPositionMultiHeadAttention.forward(mask))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(batch, time1, time2)

-

(`pos_emb`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.RelPositionMultiHeadAttention.forward(pos_emb))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`None`

) –(batch, time1, size)


Returns:

-
(`output`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)transformed

`value`

(batch, time1, d_model) weighted by the query dot key attention

## Source code in `vllm/model_executor/models/cohere_asr.py`


###

`rel_shift(x)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.RelPositionMultiHeadAttention.rel_shift)

Compute relative positional encoding.

Parameters:

## Source code in `vllm/model_executor/models/cohere_asr.py`


##

`RelPositionalEncoding`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.RelPositionalEncoding)

Bases: [PositionalEncoding](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.PositionalEncoding)

Relative positional encoding for TransformerXL's layers See : Appendix B in https://arxiv.org/abs/1901.02860 Args: d_model (int): embedding dim max_len (int): maximum input length xscale (bool): whether to scale the input by sqrt(d_model)

Methods:

-
–[extend_pe](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.RelPositionalEncoding.extend_pe)Reset and extend the positional encodings if needed.

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.RelPositionalEncoding.forward)Compute positional encoding.


## Source code in `vllm/model_executor/models/cohere_asr.py`


###

`extend_pe(length, device, dtype)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.RelPositionalEncoding.extend_pe)

Reset and extend the positional encodings if needed.

## Source code in `vllm/model_executor/models/cohere_asr.py`


###

`forward(x, cache_len=0)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.RelPositionalEncoding.forward)

Compute positional encoding.

Parameters:

-

(`x`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.RelPositionalEncoding.forward(x))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input. Its shape is (batch, time, feature_size)

-

(`cache_len`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere_asr.RelPositionalEncoding.forward(cache_len))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –the size of the cache which is used to shift positions


Returns: x (torch.Tensor): Its shape is (batch, time, feature_size) pos_emb (torch.Tensor): Its shape is (1, time, feature_size)