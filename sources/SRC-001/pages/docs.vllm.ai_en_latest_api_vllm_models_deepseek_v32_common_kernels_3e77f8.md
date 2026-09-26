source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v32/common/kernels/
lastmod: 2026-09-24

#

`vllm.models.deepseek_v32.common.kernels`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v32.common.kernels)

Functions:

-
–[fused_eh_norm](https://docs.vllm.ai#vllm.models.deepseek_v32.common.kernels.fused_eh_norm)Returns cat([enorm(masked embeds), hnorm(prev_hidden)]) -> [N, 2H].

-
–[fused_q](https://docs.vllm.ai#vllm.models.deepseek_v32.common.kernels.fused_q)Fuse the MQA-query and indexer-query RoPE/quantization.


##

`_fp8_ue8m0_quantize(vals, FP8_MAX, USE_FNUZ)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v32.common.kernels._fp8_ue8m0_quantize)

Quantize float32 values to FP8 E4M3 with a ue8m0 (power-of-2) scale.

Returns (fp8_vals, scale) so the caller can store them or reuse the scale.

## Source code in `vllm/models/deepseek_v32/common/kernels.py`


##

`_fused_eh_norm_kernel(pos_ptr, embeds_ptr, embeds_stride, prev_ptr, prev_stride, enorm_w_ptr, hnorm_w_ptr, eps, out_ptr, out_stride, H, BLOCK)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v32.common.kernels._fused_eh_norm_kernel)

MTP input fusion: zero embeds at position 0, RMSNorm(embeds) with enorm and RMSNorm(prev_hidden) with hnorm, written side-by-side into `out`

([N, 2H]) ready for the eh_proj GEMM. Replaces where + 2x RMSNorm + cat.

## Source code in `vllm/models/deepseek_v32/common/kernels.py`


##

`fused_eh_norm(positions, inputs_embeds, previous_hidden, enorm_w, hnorm_w, eps)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v32.common.kernels.fused_eh_norm)

Returns cat([enorm(masked embeds), hnorm(prev_hidden)]) -> [N, 2H].

## Source code in `vllm/models/deepseek_v32/common/kernels.py`


##

`fused_q(positions, q_pe, q_pe_cos_sin_cache, index_q, index_q_cos_sin_cache, ql_nope, q_scale, index_weights, index_weights_softmax_scale, index_weights_head_scale, has_indexer=True, index_rope_interleave=False, quantize_mqa=True)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v32.common.kernels.fused_q)

Fuse the MQA-query and indexer-query RoPE/quantization.

Returns `(index_q_fp8, index_weights_out, mqa_q)`

. When `quantize_mqa`

is True (FlashInfer sparse, fp8 query) `mqa_q`

is a single fp8 tensor packing `[ql_nope; q_pe]`

. When False (FlashMLA sparse, bf16 query) it is the RoPE'd `q_pe`

in bf16; the caller pairs it with `ql_nope`

as the `(ql_nope, q_pe)`

tuple the backend expects.

## Source code in `vllm/models/deepseek_v32/common/kernels.py`


|
|