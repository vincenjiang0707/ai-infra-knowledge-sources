source: https://docs.vllm.ai/en/latest/api/vllm/models/minimax_m3/amd/ops/
lastmod: 2026-09-23

#

`vllm.models.minimax_m3.amd.ops`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.amd.ops)

AMD/ROCm fused Triton ops for MiniMax-M3.

These replace per-element PyTorch fallbacks (FlashInfer / fused HIP kernels are unavailable on ROCm) with single-pass Triton kernels to cut launch overhead and intermediate-tensor traffic during decode.

Modules:

-
–[gemma_rmsnorm](https://docs.vllm.ai/gemma_rmsnorm/#vllm.models.minimax_m3.amd.ops.gemma_rmsnorm)Fused Gemma-style RMSNorm for AMD ROCm via Triton.

-
–[index_topk](https://docs.vllm.ai/index_topk/#vllm.models.minimax_m3.amd.ops.index_topk)Triton kernels for MiniMax M3 lightning-indexer block scoring + top-k.

-
–[sparse_attn](https://docs.vllm.ai/sparse_attn/#vllm.models.minimax_m3.amd.ops.sparse_attn)ROCm gfx942/gfx950 block-sparse GQA prefill kernel for MiniMax-M3.

-
–[sparse_pa](https://docs.vllm.ai/sparse_pa/#vllm.models.minimax_m3.amd.ops.sparse_pa)AITER page-16 sparse paged-attention helpers for MiniMax-M3 on ROCm.

-
–[swiglu_oai](https://docs.vllm.ai/swiglu_oai/#vllm.models.minimax_m3.amd.ops.swiglu_oai)Fused SwiGLU-OAI activation (split layout) for AMD ROCm via Triton.


Functions:

-
–[swiglu_oai_quantize_mxfp8](https://docs.vllm.ai#vllm.models.minimax_m3.amd.ops.swiglu_oai_quantize_mxfp8)SwiGLU-OAI on split-layout

`[M, 2I]`

fused with MXFP8 activation-quant. -
–[swiglu_oai_split](https://docs.vllm.ai#vllm.models.minimax_m3.amd.ops.swiglu_oai_split)SwiGLU-OAI on a split-layout

`[*, 2I]`

tensor ->`[*, I]`

.

##

`swiglu_oai_quantize_mxfp8(gate_up, alpha, beta, limit, block_m=64)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.amd.ops.swiglu_oai_quantize_mxfp8)

SwiGLU-OAI on split-layout `[M, 2I]`

fused with MXFP8 activation-quant.

Returns `(act_q [M, I] float8_e4m3fn, act_scale [M, I//32] uint8 E8M0)`

, identical to `mxfp8_e4m3_quantize(swiglu_oai_split(gate_up))`

but in a single Triton pass (no bf16 intermediate). Used between the two GEMMs of the native MXFP8 MoE. Numerically equivalent to the unfused chain (bit-exact on measured MoE shapes); marginally more accurate (fp32 act, no bf16 round-trip).

## Source code in `vllm/models/minimax_m3/amd/ops/swiglu_oai.py`


##

`swiglu_oai_split(gate_up, alpha, beta, limit, out_dtype=None)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.amd.ops.swiglu_oai_split)

SwiGLU-OAI on a split-layout `[*, 2I]`

tensor -> `[*, I]`

.