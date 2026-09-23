source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/phi4mm_utils/
lastmod: 2026-09-23

#

`vllm.model_executor.models.phi4mm_utils`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils)

Classes:

-
–[AbsolutePositionalEncoding](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.AbsolutePositionalEncoding)Absolute Positional encoding module.

-
–[AttModule](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.AttModule)Attention abstraction module.

-
–[BlockBase](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.BlockBase)Block abstract module.

-
–[CausalConv1D](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.CausalConv1D)A causal version of nn.Conv1d where each step would have limited access to

-
–[CausalConv2D](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.CausalConv2D)A causal version of nn.Conv2d where each location in the 2D matrix would

-
–[ConvModule](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.ConvModule)ConvModule Module for the conformer block.

-
–[DepthWiseSeparableConv1d](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.DepthWiseSeparableConv1d)DepthWiseSeparableConv1d module used in ConvNet module

-
–[FeedForward](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.FeedForward)FeedForward Module.

-
–[GLU](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.GLU)Implement Gated Linear Unit (GLU) module.

-
–[GLULinear](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.GLULinear)Linear + GLU module.

-
–[GLUPointWiseConv](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.GLUPointWiseConv)GLUPointWiseConv module

-
–[MeanVarianceNormLayer](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.MeanVarianceNormLayer)Mean/variance normalization layer.

-
–[MultiHeadedAttention](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.MultiHeadedAttention)Multi-Head Attention layer with optional relative position embedding

-
–[MultiSequential](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.MultiSequential)Multi-input multi-output torch.nn.Sequential.

-
–[NemoConvSubsampling](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.NemoConvSubsampling)Convlutional subsampling module, taken from NeMo ASR

-
–[T5RelativeAttentionLogitBias](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.T5RelativeAttentionLogitBias)This module implements the relative position bias described in Section


Functions:

-
–[adaptive_enc_mask](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.adaptive_enc_mask)The function is very important for Transformer Transducer Streaming mode

-
–[calc_length_int](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.calc_length_int)Integer-only variant of calc_length for meta-safe shape computation.

-
–[get_activation](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.get_activation)Select an activation function by name.

-
–[get_offset](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.get_offset)Get an offset. We will use the offset for determining #frames of a

-
–[unfold_tensor](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.unfold_tensor)For a given tensor with shape of (N, T, D), if sequence length T is


##

`AbsolutePositionalEncoding`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.AbsolutePositionalEncoding)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Absolute Positional encoding module. This module implement Absolute sinusoidal positional encoding from: https://arxiv.org/pdf/1706.03762.pdf

Parameters:

-

(`d_model`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.AbsolutePositionalEncoding(d_model))

) –[int](https://docs.python.org/3/builtins/functions.html#int)int Input embedding size.

-

(`dropout_rate`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.AbsolutePositionalEncoding(dropout_rate))

) –[float](https://docs.python.org/3/builtins/functions.html#float)float dropout rate

-

(`max_len`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.AbsolutePositionalEncoding(max_len))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`5000`

) –int, optional Maximum input length sequence, Default 5000


Methods:

-
–[__init__](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.AbsolutePositionalEncoding.__init__)Construct an PositionalEncoding object.

-
–[extend_pe](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.AbsolutePositionalEncoding.extend_pe)Reset the positional encodings.

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.AbsolutePositionalEncoding.forward)Add positional encoding.


## Source code in `vllm/model_executor/models/phi4mm_utils.py`


###

`__init__(d_model, dropout_rate, max_len=5000)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.AbsolutePositionalEncoding.__init__)

Construct an PositionalEncoding object.

## Source code in `vllm/model_executor/models/phi4mm_utils.py`


###

`extend_pe(x)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.AbsolutePositionalEncoding.extend_pe)

Reset the positional encodings.

Parameters:

## Source code in `vllm/model_executor/models/phi4mm_utils.py`


###

`forward(x)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.AbsolutePositionalEncoding.forward)

Add positional encoding.

Parameters:

Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Encoded tensor. Its shape is (batch, time, ...)


## Source code in `vllm/model_executor/models/phi4mm_utils.py`


##

`AttModule`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.AttModule)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Attention abstraction module.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.AttModule.forward)AttModule forward.

-
–[set_export](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.AttModule.set_export)Set the export mode.


## Source code in `vllm/model_executor/models/phi4mm_utils.py`


###

`forward(x, memory=None, pos_emb=None, att_mask=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.AttModule.forward)

AttModule forward.

Parameters:

-

(`x`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.AttModule.forward(x))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)input tensor.

-

(`memory`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.AttModule.forward(memory))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –memory tensor.

-

(`pos_emb`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.AttModule.forward(pos_emb))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –positional encoder embedding.

-

(`att_mask`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.AttModule.forward(att_mask))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –attention mask tensor.


## Source code in `vllm/model_executor/models/phi4mm_utils.py`


##

`BlockBase`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.BlockBase)

##

`CausalConv1D`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.CausalConv1D)

Bases: [Conv1d](https://pytorch.org/docs/stable/generated/torch.nn.Conv1d.html#torch.nn.Conv1d)

A causal version of nn.Conv1d where each step would have limited access to locations on its right or left All arguments are the same as nn.Conv1d except padding.

If padding is set None, then paddings are set automatically to make it a causal convolution where each location would not see any steps on its right.

If padding is set as a list (size of 2), then padding[0] would be used as left padding and padding[1] as right padding. It would make it possible to control the number of steps to be accessible on the right and left. This mode is not supported when stride > 1. padding[0]+padding[1] should be equal to (kernel_size - 1).

## Source code in `vllm/model_executor/models/phi4mm_utils.py`


|
|

##

`CausalConv2D`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.CausalConv2D)

Bases: [Conv2d](https://pytorch.org/docs/stable/generated/torch.nn.Conv2d.html#torch.nn.Conv2d)

A causal version of nn.Conv2d where each location in the 2D matrix would have no access to locations on its right or down All arguments are the same as nn.Conv2d except padding which should be set as None

## Source code in `vllm/model_executor/models/phi4mm_utils.py`


##

`ConvModule`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.ConvModule)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

ConvModule Module for the conformer block. for more details see: https://arxiv.org/pdf/2005.08100v1.pdf

Parameters:

-

(`input_dim`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.ConvModule(input_dim))

) –[int](https://docs.python.org/3/builtins/functions.html#int)int input channel size.

-

(`ext_pw_out_channel`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.ConvModule(ext_pw_out_channel))

) –[int](https://docs.python.org/3/builtins/functions.html#int)int if > 0, ext_pw_out_channel is a dim channel size for the last pointwise conv after swish activation.

-

(`depthwise_seperable_out_channel`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.ConvModule(depthwise_seperable_out_channel))

) –[int](https://docs.python.org/3/builtins/functions.html#int)int if set different to 0, the number of depthwise_seperable_out_channel will be used as a channel_out of the second conv1d layer. otherwise, it equal to 0, the second conv1d layer is skipped.

-

(`ext_pw_kernel_size`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.ConvModule(ext_pw_kernel_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)int kernel size of the conv pointwise of the conformer.

-

(`kernel_size`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.ConvModule(kernel_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)int kernel size.

-

(`depthwise_multiplier`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.ConvModule(depthwise_multiplier))

) –[int](https://docs.python.org/3/builtins/functions.html#int)int number of input_dim channels duplication. this value will be used to compute the hidden channels of the Conv1D.

-

(`dropout_rate`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.ConvModule(dropout_rate))

) –[float](https://docs.python.org/3/builtins/functions.html#float)float dropout rate.

-

(`causal`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.ConvModule(causal))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –bool, optional if set to True, convolution have no access to future frames. default False.

-

(`batch_norm`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.ConvModule(batch_norm))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –bool, optional if set to True, apply batchnorm before activation. default False

-

(`chunk_se`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.ConvModule(chunk_se))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –int, optional 0 for offline SE. 1 for streaming SE, where mean is computed by accumulated history until current chunk_se. 2 for streaming SE, where mean is computed by only the current chunk.

-

(`chunk_size`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.ConvModule(chunk_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)|[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]`18`

) –int, optional chunk size for cnn. default 18

-

(`activation`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.ConvModule(activation))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'relu'`

) –str, optional activation function used in ConvModule, default: "relu".

-

(`glu_type`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.ConvModule(glu_type))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'sigmoid'`

) –str, optional activation function used for the glu, default: "sigmoid".

-

(`bias_in_glu`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.ConvModule(bias_in_glu))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –bool, optional if set to True, use additive bias in the weight module before GLU.

-

(`linear_glu_in_convm`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.ConvModule(linear_glu_in_convm))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –bool, optional if set to True, use GLULinear module, otherwise, used GLUPointWiseConv module. default to False.

-

(`export`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.ConvModule(export))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –bool, optional, if set to True, padding is equal to 0. This is for inference, or onnx export. Typically this is set by the export program or the decoder program, and it isn't present in your config file. default False


Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.ConvModule.forward)ConvModule Forward.


## Source code in `vllm/model_executor/models/phi4mm_utils.py`


|
|

###

`_add_ext_pw_layer()`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.ConvModule._add_ext_pw_layer)

This function is an extension of **init** function and dedicated to the convolution module creation of the conformer.

## Source code in `vllm/model_executor/models/phi4mm_utils.py`


###

`forward(x)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.ConvModule.forward)

ConvModule Forward.

Parameters:

## Source code in `vllm/model_executor/models/phi4mm_utils.py`


##

`DepthWiseSeparableConv1d`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.DepthWiseSeparableConv1d)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

DepthWiseSeparableConv1d module used in ConvNet module for the conformer, for more details see: https://arxiv.org/pdf/2005.08100v1.pdf

Parameters:

-

(`input_dim`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.DepthWiseSeparableConv1d(input_dim))

) –[int](https://docs.python.org/3/builtins/functions.html#int)int input channel size.

-

(`depthwise_seperable_out_channel`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.DepthWiseSeparableConv1d(depthwise_seperable_out_channel))

) –[int](https://docs.python.org/3/builtins/functions.html#int)int if set different to 0, the number of depthwise_seperable_out_channel will be used as a channel_out of the second conv1d layer. otherwise, it equals to 0, the second conv1d layer is skipped.

-

(`kernel_size`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.DepthWiseSeparableConv1d(kernel_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)int kernel_size

-

(`depthwise_multiplier`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.DepthWiseSeparableConv1d(depthwise_multiplier))

) –[int](https://docs.python.org/3/builtins/functions.html#int)int number of input_dim channels duplication. this value will be used to compute the hidden channels of the Conv1D.

-

(`padding`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.DepthWiseSeparableConv1d(padding))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –int, optional padding for the conv1d, default: 0.


Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.DepthWiseSeparableConv1d.forward)Args:


## Source code in `vllm/model_executor/models/phi4mm_utils.py`


##

`FeedForward`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.FeedForward)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

FeedForward Module. For more details see Conformer paper: https://arxiv.org/pdf/2005.08100.pdf

Parameters:

-

(`d_model`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.FeedForward(d_model))

) –[int](https://docs.python.org/3/builtins/functions.html#int)int input size.

-

(`d_inner`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.FeedForward(d_inner))

) –[int](https://docs.python.org/3/builtins/functions.html#int)int output size.

-

(`dropout_rate`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.FeedForward(dropout_rate))

) –[float](https://docs.python.org/3/builtins/functions.html#float)float, dropout rate.

-

(`activation`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.FeedForward(activation))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'sigmoid'`

) –str, activation function name, one of ["relu", "swish", "sigmoid"], sigmoid activation is only used with "glu_in_fnn=True", default "sigmoid".

-

(`bias_in_glu`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.FeedForward(bias_in_glu))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –bool, optional


Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.FeedForward.forward)FeedForward forward function.


## Source code in `vllm/model_executor/models/phi4mm_utils.py`


###

`forward(x)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.FeedForward.forward)

FeedForward forward function.

Parameters:

##

`GLU`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.GLU)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Implement Gated Linear Unit (GLU) module.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.GLU.forward)GLU forward


## Source code in `vllm/model_executor/models/phi4mm_utils.py`


###

`forward(x)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.GLU.forward)

GLU forward Apply Swish function on the first half of input matrices with sigmoid of the second half.

Parameters:

## Source code in `vllm/model_executor/models/phi4mm_utils.py`


##

`GLULinear`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.GLULinear)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Linear + GLU module.

Parameters:

-

(`input_dim`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.GLULinear(input_dim))

) –[int](https://docs.python.org/3/builtins/functions.html#int)int input size

-

(`output_dim`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.GLULinear(output_dim))

) –[int](https://docs.python.org/3/builtins/functions.html#int)int output size.

-

(`glu_type`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.GLULinear(glu_type))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'sigmoid'`

) –activation function name used in glu module. default "sigmoid" (swish function).

-

(`bias_in_glu`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.GLULinear(bias_in_glu))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –bool, optional If True, the addtive bias is added. Default False.


Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.GLULinear.forward)GLULinear forward.


## Source code in `vllm/model_executor/models/phi4mm_utils.py`


##

`GLUPointWiseConv`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.GLUPointWiseConv)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

GLUPointWiseConv module used for conformer architecture, for more details see: https://arxiv.org/pdf/2005.08100v1.pdf

Parameters:

-

(`input_dim`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.GLUPointWiseConv(input_dim))

) –[int](https://docs.python.org/3/builtins/functions.html#int)int input channel size.

-

(`output_dim`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.GLUPointWiseConv(output_dim))

) –[int](https://docs.python.org/3/builtins/functions.html#int)int output channel size.

-

(`kernel_size`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.GLUPointWiseConv(kernel_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)int kernel size

-

(`glu_type`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.GLUPointWiseConv(glu_type))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'sigmoid'`

) –str, optional activation function one of ["sigmoid", "relu", "gelu"] default "sigmoid".

-

(`bias_in_glu`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.GLUPointWiseConv(bias_in_glu))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –bool, optional use addtive bias in glu

-

(`causal`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.GLUPointWiseConv(causal))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –bool, optional if set to True, padding is set to the half of kernel size, ie, convolution can't see future frames. default False.


Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.GLUPointWiseConv.forward)Args:


## Source code in `vllm/model_executor/models/phi4mm_utils.py`


|
|

###

`forward(x)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.GLUPointWiseConv.forward)

Args: x: input tensor

## Source code in `vllm/model_executor/models/phi4mm_utils.py`


##

`MeanVarianceNormLayer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.MeanVarianceNormLayer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Mean/variance normalization layer.

Will subtract mean and multiply input by inverted standard deviation. Typically used as a very first layer in a model.

Parameters:

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.MeanVarianceNormLayer.forward)MeanVarianceNormLayer Forward.


## Source code in `vllm/model_executor/models/phi4mm_utils.py`


###

`forward(input_)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.MeanVarianceNormLayer.forward)

MeanVarianceNormLayer Forward.

Parameters:

##

`MultiHeadedAttention`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.MultiHeadedAttention)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Multi-Head Attention layer with optional relative position embedding and GLU.

Parameters:

-

(`n_head`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.MultiHeadedAttention(n_head))

) –[int](https://docs.python.org/3/builtins/functions.html#int)int the number of heads.

-

(`n_feat`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.MultiHeadedAttention(n_feat))

) –[int](https://docs.python.org/3/builtins/functions.html#int)int input size features.

-

(`dropout_rate`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.MultiHeadedAttention(dropout_rate))

) –[float](https://docs.python.org/3/builtins/functions.html#float)float dropout rate.

-

(`attention_inner_dim`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.MultiHeadedAttention(attention_inner_dim))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`-1`

) –int, optional the attention dimension used in the class, it can be different from the input dimension n_feat. default: -1 (equal to n_feat).

-

(`use_pt_scaled_dot_product_attention`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.MultiHeadedAttention(use_pt_scaled_dot_product_attention))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –bool, optional if set True, use pytorch scaled dot product attention in training. NOTE: this will NOT be used in ONNX decoding due to a lack of support. In that case, we use the original attention implementation, which shows no regression. default: False.

-

(`n_value`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.MultiHeadedAttention(n_value))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`-1`

) –int, optional if set to values other than -1, use a different dimension for value. With the default value (i.e. -1), it is backward compatible.

-

(`group_size`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.MultiHeadedAttention(group_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`1`

) –int, optional. must divide

`n_head`

if group_size > 1: GQA if group_size = 1: MHA if group_size = n_head: MQA

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.MultiHeadedAttention.forward)Compute 'Scaled Dot Product Attention'.


## Source code in `vllm/model_executor/models/phi4mm_utils.py`


|
|

###

`forward(query, key, value, pos_k, pos_v, mask, relative_attention_bias=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.MultiHeadedAttention.forward)

Compute 'Scaled Dot Product Attention'.

Parameters:

-

(`query`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.MultiHeadedAttention.forward(query))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)query tensor (batch, time1, size)

-

(`key`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.MultiHeadedAttention.forward(key))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)key tensor (batch, time2, size)

-

(`value`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.MultiHeadedAttention.forward(value))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)value tensor (batch, time1, size)

-

(`pos_k`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.MultiHeadedAttention.forward(pos_k))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| Nonekey tensor used for relative positional embedding.

-

(`pos_v`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.MultiHeadedAttention.forward(pos_v))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| Nonevalue tensor used for relative positional embedding.

-

(`mask`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.MultiHeadedAttention.forward(mask))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| Nonemask tensor (batch, time1, time2)

-

(`relative_attention_bias`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.MultiHeadedAttention.forward(relative_attention_bias))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –bias added to attention logits w.r.t. relative positions (1, n_head, time1, time2)


## Source code in `vllm/model_executor/models/phi4mm_utils.py`


|
|

##

`MultiSequential`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.MultiSequential)

Bases: [Sequential](https://pytorch.org/docs/stable/generated/torch.nn.Sequential.html#torch.nn.Sequential)

Multi-input multi-output torch.nn.Sequential.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.MultiSequential.forward)Forward method implementation.


## Source code in `vllm/model_executor/models/phi4mm_utils.py`


##

`NemoConvSubsampling`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.NemoConvSubsampling)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Convlutional subsampling module, taken from NeMo ASR (https://github.com/NVIDIA/NeMo/blob/b367413645d5c72db3c2c96e46e95a 34501479cf/nemo/collections/asr/parts/submodules/subsampling.py)

Striding Subsampling: "Speech-Transformer: A No-Recurrence Sequence-to-Sequence Model for Speech Recognition" by Linhao Dong et al. (https://ieeexplore.ieee.org/document/8462506)

Compared with the EncoderConv2D (`input_layer: custom`

), this is a much simplified approach, and uses no LayerNorm and far fewer Conv2Ds. Moreover, depthwise convolutions are used to reduce FLOPs, but the first layer is kept as a regular convolution so as not to degrade accuracy.

`Striding`

and `dw_striding`

are the same except that the latter uses depthwise convolutions after the first layer, whereas the former does not.

Parameters:

-

(`subsampling_factor`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.NemoConvSubsampling(subsampling_factor))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`4`

) –Time reduction factor

-

(`feat_in`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.NemoConvSubsampling(feat_in))

) –[int](https://docs.python.org/3/builtins/functions.html#int)size of the input features

-

(`feat_out`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.NemoConvSubsampling(feat_out))

) –[int](https://docs.python.org/3/builtins/functions.html#int)size of the output features

-

(`subsampling`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.NemoConvSubsampling(subsampling))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'dw_striding'`

) –The subsampling technique, choose from {"striding", "dw-striding", "striding_conv1d", "dw_striding_conv1d"}

-

(`conv_channels`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.NemoConvSubsampling(conv_channels))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`256`

) –Number of channels for the convolution layers, default is 256.

-

(`subsampling_conv_chunking_factor`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.NemoConvSubsampling(subsampling_conv_chunking_factor))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`1`

) –Input chunking factor which can be -1 (no chunking) 1 (auto) or a power of 2. Default is 1

-

(`activation`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.NemoConvSubsampling(activation))`Module`

, default:

) –[ReLU](https://pytorch.org/docs/stable/generated/torch.nn.ReLU.html#torch.nn.ReLU)()activation function, default is nn.ReLU()

-

(`is_causal`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.NemoConvSubsampling(is_causal))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –whether to use causal Conv1/2D, where each step will have limited access to locations on its right or left


Methods:

-
–[channel_chunked_conv](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.NemoConvSubsampling.channel_chunked_conv)Performs channel chunked convolution.

-
–[conv_split_by_batch](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.NemoConvSubsampling.conv_split_by_batch)Tries to split input by batch, run conv and concat results.

-
–[conv_split_by_channel](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.NemoConvSubsampling.conv_split_by_channel)For dw convs, tries to split input by time, run conv and concat

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.NemoConvSubsampling.forward)Forward method for NeMo subsampling.


## Source code in `vllm/model_executor/models/phi4mm_utils.py`


|
|

###

`channel_chunked_conv(conv, chunk_size, x)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.NemoConvSubsampling.channel_chunked_conv)

Performs channel chunked convolution.

## Source code in `vllm/model_executor/models/phi4mm_utils.py`


###

`conv_split_by_batch(x)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.NemoConvSubsampling.conv_split_by_batch)

Tries to split input by batch, run conv and concat results.

## Source code in `vllm/model_executor/models/phi4mm_utils.py`


###

`conv_split_by_channel(x)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.NemoConvSubsampling.conv_split_by_channel)

For dw convs, tries to split input by time, run conv and concat results

## Source code in `vllm/model_executor/models/phi4mm_utils.py`


###

`forward(x, mask)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.NemoConvSubsampling.forward)

Forward method for NeMo subsampling.

Parameters:

Returns:

-
(`x`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Resulting tensor from subsampling (B, T // time_reduction_factor, feat_out)

-
(`pad_mask`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| Nonetensor of padded hidden state sequences (B, 1, T // time_reduction_factor)


## Source code in `vllm/model_executor/models/phi4mm_utils.py`


|
|

##

`T5RelativeAttentionLogitBias`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.T5RelativeAttentionLogitBias)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

This module implements the relative position bias described in Section 2.1 of the T5 paper: https://arxiv.org/pdf/1910.10683.pdf

The Huggingface implementation is used as a reference https://github.com/huggingface/transformers/blob/v4.30.0/src/ transformers/models/t5/modeling_t5.py#L435

Modifies attention as Q*K^T + B, where B is a learned scalar bias based on relative position of the query and key. It is HxNxN, where H is the number of heads, N is the sequence length.

I've made these modifications to the original T5 bias: - Skipping of the bucketing step. Original T5 bias converted rel position distances into logarithmically increasing buckets. This is supposed to help with length generalization. - I just directly use rel position index as bias values, as we don't need length generalization (40s max is good enough for ASR encoder), and it keeps ONNX export simple. - I've also extended it so that biases can be asymmetric, the default implementation treats L->R and R->L the same. Asymmetric was found to yield better results in my experiments.

Parameters:

-

(`num_heads`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.T5RelativeAttentionLogitBias(num_heads))

) –[int](https://docs.python.org/3/builtins/functions.html#int)int Number of attention heads

-

(`num_buckets`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.T5RelativeAttentionLogitBias(num_buckets))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`-1`

) –int Number of buckets to use for relative attention bias. This is the size of the learnable bias parameter. Bucketing is not yet supported, so this defaults to -1 which means no bucketing is used (max_distance determines size of bias param).

-

(`max_distance`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.T5RelativeAttentionLogitBias(max_distance))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`1000`

) –int Maximum distance to use for relative attention bias. With num_buckets=-1, this directly controls the max size of the bias parameter. When num_buckets > 0 is supported, this will control the maximum distance for logarithmic bucketing after which all positions are in the same bucket.

-

(`symmetric`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.T5RelativeAttentionLogitBias(symmetric))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –bool Whether to use symmetric or asymmetric biases. symmetric=False uses 2x number of bias params to distinguish L->R from R->L. This was found to be better for the encoder.


## Source code in `vllm/model_executor/models/phi4mm_utils.py`


|
|

##

`_pre_hook(state_dict, prefix, local_metadata, strict, missing_keys, unexpected_keys, error_msgs)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils._pre_hook)

Perform pre-hook in load_state_dict for backward compatibility.

## Note

We saved self.pe until v.0.5.2 but we have omitted it later. Therefore, we remove the item "pe" from `state_dict`

for backward compatibility.

## Source code in `vllm/model_executor/models/phi4mm_utils.py`


##

`adaptive_enc_mask(x_len, chunk_start_idx, left_window=0, right_window=0)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.adaptive_enc_mask)

The function is very important for Transformer Transducer Streaming mode Args: x_len: sequence length chunk_start_idx: first idx of each chunk, such as [0,18,36,48]. It also supports adaptive chunk size [0,10,15,45] left_window: how many left chunks can be seen right_window: how many right chunks can be seen. It is used for chunk overlap model.

Returns:

-
(`mask`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)a mask tensor for streaming model

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Torch 1.0.1

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)tensor([[1., 1., 0., 0.], [0., 1., 1., 0.], [0., 0., 1., 1.]])

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Torch 1.4.1

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)tensor([[True., True., False., False.], [False., True., True., False.], [False., False., True., True.]])


## Source code in `vllm/model_executor/models/phi4mm_utils.py`


##

`calc_length_int(lengths, all_paddings, kernel_size, stride, ceil_mode, repeat_num=1)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.calc_length_int)

Integer-only variant of calc_length for meta-safe shape computation.

Computes the output length of a 1D convolution / pooling stack using the same formula as calc_length, but operates purely on Python numbers so it can be safely used during meta tensor initialization.

## Source code in `vllm/model_executor/models/phi4mm_utils.py`


##

`get_activation(name='relu')`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.get_activation)

Select an activation function by name.

Parameters:

-

(`name`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.get_activation(name))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'relu'`

) –str activation function name, one of ["relu", "gelu", "swish", "sigmoid"], default "relu".


## Source code in `vllm/model_executor/models/phi4mm_utils.py`


##

`get_offset(input_layer, time_reduction)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.get_offset)

Get an offset. We will use the offset for determining #frames of a subsampled feature.

Parameters:

-

(`input_layer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.get_offset(input_layer))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Type of an input layer

-

(`time_reduction`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.get_offset(time_reduction))

) –[int](https://docs.python.org/3/builtins/functions.html#int)time reduction factor for downsampling a feature


Returns: int: offset

## Source code in `vllm/model_executor/models/phi4mm_utils.py`


##

`unfold_tensor(xs_pad, max_seq_len)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.phi4mm_utils.unfold_tensor)

For a given tensor with shape of (N, T, D), if sequence length T is longer than max_seq_len, this function unfold it to a (NT', max_seq_len, D) where T' is T // max_seq_len.

Parameters: