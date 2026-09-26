source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/mxfp8/Mxfp8LinearKernel/
lastmod: 2026-09-24

#

`vllm.model_executor.kernels.linear.mxfp8.Mxfp8LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp8.Mxfp8LinearKernel)

Classes:

-
–[Mxfp8LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp8.Mxfp8LinearKernel.Mxfp8LinearKernel)Base class for MXFP8 quantized linear kernels.

-
–[Mxfp8LinearLayerConfig](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp8.Mxfp8LinearKernel.Mxfp8LinearLayerConfig)Configuration for an MXFP8 linear layer.


##

`Mxfp8LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp8.Mxfp8LinearKernel.Mxfp8LinearKernel)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Base class for MXFP8 quantized linear kernels.

Each subclass implements a specific GEMM backend (FlashInfer CUTLASS, Marlin, emulation).

Methods:

-
–[input_quant_key](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp8.Mxfp8LinearKernel.Mxfp8LinearKernel.input_quant_key)Return the input quantization key supported by this kernel. If the kernel


Attributes:

-
([supports_pre_processed_weights](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp8.Mxfp8LinearKernel.Mxfp8LinearKernel.supports_pre_processed_weights)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)True if

`process_weights_after_loading`

only rewrites parameters, so

## Source code in `vllm/model_executor/kernels/linear/mxfp8/Mxfp8LinearKernel.py`


###

`supports_pre_processed_weights = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp8.Mxfp8LinearKernel.Mxfp8LinearKernel.supports_pre_processed_weights)

True if `process_weights_after_loading`

only rewrites parameters, so weights exported by the weight cache daemon can be used as-is.

###

`input_quant_key()`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp8.Mxfp8LinearKernel.Mxfp8LinearKernel.input_quant_key)

Return the input quantization key supported by this kernel. If the kernel does not support input quantization outside of the kernel, return None.

## Source code in `vllm/model_executor/kernels/linear/mxfp8/Mxfp8LinearKernel.py`


##

`Mxfp8LinearLayerConfig`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp8.Mxfp8LinearKernel.Mxfp8LinearLayerConfig)

Configuration for an MXFP8 linear layer.

All MXFP8 layers share the same structure: FP8-E4M3 weights with uint8 (E8M0) per-block scales at block size 32.