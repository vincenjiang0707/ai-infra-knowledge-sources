source: https://docs.vllm.ai/en/latest/api/vllm/models/minimax_m3/amd/ops/gemma_rmsnorm/
lastmod: 2026-09-24

#

`vllm.models.minimax_m3.amd.ops.gemma_rmsnorm`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.amd.ops.gemma_rmsnorm)

Fused Gemma-style RMSNorm for AMD ROCm via Triton.

Gemma RMSNorm = normalize(x) * (1 + weight), computed in fp32. FlashInfer's `gemma_rmsnorm`

/ `gemma_fused_add_rmsnorm`

CUDA kernels are unavailable on ROCm, so the AMD path previously used a ~8-op PyTorch sequence (float cast, add, pow, mean, rsqrt, two muls, cast) — each a separate kernel launch materializing fp32 intermediates. These kernels collapse that into a single pass per row.

## Two entry points

`gemma_rmsnorm(x, w, eps)`

-> normalized tensor`gemma_fused_add_rmsnorm(x, res, w, eps)`

-> (normalized, x + res)

Both normalize over the last dim and broadcast `weight`

(shape [N]) over it, so they serve both the full-hidden norms (input/post-attn/final) and the per-head q_norm/k_norm (N == head_dim). Inputs may be non-contiguous views (e.g. `qkv.split`

slices); strides are passed through and outputs are written contiguous.