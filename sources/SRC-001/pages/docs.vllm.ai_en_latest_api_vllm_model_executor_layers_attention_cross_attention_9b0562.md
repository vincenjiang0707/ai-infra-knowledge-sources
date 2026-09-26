source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/attention/cross_attention/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.attention.cross_attention`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.cross_attention)

Classes:

-
–[CrossAttention](https://docs.vllm.ai#vllm.model_executor.layers.attention.cross_attention.CrossAttention)Cross-attention for encoder-decoder models.


##

`CrossAttention`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.cross_attention.CrossAttention)

Bases: [Attention](https://docs.vllm.ai/#vllm.model_executor.layers.attention.Attention)

Cross-attention for encoder-decoder models. Handles attention between decoder queries and encoder keys/values.

## Source code in `vllm/model_executor/layers/attention/cross_attention.py`


##

`_get_cross_slot_mapping(encoder_seq_lens, block_table_tensor, kv_cache_spec, device)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.cross_attention._get_cross_slot_mapping)

Get cross-attention slot mappings.