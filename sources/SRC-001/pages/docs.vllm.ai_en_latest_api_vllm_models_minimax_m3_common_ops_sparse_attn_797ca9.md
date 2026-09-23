source: https://docs.vllm.ai/en/latest/api/vllm/models/minimax_m3/common/ops/sparse_attn/
lastmod: 2026-09-23

#

`vllm.models.minimax_m3.common.ops.sparse_attn`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.ops.sparse_attn)

Triton kernels for MiniMax M3 block-sparse GQA attention.

The main heads attend only to the blocks selected by the lightning indexer (see `index_topk`

). Adapted to vLLM's paged KV cache: the KV page size is forced to equal the sparse block size (128), so one selected block maps to exactly one page.

Main K/V cache layout (vLLM): `(num_blocks, num_kv_heads, 128, 2 * head_dim)`

K=[..., :head_dim] V=[..., head_dim:]

Only the paths MiniMax M3 uses are implemented: no attention sink, base-2 (exp2/log2) softmax. The decode kernels use split-K (flash-decoding) over the selected blocks with a separate merge step, since one query token per request leaves the prefill kernels (which parallelize over the query dim) idle.

Functions:

-
–[minimax_m3_sparse_attn](https://docs.vllm.ai#vllm.models.minimax_m3.common.ops.sparse_attn.minimax_m3_sparse_attn)GQA block-sparse attention over the selected blocks. block_size_q == 1.

-
–[minimax_m3_sparse_attn_decode](https://docs.vllm.ai#vllm.models.minimax_m3.common.ops.sparse_attn.minimax_m3_sparse_attn_decode)GQA block-sparse attention for decode (split-K over the top-k blocks).


##

`minimax_m3_sparse_attn(q, kv_cache, topk_idx, block_table, cu_seqlens_q, seq_lens, prefix_lens, max_query_len, num_kv_heads, sm_scale, output, k_scale=None, v_scale=None)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.ops.sparse_attn.minimax_m3_sparse_attn)

GQA block-sparse attention over the selected blocks. block_size_q == 1.

## Source code in `vllm/models/minimax_m3/common/ops/sparse_attn.py`


|
|

##

`minimax_m3_sparse_attn_decode(q, kv_cache, topk_idx, block_table, seq_lens, num_kv_heads, sm_scale, output, decode_query_len, k_scale=None, v_scale=None)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.ops.sparse_attn.minimax_m3_sparse_attn_decode)

GQA block-sparse attention for decode (split-K over the top-k blocks).

## Source code in `vllm/models/minimax_m3/common/ops/sparse_attn.py`


|
|