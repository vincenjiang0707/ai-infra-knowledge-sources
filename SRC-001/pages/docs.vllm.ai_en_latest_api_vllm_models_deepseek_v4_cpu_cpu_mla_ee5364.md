source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v4/cpu/cpu_mla/
lastmod: 2026-09-23

#

`vllm.models.deepseek_v4.cpu.cpu_mla`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_mla)

CPU DeepSeek-V4 sparse-MLA backend descriptor.

DeepSeek-V4 attention runs entirely through `DeepseekV4Attention`

/`DeepseekV4CPUAttention`

, never through a generic `AttentionImpl`

. `DeepseekV4CPUSparseBackend`

exists so the CPU attention layer has its own backend name and its own metadata-builder class: CPU is not allowed to run triton-cpu inside the model's forward path, so `DeepseekV4CPUFlashMLAMetadataBuilder`

overrides the shared base's `_build_c128a_metadata`

(triton-backed in `DeepseekV4SparseMLAMetadataBuilder`

) with a plain-eager-PyTorch reimplementation of the same per-token block-table-resolution math.

Classes:

-
–[DeepseekV4CPUFlashMLAMetadataBuilder](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_mla.DeepseekV4CPUFlashMLAMetadataBuilder)CPU sparse-MLA metadata builder: same fields as the shared base, but

-
–[DeepseekV4CPUIndexerMetadataBuilder](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_mla.DeepseekV4CPUIndexerMetadataBuilder)CPU indexer metadata builder: same fields as the shared base, but

-
–[DeepseekV4CPUSparseSWAMetadataBuilder](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_mla.DeepseekV4CPUSparseSWAMetadataBuilder)CPU SWA metadata builder: same fields as the shared base.


##

`DeepseekV4CPUFlashMLAMetadataBuilder`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_mla.DeepseekV4CPUFlashMLAMetadataBuilder)

Bases: [DeepseekV4SparseMLAMetadataBuilder](https://docs.vllm.ai/sparse_mla/#vllm.models.deepseek_v4.sparse_mla.DeepseekV4SparseMLAMetadataBuilder)

CPU sparse-MLA metadata builder: same fields as the shared base, but skips the C128A dense-topk metadata entirely -- unlike CUDA/XPU/ROCm, `DeepseekV4CPUAttention.forward_mqa`

never reads `c128a_global_decode_topk_indices`

/`c128a_decode_topk_lens`

/ `c128a_prefill_topk_indices`

; it recomputes the same local top-k directly from `positions`

instead, so building it here (whether eagerly or via the shared base's triton kernel) would be wasted work.

## Source code in `vllm/models/deepseek_v4/cpu/cpu_mla.py`


##

`DeepseekV4CPUIndexerMetadataBuilder`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_mla.DeepseekV4CPUIndexerMetadataBuilder)

Bases: [DeepseekV32IndexerMetadataBuilder](https://docs.vllm.ai/v1/attention/backends/mla/indexer/#vllm.v1.attention.backends.mla.indexer.DeepseekV32IndexerMetadataBuilder)

CPU indexer metadata builder: same fields as the shared base, but prefill requests are never split into multiple chunks.

`DeepseekV32IndexerMetadataBuilder._split_indexer_prefill_chunks`

(the shared base's default) bounds two things the CUDA/XPU indexer kernels need: the flat-gather workspace size and the dense M*N logits tensor those kernels allocate for a chunk. The CPU indexer (`sparse_attn_indexer_cpu`

) allocates neither -- it reads the paged K-cache directly via `fp8_paged_mqa_logits_cpu`

/ `topk_transform_512_cpu`

, with no chunk-splitting of its own. With chunked prefill now enabled for this model on CPU (see `CpuPlatform.check_and_update_config`

's `amx_mla_or_dsv4_enabled`

), the total query-token count for one step is already bounded by `max_num_batched_tokens`

-- there is nothing left here to bound, so this always returns a single chunk spanning the whole step's prefill batch.

## Source code in `vllm/models/deepseek_v4/cpu/cpu_mla.py`


##

`DeepseekV4CPUSparseSWAMetadataBuilder`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_mla.DeepseekV4CPUSparseSWAMetadataBuilder)

Bases: [DeepseekSparseSWAMetadataBuilder](https://docs.vllm.ai/v1/attention/backends/mla/sparse_swa/#vllm.v1.attention.backends.mla.sparse_swa.DeepseekSparseSWAMetadataBuilder)

CPU SWA metadata builder: same fields as the shared base.

Methods:

-
–[build_tile_scheduler](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_mla.DeepseekV4CPUSparseSWAMetadataBuilder.build_tile_scheduler)CPU never runs the FlashMLA tile-scheduler planner (that's a CUDA


## Source code in `vllm/models/deepseek_v4/cpu/cpu_mla.py`


###

`build_tile_scheduler(num_decode_tokens)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_mla.DeepseekV4CPUSparseSWAMetadataBuilder.build_tile_scheduler)

CPU never runs the FlashMLA tile-scheduler planner (that's a CUDA C++ decode-path concern) -- always return the all-`None`

sentinel the shared base's own CPU branch returns.