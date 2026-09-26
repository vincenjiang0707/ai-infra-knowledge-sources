source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/cohere2_moe/
lastmod: 2026-09-24

#

`vllm.model_executor.models.cohere2_moe`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere2_moe)

Classes:

-
–[Cohere2Moe](https://docs.vllm.ai#vllm.model_executor.models.cohere2_moe.Cohere2Moe)Tensor-parallel MoE block for Cohere2Moe with shared experts.

-
–[Cohere2MoeAttention](https://docs.vllm.ai#vllm.model_executor.models.cohere2_moe.Cohere2MoeAttention)Cohere MoE attention with sliding-window interleave.

-
–[Cohere2MoeMLP](https://docs.vllm.ai#vllm.model_executor.models.cohere2_moe.Cohere2MoeMLP)Cohere MLP used as shared experts in the MoE block.

-
–[Cohere2MoeModel](https://docs.vllm.ai#vllm.model_executor.models.cohere2_moe.Cohere2MoeModel)Transformer decoder for Cohere2Moe.


Functions:

-
–[is_prefix_dense_layer](https://docs.vllm.ai#vllm.model_executor.models.cohere2_moe.is_prefix_dense_layer)True when layer_idx lies in the contiguous dense MLP prefix.

-
–[select_norm_impl](https://docs.vllm.ai#vllm.model_executor.models.cohere2_moe.select_norm_impl)Returns (norm_class, eps). Uses RMSNorm when config.rms_norm_eps is set,

-
–[token_choice_with_bias](https://docs.vllm.ai#vllm.model_executor.models.cohere2_moe.token_choice_with_bias)Sigmoid -> top-k (-> renormalize) custom routing for Cohere2Moe.


##

`Cohere2Moe`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere2_moe.Cohere2Moe)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Tensor-parallel MoE block for Cohere2Moe with shared experts.

## Source code in `vllm/model_executor/models/cohere2_moe.py`


|
|

##

`Cohere2MoeAttention`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere2_moe.Cohere2MoeAttention)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Cohere MoE attention with sliding-window interleave.

## Source code in `vllm/model_executor/models/cohere2_moe.py`


|
|

##

`Cohere2MoeMLP`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere2_moe.Cohere2MoeMLP)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Cohere MLP used as shared experts in the MoE block.

## Source code in `vllm/model_executor/models/cohere2_moe.py`


##

`Cohere2MoeModel`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere2_moe.Cohere2MoeModel)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)`EagleModelMixin`


Transformer decoder for Cohere2Moe.

## Source code in `vllm/model_executor/models/cohere2_moe.py`


|
|

##

`is_prefix_dense_layer(config, layer_idx)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere2_moe.is_prefix_dense_layer)

True when layer_idx lies in the contiguous dense MLP prefix.

## Source code in `vllm/model_executor/models/cohere2_moe.py`


##

`select_norm_impl(config)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere2_moe.select_norm_impl)

Returns (norm_class, eps). Uses RMSNorm when config.rms_norm_eps is set, otherwise falls back to LayerNorm with config.layer_norm_eps.

## Source code in `vllm/model_executor/models/cohere2_moe.py`


##

`token_choice_with_bias(hidden_states, gating_output, topk, renormalize)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.cohere2_moe.token_choice_with_bias)

Sigmoid -> top-k (-> renormalize) custom routing for Cohere2Moe.