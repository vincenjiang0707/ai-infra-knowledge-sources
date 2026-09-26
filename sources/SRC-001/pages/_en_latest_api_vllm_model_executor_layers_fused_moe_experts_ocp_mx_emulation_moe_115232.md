source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/ocp_mx_emulation_moe/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.fused_moe.experts.ocp_mx_emulation_moe`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.ocp_mx_emulation_moe)

OCP MX quantization emulation for MoE.

This file implements OCP MX (MXFP4/MXFP6) emulation for MoE in case the hardware used does not natively support OCP MX MoE.

Weights are dequantized on the fly during each forward, we fall back to calling `TritonExperts`

using BF16, and fake OCP MX quantize-dequantize is applied on activations via `moe_kernel_quantize_input`

.

Classes:

-
–[OCP_MXQuantizationEmulationTritonExperts](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.ocp_mx_emulation_moe.OCP_MXQuantizationEmulationTritonExperts)Extension of TritonExperts to support emulated OCP MX MoE experts.


Functions:

-
–[activation_quant_dtype](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.ocp_mx_emulation_moe.activation_quant_dtype)Activation dtype

`moe_kernel_quantize_input`

should fake-quantize to.

##

`OCP_MXQuantizationEmulationTritonExperts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.ocp_mx_emulation_moe.OCP_MXQuantizationEmulationTritonExperts)

Bases: [TritonExperts](https://docs.vllm.ai/triton_moe/#vllm.model_executor.layers.fused_moe.experts.triton_moe.TritonExperts)

Extension of TritonExperts to support emulated OCP MX MoE experts.

It may be used for OCP MX (MXFP4/MXFP6) models when the device does not have native support for these dtypes.

Methods:

-
–[apply](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.ocp_mx_emulation_moe.OCP_MXQuantizationEmulationTritonExperts.apply)Apply emulated quantized MoE computation.


## Source code in `vllm/model_executor/layers/fused_moe/experts/ocp_mx_emulation_moe.py`


|
|

###

`_dequantize_weights(w, w_scale, dtype)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.ocp_mx_emulation_moe.OCP_MXQuantizationEmulationTritonExperts._dequantize_weights)

Dequantize weights based on the OCP MX scheme.

## Source code in `vllm/model_executor/layers/fused_moe/experts/ocp_mx_emulation_moe.py`


###

`apply(output, hidden_states, w1, w2, topk_weights, topk_ids, activation, global_num_experts, expert_map, a1q_scale, a2_scale, workspace13, workspace2, expert_tokens_meta, apply_router_weight_on_input)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.ocp_mx_emulation_moe.OCP_MXQuantizationEmulationTritonExperts.apply)

Apply emulated quantized MoE computation.

This dequantizes the weights on the fly and calls TritonExperts.apply with activation quantization support.

## Source code in `vllm/model_executor/layers/fused_moe/experts/ocp_mx_emulation_moe.py`


##

`activation_quant_dtype(ocp_mx_scheme)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.ocp_mx_emulation_moe.activation_quant_dtype)

Activation dtype `moe_kernel_quantize_input`

should fake-quantize to.

Parameters:

-

(`ocp_mx_scheme`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.ocp_mx_emulation_moe.activation_quant_dtype(ocp_mx_scheme))`OCP_MX_Scheme |`

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The OCP MX scheme the emulated experts run. Accepts the enum member or its string value.


Returns:

-

–[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)|[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneA

`quant_dtype`

`moe_kernel_quantize_input`

dispatches on, or None for -

–[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)|[str](https://docs.python.org/3/builtins/stdtypes.html#str)| Noneweight-only schemes, which leave activations untouched.


Raises:

-

–[NotImplementedError](https://docs.python.org/3/builtins/exceptions.html#NotImplementedError)If the scheme has no emulated activation dtype.