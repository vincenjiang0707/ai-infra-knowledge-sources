source: https://docs.vllm.ai/en/latest/api/vllm/models/minimax_m3/amd/ops/swiglu_oai/
lastmod: 2026-09-24

#

`vllm.models.minimax_m3.amd.ops.swiglu_oai`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.amd.ops.swiglu_oai)

Fused SwiGLU-OAI activation (split layout) for AMD ROCm via Triton.

SwiGLU-OAI on a `[*, 2I]`

split-layout input (gate = first half, up = second half):

```
gate = clamp(gate, max=limit)
up = clamp(up, -limit, +limit)
out = gate * sigmoid(alpha * gate) * (up + beta)
```


On ROCm the dense MLP and the native MXFP8 MoE (between its two GEMMs) fell back to a chain of elementwise PyTorch ops with fp32 intermediates: vLLM's shared `SiluAndMulWithClamp`

blanket-routes ROCm to `forward_native`

, and the MoE applies the activation inline in PyTorch. This Triton kernel collapses that into a single pass producing the `[*, I]`

output directly, and computes in fp32 (rel ~1e-6 vs reference).

Note: the vectorized `torch.ops._C.silu_and_mul_with_clamp`

op IS built on ROCm and is ~1.2-2.2x faster in isolation, but the win is launch overhead that HIP graphs already eliminate — measured end-to-end throughput is identical (within noise), so we keep the fp32-accurate Triton kernel.

Functions:

-
–[swiglu_oai_quantize_mxfp8](https://docs.vllm.ai#vllm.models.minimax_m3.amd.ops.swiglu_oai.swiglu_oai_quantize_mxfp8)SwiGLU-OAI on split-layout

`[M, 2I]`

fused with MXFP8 activation-quant. -
–[swiglu_oai_split](https://docs.vllm.ai#vllm.models.minimax_m3.amd.ops.swiglu_oai.swiglu_oai_split)SwiGLU-OAI on a split-layout

`[*, 2I]`

tensor ->`[*, I]`

.

##

`_swiglu_oai_quant_kernel(g_ptr, aq_ptr, as_ptr, M, n_inter, stride_gm, stride_gn, stride_qm, stride_qn, stride_sm, stride_sk, alpha, beta, limit, HAS_LIMIT, BLOCK_M, FP8_MAX, TINY)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.amd.ops.swiglu_oai._swiglu_oai_quant_kernel)

SwiGLU-OAI (split layout) fused with per-32-block MXFP8 (E4M3 + E8M0) quant. Each program handles `[BLOCK_M, 32]`

of the `[M, I]`

output (one MX block): it reads the matching gate/up columns from `g1`

(`[M, 2I]`

), computes the SwiGLU in fp32, then derives the block E8M0 scale and emits the FP8 values + scale in a single pass — no bf16 `act`

round-trip to HBM.

## Source code in `vllm/models/minimax_m3/amd/ops/swiglu_oai.py`


##

`swiglu_oai_quantize_mxfp8(gate_up, alpha, beta, limit, block_m=64)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.amd.ops.swiglu_oai.swiglu_oai_quantize_mxfp8)

SwiGLU-OAI on split-layout `[M, 2I]`

fused with MXFP8 activation-quant.

Returns `(act_q [M, I] float8_e4m3fn, act_scale [M, I//32] uint8 E8M0)`

, identical to `mxfp8_e4m3_quantize(swiglu_oai_split(gate_up))`

but in a single Triton pass (no bf16 intermediate). Used between the two GEMMs of the native MXFP8 MoE. Numerically equivalent to the unfused chain (bit-exact on measured MoE shapes); marginally more accurate (fp32 act, no bf16 round-trip).

## Source code in `vllm/models/minimax_m3/amd/ops/swiglu_oai.py`


##

`swiglu_oai_split(gate_up, alpha, beta, limit, out_dtype=None)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.amd.ops.swiglu_oai.swiglu_oai_split)

SwiGLU-OAI on a split-layout `[*, 2I]`

tensor -> `[*, I]`

.