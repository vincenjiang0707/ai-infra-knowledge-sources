source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/mamba/abstract/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.mamba.abstract`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.abstract)

Classes:

-
–[MambaBase](https://docs.vllm.ai#vllm.model_executor.layers.mamba.abstract.MambaBase)Base class for Mamba-like layers which support the v1 engine.


##

`MambaBase`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.abstract.MambaBase)

Bases: [AttentionLayerBase](https://docs.vllm.ai/attention_layer_base/#vllm.model_executor.layers.attention_layer_base.AttentionLayerBase)

Base class for Mamba-like layers which support the v1 engine. Inherit from this class if you implement a custom layer.

Methods:

-
–[bind_kv_cache](https://docs.vllm.ai#vllm.model_executor.layers.mamba.abstract.MambaBase.bind_kv_cache)Unpack a raw

`[B, 1, 1, C]`

int8 page view into per-state views. -
–[get_attn_backend](https://docs.vllm.ai#vllm.model_executor.layers.mamba.abstract.MambaBase.get_attn_backend)Get the attention backend class for this Mamba layer.

-
–[get_state_shape](https://docs.vllm.ai#vllm.model_executor.layers.mamba.abstract.MambaBase.get_state_shape)Defines the shape of the state.


## Source code in `vllm/model_executor/layers/mamba/abstract.py`


###

`bind_kv_cache(kv_cache)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.abstract.MambaBase.bind_kv_cache)

Unpack a raw `[B, 1, 1, C]`

int8 page view into per-state views.

Each block's `C`

bytes hold the layer's states (e.g. conv, ssm) packed contiguously; slice them out and reinterpret per dtype/shape.

## Source code in `vllm/model_executor/layers/mamba/abstract.py`


###

`get_attn_backend()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.abstract.MambaBase.get_attn_backend)

###

`get_state_shape()`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.abstract.MambaBase.get_state_shape)

Defines the shape of the state. For mamba layers this is usually a (conv_state, ssm_state) tuple. In this case, returns (conv_state_shape, ssm_state_shape).