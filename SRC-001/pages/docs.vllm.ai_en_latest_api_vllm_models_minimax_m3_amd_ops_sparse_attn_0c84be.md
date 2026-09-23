source: https://docs.vllm.ai/en/latest/api/vllm/models/minimax_m3/amd/ops/sparse_attn/
lastmod: 2026-09-23

#

`vllm.models.minimax_m3.amd.ops.sparse_attn`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.amd.ops.sparse_attn)

ROCm gfx942/gfx950 block-sparse GQA prefill kernel for MiniMax-M3.

Only the prefill path is specialized on CDNA: each 128-token KV block is split into SUB_K-token sub-tiles to right-size the per-block QK/PV MFMAs. Everything else -- the decode split-K kernels, the FP8 dtype set, the sparse block size -- is reused unchanged from `common.ops.sparse_attn`

.

Functions:

-
–[minimax_m3_sparse_attn](https://docs.vllm.ai#vllm.models.minimax_m3.amd.ops.sparse_attn.minimax_m3_sparse_attn)GQA block-sparse attention over the selected blocks. block_size_q == 1.

-
–[minimax_m3_sparse_attn_decode](https://docs.vllm.ai#vllm.models.minimax_m3.amd.ops.sparse_attn.minimax_m3_sparse_attn_decode)GQA block-sparse attention for decode (split-K over the top-k blocks).


##

`_sparse_attn_prefill_kwargs()`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.amd.ops.sparse_attn._sparse_attn_prefill_kwargs)

MFMA + pipeline launch params for the sub-tiled prefill kernel.

gfx942 and gfx950 share the same params: `num_warps=1`

keeps one wave resident on the small per-sub-tile GEMM, `matrix_instr_nonkdim=16`

/ `kpack=2`

select the MFMA_16x16 path, and `num_stages=1`

fits LDS and is fastest in the sweep. Only the sub-tile width (`_SPARSE_ATTN_SUB_K`

) differs by arch. Empty on other AMD archs. Cached: arch is fixed per process.

## Source code in `vllm/models/minimax_m3/amd/ops/sparse_attn.py`


##

`minimax_m3_sparse_attn(q, kv_cache, topk_idx, block_table, cu_seqlens_q, seq_lens, prefix_lens, max_query_len, num_kv_heads, sm_scale, output, k_scale=None, v_scale=None)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.amd.ops.sparse_attn.minimax_m3_sparse_attn)

GQA block-sparse attention over the selected blocks. block_size_q == 1.

## Source code in `vllm/models/minimax_m3/amd/ops/sparse_attn.py`


|
|

##

`minimax_m3_sparse_attn_decode(q, kv_cache, topk_idx, block_table, seq_lens, num_kv_heads, sm_scale, output, decode_query_len, k_scale=None, v_scale=None)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.amd.ops.sparse_attn.minimax_m3_sparse_attn_decode)

GQA block-sparse attention for decode (split-K over the top-k blocks).

## Source code in `vllm/models/minimax_m3/common/ops/sparse_attn.py`


|
|