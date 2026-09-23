source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v4/nvidia/ops/prepare_megamoe/
lastmod: 2026-09-23

#

`vllm.models.deepseek_v4.nvidia.ops.prepare_megamoe`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.nvidia.ops.prepare_megamoe)

Triton input-staging kernel for DeepSeek V4 MegaMoE.

Quantizes hidden states to fp8 with E8M0 group scales and repacks the routing top-k tensors into the int64/float32 layout that the DeepGEMM MegaMoE kernels consume.