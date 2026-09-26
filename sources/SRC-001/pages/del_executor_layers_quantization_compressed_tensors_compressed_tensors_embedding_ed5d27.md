source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_embedding/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.quantization.compressed_tensors.compressed_tensors_embedding`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.compressed_tensors_embedding)

Quantized embedding method for compressed-tensors.

Adds dequant-on-lookup support for a pack-quantized `VocabParallelEmbedding`

(2-8 bit INT, channel- or group-quantized). Only the gathered token rows are unpacked and dequantized, so the packed weight is never densified.

##

`_dequant_gather_kernel(ids_ptr, packed_ptr, scale_ptr, out_ptr, hidden, packed_cols, num_groups, NUM_BITS, PACK_FACTOR, GROUP_SIZE, BLOCK)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.compressed_tensors_embedding._dequant_gather_kernel)

Gather embedding rows by token id, unpack int32-packed INT weights, and dequantize to `out`

dtype in one pass (no int8 intermediate).