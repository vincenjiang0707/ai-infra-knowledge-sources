source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.fused_moe`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe)

Modules:

-
–[activation](https://docs.vllm.ai/activation/#vllm.model_executor.layers.fused_moe.activation)MoE activation function enum and utilities.

-
–[all2all_utils](https://docs.vllm.ai/all2all_utils/#vllm.model_executor.layers.fused_moe.all2all_utils) -
–[b12x](https://docs.vllm.ai/b12x/#vllm.model_executor.layers.fused_moe.b12x)b12x modular tensor-parallel fused MoE backend.

-
–[config](https://docs.vllm.ai/config/#vllm.model_executor.layers.fused_moe.config) -
–[deep_gemm_utils](https://docs.vllm.ai/deep_gemm_utils/#vllm.model_executor.layers.fused_moe.deep_gemm_utils)Taken from https://github.com/ModelTC/LightLLM/blob/8ed97c74c18f11505b048b1ba00ba5c0cef8bff6/lightllm/common/fused_moe/deepep_scatter_gather.py

-
–[expert_map_manager](https://docs.vllm.ai/expert_map_manager/#vllm.model_executor.layers.fused_moe.expert_map_manager)Expert Map Manager for MoE layers.

-
–[experts](https://docs.vllm.ai/experts/#vllm.model_executor.layers.fused_moe.experts) -
–[fused_flydsl_moe](https://docs.vllm.ai/fused_flydsl_moe/#vllm.model_executor.layers.fused_moe.fused_flydsl_moe)Fused MoE Triton kernels.

-
–[fused_moe](https://docs.vllm.ai/fused_moe/#vllm.model_executor.layers.fused_moe.fused_moe)Fused MoE Triton kernels.

-
–[fused_moe_method_base](https://docs.vllm.ai/fused_moe_method_base/#vllm.model_executor.layers.fused_moe.fused_moe_method_base) -
–[hpc_moe](https://docs.vllm.ai/hpc_moe/#vllm.model_executor.layers.fused_moe.hpc_moe) -
–[layer](https://docs.vllm.ai/layer/#vllm.model_executor.layers.fused_moe.layer) -
–[modular_kernel](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel) -
–[moe_align_block_size](https://docs.vllm.ai/moe_align_block_size/#vllm.model_executor.layers.fused_moe.moe_align_block_size) -
–[moe_fused_mul_sum](https://docs.vllm.ai/moe_fused_mul_sum/#vllm.model_executor.layers.fused_moe.moe_fused_mul_sum) -
–[moe_output](https://docs.vllm.ai/moe_output/#vllm.model_executor.layers.fused_moe.moe_output)Output contract between a MoE layer and a consumer that fuses its tail.

-
–[moe_permute_unpermute](https://docs.vllm.ai/moe_permute_unpermute/#vllm.model_executor.layers.fused_moe.moe_permute_unpermute) -
–[oracle](https://docs.vllm.ai/oracle/#vllm.model_executor.layers.fused_moe.oracle) -
–[prepare_finalize](https://docs.vllm.ai/prepare_finalize/#vllm.model_executor.layers.fused_moe.prepare_finalize) -
–[routed_experts](https://docs.vllm.ai/routed_experts/#vllm.model_executor.layers.fused_moe.routed_experts) -
–[routed_experts_capturer](https://docs.vllm.ai/routed_experts_capturer/#vllm.model_executor.layers.fused_moe.routed_experts_capturer) -
–[router](https://docs.vllm.ai/router/#vllm.model_executor.layers.fused_moe.router) -
–[runner](https://docs.vllm.ai/runner/#vllm.model_executor.layers.fused_moe.runner) -
–[topk_weight_and_reduce](https://docs.vllm.ai/topk_weight_and_reduce/#vllm.model_executor.layers.fused_moe.topk_weight_and_reduce) -
–[unquantized_fused_moe_method](https://docs.vllm.ai/unquantized_fused_moe_method/#vllm.model_executor.layers.fused_moe.unquantized_fused_moe_method) -
–[utils](https://docs.vllm.ai/utils/#vllm.model_executor.layers.fused_moe.utils)

Classes:

-
–[ApplyMoEActivationConfig](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.ApplyMoEActivationConfig)Configuration forwarded to

`apply_moe_activation`

. -
–[BatchedDeepGemmExperts](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.BatchedDeepGemmExperts) -
–[BatchedTritonExperts](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.BatchedTritonExperts)A Triton based MoE expert class that operates on expert batched format,

-
–[CutlassBatchedExpertsFp8](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.CutlassBatchedExpertsFp8)Batched CUTLASS FP8 fused MoE expert implementation.

-
–[CutlassExpertsFp8](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.CutlassExpertsFp8)CUTLASS FP8 fused MoE expert implementation.

-
–[DeepGemmExperts](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.DeepGemmExperts)DeepGemm-based fused MoE expert implementation.

-
–[FusedMoEActivationFormat](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEActivationFormat)The standard activation format (num_tokens, hidden dim).

-
–[FusedMoEConfig](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEConfig) -
–[FusedMoEExpertsModular](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEExpertsModular)An abstract base class for the [Permute-Experts-Unpermute] step described

-
–[FusedMoEMethodBase](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEMethodBase) -
–[FusedMoEParallelConfig](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEParallelConfig) -
–[FusedMoEPrepareAndFinalizeModular](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEPrepareAndFinalizeModular)An abstract base class for the [Quantize-Prepare] and [Finalize] steps

-
–[FusedMoEQuantConfig](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEQuantConfig)The FusedMoEQuantConfig contains all the quantization parameters for

-
–[FusedMoERouter](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoERouter)FusedMoERouter is an abstract class that provides a 'select_experts'

-
–[GateLinear](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.GateLinear)MoE gate linear layer with multi-tier GEMM dispatch:

-
–[GroupedTopk](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.GroupedTopk)GroupedTopk used by the Deepseek-V2 and Deepseek-V3 model.

-
–[MoEActivation](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoEActivation)Activation functions for MoE layers.

-
–[MoERunner](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoERunner)Standard MoE runner implementation for executing Mixture of Experts layers.

-
–[RoutedExperts](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts)Container for routed expert weights and execution logic.

-
–[SharedExperts](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.SharedExperts) -
–[TritonExperts](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.TritonExperts)Triton-based fused MoE expert implementation.

-
–[TritonOrDeepGemmExperts](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.TritonOrDeepGemmExperts)DeepGemm with fallback to Triton for low latency shapes.

-
–[UnquantizedFusedMoEMethod](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.UnquantizedFusedMoEMethod)MoE method without quantization.


Functions:

-
–[FusedMoEFactory](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory)Factory function for creating MoE execution pipeline.

-
–[activation_without_mul](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.activation_without_mul)Get the non-gated variant of an activation function.

-
–[apply_moe_activation](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.apply_moe_activation)Apply MoE activation function.

-
–[fused_experts](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_experts)Run fused MoE expert computation using Triton kernels.

-
–[fused_moe_make_expert_params_mapping](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe_make_expert_params_mapping)Delegate to EPLB manager.


##

`ApplyMoEActivationConfig`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.ApplyMoEActivationConfig)

Configuration forwarded to `apply_moe_activation`

.

Methods:

-
–[from_configs](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.ApplyMoEActivationConfig.from_configs)Build from the model and quantization configurations.


## Source code in `vllm/model_executor/layers/fused_moe/activation.py`


###

`from_configs(moe_config, quant_config)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.ApplyMoEActivationConfig.from_configs)

Build from the model and quantization configurations.

## Source code in `vllm/model_executor/layers/fused_moe/activation.py`


##

`BatchedDeepGemmExperts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.BatchedDeepGemmExperts)

Bases: [FusedMoEExpertsModular](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular)

Methods:

-
–[__init__](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.BatchedDeepGemmExperts.__init__)max_num_tokens: Maximum number of tokens from a DP Rank

-
–[supports_packed_ue8m0_act_scales](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.BatchedDeepGemmExperts.supports_packed_ue8m0_act_scales)DeepGemm supports packed ue8m0 activation scales on Blackwell-family


## Source code in `vllm/model_executor/layers/fused_moe/experts/batched_deep_gemm_moe.py`


|
|

###

`__init__(moe_config, quant_config, max_num_tokens, num_dispatchers)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.BatchedDeepGemmExperts.__init__)

max_num_tokens: Maximum number of tokens from a DP Rank num_dispatchers: The number of DP dispatchers. quant_config: Quantization configuration

## Source code in `vllm/model_executor/layers/fused_moe/experts/batched_deep_gemm_moe.py`


###

`supports_packed_ue8m0_act_scales()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.BatchedDeepGemmExperts.supports_packed_ue8m0_act_scales)

DeepGemm supports packed ue8m0 activation scales on Blackwell-family GPUs (SM100 datacenter and SM120 consumer).

## Source code in `vllm/model_executor/layers/fused_moe/experts/batched_deep_gemm_moe.py`


##

`BatchedTritonExperts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.BatchedTritonExperts)

Bases: [FusedMoEExpertsModular](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular)

A Triton based MoE expert class that operates on expert batched format, i.e. E x max_num_tokens x K. This is the format that the batched dispatch/combine kernels use.

## Source code in `vllm/model_executor/layers/fused_moe/experts/fused_batched_moe.py`


|
|

##

`CutlassBatchedExpertsFp8`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.CutlassBatchedExpertsFp8)

Bases: `CutlassExpertsFp8Base`


Batched CUTLASS FP8 fused MoE expert implementation.

## Source code in `vllm/model_executor/layers/fused_moe/experts/cutlass_moe.py`


##

`CutlassExpertsFp8`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.CutlassExpertsFp8)

Bases: `CutlassExpertsFp8Base`


CUTLASS FP8 fused MoE expert implementation.

## Source code in `vllm/model_executor/layers/fused_moe/experts/cutlass_moe.py`


##

`DeepGemmExperts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.DeepGemmExperts)

Bases: [FusedMoEExpertsModular](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular)

DeepGemm-based fused MoE expert implementation.

## Source code in `vllm/model_executor/layers/fused_moe/experts/deep_gemm_moe.py`


|
|

##

`FusedMoEActivationFormat`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEActivationFormat)

Bases: [Enum](https://docs.python.org/3/library/enum.html#enum.Enum)

The standard activation format (num_tokens, hidden dim).

Attributes:

-
–[Standard](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEActivationFormat.Standard)The batched experts format (num experts, max tokens per expert, hidden dim)


## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


###

`Standard = ('standard',)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEActivationFormat.Standard)

The batched experts format (num experts, max tokens per expert, hidden dim)

##

`FusedMoEConfig`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEConfig)

Methods:

-
–[should_defer_moe_finalize](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEConfig.should_defer_moe_finalize)Return whether this invocation may defer the top-k reduction.


Attributes:

-
([use_deferred_moe_finalize](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEConfig.use_deferred_moe_finalize)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether experts may return an unfinalized output on this deployment.

-
([w13_num_shards](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEConfig.w13_num_shards)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of shards fused into w13: gate and up for gated, up only.


## Source code in `vllm/model_executor/layers/fused_moe/config.py`


|
|

###

`use_deferred_moe_finalize`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEConfig.use_deferred_moe_finalize)

Whether experts may return an unfinalized output on this deployment.

Evaluated on read rather than in `__post_init__`

because `defer_moe_finalize`

is set after construction, like `skip_final_all_reduce`

.

###

`w13_num_shards`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEConfig.w13_num_shards)

Number of shards fused into w13: gate and up for gated, up only.

###

`should_defer_moe_finalize(num_tokens)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEConfig.should_defer_moe_finalize)

Return whether this invocation may defer the top-k reduction.

## Source code in `vllm/model_executor/layers/fused_moe/config.py`


##

`FusedMoEExpertsModular`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEExpertsModular)

Bases: [FusedMoEExperts](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExperts)

An abstract base class for the [Permute-Experts-Unpermute] step described above.

Methods:

-
–[adjust_N_for_activation](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEExpertsModular.adjust_N_for_activation)Calculate the output dimension for the activation function.

-
–[apply](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEExpertsModular.apply)This function computes the intermediate result of a Mixture of Experts

-
–[moe_problem_size](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEExpertsModular.moe_problem_size)Extract the MoE problem size from the given tensor arguments:

-
–[workspace_dtype](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEExpertsModular.workspace_dtype)Workspace type: The dtype to use for the workspace tensors.

-
–[workspace_shapes](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEExpertsModular.workspace_shapes)Compute the shapes for the temporary and final outputs of the two gemms


## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


|
|

###

`adjust_N_for_activation(N, activation)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEExpertsModular.adjust_N_for_activation)

Calculate the output dimension for the activation function.

For *_no_mul activations (e.g. relu2_no_mul), there's no gate/up split, so output size equals input size (N).

For regular gated activations (e.g., silu, gelu, swigluoai), output size is N // 2 due to gate × activation(up) multiplication.

Parameters:

-

(`N`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEExpertsModular.adjust_N_for_activation(N))

) –[int](https://docs.python.org/3/builtins/functions.html#int)The intermediate size (width of w1/w3 weights).

-

(`activation`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEExpertsModular.adjust_N_for_activation(activation))

) –[MoEActivation](https://docs.vllm.ai/activation/#vllm.model_executor.layers.fused_moe.activation.MoEActivation)The activation function enum.


Returns:

-

–[int](https://docs.python.org/3/builtins/functions.html#int)The output dimension after activation.


## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


###

`apply(output, hidden_states, w1, w2, topk_weights, topk_ids, activation, global_num_experts, expert_map, a1q_scale, a2_scale, workspace13, workspace2, expert_tokens_meta, apply_router_weight_on_input)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEExpertsModular.apply)

This function computes the intermediate result of a Mixture of Experts (MoE) layer using two sets of weights, w1 and w2.

Parameters:

-

(`output`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEExpertsModular.apply(output))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(torch.Tensor): The unweighted, unreduced output tensor.

-

(`hidden_states`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEExpertsModular.apply(hidden_states))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(torch.Tensor): The (quantized) input tensor to the MoE layer.

-

(`w1`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEExpertsModular.apply(w1))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The first set of expert weights.

-

(`w2`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEExpertsModular.apply(w2))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The second set of expert weights.

-

(`topk_weights`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEExpertsModular.apply(topk_weights))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)A map of row to expert weights. Some implementations choose to do weight application.

-

(`topk_ids`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEExpertsModular.apply(topk_ids))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)A map of row to expert id.

-

(`activation`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEExpertsModular.apply(activation))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The activation function to apply after the first MoE layer.

-

(`global_num_experts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEExpertsModular.apply(global_num_experts))

) –[int](https://docs.python.org/3/builtins/functions.html#int)The total number of experts in the global expert space.

-

(`expert_map`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEExpertsModular.apply(expert_map))`Optional[`

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]A tensor mapping expert indices from the global expert space to the local expert space of the expert parallel shard.

-

(`a1q_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEExpertsModular.apply(a1q_scale))`Optional[`

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]Optional quantized scale to be used for a1. Result of quantization from prepare/finalize and not from the FusedMoEQuantConfig.

-

(`a2_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEExpertsModular.apply(a2_scale))`Optional[`

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]Optional quantized scale to be used for the second gemm's activations.

-

(`workspace13`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEExpertsModular.apply(workspace13))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)A scratch tensor used for gemm outputs must be large enough to hold output of either MoE gemm.

-

(`workspace2`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEExpertsModular.apply(workspace2))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)A scratch tensor used for the activation function.

-

(`expert_tokens_meta`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEExpertsModular.apply(expert_tokens_meta))`Optional[`

) –[ExpertTokensMetadata](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.ExpertTokensMetadata)]An optional ExpertTokensMetadata object containing gpu/cpu tensors as big as the number of local experts with the information about the number of tokens assigned to each local expert.

-

(`apply_router_weight_on_input`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEExpertsModular.apply(apply_router_weight_on_input))

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)True if router weights are already applied on the input. This is relevant if the implementation chooses to do weight application.


## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


###

`moe_problem_size(a1, w1, w2, topk_ids)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEExpertsModular.moe_problem_size)

Extract the MoE problem size from the given tensor arguments: - a: The hidden states, input to the MoE layer. - w1: The first set of expert weights. - w2: The second set of expert weights. - topk_ids: The topk ids.

Note: extracting the problem shape from the weight and activation tensors is not obvious. It needs to be done this way specifically due to subtle issues with particular kernels, e.g. the int4 kernels divide the trailing dimension by two, so it's not "correct" to extract N or K from the trailing dimension of w1 or w2. Similarly, some kernels transpose the weights, so this needs to be kept in mind.

Note: This implementation covers most cases. However, if experts require a specialized implementation, like MarlinExperts, they are free to override this function.

## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


###

`workspace_dtype(act_dtype)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEExpertsModular.workspace_dtype)

###

`workspace_shapes(M, N, K, topk, global_num_experts, local_num_experts, expert_tokens_meta, activation)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEExpertsModular.workspace_shapes)

Compute the shapes for the temporary and final outputs of the two gemms and activation in the fused expert function. Since the gemms are independent, the workspace for the first gemm can be shared with the workspace for the last gemm.

Inputs: - M: number of tokens. - N: Row (or column) dimension of expert weights. - K: hidden dimension - topk: The number of top-k experts to select. - global_num_experts: global number of experts. - local_num_experts: local number of experts due to DP/EP. - expert_tokens_meta: number of tokens per expert metadata for batched format.

Returns a tuple of: - workspace13 shape tuple: must be large enough to hold the result of either expert gemm. - workspace2 shape tuple: must be large enough to hold the result of the activation function. - output shape tuple: must be exact size of the final gemm output. - Note: workspace shapes can be 0 if the workspace is not needed. But in order for activation chunking to work, the first dimension of each tuple must be the number of tokens when the shape is not 0.

## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


##

`FusedMoEMethodBase`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEMethodBase)

Bases: [QuantizeMethodBase](https://docs.vllm.ai/quantization/base_config/#vllm.model_executor.layers.quantization.base_config.QuantizeMethodBase)

Methods:

-
–[apply](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEMethodBase.apply)Apply the MoE operation using modular kernels.

-
–[apply_monolithic](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEMethodBase.apply_monolithic)Apply the MoE operation using monolithic kernels.

-
–[maybe_roundup_sizes](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEMethodBase.maybe_roundup_sizes)Given layer hidden size and intermediate size per partition and MoE

-
–[uses_weight_scale_2_pattern](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEMethodBase.uses_weight_scale_2_pattern)Returns True if this quantization method uses 'weight_scale_2' pattern


Attributes:

-
([has_unpadded_output](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEMethodBase.has_unpadded_output)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Indicates that the hidden_states output might be the unpadded

-
([skip_forward_padding](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEMethodBase.skip_forward_padding)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to skip the padding in the forward before applying the moe method.


## Source code in `vllm/model_executor/layers/fused_moe/fused_moe_method_base.py`


|
|

###

`has_unpadded_output`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEMethodBase.has_unpadded_output)

Indicates that the hidden_states output might be the unpadded hidden_states shape rather than the full padded shape.

###

`skip_forward_padding`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEMethodBase.skip_forward_padding)

Whether to skip the padding in the forward before applying the moe method.

###

`apply(layer, x, topk_weights, topk_ids, shared_experts, shared_experts_input)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEMethodBase.apply)

Apply the MoE operation using modular kernels.

Parameters:

-

(`layer`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEMethodBase.apply(layer))

) –[RoutedExperts](https://docs.vllm.ai/routed_experts/#vllm.model_executor.layers.fused_moe.routed_experts.RoutedExperts)RoutedExperts instance containing weight parameters

-

(`x`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEMethodBase.apply(x))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input tensor

-

(`topk_weights`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEMethodBase.apply(topk_weights))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Expert weights from router

-

(`topk_ids`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEMethodBase.apply(topk_ids))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Selected expert IDs from router

-

(`shared_experts_input`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEMethodBase.apply(shared_experts_input))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| NoneInput for shared experts (if any)

-

(`shared_experts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEMethodBase.apply(shared_experts))

) –[SharedExperts](https://docs.vllm.ai/runner/shared_experts/#vllm.model_executor.layers.fused_moe.runner.shared_experts.SharedExperts)| NoneThe shared experts module, if any


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Output tensor from routed experts.


## Source code in `vllm/model_executor/layers/fused_moe/fused_moe_method_base.py`


###

`apply_monolithic(layer, x, router_logits, input_ids=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEMethodBase.apply_monolithic)

Apply the MoE operation using monolithic kernels.

Parameters:

-

(`layer`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEMethodBase.apply_monolithic(layer))

) –[RoutedExperts](https://docs.vllm.ai/routed_experts/#vllm.model_executor.layers.fused_moe.routed_experts.RoutedExperts)RoutedExperts instance containing weight parameters

-

(`x`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEMethodBase.apply_monolithic(x))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input tensor

-

(`router_logits`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEMethodBase.apply_monolithic(router_logits))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Router logits (routing done internally)

-

(`input_ids`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEMethodBase.apply_monolithic(input_ids))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Token ids, for routers that condition on them


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)|[UnfinalizedMoEOutput](https://docs.vllm.ai/moe_output/#vllm.model_executor.layers.fused_moe.moe_output.UnfinalizedMoEOutput)Finalized routed states or a deferred-finalize output.


## Source code in `vllm/model_executor/layers/fused_moe/fused_moe_method_base.py`


###

`maybe_roundup_sizes(hidden_size, intermediate_size_per_partition, act_dtype, moe_parallel_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEMethodBase.maybe_roundup_sizes)

Given layer hidden size and intermediate size per partition and MoE configurations, round up hidden_size and intermediate_size_per_partition if necessary.

Parameters:

-

(`hidden_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEMethodBase.maybe_roundup_sizes(hidden_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Layer hidden-size

-

(`intermediate_size_per_partition`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEMethodBase.maybe_roundup_sizes(intermediate_size_per_partition))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Intermediate size per partition for the layer.

-

(`act_dtype`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEMethodBase.maybe_roundup_sizes(act_dtype))

) –[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)Data type of the layer activations.

-

(`moe_parallel_config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEMethodBase.maybe_roundup_sizes(moe_parallel_config))

) –[FusedMoEParallelConfig](https://docs.vllm.ai/config/#vllm.model_executor.layers.fused_moe.config.FusedMoEParallelConfig)Fused MoE parallelization strategy configuration.


## Return

A tuple of (rounded_hidden_size, rounded_intermediate_size_per_partition), where: - rounded_hidden_size is the possibly rounded up hidden size. - rounded_intermediate_size_per_partition is the possibly rounded up intermediate size per partition.

## Source code in `vllm/model_executor/layers/fused_moe/fused_moe_method_base.py`


###

`uses_weight_scale_2_pattern()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEMethodBase.uses_weight_scale_2_pattern)

Returns True if this quantization method uses 'weight_scale_2' pattern for per-tensor weight scales (e.g., FP4 variants), False otherwise.

This method should be overridden by subclasses that use the 'weight_scale_2' pattern instead of the standard 'weight_scale' pattern.

## Source code in `vllm/model_executor/layers/fused_moe/fused_moe_method_base.py`


##

`FusedMoEParallelConfig`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEParallelConfig)

Methods:

-
–[make](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEParallelConfig.make)Determine MoE parallel configuration. Based on the input

`tp_size_`

, -
–[make_no_parallel](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEParallelConfig.make_no_parallel)For usage in CI/CD and testing.


## Source code in `vllm/model_executor/layers/fused_moe/config.py`


|
|

###

`make(tp_size_, pcp_size_, dp_size_, sp_size_, vllm_parallel_config)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEParallelConfig.make)

Determine MoE parallel configuration. Based on the input `tp_size_`

, `dp_size_`

and vllm's parallel config, determine what level's of parallelism to use in the fused moe layer.

Parameters:

-

(`tp_size_`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEParallelConfig.make(tp_size_))

) –[int](https://docs.python.org/3/builtins/functions.html#int)`tp_size`

passed into the FusedMoEFactory constructor. -

(`pcp_size_`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEParallelConfig.make(pcp_size_))

) –[int](https://docs.python.org/3/builtins/functions.html#int)`pcp_size`

passed into the FusedMoEFactory constructor. -

(`dp_size_`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEParallelConfig.make(dp_size_))

) –[int](https://docs.python.org/3/builtins/functions.html#int)`dp_size`

passed into the FusedMoEFactory constructor. -

(`sp_size_`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEParallelConfig.make(sp_size_))

) –[int](https://docs.python.org/3/builtins/functions.html#int)`sp_size`

passed into the FusedMoEFactory constructor. -

(`vllm_parallel_config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEParallelConfig.make(vllm_parallel_config))

) –[ParallelConfig](https://docs.vllm.ai/config/#vllm.config.ParallelConfig)vLLM's parallel config object which contains the

`enable_expert_parallel`

flag.

Examples:

When there is no parallelism requested, i.e. `tp_size_`

= `pcp_size_`

= `dp_size_`

= 1, we simply return the sizes unaltered and the ranks set to 0.

Expert Parallelism is considered only when either `dp_size_`

, `pcp_size_`

or `tp_size_`

is non trivial.

Note that PCP serves the same function as DP here.

When TP = 2, DP(PCP) = 1 and EP = False, the configuration on different devices:

- device 0 : TP = {2, 0} DP = {1, 0} EP = {1, 0} // legend : {size, rank}
- device 1 : TP = {2, 1} DP = {1, 0} EP = {1, 0}
- Comment : Tensors are sharded across 2 devices.

When TP = 1, DP(PCP) = 2 and EP = False, the configuration on different devices:

- device 0 : TP = {2, 0} DP = {2, 0} EP = {1, 0}
- device 1 : TP = {2, 1} DP = {2, 1} EP = {1, 0}
- Comment: There are 2 engine instances and the tensors are sharded across 2 decvices.

When TP = 2, DP(PCP) = 2 and EP = False, the configuration on different devices:

- device 0: TP = {4, 0} DP = {2, 0} EP = {1, 0}
- device 1: TP = {4, 1} DP = {2, 0} EP = {1, 0}
- device 2: TP = {4, 2} DP = {2, 1} EP = {1, 0}
- device 3: TP = {4, 3} DP = {2, 1} EP = {1, 0}
- Comment: There are 2 engine instances and the tensors are sharded across 4 devices.

When, TP = 2, DP(PCP) = 1 and EP = True, the configuration on different devices:

- device 0: TP = {1, 0} DP = {1, 0} EP = {2, 0}
- device 1: TP = {1, 0} DP = {1, 0} EP = {2, 1}
- Comment: The experts are split between the 2 devices.

When, TP = 1, DP(PCP) = 2 and EP = True, the configuration on different devices:

- device 0: TP = {1, 0} DP = {2, 0} EP = {2, 0}
- device 1: TP = {1, 0} DP = {2, 1} EP = {2, 1}
- Comment: There are 2 engine instances and the experts are split between the 2 devices.

When TP = 2, DP(PCP) = 2 and EP = True, the configuration on different devices:

- device 0: TP = {1, 0} DP = {2, 0} EP = {4, 0}
- device 1: TP = {1, 0} DP = {2, 0} EP = {4, 1}
- device 2: TP = {1, 0} DP = {2, 1} EP = {4, 2}
- device 3: TP = {1, 0} DP = {2, 1} EP = {4, 3}
- Comment: There are 2 engine instances and the experts are split between the 4 devices.

## Source code in `vllm/model_executor/layers/fused_moe/config.py`


|
|

###

`make_no_parallel()`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEParallelConfig.make_no_parallel)

For usage in CI/CD and testing.

## Source code in `vllm/model_executor/layers/fused_moe/config.py`


##

`FusedMoEPrepareAndFinalizeModular`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEPrepareAndFinalizeModular)

Bases: [FusedMoEPrepareAndFinalize](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalize)

An abstract base class for the [Quantize-Prepare] and [Finalize] steps described above for the Modular case.

Methods:

-
–[finalize](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEPrepareAndFinalizeModular.finalize)Perform any combine plus apply weights and perform a reduction on the

-
–[finalize_async](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEPrepareAndFinalizeModular.finalize_async)Perform any combine plus apply weights and perform a reduction on the

-
–[prepare](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEPrepareAndFinalizeModular.prepare)Perform any quantization (and/or) dispatching needed for this kernel.

-
–[prepare_async](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEPrepareAndFinalizeModular.prepare_async)Perform any quantization (and/or) dispatching needed for this kernel


## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


|
|

###

`finalize(output, fused_expert_output, topk_weights, topk_ids, apply_router_weight_on_input, weight_and_reduce_impl)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEPrepareAndFinalizeModular.finalize)

Perform any combine plus apply weights and perform a reduction on the fused experts output. - output: The output tensor, written in place. Must be (M, K) shape. - fused_expert_output: The unweighted, unreduced output of the fused experts, it will have (M, topk, K) shape. - topk_weights: The weights to be applied to the fused_experts_output. - topk_ids: The topk_ids. - apply_router_weight_on_input: When False, apply the weights to fused_expert_output. - weight_and_reduce_impl: An optional TopKWeightAndReduce implementation.

## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


###

`finalize_async(output, fused_expert_output, topk_weights, topk_ids, apply_router_weight_on_input, weight_and_reduce_impl)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEPrepareAndFinalizeModular.finalize_async)

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

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEPrepareAndFinalizeModular.prepare)

Perform any quantization (and/or) dispatching needed for this kernel. - a1: The (unquantized) input to the MoE layer. - topk_ids: The topk ids. - topk_weights: The topk weights. - num_experts: The total number of experts in the global expert space. - expert_map: A tensor mapping expert indices from the global expert space to the local expert space of the expert parallel shard. - apply_router_weight_on_input: When True, apply the weights to the activations, before quantization + dispatching. - quant_config: Quantization info provided by the fused experts. - defer_input_quant: Runtime parameter indicating whether or not to defer input quantization to the FusedMoEExpertsModular in cases where the compute kernel expects unquantized inputs

Returns a tuple of: - quantized + dispatched a. - Optional quantized + dispatched a1_scales. - Optional ExpertTokensMetadata containing gpu/cpu tensors as big as the number of local experts with the information about the number of tokens assigned to each local expert. - Optional dispatched expert topk IDs - Optional dispatched expert topk weight

## Source code in `vllm/model_executor/layers/fused_moe/modular_kernel.py`


###

`prepare_async(a1, topk_weights, topk_ids, num_experts, expert_map, apply_router_weight_on_input, quant_config, defer_input_quant)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEPrepareAndFinalizeModular.prepare_async)

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

`FusedMoEQuantConfig`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEQuantConfig)

The FusedMoEQuantConfig contains all the quantization parameters for a single FusedMoEMethodBase operation. It consists of four FusedMoEQuantDescs, one for each activation and set of weights.

Each FusedMoEMethodBase must implement a get_fused_moe_quant_config method to construct a FusedMoEQuantConfig for use with that class.

FusedMoEQuant configs are only used for modular kernels, fused_experts (from fused_moe.py), cutlass_moe_fp[48], rocm_aiter_fused_experts and triton_kernel_moe_forward. Other MoE methods can ignore the FusedMoEQuantConfig (for now) and hardcode it to None.

There are currently some restrictions on what can be expressed: - Most MoE ops only support similar quantization strategies for each parameter, e.g. both weights must have the same GroupShape and both activations must share the same GroupShape. One exception to this is the cutlass moe which allows per channel quantization on the outputs. Note: this restrictions are not always rigorously checked. - Not all fused MoE functions support all the parameters, e.g. zero points, global scales, alphas and biases are not universally supported. - Fully general GroupShapes are not allowed. Activations only support per token, per tensor or K-blocked. - Weights are not required to have a GroupShape since they have already been quantized.

Other notes: - PrecisionConfigs are specific to GPT OSS Triton. - As a follow up it would probably make sense to subclass FusedMoEQuantDesc or FusedMoEQuantConfig for particular FusedMoEMethodBase subclasses so that only the required quantization parameters are used/stored.

Methods:

-
–[batched_scale_shape](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEQuantConfig.batched_scale_shape)Construct the proper activation batched scale shape for this

-
–[config_name](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEQuantConfig.config_name)Return a string used to construct the filename that contains the

-
–[make](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEQuantConfig.make)General builder function for a FusedMoEQuantConfig.

-
–[scale_shape](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEQuantConfig.scale_shape)Construct the proper activation scale shape for this


## Source code in `vllm/model_executor/layers/fused_moe/config.py`


|
|

###

`batched_scale_shape(num_experts, max_tokens, hidden_dim)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEQuantConfig.batched_scale_shape)

Construct the proper activation batched scale shape for this config, e.g. (num experts, *scale_shape).

## Source code in `vllm/model_executor/layers/fused_moe/config.py`


###

`config_name(dtype)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEQuantConfig.config_name)

Return a string used to construct the filename that contains the tuning info for a particular quantization scheme. See try_get_optimal_moe_config in fused_moe.py.

## Source code in `vllm/model_executor/layers/fused_moe/config.py`


###

`make(quant_dtype=None, per_act_token_quant=False, per_out_ch_quant=False, block_shape=None, w1_scale=None, w2_scale=None, a1_scale=None, a2_scale=None, g1_alphas=None, g2_alphas=None, a1_gscale=None, a2_gscale=None, w1_bias=None, w2_bias=None, w1_zp=None, w2_zp=None, weight_dtype=None, is_scale_swizzled=True, gemm1_alpha=None, gemm1_beta=None, gemm1_clamp_limit=None)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEQuantConfig.make)

General builder function for a FusedMoEQuantConfig. - quant_dtype: Optional quantization type. None if activations are unquantized or quantized prior to calling. Note: "nvfp4", "mxfp4", "mxfp6_e3m2", "mxfp6_e2m3" are the only valid string values for quant_dtype. - per_act_token_quant: Activations have per token quantization. - per_out_ch_quant: Outputs have per channel quantization. (only for cutlass). - block_shape: Optional block size for block-wise quantization. Incompatible with per_act_token and per_out_ch quant. - w1_scale: Optional scale to be used for w1. - w2_scale: Optional scale to be used for w2. - a1_scale: Optional scale to be used for a1. - a2_scale: Optional scale to be used for a2. - g1_alphas: Optional global quantization scales for w1 (for nvfp4). Optional per-channel scales for w1 (for W4A8 FP8). Optional dq scale i.e. w_scale * a_scale (for W8A8 fp8). - g2_alphas: Optional global quantization scales for w2 (for nvfp4). Optional per-channel scales for w2 (for W4A8 FP8). Optional dq scale i.e. w_scale * a_scale (for W8A8 fp8). - a1_gscale: Optional global quantization scales for a1 (1.0 /a2_scale). - a2_gscale: Optional global quantization scales for a2 (1.0 /a2_scale).

- w1_bias: Optional biases for w1 (GPT OSS Triton).
- w2_bias: Optional biases for w1 (GPT OSS Triton).
- w1_zp: Optional w1 zero points for int4/int8 quantization.
- w2_zp: Optional w2 zero points for int4/int8 quantization.
- is_scale_swizzled: Whether the activation scale-factor layout is swizzled. Pass through to the underlying quantization kernel for dtypes that distinguish layouts (nvfp4, mxfp8). Defaults to True.
- gemm1_alpha: Optional MXFP4 TRTLLM SwiGLU alpha parameter.
- gemm1_beta: Optional MXFP4 TRTLLM SwiGLU beta parameter.
- gemm1_clamp_limit: Optional MXFP4 TRTLLM SwiGLU clamp limit.

## Source code in `vllm/model_executor/layers/fused_moe/config.py`


|
|

###

`scale_shape(max_tokens, hidden_dim)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEQuantConfig.scale_shape)

Construct the proper activation scale shape for this config.

## Source code in `vllm/model_executor/layers/fused_moe/config.py`


##

`FusedMoERouter`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoERouter)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

FusedMoERouter is an abstract class that provides a 'select_experts' method that is used for routing hidden states based on router logits.

Methods:

-
–[select_experts](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoERouter.select_experts)Route the input hidden states to the top-k experts based on the


## Source code in `vllm/model_executor/layers/fused_moe/router/fused_moe_router.py`


###

`select_experts(hidden_states, router_logits, topk_indices_dtype=None, *, input_ids=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoERouter.select_experts)

Route the input hidden states to the top-k experts based on the router logits.

Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(topk_weights, topk_ids)

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)] -

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]The weights and expert ids computation result.

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]**Compatibility**: When EPLB is not enabled, the returned ids are -

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]equivalent to global logical ids, so should be compatible with

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]plain MoE implementations without redundant experts.


## Source code in `vllm/model_executor/layers/fused_moe/router/fused_moe_router.py`


##

`GateLinear`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.GateLinear)

Bases: [ReplicatedLinear](https://docs.vllm.ai/linear/#vllm.model_executor.layers.linear.ReplicatedLinear)

MoE gate linear layer with multi-tier GEMM dispatch:

- cuteDSL ll_bf16_gemm (SM90+, M<=16, bf16 in, fp32 out, K divisible by 8)
- fp32 specialized kernel (SM90+ or gfx950, bf16/fp32 in, fp32 out, M<=32, model-specific shapes)
- bf16x3 CuteDSL kernel (SM100, bf16 in, fp32 weight)
- cuBLAS bf16×bf16→fp32 (SM90+ + bf16 weight + fp32 out_dtype)
- F.linear via ReplicatedLinear (ultimate fallback)

The `out_dtype`

attribute is mutable and can be set after init (e.g. when the required dtype depends on the expert quantization method which is only known later).

A `quant_config`

that actually quantizes the gate disables every specialized tier, leaving plain `ReplicatedLinear`

behavior.

Methods:

-
–[set_out_dtype](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.GateLinear.set_out_dtype)Set output dtype for the router logits after init.


## Source code in `vllm/model_executor/layers/fused_moe/router/gate_linear.py`


|
|

###

`set_out_dtype(out_dtype)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.GateLinear.set_out_dtype)

Set output dtype for the router logits after init.

Useful when the required dtype depends on the expert quantization method which is only known after the gate is constructed.

## Source code in `vllm/model_executor/layers/fused_moe/router/gate_linear.py`


##

`GroupedTopk`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.GroupedTopk)

Bases: [CustomOp](https://docs.vllm.ai/custom_op/#vllm.model_executor.custom_op.CustomOp)

GroupedTopk used by the Deepseek-V2 and Deepseek-V3 model.

## Source code in `vllm/model_executor/layers/fused_moe/router/grouped_topk_router.py`


|
|

##

`MoEActivation`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoEActivation)

Bases: [Enum](https://docs.python.org/3/library/enum.html#enum.Enum)

Activation functions for MoE layers.

Methods:

-
–[from_str](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoEActivation.from_str)Parse from string for backward compatibility.

-
–[without_mul](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoEActivation.without_mul)Get the non-gated variant of this activation.


Attributes:

-
([custom_op_name](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoEActivation.custom_op_name)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Maps to the CustomOp name of activations

-
([is_gated](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoEActivation.is_gated)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Returns True if activation expects gate*activation(up) pattern.


## Source code in `vllm/model_executor/layers/fused_moe/activation.py`


###

`custom_op_name`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoEActivation.custom_op_name)

Maps to the CustomOp name of activations in vllm/model_executor/layers/activation.py.

###

`is_gated`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoEActivation.is_gated)

Returns True if activation expects gate*activation(up) pattern.

Gated activations expect input tensor with 2x the output size, where the first half is the gate and second half is the up projection.

###

`from_str(s)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoEActivation.from_str)

Parse from string for backward compatibility.

## Source code in `vllm/model_executor/layers/fused_moe/activation.py`


###

`without_mul()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoEActivation.without_mul)

Get the non-gated variant of this activation.

For activations that have a _no_mul variant, returns that variant. For activations without a _no_mul variant (or already _no_mul), returns self.

## Source code in `vllm/model_executor/layers/fused_moe/activation.py`


##

`MoERunner`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoERunner)

Bases: [MoERunnerInterface](https://docs.vllm.ai/runner/moe_runner_interface/#vllm.model_executor.layers.fused_moe.runner.moe_runner_interface.MoERunnerInterface)

Standard MoE runner implementation for executing Mixture of Experts layers.

This is the primary concrete implementation of MoE execution logic, providing comprehensive support for standard MoE operations. It handles: - Expert routing and token dispatching using various routing strategies - Shared experts computation with optional parallel execution using CUDA streams - Tensor model parallel and expert parallel operations - Multiple quantization methods and optimized kernel selection - Both monolithic and decomposed expert execution paths - Integration with various parallel execution modes (TP, EP, DP)

The runner orchestrates the complete MoE forward pass including routing tokens to experts, executing expert computations in parallel, and combining results. It supports advanced features like overlapped execution of shared experts, optimized kernels for different parallel configurations, and seamless integration with vLLM's distributed execution framework.

Eventually, this class may be split into more specialized implementations for different configurations (e.g., with/without shared experts, gates, etc.).

Methods:

-
–[apply_routed_input_transform](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoERunner.apply_routed_input_transform)Apply transform for routed experts (e.g., latent projection).

-
–[apply_routed_output_transform](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoERunner.apply_routed_output_transform)Apply transform to routed expert output (e.g., latent to full dim).

-
–[forward](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoERunner.forward)Invoke the fused moe layer.

-
–[set_eplb_state](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoERunner.set_eplb_state)Register the EPLB state in this layer.


Attributes:

-
([expert_local_to_global](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoERunner.expert_local_to_global)

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| NoneRouting table: local expert ID to global expert ID.

-
–[expert_map_manager](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoERunner.expert_map_manager)Forward to routed_experts.expert_map_manager for backward compatibility.

-
([expert_physical_to_global](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoERunner.expert_physical_to_global)

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| NoneRouting table: physical expert ID to global expert ID.


## Source code in `vllm/model_executor/layers/fused_moe/runner/moe_runner.py`


|
|

###

`expert_local_to_global`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoERunner.expert_local_to_global)

Routing table: local expert ID to global expert ID.

###

`expert_map_manager`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoERunner.expert_map_manager)

Forward to routed_experts.expert_map_manager for backward compatibility.

###

`expert_physical_to_global`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoERunner.expert_physical_to_global)

Routing table: physical expert ID to global expert ID.

###

`_apply_quant_method(hidden_states, router_logits, shared_experts_input, input_ids=None, shared_experts_overlapping=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoERunner._apply_quant_method)

Run expert routing and the fused MoE kernel via the quant method.

Orchestrates shared expert execution (before/after), expert selection via the router, and the actual fused MoE computation. Returns (shared_expert_output, fused_expert_output).

`shared_experts_overlapping`

should be True only if using multi-stream overlap. Then the shared expert was already launched in a separate stream, so the results only have to be awaited here.

## Source code in `vllm/model_executor/layers/fused_moe/runner/moe_runner.py`


###

`_forward_impl(hidden_states, router_logits, shared_experts_input, input_ids=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoERunner._forward_impl)

Entry point called by the custom op to run the MoE computation.

Handles pre-dispatch setup (gate application, external shared expert triggering, quant config init) then performs the following steps within the sequence-parallel context.

- Performs expert routing
- fused MoE kernel execution
- shared expert computation.

Returns routed output, optionally paired with shared-expert output. A fused consumer may request the routed output in deferred-finalize form.

## Source code in `vllm/model_executor/layers/fused_moe/runner/moe_runner.py`


###

`_map_global_expert_id_to_local_expert_id(expert_id)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoERunner._map_global_expert_id_to_local_expert_id)

Map global expert ID to local expert ID.

###

`_maybe_add_zero_expert_output(result)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoERunner._maybe_add_zero_expert_output)

Add the zero expert's contribution to the final result.

When a ZeroExpertRouter is used, it computes a bias-like output from the "zero expert" that is added to the combined routed+shared expert output.

## Source code in `vllm/model_executor/layers/fused_moe/runner/moe_runner.py`


###

`_maybe_apply_routed_scale_to_output(shared_output, fused_output)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoERunner._maybe_apply_routed_scale_to_output)

Apply routed_scaling_factor to the output with FP16 overflow protection.

Scale the fused expert output by routed_scaling_factor. For FP16, avoid overflow by dividing shared_output by the scale instead (the decoder layer compensates with matching divisions).

## Source code in `vllm/model_executor/layers/fused_moe/runner/moe_runner.py`


###

`_maybe_fuse_gate_weights()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoERunner._maybe_fuse_gate_weights)

Fuse router and shared expert gate weights on first call.

Cannot be done at **init** because gate weights are loaded after module construction (via weight_loader). Called once from _forward_impl before the first forward pass.

## Source code in `vllm/model_executor/layers/fused_moe/runner/moe_runner.py`


###

`_maybe_pad_hidden_states(shared_experts_input, hidden_states)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoERunner._maybe_pad_hidden_states)

Pad hidden_states to moe_config.hidden_dim and compute the original dimension for later truncation.

For latent MoE, the routed hidden_states may be smaller than hidden_dim. Padding ensures uniform tensor sizes through the fused MoE kernel. The returned trunc_size is used by _maybe_reduce_final_output to strip the padding from the result.

## Source code in `vllm/model_executor/layers/fused_moe/runner/moe_runner.py`


###

`_maybe_reduce_final_output(states, trunc_size, output_is_reduced=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoERunner._maybe_reduce_final_output)

All-reduce the combined output if needed.

This is the "late" all-reduce path. When neither fused nor shared output was individually reduced, the combined sum is all-reduced here. Skipped when sequence-parallel is active (SP handles its own reduction) or when the early path already reduced both outputs.

## Source code in `vllm/model_executor/layers/fused_moe/runner/moe_runner.py`


###

`_maybe_reduce_routed_output_before_transform(fused_output, fused_output_is_reduced)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoERunner._maybe_reduce_routed_output_before_transform)

All-reduce latent routed output before its output transform.

Latent MoE output transforms may contain non-linear ops, e.g. RMSNorm. TP partial routed outputs must be summed in latent space before such transforms are applied.

A transform that commutes with the TP sum is exempt: if `sum_r T(x_r) == T(sum_r x_r)`

, applying the transform to the local partial output and letting the existing late all-reduce sum the combined result is equivalent, and costs one collective instead of two. Such a transform opts out by setting `reduce_commutative = True`

. The default is False, so transforms that do not declare themselves keep being reduced early.

## Source code in `vllm/model_executor/layers/fused_moe/runner/moe_runner.py`


###

`_maybe_reduce_shared_expert_output(shared_output, fused_output_is_reduced=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoERunner._maybe_reduce_shared_expert_output)

All-reduce shared expert output when the combine kernel already reduced fused output.

- If the combine kernel does the reduction for fused_output, reduce shared_output separately. O.w, reduce fused_output+shared_output later.
- If we have SP (TP=N, DP=M, EP), there is a separate AG step handled in the model.

## Source code in `vllm/model_executor/layers/fused_moe/runner/moe_runner.py`


###

`_sequence_parallel_context()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoERunner._sequence_parallel_context)

Return a context manager for sequence-parallel token redistribution.

When sequence parallelism is active, returns a context that handles local size tracking for proper token scatter/gather. Otherwise returns a no-op context.

## Source code in `vllm/model_executor/layers/fused_moe/runner/moe_runner.py`


###

`apply_routed_input_transform(hidden_states)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoERunner.apply_routed_input_transform)

Apply transform for routed experts (e.g., latent projection).

This is called by MoERunner.forward_native. The original hidden_states is saved separately so shared experts get [S, hidden_size] while routed experts get the transformed [S, moe_latent_size].

Returns (possibly transformed) hidden states and the input for shared experts (or None if there are no shared experts).

## Source code in `vllm/model_executor/layers/fused_moe/runner/moe_runner.py`


###

`apply_routed_output_transform(fused_output)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoERunner.apply_routed_output_transform)

Apply transform to routed expert output (e.g., latent to full dim).

Used by latent MoE models (e.g., NemotronH) where routed experts operate in a compressed latent space and need projection back to the full hidden dimension before combining with shared expert output.

## Source code in `vllm/model_executor/layers/fused_moe/runner/moe_runner.py`


###

`forward(hidden_states, router_logits, input_ids=None, shared_experts_input=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoERunner.forward)

Invoke the fused moe layer.

Input: - hidden_states - router_logits

Output: - The new hidden_states.

Calling sequence - forward - self._forward_entry (_moe_forward or _moe_forward_shared custom op) - _forward_impl

Note: The existence of _moe_forward and _moe_forward_shared custom ops are due to the following reason: 1. pytorch cannot handle union types in custom op signatures so _moe_forward and _moe_forward_shared must be split.

## Source code in `vllm/model_executor/layers/fused_moe/runner/moe_runner.py`


|
|

###

`set_eplb_state(moe_layer_idx, expert_load_view, logical_to_physical_map, logical_replica_count)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.MoERunner.set_eplb_state)

Register the EPLB state in this layer.

This is used later in forward pass, where we get the expert mapping and record the load metrics in `expert_load_view`

.

## Source code in `vllm/model_executor/layers/fused_moe/runner/moe_runner.py`


##

`RoutedExperts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts)

Bases: [PluggableLayer](https://docs.vllm.ai/custom_op/#vllm.model_executor.custom_op.PluggableLayer)

Container for routed expert weights and execution logic.

This module owns the expert weight parameters (w13_weight, w2_weight, scales, etc.) and handles: - Loading checkpoint weights into parameters - Executing routed experts via quant_method.apply()

Methods:

-
–[build_expert_params_mapping](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts.build_expert_params_mapping)Create expert parameter mapping for weight loading with redundant experts.

-
–[forward_modular](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts.forward_modular)Execute routed experts using the quantization method's apply function.

-
–[forward_monolithic](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts.forward_monolithic)Execute routed experts using the quantization method's apply function.

-
–[make_expert_params_mapping](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts.make_expert_params_mapping)Build the expert mapping, detecting the LoRA

`base_layer.`

prefix by

## Source code in `vllm/model_executor/layers/fused_moe/routed_experts.py`


|
|

###

`_get_hidden_dim(shard_dim, ndim)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts._get_hidden_dim)

Compute the hidden dimension index from the shard (intermediate) dimension and tensor rank.

For 2D weight tensors the two data dims are (0, 1). For 3D tensors with an expert dimension at dim 0, they are (1, 2). `shard_dim`

occupies one of these; the hidden dimension is the other. For 1D tensors (e.g. per-channel scales) returns 0.

## Source code in `vllm/model_executor/layers/fused_moe/routed_experts.py`


###

`_get_quant_method(prefix, quant_config, moe_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts._get_quant_method)

Helper method to ensure quant_method is never None and of the proper type.

## Source code in `vllm/model_executor/layers/fused_moe/routed_experts.py`


###

`_load_combined_w13_weight_scale(shard_dim, loaded_weight, param, tp_rank)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts._load_combined_w13_weight_scale)

Load w13 weight scales assuming that w1 weight scales and w3 weight scales are stored in the same loaded_weight tensor.

## Source code in `vllm/model_executor/layers/fused_moe/routed_experts.py`


###

`_load_model_weight_or_group_weight_scale(shard_dim, expert_data, shard_id, loaded_weight, tp_rank, is_scale=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts._load_model_weight_or_group_weight_scale)

Load grouped weight scales for group quantization or model weights

Parameters:

-

(`shard_dim`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts._load_model_weight_or_group_weight_scale(shard_dim))

) –[int](https://docs.python.org/3/builtins/functions.html#int)dimension to shard

-

(`expert_data`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts._load_model_weight_or_group_weight_scale(expert_data))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)parameter for a particular expert

-

(`shard_id`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts._load_model_weight_or_group_weight_scale(shard_id))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)either w1, w2, or w3

-

(`loaded_weight`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts._load_model_weight_or_group_weight_scale(loaded_weight))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)checkpoint weight to load into the param

-

(`tp_rank`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts._load_model_weight_or_group_weight_scale(tp_rank))

) –[int](https://docs.python.org/3/builtins/functions.html#int)tensor parallel rank

-

(`is_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts._load_model_weight_or_group_weight_scale(is_scale))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –whether padding should use unit scales instead of zero weights.


## Source code in `vllm/model_executor/layers/fused_moe/routed_experts.py`


###

`_map_global_expert_id_to_local_expert_id(expert_id)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts._map_global_expert_id_to_local_expert_id)

Map global expert ID to local expert ID.

###

`_narrow_expert_data_for_padding(expert_data, loaded_weight, hidden_dim, shard_dim=None)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts._narrow_expert_data_for_padding)

Narrow expert_data to match loaded_weight for padded dimensions.

When backends (e.g., DeepEP) round up hidden_size, weight parameters are larger than checkpoint weights. Narrow the padded hidden dimension before copying. Similarly, when padding occurs on the shard (intermediate) dimension (e.g. for MXFP4 GEMM), narrow that dimension as well.

Parameters:

-

(`expert_data`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts._narrow_expert_data_for_padding(expert_data))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The (possibly padded) parameter tensor to narrow.

-

(`loaded_weight`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts._narrow_expert_data_for_padding(loaded_weight))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The checkpoint weight tensor with original size.

-

(`hidden_dim`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts._narrow_expert_data_for_padding(hidden_dim))

) –[int](https://docs.python.org/3/builtins/functions.html#int)The dimension index corresponding to hidden_size. Must be non-negative.

-

(`shard_dim`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts._narrow_expert_data_for_padding(shard_dim))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –The dimension index corresponding to the shard (intermediate) dimension. Defaults to

`None`

.

## Source code in `vllm/model_executor/layers/fused_moe/routed_experts.py`


###

`_orient_fused_weight(fused_weight, is_fused_checkpoint_transposed)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts._orient_fused_weight)

Normalise a fused expert tensor to the vLLM weight layout.

## Source code in `vllm/model_executor/layers/fused_moe/routed_experts.py`


###

`build_expert_params_mapping(ckpt_gate_proj_name, ckpt_down_proj_name, ckpt_up_proj_name, num_experts, num_redundant_experts=0, routed_experts_prefix='routed_experts', lora_base_layer_prefix='', lora_base_layer_prefix_on_param_name='', include_fused=False)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts.build_expert_params_mapping)

Create expert parameter mapping for weight loading with redundant experts.

This mapping handles the physical-to-logical expert ID conversion needed when loading weights with EPLB redundant experts.

Parameters:

-

(`ckpt_gate_proj_name`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts.build_expert_params_mapping(ckpt_gate_proj_name))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Name of gate projection in checkpoint

-

(`ckpt_down_proj_name`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts.build_expert_params_mapping(ckpt_down_proj_name))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Name of down projection in checkpoint

-

(`ckpt_up_proj_name`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts.build_expert_params_mapping(ckpt_up_proj_name))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Name of up projection in checkpoint

-

(`num_experts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts.build_expert_params_mapping(num_experts))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of logical (non-redundant) experts

-

(`num_redundant_experts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts.build_expert_params_mapping(num_redundant_experts))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –Number of redundant experts

-

(`lora_base_layer_prefix`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts.build_expert_params_mapping(lora_base_layer_prefix))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`''`

) –LoRA

`base_layer.`

prefix for the`weight_name`

(checkpoint) side -

(`lora_base_layer_prefix_on_param_name`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts.build_expert_params_mapping(lora_base_layer_prefix_on_param_name))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`''`

) –same, for the

`param_name`

side. Independent because`get_expert_mapping`

resolves`param_name`

via`getattr`

against this layer's bare`w13_weight`

/`w2_weight`

(no prefix), while`make_expert_params_mapping`

indexes the model-wide`params_dict`

(prefix included). -

(`include_fused`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts.build_expert_params_mapping(include_fused))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Prepend the fused pre-fused-checkpoint entries

-

(`routed_experts_prefix`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts.build_expert_params_mapping(routed_experts_prefix))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'routed_experts'`

) –Prefix of the routed experts submodule


Returns:

-

–[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[str](https://docs.python.org/3/builtins/stdtypes.html#str),[int](https://docs.python.org/3/builtins/functions.html#int),[str](https://docs.python.org/3/builtins/stdtypes.html#str)]]List of tuples (param_name, weight_name, expert_id, shard_id)

-
(`where`


) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[str](https://docs.python.org/3/builtins/stdtypes.html#str),[int](https://docs.python.org/3/builtins/functions.html#int),[str](https://docs.python.org/3/builtins/stdtypes.html#str)]] -

–[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[str](https://docs.python.org/3/builtins/stdtypes.html#str),[int](https://docs.python.org/3/builtins/functions.html#int),[str](https://docs.python.org/3/builtins/stdtypes.html#str)]]- param_name: Parameter name in the layer

-

–[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[str](https://docs.python.org/3/builtins/stdtypes.html#str),[int](https://docs.python.org/3/builtins/functions.html#int),[str](https://docs.python.org/3/builtins/stdtypes.html#str)]]- weight_name: Weight name in checkpoint

-

–[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[str](https://docs.python.org/3/builtins/stdtypes.html#str),[int](https://docs.python.org/3/builtins/functions.html#int),[str](https://docs.python.org/3/builtins/stdtypes.html#str)]]- expert_id: Physical expert ID

-

–[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[str](https://docs.python.org/3/builtins/stdtypes.html#str),[int](https://docs.python.org/3/builtins/functions.html#int),[str](https://docs.python.org/3/builtins/stdtypes.html#str)]]- shard_id: Shard identifier (w1, w2, w3)


## Source code in `vllm/model_executor/layers/fused_moe/routed_experts.py`


|
|

###

`forward_modular(x, topk_weights, topk_ids, shared_experts=None, shared_experts_input=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts.forward_modular)

Execute routed experts using the quantization method's apply function.

This is called by the runner after router selection (for modular kernels) quant_method.apply() which accesses the weights on this RoutedExperts instance.

Parameters:

-

(`x`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts.forward_modular(x))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input tensor after any transforms

-

(`topk_weights`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts.forward_modular(topk_weights))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Routing weights from router (for modular kernels)

-

(`topk_ids`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts.forward_modular(topk_ids))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Selected expert IDs from router (for modular kernels)

-

(`shared_experts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts.forward_modular(shared_experts))

, default:[SharedExperts](https://docs.vllm.ai/runner/shared_experts/#vllm.model_executor.layers.fused_moe.runner.shared_experts.SharedExperts)| None`None`

) –The shared experts (if any)

-

(`shared_experts_input`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts.forward_modular(shared_experts_input))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Input for shared experts (if any)


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Output tensor from routed experts.


## Source code in `vllm/model_executor/layers/fused_moe/routed_experts.py`


###

`forward_monolithic(x, router_logits=None, input_ids=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts.forward_monolithic)

Execute routed experts using the quantization method's apply function.

This is called by the runner after router selection (for modular kernels) or with router logits (for monolithic kernels). It delegates to quant_method.apply() which accesses the weights on this RoutedExperts instance.

Parameters:

-

(`x`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts.forward_monolithic(x))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input tensor after any transforms

-

(`router_logits`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts.forward_monolithic(router_logits))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Router logits (for monolithic kernels)

-

(`input_ids`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts.forward_monolithic(input_ids))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –input ids for DeepSeek V4


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)|[UnfinalizedMoEOutput](https://docs.vllm.ai/moe_output/#vllm.model_executor.layers.fused_moe.moe_output.UnfinalizedMoEOutput)Finalized routed states or a deferred-finalize output.


## Source code in `vllm/model_executor/layers/fused_moe/routed_experts.py`


###

`make_expert_params_mapping(model, ckpt_gate_proj_name, ckpt_down_proj_name, ckpt_up_proj_name, num_experts, num_redundant_experts=0, routed_experts_prefix='routed_experts')`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.RoutedExperts.make_expert_params_mapping)

Build the expert mapping, detecting the LoRA `base_layer.`

prefix by scanning `model`

's parameters.

Legacy entry point for models that still hand-roll `load_weights`

; the `RoutedExperts`

weight loader uses `get_expert_mapping`

/ `build_expert_params_mapping`

instead (which take the prefix directly). See `build_expert_params_mapping`

for the returned tuple format.

## Source code in `vllm/model_executor/layers/fused_moe/routed_experts.py`


##

`SharedExperts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.SharedExperts)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[maybe_forward_async](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.SharedExperts.maybe_forward_async)Enqueue shared experts on the aux stream without waiting for them.

-
–[wait](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.SharedExperts.wait)Block the main stream until

`maybe_forward_async`

output is ready.

## Source code in `vllm/model_executor/layers/fused_moe/runner/shared_experts.py`


|
|

###

`maybe_forward_async(shared_experts_input)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.SharedExperts.maybe_forward_async)

Enqueue shared experts on the aux stream without waiting for them.

Returns true if the shared experts were enqueued, false otherwise. Call `wait`

to wait for the shared experts to finish if this returns true.

## Source code in `vllm/model_executor/layers/fused_moe/runner/shared_experts.py`


###

`wait()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.SharedExperts.wait)

Block the main stream until `maybe_forward_async`

output is ready.

##

`TritonExperts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.TritonExperts)

Bases:

, [LoRAExpertsMixin](https://docs.vllm.ai/experts/lora_experts_mixin/#vllm.model_executor.layers.fused_moe.experts.lora_experts_mixin.LoRAExpertsMixin)[FusedMoEExpertsModular](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular)

Triton-based fused MoE expert implementation.

## Source code in `vllm/model_executor/layers/fused_moe/experts/triton_moe.py`


|
|

##

`TritonOrDeepGemmExperts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.TritonOrDeepGemmExperts)

Bases: [FallbackExperts](https://docs.vllm.ai/experts/fallback/#vllm.model_executor.layers.fused_moe.experts.fallback.FallbackExperts)

DeepGemm with fallback to Triton for low latency shapes.

## Source code in `vllm/model_executor/layers/fused_moe/experts/triton_deep_gemm_moe.py`


##

`UnquantizedFusedMoEMethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.UnquantizedFusedMoEMethod)

Bases:

, [FusedMoEMethodBase](https://docs.vllm.ai/fused_moe_method_base/#vllm.model_executor.layers.fused_moe.fused_moe_method_base.FusedMoEMethodBase)[CustomOp](https://docs.vllm.ai/custom_op/#vllm.model_executor.custom_op.CustomOp)

MoE method without quantization.

## Source code in `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`


|
|

###

`_init_moe_kernel(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.UnquantizedFusedMoEMethod._init_moe_kernel)

Build the MoE kernel from the layer's current (shuffled) weights.

## Source code in `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`


##

`FusedMoEFactory(num_experts, top_k, hidden_size, intermediate_size, intermediate_pad=None, params_dtype=None, renormalize=True, use_grouped_topk=False, num_expert_group=None, topk_group=None, quant_config=None, tp_size=None, dp_size=None, pcp_size=None, prefix='', custom_routing_function=None, router=None, scoring_func='softmax', routed_scaling_factor=1.0, swiglu_limit=None, swiglu_alpha=None, swiglu_beta=None, activation_situ_beta=None, activation_situ_linear_beta=None, e_score_correction_bias=None, apply_router_weight_on_input=False, activation='silu', enable_eplb=False, num_redundant_experts=0, has_bias=False, is_sequence_parallel=False, reduce_results=True, ckpt_names=('gate_proj', 'down_proj', 'up_proj'), is_fused_checkpoint_transposed=False, n_shared_experts=None, fuse_shared_experts=False, router_logits_dtype=None, gate=None, shared_experts=None, shared_expert_gate=None, routed_input_transform=None, routed_output_transform=None, apply_routed_scale_to_output=False, zero_expert_type=None, hash_indices_table=None, bias_vl=None, image_sentinel_lo=0, runner_cls=None, runner_args=None, routed_experts_cls=None, routed_experts_args=None, skip_padding=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory)

Factory function for creating MoE execution pipeline.

Creates and configures a complete MoE execution pipeline including: - Router (for token-to-expert assignment) - RoutedExperts (containing expert weight parameters) - MoERunner (orchestrates the complete forward pass)

The experts contain both MergedColumnParallel weights (gate_up_proj/w13) and RowParallelLinear weights (down_proj/w2).

Note: Mixtral uses w1, w2, and w3 for gate, up, and down_proj. We copy that naming convention here and handle any remapping in the load_weights function in each model implementation.

Parameters:

-

(`intermediate_pad`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(intermediate_pad))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –Padding added to the intermediate size, if any.

-

(`swiglu_alpha`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(swiglu_alpha))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)| None`None`

) –Optional alpha parameter for the SwiGLU activation.

-

(`swiglu_beta`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(swiglu_beta))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)| None`None`

) –Optional beta parameter for the SwiGLU activation.


Parameters:

-

(`num_experts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(num_experts))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of experts in the model (global count)

-

(`top_k`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(top_k))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of experts selected for each token

-

(`hidden_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(hidden_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Input hidden state size of the transformer

-

(`intermediate_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(intermediate_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Intermediate size of the experts

-

(`params_dtype`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(params_dtype))

, default:[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)| None`None`

) –Data type for the parameters

-

(`renormalize`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(renormalize))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –Whether to renormalize the logits in the router

-

(`use_grouped_topk`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(use_grouped_topk))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether to use grouped top-k routing

-

(`num_expert_group`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(num_expert_group))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –Number of expert groups for grouped top-k

-

(`topk_group`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(topk_group))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –Top-k value per group for grouped top-k

-

(`quant_config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(quant_config))

, default:[QuantizationConfig](https://docs.vllm.ai/quantization/base_config/#vllm.model_executor.layers.quantization.base_config.QuantizationConfig)| None`None`

) –Quantization configuration

-

(`tp_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(tp_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –Tensor parallelism size (None = use global default)

-

(`dp_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(dp_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –Data parallelism size (None = use global default)

-

(`pcp_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(pcp_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –Pipeline context parallelism size (None = use global default)

-

(`prefix`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(prefix))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`''`

) –Layer name prefix for weight loading

-

(`custom_routing_function`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(custom_routing_function))

, default:[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)| None`None`

) –Custom routing function override

-

(`router`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(router))

, default:[FusedMoERouter](https://docs.vllm.ai/router/fused_moe_router/#vllm.model_executor.layers.fused_moe.router.fused_moe_router.FusedMoERouter)| None`None`

) –Pre-configured router instance (None = create default)

-

(`scoring_func`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(scoring_func))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'softmax'`

) –Scoring function for routing ("softmax" or others)

-

(`routed_scaling_factor`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(routed_scaling_factor))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)`1.0`

) –Scaling factor applied to topk_weights or output

-

(`swiglu_limit`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(swiglu_limit))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)| None`None`

) –SwiGLU activation limit

-

(`activation_situ_beta`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(activation_situ_beta))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)| None`None`

) –SituGLU activation beta

-

(`activation_situ_linear_beta`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(activation_situ_linear_beta))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)| None`None`

) –SituGLU linear beta

-

(`e_score_correction_bias`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(e_score_correction_bias))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Expert score correction bias tensor

-

(`apply_router_weight_on_input`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(apply_router_weight_on_input))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether to apply router weights on input

-

(`activation`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(activation))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'silu'`

) –Activation function name ("silu", "gelu", etc.)

-

(`enable_eplb`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(enable_eplb))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether to enable expert parallelism load balancer

-

(`num_redundant_experts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(num_redundant_experts))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –Number of redundant experts for EPLB

-

(`has_bias`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(has_bias))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether expert layers have bias terms

-

(`is_sequence_parallel`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(is_sequence_parallel))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether sequence parallelism is enabled

-

(`reduce_results`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(reduce_results))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –Whether to all-reduce the final output. Setting this to False (to fuse the all-reduce downstream) is only honored on the late-AR path.

-

(`ckpt_names`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(ckpt_names))

, default:[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[str](https://docs.python.org/3/builtins/stdtypes.html#str),[str](https://docs.python.org/3/builtins/stdtypes.html#str)]`('gate_proj', 'down_proj', 'up_proj')`

) –Checkpoint parameter name tuple (gate_proj, down_proj, up_proj) used for weight loading

-

(`is_fused_checkpoint_transposed`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(is_fused_checkpoint_transposed))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether fused checkpoint weights and block scales use transposed storage.

-

(`n_shared_experts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(n_shared_experts))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –Number of shared experts to fuse into the routed grouped GEMM (ROCm; requires aiter FSE or the router-append path)

-

(`fuse_shared_experts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(fuse_shared_experts))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether to enable shared-expert fusion.

-

(`router_logits_dtype`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(router_logits_dtype))

, default:[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)| None`None`

) –Data type for router logits buffers

-

(`gate`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(gate))

, default:[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)| None`None`

) –Pre-configured gate module

-

(`shared_experts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(shared_experts))

, default:[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)| None`None`

) –Pre-configured shared experts module

-

(`shared_expert_gate`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(shared_expert_gate))

, default:[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)| None`None`

) –Pre-configured shared expert gate module

-

(`routed_input_transform`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(routed_input_transform))

, default:[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)| None`None`

) –Input transformation module

-

(`routed_output_transform`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(routed_output_transform))

, default:[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)| None`None`

) –Output transformation module

-

(`apply_routed_scale_to_output`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(apply_routed_scale_to_output))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether to apply routed_scaling_factor to output instead of topk_weights

-

(`zero_expert_type`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(zero_expert_type))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –Type of zero expert handling

-

(`hash_indices_table`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(hash_indices_table))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Hash table for expert indices

-

(`bias_vl`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(bias_vl))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Vision routing bias for image tokens (Deepseek V4)

-

(`image_sentinel_lo`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(image_sentinel_lo))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –First of five consecutive in-vocab image sentinel ids (0 = vision routing disabled)

-

(`runner_cls`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(runner_cls))

, default:[type](https://docs.python.org/3/builtins/functions.html#type)[[MoERunner](https://docs.vllm.ai/runner/moe_runner/#vllm.model_executor.layers.fused_moe.runner.moe_runner.MoERunner)] | None`None`

) –Custom MoERunner class (None = use default MoERunner)

-

(`runner_args`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(runner_args))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None`None`

) –Additional arguments for runner constructor

-

(`routed_experts_cls`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(routed_experts_cls))

, default:[type](https://docs.python.org/3/builtins/functions.html#type)[[RoutedExperts](https://docs.vllm.ai/routed_experts/#vllm.model_executor.layers.fused_moe.routed_experts.RoutedExperts)] | None`None`

) –Custom RoutedExperts class (None = use default)

-

(`routed_experts_args`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(routed_experts_args))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None`None`

) –Additional arguments for routed_experts constructor

-

(`skip_padding`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.FusedMoEFactory(skip_padding))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether grouped routing should invalidate padding rows.


Returns:

-
(`MoERunner`


) –[MoERunner](https://docs.vllm.ai/runner/moe_runner/#vllm.model_executor.layers.fused_moe.runner.moe_runner.MoERunner)Configured MoE execution pipeline ready for forward passes


## Source code in `vllm/model_executor/layers/fused_moe/layer.py`


|
|

##

`activation_without_mul(activation)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.activation_without_mul)

Get the non-gated variant of an activation function.

Parameters:

Returns:

-

–[str](https://docs.python.org/3/builtins/stdtypes.html#str)The non-gated activation name (e.g., "silu_no_mul", "gelu_no_mul")


## Source code in `vllm/model_executor/layers/fused_moe/activation.py`


##

`apply_moe_activation(activation, output, input, *, activation_config=None, topk_ids=None, expert_map=None, valid_token_counts=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.apply_moe_activation)

Apply MoE activation function.

The configuration drives specialized activation behavior. Routing tensors and valid token counts remain per-call inputs because they depend on the current token assignment. A single token count masks a flat `[T, D]`

buffer; one count per expert masks each prefix in a padded `[E, T, D]`

buffer.

## Source code in `vllm/model_executor/layers/fused_moe/activation.py`


|
|

##

`fused_experts(hidden_states, w1, w2, topk_weights, topk_ids, activation=MoEActivation.SILU, apply_router_weight_on_input=False, global_num_experts=-1, expert_map=None, quant_config=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_experts)

Run fused MoE expert computation using Triton kernels.

## Source code in `vllm/model_executor/layers/fused_moe/fused_moe.py`


##

`fused_moe_make_expert_params_mapping(model, ckpt_gate_proj_name, ckpt_down_proj_name, ckpt_up_proj_name, num_experts, num_redundant_experts=0, routed_experts_prefix='routed_experts')`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.fused_moe_make_expert_params_mapping)

Delegate to EPLB manager.