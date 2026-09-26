source: https://docs.vllm.ai/en/latest/api/vllm/models/inkling/amd/ops/fa4_rel_attention/
lastmod: 2026-09-24

#

`vllm.models.inkling.amd.ops.fa4_rel_attention`

[¶](https://docs.vllm.ai#vllm.models.inkling.amd.ops.fa4_rel_attention)

ROCm paged attention with Inkling's query-dependent relative bias.

The NVIDIA implementation uses the score-mod hook in tml-fa4. ROCm Flash Attention and AITER do not expose an equivalent hook, so this module implements the same operation directly in Triton. Query heads belonging to one KV head are processed together and KV pages are gathered through vLLM's block table.

Functions:

-
–[bucket_max_seqlen_q](https://docs.vllm.ai#vllm.models.inkling.amd.ops.fa4_rel_attention.bucket_max_seqlen_q)Round the scheduling bound up to a power of two.

-
–[inkling_fa4_num_splits](https://docs.vllm.ai#vllm.models.inkling.amd.ops.fa4_rel_attention.inkling_fa4_num_splits)Keep the NVIDIA-facing split heuristic as API-compatible metadata.

-
–[inkling_fa4_rel_attention](https://docs.vllm.ai#vllm.models.inkling.amd.ops.fa4_rel_attention.inkling_fa4_rel_attention)Paged varlen attention with Inkling's relative score modification.

-
–[use_gfx950_gluon_decode](https://docs.vllm.ai#vllm.models.inkling.amd.ops.fa4_rel_attention.use_gfx950_gluon_decode)Use the vendored TokenSpeed CDNA4 decode kernel where it is supported.

-
–[use_gfx950_gluon_extend](https://docs.vllm.ai#vllm.models.inkling.amd.ops.fa4_rel_attention.use_gfx950_gluon_extend)Use Gluon only for the long full-attention extend regime it wins.


##

`bucket_max_seqlen_q(max_seqlen_q)`

[¶](https://docs.vllm.ai#vllm.models.inkling.amd.ops.fa4_rel_attention.bucket_max_seqlen_q)

##

`inkling_fa4_num_splits(*, is_local, batch_size, max_query_len, num_heads, num_kv_heads, max_kv_len)`

[¶](https://docs.vllm.ai#vllm.models.inkling.amd.ops.fa4_rel_attention.inkling_fa4_num_splits)

Keep the NVIDIA-facing split heuristic as API-compatible metadata.

The ROCm Triton implementation performs online softmax in one program and does not consume the result. Keeping this function unchanged avoids platform-specific scheduling branches in :mod:`inkling.amd.attention`

.

## Source code in `vllm/models/inkling/amd/ops/fa4_rel_attention.py`


##

`inkling_fa4_rel_attention(q, key_cache, value_cache, *, block_table, cache_seqlens, cu_seqlens_q, max_seqlen_q, softmax_scale, causal, window_size, rel_extent, rel_logits, num_splits=32, max_kv_len=None, out=None)`

[¶](https://docs.vllm.ai#vllm.models.inkling.amd.ops.fa4_rel_attention.inkling_fa4_rel_attention)

Paged varlen attention with Inkling's relative score modification.

## Source code in `vllm/models/inkling/amd/ops/fa4_rel_attention.py`


|
|

##

`use_gfx950_gluon_decode(*, max_query_len, page_size, head_dim)`

[¶](https://docs.vllm.ai#vllm.models.inkling.amd.ops.fa4_rel_attention.use_gfx950_gluon_decode)

Use the vendored TokenSpeed CDNA4 decode kernel where it is supported.

## Source code in `vllm/models/inkling/amd/ops/fa4_rel_attention.py`


##

`use_gfx950_gluon_extend(*, max_query_len, max_kv_len, page_size, head_dim, window_left)`

[¶](https://docs.vllm.ai#vllm.models.inkling.amd.ops.fa4_rel_attention.use_gfx950_gluon_extend)

Use Gluon only for the long full-attention extend regime it wins.