source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/utils/nvfp4_emulation_utils/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.quantization.utils.nvfp4_emulation_utils`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.nvfp4_emulation_utils)

Functions:

-
–[dequantize_to_dtype](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.nvfp4_emulation_utils.dequantize_to_dtype)Dequantize the fp4 tensor back to high precision.


##

`_dequantize_nvfp4_kernel(fp4_ptr, scale_ptr, global_scale_ptr, output_ptr, rows_per_batch, num_blocks, BLOCK_SIZE, has_batch_global_scale, TILE_BLOCKS)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.nvfp4_emulation_utils._dequantize_nvfp4_kernel)

Triton kernel for NVFP4 dequantization (swizzle=False).

Optimized with 2D tile processing + interleave for coalesced stores.

## Source code in `vllm/model_executor/layers/quantization/utils/nvfp4_emulation_utils.py`


##

`_e2m1_inline(nibble)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.nvfp4_emulation_utils._e2m1_inline)

Decode an NVFP4 nibble (4 bits: 1 sign + 3 magnitude) to float32.

Uses direct IEEE 754 bit construction. For magnitudes 2-7 the FP32 bit pattern is 0x3F000000 + (mag << 22), which is a single shift + add + bitcast. Magnitudes 0 (zero) and 1 (E2M1 subnormal = 0.5) are patched with two tl.where ops.

## Source code in `vllm/model_executor/layers/quantization/utils/nvfp4_emulation_utils.py`


##

`_nvfp4_gathered_bias_kernel(markov_ptr, packed_weight_ptr, weight_scale_ptr, global_scale_ptr, values_ptr, index_ptr, logits_ptr, stride_markov_b, stride_markov_k, stride_weight_v, stride_weight_k, stride_scale_v, stride_scale_k, stride_values_b, stride_values_j, stride_index_b, stride_index_j, stride_logits_b, stride_logits_v, alpha, TOPK, K, NUM_BLOCKS)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.nvfp4_emulation_utils._nvfp4_gathered_bias_kernel)

Apply selected NVFP4 Markov-projection rows to dense logits.

BF16: `weight[index] -> baddbmm_ -> scatter_`

. NVFP4: `gather packed W2 row -> dequantize 16-element blocks -> dot with Markov embedding -> add base value -> scatter corrected logit`

.

The fused NVFP4 path is needed because packed weights cannot be indexed as BF16 rows, while dequantizing the full vocabulary would defeat top-k.

## Source code in `vllm/model_executor/layers/quantization/utils/nvfp4_emulation_utils.py`


|
|

##

`_nvfp4_quant_dequant_kernel(input_ptr, output_ptr, global_scale_ptr, k, num_blocks, BLOCK_SIZE, FP4_MAX_RECIPROCAL, TILE_BLOCKS)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.nvfp4_emulation_utils._nvfp4_quant_dequant_kernel)

Fused NVFP4 quantize-dequantize kernel.

Uses a 2D grid (rows x tiles) to parallelize across both rows and quantization groups within a row. Each program handles TILE_BLOCKS groups at once using vectorized 2D operations.

## Source code in `vllm/model_executor/layers/quantization/utils/nvfp4_emulation_utils.py`


##

`_round_to_fp4(x)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.nvfp4_emulation_utils._round_to_fp4)

Round float values to the nearest E2M1 representable value.

Matches the thresholds in the Python `cast_to_fp4`

exactly.

## Source code in `vllm/model_executor/layers/quantization/utils/nvfp4_emulation_utils.py`


##

`_triton_dequantize_nvfp4(tensor_fp4, tensor_sf, global_scale, dtype, block_size=16)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.nvfp4_emulation_utils._triton_dequantize_nvfp4)

Dequantize NVFP4 using Triton (swizzle=False only).

Supports both 2D and 3D inputs: - 2D: [m, packed_k] -> [m, k] - 3D: [dim0, m, packed_k] -> [dim0, m, k]

## Source code in `vllm/model_executor/layers/quantization/utils/nvfp4_emulation_utils.py`


##

`_triton_nvfp4_quant_dequant(x, global_scale, block_size)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.nvfp4_emulation_utils._triton_nvfp4_quant_dequant)

Triton-accelerated NVFP4 quantize-dequantize.

## Source code in `vllm/model_executor/layers/quantization/utils/nvfp4_emulation_utils.py`


##

`dequantize_to_dtype(tensor_fp4, tensor_sf, global_scale, dtype, block_size=16, swizzle=True)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.nvfp4_emulation_utils.dequantize_to_dtype)

Dequantize the fp4 tensor back to high precision.

Supports both 2D and 3D inputs: - 2D: [m, packed_k] -> [m, k] - 3D: [dim0, m, packed_k] -> [dim0, m, k]

## Source code in `vllm/model_executor/layers/quantization/utils/nvfp4_emulation_utils.py`


##

`ref_nvfp4_quant_dequant(x, global_scale, block_size)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.nvfp4_emulation_utils.ref_nvfp4_quant_dequant)

NVFP4 quantize-dequantize operation.

`global_scale`

is expected to have a single element.