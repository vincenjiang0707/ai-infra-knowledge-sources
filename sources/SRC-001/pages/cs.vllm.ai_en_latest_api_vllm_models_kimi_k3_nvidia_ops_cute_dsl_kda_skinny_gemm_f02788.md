source: https://docs.vllm.ai/en/latest/api/vllm/models/kimi_k3/nvidia/ops/cute_dsl/kda_skinny_gemm/
lastmod: 2026-09-24

#

`vllm.models.kimi_k3.nvidia.ops.cute_dsl.kda_skinny_gemm`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.cute_dsl.kda_skinny_gemm)

Kimi-K3 TP8 skinny GEMMs for the KDA F_A/beta and F_B projections.

##

`_fma_f32_bf16_portable(a, b, acc, *, loc=None, ip=None)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.cute_dsl.kda_skinny_gemm._fma_f32_bf16_portable)

BF16 multiply with FP32 accumulation for pre-SM100 GPUs.

PTX `fma.f32.bf16`

requires SM100 or newer. Converting the operands to FP32 first keeps this kernel available on Hopper, where an unconditional mixed-precision FMA fails libNVVM compilation for `sm_90a`

.

## Source code in `vllm/models/kimi_k3/nvidia/ops/cute_dsl/kda_skinny_gemm.py`


##

`_has_mixed_precision_bf16_fma()`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.cute_dsl.kda_skinny_gemm._has_mixed_precision_bf16_fma)

Whether PTX `fma.f32.bf16`

is supported by the current GPU.