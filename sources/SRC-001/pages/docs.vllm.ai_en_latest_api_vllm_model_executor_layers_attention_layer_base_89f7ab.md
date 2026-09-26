source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/attention_layer_base/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.attention_layer_base`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention_layer_base)

Base class for attention-like layers.

Classes:

-
–[AttentionLayerBase](https://docs.vllm.ai#vllm.model_executor.layers.attention_layer_base.AttentionLayerBase)Base class for attention-like layers (Attention, Mamba, etc.)


##

`AttentionLayerBase`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention_layer_base.AttentionLayerBase)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Base class for attention-like layers (Attention, Mamba, etc.) that support the v1 engine.

This provides a common interface for getting attention backends from different layer types.

Methods:

-
–[bind_kv_cache](https://docs.vllm.ai#vllm.model_executor.layers.attention_layer_base.AttentionLayerBase.bind_kv_cache)Bind the allocated KV cache tensor to this layer.

-
–[get_attn_backend](https://docs.vllm.ai#vllm.model_executor.layers.attention_layer_base.AttentionLayerBase.get_attn_backend)Get the attention backend class for this layer.

-
–[get_kv_cache_spec](https://docs.vllm.ai#vllm.model_executor.layers.attention_layer_base.AttentionLayerBase.get_kv_cache_spec)Get the KV cache spec for this layer.


## Source code in `vllm/model_executor/layers/attention_layer_base.py`


###

`bind_kv_cache(kv_cache)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention_layer_base.AttentionLayerBase.bind_kv_cache)

Bind the allocated KV cache tensor to this layer.

The default stores the cache view as-is; subclasses (e.g. Mamba) override this to unpack the raw buffer into per-state views.

## Source code in `vllm/model_executor/layers/attention_layer_base.py`


###

`get_attn_backend()`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention_layer_base.AttentionLayerBase.get_attn_backend)

###

`get_kv_cache_spec(vllm_config)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention_layer_base.AttentionLayerBase.get_kv_cache_spec)

Get the KV cache spec for this layer. May be None if the layer does not need KV cache.