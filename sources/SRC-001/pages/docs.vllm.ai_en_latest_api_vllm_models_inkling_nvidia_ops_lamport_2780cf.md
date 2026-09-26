source: https://docs.vllm.ai/en/latest/api/vllm/models/inkling/nvidia/ops/lamport/
lastmod: 2026-09-24

#

`vllm.models.inkling.nvidia.ops.lamport`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.lamport)

Deadlock-free fused RS + short-conv + AG + residual + RMSNorm.

The public integration surface is `LamportRSConv.rs_sconv_ag_add_norm`

.

### Liveness[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.lamport--liveness)

Large grids are deliberately split at the two communication dependencies:

`_publish_input_kernel`

only publishes rank partials.`_reduce_insert_kernel`

waits, reduces, and inserts the local shard.`_sconv_publish_kernel`

only computes and publishes the local result.`_gather_norm_kernel`

waits, gathers, and normalizes.

Without PDL, CUDA stream order completes a producer before its consumer. With PDL, every producer CTA posts all peer stores before triggering its dependent, and the consumer executes `gdc_wait`

before polling. A consumer therefore waits only for stores from a producer that is already running (or complete) on another GPU. It never waits for another block in its own grid. Consequently spinning consumers cannot occupy resources needed by any producer, and the wait-for graph has no cycle. The proof is independent of grid size, block dispatch order, and occupancy.

For one token, the first three phases use eight independent channel slices to expose enough CTA parallelism for decode latency. Each slice has exclusive ownership of its cache and Lamport columns; the gather/RMSNorm phase retains one CTA per token so no cross-CTA reduction or completion counter is needed.

Immediate buffer reuse (including replay of a captured CUDA graph) is also safe. Rank R cannot republish input for call n+1 until its gather for n has finished; that gather waited for owner O's output, which O publishes only after consuming R's input for n. Likewise, R cannot republish output for n+1 until its reduction for n+1 has observed destination D's input; D publishes that input only after its gather consumed R's output for n. Thus every prior read happens-before a same-slot rewrite. Three generations reduce incidental coupling for ordinary launches, but correctness does not depend on rotation.

The payload itself is the Lamport flag. A 32-bit store publishes two bf16s atomically; 0x80008000 (two negative zeroes) denotes an empty pair. Real negative zeroes are changed to positive zero before publication. Consumers use volatile 32-bit loads and restore the sentinel after consuming a slot.

Classes:

-
–[LamportRSConv](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.lamport.LamportRSConv)Persistent symmetric buffers for one TP group.


Functions:

-
–[get_lamport_rs_conv](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.lamport.get_lamport_rs_conv)Return the state initialized with the model, or

`None`

for fallback. -
–[initialize_lamport_rs_conv](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.lamport.initialize_lamport_rs_conv)Collectively initialize the TP-group state during model construction.


##

`LamportRSConv`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.lamport.LamportRSConv)

Persistent symmetric buffers for one TP group.

Methods:

-
–[rs_sconv_ag_add_norm](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.lamport.LamportRSConv.rs_sconv_ag_add_norm)Return

`(normed | None, new_residual)`

, both shaped`[T, 6144]`

.

## Source code in `vllm/models/inkling/nvidia/ops/lamport.py`


|
|

###

`_initialize_lamport_buffers()`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.lamport.LamportRSConv._initialize_lamport_buffers)

Arm every slot and collectively verify the exact sentinel bits.

Do not replace this with a zero-fill: Lamport readiness distinguishes the bf16 bit pattern for -0.0 (0x8000) from every published payload. The validation is deliberately collective so one rank cannot enter the first polling kernel while another rank still has an unarmed buffer.

## Source code in `vllm/models/inkling/nvidia/ops/lamport.py`


###

`_initialize_mnnvl_buffers()`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.lamport.LamportRSConv._initialize_mnnvl_buffers)

Initialize and validate FlashInfer fabric-mapped Lamport storage.

## Source code in `vllm/models/inkling/nvidia/ops/lamport.py`


###

`rs_sconv_ag_add_norm(input_tensor, residual, conv_weight, norm_weight, eps, cache, positions, block_table, seq_idx, slot_mapping, off_s, ws, block_size, shared_tensor=None)`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.lamport.LamportRSConv.rs_sconv_ag_add_norm)

Return `(normed | None, new_residual)`

, both shaped `[T, 6144]`

.

## Source code in `vllm/models/inkling/nvidia/ops/lamport.py`


|
|

##

`_gather_norm_kernel(output_peer_ptrs, output_peer_offset_u32, norm_weight_ptr, normed_ptr, residual_out_ptr, eps, stride_output_t, C, C_P2, RANK, HAS_NORM, USE_PDL, launch_pdl)`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.lamport._gather_norm_kernel)

Consume a complete row; one CTA owns all outputs for one token.

## Source code in `vllm/models/inkling/nvidia/ops/lamport.py`


##

`_pack_bf16_pairs(values)`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.lamport._pack_bf16_pairs)

Pack bf16 values into atomic u32 pairs and reserve negative zero.

## Source code in `vllm/models/inkling/nvidia/ops/lamport.py`


##

`_publish_input_kernel(stage_ptr, shared_ptr, peer_ptrs, peer_offset_u32, stride_stage_t, stride_shared_t, C, CS, CS_P2, SPLITS, RANK, WORLD, HAS_SHARED, USE_PDL, launch_pdl)`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.lamport._publish_input_kernel)

Publish this rank's full partial row into every shard owner's slots.

## Source code in `vllm/models/inkling/nvidia/ops/lamport.py`


##

`_reduce_insert_kernel(input_peer_ptrs, input_peer_offset_u32, cache_ptr, slot_ptr, stride_cache_block, stride_cache_head, stride_cache_token, stride_cache_dim, block_size, C, CS, CS_P2, SPLITS, HEAD_SIZE, CACHE_OFFSET, RANK, WORLD, USE_PDL, launch_pdl)`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.lamport._reduce_insert_kernel)

Consume all partials for this rank and insert the reduced cache row.

## Source code in `vllm/models/inkling/nvidia/ops/lamport.py`


##

`_sconv_publish_kernel(peer_ptrs, peer_offset_u32, residual_ptr, weight_ptr, cache_ptr, position_ptr, sequence_ptr, slot_ptr, block_table_ptr, stride_residual_t, stride_cache_block, stride_cache_head, stride_cache_token, stride_cache_dim, stride_block_table_r, max_blocks, block_size, C, CS, CS_P2, SPLITS, HEAD_SIZE, CACHE_OFFSET, RANK, WORLD, WINDOW, USE_PDL, launch_pdl)`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.lamport._sconv_publish_kernel)

Compute this rank's shard, then publish it to every rank.

## Source code in `vllm/models/inkling/nvidia/ops/lamport.py`


|
|

##

`_validate_lamport_init_kernel(input_peer_ptrs, output_peer_ptrs, bad_ptr, num_pairs, RANK, BLOCK)`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.lamport._validate_lamport_init_kernel)

Validate both complete local allocations through their fabric pointers.

## Source code in `vllm/models/inkling/nvidia/ops/lamport.py`


##

`get_lamport_rs_conv(hidden_size, window_size)`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.lamport.get_lamport_rs_conv)

Return the state initialized with the model, or `None`

for fallback.

## Source code in `vllm/models/inkling/nvidia/ops/lamport.py`


##

`initialize_lamport_rs_conv(hidden_size, window_size, max_num_batched_tokens)`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.lamport.initialize_lamport_rs_conv)

Collectively initialize the TP-group state during model construction.