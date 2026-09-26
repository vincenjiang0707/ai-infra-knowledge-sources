source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/utils/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.fused_moe.utils`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.utils)

Functions:

-
–[count_expert_num_tokens](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.utils.count_expert_num_tokens)Count the number to tokens assigned to each expert.

-
–[fi_moe_largest_bucket](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.utils.fi_moe_largest_bucket)Estimate FlashInfer's MoE autotuning maximum token count.

-
–[is_model_fused_shared_expert_compatible](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.utils.is_model_fused_shared_expert_compatible)Resolve one fused-shared-expert state for a model's MoE layers.

-
–[moe_use_td_hw_supported](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.utils.moe_use_td_hw_supported)Whether the current device can run the TD (gather) path of

-
–[resolve_layer_fused_shared_expert](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.utils.resolve_layer_fused_shared_expert)Resolve whether AITER fused shared-expert execution is enabled.

-
–[resolve_moe_use_td](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.utils.resolve_moe_use_td)Tri-state resolver for

`VLLM_TRITON_USE_TD`

. -
–[warn_if_moe_use_td_ineffective](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.utils.warn_if_moe_use_td_ineffective)One-shot warning when

`VLLM_TRITON_USE_TD`

is set but ignored.

##

`_fp8_quantize(A, A_scale, per_act_token, block_shape=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.utils._fp8_quantize)

Perform fp8 quantization on the inputs. If a block_shape is provided, the output will be blocked.

## Source code in `vllm/model_executor/layers/fused_moe/utils.py`


##

`_int8_quantize(A, A_scale, per_act_token, block_shape=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.utils._int8_quantize)

Perform int8 quantization on the inputs. If a block_shape is provided, the output will be blocked.

## Source code in `vllm/model_executor/layers/fused_moe/utils.py`


##

`_resize_cache(x, v)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.utils._resize_cache)

Shrink the given tensor and apply the given view to it. This is used to resize the intermediate fused_moe caches.

## Source code in `vllm/model_executor/layers/fused_moe/utils.py`


##

`count_expert_num_tokens(topk_ids, num_local_experts, expert_map)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.utils.count_expert_num_tokens)

Count the number to tokens assigned to each expert.

Parameters:

-

(`topk_ids`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.utils.count_expert_num_tokens(topk_ids))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Tensor mapping each token to its list of experts.

-

(`num_local_experts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.utils.count_expert_num_tokens(num_local_experts))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of experts in this rank.

-

(`expert_map`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.utils.count_expert_num_tokens(expert_map))`Optional[`

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]A tensor mapping expert indices from the global expert space to the local expert space of the expert parallel shard.


Returns: A tensor of size num_local_experts, where tensor[i] holds the number of tokens assigned to the ith expert.

## Source code in `vllm/model_executor/layers/fused_moe/utils.py`


##

`fi_moe_largest_bucket(moe_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.utils.fi_moe_largest_bucket)

Estimate FlashInfer's MoE autotuning maximum token count.

All DP ranks may contribute `max_num_tokens`

to one invocation. Keep FlashInfer's default moe `tune_max_num_tokens=8192`

floor to avoid over-underestimation. DeepEP, SP, or PCP may make this underestimate, however overestimation may be dangerous, increasing tuning- cost and memory use.

NOTE: The DP factor applies even when EP is disabled:

Without

`--enable-expert-parallel`

, MoE layers would use tensor parallelism.

For a detailed explanation, see: `docs/serving/data_parallel_deployment.md`


## Source code in `vllm/model_executor/layers/fused_moe/utils.py`


##

`is_model_fused_shared_expert_compatible(layers, moe_cls, moe_name)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.utils.is_model_fused_shared_expert_compatible)

Resolve one fused-shared-expert state for a model's MoE layers.

## Source code in `vllm/model_executor/layers/fused_moe/utils.py`


##

`moe_use_td_hw_supported()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.utils.moe_use_td_hw_supported)

Whether the current device can run the TD (gather) path of `fused_moe_kernel`

(ignores the `VLLM_TRITON_USE_TD`

override).

The A-load uses `tensor_descriptor.gather`

, which lowers to the PTX `tile::gather4`

instruction. That instruction is part of the `tcgen05`

/Tensor Memory (TMEM) family introduced with Blackwell and has no Hopper (sm90) equivalent -- ptxas rejects it there ("Feature '.tile::gather4 ...' requires .target sm_100 or higher"). Unlike `scatter4`

, `gather4`

is supported across the whole sm100+ range including consumer Blackwell (sm120/sm121): see triton-lang/triton#8498, which enables `gather4`

on sm120/sm121 while leaving `scatter4`

unsupported there. So this gates on a blanket `has_device_capability(100)`

rather than the sm100 *family* check used for the scatter store path.

## Source code in `vllm/model_executor/layers/fused_moe/utils.py`


##

`resolve_layer_fused_shared_expert(quant_config, prefix, shared_expert_name='shared_experts')`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.utils.resolve_layer_fused_shared_expert)

Resolve whether AITER fused shared-expert execution is enabled.

Parameters:

-

(`quant_config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.utils.resolve_layer_fused_shared_expert(quant_config))

) –[QuantizationConfig](https://docs.vllm.ai/quantization/#vllm.model_executor.layers.quantization.QuantizationConfig)| NoneModel quantization configuration.

-

(`prefix`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.utils.resolve_layer_fused_shared_expert(prefix))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)MoE module prefix.

-

(`shared_expert_name`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.utils.resolve_layer_fused_shared_expert(shared_expert_name))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'shared_experts'`

) –Shared-expert module name under

`prefix`

.

Returns:

-

–[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether AITER fused shared experts are enabled.


Raises:

-

–[ValueError](https://docs.python.org/3/builtins/exceptions.html#ValueError)If requested shared-expert fusion is quantization-incompatible.


## Source code in `vllm/model_executor/layers/fused_moe/utils.py`


##

`resolve_moe_use_td()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.utils.resolve_moe_use_td)

Tri-state resolver for `VLLM_TRITON_USE_TD`

.

Unset auto-selects the TD path on XPU only, mirroring the attention dispatcher in `triton_attn.py`

. `1`

/`0`

force it on/off regardless of hardware; forcing `1`

where it cannot compile (see `moe_use_td_hw_supported`

) fails at ptxas. Blackwell CUDA (sm100+) can compile it but is opt-in only, pending validation.

## Source code in `vllm/model_executor/layers/fused_moe/utils.py`


##

`warn_if_moe_use_td_ineffective(active_backend, is_quantized=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.utils.warn_if_moe_use_td_ineffective)

One-shot warning when `VLLM_TRITON_USE_TD`

is set but ignored.

Fires when the user set the env explicitly and either (a) the active MoE backend is not the fused Triton kernel, or (b) the model is quantized (the TD path falls back to the pointer path under any quantization).