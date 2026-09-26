source: https://docs.vllm.ai/en/latest/api/vllm/lora/ops/triton_ops/lora_expand_fp8_op/
lastmod: 2026-09-24

#

`vllm.lora.ops.triton_ops.lora_expand_fp8_op`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.lora_expand_fp8_op)

Based on: Chen, L., Ye, Z., Wu, Y., Zhuo, D., Ceze, L., & Krishnamurthy, A. (2023). Punica: Multi-Tenant LoRA Serving. https://arxiv.org/abs/2310.18547

##

`_get_expand_lora_scale_ptr(lora_weights, device)`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.lora_expand_fp8_op._get_expand_lora_scale_ptr)

`_EXPAND_LORA_SCALE_PTR_DICT`

collects the required information during `profile_run`

, After this, it remains constant and subsequent usage is through LUT. Refer to: https://github.com/triton-lang/triton/blob/release/3.1.x/python/tutorials/08-grouped-gemm.py

## Source code in `vllm/lora/ops/triton_ops/lora_expand_fp8_op.py`


##

`_lora_expand_fp8(inputs, lora_b_weights, output_tensor, token_lora_mapping, token_indices_sorted_by_lora_ids, num_tokens_per_lora, lora_token_start_loc, lora_ids, no_lora_flag_cpu, num_active_loras, b_scale, a_scale=None, offset_start=0, add_inputs=False, group_k=0, group_n=0, use_fp8_w8a8=False, per_channel_quant=False)`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.lora_expand_fp8_op._lora_expand_fp8)

FP8-compatible LoRA expand operation.

Parameters:

-

(`inputs`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.lora_expand_fp8_op._lora_expand_fp8(inputs))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input tensor from shrink operation [num_slices, num_tokens, lora_rank]

-

(`lora_b_weights`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.lora_expand_fp8_op._lora_expand_fp8(lora_b_weights))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]List of FP8 LoRA B weights per slice

-

(`output_tensor`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.lora_expand_fp8_op._lora_expand_fp8(output_tensor))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Output tensor

-

(`a_scale`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.lora_expand_fp8_op._lora_expand_fp8(a_scale))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional scale for input (if input is quantized)

-

(`b_scale`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.lora_expand_fp8_op._lora_expand_fp8(b_scale))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]Weight quantization scales per slice

-

(`token_lora_mapping`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.lora_expand_fp8_op._lora_expand_fp8(token_lora_mapping))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Token to LoRA ID mapping

-

(`token_indices_sorted_by_lora_ids`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.lora_expand_fp8_op._lora_expand_fp8(token_indices_sorted_by_lora_ids))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Sorted token indices

-

(`num_tokens_per_lora`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.lora_expand_fp8_op._lora_expand_fp8(num_tokens_per_lora))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Number of tokens per LoRA

-

(`lora_token_start_loc`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.lora_expand_fp8_op._lora_expand_fp8(lora_token_start_loc))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Start location for each LoRA's tokens

-

(`lora_ids`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.lora_expand_fp8_op._lora_expand_fp8(lora_ids))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)LoRA IDs to process

-

(`num_active_loras`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.lora_expand_fp8_op._lora_expand_fp8(num_active_loras))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of active LoRAs. Accepted for API parity with the non-FP8 kernel and unused here.

-

(`no_lora_flag_cpu`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.lora_expand_fp8_op._lora_expand_fp8(no_lora_flag_cpu))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)A CPU tensor of size 1, that indicates if there are any requests that require LoRA.

-

(`offset_start`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.lora_expand_fp8_op._lora_expand_fp8(offset_start))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –Offset start for output_tensor. Defaults to 0.

-

(`add_inputs`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.lora_expand_fp8_op._lora_expand_fp8(add_inputs))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether to add the input tensor to the output tensor. Defaults to False.

-

(`group_k`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.lora_expand_fp8_op._lora_expand_fp8(group_k))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –Block size for K in block-wise quantization.

-

(`group_n`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.lora_expand_fp8_op._lora_expand_fp8(group_n))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –Block size for N in block-wise quantization.

-

(`use_fp8_w8a8`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.lora_expand_fp8_op._lora_expand_fp8(use_fp8_w8a8))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether to use FP8 W8A8 quantization.

-

(`per_channel_quant`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.lora_expand_fp8_op._lora_expand_fp8(per_channel_quant))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether to use per-channel quantization.


## Source code in `vllm/lora/ops/triton_ops/lora_expand_fp8_op.py`


|
|

##

`_lora_expand_kernel_fp8(input_ptr, lora_ptr, out_ptr, a_scale_ptr, b_scale_ptr, M, N, K, token_indices_sorted_by_lora_ids, num_tokens_per_lora, lora_token_start_loc, lora_ids, slice_start_loc, input_d0_stride, input_d1_stride, input_d2_stride, ls_d0_ptr, ls_d1_ptr, ls_d2_ptr, a_scale_m_stride, a_scale_k_stride, b_scale_l_stride, b_scale_n_stride, b_scale_k_stride, output_d0_stride, output_d1_stride, output_hs_ptr, group_n, group_k, BLOCK_M, BLOCK_N, BLOCK_K, EVEN_K, ADD_INPUTS, CAST_TYPE, SLICE_NUM, SAME_STRIDE, USE_GDC, use_fp8_w8a8, per_channel_quant, launch_pdl)`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.lora_expand_fp8_op._lora_expand_kernel_fp8)

FP8-compatible expand kernel wrapper.

## Source code in `vllm/lora/ops/triton_ops/lora_expand_fp8_op.py`


|
|