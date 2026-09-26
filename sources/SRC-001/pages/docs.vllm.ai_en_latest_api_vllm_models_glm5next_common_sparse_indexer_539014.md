source: https://docs.vllm.ai/en/latest/api/vllm/models/glm5next/common/sparse_indexer/
lastmod: 2026-09-24

#

`vllm.models.glm5next.common.sparse_indexer`

[¶](https://docs.vllm.ai#vllm.models.glm5next.common.sparse_indexer)

Shared helpers for the glm5next sparse attention indexer (kpool) layers.

Functions:

-
–[kv_cache_as_quant_view](https://docs.vllm.ai#vllm.models.glm5next.common.sparse_indexer.kv_cache_as_quant_view)4D

`[num_blocks, block_size, 1, head_width]`

view expected by

##

`_build_decode_scatter_indices(decode_lens, num_requests, n)`

[¶](https://docs.vllm.ai#vllm.models.glm5next.common.sparse_indexer._build_decode_scatter_indices)

Per-token (request id, intra-request index) for a non-uniform decode batch, with `n == decode_lens.sum()`

as a host int (avoids a device sync and keeps both repeat_interleaves sync-free).

Shared by every `_scatter_decode_tokens_by_request`

call in a step: building it per call would repeat the same repeat_interleave/cumsum chain up to 5x per layer on the eager decode break.

## Source code in `vllm/models/glm5next/common/sparse_indexer.py`


##

`_decode_topk_seq_lens(positions, decode_lens, num_decode_tokens, batch_size, next_n, requires_padding)`

[¶](https://docs.vllm.ai#vllm.models.glm5next.common.sparse_indexer._decode_topk_seq_lens)

Token-granular seq_len (pos + 1) per pool-topk row, layout-aware.

`pool_topk`

(and the logits it comes from) follow the padded `[batch_size, next_n]`

grid whenever `requires_padding`

is set, so row `(b, t)`

corresponds to flat decode token `offset_b + t`

-- NOT `b * next_n + t`

. Slicing flat `positions[: batch_size * next_n]`

(the uniform-layout shortcut) misaligns every row after the first non-uniform request and, past the decode region, reads prefill tokens' positions; `expand_pools_and_append_tail`

then anchors the tail at another request's length, dropping the row's real tail tokens or emitting indices past its sequence (out-of-bounds block-table reads). Padded rows get 0 (empty tail); they are dropped by `unpack_seq_triton`

anyway.

## Source code in `vllm/models/glm5next/common/sparse_indexer.py`


##

`_fill_short_decode_causal_indices(topk_indices_buffer, positions, num_decode_tokens, max_seq_len, topk_tokens)`

[¶](https://docs.vllm.ai#vllm.models.glm5next.common.sparse_indexer._fill_short_decode_causal_indices)

Fill exact causal rows when sparse decode would select every token.

## Source code in `vllm/models/glm5next/common/sparse_indexer.py`


##

`_gather_workspace_shapes(total_seq_lens, head_dim, fp8_dtype, use_fp4_cache)`

[¶](https://docs.vllm.ai#vllm.models.glm5next.common.sparse_indexer._gather_workspace_shapes)

Return ((values_shape, values_dtype), (scales_shape, scales_dtype)) for the K-gather workspace. FP8 path: (T, head_dim) fp8 + (T, 4) uint8 fp32 scales. MXFP4 path: (T, head_dim // 2) uint8 packed mxfp4 + (T, head_dim // MXFP4_BLOCK_SIZE) uint8 ue8m0 scales.

## Source code in `vllm/models/glm5next/common/sparse_indexer.py`


##

`_scatter_decode_tokens_by_request(tokens, pad_value, num_requests, lmax, scatter_indices)`

[¶](https://docs.vllm.ai#vllm.models.glm5next.common.sparse_indexer._scatter_decode_tokens_by_request)

Group `[N, ...]`

decode tokens into a padded `[num_requests, lmax, ...]`

layout: request `r`

's tokens at row `r`

in order; short requests padded.

Unlike `pack_seq_triton`

this is dtype-agnostic (needed for the int32 slot/pos tensors) — it scatters with the shared per-step indices from `_build_decode_scatter_indices`

. Used only for the non-uniform (`requires_padding`

) decode batch; uniform batches use a zero-copy reshape.

## Source code in `vllm/models/glm5next/common/sparse_indexer.py`


##

`kv_cache_as_quant_view(kv_cache, head_dim, use_fp4_cache)`

[¶](https://docs.vllm.ai#vllm.models.glm5next.common.sparse_indexer.kv_cache_as_quant_view)

4D `[num_blocks, block_size, 1, head_width]`

view expected by DeepGEMM, from the 3D indexer kv-cache allocation.