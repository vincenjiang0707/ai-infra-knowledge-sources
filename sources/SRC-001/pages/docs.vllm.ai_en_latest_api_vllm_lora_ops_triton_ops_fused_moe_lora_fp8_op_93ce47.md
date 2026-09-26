source: https://docs.vllm.ai/en/latest/api/vllm/lora/ops/triton_ops/fused_moe_lora_fp8_op/
lastmod: 2026-09-24

#

`vllm.lora.ops.triton_ops.fused_moe_lora_fp8_op`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fused_moe_lora_fp8_op)

##

`_adjust_kernel_inputs(num_active_loras, sorted_token_ids, expert_ids)`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fused_moe_lora_fp8_op._adjust_kernel_inputs)

Helper function to adjust kernel inputs when sorted_token_ids is None.

## Source code in `vllm/lora/ops/triton_ops/fused_moe_lora_fp8_op.py`


##

`_get_expert_id(expert_ids_ptr, lora_id, pid_m, stride_el, max_loras, naive_block_assignment)`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fused_moe_lora_fp8_op._get_expert_id)

Returns expert_id.

## Source code in `vllm/lora/ops/triton_ops/fused_moe_lora_fp8_op.py`


##

`_get_lora_id(lora_ids, token_lora_mapping_ptr, lora_idx, pid_m, top_k_num, naive_block_assignment)`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fused_moe_lora_fp8_op._get_lora_id)

Returns lora_id.

## Source code in `vllm/lora/ops/triton_ops/fused_moe_lora_fp8_op.py`


##

`_get_ptr(lora_weights, device)`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fused_moe_lora_fp8_op._get_ptr)

`_LORA_PTR_DICT`

collects the required information during `profile_run`

, After this, it remains constant and subsequent usage is through LUT. Refer to: https://github.com/triton-lang/triton/blob/release/3.1.x/python/tutorials/08-grouped-gemm.py

## Source code in `vllm/lora/ops/triton_ops/fused_moe_lora_fp8_op.py`


##

`_get_token_offs(sorted_token_ids_ptr, lora_id, pid_m, offs, stride_tl, max_loras, num_valid_tokens, naive_block_assignment, BLOCK_SIZE_M)`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fused_moe_lora_fp8_op._get_token_offs)

Returns token offsets.