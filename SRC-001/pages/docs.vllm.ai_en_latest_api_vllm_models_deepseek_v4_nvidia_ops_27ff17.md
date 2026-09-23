source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v4/nvidia/ops/
lastmod: 2026-09-23

#

`vllm.models.deepseek_v4.nvidia.ops`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.nvidia.ops)

NVIDIA-only (cutedsl/cutlass) kernels for DeepSeek V4.

These modules import `cutlass`

/`cutedsl`

at module top level, so they must not be imported on non-CUDA platforms. Callers should gate on `vllm.utils.import_utils.has_cutedsl()`

before importing from here.

This `__init__`

deliberately imports nothing: re-exporting the cutedsl modules here would eagerly `import cutlass`

(initializing the CUDA driver) for anyone who imports `vllm.models.deepseek_v4`

, breaking forked subprocesses. Import the leaf modules directly under a `has_cutedsl()`

/`is_cuda()`

gate.

Modules:

-
–[fused_indexer_q_cutedsl](https://docs.vllm.ai/fused_indexer_q_cutedsl/#vllm.models.deepseek_v4.nvidia.ops.fused_indexer_q_cutedsl) -
–[o_proj](https://docs.vllm.ai/o_proj/#vllm.models.deepseek_v4.nvidia.ops.o_proj) -
–[prepare_megamoe](https://docs.vllm.ai/prepare_megamoe/#vllm.models.deepseek_v4.nvidia.ops.prepare_megamoe)Triton input-staging kernel for DeepSeek V4 MegaMoE.

-
–[sparse_attn_compress_cutedsl](https://docs.vllm.ai/sparse_attn_compress_cutedsl/#vllm.models.deepseek_v4.nvidia.ops.sparse_attn_compress_cutedsl)CuTe DSL sparse-attention compressor for DeepSeek V4.