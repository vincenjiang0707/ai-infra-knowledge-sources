source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v41/nvidia/ops/o_proj/
lastmod: 2026-09-27

#

`vllm.models.deepseek_v41.nvidia.ops.o_proj`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.ops.o_proj)

DSV4.1 output projection with a small-batch SM100/SM103 fusion.

Functions:

-
–[dsv41_o_proj](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.ops.o_proj.dsv41_o_proj)`deep_gemm_fp8_o_proj`

with WO-A fused for small SM100/SM103 batches. -
–[register_dsv41_o_proj_warmup](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.ops.o_proj.register_dsv41_o_proj_warmup)Warm the fused WO-A token counts

`dsv41_o_proj`

can dispatch.

##

`_can_fuse_wo_a(layer)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.ops.o_proj._can_fuse_wo_a)

Whether the attention layer matches the fused WO-A kernel's layout.

## Source code in `vllm/models/deepseek_v41/nvidia/ops/o_proj.py`


##

`dsv41_o_proj(layer, attn_out, positions)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.ops.o_proj.dsv41_o_proj)

`deep_gemm_fp8_o_proj`

with WO-A fused for small SM100/SM103 batches.

## Source code in `vllm/models/deepseek_v41/nvidia/ops/o_proj.py`


##

`register_dsv41_o_proj_warmup(layer)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.ops.o_proj.register_dsv41_o_proj_warmup)

Warm the fused WO-A token counts `dsv41_o_proj`

can dispatch.