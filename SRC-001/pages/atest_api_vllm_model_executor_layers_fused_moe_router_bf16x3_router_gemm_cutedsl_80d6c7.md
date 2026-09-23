source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/router/bf16x3_router_gemm_cutedsl/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.fused_moe.router.bf16x3_router_gemm_cutedsl`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.bf16x3_router_gemm_cutedsl)

CuteDSL BF16x3 router GEMM.

Computes `X @ W.T`

for BF16 `X`

with shape `[N, K]`

and FP32 router weights `W`

with shape `[M, K]`

by decomposing each FP32 weight value into three BF16 residual terms inside the kernel, then accumulating the three BF16 MMA results into FP32 TMEM output.

The TMEM accumulation chain is bounded to `num_tmem_acc`

K-tiles: at chunk boundaries the epilogue warps drain the main-term accumulator into a register master accumulator and the MMA warp resets it.

##

`_bf16x3_router_gemm(X, W)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.bf16x3_router_gemm_cutedsl._bf16x3_router_gemm)

Return `X @ W.T`

using the SM100 BF16x3 router GEMM kernel.

## Source code in `vllm/model_executor/layers/fused_moe/router/bf16x3_router_gemm_cutedsl.py`


##

`_pick_tile_config(N, K, M, num_sms)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.bf16x3_router_gemm_cutedsl._pick_tile_config)

Return (BN, split_k): tuned table mid-range, generic rule otherwise.

## Source code in `vllm/model_executor/layers/fused_moe/router/bf16x3_router_gemm_cutedsl.py`


##

`warmup_bf16x3_router_gemm(K, M, min_num_tokens, max_num_tokens)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.bf16x3_router_gemm_cutedsl.warmup_bf16x3_router_gemm)

Compile every BF16x3 router GEMM configuration reachable at runtime.