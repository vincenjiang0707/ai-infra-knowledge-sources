source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/router/fused_moe_router/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.fused_moe.router.fused_moe_router`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.fused_moe_router)

Classes:

-
–[FusedMoERouter](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.fused_moe_router.FusedMoERouter)FusedMoERouter is an abstract class that provides a 'select_experts'


##

`FusedMoERouter`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.fused_moe_router.FusedMoERouter)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

FusedMoERouter is an abstract class that provides a 'select_experts' method that is used for routing hidden states based on router logits.

Methods:

-
–[select_experts](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.fused_moe_router.FusedMoERouter.select_experts)Route the input hidden states to the top-k experts based on the


## Source code in `vllm/model_executor/layers/fused_moe/router/fused_moe_router.py`


###

`select_experts(hidden_states, router_logits, topk_indices_dtype=None, *, input_ids=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.fused_moe_router.FusedMoERouter.select_experts)

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