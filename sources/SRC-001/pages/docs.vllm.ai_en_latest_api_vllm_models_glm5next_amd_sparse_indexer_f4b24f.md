source: https://docs.vllm.ai/en/latest/api/vllm/models/glm5next/amd/sparse_indexer/
lastmod: 2026-09-23

#

`vllm.models.glm5next.amd.sparse_indexer`

[¶](https://docs.vllm.ai#vllm.models.glm5next.amd.sparse_indexer)

Custom Sparse Attention Indexer layers.

Classes:

-
–[SparseAttnIndexerKpool](https://docs.vllm.ai#vllm.models.glm5next.amd.sparse_indexer.SparseAttnIndexerKpool)Sparse Attention Indexer Custom Op Layer. This layer is extracted as a


##

`SparseAttnIndexerKpool`

[¶](https://docs.vllm.ai#vllm.models.glm5next.amd.sparse_indexer.SparseAttnIndexerKpool)

Bases: [CustomOp](https://docs.vllm.ai/model_executor/custom_op/#vllm.model_executor.custom_op.CustomOp)

Sparse Attention Indexer Custom Op Layer. This layer is extracted as a separate custom op since it involves heavy custom kernels like `mqa_logits`

, `paged_mqa_logits`

and `top_k_per_row`

, etc. Those kernels maybe requires specific memory layout or implementation for different hardware backends to achieve optimal performance.

For now, the default native path will use CUDA backend path. Other platform may requires add the corresponding Custom Op name `sparse_attn_indexer`

to `custom_ops`

in `CompilationConfig`

to enable the platform specific path.

## Source code in `vllm/models/glm5next/amd/sparse_indexer.py`


|
|

##

`_kpool_compress_insert(k, gate_score, ape, kv_cache, slot_mapping, kpool, head_dim, round_scale)`

[¶](https://docs.vllm.ai#vllm.models.glm5next.amd.sparse_indexer._kpool_compress_insert)

Pool `kpool`

consecutive tokens into one fp8 K and write at pool slots.

`slot_mapping`

is pool-granular (compress_ratio == kpool on the spec): only the *last* token of each complete pool carries a valid (>=0) slot; intra-pool tokens are -1. Every position is treated as a pool-completion candidate and non-completions are masked off inside the kernel. Compacting the valid rows first costs two device syncs on the eager prefill path and buys nothing numerically. Assumes pool-aligned chunk starts.