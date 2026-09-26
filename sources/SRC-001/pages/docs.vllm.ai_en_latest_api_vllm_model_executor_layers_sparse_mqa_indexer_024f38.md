source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/sparse_mqa_indexer/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.sparse_mqa_indexer`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.sparse_mqa_indexer)

Sparse Attention Indexer that scores only the candidate blocks.

DeepSeek V4.1 two-level selection: the candidate-source indexer publishes the top candidate blocks and later indexers pick their top-k inside them. `SparseAttnIndexer`

does that by computing dense logits over the whole context and masking; this layer instead calls DeepGEMM's sparse MQA-logits kernels on the candidate blocks only, so the work is O(candidate blocks) instead of O(context). It requires the `DeepseekV41SparseIndexerBackend`

metadata (see `AttentionConfig.indexer_sparse_logits`

).

Classes:

-
–[SparseMQAIndexer](https://docs.vllm.ai#vllm.model_executor.layers.sparse_mqa_indexer.SparseMQAIndexer)Candidate-consuming indexer on DeepGEMM's sparse MQA-logits kernels.


##

`SparseMQAIndexer`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.sparse_mqa_indexer.SparseMQAIndexer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Candidate-consuming indexer on DeepGEMM's sparse MQA-logits kernels.

Only valid for indexer layers that read candidate blocks with the MXFP4 indexer cache on SM100. The K cache is written by the model before this runs; `forward`

takes the same arguments as `SparseAttnIndexer`

so the attention layer can call either.

Attributes:

-
–[weights_dtype](https://docs.vllm.ai#vllm.model_executor.layers.sparse_mqa_indexer.SparseMQAIndexer.weights_dtype)Per-head weights dtype the sparse kernels take. The fused Q RoPE-quant


## Source code in `vllm/model_executor/layers/sparse_mqa_indexer.py`


|
|

###

`weights_dtype = torch.bfloat16`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.sparse_mqa_indexer.SparseMQAIndexer.weights_dtype)

Per-head weights dtype the sparse kernels take. The fused Q RoPE-quant kernel writes it directly so no cast runs per step.

###

`_reserve_workspaces(device)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.sparse_mqa_indexer.SparseMQAIndexer._reserve_workspaces)

Profiling run: claim the K-gather workspace and the peak sparse logits allocation so the memory estimate covers them.

## Source code in `vllm/model_executor/layers/sparse_mqa_indexer.py`


##

`_gather_prefill_chunk_k(kv_cache, k_quant_full, k_scale_full, chunk)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.sparse_mqa_indexer._gather_prefill_chunk_k)

Gather one prefill chunk's paged K into the packed workspace.

## Source code in `vllm/model_executor/layers/sparse_mqa_indexer.py`


##

`_prefill_k_workspaces(total_seq_lens, head_dim)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.sparse_mqa_indexer._prefill_k_workspaces)

The packed MXFP4 K-gather workspace `(values, scales)`

, shared with the dense indexer layers of the same model.