source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/fused_moe/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.fused_moe.fused_moe`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe)

Fused MoE Triton kernels.

Functions:

-
–[fused_experts](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe.fused_experts)Run fused MoE expert computation using Triton kernels.

-
–[fused_moe_kernel](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe.fused_moe_kernel)Implements the fused computation for a Mixture of Experts (MOE) using

-
–[fused_moe_kernel_gptq_awq](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe.fused_moe_kernel_gptq_awq)Implements the fused computation for a Mixture of Experts (MOE) using

-
–[get_moe_configs](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe.get_moe_configs)Return optimized configurations for the fused MoE kernel.


##

`_ensure_block_size_k_divisible(size_k, block_size_k, group_size)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe._ensure_block_size_k_divisible)

Ensure block_size_k is a divisor of size_k and divisible by group_size.

This ensures BLOCK_SIZE_K compatibility with MoeWNA16 CUDA kernel which requires size_k % BLOCK_SIZE_K == 0 and BLOCK_SIZE_K % group_size == 0.

Parameters:

-

(`size_k`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe._ensure_block_size_k_divisible(size_k))

) –[int](https://docs.python.org/3/builtins/functions.html#int)The size_k dimension that must be divisible by result.

-

(`block_size_k`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe._ensure_block_size_k_divisible(block_size_k))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Preferred block size (will be adjusted if needed).

-

(`group_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe._ensure_block_size_k_divisible(group_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)The result must be divisible by this.


Returns:

-

–[int](https://docs.python.org/3/builtins/functions.html#int)A valid BLOCK_SIZE_K that divides size_k and is divisible by group_size.


## Source code in `vllm/model_executor/layers/fused_moe/fused_moe.py`


##

`_get_config_quant_dtype(use_fp8_w8a8, use_int8_w8a8)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe._get_config_quant_dtype)

Get the quantization type based on the quantization strategy flags. We don't have a quant_config at this point so we need to work backwards. A return type of None means no quantization is required because the input is unquantized or has been quantized prior to calling fused_experts_impl.

## Source code in `vllm/model_executor/layers/fused_moe/fused_moe.py`


##

`_prepare_expert_assignment(topk_ids, config, num_tokens, top_k_num, global_num_experts, expert_map, *, use_int8_w8a16=False, use_int4_w4a16=False, block_shape=None, ignore_invalid_experts=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe._prepare_expert_assignment)

Prepare expert assignments for the aligned and low-latency Triton paths.

## Source code in `vllm/model_executor/layers/fused_moe/fused_moe.py`


##

`fused_experts(hidden_states, w1, w2, topk_weights, topk_ids, activation=MoEActivation.SILU, apply_router_weight_on_input=False, global_num_experts=-1, expert_map=None, quant_config=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe.fused_experts)

Run fused MoE expert computation using Triton kernels.

## Source code in `vllm/model_executor/layers/fused_moe/fused_moe.py`


##

`fused_moe_kernel(a_ptr, b_ptr, c_ptr, b_bias_ptr, a_scale_ptr, b_scale_ptr, topk_weights_ptr, sorted_token_ids_ptr, expert_ids_ptr, num_tokens_post_padded_ptr, N, K, EM, num_valid_tokens, stride_am, stride_ak, stride_be, stride_bk, stride_bn, stride_cm, stride_cn, stride_asm, stride_ask, stride_bse, stride_bsk, stride_bsn, stride_bbe, stride_bbn, group_n, group_k, naive_block_assignment, BLOCK_SIZE_M, BLOCK_SIZE_N, BLOCK_SIZE_K, GROUP_SIZE_M, SPLIT_K, MUL_ROUTED_WEIGHT, top_k, compute_type, use_fp8_w8a8, use_int8_w8a8, use_int8_w8a16, per_channel_quant, HAS_BIAS, SWAP_AB, USE_TD=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe.fused_moe_kernel)

Implements the fused computation for a Mixture of Experts (MOE) using token and expert matrices.

Key Parameters: - A: The input tensor representing tokens with shape (*, K), where '*' can be any shape representing batches and K is the feature dimension of each token. - B: The stacked MOE weight tensor with shape (E, N, K), where E is the number of experts, K is the input feature dimension, and N is the output feature dimension. - C: The output cache tensor with shape (M, topk, N), where M is the total number of tokens post padding, topk is the number of times each token is repeated, and N is the output feature dimension. - sorted_token_ids: A tensor containing the sorted indices of tokens, repeated topk times and arranged by the expert index they are assigned to. - expert_ids: A tensor containing the indices of the expert for each block. It determines which expert matrix from B should be used for each block in A. - naive_block_assignment: A boolean flag indicating whether to use naive token wise block assignment. If True, each block corresponds to a single token. This kernel performs the multiplication of a token by its corresponding expert matrix as determined by `expert_ids`

. The sorting of `sorted_token_ids`

by expert index and padding ensures divisibility by BLOCK_SIZE_M, which is necessary to maintain consistency in block matrix multiplication across different blocks processed by the same expert.

## Source code in `vllm/model_executor/layers/fused_moe/fused_moe.py`


|
|

##

`fused_moe_kernel_gptq_awq(a_ptr, b_ptr, c_ptr, b_scale_ptr, b_zp_ptr, topk_weights_ptr, sorted_token_ids_ptr, expert_ids_ptr, num_tokens_post_padded_ptr, N, K, EM, num_valid_tokens, stride_am, stride_ak, stride_be, stride_bk, stride_bn, stride_cm, stride_cn, stride_bse, stride_bsk, stride_bsn, stride_bze, stride_bzk, stride_bzn, block_k_diviable, group_size, BLOCK_SIZE_M, BLOCK_SIZE_N, BLOCK_SIZE_K, GROUP_SIZE_M, SPLIT_K, MUL_ROUTED_WEIGHT, top_k, compute_type, has_zp, use_int4_w4a16, use_int8_w8a16)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe.fused_moe_kernel_gptq_awq)

Implements the fused computation for a Mixture of Experts (MOE) using token and expert matrices.

Key Parameters: - A: The input tensor representing tokens with shape (*, K), where '*' can be any shape representing batches and K is the feature dimension of each token. - B: The stacked MOE weight tensor with shape (E, N, K), where E is the number of experts, K is the input feature dimension, and N is the output feature dimension. - C: The output cache tensor with shape (M, topk, N), where M is the total number of tokens post padding, topk is the number of times each token is repeated, and N is the output feature dimension. - sorted_token_ids: A tensor containing the sorted indices of tokens, repeated topk times and arranged by the expert index they are assigned to. - expert_ids: A tensor containing the indices of the expert for each block. It determines which expert matrix from B should be used for each block in A. This kernel performs the multiplication of a token by its corresponding expert matrix as determined by `expert_ids`

. The sorting of `sorted_token_ids`

by expert index and padding ensures divisibility by BLOCK_SIZE_M, which is necessary to maintain consistency in block matrix multiplication across different blocks processed by the same expert.

## Source code in `vllm/model_executor/layers/fused_moe/fused_moe.py`


|
|

##

`get_moe_configs(E, N, dtype, block_n=None, block_k=None)`

`cached`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe.get_moe_configs)

Return optimized configurations for the fused MoE kernel.

The return value will be a dictionary that maps an irregular grid of batch sizes to configurations of the fused_moe kernel. To evaluate the kernel on a given batch size bs, the closest batch size in the grid should be picked and the associated configuration chosen to invoke the kernel.

## Source code in `vllm/model_executor/layers/fused_moe/fused_moe.py`


|
|