source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/quark/schemes/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.quantization.quark.schemes`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.schemes)

Modules:

Classes:

-
–[QuarkNVFP4](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.schemes.QuarkNVFP4)Quark NVFP4 quantization scheme.

-
–[QuarkScheme](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.schemes.QuarkScheme)Abstract class used to describe the weight creation and forward pass

-
–[QuarkW4A16Int4](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.schemes.QuarkW4A16Int4)Quark packed INT4 weight-only linear scheme via MPLinearKernel.

-
–[QuarkW4A8_MXFP4_FP8](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.schemes.QuarkW4A8_MXFP4_FP8)- Weights: MXFP4 with E8M0 scales per block of 32


##

`QuarkNVFP4`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.schemes.QuarkNVFP4)

Bases: [QuarkScheme](https://docs.vllm.ai/quark_scheme/#vllm.model_executor.layers.quantization.quark.schemes.quark_scheme.QuarkScheme)

Quark NVFP4 quantization scheme.

Supports loading NVFP4 checkpoints with the following structure: - weight: uint8, shape [out_features, in_features // 2] (packed FP4) - weight_scale: float8_e4m3fn, shape [out_features, in_features // group_size] - weight_scale_2: bfloat16/float32, scalar (global weight scale) - input_scale_2: bfloat16/float32, scalar (global input scale)

## Source code in `vllm/model_executor/layers/quantization/quark/schemes/quark_nvfp4.py`


|
|

##

`QuarkScheme`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.schemes.QuarkScheme)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Abstract class used to describe the weight creation and forward pass of different quantization schemes supported by Quark.

Methods:

-
–[apply_weights](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.schemes.QuarkScheme.apply_weights)Run the forward pass for the particular scheme. This is where

-
–[create_weights](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.schemes.QuarkScheme.create_weights)Weight creation for the particular scheme. Inputs to this function.

-
–[get_min_capability](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.schemes.QuarkScheme.get_min_capability)Get minimum device capability.

-
–[process_weights_after_loading](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.schemes.QuarkScheme.process_weights_after_loading)Called after weight loading is complete for any cleanup that


## Source code in `vllm/model_executor/layers/quantization/quark/schemes/quark_scheme.py`


###

`apply_weights(layer, x, bias)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.schemes.QuarkScheme.apply_weights)

Run the forward pass for the particular scheme. This is where scheme-specific dequant/quant steps/kernels should be applied.

Parameters:

-

(`layer`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.schemes.QuarkScheme.apply_weights(layer))

) –[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)torch.nn.Module with the registered weights and other parameters relevant to the particular scheme.

-

(`x`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.schemes.QuarkScheme.apply_weights(x))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)input to the layer

-

(`bias`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.schemes.QuarkScheme.apply_weights(bias))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| Nonebias parameter


## Source code in `vllm/model_executor/layers/quantization/quark/schemes/quark_scheme.py`


###

`create_weights(*args, **kwargs)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.schemes.QuarkScheme.create_weights)

Weight creation for the particular scheme. Inputs to this function.

###

`get_min_capability()`

`abstractmethod`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.schemes.QuarkScheme.get_min_capability)

###

`process_weights_after_loading(layer)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.schemes.QuarkScheme.process_weights_after_loading)

Called after weight loading is complete for any cleanup that needs to occur.

##

`QuarkW4A16Int4`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.schemes.QuarkW4A16Int4)

Bases: [QuarkScheme](https://docs.vllm.ai/quark_scheme/#vllm.model_executor.layers.quantization.quark.schemes.quark_scheme.QuarkScheme)

Quark packed INT4 weight-only linear scheme via MPLinearKernel.

## Source code in `vllm/model_executor/layers/quantization/quark/schemes/quark_w4a16_int4.py`


|
|

##

`QuarkW4A8_MXFP4_FP8`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.schemes.QuarkW4A8_MXFP4_FP8)

Bases: [QuarkScheme](https://docs.vllm.ai/quark_scheme/#vllm.model_executor.layers.quantization.quark.schemes.quark_scheme.QuarkScheme)

- Weights: MXFP4 with E8M0 scales per block of 32
- Activations: FP8 E4M3 (static per-tensor quantization)

Uses the AITER Triton kernel and falls back to emulation if AITER not available.

## Source code in `vllm/model_executor/layers/quantization/quark/schemes/quark_w4a8_mxfp4_fp8.py`


|
|