source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/activation/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.fused_moe.activation`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.activation)

MoE activation function enum and utilities.

Classes:

-
–[ApplyMoEActivationConfig](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.activation.ApplyMoEActivationConfig)Configuration forwarded to

`apply_moe_activation`

. -
–[MoEActivation](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.activation.MoEActivation)Activation functions for MoE layers.


Functions:

-
–[activation_without_mul](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.activation.activation_without_mul)Get the non-gated variant of an activation function.

-
–[apply_moe_activation](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.activation.apply_moe_activation)Apply MoE activation function.

-
–[apply_moe_activation_masked_supported](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.activation.apply_moe_activation_masked_supported)Whether the masked

`apply_moe_activation`

path supports an activation. -
–[apply_moe_activation_supported](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.activation.apply_moe_activation_supported)Whether

`apply_moe_activation`

supports an activation. -
–[situ_and_mul_quant](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.activation.situ_and_mul_quant)Fused Kimi SITU activation + dynamic FP8 quantization.


##

`ApplyMoEActivationConfig`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.activation.ApplyMoEActivationConfig)

Configuration forwarded to `apply_moe_activation`

.

Methods:

-
–[from_configs](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.activation.ApplyMoEActivationConfig.from_configs)Build from the model and quantization configurations.


## Source code in `vllm/model_executor/layers/fused_moe/activation.py`


###

`from_configs(moe_config, quant_config)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.activation.ApplyMoEActivationConfig.from_configs)

Build from the model and quantization configurations.

## Source code in `vllm/model_executor/layers/fused_moe/activation.py`


##

`MoEActivation`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.activation.MoEActivation)

Bases: [Enum](https://docs.python.org/3/library/enum.html#enum.Enum)

Activation functions for MoE layers.

Methods:

-
–[from_str](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.activation.MoEActivation.from_str)Parse from string for backward compatibility.

-
–[without_mul](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.activation.MoEActivation.without_mul)Get the non-gated variant of this activation.


Attributes:

-
([custom_op_name](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.activation.MoEActivation.custom_op_name)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Maps to the CustomOp name of activations

-
([is_gated](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.activation.MoEActivation.is_gated)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Returns True if activation expects gate*activation(up) pattern.


## Source code in `vllm/model_executor/layers/fused_moe/activation.py`


###

`custom_op_name`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.activation.MoEActivation.custom_op_name)

Maps to the CustomOp name of activations in vllm/model_executor/layers/activation.py.

###

`is_gated`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.activation.MoEActivation.is_gated)

Returns True if activation expects gate*activation(up) pattern.

Gated activations expect input tensor with 2x the output size, where the first half is the gate and second half is the up projection.

###

`from_str(s)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.activation.MoEActivation.from_str)

Parse from string for backward compatibility.

## Source code in `vllm/model_executor/layers/fused_moe/activation.py`


###

`without_mul()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.activation.MoEActivation.without_mul)

Get the non-gated variant of this activation.

For activations that have a _no_mul variant, returns that variant. For activations without a _no_mul variant (or already _no_mul), returns self.

## Source code in `vllm/model_executor/layers/fused_moe/activation.py`


##

`activation_without_mul(activation)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.activation.activation_without_mul)

Get the non-gated variant of an activation function.

Parameters:

Returns:

-

–[str](https://docs.python.org/3/builtins/stdtypes.html#str)The non-gated activation name (e.g., "silu_no_mul", "gelu_no_mul")


## Source code in `vllm/model_executor/layers/fused_moe/activation.py`


##

`apply_moe_activation(activation, output, input, *, activation_config=None, topk_ids=None, expert_map=None, valid_token_counts=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.activation.apply_moe_activation)

Apply MoE activation function.

The configuration drives specialized activation behavior. Routing tensors and valid token counts remain per-call inputs because they depend on the current token assignment. A single token count masks a flat `[T, D]`

buffer; one count per expert masks each prefix in a padded `[E, T, D]`

buffer.

## Source code in `vllm/model_executor/layers/fused_moe/activation.py`


|
|

##

`apply_moe_activation_masked_supported(activation)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.activation.apply_moe_activation_masked_supported)

Whether the masked `apply_moe_activation`

path supports an activation.

##

`apply_moe_activation_supported(activation)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.activation.apply_moe_activation_supported)

Whether `apply_moe_activation`

supports an activation.

##

`situ_and_mul_quant(output, scale, input, *, beta, linear_beta, group_size=0, num_valid_tokens=None, topk=1)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.activation.situ_and_mul_quant)

Fused Kimi SITU activation + dynamic FP8 quantization.

Writes the quantized fp8 down-projection input into `output`

[M, d] and its float32 scale into `scale`

(dequant = q * scale), fusing the SITU activation with the FP8 quant that Humming's w2 GEMM would otherwise perform in a separate pass -- this avoids materializing (and rounding through) the bf16 activation_output buffer.

`group_size`

selects the quant granularity: `0`

gives per-token scales `scale`

[M, 1]; `128`

gives k-major block-FP8 group scales `scale`

[M, d // 128], matching humming `quant_input(group_size=128, float32)`

.

`linear_beta`

<= 0 (or None) means "unset" (up passed through), matching `SituAndMul(linear_beta=None)`

. `num_valid_tokens`

(int32 scalar tensor) is the DeepEP v2 contiguous-layout token count (e.g. `psum[-1:]`

); the kernel multiplies it by `topk`

to bound rows. Padding rows are skipped and receive a benign scale of 1.0. Kept in this module so that every `torch.ops._C.situ*`

call lives in one file.