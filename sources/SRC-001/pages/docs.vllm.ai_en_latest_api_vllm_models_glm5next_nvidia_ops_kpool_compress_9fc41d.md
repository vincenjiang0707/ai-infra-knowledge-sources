source: https://docs.vllm.ai/en/latest/api/vllm/models/glm5next/nvidia/ops/kpool_compress/
lastmod: 2026-09-24

#

`vllm.models.glm5next.nvidia.ops.kpool_compress`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress)

kpool (key-pooling) Triton kernels for the sparse-attention indexer.

The cache stores POOLS (1 entry per `pool_size`

consecutive tokens) rather than individual tokens. `compress_ratio == pool_size`

on the kv_cache_spec makes the metadata builder emit pool-granular slot_mapping / seq_lens / cu_seq_lens / page_table for free; this file supplies the compress-write kernel (replacing `indexer_k_quant_and_cache`

) and the pool-level topk helpers (select pools -> expand to tokens -> append tail).

Functions:

-
–[append_tail_to_topk](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.append_tail_to_topk)Append non-pooled tail tokens after expanded history tokens.

-
–[expand_pools_and_append_tail](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.expand_pools_and_append_tail)Fuse

`expand_pools_to_tokens`

+`append_tail_to_topk`

(identity path). -
–[expand_pools_to_tokens](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.expand_pools_to_tokens)Expand selected full-pool ids to a strict-width token topk tensor.

-
–[fwht128_quant_fp8](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.fwht128_quant_fp8)Rotate each 128-wide row by the Hadamard-128 transform, then FP8-quant.

-
–[history_group_budget_for_topk](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.history_group_budget_for_topk)Number of pools to select so that expanding yields

`topk`

tokens. -
–[kpool_compress_and_write_cache](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.kpool_compress_and_write_cache)Compress

`pool_size`

tokens into one fp8 K and write at`loc`

. -
–[kpool_decode_update_and_maybe_write_cache_batched](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.kpool_decode_update_and_maybe_write_cache_batched)Batched decode-step kpool update for spec verify (

`next_n > 1`

). -
–[kpool_seed_tail_cache](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.kpool_seed_tail_cache)Seed the paged tail cache from a prefill batch (see the kernel).


##

`_fwht_quant_kernel(q_ptr, qout_ptr, sout_ptr, n_rows, BLOCK_R)`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress._fwht_quant_kernel)

Fused Hadamard-128 rotation + per-row absmax FP8 (ue8m0) quant.

Each row uses fp32 butterflies and scaling, rounds to bf16, then applies absmax quantization with a power-of-two scale.

## Source code in `vllm/models/glm5next/nvidia/ops/kpool_compress.py`


##

`_kpool_decode_update_batched_kernel(buf_fp8_ptr, buf_fp32_ptr, tail_kv_ptr, tail_slot_mapping_ptr, key_ptr, key_stride_b, key_stride_t, slot_score_ptr, ss_stride_b, ss_stride_t, ape_ptr, ape_stride_0, slot_mapping_ptr, positions_ptr, NEXT_N, PAGE_SIZE, BUF_NUMEL_PER_PAGE, POOL_SIZE, TAIL_BLOCK_ELEMS, KPOOL_HEAD, HEAD_DIM, S_OFFSET_NBYTES_IN_PAGE, ROUND_SCALE, BLOCK_D)`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress._kpool_decode_update_batched_kernel)

One program per request; iterates its NEXT_N verify tokens in order.

Replaces the caller's per-token sequential launch loop. The intra-request iteration MUST stay in position order: a pool-completion at token t* reads the tail-ring slots that tokens t < t* (same request) just stashed in this same invocation. `tl.range`

iterates sequentially within the program, so those stashes are visible to the later completion read. Cross-request programs are independent (distinct tail blocks). With NEXT_N < POOL_SIZE (the spec-verify case: NEXT_N ~= num_spec+1, POOL_SIZE=16) at most one completion can occur per request per call, but the ordered loop is correct for any NEXT_N.

## Source code in `vllm/models/glm5next/nvidia/ops/kpool_compress.py`


|
|

##

`_kpool_softmax_rotate_write_cache_kernel(buf_fp8_ptr, buf_fp32_ptr, slot_k_ptr, slot_score_ptr, ape_ptr, loc_ptr, write_mask_ptr, compressed_k_ptr, compressed_scale_ptr, slot_k_stride_0, slot_k_stride_1, slot_score_stride_0, slot_score_stride_1, ape_stride_0, PAGE_SIZE, BUF_NUMEL_PER_PAGE, POOL_SIZE, HEAD_DIM, S_OFFSET_NBYTES_IN_PAGE, ROUND_SCALE, HAS_WRITE_MASK, RETURN_COMPRESSED, WRITE_CACHE, BLOCK_D)`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress._kpool_softmax_rotate_write_cache_kernel)

One program per pool. softmax(slot_score+ape)-weighted sum of slot_k -> Hadamard-128 -> per-vector fp8 absmax quant -> write to cache at `loc`

.

## Source code in `vllm/models/glm5next/nvidia/ops/kpool_compress.py`


|
|

##

`_kpool_tail_seed_kernel(key_ptr, score_ptr, tslot_ptr, tail_ptr, n_tokens, TAIL_BLOCK_ELEMS, KPOOL_HEAD, HEAD_DIM, KPOOL, BLOCK_D)`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress._kpool_tail_seed_kernel)

Copy token `i`

's raw K + gate into its request's tail block.

Token `i`

is among its request's last KPOOL tokens iff the token KPOOL ahead belongs to a different tail block (or is past the batch / padding, slot < 0). `tslot = block * KPOOL + pos % KPOOL`

; the destination is `tail[block, {0:K, 1:score}, pos % KPOOL, :]`

.

The tail cache aliases the indexer cache with the indexer's (padded) block stride, so blocks are addressed through `TAIL_BLOCK_ELEMS`

/ `KPOOL_HEAD`

(`tail.stride(0)`

/ `tail.stride(1)`

), never as a dense `[num_blocks, 2, KPOOL, HEAD_DIM]`

array.

## Source code in `vllm/models/glm5next/nvidia/ops/kpool_compress.py`


##

`append_tail_to_topk(topk_result, seq_lens, pool_lens, pool_size, page_table=None, topk_offsets=None)`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.append_tail_to_topk)

Append non-pooled tail tokens after expanded history tokens.

`index_kpool_always_select_tail`

keeps the (incomplete) trailing pool so the most recent tokens are always attended to.

## Source code in `vllm/models/glm5next/nvidia/ops/kpool_compress.py`


##

`expand_pools_and_append_tail(pool_ids, seq_lens, pool_size)`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.expand_pools_and_append_tail)

Fuse `expand_pools_to_tokens`

+ `append_tail_to_topk`

(identity path).

Produces the same `[rows, topk + pool_size - 1]`

int32 output as calling the two functions in sequence when neither `page_table`

nor `topk_offsets`

is passed — the only path used by the GLM-5.3-Flash indexer. The kernel derives `pool_len = seq_len // pool_size`

internally, so the caller no longer needs to precompute it. Replaces ~25 elementwise kernels with one Triton launch.

## Source code in `vllm/models/glm5next/nvidia/ops/kpool_compress.py`


##

`expand_pools_to_tokens(group_ids, group_valid, topk, pool_size, page_table=None, topk_offsets=None)`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.expand_pools_to_tokens)

Expand selected full-pool ids to a strict-width token topk tensor.

## Source code in `vllm/models/glm5next/nvidia/ops/kpool_compress.py`


##

`fwht128_quant_fp8(q)`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.fwht128_quant_fp8)

Rotate each 128-wide row by the Hadamard-128 transform, then FP8-quant.

The fused kernel avoids materializing the rotated tensor and uses an exact fp32 `1 / sqrt(128)`

scale before block-128 ue8m0 quantization.

Parameters:

Returns:

## Source code in `vllm/models/glm5next/nvidia/ops/kpool_compress.py`


##

`history_group_budget_for_topk(topk, pool_size)`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.history_group_budget_for_topk)

Number of pools to select so that expanding yields `topk`

tokens.

##

`kpool_compress_and_write_cache(kv_cache, slot_k, slot_score, ape, loc, pool_size, head_dim=INDEX_HEAD_DIM, write_mask=None, round_scale=True, return_compressed=False, write_cache=True)`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.kpool_compress_and_write_cache)

Compress `pool_size`

tokens into one fp8 K and write at `loc`

.

Parameters:

-

(`kv_cache`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.kpool_compress_and_write_cache(kv_cache))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)indexer K cache

`[num_blocks, block_size, head_dim+4]`

uint8. -

(`slot_k`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.kpool_compress_and_write_cache(slot_k))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`[n_pools, pool_size, head_dim]`

bf16 — raw per-token K. -

(`slot_score`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.kpool_compress_and_write_cache(slot_score))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`[n_pools, pool_size, head_dim]`

— per-token gate score. -

(`ape`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.kpool_compress_and_write_cache(ape))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`[pool_size, head_dim]`

fp32 — per-slot position bias. -

(`loc`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.kpool_compress_and_write_cache(loc))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`[n_pools]`

int64 — flat physical slot per pool. -

(`pool_size`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.kpool_compress_and_write_cache(pool_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of tokens compressed into one cache entry.

-

(`head_dim`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.kpool_compress_and_write_cache(head_dim))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`INDEX_HEAD_DIM`

) –Indexer head dimension.

-

(`write_mask`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.kpool_compress_and_write_cache(write_mask))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –`[n_pools]`

bool — pools to write, or None for all. -

(`round_scale`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.kpool_compress_and_write_cache(round_scale))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –Round each fp8 scale down to a power of two.

-

(`return_compressed`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.kpool_compress_and_write_cache(return_compressed))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Also return the compressed K and scales.

-

(`write_cache`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.kpool_compress_and_write_cache(write_cache))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –Write the compressed result into

`kv_cache`

.

## Source code in `vllm/models/glm5next/nvidia/ops/kpool_compress.py`


|
|

##

`kpool_decode_update_and_maybe_write_cache_batched(kv_cache, tail_kv_cache, tail_slot_mapping, key, slot_score, ape, slot_mapping, positions, pool_size, head_dim=INDEX_HEAD_DIM, round_scale=True)`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.kpool_decode_update_and_maybe_write_cache_batched)

Batched decode-step kpool update for spec verify (`next_n > 1`

).

One launch replaces the caller's per-token loop. Inputs are grouped per request: `[num_requests, next_n, ...]`

. Each program handles one request's `next_n`

tokens in position order (see the kernel docstring for why ordering is required for pool-completion correctness).

Plain decode (`next_n == 1`

) is handled here too — the kernel collapses to a single-iteration loop.

Parameters:

-

(`kv_cache`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.kpool_decode_update_and_maybe_write_cache_batched(kv_cache))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)indexer K cache

`[num_blocks, block_size, head_dim+4]`

uint8. -

(`tail_kv_cache`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.kpool_decode_update_and_maybe_write_cache_batched(tail_kv_cache))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)paged tail cache

`[num_blocks, 2, pool_size, head_dim]`

bf16 (K at half 0, gate score at half 1). -

(`tail_slot_mapping`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.kpool_decode_update_and_maybe_write_cache_batched(tail_slot_mapping))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`[num_requests, next_n]`

int32. -

(`key`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.kpool_decode_update_and_maybe_write_cache_batched(key))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`[num_requests, next_n, head_dim]`

bf16. -

(`slot_score`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.kpool_decode_update_and_maybe_write_cache_batched(slot_score))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`[num_requests, next_n, head_dim]`

bf16. -

(`ape`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.kpool_decode_update_and_maybe_write_cache_batched(ape))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`[pool_size, head_dim]`

fp32. -

(`slot_mapping`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.kpool_decode_update_and_maybe_write_cache_batched(slot_mapping))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`[num_requests, next_n]`

int32. -

(`positions`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.kpool_decode_update_and_maybe_write_cache_batched(positions))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`[num_requests, next_n]`

int32. -

(`pool_size`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.kpool_decode_update_and_maybe_write_cache_batched(pool_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of tokens compressed into one cache entry.

-

(`head_dim`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.kpool_decode_update_and_maybe_write_cache_batched(head_dim))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`INDEX_HEAD_DIM`

) –Indexer head dimension.

-

(`round_scale`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.kpool_decode_update_and_maybe_write_cache_batched(round_scale))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –Round each fp8 scale down to a power of two.


## Source code in `vllm/models/glm5next/nvidia/ops/kpool_compress.py`


|
|

##

`kpool_seed_tail_cache(tail_kv_cache, key, gate_score, tslot, kpool, head_dim=INDEX_HEAD_DIM)`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.kpool_compress.kpool_seed_tail_cache)

Seed the paged tail cache from a prefill batch (see the kernel).