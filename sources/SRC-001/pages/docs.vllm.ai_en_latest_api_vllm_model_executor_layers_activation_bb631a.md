source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/activation/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.activation`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.activation)

Custom activation functions.

Classes:

-
–[FastGELU](https://docs.vllm.ai#vllm.model_executor.layers.activation.FastGELU) -
–[FatreluAndMul](https://docs.vllm.ai#vllm.model_executor.layers.activation.FatreluAndMul)An activation function for FATReLU.

-
–[GeluAndMul](https://docs.vllm.ai#vllm.model_executor.layers.activation.GeluAndMul)An activation function for GeGLU.

-
–[GeluAndMulSparse](https://docs.vllm.ai#vllm.model_executor.layers.activation.GeluAndMulSparse)An activation function for GeluAndMulSparse.

-
–[MulAndSilu](https://docs.vllm.ai#vllm.model_executor.layers.activation.MulAndSilu)An activation function for SwiGLU.

-
–[NewGELU](https://docs.vllm.ai#vllm.model_executor.layers.activation.NewGELU) -
–[QuickGELU](https://docs.vllm.ai#vllm.model_executor.layers.activation.QuickGELU) -
–[ReLUSquaredActivation](https://docs.vllm.ai#vllm.model_executor.layers.activation.ReLUSquaredActivation)Applies the relu^2 activation introduced in https://arxiv.org/abs/2109.08668v2.

-
–[SiluAndMul](https://docs.vllm.ai#vllm.model_executor.layers.activation.SiluAndMul)An activation function for SwiGLU.

-
–[SiluAndMulWithClamp](https://docs.vllm.ai#vllm.model_executor.layers.activation.SiluAndMulWithClamp)SwiGLU activation with input clamping (used by some MoE shared experts).

-
–[SituAndMul](https://docs.vllm.ai#vllm.model_executor.layers.activation.SituAndMul)SituGLU activation used by Kimi models.

-
–[SwigluOAIAndMul](https://docs.vllm.ai#vllm.model_executor.layers.activation.SwigluOAIAndMul) -
–[SwigluStepAndMul](https://docs.vllm.ai#vllm.model_executor.layers.activation.SwigluStepAndMul)An activation function for SwiGLU with clamping.

-
–[XIELU](https://docs.vllm.ai#vllm.model_executor.layers.activation.XIELU)Applies the xIELU activation function introduced in https://arxiv.org/abs/2411.13010


Functions:

-
–[get_act_and_mul_fn](https://docs.vllm.ai#vllm.model_executor.layers.activation.get_act_and_mul_fn)Get an activation-and-mul (i.e. SiluAndMul) function by name.

-
–[get_act_fn](https://docs.vllm.ai#vllm.model_executor.layers.activation.get_act_fn)Get an activation function by name.


##

`FastGELU`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.activation.FastGELU)

Bases: [CustomOp](https://docs.vllm.ai/custom_op/#vllm.model_executor.custom_op.CustomOp)

Methods:

-
–[forward_native](https://docs.vllm.ai#vllm.model_executor.layers.activation.FastGELU.forward_native)PyTorch-native implementation equivalent to forward().


## Source code in `vllm/model_executor/layers/activation.py`


###

`forward_native(x)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.activation.FastGELU.forward_native)

PyTorch-native implementation equivalent to forward().

##

`FatreluAndMul`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.activation.FatreluAndMul)

Bases: [CustomOp](https://docs.vllm.ai/custom_op/#vllm.model_executor.custom_op.CustomOp)

An activation function for FATReLU.

The function computes x -> FATReLU(x[:d]) * x[d:] where d = x.shape[-1] // 2. This is used in openbmb/MiniCPM-S-1B-sft.

## Shapes

x: (num_tokens, 2 * d) or (batch_size, seq_len, 2 * d) return: (num_tokens, d) or (batch_size, seq_len, d)

## Source code in `vllm/model_executor/layers/activation.py`


##

`GeluAndMul`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.activation.GeluAndMul)

Bases: [CustomOp](https://docs.vllm.ai/custom_op/#vllm.model_executor.custom_op.CustomOp)

An activation function for GeGLU.

The function computes x -> GELU(x[:d]) * x[d:] where d = x.shape[-1] // 2.

## Shapes

x: (batch_size, seq_len, 2 * d) or (num_tokens, 2 * d) return: (batch_size, seq_len, d) or (num_tokens, d)

Methods:

-
–[forward_native](https://docs.vllm.ai#vllm.model_executor.layers.activation.GeluAndMul.forward_native)PyTorch-native implementation equivalent to forward().


## Source code in `vllm/model_executor/layers/activation.py`


###

`forward_native(x)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.activation.GeluAndMul.forward_native)

PyTorch-native implementation equivalent to forward().

## Source code in `vllm/model_executor/layers/activation.py`


##

`GeluAndMulSparse`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.activation.GeluAndMulSparse)

Bases: [CustomOp](https://docs.vllm.ai/custom_op/#vllm.model_executor.custom_op.CustomOp)

An activation function for GeluAndMulSparse. This activation function is used in Gemma3n. It computes: up_proj = self.up_proj(x) gate_proj = self.gate_proj(x) gate_proj = self._gaussian_topk(gate_proj) # sparsity activations = self.act_fn(gate_proj) # gelu down_proj = self.down_proj(activations * up_proj) Shapes: x: (num_tokens, 2 * d) or (batch_size, seq_len, 2 * d) return: (num_tokens, d) or (batch_size, seq_len, d)

Methods:

-
–[forward_native](https://docs.vllm.ai#vllm.model_executor.layers.activation.GeluAndMulSparse.forward_native)PyTorch-native implementation equivalent to forward().


## Source code in `vllm/model_executor/layers/activation.py`


###

`forward_native(x)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.activation.GeluAndMulSparse.forward_native)

PyTorch-native implementation equivalent to forward().

##

`MulAndSilu`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.activation.MulAndSilu)

Bases: [CustomOp](https://docs.vllm.ai/custom_op/#vllm.model_executor.custom_op.CustomOp)

An activation function for SwiGLU.

The function computes x -> x[:d] * silu(x[d:]) where d = x.shape[-1] // 2.

## Shapes

x: (num_tokens, 2 * d) or (batch_size, seq_len, 2 * d) return: (num_tokens, d) or (batch_size, seq_len, d)

Methods:

-
–[forward_native](https://docs.vllm.ai#vllm.model_executor.layers.activation.MulAndSilu.forward_native)PyTorch-native implementation equivalent to forward().


## Source code in `vllm/model_executor/layers/activation.py`


###

`forward_native(x)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.activation.MulAndSilu.forward_native)

PyTorch-native implementation equivalent to forward().

##

`NewGELU`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.activation.NewGELU)

Bases: [CustomOp](https://docs.vllm.ai/custom_op/#vllm.model_executor.custom_op.CustomOp)

Methods:

-
–[forward_native](https://docs.vllm.ai#vllm.model_executor.layers.activation.NewGELU.forward_native)PyTorch-native implementation equivalent to forward().


## Source code in `vllm/model_executor/layers/activation.py`


###

`forward_native(x)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.activation.NewGELU.forward_native)

PyTorch-native implementation equivalent to forward().

##

`QuickGELU`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.activation.QuickGELU)

Bases: [CustomOp](https://docs.vllm.ai/custom_op/#vllm.model_executor.custom_op.CustomOp)

Methods:

-
–[forward_native](https://docs.vllm.ai#vllm.model_executor.layers.activation.QuickGELU.forward_native)PyTorch-native implementation equivalent to forward().


## Source code in `vllm/model_executor/layers/activation.py`


##

`ReLUSquaredActivation`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.activation.ReLUSquaredActivation)

Bases: [CustomOp](https://docs.vllm.ai/custom_op/#vllm.model_executor.custom_op.CustomOp)

Applies the relu^2 activation introduced in https://arxiv.org/abs/2109.08668v2.

Methods:

-
–[forward_native](https://docs.vllm.ai#vllm.model_executor.layers.activation.ReLUSquaredActivation.forward_native)PyTorch-native implementation equivalent to forward().


## Source code in `vllm/model_executor/layers/activation.py`


##

`SiluAndMul`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.activation.SiluAndMul)

Bases: [CustomOp](https://docs.vllm.ai/custom_op/#vllm.model_executor.custom_op.CustomOp)

An activation function for SwiGLU.

The function computes x -> silu(x[:d]) * x[d:] where d = x.shape[-1] // 2.

## Shapes

x: (num_tokens, 2 * d) or (batch_size, seq_len, 2 * d) return: (num_tokens, d) or (batch_size, seq_len, d)

Methods:

-
–[forward_native](https://docs.vllm.ai#vllm.model_executor.layers.activation.SiluAndMul.forward_native)PyTorch-native implementation equivalent to forward().


## Source code in `vllm/model_executor/layers/activation.py`


###

`forward_native(x)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.activation.SiluAndMul.forward_native)

PyTorch-native implementation equivalent to forward().

##

`SiluAndMulWithClamp`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.activation.SiluAndMulWithClamp)

Bases: [CustomOp](https://docs.vllm.ai/custom_op/#vllm.model_executor.custom_op.CustomOp)

SwiGLU activation with input clamping (used by some MoE shared experts).

## Computes

gate = clamp(x[..., :d], max=swiglu_limit) up = clamp(x[..., d:], min=-swiglu_limit, max=swiglu_limit) out = gate * sigmoid(alpha * gate) * (up + beta)

where d = x.shape[-1] // 2. The defaults alpha=1.0, beta=0.0 reduce this to `silu(gate) * up`

; SwiGLU-OAI style models pass alpha (sigmoid scale) and beta=1.0 (up bias).

## Shapes

x: (num_tokens, 2 * d) or (batch_size, seq_len, 2 * d) return: (num_tokens, d) or (batch_size, seq_len, d)

## Source code in `vllm/model_executor/layers/activation.py`


##

`SituAndMul`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.activation.SituAndMul)

Bases: [CustomOp](https://docs.vllm.ai/custom_op/#vllm.model_executor.custom_op.CustomOp)

SituGLU activation used by Kimi models.

Computes beta * tanh(gate / beta) * sigmoid(gate) * up. When `linear_beta`

is set, the up projection is also softly clipped with linear_beta * tanh(up / linear_beta).

## Source code in `vllm/model_executor/layers/activation.py`


##

`SwigluOAIAndMul`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.activation.SwigluOAIAndMul)

Bases: [CustomOp](https://docs.vllm.ai/custom_op/#vllm.model_executor.custom_op.CustomOp)

Methods:

-
–[forward_native](https://docs.vllm.ai#vllm.model_executor.layers.activation.SwigluOAIAndMul.forward_native)PyTorch-native implementation equivalent to forward().


## Source code in `vllm/model_executor/layers/activation.py`


###

`forward_native(x)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.activation.SwigluOAIAndMul.forward_native)

PyTorch-native implementation equivalent to forward().

## Source code in `vllm/model_executor/layers/activation.py`


##

`SwigluStepAndMul`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.activation.SwigluStepAndMul)

Bases: [CustomOp](https://docs.vllm.ai/custom_op/#vllm.model_executor.custom_op.CustomOp)

An activation function for SwiGLU with clamping.

Computes x -> silu(x[:d]).clamp(max=limit) * x[d:].clamp(-limit, limit) where d = x.shape[-1] // 2.

## Shapes

x: (num_tokens, 2 * d) or (batch_size, seq_len, 2 * d) return: (num_tokens, d) or (batch_size, seq_len, d)

Methods:

-
–[forward_native](https://docs.vllm.ai#vllm.model_executor.layers.activation.SwigluStepAndMul.forward_native)PyTorch-native implementation equivalent to forward().


## Source code in `vllm/model_executor/layers/activation.py`


###

`forward_native(x)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.activation.SwigluStepAndMul.forward_native)

PyTorch-native implementation equivalent to forward().

## Source code in `vllm/model_executor/layers/activation.py`


##

`XIELU`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.activation.XIELU)

Bases: [CustomOp](https://docs.vllm.ai/custom_op/#vllm.model_executor.custom_op.CustomOp)

Applies the xIELU activation function introduced in https://arxiv.org/abs/2411.13010 If the user has installed the nickjbrowning/XIELU, we import xIELU CUDA Otherwise, we emit a single warning and use xIELU Python

## Source code in `vllm/model_executor/layers/activation.py`


|
|

###

`_xielu_cuda(x)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.activation.XIELU._xielu_cuda)

Firewall function to prevent torch.compile from seeing .item().

## Source code in `vllm/model_executor/layers/activation.py`


##

`_get_gelu_pytorch_tanh()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.activation._get_gelu_pytorch_tanh)

Get PyTorch GELU with tanh approximation, with ROCm fallback and fast GELU for ARM.

## Source code in `vllm/model_executor/layers/activation.py`


##

`get_act_and_mul_fn(act_fn_name, *, compile_native=True)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.activation.get_act_and_mul_fn)

Get an activation-and-mul (i.e. SiluAndMul) function by name.

## Source code in `vllm/model_executor/layers/activation.py`


##

`get_act_fn(act_fn_name)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.activation.get_act_fn)

Get an activation function by name.