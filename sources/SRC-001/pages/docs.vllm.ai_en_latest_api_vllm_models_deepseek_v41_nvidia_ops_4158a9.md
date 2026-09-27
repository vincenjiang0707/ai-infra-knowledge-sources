source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v41/nvidia/ops/
lastmod: 2026-09-27

#

`vllm.models.deepseek_v41.nvidia.ops`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.ops)

Modules:

-
–[cute_dsl](https://docs.vllm.ai/cute_dsl/#vllm.models.deepseek_v41.nvidia.ops.cute_dsl)CuTe DSL kernels for DSV4.1 mHC.

-
–[fused_wo_a](https://docs.vllm.ai/fused_wo_a/#vllm.models.deepseek_v41.nvidia.ops.fused_wo_a)DSV4.1 small-batch MXFP8 WO-A with inverse RoPE and quantization.

-
–[mega_mhc](https://docs.vllm.ai/mega_mhc/#vllm.models.deepseek_v41.nvidia.ops.mega_mhc) -
–[mhc](https://docs.vllm.ai/mhc/#vllm.models.deepseek_v41.nvidia.ops.mhc)Dispatch DSV4.1 mHC operations and overlap coefficient generation.

-
–[o_proj](https://docs.vllm.ai/o_proj/#vllm.models.deepseek_v41.nvidia.ops.o_proj)DSV4.1 output projection with a small-batch SM100/SM103 fusion.