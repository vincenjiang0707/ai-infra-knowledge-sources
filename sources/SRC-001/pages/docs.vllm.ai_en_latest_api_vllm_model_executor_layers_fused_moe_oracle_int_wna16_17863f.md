source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/oracle/int_wna16/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.fused_moe.oracle.int_wna16`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16)

Functions:

-
–[backend_to_kernel_cls](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16.backend_to_kernel_cls)Return the experts class for the given backend, or None for NONE.

-
–[convert_to_wna16_moe_kernel_format](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16.convert_to_wna16_moe_kernel_format)Dispatch weight post-processing to the appropriate per-backend handler.

-
–[make_wna16_moe_quant_config](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16.make_wna16_moe_quant_config)Create the FusedMoEQuantConfig for 4 or 8-bit WNA16 MoE.

-
–[map_wna16_backend](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16.map_wna16_backend)Map user's MoEBackend to WNA16MoEBackend.

-
–[select_wna16_moe_backend](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16.select_wna16_moe_backend)Select the WNA16 MoE backend.


##

`_MoeWNA16HummingWeightSchema`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16._MoeWNA16HummingWeightSchema)

Adapter from MoeWNA16's generic packed layout to Humming's layout.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`


##

`_convert_moe_wna16_humming_tensors(tensors, has_zero_point)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16._convert_moe_wna16_humming_tensors)

Convert MoeWNA16's N-first uint8 packing to Humming's int32 packing.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`


##

`_get_priority_backends()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16._get_priority_backends)

Get available backends in priority order based on platform and config.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`


##

`_humming_wna16_weight_schema(quant_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16._humming_wna16_weight_schema)

Humming weight schema for a WNA16 checkpoint, derived from the quant config rather than the running kernel.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`


##

`_pad_rows(x, padded_rows)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16._pad_rows)

Zero-pad a `(E, rows, cols)`

tensor to `padded_rows`

rows.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`


##

`_pad_w13_bias(bias, n, padded_n)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16._pad_w13_bias)

Zero-pad each gate/up shard of a `(E, 2 * n)`

bias to `padded_n`

.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`


##

`_pad_w13_shard_cols(x, unit, padded_unit)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16._pad_w13_shard_cols)

Zero-pad each of the two gate/up shards of a `(E, rows, 2 * unit)`

tensor along its last dim, from `unit`

to `padded_unit`

columns.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`


##

`_process_awq_weights_marlin(layer, weight_bits, pack_factor, group_size, input_dtype, w13_qweight, w2_qweight, w13_scales, w2_scales, w13_qzeros, w2_qzeros, w13_bias=None, w2_bias=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16._process_awq_weights_marlin)

AWQ-specific Marlin weight post-processing.

AWQ checkpoints use a different packing order than GPTQ, so they need AWQ-specific weight repacking and zero-point conversion before Marlin runs.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`


|
|

##

`_process_weights_cpu(quant_config, w13, w2, w13_scale, w2_scale, w13_qzeros=None, w2_qzeros=None, w13_bias=None, w2_bias=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16._process_weights_cpu)

CPU INT4 W4A16 weight post-processing.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`


|
|

##

`_process_weights_emulation_awq(w13, w2, w13_scale, w2_scale, w13_qzeros, w2_qzeros)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16._process_weights_emulation_awq)

Dequantize AWQ int4 weights to BF16 for the emulation backend.

## AWQ inputs

w13: [E, K, 2*N//8] int32 (packed along N, gate+up on dim 2) w2: [E, N, K//8] int32 (packed along K) w13_scale: [E, K//gs, 2*N] float16 w2_scale: [E, N//gs, K] float16

Outputs (what TritonExperts expects): w13_out: [E, 2*N, K] bfloat16 w2_out: [E, K, N] bfloat16

## Source code in `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`


##

`_process_weights_emulation_gptq(w13, w2, w13_scale, w2_scale, w13_qzeros, w2_qzeros)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16._process_weights_emulation_gptq)

Dequantize int4 weights to BF16 for the emulation backend.

## Inputs are in GPTQ packed format

w13: [E, K//8, 2*N] int32 (gate+up proj stacked on dim 2) w2: [E, N//8, K] int32 w13_scale: [E, K//gs, 2*N] float16 w2_scale: [E, N//gs, K] float16

Outputs (what TritonExperts expects): w13_out: [E, 2*N, K] bfloat16 w2_out: [E, K, N] bfloat16

## Source code in `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`


##

`_process_weights_flashinfer(w13_qweight, w2_qweight, w13_scales, w2_scales, w13_bias=None, w2_bias=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16._process_weights_flashinfer)

Flashinfer (TRT-LLM MXINT4) weight post-processing.

#### Steps[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16._process_weights_flashinfer--steps)

- Transform weights/scales via
`prepare_static_weights_for_trtllm_mxint4_moe`

. - Return transformed tensors and biases.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`


##

`_process_weights_marlin(layer, input_dtype, num_bits, pack_factor, group_size, w13_qweight, w2_qweight, w13_scales, w2_scales, w13_qzeros=None, w2_qzeros=None, w13_bias=None, w2_bias=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16._process_weights_marlin)

Standard Marlin weight post-processing shared by MARLIN and BATCHED_MARLIN backends.

#### Steps[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16._process_weights_marlin--steps)

- Optional FP8 preprocessing of packed weights / scales.
- Repack weights via
`gptq_marlin_moe_repack`

. - Permute scales (and optionally extract INT8 global scales).
- Permute bias tensors.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`


|
|

##

`_process_weights_rdna3(w13, w2, w13_scale, w2_scale, group_size)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16._process_weights_rdna3)

RDNA3 (gfx1100) W4A16 weight post-processing.

Interleaves the packed nibbles per expert (the exllama shuffle the dense RDNA3 kernel also uses) and synthesizes the symmetric zero points that `moe_gptq_gemm_rdna3`

dequantizes with. The packed layout `[E, K // 8, N]`

and the `[E, groups, N]`

scales are already what the kernel wants, so neither is repacked.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`


##

`_process_weights_xpu(layer, quant_config, w13_qweight, w2_qweight, w13_scales, w2_scales, w13_bias=None, w2_bias=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16._process_weights_xpu)

Repack GPTQ-format INT4 MoE weights into the layout `vllm_xpu_kernels.fused_moe_interface.xpu_fused_moe(is_int4=True)`

expects:

```
w13: [E, 2*N, K] int4 (uint8 storage [E, 2*N, K // 2])
w13_scales: [E, 2*N, K // group_size] params_dtype
w2: [E, K, N] int4 (uint8 storage [E, K, N // 2])
w2_scales: [E, K, N // group_size] params_dtype
```


Input GPTQ layout from MoERunner.weight_loader: w13: [E, K // 8, 2*N] int32 (8 nibbles per int32 along the input dim) w13_scales: [E, K // group_size, 2*N] params_dtype w2: [E, N // 8, K] int32 w2_scales: [E, N // group_size, K] params_dtype

Transpose dim 1 ↔ dim 2 then view int32 → uint8 to recover sequential int4-packed bytes along the input dim. Each packed int32 holds 8 nibbles `(n7<<28)|(n6<<24)|...|(n1<<4)|n0`

in ascending K order; on a little-endian host the int32→uint8 view exposes them as bytes `[n1<<4|n0, n3<<4|n2, n5<<4|n4, n7<<4|n6]`

, i.e. two nibbles per byte with the lower nibble = lower input-K index. xpu_fused_moe(is_int4=True) expects this convention; on a big-endian host the byte order reverses and the kernel would silently miscompute, so we hard-fail.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`


|
|

##

`_synthesize_rdna3_qzeros(groups, out_features, device)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16._synthesize_rdna3_qzeros)

Create the packed zero-point tensor for symmetric quantization.

GPTQv1 +1 quirk: the kernel adds 1 to the stored zeros, so encode (bias - 1) = 7 for uint4b8 (bias=8).

## Source code in `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`


##

`_unpack_and_dequant_int4_awq(w_int32, scale, qzeros, transpose_output, output_dtype=torch.bfloat16)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16._unpack_and_dequant_int4_awq)

Unpack AWQ-packed int4 weights and dequantize to output_dtype.

AWQ packs along the N (column) dimension with an interleave permutation [0,2,4,6,1,3,5,7] applied before packing, so unpacking must undo that.

Parameters:

-

(`w_int32`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16._unpack_and_dequant_int4_awq(w_int32))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)packed weights, shape [E, K, N_packed] where N_packed = N//8 (8 nibbles per int32, packed along N with AWQ interleaving).

-

(`scale`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16._unpack_and_dequant_int4_awq(scale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)per-group scales, shape [E, K//group_size, N], float16.

-

(`qzeros`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16._unpack_and_dequant_int4_awq(qzeros))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| Noneasymmetric zero-points, shape [E, K//gs, N_packed], int32. None for symmetric (uint4b8 with implicit bias 8).

-

(`transpose_output`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16._unpack_and_dequant_int4_awq(transpose_output))

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)if True return [E, N, K]; if False return [E, K, N].

-

(`output_dtype`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16._unpack_and_dequant_int4_awq(output_dtype))

, default:[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)`bfloat16`

) –target floating-point dtype (bfloat16 or float16).


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Dequantized weight tensor in the requested layout.


## Source code in `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`


|
|

##

`_unpack_and_dequant_int4_gptq(w_int32, scale, qzeros, transpose_output, output_dtype=torch.bfloat16)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16._unpack_and_dequant_int4_gptq)

Unpack GPTQ-packed int4 weights and dequantize to output_dtype.

Parameters:

-

(`w_int32`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16._unpack_and_dequant_int4_gptq(w_int32))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)packed weights, shape [E, K_packed, N] where K_packed = K//8 (8 nibbles per int32, LSB-first in the K dimension).

-

(`scale`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16._unpack_and_dequant_int4_gptq(scale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)per-group scales, shape [E, K//group_size, N], float16.

-

(`qzeros`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16._unpack_and_dequant_int4_gptq(qzeros))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| Noneoptional asymmetric zero-points, shape [E, K//gs, N//8], int32. None for symmetric (uint4b8 with implicit bias 8).

-

(`transpose_output`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16._unpack_and_dequant_int4_gptq(transpose_output))

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)if True return [E, N, K]; if False return [E, K, N].

-

(`output_dtype`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16._unpack_and_dequant_int4_gptq(output_dtype))

, default:[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)`bfloat16`

) –target floating-point dtype (bfloat16 or float16).


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Dequantized weight tensor in the requested layout.


## Source code in `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`


##

`backend_to_kernel_cls(backend)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16.backend_to_kernel_cls)

Return the experts class for the given backend, or None for NONE.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`


##

`convert_to_wna16_moe_kernel_format(backend, layer, quant_config, input_dtype, w13, w2, w13_scale, w2_scale, w13_qzeros=None, w2_qzeros=None, w13_bias=None, w2_bias=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16.convert_to_wna16_moe_kernel_format)

Dispatch weight post-processing to the appropriate per-backend handler.

To add a new backend, implement a `_process_weights_<name>`

helper and add a branch here. Backends that rewrite the layer's parameters in place (e.g. Humming) return `None`

; the caller then skips the param scatter.

Parameters:

-

(`backend`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16.convert_to_wna16_moe_kernel_format(backend))`WNA16MoEBackend`

) –the selected

`WNA16MoEBackend`

. -

(`layer`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16.convert_to_wna16_moe_kernel_format(layer))

) –[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)the

`MoERunner`

layer whose parameters are being prepared. -

(`quant_config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16.convert_to_wna16_moe_kernel_format(quant_config))

) –[QuantizationConfig](https://docs.vllm.ai/quantization/base_config/#vllm.model_executor.layers.quantization.base_config.QuantizationConfig)| QuantizationArgs | Nonethe

`QuantizationConfig`

for this layer. -

(`input_dtype`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16.convert_to_wna16_moe_kernel_format(input_dtype))

) –[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)| Noneoptional activation dtype, usually should be 16 bit.

-

(`w13`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16.convert_to_wna16_moe_kernel_format(w13))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)fused gate/up expert weights.

-

(`w2`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16.convert_to_wna16_moe_kernel_format(w2))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)down-projection expert weights.

-

(`w13_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16.convert_to_wna16_moe_kernel_format(w13_scale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)quantization scales for

`w13`

. -

(`w2_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16.convert_to_wna16_moe_kernel_format(w2_scale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)quantization scales for

`w2`

. -

(`w13_qzeros`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16.convert_to_wna16_moe_kernel_format(w13_qzeros))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –optional zero points for

`w13`

. -

(`w2_qzeros`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16.convert_to_wna16_moe_kernel_format(w2_qzeros))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –optional zero points for

`w2`

. -

(`w13_bias`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16.convert_to_wna16_moe_kernel_format(w13_bias))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –optional bias for

`w13`

. -

(`w2_bias`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16.convert_to_wna16_moe_kernel_format(w2_bias))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –optional bias for

`w2`

.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`


|
|

##

`make_wna16_moe_quant_config(w1_scale, w2_scale, group_size, num_bits, w1_zp=None, w2_zp=None, w1_bias=None, w2_bias=None, a1_gscale=None, a2_gscale=None, gemm1_clamp_limit=None, gemm1_alpha=None, gemm1_beta=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16.make_wna16_moe_quant_config)

Create the FusedMoEQuantConfig for 4 or 8-bit WNA16 MoE.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`


##

`map_wna16_backend(runner_backend)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16.map_wna16_backend)

Map user's MoEBackend to WNA16MoEBackend.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`


##

`select_wna16_moe_backend(config, weight_key, quant_config, may_have_zp, may_have_bias, allow_tile_padding=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16.select_wna16_moe_backend)

Select the WNA16 MoE backend.

Parameters:

-

(`config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16.select_wna16_moe_backend(config))

) –[FusedMoEConfig](https://docs.vllm.ai/config/#vllm.model_executor.layers.fused_moe.config.FusedMoEConfig)the shared

`FusedMoEConfig`

for this layer. -

(`weight_key`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16.select_wna16_moe_backend(weight_key))

) –[QuantKey](https://docs.vllm.ai/quantization/utils/quant_utils/#vllm.model_executor.layers.quantization.utils.quant_utils.QuantKey)The QuantKey describing the weight quantization. Must have int4 or int8 type.

-

(`quant_config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16.select_wna16_moe_backend(quant_config))

) –[QuantizationConfig](https://docs.vllm.ai/quantization/base_config/#vllm.model_executor.layers.quantization.base_config.QuantizationConfig)| QuantizationArgsQuantization structure and checkpoint format description.

-

(`may_have_zp`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16.select_wna16_moe_backend(may_have_zp))

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether the integration can provide weight zero points.

-

(`may_have_bias`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16.select_wna16_moe_backend(may_have_bias))

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether the integration can provide expert bias.

-

(`allow_tile_padding`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.int_wna16.select_wna16_moe_backend(allow_tile_padding))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether backends that require padding the weights up to a tile boundary may be selected.


Returns:

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[WNA16MoEBackend,[type](https://docs.python.org/3/builtins/functions.html#type)[[FusedMoEExperts](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExperts)]]A tuple of (

`WNA16MoEBackend`

, experts class or`None`

).

## Source code in `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`


|
|