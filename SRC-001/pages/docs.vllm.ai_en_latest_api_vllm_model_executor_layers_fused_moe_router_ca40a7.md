source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/router/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.fused_moe.router`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router)

Modules:

-
–[aiter_shared_routed_fused_moe_router](https://docs.vllm.ai/aiter_shared_routed_fused_moe_router/#vllm.model_executor.layers.fused_moe.router.aiter_shared_routed_fused_moe_router) -
–[base_router](https://docs.vllm.ai/base_router/#vllm.model_executor.layers.fused_moe.router.base_router) -
–[bf16x3_router_gemm_cutedsl](https://docs.vllm.ai/bf16x3_router_gemm_cutedsl/#vllm.model_executor.layers.fused_moe.router.bf16x3_router_gemm_cutedsl)CuteDSL BF16x3 router GEMM.

-
–[cpu_router](https://docs.vllm.ai/cpu_router/#vllm.model_executor.layers.fused_moe.router.cpu_router)Router for CPU MoE experts.

-
–[custom_routing_router](https://docs.vllm.ai/custom_routing_router/#vllm.model_executor.layers.fused_moe.router.custom_routing_router) -
–[fused_moe_router](https://docs.vllm.ai/fused_moe_router/#vllm.model_executor.layers.fused_moe.router.fused_moe_router) -
–[fused_topk_bias_router](https://docs.vllm.ai/fused_topk_bias_router/#vllm.model_executor.layers.fused_moe.router.fused_topk_bias_router) -
–[fused_topk_router](https://docs.vllm.ai/fused_topk_router/#vllm.model_executor.layers.fused_moe.router.fused_topk_router) -
–[gate_linear](https://docs.vllm.ai/gate_linear/#vllm.model_executor.layers.fused_moe.router.gate_linear) -
–[grouped_topk_router](https://docs.vllm.ai/grouped_topk_router/#vllm.model_executor.layers.fused_moe.router.grouped_topk_router) -
–[rocm_fp32_router_gemm](https://docs.vllm.ai/rocm_fp32_router_gemm/#vllm.model_executor.layers.fused_moe.router.rocm_fp32_router_gemm)Low-token FP32 router GEMM for gfx950.

-
–[router_factory](https://docs.vllm.ai/router_factory/#vllm.model_executor.layers.fused_moe.router.router_factory) -
–[routing_simulator_router](https://docs.vllm.ai/routing_simulator_router/#vllm.model_executor.layers.fused_moe.router.routing_simulator_router) -
–[zero_expert_router](https://docs.vllm.ai/zero_expert_router/#vllm.model_executor.layers.fused_moe.router.zero_expert_router)