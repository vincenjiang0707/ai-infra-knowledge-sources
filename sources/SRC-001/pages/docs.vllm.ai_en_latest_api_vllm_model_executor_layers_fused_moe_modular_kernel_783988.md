source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/modular_kernel/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.fused_moe.modular_kernel`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel)

Classes:

-
–[ExpertTokensMetadata](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.ExpertTokensMetadata)Metadata regarding expert-token routing.

-
–[FusedMoEActivationFormat](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEActivationFormat)The standard activation format (num_tokens, hidden dim).

-
–[FusedMoEExperts](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExperts) -
–[FusedMoEExpertsModular](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular)An abstract base class for the [Permute-Experts-Unpermute] step described

-
–[FusedMoEExpertsMonolithic](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsMonolithic)An abstract base class for the [Permute-Experts-Unpermute] step described

-
–[FusedMoEKernel](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEKernel) -
–[FusedMoEKernelModularImpl](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEKernelModularImpl) -
–[FusedMoEKernelMonolithicImpl](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEKernelMonolithicImpl) -
–[FusedMoEPrepareAndFinalize](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalize)An abstract base class for the [Quantize-Prepare] and [Finalize] steps

-
–[FusedMoEPrepareAndFinalizeModular](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalizeModular)An abstract base class for the [Quantize-Prepare] and [Finalize] steps

-
–[FusedMoEPrepareAndFinalizeMonolithic](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalizeMonolithic)An abstract base class for the [Quantize-Prepare] and [Finalize] steps

-
–[TopKWeightAndReduce](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.TopKWeightAndReduce)An abstract base class for weight application and reduction implementations.


##

`ExpertTokensMetadata`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.ExpertTokensMetadata)

Metadata regarding expert-token routing.

## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


##

`FusedMoEActivationFormat`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEActivationFormat)

Bases: [Enum](https://docs.python.org/3/library/enum.html#enum.Enum)

The standard activation format (num_tokens, hidden dim).

Attributes:

-
–[Standard](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEActivationFormat.Standard)The batched experts format (num experts, max tokens per expert, hidden dim)


## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


###

`Standard = ('standard',)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEActivationFormat.Standard)

The batched experts format (num experts, max tokens per expert, hidden dim)

##

`FusedMoEExperts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExperts)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Methods:

-
–[__init__](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExperts.__init__)moe_config: MoE layer configuration.

-
–[activation_format](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExperts.activation_format)A property which is a tuple of the input and output activation formats

-
–[supports_lora](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExperts.supports_lora)Return True if this expert impl natively handles LoRA.

-
–[supports_packed_ue8m0_act_scales](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExperts.supports_packed_ue8m0_act_scales)A flag indicating whether or not this class can process packed ue8m0


Attributes:

-
([expects_unquantized_inputs](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExperts.expects_unquantized_inputs)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether or not the PrepareFinalize should defer input quantization


## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


|
|

###

`expects_unquantized_inputs`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExperts.expects_unquantized_inputs)

Whether or not the PrepareFinalize should defer input quantization in the prepare step. If True, then the Experts kernel will execute the input quantization itself.

Sample subclasses that override are AITER and FlashInfer CUTLASS.

###

`__init__(moe_config, quant_config, max_num_tokens=None, num_dispatchers=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExperts.__init__)

moe_config: MoE layer configuration. quant_config: Quantization parameters for this experts instance.

## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


###

`_supports_activation(activation)`

`abstractmethod`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExperts._supports_activation)

Whether the kernel supports a particular act function.

###

`_supports_batch_invariance()`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExperts._supports_batch_invariance)

Whether the kernel supports batch invariance, i.e. the output does not depend on the order of the tokens in the input batch. This is useful for determining if the kernel can used with VLLM_BATCH_INVARIANT=1.

## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


###

`_supports_current_device()`

`abstractmethod`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExperts._supports_current_device)

Whether the kernel supports the current device type (compute cability and current platform).

###

`_supports_no_act_and_mul()`

`abstractmethod`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExperts._supports_no_act_and_mul)

Whether the kernel supports act_and_mul=False, i.e. non-gated MoE models like Nemotron-Nano.

###

`_supports_parallel_config(moe_parallel_config)`

`abstractmethod`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExperts._supports_parallel_config)

Whether the kernel supports deployment in particular parallel config.

Can be overridden if a kernel does not support EP, SP or some other configuration.

## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


###

`_supports_router_logits_dtype(router_logits_dtype, routing_method)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExperts._supports_router_logits_dtype)

Whether a kernel supports a particular dtype for router logits input.

Can be overridden by monolithic kernels that execute the router in addition to the experts if certain dtypes are not supported.

## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


###

`_supports_routing_method(routing_method, weight_key, activation_key)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExperts._supports_routing_method)

Whether the kernel supports a routing method (e.g. GroupedTopK).

Can be overridden by monolithic kernels that execute the router in addition to the experts if certain routers are not supported.

## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


###

`_supports_shape(hidden_dim)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExperts._supports_shape)

Whether a kernel supports a particular shape. Can be overridden if a kernel has specific shape requirements.

###

`activation_format()`

`abstractmethod`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExperts.activation_format)

A property which is a tuple of the input and output activation formats for the 'apply' method.

## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


###

`supports_lora()`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExperts.supports_lora)

Return True if this expert impl natively handles LoRA.

LoRA-aware experts should mix in LoRAExpertsMixin, which flips this to True and provides the per-forward LoRA state plumbing.

## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


###

`supports_packed_ue8m0_act_scales()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExperts.supports_packed_ue8m0_act_scales)

A flag indicating whether or not this class can process packed ue8m0 activation scales.

##

`FusedMoEExpertsModular`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular)

Bases: [FusedMoEExperts](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExperts)

An abstract base class for the [Permute-Experts-Unpermute] step described above.

Methods:

-
–[adjust_N_for_activation](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular.adjust_N_for_activation)Calculate the output dimension for the activation function.

-
–[apply](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular.apply)This function computes the intermediate result of a Mixture of Experts

-
–[moe_problem_size](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular.moe_problem_size)Extract the MoE problem size from the given tensor arguments:

-
–[workspace_dtype](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular.workspace_dtype)Workspace type: The dtype to use for the workspace tensors.

-
–[workspace_shapes](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular.workspace_shapes)Compute the shapes for the temporary and final outputs of the two gemms


## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


|
|

###

`adjust_N_for_activation(N, activation)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular.adjust_N_for_activation)

Calculate the output dimension for the activation function.

For *_no_mul activations (e.g. relu2_no_mul), there's no gate/up split, so output size equals input size (N).

For regular gated activations (e.g., silu, gelu, swigluoai), output size is N // 2 due to gate × activation(up) multiplication.

Parameters:

-

(`N`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular.adjust_N_for_activation(N))

) –[int](https://docs.python.org/3/builtins/functions.html#int)The intermediate size (width of w1/w3 weights).

-

(`activation`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular.adjust_N_for_activation(activation))

) –[MoEActivation](https://docs.vllm.ai/activation/#vllm.model_executor.layers.fused_moe.activation.MoEActivation)The activation function enum.


Returns:

-

–[int](https://docs.python.org/3/builtins/functions.html#int)The output dimension after activation.


## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


###

`apply(output, hidden_states, w1, w2, topk_weights, topk_ids, activation, global_num_experts, expert_map, a1q_scale, a2_scale, workspace13, workspace2, expert_tokens_meta, apply_router_weight_on_input)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular.apply)

This function computes the intermediate result of a Mixture of Experts (MoE) layer using two sets of weights, w1 and w2.

Parameters:

-

(`output`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular.apply(output))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(torch.Tensor): The unweighted, unreduced output tensor.

-

(`hidden_states`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular.apply(hidden_states))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(torch.Tensor): The (quantized) input tensor to the MoE layer.

-

(`w1`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular.apply(w1))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The first set of expert weights.

-

(`w2`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular.apply(w2))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The second set of expert weights.

-

(`topk_weights`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular.apply(topk_weights))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)A map of row to expert weights. Some implementations choose to do weight application.

-

(`topk_ids`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular.apply(topk_ids))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)A map of row to expert id.

-

(`activation`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular.apply(activation))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The activation function to apply after the first MoE layer.

-

(`global_num_experts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular.apply(global_num_experts))

) –[int](https://docs.python.org/3/builtins/functions.html#int)The total number of experts in the global expert space.

-

(`expert_map`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular.apply(expert_map))`Optional[`

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]A tensor mapping expert indices from the global expert space to the local expert space of the expert parallel shard.

-

(`a1q_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular.apply(a1q_scale))`Optional[`

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]Optional quantized scale to be used for a1. Result of quantization from prepare/finalize and not from the FusedMoEQuantConfig.

-

(`a2_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular.apply(a2_scale))`Optional[`

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]Optional quantized scale to be used for the second gemm's activations.

-

(`workspace13`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular.apply(workspace13))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)A scratch tensor used for gemm outputs must be large enough to hold output of either MoE gemm.

-

(`workspace2`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular.apply(workspace2))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)A scratch tensor used for the activation function.

-

(`expert_tokens_meta`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular.apply(expert_tokens_meta))`Optional[`

) –[ExpertTokensMetadata](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.ExpertTokensMetadata)]An optional ExpertTokensMetadata object containing gpu/cpu tensors as big as the number of local experts with the information about the number of tokens assigned to each local expert.

-

(`apply_router_weight_on_input`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular.apply(apply_router_weight_on_input))

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)True if router weights are already applied on the input. This is relevant if the implementation chooses to do weight application.


## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


###

`moe_problem_size(a1, w1, w2, topk_ids)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular.moe_problem_size)

Extract the MoE problem size from the given tensor arguments: - a: The hidden states, input to the MoE layer. - w1: The first set of expert weights. - w2: The second set of expert weights. - topk_ids: The topk ids.

Note: extracting the problem shape from the weight and activation tensors is not obvious. It needs to be done this way specifically due to subtle issues with particular kernels, e.g. the int4 kernels divide the trailing dimension by two, so it's not "correct" to extract N or K from the trailing dimension of w1 or w2. Similarly, some kernels transpose the weights, so this needs to be kept in mind.

Note: This implementation covers most cases. However, if experts require a specialized implementation, like MarlinExperts, they are free to override this function.

## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


###

`workspace_dtype(act_dtype)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular.workspace_dtype)

###

`workspace_shapes(M, N, K, topk, global_num_experts, local_num_experts, expert_tokens_meta, activation)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular.workspace_shapes)

Compute the shapes for the temporary and final outputs of the two gemms and activation in the fused expert function. Since the gemms are independent, the workspace for the first gemm can be shared with the workspace for the last gemm.

Inputs: - M: number of tokens. - N: Row (or column) dimension of expert weights. - K: hidden dimension - topk: The number of top-k experts to select. - global_num_experts: global number of experts. - local_num_experts: local number of experts due to DP/EP. - expert_tokens_meta: number of tokens per expert metadata for batched format.

Returns a tuple of: - workspace13 shape tuple: must be large enough to hold the result of either expert gemm. - workspace2 shape tuple: must be large enough to hold the result of the activation function. - output shape tuple: must be exact size of the final gemm output. - Note: workspace shapes can be 0 if the workspace is not needed. But in order for activation chunking to work, the first dimension of each tuple must be the number of tokens when the shape is not 0.

## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


##

`FusedMoEExpertsMonolithic`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsMonolithic)

Bases: [FusedMoEExperts](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExperts)

An abstract base class for the [Permute-Experts-Unpermute] step described above, but with the monolithic interface (accepts router logits rather than topk ids and weights).

Methods:

-
–[apply](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsMonolithic.apply)Same as

`FusedMoEExperts.apply`

, except uses router_logits as opposed -
–[supports_routing_replay_capture](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsMonolithic.supports_routing_replay_capture)Whether this expert supports routing replay capture.


## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


|
|

###

`_supports_router_logits_dtype(router_logits_dtype, routing_method)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsMonolithic._supports_router_logits_dtype)

Whether the kernel supports a dtype for router logits.

Modular kernels should opt-in to support.

## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


###

`_supports_routing_method(routing_method, weight_key, activation_key)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsMonolithic._supports_routing_method)

Whether the kernel supports a routing method (e.g. GroupedTopK).

Monolithic kernels should explicitly opt-in to support.

## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


###

`apply(hidden_states, w1, w2, router_logits, activation, global_num_experts, expert_map, a1q_scale, apply_router_weight_on_input, num_expert_group=None, e_score_correction_bias=None, routed_scaling_factor=None, topk_group=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsMonolithic.apply)

Same as `FusedMoEExperts.apply`

, except uses router_logits as opposed to the topk_ids and topk_weights. This is useful for kernels with fused router and fused_experts (e.g. FLASHINFER_TRTLLM).

## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


###

`supports_routing_replay_capture()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsMonolithic.supports_routing_replay_capture)

Whether this expert supports routing replay capture.

Subclasses backed by a kernel that exposes routed expert IDs (e.g. FlashInfer's `routing_replay_out`

) should override.

## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


##

`FusedMoEKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEKernel)

Methods:

-
–[output_is_reduced](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEKernel.output_is_reduced)Indicates whether or not the output of fused MoE kernel


## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


|
|

##

`FusedMoEKernelModularImpl`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEKernelModularImpl)

Methods:

-
–[apply](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEKernelModularImpl.apply)This function computes a Mixture of Experts (MoE) layer using two sets


## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


|
|

###

`_allocate_buffers(out_dtype, device, M_chunk, M_full, N, K, top_k, global_num_experts, local_num_experts, expert_tokens_meta, activation)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEKernelModularImpl._allocate_buffers)

Allocate temporary and output buffers for the fused experts op. Inputs: - out_dtype: output type of workspace and output tensors. - device: the device of the workspace and output tensors. See `workspace_shapes`

for a description of the remainder of arguments. Returns a tuple of (workspace13, workspace2, output) tensors.

## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


|
|

###

`_finalize(output, fused_out, hidden_states, topk_weights, topk_ids, apply_router_weight_on_input, shared_experts, shared_experts_input)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEKernelModularImpl._finalize)

The _finalize method is a wrapper around self.prepare_finalize.finalize that handles DBO, async and shared expert overlap.

Parameters:

-

(`output`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEKernelModularImpl._finalize(output))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Tensor the finalized result is written into.

-

(`fused_out`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEKernelModularImpl._finalize(fused_out))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The unweighted, unreduced output of the fused experts.

-

(`hidden_states`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEKernelModularImpl._finalize(hidden_states))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The input tensor to the MoE layer.

-

(`topk_weights`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEKernelModularImpl._finalize(topk_weights))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)A map of row to expert weights.

-

(`topk_ids`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEKernelModularImpl._finalize(topk_ids))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)A map of row to expert id.

-

(`apply_router_weight_on_input`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEKernelModularImpl._finalize(apply_router_weight_on_input))

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)True if the router weights were already applied on the input.

-

(`shared_experts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEKernelModularImpl._finalize(shared_experts))

) –[SharedExperts](https://docs.vllm.ai/runner/shared_experts/#vllm.model_executor.layers.fused_moe.runner.shared_experts.SharedExperts)| NoneSharedExperts | None. The shared experts if any.

-

(`shared_experts_input`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEKernelModularImpl._finalize(shared_experts_input))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| NoneOptional separate input for shared experts. When latent MoE is used, hidden_states is the latent-projected tensor (smaller dimension) used by routed experts, while shared_experts_input is the original hidden_states (full dimension) needed by the shared expert MLP.


## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


|
|

###

`_prepare(hidden_states, topk_weights, topk_ids, global_num_experts, expert_map, apply_router_weight_on_input)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEKernelModularImpl._prepare)

The _prepare method is a wrapper around self.prepare_finalize.prepare that handles DBO and async.

## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


|
|

###

`apply(hidden_states, w1, w2, topk_ids, topk_weights, activation=MoEActivation.SILU, global_num_experts=-1, expert_map=None, apply_router_weight_on_input=False, shared_experts=None, shared_experts_input=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEKernelModularImpl.apply)

This function computes a Mixture of Experts (MoE) layer using two sets of weights, w1 and w2, and top-k gating mechanism.

Parameters:

-

(`hidden_states`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEKernelModularImpl.apply(hidden_states))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(torch.Tensor): The input tensor to the MoE layer.

-

(`w1`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEKernelModularImpl.apply(w1))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The first set of expert weights.

-

(`w2`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEKernelModularImpl.apply(w2))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The second set of expert weights.

-

(`topk_ids`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEKernelModularImpl.apply(topk_ids))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)A map of row to expert id.

-

(`topk_weights`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEKernelModularImpl.apply(topk_weights))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The topk weights applied at the end of the layer.

-

(`activation`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEKernelModularImpl.apply(activation))

, default:[MoEActivation](https://docs.vllm.ai/activation/#vllm.model_executor.layers.fused_moe.activation.MoEActivation)`SILU`

) –The activation function to apply after the first MoE layer.

-

(`global_num_experts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEKernelModularImpl.apply(global_num_experts))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`-1`

) –The total number of experts in the global expert space.

-

(`expert_map`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEKernelModularImpl.apply(expert_map))`Optional[`

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]`None`

) –A tensor mapping expert indices from the global expert space to the local expert space of the expert parallel shard.

-

(`apply_router_weight_on_input`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEKernelModularImpl.apply(apply_router_weight_on_input))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –When true, the topk weights are applied directly on the inputs. This is only applicable when topk is 1.

-

(`shared_experts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEKernelModularImpl.apply(shared_experts))

, default:[SharedExperts](https://docs.vllm.ai/runner/shared_experts/#vllm.model_executor.layers.fused_moe.runner.shared_experts.SharedExperts)| None`None`

) –SharedExperts | None. The shared experts if any.

-

(`shared_experts_input`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEKernelModularImpl.apply(shared_experts_input))`Optional[`

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]`None`

) –Optional separate input for shared experts. For latent MoE, this is the original hidden_states before latent projection.


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)torch.Tensor: The output tensor after applying the MoE layer.


## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


|
|

##

`FusedMoEKernelMonolithicImpl`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEKernelMonolithicImpl)

Methods:

-
–[apply](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEKernelMonolithicImpl.apply)Same as forward(), except uses router_logits as opposed


## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


|
|

###

`apply(hidden_states, w1, w2, router_logits, activation, global_num_experts, expert_map, apply_router_weight_on_input, num_expert_group=None, e_score_correction_bias=None, routed_scaling_factor=None, topk_group=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEKernelMonolithicImpl.apply)

Same as forward(), except uses router_logits as opposed to the topk_ids and topk_weights. This is used for kernels that have fused router + experts (e.g. FLASHINFER_TRTLLM).

## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


##

`FusedMoEPrepareAndFinalize`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalize)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

An abstract base class for the [Quantize-Prepare] and [Finalize] steps described above.

There are two variants of this class: * FusedMoEPrepareAndFinalizeModular - this operates on topk ids and weights * FusedMoEPrepareAndFinalizeMonolithic - the operates on router_logits

Methods:

-
–[max_num_tokens_per_rank](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalize.max_num_tokens_per_rank)Some PrepareFinalize All2All implementations are batched. Meaning,

-
–[output_is_reduced](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalize.output_is_reduced)Indicates whether or not the output of finalize is reduced across all

-
–[post_init_setup](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalize.post_init_setup)Initialize FusedMoEPrepareAndFinalizeModular settings that depend on

-
–[supports_async](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalize.supports_async)Indicates whether or not this class implements prepare_async and

-
–[topk_indices_dtype](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalize.topk_indices_dtype)The PrepareFinalize All2All implementations generally constrain the


Attributes:

-
([activation_format](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalize.activation_format)

) –[FusedMoEActivationFormat](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEActivationFormat)A property indicating the output format of the activations for the


## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


###

`activation_format`

`abstractmethod`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalize.activation_format)

A property indicating the output format of the activations for the 'prepare' method.

###

`max_num_tokens_per_rank()`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalize.max_num_tokens_per_rank)

Some PrepareFinalize All2All implementations are batched. Meaning, they can process only as set of tokens at a time. This function returns the batch size i.e the maximum number of tokens the implementation can process at a time. Return None if there are no such restrictions.

## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


###

`output_is_reduced()`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalize.output_is_reduced)

Indicates whether or not the output of finalize is reduced across all ranks.

###

`post_init_setup(fused_experts)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalize.post_init_setup)

Initialize FusedMoEPrepareAndFinalizeModular settings that depend on FusedMoEExpertsModular experts object. The FusedMoEPrepareAndFinalizeModular implementations that have such dependencies may choose to override this function.

## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


###

`supports_async()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalize.supports_async)

Indicates whether or not this class implements prepare_async and finalize_async.

###

`topk_indices_dtype()`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalize.topk_indices_dtype)

The PrepareFinalize All2All implementations generally constrain the dtype of the topk_ids they support. This function returns the required topk indices dtype so it can be respected. Return None if there are no such restrictions.

## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


##

`FusedMoEPrepareAndFinalizeModular`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalizeModular)

Bases: [FusedMoEPrepareAndFinalize](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalize)

An abstract base class for the [Quantize-Prepare] and [Finalize] steps described above for the Modular case.

Methods:

-
–[finalize](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalizeModular.finalize)Perform any combine plus apply weights and perform a reduction on the

-
–[finalize_async](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalizeModular.finalize_async)Perform any combine plus apply weights and perform a reduction on the

-
–[prepare](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalizeModular.prepare)Perform any quantization (and/or) dispatching needed for this kernel.

-
–[prepare_async](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalizeModular.prepare_async)Perform any quantization (and/or) dispatching needed for this kernel


## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


|
|

###

`finalize(output, fused_expert_output, topk_weights, topk_ids, apply_router_weight_on_input, weight_and_reduce_impl)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalizeModular.finalize)

Perform any combine plus apply weights and perform a reduction on the fused experts output. - output: The output tensor, written in place. Must be (M, K) shape. - fused_expert_output: The unweighted, unreduced output of the fused experts, it will have (M, topk, K) shape. - topk_weights: The weights to be applied to the fused_experts_output. - topk_ids: The topk_ids. - apply_router_weight_on_input: When False, apply the weights to fused_expert_output. - weight_and_reduce_impl: An optional TopKWeightAndReduce implementation.

## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


###

`finalize_async(output, fused_expert_output, topk_weights, topk_ids, apply_router_weight_on_input, weight_and_reduce_impl)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalizeModular.finalize_async)

Perform any combine plus apply weights and perform a reduction on the fused experts output but do not wait for results from other workers. - output: The output tensor, written in place. Must be (M, K) shape. - fused_expert_output: The unweighted, unreduced output of the fused experts, it will have (M, topk, K) shape. - topk_weights: The weights to be applied to the fused_experts_output. - topk_ids: The topk_ids. - apply_router_weight_on_input: When False, apply the weights to fused_expert_output. - weight_and_reduce_impl: An optional TopKWeightAndReduce implementation.

Returns a callback or a hook callback pair that when invoked waits for results from other workers and has the same return signature as `finalize`

, if a hook is returned this is more lightweight check that the recv is complete without doing extra work (used by DBO, will be refactored in the very near future)

ret = obj.finalize_async(output, ...) ... output not valid yet ... if isinstance(ret, tuple): hook, receiver = ret hook() receiver() ... output valid here ...

is equivalent to:

obj.finalize(output, ...)

## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


###

`prepare(a1, topk_weights, topk_ids, num_experts, expert_map, apply_router_weight_on_input, quant_config, defer_input_quant)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalizeModular.prepare)

Perform any quantization (and/or) dispatching needed for this kernel. - a1: The (unquantized) input to the MoE layer. - topk_ids: The topk ids. - topk_weights: The topk weights. - num_experts: The total number of experts in the global expert space. - expert_map: A tensor mapping expert indices from the global expert space to the local expert space of the expert parallel shard. - apply_router_weight_on_input: When True, apply the weights to the activations, before quantization + dispatching. - quant_config: Quantization info provided by the fused experts. - defer_input_quant: Runtime parameter indicating whether or not to defer input quantization to the FusedMoEExpertsModular in cases where the compute kernel expects unquantized inputs

Returns a tuple of: - quantized + dispatched a. - Optional quantized + dispatched a1_scales. - Optional ExpertTokensMetadata containing gpu/cpu tensors as big as the number of local experts with the information about the number of tokens assigned to each local expert. - Optional dispatched expert topk IDs - Optional dispatched expert topk weight

## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


###

`prepare_async(a1, topk_weights, topk_ids, num_experts, expert_map, apply_router_weight_on_input, quant_config, defer_input_quant)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalizeModular.prepare_async)

Perform any quantization (and/or) dispatching needed for this kernel but do not wait for results from other workers. - a1: The (unquantized) input to the MoE layer. - a1_scale: Optional scales for a1 - a2_scale: Optional scales for the second MoE gemm. Required to make sure the quantization is consistent for both gemms. - topk_ids: The topk ids. - topk_weights: The topk weights. - num_experts: The total number of experts in the global expert space. - expert_map: A tensor mapping expert indices from the global expert space to the local expert space of the expert parallel shard. - apply_router_weight_on_input: When True, apply the weights to the activations, before quantization + dispatching. - defer_input_quant: Runtime parameter indicating whether or not to defer input quantization to the FusedMoEExpertsModular in cases where the compute kernel expects unquantized inputs

Returns a callback or a hook callback pair that when invoked waits for results from other workers and has the same return signature as `prepare`

, if a hook is returned this is more lightweight check that the recv is complete without doing extra work (used by DBO, will be refactored in the very near future)

e.g.

ret = obj.prepare_async(...)

if isinstance(ret, tuple): hook, receiver = ret hook()

if hook is not None: a, a_scales, expert_meta, topk_ids, topk_weights = receiver()

is equivalent to:

a, a_scales, expert_meta, topk_ids, topk_weights = obj.prepare(...)

## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


##

`FusedMoEPrepareAndFinalizeMonolithic`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalizeMonolithic)

Bases: [FusedMoEPrepareAndFinalize](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalize)

An abstract base class for the [Quantize-Prepare] and [Finalize] steps described above for the monolithic case.

Methods:

-
–[finalize](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalizeMonolithic.finalize)Optional method for subclasses compatible with monolithic

-
–[prepare](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalizeMonolithic.prepare)Optional method for subclasses compatible with monolithic


## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


###

`finalize(fused_expert_output)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalizeMonolithic.finalize)

Optional method for subclasses compatible with monolithic FusedMoEExpertsModular kernels.

Perform any combine plus apply weights and perform a reduction on the fused experts output. - fused_expert_output: The unweighted, unreduced output of the fused experts, it will have (M, topk, K) shape.

## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


###

`prepare(a1, router_logits, quant_config, defer_input_quant=False)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalizeMonolithic.prepare)

Optional method for subclasses compatible with monolithic FusedMoEExpertsModular kernels.

Perform any quantization (and/or) dispatching needed for this kernel. - a1: The (unquantized) input to the MoE layer. - quant_config: Quantization info provided by the fused experts. - defer_input_quant: Runtime parameter indicating whether or not to defer input quantization to the FusedMoEExpertsModular

Returns a tuple of: - quantized + dispatched a. - Optional quantized + dispatched a1_scales.

## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


##

`TopKWeightAndReduce`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.TopKWeightAndReduce)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

An abstract base class for weight application and reduction implementations.

Methods:

-
–[apply](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.TopKWeightAndReduce.apply)Apply topk_weights to the fused_experts_outputs and/or reduce.


## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


###

`apply(output, fused_expert_output, topk_weights, topk_ids, apply_router_weight_on_input)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.modular_kernel.TopKWeightAndReduce.apply)

Apply topk_weights to the fused_experts_outputs and/or reduce. If an output tensor is not passed, it will be created in the function.