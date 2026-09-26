source: https://docs.vllm.ai/en/latest/api/vllm/models/minimax_m3/common/ops/
lastmod: 2026-09-24

#

`vllm.models.minimax_m3.common.ops`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.ops)

Cross-platform (Triton) kernels for MiniMax M3 sparse attention.

Modules:

-
–[index_topk](https://docs.vllm.ai/index_topk/#vllm.models.minimax_m3.common.ops.index_topk)Triton kernels for MiniMax M3 lightning-indexer block scoring + top-k.

-
–[sparse_attn](https://docs.vllm.ai/sparse_attn/#vllm.models.minimax_m3.common.ops.sparse_attn)Triton kernels for MiniMax M3 block-sparse GQA attention.


Functions:

-
–[minimax_m3_index_decode](https://docs.vllm.ai#vllm.models.minimax_m3.common.ops.minimax_m3_index_decode)Decode index block-score + top-k, both split-K (cudagraph-safe).

-
–[minimax_m3_index_decode_score](https://docs.vllm.ai#vllm.models.minimax_m3.common.ops.minimax_m3_index_decode_score)Decode index block-score (split-K, cudagraph-safe); no top-k.

-
–[minimax_m3_index_score](https://docs.vllm.ai#vllm.models.minimax_m3.common.ops.minimax_m3_index_score)Compute per-token index scores for each visible sparse block.

-
–[minimax_m3_index_topk](https://docs.vllm.ai#vllm.models.minimax_m3.common.ops.minimax_m3_index_topk)Select index top-k from a precomputed score tensor.

-
–[minimax_m3_sparse_attn](https://docs.vllm.ai#vllm.models.minimax_m3.common.ops.minimax_m3_sparse_attn)GQA block-sparse attention over the selected blocks. block_size_q == 1.

-
–[minimax_m3_sparse_attn_decode](https://docs.vllm.ai#vllm.models.minimax_m3.common.ops.minimax_m3_sparse_attn_decode)GQA block-sparse attention for decode (split-K over the top-k blocks).


##

`minimax_m3_index_decode(idx_q, index_kv_cache, block_table, seq_lens, max_seq_len, topk, init_blocks, local_blocks, num_kv_heads, decode_query_len, max_decode_query_len, out=None, score_out=None)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.ops.minimax_m3_index_decode)

Decode index block-score + top-k, both split-K (cudagraph-safe).

Returns topk_idx [num_kv_heads, total_q, topk] (0-indexed block ids, -1 pad). When `out`

([num_kv_heads, >=total_q, topk]) is given, writes into `out[:, :total_q, :]`

(stable address for cudagraph) instead of allocating. When `score_out`

([num_kv_heads, total_q, >=max_block]) is given, the block scores are written into it (read back by the top-k) instead of a fresh tensor -- used to share a unified score buffer with the prefill side. Reads via strides, so a transposed view of a block-major buffer is accepted.

## Source code in `vllm/models/minimax_m3/common/ops/index_topk.py`


|
|

##

`minimax_m3_index_decode_score(idx_q, index_kv_cache, block_table, seq_lens, max_seq_len, init_blocks, local_blocks, num_kv_heads, decode_query_len, max_decode_query_len, score_out=None)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.ops.minimax_m3_index_decode_score)

Decode index block-score (split-K, cudagraph-safe); no top-k.

Returns score [num_kv_heads, total_q, >=max_block] (fp32; init/local blocks forced to 1e30/1e29). When `score_out`

is given the scores are written into it (read/written by strides, so a transposed view of a unified buffer is accepted) instead of a fresh tensor -- used to share a unified score buffer with the prefill side and run a single top-k over both.

## Source code in `vllm/models/minimax_m3/common/ops/index_topk.py`


|
|

##

`minimax_m3_index_score(idx_q, index_kv_cache, block_table, cu_seqlens_q, seq_lens, prefix_lens, max_query_len, max_seq_len, num_kv_heads)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.ops.minimax_m3_index_score)

Compute per-token index scores for each visible sparse block.

Returns score [num_kv_heads, total_q, max_block], where each score is the max over a 128-token index-K block. M3 has num_idx_heads == num_kv_heads.

## Source code in `vllm/models/minimax_m3/common/ops/index_topk.py`


##

`minimax_m3_index_topk(score, cu_seqlens_q, prefix_lens, max_query_len, topk, init_blocks, local_blocks, out=None)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.ops.minimax_m3_index_topk)

Select index top-k from a precomputed score tensor.

When `out`

is provided (a `[num_idx_heads, >=total_q, topk]`

buffer), the result is written into `out[:, :total_q, :]`

instead of a fresh tensor -- used to keep the top-k output at a stable address for cudagraph capture.

## Source code in `vllm/models/minimax_m3/common/ops/index_topk.py`


##

`minimax_m3_sparse_attn(q, kv_cache, topk_idx, block_table, cu_seqlens_q, seq_lens, prefix_lens, max_query_len, num_kv_heads, sm_scale, output, k_scale=None, v_scale=None)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.ops.minimax_m3_sparse_attn)

GQA block-sparse attention over the selected blocks. block_size_q == 1.

## Source code in `vllm/models/minimax_m3/common/ops/sparse_attn.py`


|
|

##

`minimax_m3_sparse_attn_decode(q, kv_cache, topk_idx, block_table, seq_lens, num_kv_heads, sm_scale, output, decode_query_len, k_scale=None, v_scale=None)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.ops.minimax_m3_sparse_attn_decode)

GQA block-sparse attention for decode (split-K over the top-k blocks).

## Source code in `vllm/models/minimax_m3/common/ops/sparse_attn.py`


|
|