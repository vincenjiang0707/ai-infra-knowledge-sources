source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/router/rocm_fp32_router_gemm/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.fused_moe.router.rocm_fp32_router_gemm`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.rocm_fp32_router_gemm)

Low-token FP32 router GEMM for gfx950.

Functions:

-
–[can_use_rocm_fp32_router_gemm](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.rocm_fp32_router_gemm.can_use_rocm_fp32_router_gemm)Return whether the tensors match the tuned gfx950 fast path.

-
–[rocm_fp32_router_gemm](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.rocm_fp32_router_gemm.rocm_fp32_router_gemm)Compute

`hidden_states @ router_weight.T`

with FP32 accumulation.

##

`can_use_rocm_fp32_router_gemm(hidden_states, router_weight)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.rocm_fp32_router_gemm.can_use_rocm_fp32_router_gemm)

Return whether the tensors match the tuned gfx950 fast path.

## Source code in `vllm/model_executor/layers/fused_moe/router/rocm_fp32_router_gemm.py`


##

`rocm_fp32_router_gemm(hidden_states, router_weight)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.rocm_fp32_router_gemm.rocm_fp32_router_gemm)

Compute `hidden_states @ router_weight.T`

with FP32 accumulation.