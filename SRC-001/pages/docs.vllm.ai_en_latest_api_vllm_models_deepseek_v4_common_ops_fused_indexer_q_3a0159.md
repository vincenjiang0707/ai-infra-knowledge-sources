source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v4/common/ops/fused_indexer_q/
lastmod: 2026-09-23

#

`vllm.models.deepseek_v4.common.ops.fused_indexer_q`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.fused_indexer_q)

Functions:

-
–[fused_indexer_q_rope_quant](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.fused_indexer_q.fused_indexer_q_rope_quant)Fused RoPE + quantize Q for the sparse indexer.


##

`_indexer_weights_out_dtypes(vllm_config)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.fused_indexer_q._indexer_weights_out_dtypes)

Weights dtypes the model's indexer layers ask for: fp32 for the dense scoring kernels, plus bf16 when the DeepSeek V4.1 sparse-logits indexer (`SparseMQAIndexer`

) is enabled.

## Source code in `vllm/models/deepseek_v4/common/ops/fused_indexer_q.py`


##

`_quantize_mxfp4_pair(x_lo, x_hi)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.fused_indexer_q._quantize_mxfp4_pair)

Quantize a block of MXFP4_BLOCK_SIZE fp32 values given as two interleaved halves (x_lo = values at even positions in the block, x_hi = values at odd positions). Returns: - packed : uint8[BLOCK/2] (low nibble = quant(x_lo), high = quant(x_hi)) - ue8m0 : scalar uint8 (block scale = 2^(ue8m0 - 127))

## Source code in `vllm/models/deepseek_v4/common/ops/fused_indexer_q.py`


##

`fused_indexer_q_rope_quant(positions, index_q, index_q_cos_sin_cache, index_weights, index_weights_softmax_scale, index_weights_head_scale, use_fp4=False, weights_out_dtype=torch.float32)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.fused_indexer_q.fused_indexer_q_rope_quant)

Fused RoPE + quantize Q for the sparse indexer.

`weights_out_dtype`

is the dtype the downstream scoring kernel takes: fp32 for the dense MQA-logits kernels, bf16 for DeepGEMM's sparse MQA-logits kernels (CUDA MXFP4 path only).

Weight-fold semantics (important — the two paths differ):

FP8 path (use_fp4=False, default): q_fp8 : (T, H, HEAD_DIM) platform fp8 (e4m3fnuz on gfx942, e4m3fn elsewhere); per-token-per-head scalar scale (NOT stored — folded into weights below) weights_out = weights * q_scale * softmax_scale * head_scale Rationale: a single per-token q_scale is a scalar the downstream FP8 logits kernel would otherwise multiply in. Folding it into `weights`

avoids emitting a separate tensor and is free for the logits kernel.

MXFP4 path (use_fp4=True): q_packed : (T, H, HEAD_DIM // 2) uint8 (2 E2M1 nibbles per byte) q_scale : (T, H, HEAD_DIM // MXFP4_BLOCK_SIZE) uint8 ue8m0 bytes weights_out = weights * softmax_scale * head_scale Rationale: MXFP4 has PER-BLOCK (32-element) scales that live with the Q values — they cannot be folded into a per-token weight scalar, so `weights`

carries only the softmax and head scales.

Returns (q_quant, weights_out) where q_quant is either a Tensor (FP8) or a (values, scales) tuple (MXFP4). This matches the union type accepted by `SparseAttnIndexer.forward_*`

.

## Source code in `vllm/models/deepseek_v4/common/ops/fused_indexer_q.py`


|
|