source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/utils/fp8_utils/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.quantization.utils.fp8_utils`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils)

Functions:

-
–[create_fp8_input_scale](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.create_fp8_input_scale)Create input scale parameter for static activation quantization.

-
–[create_fp8_scale_parameter](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.create_fp8_scale_parameter)Create scale parameter based on quantization strategy.

-
–[create_fp8_weight_parameter](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.create_fp8_weight_parameter)Create FP8 weight parameter.

-
–[get_fp8_block_weight_scale](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.get_fp8_block_weight_scale)Return the block-FP8 weight scale for supported quant methods.

-
–[get_w8a8_block_fp8_configs](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.get_w8a8_block_fp8_configs)Return optimized configurations for the w8a8 block fp8 kernel.

-
–[input_to_float8](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.input_to_float8)This function quantizes input values to float8 values "

-
–[per_token_group_quant_fp8](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.per_token_group_quant_fp8)Function to perform per-token-group quantization on an input tensor

`x`

. -
–[per_token_group_quant_fp8_packed_for_deepgemm](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.per_token_group_quant_fp8_packed_for_deepgemm)FP8 per-token-group quantization for DeepGEMM.

-
–[process_fp8_input_tensor_strategy_moe](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.process_fp8_input_tensor_strategy_moe)Process moe input scales for tensor-wise quantization strategy.

-
–[process_fp8_weight_block_strategy](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.process_fp8_weight_block_strategy)Process weights for block-wise quantization strategy.

-
–[process_fp8_weight_channel_strategy](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.process_fp8_weight_channel_strategy)Process weights for channel-wise quantization strategy.

-
–[process_fp8_weight_tensor_strategy](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.process_fp8_weight_tensor_strategy)Process weights for tensor-wise quantization strategy.

-
–[process_fp8_weight_tensor_strategy_moe](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.process_fp8_weight_tensor_strategy_moe)Process moe weights for tensor-wise quantization strategy.

-
–[requant_weight_ue8m0_inplace](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.requant_weight_ue8m0_inplace)Re-quantise

*weight*so that its per-block scaling factors are in the -
–[silu_mul_per_token_group_quant_fp8_colmajor](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.silu_mul_per_token_group_quant_fp8_colmajor)Gated activation + block-fp8 quant.

`alpha`

/`beta`

select the gate -
–[validate_fp8_block_shape](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.validate_fp8_block_shape)Validate block quantization shapes for tensor parallelism.

-
–[validate_fp8_block_shape_moe](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.validate_fp8_block_shape_moe)Validate fused MoE block quantization shapes for tensor parallelism.

-
–[w8a8_triton_block_scaled_mm](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.w8a8_triton_block_scaled_mm)This function performs matrix multiplication with block-wise


##

`_maybe_pad_fp8_weight(weight)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils._maybe_pad_fp8_weight)

Pad the weight tensor. This is an optimization on ROCm platform, which can benefit from tensors located far enough from one another in memory

## Source code in `vllm/model_executor/layers/quantization/utils/fp8_utils.py`


##

`_per_token_group_quant_fp8(y_ptr, y_q_ptr, y_s_ptr, group_size, y_num_columns, y_row_stride, eps, fp8_min, fp8_max, use_ue8m0, BLOCK)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils._per_token_group_quant_fp8)

A Triton-accelerated function to perform per-token-group quantization on a tensor. This function converts the tensor values into float8 values.

## Source code in `vllm/model_executor/layers/quantization/utils/fp8_utils.py`


##

`_per_token_group_quant_fp8_colmajor(y_ptr, y_q_ptr, y_s_ptr, group_size, y_num_columns, y_row_stride, y_s_col_stride, eps, fp8_min, fp8_max, use_ue8m0, BLOCK)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils._per_token_group_quant_fp8_colmajor)

A Triton-accelerated function to perform per-token-group quantization on a tensor. This function converts the tensor values into float8 values.

## Source code in `vllm/model_executor/layers/quantization/utils/fp8_utils.py`


##

`_silu_mul_per_token_group_quant_fp8_colmajor(y_ptr, y_q_ptr, y_s_ptr, M, N, y_s_col_stride, eps, clamp_limit, alpha, beta, fp8_min, fp8_max, use_ue8m0, HAS_CLAMP, GROUP_SIZE, BLOCK_M, BLOCK_N)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils._silu_mul_per_token_group_quant_fp8_colmajor)

Each thread block (BLOCK_N) computes [BLOCK_M, GROUP_SIZE] act-mul outputs. Then the thread block quantizes the [BLOCK_M, GROUP_SIZE] block of values and fills the outputs tensors at the right positions.

## Source code in `vllm/model_executor/layers/quantization/utils/fp8_utils.py`


|
|

##

`_upcast_e8m0_to_fp32(scale)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils._upcast_e8m0_to_fp32)

Upcast E8M0 (exponent-only) scale to float32.

E8M0 stores only the 8-bit biased exponent (bias=127). To convert to float32 we place those 8 bits into the exponent field of an IEEE-754 float32 (bits 23-30) with sign=0 and mantissa=0.

## Source code in `vllm/model_executor/layers/quantization/utils/fp8_utils.py`


##

`_w8a8_triton_block_scaled_mm(A, B, C, As, Bs, M, N, K, group_n, group_k, stride_am, stride_ak, stride_bk, stride_bn, stride_cm, stride_cn, stride_As_m, stride_As_k, stride_Bs_k, stride_Bs_n, BLOCK_SIZE_M, BLOCK_SIZE_N, BLOCK_SIZE_K, GROUP_SIZE_M)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils._w8a8_triton_block_scaled_mm)

Triton-accelerated function used to perform linear operations (dot product) on input tensors `A`

and `B`

with block-wise quantization, and store the result in output tensor `C`

.

## Source code in `vllm/model_executor/layers/quantization/utils/fp8_utils.py`


|
|

##

`create_fp8_input_scale(output_partition_sizes, weight_loader)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.create_fp8_input_scale)

Create input scale parameter for static activation quantization.

## Source code in `vllm/model_executor/layers/quantization/utils/fp8_utils.py`


##

`create_fp8_scale_parameter(parameter_type, output_partition_sizes, input_size_per_partition, block_size, weight_loader, scale_dtype=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.create_fp8_scale_parameter)

Create scale parameter based on quantization strategy.

## Source code in `vllm/model_executor/layers/quantization/utils/fp8_utils.py`


##

`create_fp8_weight_parameter(output_size_per_partition, input_size_per_partition, weight_loader)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.create_fp8_weight_parameter)

Create FP8 weight parameter.

## Source code in `vllm/model_executor/layers/quantization/utils/fp8_utils.py`


##

`get_fp8_block_weight_scale(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.get_fp8_block_weight_scale)

Return the block-FP8 weight scale for supported quant methods.

## Source code in `vllm/model_executor/layers/quantization/utils/fp8_utils.py`


##

`get_w8a8_block_fp8_configs(N, K, block_n, block_k)`

`cached`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.get_w8a8_block_fp8_configs)

Return optimized configurations for the w8a8 block fp8 kernel. The return value will be a dictionary that maps an irregular grid of batch sizes to configurations of the w8a8 block fp8 kernel. To evaluate the kernel on a given batch size bs, the closest batch size in the grid should be picked and the associated configuration chosen to invoke the kernel.

## Source code in `vllm/model_executor/layers/quantization/utils/fp8_utils.py`


##

`input_to_float8(x, dtype=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.input_to_float8)

This function quantizes input values to float8 values " "with tensor-wise quantization.

## Source code in `vllm/model_executor/layers/quantization/utils/fp8_utils.py`


##

`per_token_group_quant_fp8(x, group_size, eps=1e-10, dtype=None, column_major_scales=False, tma_aligned_scales=False, out_q=None, use_ue8m0=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.per_token_group_quant_fp8)

Function to perform per-token-group quantization on an input tensor `x`

. It converts the tensor values into signed float8 values and returns the quantized tensor along with the scaling factor used for quantization.

Parameters:

-

(`x`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.per_token_group_quant_fp8(x))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The input tensor with ndim >= 2.

-

(`group_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.per_token_group_quant_fp8(group_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)The group size used for quantization.

-

(`eps`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.per_token_group_quant_fp8(eps))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)`1e-10`

) –The minimum to avoid dividing zero.

-

(`dtype`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.per_token_group_quant_fp8(dtype))

, default:[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)| None`None`

) –The dtype of output tensor. Note that only

`torch.float8_e4m3fn`

is supported for now. -

(`column_major_scales`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.per_token_group_quant_fp8(column_major_scales))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Outputs scales in column major.

-

(`tma_aligned_scales`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.per_token_group_quant_fp8(tma_aligned_scales))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Outputs scales in TMA-aligned layout.

-

(`out_q`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.per_token_group_quant_fp8(out_q))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional output tensor. If not provided, function will create.

-

(`use_ue8m0`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.per_token_group_quant_fp8(use_ue8m0))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)| None`None`

) –If True, round each scale down to a power of two (UE8M0 format). None defers to the platform default.


Returns:

## Source code in `vllm/model_executor/layers/quantization/utils/fp8_utils.py`


|
|

##

`per_token_group_quant_fp8_packed_for_deepgemm(x, group_size, eps=1e-10, use_ue8m0=None, out_q=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.per_token_group_quant_fp8_packed_for_deepgemm)

FP8 per-token-group quantization for DeepGEMM.

Returns:

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)](x_q, x_s_packed) x_q: FP8 activations, same shape as

`x`

. x_s_packed: Int32 tensor with logical shape [mn, ceil(num_groups_per_row / 4)], laid out with TMA-aligned stride along the packed-K dimension

## Source code in `vllm/model_executor/layers/quantization/utils/fp8_utils.py`


##

`process_fp8_input_tensor_strategy_moe(w13_input_scale, w2_input_scale, enable_eplb)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.process_fp8_input_tensor_strategy_moe)

Process moe input scales for tensor-wise quantization strategy.

## Source code in `vllm/model_executor/layers/quantization/utils/fp8_utils.py`


##

`process_fp8_weight_block_strategy(weight, weight_scale)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.process_fp8_weight_block_strategy)

Process weights for block-wise quantization strategy.

## Source code in `vllm/model_executor/layers/quantization/utils/fp8_utils.py`


##

`process_fp8_weight_channel_strategy(weight, weight_scale, input_scale=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.process_fp8_weight_channel_strategy)

Process weights for channel-wise quantization strategy.

## Source code in `vllm/model_executor/layers/quantization/utils/fp8_utils.py`


##

`process_fp8_weight_tensor_strategy(weight, weight_scale, logical_widths, input_scale=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.process_fp8_weight_tensor_strategy)

Process weights for tensor-wise quantization strategy.

## Source code in `vllm/model_executor/layers/quantization/utils/fp8_utils.py`


##

`process_fp8_weight_tensor_strategy_moe(weight, weight_scales, shard_size, num_experts, is_act_and_mul=True)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.process_fp8_weight_tensor_strategy_moe)

Process moe weights for tensor-wise quantization strategy.

## Source code in `vllm/model_executor/layers/quantization/utils/fp8_utils.py`


##

`requant_weight_ue8m0_inplace(weight, weight_scale, block_size=(128, 128))`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.requant_weight_ue8m0_inplace)

Re-quantise *weight* so that its per-block scaling factors are in the UE8M0 (power-of-two) format expected by the new DeepGEMM kernels inplace.

Parameters:

-

(`weight`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.requant_weight_ue8m0_inplace(weight))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Block-quantised weight tensor stored in

`torch.float8_e4m3fn`

. Expected shape`(..., M, K)`

. -

(`weight_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.requant_weight_ue8m0_inplace(weight_scale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Corresponding per-block scale tensor (

`torch.float32`

) with shape`(..., M // block_size[0], K // block_size[1])`

. -

(`block_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.requant_weight_ue8m0_inplace(block_size))

, default:[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[int](https://docs.python.org/3/builtins/functions.html#int)]`(128, 128)`

) –2-element iterable

`[block_m, block_k]`

describing the block quantisation granularity.

## Source code in `vllm/model_executor/layers/quantization/utils/fp8_utils.py`


##

`silu_mul_per_token_group_quant_fp8_colmajor(input, output=None, use_ue8m0=None, eps=1e-10, clamp_limit=None, group_size=128, alpha=1.0, beta=0.0)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.silu_mul_per_token_group_quant_fp8_colmajor)

Gated activation + block-fp8 quant. `alpha`

/`beta`

select the gate (silu: alpha=1, beta=0; swigluoai: alpha, beta from config).

## Source code in `vllm/model_executor/layers/quantization/utils/fp8_utils.py`


##

`validate_fp8_block_shape(layer, input_size, output_size, input_size_per_partition, output_partition_sizes, block_size)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.validate_fp8_block_shape)

Validate block quantization shapes for tensor parallelism.

## Source code in `vllm/model_executor/layers/quantization/utils/fp8_utils.py`


##

`validate_fp8_block_shape_moe(intermediate_size_per_partition, block_size)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.validate_fp8_block_shape_moe)

Validate fused MoE block quantization shapes for tensor parallelism.

## Source code in `vllm/model_executor/layers/quantization/utils/fp8_utils.py`


##

`w8a8_triton_block_scaled_mm(A, B, As, Bs, block_size, output_dtype=torch.float16)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.w8a8_triton_block_scaled_mm)

This function performs matrix multiplication with block-wise quantization. It takes two input tensors `A`

and `B`

with scales `As`

and `Bs`

. The output is returned in the specified `output_dtype`

.

Parameters:

-

(`A`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.w8a8_triton_block_scaled_mm(A))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The input tensor, e.g., activation.

-

(`B`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.w8a8_triton_block_scaled_mm(B))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The input tensor, e.g., weight.

-

(`As`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.w8a8_triton_block_scaled_mm(As))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The per-token-group quantization scale for

`A`

. -

(`Bs`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.w8a8_triton_block_scaled_mm(Bs))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The per-block quantization scale for

`B`

. -

(`block_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.w8a8_triton_block_scaled_mm(block_size))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]The block size for per-block quantization. It should be 2-dim, e.g., [128, 128].

-

(`output_dtype`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.fp8_utils.w8a8_triton_block_scaled_mm(output_dtype))

, default:[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)`float16`

) –The dtype of the returned tensor.


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)torch.Tensor: The result of matmul.


## Source code in `vllm/model_executor/layers/quantization/utils/fp8_utils.py`


|
|