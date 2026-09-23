source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/compressed_tensors/schemes/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.quantization.compressed_tensors.schemes`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.schemes)

Modules:

-
–[compressed_tensors_scheme](https://docs.vllm.ai/compressed_tensors_scheme/#vllm.model_executor.layers.quantization.compressed_tensors.schemes.compressed_tensors_scheme) -
–[compressed_tensors_w4a4_mxfp4](https://docs.vllm.ai/compressed_tensors_w4a4_mxfp4/#vllm.model_executor.layers.quantization.compressed_tensors.schemes.compressed_tensors_w4a4_mxfp4) -
–[compressed_tensors_w8a8_mxfp8](https://docs.vllm.ai/compressed_tensors_w8a8_mxfp8/#vllm.model_executor.layers.quantization.compressed_tensors.schemes.compressed_tensors_w8a8_mxfp8) -
–[compressed_tensors_wNa4](https://docs.vllm.ai/compressed_tensors_wNa4/#vllm.model_executor.layers.quantization.compressed_tensors.schemes.compressed_tensors_wNa4)Weight N-bit INT scheme with symmetric INT4 activation quant via Humming.

-
–[compressed_tensors_wNa8](https://docs.vllm.ai/compressed_tensors_wNa8/#vllm.model_executor.layers.quantization.compressed_tensors.schemes.compressed_tensors_wNa8)Weight N-bit INT scheme with symmetric INT8 activation quant via Humming.

-
–[compressed_tensors_wNa8o8](https://docs.vllm.ai/compressed_tensors_wNa8o8/#vllm.model_executor.layers.quantization.compressed_tensors.schemes.compressed_tensors_wNa8o8)Weight N-bit INT scheme with static INT8 input/output activation quant.


Classes:

-
–[CompressedTensorsScheme](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.schemes.CompressedTensorsScheme)Abstract class used to describe the weight creation and forward pass

-
–[CompressedTensorsW4A4Mxfp4](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.schemes.CompressedTensorsW4A4Mxfp4)Compressed tensors scheme for MXFP4.

-
–[CompressedTensorsW8A8Mxfp8](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.schemes.CompressedTensorsW8A8Mxfp8)Compressed tensors scheme for MXFP8 quantization (W8A8).

-
–[CompressedTensorsWNA4Int](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.schemes.CompressedTensorsWNA4Int) -
–[CompressedTensorsWNA8Int](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.schemes.CompressedTensorsWNA8Int) -
–[CompressedTensorsWNA8O8Int](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.schemes.CompressedTensorsWNA8O8Int)

##

`CompressedTensorsScheme`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.schemes.CompressedTensorsScheme)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Abstract class used to describe the weight creation and forward pass of different quantization schemes supported by CompressedTensors.

Methods:

-
–[apply_weights](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.schemes.CompressedTensorsScheme.apply_weights)Run the forward pass for the particular scheme. This is where

-
–[create_weights](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.schemes.CompressedTensorsScheme.create_weights)Weight creation for the particular scheme. Inputs to this function.

-
–[get_min_capability](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.schemes.CompressedTensorsScheme.get_min_capability)Get minimum device capability.

-
–[process_weights_after_loading](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.schemes.CompressedTensorsScheme.process_weights_after_loading)Called after weight loading is complete for any cleanup that


## Source code in `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_scheme.py`


###

`apply_weights(layer, x, bias)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.schemes.CompressedTensorsScheme.apply_weights)

Run the forward pass for the particular scheme. This is where scheme-specific dequant/quant steps/kernels should be applied.

Parameters:

-

(`layer`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.schemes.CompressedTensorsScheme.apply_weights(layer))

) –[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)torch.nn.Module with the registered weights and other parameters relevant to the particular scheme.

-

(`x`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.schemes.CompressedTensorsScheme.apply_weights(x))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)input to the layer

-

(`bias`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.schemes.CompressedTensorsScheme.apply_weights(bias))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| Nonebias parameter


## Source code in `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_scheme.py`


###

`create_weights(*args, **kwargs)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.schemes.CompressedTensorsScheme.create_weights)

Weight creation for the particular scheme. Inputs to this function.

###

`get_min_capability()`

`abstractmethod`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.schemes.CompressedTensorsScheme.get_min_capability)

###

`process_weights_after_loading(layer)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.schemes.CompressedTensorsScheme.process_weights_after_loading)

Called after weight loading is complete for any cleanup that needs to occur.

## Source code in `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_scheme.py`


##

`CompressedTensorsW4A4Mxfp4`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.schemes.CompressedTensorsW4A4Mxfp4)

Bases: [CompressedTensorsScheme](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.schemes.CompressedTensorsScheme)

Compressed tensors scheme for MXFP4.

Supports models quantized with the compressed-tensors mxfp4-pack-quantized format.

MXFP4 format: - 4-bit float weights (E2M1) packed into uint8 - Per-group E8M0 scales with group_size=32 - No global scale (unlike NVFP4)

On SM100+ with FlashInfer: true W4A4 (activations dynamically quantized). Otherwise: W4A16 weight-only via Marlin.

## Source code in `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_mxfp4.py`


##

`CompressedTensorsW8A8Mxfp8`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.schemes.CompressedTensorsW8A8Mxfp8)

Bases: [CompressedTensorsScheme](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.schemes.CompressedTensorsScheme)

Compressed tensors scheme for MXFP8 quantization (W8A8).

Loads pre-quantized MXFP8 weights from compressed-tensors checkpoints. Activations are dynamically quantized to MXFP8 at runtime.

MXFP8 format: - 8-bit float weights (E4M3) stored as float8_e4m3fn - Per-group E8M0 scales (uint8) with group_size=32 - Activations dynamically quantized to MXFP8 during inference

## Source code in `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_mxfp8.py`


##

`CompressedTensorsWNA4Int`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.schemes.CompressedTensorsWNA4Int)

Bases: [CompressedTensorsScheme](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.schemes.CompressedTensorsScheme)

## Source code in `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa4.py`


|
|

###

`_build_input_quant_config()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.schemes.CompressedTensorsWNA4Int._build_input_quant_config)

Build the config dict that BaseInputSchema.from_config expects.

## Source code in `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa4.py`


##

`CompressedTensorsWNA8Int`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.schemes.CompressedTensorsWNA8Int)

Bases: [CompressedTensorsScheme](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.schemes.CompressedTensorsScheme)

## Source code in `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa8.py`


|
|

###

`_build_input_quant_config()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.schemes.CompressedTensorsWNA8Int._build_input_quant_config)

Build the config dict that BaseInputSchema.from_config expects.

## Source code in `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa8.py`


##

`CompressedTensorsWNA8O8Int`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.schemes.CompressedTensorsWNA8O8Int)

Bases: [CompressedTensorsScheme](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.schemes.CompressedTensorsScheme)

## Source code in `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa8o8.py`


|
|

###

`_pack_int_quantized_weight(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.compressed_tensors.schemes.CompressedTensorsWNA8O8Int._pack_int_quantized_weight)

Normalize an int-quantized (plain int8) weight to the canonical `weight_packed`

int32 + `weight_shape`

layout the MP kernels expect.