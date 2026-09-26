source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/utils/int8_utils/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.quantization.utils.int8_utils`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.int8_utils)

Functions:

-
–[block_dequant](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.int8_utils.block_dequant)This function conducts block-wise dequantization.

-
–[per_token_group_quant_int8](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.int8_utils.per_token_group_quant_int8)Function to perform per-token-group quantization on an input tensor

`x`

.

##

`_per_token_group_quant_int8(y_ptr, y_q_ptr, y_s_ptr, y_stride, N, eps, int8_min, int8_max, BLOCK)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.int8_utils._per_token_group_quant_int8)

A Triton-accelerated function to perform per-token-group quantization on a tensor.

This function converts the tensor values into int8 values.

## Source code in `vllm/model_executor/layers/quantization/utils/int8_utils.py`


##

`block_dequant(x_q_block, x_s, block_size)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.int8_utils.block_dequant)

This function conducts block-wise dequantization. The inputs are block-wise quantization tensor `x_q_block`

, block-wise quantization scale and the block size. The outputs are dequantized tensor.

## Source code in `vllm/model_executor/layers/quantization/utils/int8_utils.py`


##

`per_token_group_quant_int8(x, group_size, eps=1e-10, dtype=torch.int8)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.int8_utils.per_token_group_quant_int8)

Function to perform per-token-group quantization on an input tensor `x`

.

It converts the tensor values into signed int8 values and returns the quantized tensor along with the scaling factor used for quantization.

Parameters:

-

(`x`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.int8_utils.per_token_group_quant_int8(x))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The input tensor with ndim >= 2.

-

(`group_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.int8_utils.per_token_group_quant_int8(group_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)The group size used for quantization.

-

(`eps`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.int8_utils.per_token_group_quant_int8(eps))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)`1e-10`

) –The minimum to avoid dividing zero.

-

(`dtype`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.int8_utils.per_token_group_quant_int8(dtype))

, default:[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)`int8`

) –The dype of output tensor. Note that only

`torch.int8`

is supported for now.

Returns:

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]tuple[torch.Tensor, torch.Tensor]: The quantized tensor and the scaling factor for quantization.