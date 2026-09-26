source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/mxfp8/
lastmod: 2026-09-24

#

`vllm.model_executor.kernels.linear.mxfp8`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp8)

Modules:

-
–[Mxfp8LinearKernel](https://docs.vllm.ai/Mxfp8LinearKernel/#vllm.model_executor.kernels.linear.mxfp8.Mxfp8LinearKernel) -
–[b12x](https://docs.vllm.ai/b12x/#vllm.model_executor.kernels.linear.mxfp8.b12x) -
–[deep_gemm](https://docs.vllm.ai/deep_gemm/#vllm.model_executor.kernels.linear.mxfp8.deep_gemm) -
–[emulation](https://docs.vllm.ai/emulation/#vllm.model_executor.kernels.linear.mxfp8.emulation) -
–[flashinfer](https://docs.vllm.ai/flashinfer/#vllm.model_executor.kernels.linear.mxfp8.flashinfer) -
–[humming](https://docs.vllm.ai/humming/#vllm.model_executor.kernels.linear.mxfp8.humming) -
–[marlin](https://docs.vllm.ai/marlin/#vllm.model_executor.kernels.linear.mxfp8.marlin) -
–[rocm_native](https://docs.vllm.ai/rocm_native/#vllm.model_executor.kernels.linear.mxfp8.rocm_native)Native MXFP8 linear GEMM for AMD CDNA4 (gfx950) via Triton

`tl.dot_scaled`

. -
–[xpu](https://docs.vllm.ai/xpu/#vllm.model_executor.kernels.linear.mxfp8.xpu)

Classes:

-
–[Mxfp8LinearLayerConfig](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp8.Mxfp8LinearLayerConfig)Configuration for an MXFP8 linear layer.


##

`Mxfp8LinearLayerConfig`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp8.Mxfp8LinearLayerConfig)

Configuration for an MXFP8 linear layer.

All MXFP8 layers share the same structure: FP8-E4M3 weights with uint8 (E8M0) per-block scales at block size 32.