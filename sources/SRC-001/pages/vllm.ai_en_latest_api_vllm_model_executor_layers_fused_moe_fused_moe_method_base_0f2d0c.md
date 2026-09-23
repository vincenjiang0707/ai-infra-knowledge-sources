source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/fused_moe_method_base/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.fused_moe.fused_moe_method_base`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe_method_base)

Classes:

##

`FusedMoEMethodBase`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe_method_base.FusedMoEMethodBase)

Bases: [QuantizeMethodBase](https://docs.vllm.ai/quantization/base_config/#vllm.model_executor.layers.quantization.base_config.QuantizeMethodBase)

Methods:

-
–[apply](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe_method_base.FusedMoEMethodBase.apply)Apply the MoE operation using modular kernels.

-
–[apply_monolithic](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe_method_base.FusedMoEMethodBase.apply_monolithic)Apply the MoE operation using monolithic kernels.

-
–[maybe_roundup_sizes](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe_method_base.FusedMoEMethodBase.maybe_roundup_sizes)Given layer hidden size and intermediate size per partition and MoE

-
–[uses_weight_scale_2_pattern](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe_method_base.FusedMoEMethodBase.uses_weight_scale_2_pattern)Returns True if this quantization method uses 'weight_scale_2' pattern


Attributes:

-
([has_unpadded_output](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe_method_base.FusedMoEMethodBase.has_unpadded_output)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Indicates that the hidden_states output might be the unpadded

-
([skip_forward_padding](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe_method_base.FusedMoEMethodBase.skip_forward_padding)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to skip the padding in the forward before applying the moe method.


## Source code in `vllm/model_executor/layers/fused_moe/fused_moe_method_base.py`


|
|

###

`has_unpadded_output`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe_method_base.FusedMoEMethodBase.has_unpadded_output)

Indicates that the hidden_states output might be the unpadded hidden_states shape rather than the full padded shape.

###

`skip_forward_padding`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe_method_base.FusedMoEMethodBase.skip_forward_padding)

Whether to skip the padding in the forward before applying the moe method.

###

`apply(layer, x, topk_weights, topk_ids, shared_experts, shared_experts_input)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe_method_base.FusedMoEMethodBase.apply)

Apply the MoE operation using modular kernels.

Parameters:

-

(`layer`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe_method_base.FusedMoEMethodBase.apply(layer))

) –[RoutedExperts](https://docs.vllm.ai/routed_experts/#vllm.model_executor.layers.fused_moe.routed_experts.RoutedExperts)RoutedExperts instance containing weight parameters

-

(`x`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe_method_base.FusedMoEMethodBase.apply(x))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input tensor

-

(`topk_weights`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe_method_base.FusedMoEMethodBase.apply(topk_weights))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Expert weights from router

-

(`topk_ids`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe_method_base.FusedMoEMethodBase.apply(topk_ids))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Selected expert IDs from router

-

(`shared_experts_input`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe_method_base.FusedMoEMethodBase.apply(shared_experts_input))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| NoneInput for shared experts (if any)

-

(`shared_experts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe_method_base.FusedMoEMethodBase.apply(shared_experts))

) –[SharedExperts](https://docs.vllm.ai/runner/shared_experts/#vllm.model_executor.layers.fused_moe.runner.shared_experts.SharedExperts)| NoneThe shared experts module, if any


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Output tensor from routed experts.


## Source code in `vllm/model_executor/layers/fused_moe/fused_moe_method_base.py`


###

`apply_monolithic(layer, x, router_logits, input_ids=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe_method_base.FusedMoEMethodBase.apply_monolithic)

Apply the MoE operation using monolithic kernels.

Parameters:

-

(`layer`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe_method_base.FusedMoEMethodBase.apply_monolithic(layer))

) –[RoutedExperts](https://docs.vllm.ai/routed_experts/#vllm.model_executor.layers.fused_moe.routed_experts.RoutedExperts)RoutedExperts instance containing weight parameters

-

(`x`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe_method_base.FusedMoEMethodBase.apply_monolithic(x))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input tensor

-

(`router_logits`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe_method_base.FusedMoEMethodBase.apply_monolithic(router_logits))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Router logits (routing done internally)

-

(`input_ids`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe_method_base.FusedMoEMethodBase.apply_monolithic(input_ids))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Token ids, for routers that condition on them


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)|[UnfinalizedMoEOutput](https://docs.vllm.ai/moe_output/#vllm.model_executor.layers.fused_moe.moe_output.UnfinalizedMoEOutput)Finalized routed states or a deferred-finalize output.


## Source code in `vllm/model_executor/layers/fused_moe/fused_moe_method_base.py`


###

`maybe_roundup_sizes(hidden_size, intermediate_size_per_partition, act_dtype, moe_parallel_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe_method_base.FusedMoEMethodBase.maybe_roundup_sizes)

Given layer hidden size and intermediate size per partition and MoE configurations, round up hidden_size and intermediate_size_per_partition if necessary.

Parameters:

-

(`hidden_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe_method_base.FusedMoEMethodBase.maybe_roundup_sizes(hidden_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Layer hidden-size

-

(`intermediate_size_per_partition`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe_method_base.FusedMoEMethodBase.maybe_roundup_sizes(intermediate_size_per_partition))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Intermediate size per partition for the layer.

-

(`act_dtype`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe_method_base.FusedMoEMethodBase.maybe_roundup_sizes(act_dtype))

) –[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)Data type of the layer activations.

-

(`moe_parallel_config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe_method_base.FusedMoEMethodBase.maybe_roundup_sizes(moe_parallel_config))

) –[FusedMoEParallelConfig](https://docs.vllm.ai/config/#vllm.model_executor.layers.fused_moe.config.FusedMoEParallelConfig)Fused MoE parallelization strategy configuration.


## Return

A tuple of (rounded_hidden_size, rounded_intermediate_size_per_partition), where: - rounded_hidden_size is the possibly rounded up hidden size. - rounded_intermediate_size_per_partition is the possibly rounded up intermediate size per partition.

## Source code in `vllm/model_executor/layers/fused_moe/fused_moe_method_base.py`


###

`uses_weight_scale_2_pattern()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe_method_base.FusedMoEMethodBase.uses_weight_scale_2_pattern)

Returns True if this quantization method uses 'weight_scale_2' pattern for per-tensor weight scales (e.g., FP4 variants), False otherwise.

This method should be overridden by subclasses that use the 'weight_scale_2' pattern instead of the standard 'weight_scale' pattern.