source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/extract_hidden_states/
lastmod: 2026-09-23

#

`vllm.model_executor.models.extract_hidden_states`

[¶](https://docs.vllm.ai#vllm.model_executor.models.extract_hidden_states)

Hidden States Extractor Model.

This model extracts and caches hidden states from the target model without performing actual token generation. It's used with the extract_hidden_states speculative decoding method.

Classes:

-
–[CacheOnlyAttentionBackend](https://docs.vllm.ai#vllm.model_executor.models.extract_hidden_states.CacheOnlyAttentionBackend)Attention backend that only caches KV without computing attention.

-
–[CacheOnlyAttentionImpl](https://docs.vllm.ai#vllm.model_executor.models.extract_hidden_states.CacheOnlyAttentionImpl)Attention implementation that only caches KV states.

-
–[CacheOnlyAttentionLayer](https://docs.vllm.ai#vllm.model_executor.models.extract_hidden_states.CacheOnlyAttentionLayer)Attention layer that only caches key/value states without computing attention.

-
–[ExtractHiddenStatesModel](https://docs.vllm.ai#vllm.model_executor.models.extract_hidden_states.ExtractHiddenStatesModel)

Functions:

-
–[unified_kv_cache_update](https://docs.vllm.ai#vllm.model_executor.models.extract_hidden_states.unified_kv_cache_update)Returns a dummy that is passed to unified_attention to signal a side effect and


##

`CacheOnlyAttentionBackend`

[¶](https://docs.vllm.ai#vllm.model_executor.models.extract_hidden_states.CacheOnlyAttentionBackend)

Bases: [AttentionBackend](https://docs.vllm.ai/v1/attention/backend/#vllm.v1.attention.backend.AttentionBackend)

Attention backend that only caches KV without computing attention.

## Source code in `vllm/model_executor/models/extract_hidden_states.py`


##

`CacheOnlyAttentionImpl`

[¶](https://docs.vllm.ai#vllm.model_executor.models.extract_hidden_states.CacheOnlyAttentionImpl)

Bases: [AttentionImpl](https://docs.vllm.ai/v1/attention/backend/#vllm.v1.attention.backend.AttentionImpl)

Attention implementation that only caches KV states.

## Source code in `vllm/model_executor/models/extract_hidden_states.py`


##

`CacheOnlyAttentionLayer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.extract_hidden_states.CacheOnlyAttentionLayer)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)[AttentionLayerBase](https://docs.vllm.ai/layers/attention_layer_base/#vllm.model_executor.layers.attention_layer_base.AttentionLayerBase)

Attention layer that only caches key/value states without computing attention.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.extract_hidden_states.CacheOnlyAttentionLayer.forward)Cache hidden states as KV pairs without computing attention.


## Source code in `vllm/model_executor/models/extract_hidden_states.py`


|
|

###

`forward(to_cache)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.extract_hidden_states.CacheOnlyAttentionLayer.forward)

Cache hidden states as KV pairs without computing attention.

Parameters:

-

(`to_cache`

[¶](https://docs.vllm.ai#vllm.model_executor.models.extract_hidden_states.CacheOnlyAttentionLayer.forward(to_cache))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The tensor to insert into the kv cache. shape [num_tokens, num_heads, head_size]


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Dummy output tensor (not used)


## Source code in `vllm/model_executor/models/extract_hidden_states.py`


##

`ExtractHiddenStatesModel`

[¶](https://docs.vllm.ai#vllm.model_executor.models.extract_hidden_states.ExtractHiddenStatesModel)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.extract_hidden_states.ExtractHiddenStatesModel.forward)Process and cache hidden states.

-
–[load_weights](https://docs.vllm.ai#vllm.model_executor.models.extract_hidden_states.ExtractHiddenStatesModel.load_weights)No weights to load for this dummy model.


## Source code in `vllm/model_executor/models/extract_hidden_states.py`


###

`forward(hidden_states)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.extract_hidden_states.ExtractHiddenStatesModel.forward)

Process and cache hidden states.

Parameters:

-

(`hidden_states`

[¶](https://docs.vllm.ai#vllm.model_executor.models.extract_hidden_states.ExtractHiddenStatesModel.forward(hidden_states))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Hidden states from target model shape: [num_tokens, num_hidden_states, hidden_size]


Returns:

-
`None`

–Tuple of (dummy_output, dummy_output) - both unused


## Source code in `vllm/model_executor/models/extract_hidden_states.py`


##

`unified_kv_cache_update(to_cache, layer_name)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.extract_hidden_states.unified_kv_cache_update)

Returns a dummy that is passed to unified_attention to signal a side effect and the data dependency between them to ensure torch.compile preserves ordering.