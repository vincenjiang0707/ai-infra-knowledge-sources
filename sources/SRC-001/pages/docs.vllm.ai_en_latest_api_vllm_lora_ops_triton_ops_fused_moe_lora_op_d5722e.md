source: https://docs.vllm.ai/en/latest/api/vllm/lora/ops/triton_ops/fused_moe_lora_op/
lastmod: 2026-09-24

#

`vllm.lora.ops.triton_ops.fused_moe_lora_op`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fused_moe_lora_op)

##

`_adjust_kernel_inputs(num_active_loras, sorted_token_ids, expert_ids)`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fused_moe_lora_op._adjust_kernel_inputs)

Helper function to adjust kernel inputs when sorted_token_ids is None.

## Source code in `vllm/lora/ops/triton_ops/fused_moe_lora_op.py`


##

`_fused_moe_lora_small_batch_kernel(x_ptr, A_ptrs, B_ptrs, out_ptr, topk_weights_ptr, expert_ids_ptr, token_lora_mapping_ptr, adapter_enabled_ptr, N, K, top_k_num, max_loras, work_total, pair_slices, stride_xm, stride_xk, stride_A_lora, stride_A_expert, stride_A_r, stride_A_k, stride_B_lora, stride_B_expert, stride_B_n, stride_B_r, stride_om, stride_on, slice_n_offset, n_tiles_per_program, n_chunks_per_pair_slice, token_mapping_factor, MUL_ROUTED_WEIGHT, ADD_INPUTS, BLOCK_R, actual_rank, BLOCK_N, BLOCK_K, NUM_SLICES, EVEN_K)`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fused_moe_lora_op._fused_moe_lora_small_batch_kernel)

Persistent fused MoE-LoRA kernel for naive_block_assignment inputs.

Each program owns one (pair × slice × n_chunk) work item. A "chunk" covers `n_tiles_per_program`

consecutive output-N tiles, all of which share a single shrink — so the rank-vector is computed once per program and the A weights for that (lora, expert, slice) are loaded once instead of n_tiles_per_program times.

The wrapper picks `n_tiles_per_program`

to keep the grid close to 2*SM_count: at very small batch (work_total ≤ SM_count) the chunk size collapses to 1 and behaviour matches a per-tile GEMV; as batch grows the chunk grows so we trade some N-axis parallelism for shrink reuse. When `work_total`

exceeds the launched grid, the outer stride loop drains the leftover work units serially.

## Source code in `vllm/lora/ops/triton_ops/fused_moe_lora_op.py`


|
|

##

`_get_expert_id(expert_ids_ptr, lora_id, pid_m, stride_el, max_loras, naive_block_assignment)`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fused_moe_lora_op._get_expert_id)

Returns expert_id.

## Source code in `vllm/lora/ops/triton_ops/fused_moe_lora_op.py`


##

`_get_lora_id(lora_ids, token_lora_mapping_ptr, lora_idx, pid_m, top_k_num, naive_block_assignment)`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fused_moe_lora_op._get_lora_id)

Returns lora_id.

## Source code in `vllm/lora/ops/triton_ops/fused_moe_lora_op.py`


##

`_get_ptr(lora_weights, device)`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fused_moe_lora_op._get_ptr)

`_LORA_PTR_DICT`

collects the required information during `profile_run`

, After this, it remains constant and subsequent usage is through LUT. Refer to: https://github.com/triton-lang/triton/blob/release/3.1.x/python/tutorials/08-grouped-gemm.py

## Source code in `vllm/lora/ops/triton_ops/fused_moe_lora_op.py`


##

`_get_token_offs(sorted_token_ids_ptr, lora_id, pid_m, offs, stride_tl, max_loras, num_valid_tokens, naive_block_assignment, BLOCK_SIZE_M)`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fused_moe_lora_op._get_token_offs)

Returns token offsets.

## Source code in `vllm/lora/ops/triton_ops/fused_moe_lora_op.py`


##

`_pick_small_batch_chunk(pair_slices, N_tiles, sm_count)`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fused_moe_lora_op._pick_small_batch_chunk)

Pick `n_tiles_per_program`

so the launched grid stays near 2*SM_count.

Sizes for occupancy first (more programs in flight → better latency hiding for the K-loop A/x loads). Once the per-tile grid already exceeds 2*SM_count we increase the chunk size to amortise the shrink cost — at that point the GPU is saturated by per-program work and packing more tiles per program lets the rank_vec be reused.

## Source code in `vllm/lora/ops/triton_ops/fused_moe_lora_op.py`


##

`_run_fused_moe_lora_one_shot(output, qcurr_hidden_states, lora_a_stacked, lora_b_stacked, topk_weights, sorted_token_ids, expert_ids, num_tokens_post_padded, token_lora_mapping, max_lora_rank, top_k_num, lora_ids, num_active_loras, adapter_enabled, mul_routed_weight, block_size_m, add_inputs=True)`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fused_moe_lora_op._run_fused_moe_lora_one_shot)

Fast-path wrapper: launches one fused shrink+expand kernel.

The shape contract matches `_fused_moe_lora`

. `output`

has shape `(num_tokens, top_k_num, num_slices * N_per_slice)`

. When `add_inputs=True`

(default) the kernel reads-modifies-writes `output`

in place; when `add_inputs=False`

the kernel overwrites `output`

with the LoRA delta only. The latter is used by the dual-stream path that sums LoRA into the base output on a separate stream.

## Source code in `vllm/lora/ops/triton_ops/fused_moe_lora_op.py`


|
|

##

`_run_fused_moe_lora_small_batch(output, qcurr_hidden_states, lora_a_stacked, lora_b_stacked, topk_weights, expert_ids_flat, token_lora_mapping, top_k_num, adapter_enabled, mul_routed_weight, add_inputs=True)`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fused_moe_lora_op._run_fused_moe_lora_small_batch)

Small-batch GEMV-style wrapper. Naive-block-assignment inputs only.

Shape contract matches `_run_fused_moe_lora_one_shot`

: `output`

is `(num_tokens, top_k_num, num_slices * N_per_slice)`

with contiguous-style strides, `expert_ids_flat`

is the flattened `topk_ids`

of shape `(num_tokens * top_k_num,)`

, and the rank-padded LoRA weights live in `lora_a_stacked`

/ `lora_b_stacked`

.

The kernel is persistent over (pair × slice × n_chunk) work items — each program does one shrink and reuses the rank vector across `n_tiles_per_program`

expand tiles. The chunk size scales with the pair-slice count so very small batches keep per-tile parallelism while medium batches cut redundant shrinks.

## Source code in `vllm/lora/ops/triton_ops/fused_moe_lora_op.py`


|
|