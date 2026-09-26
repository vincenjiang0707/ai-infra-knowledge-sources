source: https://docs.vllm.ai/en/latest/api/vllm/models/minimax_m3/nvidia/msa_cutlass_sparse_decode/
lastmod: 2026-09-24

#

`vllm.models.minimax_m3.nvidia.msa_cutlass_sparse_decode`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.nvidia.msa_cutlass_sparse_decode)

MiniMax CUTLASS sparse decode using per-query-token page indices.

Classes:

-
–[MSACutlassDecodePlanCache](https://docs.vllm.ai#vllm.models.minimax_m3.nvidia.msa_cutlass_sparse_decode.MSACutlassDecodePlanCache)Reusable plans whose mutable tensors retain cudagraph-stable addresses.


Functions:

-
–[msa_cutlass_sparse_decode](https://docs.vllm.ai#vllm.models.minimax_m3.nvidia.msa_cutlass_sparse_decode.msa_cutlass_sparse_decode)Run CUTLASS sparse decode with metadata prepared by the MSA builder.

-
–[prepare_decode_metadata](https://docs.vllm.ai#vllm.models.minimax_m3.nvidia.msa_cutlass_sparse_decode.prepare_decode_metadata)Prepare graph-stable runtime metadata for one sparse decode step.

-
–[should_prepare_decode_metadata](https://docs.vllm.ai#vllm.models.minimax_m3.nvidia.msa_cutlass_sparse_decode.should_prepare_decode_metadata)Return whether a graph shape can use the CUTLASS decode path.

-
–[supports_cutlass_sparse_decode](https://docs.vllm.ai#vllm.models.minimax_m3.nvidia.msa_cutlass_sparse_decode.supports_cutlass_sparse_decode)Return whether static model geometry supports CUTLASS sparse decode.


##

`MSACutlassDecodePlanCache`

`dataclass`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.nvidia.msa_cutlass_sparse_decode.MSACutlassDecodePlanCache)

Reusable plans whose mutable tensors retain cudagraph-stable addresses.

## Source code in `vllm/models/minimax_m3/nvidia/msa_cutlass_sparse_decode.py`


|
|

##

`msa_cutlass_sparse_decode(query_fp8, kv_cache, topk, output, metadata, *, scale, q_scale_float, k_scale_float, v_scale_float)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.nvidia.msa_cutlass_sparse_decode.msa_cutlass_sparse_decode)

Run CUTLASS sparse decode with metadata prepared by the MSA builder.

## Source code in `vllm/models/minimax_m3/nvidia/msa_cutlass_sparse_decode.py`


##

`prepare_decode_metadata(block_table, seq_lens, seq_lens_cpu, decode_query_len, *, num_q_heads, num_kv_heads, page_size, topk_blocks, plan_cache=None)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.nvidia.msa_cutlass_sparse_decode.prepare_decode_metadata)

Prepare graph-stable runtime metadata for one sparse decode step.

## Source code in `vllm/models/minimax_m3/nvidia/msa_cutlass_sparse_decode.py`


##

`should_prepare_decode_metadata(batch_size, decode_query_len, *, decode_backend, num_q_heads, num_kv_heads, kv_cache_dtype, page_size, topk_blocks)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.nvidia.msa_cutlass_sparse_decode.should_prepare_decode_metadata)

Return whether a graph shape can use the CUTLASS decode path.

## Source code in `vllm/models/minimax_m3/nvidia/msa_cutlass_sparse_decode.py`


##

`supports_cutlass_sparse_decode(*, decode_backend, num_q_heads, num_kv_heads, kv_cache_dtype, page_size, topk_blocks)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.nvidia.msa_cutlass_sparse_decode.supports_cutlass_sparse_decode)

Return whether static model geometry supports CUTLASS sparse decode.