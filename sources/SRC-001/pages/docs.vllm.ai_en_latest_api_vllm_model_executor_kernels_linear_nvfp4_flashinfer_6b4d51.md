source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/nvfp4/flashinfer/
lastmod: 2026-09-23

#

`vllm.model_executor.kernels.linear.nvfp4.flashinfer`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.nvfp4.flashinfer)

Classes:

-
–[FlashInferB12xNvFp4LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.nvfp4.flashinfer.FlashInferB12xNvFp4LinearKernel)NVFP4 GEMM via FlashInfer's b12x CuTe DSL warp-level MMA kernel (SM120+).

-
–[FlashInferCudnnNvFp4LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.nvfp4.flashinfer.FlashInferCudnnNvFp4LinearKernel)NVFP4 GEMM via FlashInfer's cuDNN wrapper.

-
–[FlashInferCuteDslNvFp4LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.nvfp4.flashinfer.FlashInferCuteDslNvFp4LinearKernel)NVFP4 GEMM via FlashInfer's cutedsl backend.

-
–[FlashInferCuteDslNvFp4W4A16LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.nvfp4.flashinfer.FlashInferCuteDslNvFp4W4A16LinearKernel)BF16 x NVFP4 GEMM via FlashInfer's CuTe-DSL backend.

-
–[FlashInferCutlassNvFp4LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.nvfp4.flashinfer.FlashInferCutlassNvFp4LinearKernel)NVFP4 GEMM via FlashInfer's CUTLASS wrapper.

-
–[FlashInferTrtllmNvFp4LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.nvfp4.flashinfer.FlashInferTrtllmNvFp4LinearKernel)NVFP4 GEMM via FlashInfer's TensorRT-LLM wrapper.


##

`FlashInferB12xNvFp4LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.nvfp4.flashinfer.FlashInferB12xNvFp4LinearKernel)

Bases: [NvFp4LinearKernel](https://docs.vllm.ai/base/#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel)

NVFP4 GEMM via FlashInfer's b12x CuTe DSL warp-level MMA kernel (SM120+).

## Source code in `vllm/model_executor/kernels/linear/nvfp4/flashinfer.py`


##

`FlashInferCudnnNvFp4LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.nvfp4.flashinfer.FlashInferCudnnNvFp4LinearKernel)

Bases: [NvFp4LinearKernel](https://docs.vllm.ai/base/#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel)

NVFP4 GEMM via FlashInfer's cuDNN wrapper.

## Source code in `vllm/model_executor/kernels/linear/nvfp4/flashinfer.py`


##

`FlashInferCuteDslNvFp4LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.nvfp4.flashinfer.FlashInferCuteDslNvFp4LinearKernel)

Bases: [NvFp4LinearKernel](https://docs.vllm.ai/base/#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel)

NVFP4 GEMM via FlashInfer's cutedsl backend.

## Source code in `vllm/model_executor/kernels/linear/nvfp4/flashinfer.py`


##

`FlashInferCuteDslNvFp4W4A16LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.nvfp4.flashinfer.FlashInferCuteDslNvFp4W4A16LinearKernel)

Bases: [NvFp4LinearKernel](https://docs.vllm.ai/base/#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel)

BF16 x NVFP4 GEMM via FlashInfer's CuTe-DSL backend.

## Source code in `vllm/model_executor/kernels/linear/nvfp4/flashinfer.py`


##

`FlashInferCutlassNvFp4LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.nvfp4.flashinfer.FlashInferCutlassNvFp4LinearKernel)

Bases: [NvFp4LinearKernel](https://docs.vllm.ai/base/#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel)

NVFP4 GEMM via FlashInfer's CUTLASS wrapper.

Methods:

-
–[input_quant_key](https://docs.vllm.ai#vllm.model_executor.kernels.linear.nvfp4.flashinfer.FlashInferCutlassNvFp4LinearKernel.input_quant_key)This kernel supports dynamic quantization of the input. By


## Source code in `vllm/model_executor/kernels/linear/nvfp4/flashinfer.py`


|
|

###

`input_quant_key()`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.nvfp4.flashinfer.FlashInferCutlassNvFp4LinearKernel.input_quant_key)

This kernel supports dynamic quantization of the input. By convention, pre-quantized blockscales must use the swizzled layout.

##

`FlashInferTrtllmNvFp4LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.nvfp4.flashinfer.FlashInferTrtllmNvFp4LinearKernel)

Bases: [NvFp4LinearKernel](https://docs.vllm.ai/base/#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel)

NVFP4 GEMM via FlashInfer's TensorRT-LLM wrapper.