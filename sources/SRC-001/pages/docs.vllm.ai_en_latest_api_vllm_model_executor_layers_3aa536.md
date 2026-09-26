source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/
lastmod: 2026-09-24

#

`vllm.model_executor.layers`

[¶](https://docs.vllm.ai#vllm.model_executor.layers)

Modules:

-
–[activation](https://docs.vllm.ai/activation/#vllm.model_executor.layers.activation)Custom activation functions.

-
–[attention](https://docs.vllm.ai/attention/#vllm.model_executor.layers.attention) -
–[attention_layer_base](https://docs.vllm.ai/attention_layer_base/#vllm.model_executor.layers.attention_layer_base)Base class for attention-like layers.

-
–[conv](https://docs.vllm.ai/conv/#vllm.model_executor.layers.conv)Conv Layer Class.

-
–[fused_allreduce_gemma_rms_norm](https://docs.vllm.ai/fused_allreduce_gemma_rms_norm/#vllm.model_executor.layers.fused_allreduce_gemma_rms_norm)Manual fusion of tensor-parallel all-reduce with the following GemmaRMSNorm.

-
–[fused_embed_norm](https://docs.vllm.ai/fused_embed_norm/#vllm.model_executor.layers.fused_embed_norm)Replicated input embedding + its fused gather/norm kernels.

-
–[fused_moe](https://docs.vllm.ai/fused_moe/#vllm.model_executor.layers.fused_moe) -
–[fused_qk_norm_rope](https://docs.vllm.ai/fused_qk_norm_rope/#vllm.model_executor.layers.fused_qk_norm_rope)Fused QK-RMSNorm + (partial) RoPE + gate copy Triton kernel.

-
–[fusion](https://docs.vllm.ai/fusion/#vllm.model_executor.layers.fusion) -
–[hpc](https://docs.vllm.ai/hpc/#vllm.model_executor.layers.hpc) -
–[indexer_topk](https://docs.vllm.ai/indexer_topk/#vllm.model_executor.layers.indexer_topk)Top-k kernels for the DSA sparse attention indexer.

-
–[layernorm](https://docs.vllm.ai/layernorm/#vllm.model_executor.layers.layernorm)Custom normalization layers.

-
–[lightning_attn](https://docs.vllm.ai/lightning_attn/#vllm.model_executor.layers.lightning_attn) -
–[linear](https://docs.vllm.ai/linear/#vllm.model_executor.layers.linear) -
–[logits_processor](https://docs.vllm.ai/logits_processor/#vllm.model_executor.layers.logits_processor)A layer that compute logits from hidden_stats.

-
–[mamba](https://docs.vllm.ai/mamba/#vllm.model_executor.layers.mamba) -
–[mhc](https://docs.vllm.ai/mhc/#vllm.model_executor.layers.mhc) -
–[minimax_rms_norm](https://docs.vllm.ai/minimax_rms_norm/#vllm.model_executor.layers.minimax_rms_norm) -
–[mla](https://docs.vllm.ai/mla/#vllm.model_executor.layers.mla) -
–[pooler](https://docs.vllm.ai/pooler/#vllm.model_executor.layers.pooler) -
–[quantization](https://docs.vllm.ai/quantization/#vllm.model_executor.layers.quantization) -
–[resampler](https://docs.vllm.ai/resampler/#vllm.model_executor.layers.resampler)Shared resampler perceiver network used in multimodal models and

-
–[rotary_embedding](https://docs.vllm.ai/rotary_embedding/#vllm.model_executor.layers.rotary_embedding)Rotary Positional Embeddings.

-
–[sparse_attn_indexer](https://docs.vllm.ai/sparse_attn_indexer/#vllm.model_executor.layers.sparse_attn_indexer)Custom Sparse Attention Indexer layers.

-
–[sparse_mqa_indexer](https://docs.vllm.ai/sparse_mqa_indexer/#vllm.model_executor.layers.sparse_mqa_indexer)Sparse Attention Indexer that scores only the candidate blocks.

-
–[utils](https://docs.vllm.ai/utils/#vllm.model_executor.layers.utils)Utility methods for model layers.

-
–[vocab_parallel_embedding](https://docs.vllm.ai/vocab_parallel_embedding/#vllm.model_executor.layers.vocab_parallel_embedding)