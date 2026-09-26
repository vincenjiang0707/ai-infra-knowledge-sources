source: https://docs.vllm.ai/en/latest/api/vllm/models/inkling/nvidia/ops/silu_and_mul/
lastmod: 2026-09-24

#

`vllm.models.inkling.nvidia.ops.silu_and_mul`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.silu_and_mul)

SwiGLU kernels for the Inkling MLP layers.

`silu_and_mul_triton`

: SiLU-and-mul over the checkpoint's interleaved fused gate/up layout (dense MLP). `sink_silu_mul_epilogue`

: the sink-expert variant with the per-expert dequant scale and per-token gamma fused in.

Functions:

-
–[silu_and_mul_triton](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.silu_and_mul.silu_and_mul_triton)SiLU-and-mul for the interleaved fused gate/up layout.

-
–[sink_silu_mul_epilogue](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.silu_and_mul.sink_silu_mul_epilogue)Fused sink-expert epilogue: silu(g * a_e) * (u * a_e) * (gamma * r_e).


##

`silu_and_mul_triton(gateup_output)`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.silu_and_mul.silu_and_mul_triton)

SiLU-and-mul for the interleaved fused gate/up layout.

Adapted from `inkling_kernels.activation.silu_and_mul_fwd`

(without MXFP).

## Source code in `vllm/models/inkling/nvidia/ops/silu_and_mul.py`


##

`sink_silu_mul_epilogue(raw, alphas, gammas, ratios, n_experts, out_dtype)`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.silu_and_mul.sink_silu_mul_epilogue)

Fused sink-expert epilogue: silu(g * a_e) * (u * a_e) * (gamma * r_e).

One kernel replaces the per-expert dequant column scale, the SwiGLU, and the per-token gamma multiply between the two sink GEMMs.