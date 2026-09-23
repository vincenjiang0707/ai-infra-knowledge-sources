source: https://docs.vllm.ai/en/latest/api/vllm/models/inkling/amd/ops/gluon/rel_mha_extend_gfx950/
lastmod: 2026-09-23

#

`vllm.models.inkling.amd.ops.gluon.rel_mha_extend_gfx950`

[¶](https://docs.vllm.ai#vllm.models.inkling.amd.ops.gluon.rel_mha_extend_gfx950)

rel_mha extend Gluon kernel for AMD GFX950.

This handles ragged, multi-token queries against a paged KV cache. The query axis is tiled into the MFMA `M`

dimension (prefill-style): `BLOCK_M`

query rows of a single q-head share each paged KV tile, so every KV tile is loaded once and reused across all rows in the tile. The grid is `(blocks_per_req, batch, n_heads)`

-- all host-known sizes -- and each program self-locates its request from `cu_seqlens_q`

/ `cache_seqlens`

in-kernel, so the launch stays CUDA-graph static with no device->host sync.

Visibility per query row depends on `is_causal`

and the optional sliding window:

`is_causal=False`

: every query token attends the full visible cache, i.e.`visible_kv = cache_seqlens[batch]`

.`is_causal=True`

: query tokens are a causal suffix, so the`i`

-th query token of a request (0-indexed) attends`prefix + i + 1`

tokens, where`prefix = cache_seqlens[batch] - query_len[batch]`

.

Causal masking only touches the few KV tiles that reach the diagonal; the long prefix is a mask-free fast path. Sinks and sliding windows (causal or not) are applied per tile. This is the sole Gluon extend implementation.

##

`_select_extend_tile(max_seqlen_q, page_size)`

[¶](https://docs.vllm.ai#vllm.models.inkling.amd.ops.gluon.rel_mha_extend_gfx950._select_extend_tile)

Return (BLOCK_M, BLOCK_N, NUM_WARPS) for the given max query length.

Queries that fit in a single short tile use it (least padding, most occupancy); longer ones use the tall tile that covers more rows per shared-KV pass.