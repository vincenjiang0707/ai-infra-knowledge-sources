source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v41/sparse_mla/
lastmod: 2026-09-23

#

`vllm.models.deepseek_v41.sparse_mla`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.sparse_mla)

DeepSeek-V4.1 FlashMLA sparse backend, metadata, and metadata builders.

Classes:

-
–[DeepseekV41SparseSWAMetadataBuilder](https://docs.vllm.ai#vllm.models.deepseek_v41.sparse_mla.DeepseekV41SparseSWAMetadataBuilder)SWA metadata builder base for v4.1.

-
–[DeepseekV4SparseMLABackend](https://docs.vllm.ai#vllm.models.deepseek_v41.sparse_mla.DeepseekV4SparseMLABackend)DeepSeek-V4.1 sparse-MLA backend base.

-
–[FlashMLAMegaAttnBackend](https://docs.vllm.ai#vllm.models.deepseek_v41.sparse_mla.FlashMLAMegaAttnBackend)FlashMLA's mega-attention kernel: Q RoPE + sparse attention + inverse


##

`DeepseekV41SparseSWAMetadataBuilder`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.sparse_mla.DeepseekV41SparseSWAMetadataBuilder)

Bases: [DeepseekSparseSWAMetadataBuilder](https://docs.vllm.ai/v1/attention/backends/mla/sparse_swa/#vllm.v1.attention.backends.mla.sparse_swa.DeepseekSparseSWAMetadataBuilder)

SWA metadata builder base for v4.1.

The shared builder classifies decode layer types by the v4.0 ratios (1 = SWA-only, 4, 128). v4.1 uses 0 / 1 / 2, so recompute the set of tile-scheduler plans from the v4.1 topology.

## Source code in `vllm/models/deepseek_v41/sparse_mla.py`


##

`DeepseekV4SparseMLABackend`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.sparse_mla.DeepseekV4SparseMLABackend)

Bases: [AttentionBackend](https://docs.vllm.ai/v1/attention/backend/#vllm.v1.attention.backend.AttentionBackend)

DeepSeek-V4.1 sparse-MLA backend base.

Subclasses `AttentionBackend`

directly (not the V3.2 `FlashMLASparseBackend`

): DeepSeek-V4.1 runs its own attention layer (`DeepseekV4Attention`

), so it does not reuse the V3.2 builder or impl, and only needs to declare its own metadata builder, KV-cache layout, and the sparse-MLA capability flags.

## Source code in `vllm/models/deepseek_v41/sparse_mla.py`


##

`FlashMLAMegaAttnBackend`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.sparse_mla.FlashMLAMegaAttnBackend)

Bases: `DeepseekV4FlashMLABackend`


FlashMLA's mega-attention kernel: Q RoPE + sparse attention + inverse RoPE + FP8 cast of the output, in one launch.

Same metadata and KV-cache geometry as `FLASHMLA_SPARSE_DSV41`

-- what differs is the attention layer's interface contract (it takes an unnormed, unroped Q and returns an already-inverse-RoPE'd, quantized output) and the extra `nvfp4_ds_mla`

compressed-cache record only this kernel can read. SM100 only; the kernel has no SM90 instantiation.