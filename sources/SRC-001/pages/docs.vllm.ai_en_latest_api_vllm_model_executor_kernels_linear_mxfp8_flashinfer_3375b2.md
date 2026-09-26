source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/mxfp8/flashinfer/
lastmod: 2026-09-24

#

`vllm.model_executor.kernels.linear.mxfp8.flashinfer`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp8.flashinfer)

Classes:

-
–[FlashInferCutedslMxfp8LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp8.flashinfer.FlashInferCutedslMxfp8LinearKernel)MXFP8 W8A8 GEMM via FlashInfer CuTe-DSL (SM100/SM103).

-
–[FlashInferCutlassMxfp8LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp8.flashinfer.FlashInferCutlassMxfp8LinearKernel)MXFP8 W8A8 GEMM via FlashInfer CUTLASS (SM100+).

-
–[FlashInferTrtllmMxfp8LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp8.flashinfer.FlashInferTrtllmMxfp8LinearKernel)MXFP8 W8A8 GEMM via FlashInfer's TensorRT-LLM wrapper.


##

`FlashInferCutedslMxfp8LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp8.flashinfer.FlashInferCutedslMxfp8LinearKernel)

Bases: [Mxfp8LinearKernel](https://docs.vllm.ai/Mxfp8LinearKernel/#vllm.model_executor.kernels.linear.mxfp8.Mxfp8LinearKernel.Mxfp8LinearKernel)

MXFP8 W8A8 GEMM via FlashInfer CuTe-DSL (SM100/SM103).

## Source code in `vllm/model_executor/kernels/linear/mxfp8/flashinfer.py`


|
|

##

`FlashInferCutlassMxfp8LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp8.flashinfer.FlashInferCutlassMxfp8LinearKernel)

Bases: [Mxfp8LinearKernel](https://docs.vllm.ai/Mxfp8LinearKernel/#vllm.model_executor.kernels.linear.mxfp8.Mxfp8LinearKernel.Mxfp8LinearKernel)

MXFP8 W8A8 GEMM via FlashInfer CUTLASS (SM100+).

## Source code in `vllm/model_executor/kernels/linear/mxfp8/flashinfer.py`


##

`FlashInferTrtllmMxfp8LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp8.flashinfer.FlashInferTrtllmMxfp8LinearKernel)

Bases: [Mxfp8LinearKernel](https://docs.vllm.ai/Mxfp8LinearKernel/#vllm.model_executor.kernels.linear.mxfp8.Mxfp8LinearKernel.Mxfp8LinearKernel)

MXFP8 W8A8 GEMM via FlashInfer's TensorRT-LLM wrapper.

## Source code in `vllm/model_executor/kernels/linear/mxfp8/flashinfer.py`


|
|