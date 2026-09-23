source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/layer/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.fused_moe.layer`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer)

Functions:

-
–[FusedMoEFactory](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory)Factory function for creating MoE execution pipeline.

-
–[fused_moe_make_expert_params_mapping](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.fused_moe_make_expert_params_mapping)Delegate to EPLB manager.


##

`FusedMoEFactory(num_experts, top_k, hidden_size, intermediate_size, intermediate_pad=None, params_dtype=None, renormalize=True, use_grouped_topk=False, num_expert_group=None, topk_group=None, quant_config=None, tp_size=None, dp_size=None, pcp_size=None, prefix='', custom_routing_function=None, router=None, scoring_func='softmax', routed_scaling_factor=1.0, swiglu_limit=None, swiglu_alpha=None, swiglu_beta=None, activation_situ_beta=None, activation_situ_linear_beta=None, e_score_correction_bias=None, apply_router_weight_on_input=False, activation='silu', enable_eplb=False, num_redundant_experts=0, has_bias=False, is_sequence_parallel=False, reduce_results=True, ckpt_names=('gate_proj', 'down_proj', 'up_proj'), is_fused_checkpoint_transposed=False, n_shared_experts=None, fuse_shared_experts=False, router_logits_dtype=None, gate=None, shared_experts=None, shared_expert_gate=None, routed_input_transform=None, routed_output_transform=None, apply_routed_scale_to_output=False, zero_expert_type=None, hash_indices_table=None, bias_vl=None, image_sentinel_lo=0, runner_cls=None, runner_args=None, routed_experts_cls=None, routed_experts_args=None, skip_padding=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory)

Factory function for creating MoE execution pipeline.

Creates and configures a complete MoE execution pipeline including: - Router (for token-to-expert assignment) - RoutedExperts (containing expert weight parameters) - MoERunner (orchestrates the complete forward pass)

The experts contain both MergedColumnParallel weights (gate_up_proj/w13) and RowParallelLinear weights (down_proj/w2).

Note: Mixtral uses w1, w2, and w3 for gate, up, and down_proj. We copy that naming convention here and handle any remapping in the load_weights function in each model implementation.

Parameters:

-

(`intermediate_pad`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(intermediate_pad))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –Padding added to the intermediate size, if any.

-

(`swiglu_alpha`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(swiglu_alpha))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)| None`None`

) –Optional alpha parameter for the SwiGLU activation.

-

(`swiglu_beta`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(swiglu_beta))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)| None`None`

) –Optional beta parameter for the SwiGLU activation.


Parameters:

-

(`num_experts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(num_experts))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of experts in the model (global count)

-

(`top_k`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(top_k))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of experts selected for each token

-

(`hidden_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(hidden_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Input hidden state size of the transformer

-

(`intermediate_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(intermediate_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Intermediate size of the experts

-

(`params_dtype`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(params_dtype))

, default:[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)| None`None`

) –Data type for the parameters

-

(`renormalize`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(renormalize))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –Whether to renormalize the logits in the router

-

(`use_grouped_topk`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(use_grouped_topk))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether to use grouped top-k routing

-

(`num_expert_group`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(num_expert_group))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –Number of expert groups for grouped top-k

-

(`topk_group`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(topk_group))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –Top-k value per group for grouped top-k

-

(`quant_config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(quant_config))

, default:[QuantizationConfig](https://docs.vllm.ai/quantization/base_config/#vllm.model_executor.layers.quantization.base_config.QuantizationConfig)| None`None`

) –Quantization configuration

-

(`tp_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(tp_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –Tensor parallelism size (None = use global default)

-

(`dp_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(dp_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –Data parallelism size (None = use global default)

-

(`pcp_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(pcp_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –Pipeline context parallelism size (None = use global default)

-

(`prefix`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(prefix))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`''`

) –Layer name prefix for weight loading

-

(`custom_routing_function`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(custom_routing_function))

, default:[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)| None`None`

) –Custom routing function override

-

(`router`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(router))

, default:[FusedMoERouter](https://docs.vllm.ai/router/fused_moe_router/#vllm.model_executor.layers.fused_moe.router.fused_moe_router.FusedMoERouter)| None`None`

) –Pre-configured router instance (None = create default)

-

(`scoring_func`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(scoring_func))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'softmax'`

) –Scoring function for routing ("softmax" or others)

-

(`routed_scaling_factor`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(routed_scaling_factor))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)`1.0`

) –Scaling factor applied to topk_weights or output

-

(`swiglu_limit`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(swiglu_limit))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)| None`None`

) –SwiGLU activation limit

-

(`activation_situ_beta`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(activation_situ_beta))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)| None`None`

) –SituGLU activation beta

-

(`activation_situ_linear_beta`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(activation_situ_linear_beta))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)| None`None`

) –SituGLU linear beta

-

(`e_score_correction_bias`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(e_score_correction_bias))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Expert score correction bias tensor

-

(`apply_router_weight_on_input`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(apply_router_weight_on_input))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether to apply router weights on input

-

(`activation`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(activation))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'silu'`

) –Activation function name ("silu", "gelu", etc.)

-

(`enable_eplb`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(enable_eplb))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether to enable expert parallelism load balancer

-

(`num_redundant_experts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(num_redundant_experts))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –Number of redundant experts for EPLB

-

(`has_bias`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(has_bias))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether expert layers have bias terms

-

(`is_sequence_parallel`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(is_sequence_parallel))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether sequence parallelism is enabled

-

(`reduce_results`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(reduce_results))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –Whether to all-reduce the final output. Setting this to False (to fuse the all-reduce downstream) is only honored on the late-AR path.

-

(`ckpt_names`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(ckpt_names))

, default:[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[str](https://docs.python.org/3/builtins/stdtypes.html#str),[str](https://docs.python.org/3/builtins/stdtypes.html#str)]`('gate_proj', 'down_proj', 'up_proj')`

) –Checkpoint parameter name tuple (gate_proj, down_proj, up_proj) used for weight loading

-

(`is_fused_checkpoint_transposed`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(is_fused_checkpoint_transposed))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether fused checkpoint weights and block scales use transposed storage.

-

(`n_shared_experts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(n_shared_experts))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –Number of shared experts to fuse into the routed grouped GEMM (ROCm; requires aiter FSE or the router-append path)

-

(`fuse_shared_experts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(fuse_shared_experts))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether to enable shared-expert fusion.

-

(`router_logits_dtype`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(router_logits_dtype))

, default:[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)| None`None`

) –Data type for router logits buffers

-

(`gate`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(gate))

, default:[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)| None`None`

) –Pre-configured gate module

-

(`shared_experts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(shared_experts))

, default:[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)| None`None`

) –Pre-configured shared experts module

-

(`shared_expert_gate`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(shared_expert_gate))

, default:[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)| None`None`

) –Pre-configured shared expert gate module

-

(`routed_input_transform`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(routed_input_transform))

, default:[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)| None`None`

) –Input transformation module

-

(`routed_output_transform`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(routed_output_transform))

, default:[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)| None`None`

) –Output transformation module

-

(`apply_routed_scale_to_output`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(apply_routed_scale_to_output))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether to apply routed_scaling_factor to output instead of topk_weights

-

(`zero_expert_type`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(zero_expert_type))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –Type of zero expert handling

-

(`hash_indices_table`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(hash_indices_table))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Hash table for expert indices

-

(`bias_vl`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(bias_vl))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Vision routing bias for image tokens (Deepseek V4)

-

(`image_sentinel_lo`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(image_sentinel_lo))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –First of five consecutive in-vocab image sentinel ids (0 = vision routing disabled)

-

(`runner_cls`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(runner_cls))

, default:[type](https://docs.python.org/3/builtins/functions.html#type)[[MoERunner](https://docs.vllm.ai/runner/moe_runner/#vllm.model_executor.layers.fused_moe.runner.moe_runner.MoERunner)] | None`None`

) –Custom MoERunner class (None = use default MoERunner)

-

(`runner_args`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(runner_args))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None`None`

) –Additional arguments for runner constructor

-

(`routed_experts_cls`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(routed_experts_cls))

, default:[type](https://docs.python.org/3/builtins/functions.html#type)[[RoutedExperts](https://docs.vllm.ai/routed_experts/#vllm.model_executor.layers.fused_moe.routed_experts.RoutedExperts)] | None`None`

) –Custom RoutedExperts class (None = use default)

-

(`routed_experts_args`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(routed_experts_args))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None`None`

) –Additional arguments for routed_experts constructor

-

(`skip_padding`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.FusedMoEFactory(skip_padding))

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

`fused_moe_make_expert_params_mapping(model, ckpt_gate_proj_name, ckpt_down_proj_name, ckpt_up_proj_name, num_experts, num_redundant_experts=0, routed_experts_prefix='routed_experts')`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.layer.fused_moe_make_expert_params_mapping)

Delegate to EPLB manager.