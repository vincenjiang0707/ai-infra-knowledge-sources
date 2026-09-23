source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/phi4mm_audio/
lastmod: 2026-09-23

#

`vllm.model_executor.models.phi4mm_audio`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio)

Classes:

-
–[AudioEmbedding](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.AudioEmbedding)Image embedding.

-
–[ConformerEncoder](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoder)ConformerEncoder module.

-
–[ConformerEncoderLayer](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoderLayer)ConformerEncoder Layer module.

-
–[TransformerEncoderBase](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.TransformerEncoderBase)The Base class for Transformer based encoders.

-
–[WindowQformer](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.WindowQformer)Window-level Qformer.


##

`AudioEmbedding`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.AudioEmbedding)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Image embedding.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.AudioEmbedding.forward)arguments:

-
–[get_audio_features](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.AudioEmbedding.get_audio_features)arguments:


## Source code in `vllm/model_executor/models/phi4mm_audio.py`


|
|

###

`forward(audio_features, audio_attention_mask=None, audio_projection_mode='speech')`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.AudioEmbedding.forward)

Parameters:

Returns:

-
(`audio_embeds`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)audio embeddings (num_audio_tokens, hidden_dim)


## Source code in `vllm/model_executor/models/phi4mm_audio.py`


###

`get_audio_features(input_embeds, audio_attention_mask=None, audio_projection_mode='speech')`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.AudioEmbedding.get_audio_features)

arguments: input_embeds: audio features (B, T, D) B: num audios in a sequence

## Source code in `vllm/model_executor/models/phi4mm_audio.py`


##

`ConformerEncoder`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoder)

Bases: [TransformerEncoderBase](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.TransformerEncoderBase)

ConformerEncoder module. see original paper for more details: https://arxiv.org/abs/2005.08100

Please set causal = True in streaming model Args: input_size: int input feature dimension. chunk_size: int, list(int) Number of frames for each chunk This variable can take 2 forms: int: Used for inference, or single chunk size training list(int) : Used only for variable chunk size training Some examples for the 2 cases: chunk_size = 12 chunk_size = [6, 8, 12, 24] left_chunk: int, list(int) Number of chunks used for masking in streaming mode. This variable can take 2 forms: int: Used for inference, or single chunk size training list(int) : Used only for variable chunk size training. When chunk_size is a list, left_chunk must be a list with same length. Some examples for the 2 cases: left_chunk = 6 left_chunk = [12, 9, 6, 3] num_lang: int This parameter is used to store the number of languages in the lang_dict, only used for multiseed/multilingual models. default None. attention_dim: int, optional attention dimension. default 256. attention_heads: int, optional the number of heads. default 4 linear_units: the number of units of position-wise feed forward. default 2048 num_block: number of Transformer layer. default 6 dropout_rate: float, optional dropout rate. default 0.1 input_layer: str, optional input layer type before Conformer, one of ["linear", "conv2d", "custom", "vgg2l", "embed"], default "conv2d" causal: bool, optional if set to True, convolution have no access to future frames. default False. batch_norm: bool, optional if set to True, apply batchnorm before activation in ConvModule layer of the conformer. default False cnn_out: int, optional the number of CNN channels before Conformer. default -1. cnn_layer_norm: bool, optional layer norm between Conformer and the first CNN. default False. ext_pw_out_channel: int, optional the number of channel for CNN before depthwise_separable_CNN. If 0 then use linear. default 0. ext_pw_kernel_size: int, optional kernel size of N before depthwise_separable_CNN. only work for ext_pw_out_channel > 0. default 1 depthwise_seperable_out_channel: int, optional the number of channel for depthwise_separable_CNN. default 256. depthwise_multiplier: int, optional the number of multiplier for depthwise_separable_CNN. default 1. chunk_se: int, optional 0 for offline SE. 1 for streaming SE, where mean is computed by accumulated history until current chunk_se. 2 for streaming SE, where mean is computed by only the current chunk. default 0. kernel_size: int, optional the number of kernels for depthwise_separable_CNN. default 3. activation: str, optional FeedForward block activation. one of ["relu", "swish", "sigmoid"] default "relu". conv_activation: str, optional activation function used in ConvModule part of the conformer, default "relu". conv_glu_type: str, optional activation used use glu in depthwise_separable_CNN, default "sigmoid" bias_in_glu: bool, optional if set to True, use additive bias in the weight module before GLU. default True linear_glu_in_convm: bool, optional if set to True, use GLULinear module, otherwise, used GLUPointWiseConv module. default to False. attention_glu_type: str only work for glu_in_attention !=0 default "swish". export: bool, optional if set to True, it removes the padding from convolutional layers and allow the onnx conversion for inference. default False. activation_checkpointing: str, optional a dictionarry of {"module","interval","offload"}, where "module": str accept ["transformer", "attention"] to select which module should do activation checkpointing. "interval": int, default 1, interval of applying activation checkpointing, interval = 1 means that we apply checkpointing on every layer (if activation), otherwise, we apply it every x interval. "offload": bool, default False, if set to True, we offload activation to cpu and reload it during backward, otherwise, we recalculate activation in backward. default "". extra_layer_output_idx: int the layer index to be exposed. relative_attention_bias_args: dict, optional use more efficient scalar bias-based relative multihead attention (Q*K^T + B) implemented in cmb.basics.embedding. [T5/ALiBi]RelativeAttentionLogitBias usage: relative_attention_bias_args={"type": t5/alibi} additional method-specific arguments can be provided (see transformer_base.py) time_reduction: int optional time reduction factor default 4 use_pt_scaled_dot_product_attention: whether to use pytorch scaled dot product attention in training. Default: False nemo_conv_settings: dict, optional A dictionary of settings for NeMo Subsampling. default: None usage: nemo_conv_settings= { "subsampling": dw_striding/striding/dw_striding_conv1d/striding_conv1d, "conv_channels": int, "subsampling_conv_chunking_factor": int, "is_causal": True/False } conv2d_extra_padding: str, optional Add extra padding in conv2d subsampling layers. Choices are (feat, feat_time, none, True) Default: none replication_pad_for_subsample_embedding: For batched-streaming decoding, use "replication" padding for the cache at start of utterance. Default: False attention_group_size: int, optional the number of groups to use for attention, default 1 (Multi-Head Attention), 1 = typical Multi-Head Attention, 1 < attention_group_size < attention_heads = Grouped-Query Attention attention_group_size = attention_heads = Multi-Query Attention

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoder.forward)Conformer Forward function.


## Source code in `vllm/model_executor/models/phi4mm_audio.py`


|
|

###

`forward(xs_pad, masks)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoder.forward)

Conformer Forward function.

Parameters:

-

(`xs_pad`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoder.forward(xs_pad))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)torch.Tensor input tensor

-

(`masks`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoder.forward(masks))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)torch.Tensor post-embedding input lengths


## Source code in `vllm/model_executor/models/phi4mm_audio.py`


|
|

##

`ConformerEncoderLayer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoderLayer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

ConformerEncoder Layer module. for more details see conformer paper: https://arxiv.org/abs/2005.08100 This module implement the Conformer block layer.

Parameters:

-

(`d_model`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoderLayer(d_model))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`512`

) –int attention dim.

-

(`ext_pw_out_channel`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoderLayer(ext_pw_out_channel))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –int if > 0, ext_pw_out_channel is a dim channel size for the last pointwise conv after swish activation.

-

(`depthwise_seperable_out_channel`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoderLayer(depthwise_seperable_out_channel))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`256`

) –int if set different to 0, the number of depthwise_seperable_out_channel will be used as a channel_out of the second conv1d layer. otherwise, it equals to 0, the second conv1d layer is skipped.

-

(`depthwise_multiplier`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoderLayer(depthwise_multiplier))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`1`

) –int number of input_dim channels duplication. this value will be used to compute the hidden channels of the Conv1D.

-

(`n_head`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoderLayer(n_head))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`4`

) –int the number of heads for multihead attention module.

-

(`d_ffn`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoderLayer(d_ffn))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`2048`

) –int output size of the feed_forward blocks.

-

(`ext_pw_kernel_size`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoderLayer(ext_pw_kernel_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`1`

) –int kernel size of the conv pointwise of the conformer.

-

(`kernel_size`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoderLayer(kernel_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`3`

) –int kernel size.

-

(`dropout_rate`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoderLayer(dropout_rate))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)`0.1`

) –float dropout rate.

-

(`causal`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoderLayer(causal))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –bool, optional if set to True, convolution have no access to future frames. default False.

-

(`batch_norm`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoderLayer(batch_norm))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –bool, optional if set to True, apply batchnorm before activation in ConvModule layer of the conformer. default False

-

(`activation`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoderLayer(activation))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'relu'`

) –str, optional activation function name, one of ["relu", "swish", "sigmoid"], sigmoid activation is only used with "glu_in_fnn=True", default "relu".

-

(`chunk_se`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoderLayer(chunk_se))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –int, optional 0 for offline SE. 1 for streaming SE, where mean is computed by accumulated history until current chunk_se. 2 for streaming SE, where mean is computed by only the current chunk. default 0.

-

(`chunk_size`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoderLayer(chunk_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)|[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]`18`

) –int, optional chunk_size for cnn. default 18

-

(`conv_activation`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoderLayer(conv_activation))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'relu'`

) –str, optional activation function used in ConvModule part of the conformer, default "relu".

-

(`conv_glu_type`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoderLayer(conv_glu_type))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'sigmoid'`

) –str, optional activation function used for the glu inside the ConvModule part of the conformer. default: "sigmoid".

-

(`bias_in_glu`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoderLayer(bias_in_glu))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –bool, optional if set to True, use additive bias in the weight module before GLU.

-

(`linear_glu_in_convm`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoderLayer(linear_glu_in_convm))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –bool, optional if set to True, use GLULinear module, otherwise, used GLUPointWiseConv module. default to False.

-

(`attention_inner_dim`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoderLayer(attention_inner_dim))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`-1`

) –int, optional if equal to -1, attention dim for linears k/q/v is equal to d_model. otherwise attention_inner_dim is used. default -1.

-

(`attention_glu_type`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoderLayer(attention_glu_type))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'swish'`

) –str, optional activation function for glu used in the multihead attention, default "swish".

-

(`activation_checkpointing`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoderLayer(activation_checkpointing))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`''`

) –str, optional a dictionary of {"module","interval","offload"}, where "module": str accept ["transformer", "attention"] to select which module should do activation checkpointing. "interval": int, default 1, interval of applying activation checkpointing, interval = 1 means that we apply checkpointing on every layer (if activation), otherwise, we apply it every x interval. "offload": bool, default False, if set to True, we offload activation to cpu and reload it during backward, otherwise, we recalculate activation in backward. default "".

-

(`export`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoderLayer(export))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –bool, optional if set to True, it removes the padding from convolutional layers and allow the onnx conversion for inference. default False.

-

(`use_pt_scaled_dot_product_attention`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoderLayer(use_pt_scaled_dot_product_attention))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –bool, optional if set to True, use pytorch's scaled dot product attention implementation in training.

-

(`attn_group_sizes`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoderLayer(attn_group_sizes))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`1`

) –int, optional the number of groups to use for attention, default 1 (Multi-Head Attention), 1 = typical Multi-Head Attention, 1 < attn_group_sizes < attention_heads = Grouped-Query Attention attn_group_sizes = attention_heads = Multi-Query Attention


Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoderLayer.forward)ConformerEncoder forward.


## Source code in `vllm/model_executor/models/phi4mm_audio.py`


|
|

###

`forward(x, pos_k, pos_v, mask, relative_attention_bias=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoderLayer.forward)

ConformerEncoder forward.

Parameters:

-

(`x`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoderLayer.forward(x))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)input feature of shape (batch, max_time_in, size)

-

(`pos_k`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoderLayer.forward(pos_k))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)positional key embedding.

-

(`pos_v`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoderLayer.forward(pos_v))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)positional value embedding.

-

(`mask`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoderLayer.forward(mask))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)mask for x (batch, max_time_in)

-

(`relative_attention_bias`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.ConformerEncoderLayer.forward(relative_attention_bias))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –bias added to attention logits w.r.t. relative positions (1, n_head, time1, time2)


## Source code in `vllm/model_executor/models/phi4mm_audio.py`


##

`TransformerEncoderBase`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.TransformerEncoderBase)

The Base class for Transformer based encoders.

Please set causal = True in streaming model Args: input_size: int input feature dimension. chunk_size: int, list(int) Number of frames for each chunk This variable can take 2 forms: int: Used for inference, or single chunk size training list(int) : Used only for variable chunk size training Some examples for the 2 cases: chunk_size = 12 chunk_size = [6, 8, 12, 24] left_chunk: int, list(int) Number of chunks used for masking in streaming mode. This variable can take 2 forms: int: Used for inference, or single chunk size training list(int) : Used only for variable chunk size training. When chunk_size is a list, left_chunk must be a list with same length. Some examples for the 2 cases: left_chunk = 6 left_chunk = [12, 9, 6, 3] attention_dim: int, optional attention dimension. default 256. attention_heads: int, optional the number of heads. default 4 input_layer: str, optional input layer type before Conformer, one of ["linear", "conv2d", "custom", "vgg2l", "embed"], default "conv2d" cnn_out: int, optional the number of CNN channels before Conformer. default -1. cnn_layer_norm: bool, optional layer norm between Conformer and the first CNN. default False. time_reduction: int, optional time reduction factor default 4 dropout_rate: float, optional dropout rate. default 0.1 padding_idx: int, optional padding index for input_layer=embed default -1 relative_attention_bias_args: dict, optional use more efficient scalar bias-based relative multihead attention (Q*K^T + B) implemented in cmb.basics.embedding. [T5/ALiBi]RelativeAttentionLogitBias usage: relative_attention_bias_args={"type": t5/alibi} additional method-specific arguments can be provided (see transformer_base.py) positional_dropout_rate: float, optional dropout rate after positional encoding. default 0.0 nemo_conv_settings: dict, optional A dictionary of settings for NeMo Subsampling. default None conv2d_extra_padding: str, optional Add extra padding in conv2d subsampling layers. Choices are (feat, feat_time, none, True). if True or feat_time, the extra padding is added into non full supraframe utts in batch. Default: none attention_group_size: int, optional the number of groups to use for attention, default 1 (Multi-Head Attention), 1 = typical Multi-Head Attention, 1 < attention_group_size < attention_heads = Grouped-Query Attention attention_group_size = attention_heads = Multi-Query Attention

Methods:

-
–[compute_lens_change](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.TransformerEncoderBase.compute_lens_change)feature_lens: int

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.TransformerEncoderBase.forward)Abstract forward method implementation.

-
–[forward_embeddings](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.TransformerEncoderBase.forward_embeddings)Forwarding the inputs through the top embedding layers.

-
–[get_offset](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.TransformerEncoderBase.get_offset)Returns offset used when retaining inputs for decoding.


## Source code in `vllm/model_executor/models/phi4mm_audio.py`


|
|

###

`_chunk_size_selection(chunk_size=None, left_chunk=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.TransformerEncoderBase._chunk_size_selection)

If chunk size is a list, we will randomly select a chunk size.

## Source code in `vllm/model_executor/models/phi4mm_audio.py`


###

`compute_lens_change(feature_lens)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.TransformerEncoderBase.compute_lens_change)

feature_lens: int return updated feature lens.

This used to return a different lambda function for each case that computed the right thing. That does not work within Torchscript. If you really need this to be faster, create nn.Module()-s for all the cases and return one of them. Torchscript does support that.

## Source code in `vllm/model_executor/models/phi4mm_audio.py`


###

`forward()`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.TransformerEncoderBase.forward)

###

`forward_embeddings(xs_pad, masks, chunk_size_nc=None, left_chunk_nc=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.TransformerEncoderBase.forward_embeddings)

Forwarding the inputs through the top embedding layers.

Parameters:

-

(`xs_pad`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.TransformerEncoderBase.forward_embeddings(xs_pad))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)torch.Tensor input tensor

-

(`masks`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.TransformerEncoderBase.forward_embeddings(masks))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)torch.Tensor input mask

-

(`chunk_size_nc`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.TransformerEncoderBase.forward_embeddings(chunk_size_nc))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)|[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | None`None`

) –(optional, default is None) chunk size for non-causal layers

-

(`left_chunk_nc`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.TransformerEncoderBase.forward_embeddings(left_chunk_nc))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)|[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | None`None`

) –(optional, default is None) # of left chunks for non-causal layers


## Source code in `vllm/model_executor/models/phi4mm_audio.py`


|
|

###

`get_offset()`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.TransformerEncoderBase.get_offset)

Returns offset used when retaining inputs for decoding.

This is essentially, how many additional frames have to be added to the front-end CNN input to ensure it can produce a single output. So if the "padding" parameter is 0, typically offset will be > 0.

## Source code in `vllm/model_executor/models/phi4mm_audio.py`


##

`WindowQformer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.WindowQformer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Window-level Qformer.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.WindowQformer.forward)Forward decoder.


## Source code in `vllm/model_executor/models/phi4mm_audio.py`


|
|

###

`forward(audio_embed, mask, embed_len=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_audio.WindowQformer.forward)

Forward decoder.