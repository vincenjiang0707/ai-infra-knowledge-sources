source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/param2moe/
lastmod: 2026-09-24

#

`vllm.model_executor.models.param2moe`

[¶](https://docs.vllm.ai#vllm.model_executor.models.param2moe)

Classes:

-
–[Param2MoEAttention](https://docs.vllm.ai#vllm.model_executor.models.param2moe.Param2MoEAttention)Grouped-Query Attention (GQA) for Param2MoE.

-
–[Param2MoEDecoderLayer](https://docs.vllm.ai#vllm.model_executor.models.param2moe.Param2MoEDecoderLayer)Single transformer decoder block.

-
–[Param2MoEForCausalLM](https://docs.vllm.ai#vllm.model_executor.models.param2moe.Param2MoEForCausalLM)vLLM-native Param2MoE CausalLM.

-
–[Param2MoEMLP](https://docs.vllm.ai#vllm.model_executor.models.param2moe.Param2MoEMLP)SwiGLU feed-forward block used for dense layers.

-
–[Param2MoEMixtureOfExperts](https://docs.vllm.ai#vllm.model_executor.models.param2moe.Param2MoEMixtureOfExperts)Implements the vLLM MixtureOfExperts protocol for Param2MoE.

-
–[Param2MoEMoEBlock](https://docs.vllm.ai#vllm.model_executor.models.param2moe.Param2MoEMoEBlock)Mixture-of-Experts block for Param2MoE.


##

`Param2MoEAttention`

[¶](https://docs.vllm.ai#vllm.model_executor.models.param2moe.Param2MoEAttention)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Grouped-Query Attention (GQA) for Param2MoE.

## Notable differences from a vanilla GQA layer

- The checkpoint fuses Q, K, V into a single
`query_key_value`

weight. vLLM receives it already renamed to`qkv_proj`

by the weight-name translator and loads it directly;`QKVParallelLinear`

splits the fused`[Q|K|V]`

tensor internally. - Optional per-head RMS norms on Q and K (
`use_qk_norm=True`

).

## Source code in `vllm/model_executor/models/param2moe.py`


|
|

##

`Param2MoEDecoderLayer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.param2moe.Param2MoEDecoderLayer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Single transformer decoder block.

Dense for the first `first_k_dense_replace`

layers; MoE thereafter.

## Source code in `vllm/model_executor/models/param2moe.py`


##

`Param2MoEForCausalLM`

[¶](https://docs.vllm.ai#vllm.model_executor.models.param2moe.Param2MoEForCausalLM)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

, [SupportsPP](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsPP)

, [SupportsLoRA](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsLoRA)[Param2MoEMixtureOfExperts](https://docs.vllm.ai#vllm.model_executor.models.param2moe.Param2MoEMixtureOfExperts)

vLLM-native Param2MoE CausalLM.

Uses Grouped-Query Attention (GQA) with a Sigmoid-scored, grouped-topk Mixture-of-Experts MLP.

## Source code in `vllm/model_executor/models/param2moe.py`


|
|

##

`Param2MoEMLP`

[¶](https://docs.vllm.ai#vllm.model_executor.models.param2moe.Param2MoEMLP)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

SwiGLU feed-forward block used for dense layers.

## Source code in `vllm/model_executor/models/param2moe.py`


##

`Param2MoEMixtureOfExperts`

[¶](https://docs.vllm.ai#vllm.model_executor.models.param2moe.Param2MoEMixtureOfExperts)

Bases: [MixtureOfExperts](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.MixtureOfExperts)

Implements the vLLM MixtureOfExperts protocol for Param2MoE.

## Source code in `vllm/model_executor/models/param2moe.py`


##

`Param2MoEMoEBlock`

[¶](https://docs.vllm.ai#vllm.model_executor.models.param2moe.Param2MoEMoEBlock)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Mixture-of-Experts block for Param2MoE.

## Routing

- Sigmoid scoring (config.score_function = "sigmoid")
- Grouped top-k (n_group, topk_group)
- Per-expert bias (gate.expert_bias → e_score_correction_bias)
- routed_scaling_factor normalisation

One set of shared (always-active) experts is added on top.

## Source code in `vllm/model_executor/models/param2moe.py`


|
|

##

`_is_expert_bias_name(name)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.param2moe._is_expert_bias_name)

##

`_normalize_expert_bias(weights)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.param2moe._normalize_expert_bias)

Zero-mean the MoE router's per-expert score bias for load balance.

The rename to `e_score_correction_bias`

is done by the mapper; only the tensor adjustment lives here, since a WeightsMapper cannot transform data.