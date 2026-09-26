source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/router/fused_topk_router/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.fused_moe.router.fused_topk_router`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.fused_topk_router)

Classes:

-
–[FusedTopKRouter](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.fused_topk_router.FusedTopKRouter)Default router using standard fused top-k routing.


##

`FusedTopKRouter`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.fused_topk_router.FusedTopKRouter)

Bases: [BaseRouter](https://docs.vllm.ai/base_router/#vllm.model_executor.layers.fused_moe.router.base_router.BaseRouter)

Default router using standard fused top-k routing.

## Source code in `vllm/model_executor/layers/fused_moe/router/fused_topk_router.py`


###

`_compute_routing(hidden_states, router_logits, indices_type, *, input_ids=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.fused_topk_router.FusedTopKRouter._compute_routing)

Compute routing using standard fused top-k.