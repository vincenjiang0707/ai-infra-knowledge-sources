source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/attention/dsa/sparse_mqa_logits/
lastmod: 2026-09-23

#

`vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits)

DeepGEMM sparse MQA-logits path for the DeepSeek V4.1 two-level indexer.

The candidate-source indexer publishes the top candidate blocks (in units of `candidate_block_size`

compressed positions). Instead of scoring every KV position and masking the dense logits down to those blocks, this path scores only the candidate tokens with DeepGEMM's sparse MQA logits kernels (`fp8_fp4_(paged_)sparse_mqa_logits`

, DeepGEMM >= 2.8, SM100 only), runs DeepSelect's top-k directly on the bf16 logits they produce, and remaps the selected columns back to request-local positions.

Only the MXFP4 indexer cache is supported: the kernels require UE8M0-packed (granularity-32) Q/KV scales, which is exactly the MXFP4 cache layout. The FP8 indexer cache stores one fp32 scale per quant block instead.

The functions here take caller-owned output buffers (`sparse_indices`

, `end`

, `col_indices`

) so the hot path allocates nothing; the indexer metadata builder owns them.

Functions:

-
–[candidate_blocks_to_sparse_indices](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.candidate_blocks_to_sparse_indices)Expand request-local candidate blocks into DeepGEMM sparse block ids.

-
–[check_deep_select_layout](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.check_deep_select_layout)Raise unless DeepSelect accepts the sparse logits layout.

-
–[has_deep_select](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.has_deep_select)Whether the DeepSelect top-k extension is built and this GPU runs it.

-
–[pick_sparse_block_kv](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.pick_sparse_block_kv)Largest sparse-block size (tokens) dividing the candidate block size.

-
–[sparse_mqa_logits_paged_decode](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_paged_decode)Sparse-MQA logits + top-k for paged decode rows.

-
–[sparse_mqa_logits_prefill_chunk](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_prefill_chunk)Sparse-MQA logits + top-k for one prefill chunk (packed KV workspace).

-
–[sparse_topk_remap](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_topk_remap)Row top-k over sparse logits, remapped to request-local positions.


##

`_expand_candidates_kernel(cand_ptr, cand_stride, ks_ptr, ks_stride, ke_ptr, ke_stride, si_ptr, si_stride, end_ptr, end_stride, K, S, RATIO, SBK)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits._expand_candidates_kernel)

One program per row: expand + filter + sort candidate blocks.

Each row's valid sparse blocks come out sorted ascending (no dedup pass: production candidates are unique, and the kernel tolerates repeats), padded by repeating the last valid block — DeepGEMM's padding convention. `end`

counts valid sparse-token columns; valid columns form a prefix because block ids are sorted.

## Source code in `vllm/model_executor/kernels/attention/dsa/sparse_mqa_logits.py`


##

`_sparse_topk_remap_kernel(col_ptr, col_stride, si_ptr, si_stride, ks_ptr, ks_stride, out_ptr, out_stride, k, SBK, K_POW2)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits._sparse_topk_remap_kernel)

Remap sparse top-k columns to request-local positions.

Column `j * SBK + o`

scores the token at `(si[row, j] - ks // SBK) * SBK + o`

; -1 columns stay -1.

## Source code in `vllm/model_executor/kernels/attention/dsa/sparse_mqa_logits.py`


##

`candidate_blocks_to_sparse_indices(candidate_blocks, row_ks, row_ke, candidate_block_size, sparse_block_kv, out=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.candidate_blocks_to_sparse_indices)

Expand request-local candidate blocks into DeepGEMM sparse block ids.

Parameters:

-

(`candidate_blocks`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.candidate_blocks_to_sparse_indices(candidate_blocks))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[rows, K] int32 request-local candidate block ids (-1 padded), in units of

`candidate_block_size`

positions. K must be a power of two (the in-kernel sort); rows may be strided. -

(`row_ks`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.candidate_blocks_to_sparse_indices(row_ks))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[rows] int32 per-row K range start; bounds are in the same (packed-workspace) coordinates the sparse kernel iterates over. Pass zeros for the paged path, whose blocks are context-relative.

-

(`row_ke`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.candidate_blocks_to_sparse_indices(row_ke))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[rows] int32 per-row K range end, in the same coordinates as

`row_ks`

. -

(`candidate_block_size`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.candidate_blocks_to_sparse_indices(candidate_block_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Positions per candidate block.

-

(`sparse_block_kv`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.candidate_blocks_to_sparse_indices(sparse_block_kv))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Positions per sparse block (8 or 16).

-

(`out`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.candidate_blocks_to_sparse_indices(out))

, default:[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)] | None`None`

) –Optional

`(sparse_indices, end)`

buffers to write into, shaped [rows, K * ratio] and [rows], both int32.

Returns:

-
(`sparse_indices`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[rows, K * ratio] int32 block ids for DeepGEMM, sorted ascending per row with the valid prefix first (unique in production, where candidates are unique) and the remaining slots repeating the last valid block (the kernel's padding convention). With the unaligned-ks variant, block

`i`

starts at`i * sparse_block_kv + ks % sparse_block_kv`

. -
(`end`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[rows] int32 count of valid sparse-token columns; valid columns always form a prefix because the block ids are sorted.


## Source code in `vllm/model_executor/kernels/attention/dsa/sparse_mqa_logits.py`


##

`check_deep_select_layout(num_sparse_cols, topk_tokens)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.check_deep_select_layout)

Raise unless DeepSelect accepts the sparse logits layout.

The sparse kernels return contiguous bf16 `[rows, num_sparse_cols]`

logits and the top-k writes int32 `[rows, topk_tokens]`

indices; DeepSelect needs both row strides aligned (1024B / 32B on SM100).

## Source code in `vllm/model_executor/kernels/attention/dsa/sparse_mqa_logits.py`


##

`has_deep_select()`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.has_deep_select)

Whether the DeepSelect top-k extension is built and this GPU runs it.

## Source code in `vllm/model_executor/kernels/attention/dsa/sparse_mqa_logits.py`


##

`pick_sparse_block_kv(candidate_block_size)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.pick_sparse_block_kv)

Largest sparse-block size (tokens) dividing the candidate block size.

## Source code in `vllm/model_executor/kernels/attention/dsa/sparse_mqa_logits.py`


##

`sparse_mqa_logits_paged_decode(q, q_scale, kv_cache, weights, context_lens, block_table, row_indices, candidate_blocks, candidate_block_size, sparse_block_kv, topk_tokens, topk_indices, *, row_ks, sparse_indices, end, col_indices, kernel_metadata=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_paged_decode)

Sparse-MQA logits + top-k for paged decode rows.

Every query is one row (spec-decode rows are flattened by the metadata builder), so `block_table`

is already per row.

Parameters:

-

(`q`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_paged_decode(q))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[rows, 1, H, D] packed Q values (MXFP4 viewed as int8).

-

(`q_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_paged_decode(q_scale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[rows, 1, H] int32 packed UE8M0 Q scales.

-

(`kv_cache`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_paged_decode(kv_cache))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)4D [num_pages, page_kv, 1, head_bytes] uint8 fused cache view; the page stride must be 512B-aligned.

-

(`weights`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_paged_decode(weights))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[rows, H] bf16 per-head weights.

-

(`context_lens`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_paged_decode(context_lens))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[rows] int32 per-row (compressed) context lengths.

-

(`block_table`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_paged_decode(block_table))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[rows, P] int32 per-row page table,

`stride(-1) == 1`

. -

(`row_indices`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_paged_decode(row_indices))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[rows] int32 row -> request map (pairing only affects scheduling).

-

(`candidate_blocks`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_paged_decode(candidate_blocks))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[rows, K] int32 candidate block ids.

-

(`candidate_block_size`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_paged_decode(candidate_block_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Positions per candidate block.

-

(`sparse_block_kv`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_paged_decode(sparse_block_kv))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Positions per sparse block (8 or 16).

-

(`topk_tokens`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_paged_decode(topk_tokens))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of tokens to keep per row.

-

(`topk_indices`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_paged_decode(topk_indices))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[rows, topk_tokens] output buffer.

-

(`row_ks`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_paged_decode(row_ks))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[rows] int32 zeros (paged blocks are context-relative).

-

(`sparse_indices`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_paged_decode(sparse_indices))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Caller-owned scratch.

-

(`end`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_paged_decode(end))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Caller-owned scratch.

-

(`col_indices`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_paged_decode(col_indices))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Caller-owned scratch.

-

(`kernel_metadata`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_paged_decode(kernel_metadata))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –See

`sparse_mqa_logits_prefill_chunk`

.

Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The DeepGEMM schedule metadata used, for reuse by later layers.


## Source code in `vllm/model_executor/kernels/attention/dsa/sparse_mqa_logits.py`


|
|

##

`sparse_mqa_logits_prefill_chunk(q, q_scale, k_quant, k_scale, weights, cu_seqlen_ks, cu_seqlen_ke, candidate_blocks, candidate_block_size, sparse_block_kv, topk_tokens, topk_indices, *, sparse_indices, end, col_indices, kernel_metadata=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_prefill_chunk)

Sparse-MQA logits + top-k for one prefill chunk (packed KV workspace).

Parameters:

-

(`q`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_prefill_chunk(q))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[rows, H, D] packed Q values (MXFP4 viewed as int8).

-

(`q_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_prefill_chunk(q_scale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[rows, H] int32 packed UE8M0 Q scales.

-

(`k_quant`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_prefill_chunk(k_quant))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[total_kv, D] packed K workspace (MXFP4 viewed as int8).

-

(`k_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_prefill_chunk(k_scale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[total_kv] int32 packed UE8M0 K scales.

-

(`weights`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_prefill_chunk(weights))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[rows, H] bf16 per-head weights; the sparse kernels take bf16 and do not fold the Q scale in.

-

(`cu_seqlen_ks`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_prefill_chunk(cu_seqlen_ks))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[rows] int32 per-token K start bounds in the packed workspace.

-

(`cu_seqlen_ke`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_prefill_chunk(cu_seqlen_ke))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[rows] int32 per-token K end bounds in the packed workspace.

-

(`candidate_blocks`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_prefill_chunk(candidate_blocks))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[rows, K] int32 request-local candidate block ids.

-

(`candidate_block_size`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_prefill_chunk(candidate_block_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Positions per candidate block.

-

(`sparse_block_kv`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_prefill_chunk(sparse_block_kv))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Positions per sparse block (8 or 16).

-

(`topk_tokens`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_prefill_chunk(topk_tokens))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of tokens to keep per row.

-

(`topk_indices`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_prefill_chunk(topk_indices))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[rows, topk_tokens] output buffer.

-

(`sparse_indices`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_prefill_chunk(sparse_indices))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Caller-owned scratch, see

`candidate_blocks_to_sparse_indices`

. -

(`end`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_prefill_chunk(end))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Caller-owned scratch, see

`candidate_blocks_to_sparse_indices`

. -

(`col_indices`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_prefill_chunk(col_indices))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Caller-owned scratch, see

`sparse_topk_remap`

. -

(`kernel_metadata`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_mqa_logits_prefill_chunk(kernel_metadata))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –DeepGEMM schedule from a previous call with the same candidates and bounds (i.e. another indexer layer in the same step). When given, the candidate expansion is skipped and

`sparse_indices`

/`end`

are assumed to be up to date.

Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The DeepGEMM schedule metadata used, for reuse by later layers.


## Source code in `vllm/model_executor/kernels/attention/dsa/sparse_mqa_logits.py`


|
|

##

`sparse_topk_remap(logits, sparse_indices, end, row_ks, sparse_block_kv, topk_tokens, topk_indices, *, col_indices)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_topk_remap)

Row top-k over sparse logits, remapped to request-local positions.

Column `j * sparse_block_kv + o`

of `logits`

scores the token at request-local position `(sparse_indices[row, j] - ks // sparse_block_kv) * sparse_block_kv + o`

.

DeepSelect consumes the bf16 logits as they come out of the sparse kernels; the valid columns form a prefix (block ids are sorted), so the per-row `end`

bounds drive it directly. Slots beyond a row's valid count come back as -1.

Parameters:

-

(`logits`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_topk_remap(logits))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[rows, width] bf16 sparse logits, as produced by the sparse kernels.

-

(`sparse_indices`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_topk_remap(sparse_indices))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[rows, S] int32 sparse block ids backing

`logits`

. -

(`end`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_topk_remap(end))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[rows] int32 per-row count of valid logit columns.

-

(`row_ks`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_topk_remap(row_ks))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[rows] int32 per-row K range start.

-

(`sparse_block_kv`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_topk_remap(sparse_block_kv))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Positions per sparse block (8 or 16).

-

(`topk_tokens`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_topk_remap(topk_tokens))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of tokens to keep per row.

-

(`topk_indices`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_topk_remap(topk_indices))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[rows, topk_tokens] int32 output buffer.

-

(`col_indices`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.sparse_mqa_logits.sparse_topk_remap(col_indices))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[rows, topk_tokens] int32 scratch for the sparse-column top-k result (row stride 32B-aligned for DeepSelect).