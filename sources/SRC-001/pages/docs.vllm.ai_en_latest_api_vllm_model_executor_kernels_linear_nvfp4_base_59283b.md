source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/nvfp4/base/
lastmod: 2026-09-24

#

`vllm.model_executor.kernels.linear.nvfp4.base`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.nvfp4.base)

Classes:

-
–[NvFp4LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel)Base class for NVFP4 quantized linear kernels.

-
–[NvFp4LinearLayerConfig](https://docs.vllm.ai#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearLayerConfig)Configuration for an NVFP4 linear layer.


##

`NvFp4LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Base class for NVFP4 quantized linear kernels.

Each subclass implements a specific GEMM backend (CUTLASS, Marlin, etc). The kernel selection mechanism iterates over registered subclasses in priority order,calling `is_supported`

and `can_implement`

to find the best match for the current hardware.

Methods:

-
–[apply_weights](https://docs.vllm.ai#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel.apply_weights)Run the quantized GEMM.

-
–[can_implement](https://docs.vllm.ai#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel.can_implement)Return whether this kernel can handle

*config*. -
–[input_quant_key](https://docs.vllm.ai#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel.input_quant_key)Return the input quantization key supported by this kernel. If the kernel

-
–[is_supported](https://docs.vllm.ai#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel.is_supported)Return whether this kernel can run on the current platform.

-
–[process_weights_after_loading](https://docs.vllm.ai#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel.process_weights_after_loading)Transform weights into the format required by this kernel.


## Source code in `vllm/model_executor/kernels/linear/nvfp4/base.py`


###

`apply_weights(layer, x, bias=None)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel.apply_weights)

Run the quantized GEMM.

###

`can_implement(config)`

`abstractmethod`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel.can_implement)

Return whether this kernel can handle *config*.

###

`input_quant_key()`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel.input_quant_key)

Return the input quantization key supported by this kernel. If the kernel does not support input quantization outside of the kernel, return None.

###

`is_supported(compute_capability=None)`

`abstractmethod`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel.is_supported)

Return whether this kernel can run on the current platform.

###

`process_weights_after_loading(layer)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel.process_weights_after_loading)

Transform weights into the format required by this kernel.

Called once after checkpoint weights have been loaded onto the device. Implementations should repack / swizzle / pad weights and scales in-place on *layer*.

## Source code in `vllm/model_executor/kernels/linear/nvfp4/base.py`


##

`NvFp4LinearLayerConfig`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearLayerConfig)

Configuration for an NVFP4 linear layer.

All NVFP4 layers share the same structure: packed uint8 weights (2 FP4 values per byte), FP8-E4M3 per-block weight scales (group size 16), and scalar global scales for both weights and activations.