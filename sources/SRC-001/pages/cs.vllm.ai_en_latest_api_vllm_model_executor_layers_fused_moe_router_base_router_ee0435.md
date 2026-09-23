source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/router/base_router/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.fused_moe.router.base_router`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.base_router)

Classes:

-
–[BaseRouter](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.base_router.BaseRouter)Base class providing common functionality for all router implementations.


##

`BaseRouter`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.base_router.BaseRouter)

Bases: [FusedMoERouter](https://docs.vllm.ai/fused_moe_router/#vllm.model_executor.layers.fused_moe.router.fused_moe_router.FusedMoERouter)

Base class providing common functionality for all router implementations.

This class implements the template method pattern where select_experts() handles common pre-processing and post-processing, delegating the actual routing logic to the abstract _compute_routing() method.

Methods:

-
–[__init__](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.base_router.BaseRouter.__init__)Args:

-
–[set_capture_fn](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.base_router.BaseRouter.set_capture_fn)Set a capture callback for logical routed expert IDs.


## Source code in `vllm/model_executor/layers/fused_moe/router/base_router.py`


|
|

###

`__init__(top_k, global_num_experts, eplb_state=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.base_router.BaseRouter.__init__)

Args: top_k: Number of experts to select per token global_num_experts: Total number of experts eplb_state: Optional EPLBLayerState for load balancing

## Source code in `vllm/model_executor/layers/fused_moe/router/base_router.py`


###

`_apply_eplb_mapping(topk_ids)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.base_router.BaseRouter._apply_eplb_mapping)

Apply EPLB mapping to convert logical expert IDs to physical expert IDs.

## Source code in `vllm/model_executor/layers/fused_moe/router/base_router.py`


###

`_compute_routing(hidden_states, router_logits, indices_type, *, input_ids=None)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.base_router.BaseRouter._compute_routing)

Compute the actual routing logic.

This method must be implemented by subclasses to provide the specific routing algorithm (e.g., grouped_topk, fused_topk, custom routing, etc.).

Parameters:

-

(`hidden_states`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.base_router.BaseRouter._compute_routing(hidden_states))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input hidden states

-

(`router_logits`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.base_router.BaseRouter._compute_routing(router_logits))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Router logits for expert selection

-

(`indices_type`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.base_router.BaseRouter._compute_routing(indices_type))

) –[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)| NoneDesired dtype for expert indices (may be None)

-

(`input_ids`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.base_router.BaseRouter._compute_routing(input_ids))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Token ids, for routers that condition on them


Returns:

## Source code in `vllm/model_executor/layers/fused_moe/router/base_router.py`


###

`_convert_indices_dtype(topk_ids, indices_type)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.base_router.BaseRouter._convert_indices_dtype)

Convert topk_ids to the desired dtype if needed.

## Source code in `vllm/model_executor/layers/fused_moe/router/base_router.py`


###

`_select_experts(hidden_states, router_logits, topk_indices_dtype=None, *, input_ids=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.base_router.BaseRouter._select_experts)

Route the input hidden states to the top-k experts based on the router logits.

This method implements the template method pattern: 1. Validates EPLB state 2. Calls _compute_routing() to get topk_weights and topk_ids 3. Applies EPLB mapping if enabled 4. Converts indices dtype if needed

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


## Source code in `vllm/model_executor/layers/fused_moe/router/base_router.py`


###

`_validate_eplb_state()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.base_router.BaseRouter._validate_eplb_state)

Validate that EPLB state is properly initialized if EPLB is enabled.

## Source code in `vllm/model_executor/layers/fused_moe/router/base_router.py`


###

`set_capture_fn(capture_fn)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.base_router.BaseRouter.set_capture_fn)

Set a capture callback for logical routed expert IDs.