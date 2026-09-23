source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16_flydsl/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.quantization.compressed_tensors.compressed_tensors_moe.compressed_tensors_moe_w4a16_flydsl`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.compressed_tensors_moe.compressed_tensors_moe_w4a16_flydsl)

##

`_gptq_int32_to_flydsl_packed(w_int32)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.compressed_tensors_moe.compressed_tensors_moe_w4a16_flydsl._gptq_int32_to_flydsl_packed)

Convert GPTQ int32 [E, K//8, N] to FlyDSL shuffled packed int4 [E, N, K//2]. Steps: 1. Unpack int32 to individual signed int4 values (as int8) 2. Apply FlyDSL preshuffle (on individual int8 values) 3. Pack with FlyDSL's interleaved int4 packing

## Source code in `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16_flydsl.py`


##

`_pack_shuffled_int8_to_packed_int4_no_perm(x_shuf_i8)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.compressed_tensors_moe.compressed_tensors_moe_w4a16_flydsl._pack_shuffled_int8_to_packed_int4_no_perm)

Pack a preshuffled int8 tensor (values in [-8, 7]) into packed int4 bytes. Each contiguous 8-value block [v0..v7] -> 4 bytes: b0=(v4<<4)|v0, b1=(v5<<4)|v1, b2=(v6<<4)|v2, b3=(v7<<4)|v3. This matches the 7-op in-kernel unpack sequence and avoids any v_perm.

## Source code in `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16_flydsl.py`


##

`_unpack_gptq_int32_to_signed_int4(w_int32)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.compressed_tensors_moe.compressed_tensors_moe_w4a16_flydsl._unpack_gptq_int32_to_signed_int4)

Unpack GPTQ int32 [E, K//8, N] to signed int4 values [E, N, K] (as int8). Shared by both the packed-int4 and bf16-dequant paths.