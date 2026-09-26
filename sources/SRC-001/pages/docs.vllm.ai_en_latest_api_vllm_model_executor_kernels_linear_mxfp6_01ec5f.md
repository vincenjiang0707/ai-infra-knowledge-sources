source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/mxfp6/
lastmod: 2026-09-24

#

`vllm.model_executor.kernels.linear.mxfp6`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp6)

Modules:

Classes:

-
–[MxFp6LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp6.MxFp6LinearKernel)Base class for MXFP6 quantized linear kernels.

-
–[MxFp6LinearLayerConfig](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp6.MxFp6LinearLayerConfig)Configuration for an MXFP6 linear layer.


##

`MxFp6LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp6.MxFp6LinearKernel)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Base class for MXFP6 quantized linear kernels.

Each subclass implements a specific GEMM backend (CUTLASS, Marlin, etc). The kernel selection mechanism iterates over registered subclasses in priority order,calling `is_supported`

and `can_implement`

to find the best match for the current hardware.

Methods:

-
–[apply_weights](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp6.MxFp6LinearKernel.apply_weights)Run the quantized GEMM.

-
–[can_implement](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp6.MxFp6LinearKernel.can_implement)Return whether this kernel can handle

*config*. -
–[is_supported](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp6.MxFp6LinearKernel.is_supported)Return whether this kernel can run on the current platform.

-
–[process_weights_after_loading](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp6.MxFp6LinearKernel.process_weights_after_loading)Transform weights into the format required by this kernel.


## Source code in `vllm/model_executor/kernels/linear/mxfp6/base.py`


###

`apply_weights(layer, x, bias=None)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp6.MxFp6LinearKernel.apply_weights)

Run the quantized GEMM.

###

`can_implement(config)`

`abstractmethod`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp6.MxFp6LinearKernel.can_implement)

Return whether this kernel can handle *config*.

###

`is_supported(compute_capability=None)`

`abstractmethod`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp6.MxFp6LinearKernel.is_supported)

Return whether this kernel can run on the current platform.

###

`process_weights_after_loading(layer)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp6.MxFp6LinearKernel.process_weights_after_loading)

Transform weights into the format required by this kernel.

Called once after checkpoint weights have been loaded onto the device. Implementations should repack / swizzle / pad weights and scales in-place on *layer*.

## Source code in `vllm/model_executor/kernels/linear/mxfp6/base.py`


##

`MxFp6LinearLayerConfig`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp6.MxFp6LinearLayerConfig)

Configuration for an MXFP6 linear layer.

All MXFP6 layers share the same structure: packed uint8 weights (4 FP6 values per 3 bytes) and per-block weight scales (group size 32).

Attributes:

-
(`weight_quant_key`


) –[QuantKey](https://docs.vllm.ai/layers/quantization/utils/quant_utils/#vllm.model_executor.layers.quantization.utils.quant_utils.QuantKey)Identifies the weight quantization format. Can be kMxfp6E2M3Static or kMxfp6E3M2Static.

-
(`activation_quant_key`


) –[QuantKey](https://docs.vllm.ai/layers/quantization/utils/quant_utils/#vllm.model_executor.layers.quantization.utils.quant_utils.QuantKey)| NoneIdentifies the activation quantization format, or

`None`

when activations must not be quantized.