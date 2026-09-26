source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v41/common/ops/query_quant/
lastmod: 2026-09-24

#

`vllm.models.deepseek_v41.common.ops.query_quant`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.query_quant)

Functions:

-
–[can_fuse_query_quant](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.query_quant.can_fuse_query_quant)Require both local projections to use the same MXFP8 activation ABI.

-
–[fused_q_kv_rmsnorm_quant](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.query_quant.fused_q_kv_rmsnorm_quant)Normalize Q/KV and quantize Q with FlashInfer's swizzled MXFP8 scales.


##

`can_fuse_query_quant(linears)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.query_quant.can_fuse_query_quant)

Require both local projections to use the same MXFP8 activation ABI.

## Source code in `vllm/models/deepseek_v41/common/ops/query_quant.py`


##

`fused_q_kv_rmsnorm_quant(qr, kv, q_weight, kv_weight, eps)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.query_quant.fused_q_kv_rmsnorm_quant)

Normalize Q/KV and quantize Q with FlashInfer's swizzled MXFP8 scales.