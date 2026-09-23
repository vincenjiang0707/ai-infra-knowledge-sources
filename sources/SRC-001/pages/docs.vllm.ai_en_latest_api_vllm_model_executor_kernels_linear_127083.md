source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/
lastmod: 2026-09-23

#

`vllm.model_executor.kernels.linear`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear)

This module re-exports linear kernel implementations to provide a stable import interface during an ongoing reorganization. Upcoming PRs will remove the scaled_mm and mixed_precision subdirectories and reorganize kernels by provider (aiter, cutlass, flashinfer, etc.) rather than by precision type. By centralizing exports here, we minimize the need to update imports across other modules when the internal structure changes. If you are adding a new kernel selector or kernel implementation, add it to this **init**.py to maintain import stability.

Modules:

-
–[Mxfp8LinearKernel](https://docs.vllm.ai/mxfp8/Mxfp8LinearKernel/#vllm.model_executor.kernels.linear.mxfp8.Mxfp8LinearKernel) -
–[ScaledMMLinearKernel](https://docs.vllm.ai/scaled_mm/ScaledMMLinearKernel/#vllm.model_executor.kernels.linear.scaled_mm.ScaledMMLinearKernel) -
–[base](https://docs.vllm.ai/base/#vllm.model_executor.kernels.linear.base) -
–[cute_dsl](https://docs.vllm.ai/cute_dsl/#vllm.model_executor.kernels.linear.cute_dsl) -
–[mixed_precision](https://docs.vllm.ai/mixed_precision/#vllm.model_executor.kernels.linear.mixed_precision) -
–[mxfp4](https://docs.vllm.ai/mxfp4/#vllm.model_executor.kernels.linear.mxfp4) -
–[mxfp6](https://docs.vllm.ai/mxfp6/#vllm.model_executor.kernels.linear.mxfp6) -
–[mxfp8](https://docs.vllm.ai/mxfp8/#vllm.model_executor.kernels.linear.mxfp8) -
–[nvfp4](https://docs.vllm.ai/nvfp4/#vllm.model_executor.kernels.linear.nvfp4) -
–[scaled_mm](https://docs.vllm.ai/scaled_mm/#vllm.model_executor.kernels.linear.scaled_mm) -
–[zentorch_utils](https://docs.vllm.ai/zentorch_utils/#vllm.model_executor.kernels.linear.zentorch_utils)Gates zentorch CPU linear dispatch on platform/op availability.


Classes:

-
–[AiterInt8ScaledMMLinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.AiterInt8ScaledMMLinearKernel) -
–[AiterMxfp4LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.AiterMxfp4LinearKernel)AITER-based native MXFP4 GEMM kernel for ROCm.

-
–[B12xFp8BlockScaledMMKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.B12xFp8BlockScaledMMKernel)K128 block-FP8 linear through the native B12X SM120 dense GEMM.

-
–[B12xMxFp4LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.B12xMxFp4LinearKernel)MXFP4 linear through the native B12X SM120 dense GEMM.

-
–[B12xMxfp8LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.B12xMxfp8LinearKernel)ModelOpt MXFP8 linear through the native b12x SM120 dense GEMM path.

-
–[B12xNvFp4LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.B12xNvFp4LinearKernel)ModelOpt NVFP4 linear through the native B12X SM120 dense GEMM.

-
–[B12xTensorFP8ScaledMMLinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.B12xTensorFP8ScaledMMLinearKernel)Static per-tensor FP8 linear through the B12X SM12x dense GEMM.

-
–[CutlassFP8ScaledMMLinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.CutlassFP8ScaledMMLinearKernel) -
–[CutlassNvFp4LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.CutlassNvFp4LinearKernel)NVFP4 GEMM via the vLLM CUTLASS kernel.

-
–[EmulationMxfp4LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.EmulationMxfp4LinearKernel)Software emulation fallback for OCP MXFP4/MXFP6 (dequant + F.linear).

-
–[EmulationMxfp6LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.EmulationMxfp6LinearKernel)Software emulation fallback for OCP MXFP4/MXFP6 (dequant + F.linear).

-
–[EmulationMxfp8LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.EmulationMxfp8LinearKernel)Software emulation fallback for MXFP8 (dequant to BF16).

-
–[EmulationNvFp4LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.EmulationNvFp4LinearKernel)Software emulation fallback for NVFP4 (dequant → BF16 matmul).

-
–[FbgemmNvFp4LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.FbgemmNvFp4LinearKernel)NVFP4 GEMM via FBGEMM.

-
–[FlashInferB12xNvFp4LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.FlashInferB12xNvFp4LinearKernel)NVFP4 GEMM via FlashInfer's b12x CuTe DSL warp-level MMA kernel (SM120+).

-
–[FlashInferCudnnNvFp4LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.FlashInferCudnnNvFp4LinearKernel)NVFP4 GEMM via FlashInfer's cuDNN wrapper.

-
–[FlashInferCuteDslNvFp4LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.FlashInferCuteDslNvFp4LinearKernel)NVFP4 GEMM via FlashInfer's cutedsl backend.

-
–[FlashInferCuteDslNvFp4W4A16LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.FlashInferCuteDslNvFp4W4A16LinearKernel)BF16 x NVFP4 GEMM via FlashInfer's CuTe-DSL backend.

-
–[FlashInferCutedslMxfp8LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.FlashInferCutedslMxfp8LinearKernel)MXFP8 W8A8 GEMM via FlashInfer CuTe-DSL (SM100/SM103).

-
–[FlashInferCutlassMxfp8LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.FlashInferCutlassMxfp8LinearKernel)MXFP8 W8A8 GEMM via FlashInfer CUTLASS (SM100+).

-
–[FlashInferCutlassNvFp4LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.FlashInferCutlassNvFp4LinearKernel)NVFP4 GEMM via FlashInfer's CUTLASS wrapper.

-
–[FlashInferFp8DeepGEMMDynamicBlockScaledKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.FlashInferFp8DeepGEMMDynamicBlockScaledKernel)Conditional FlashInfer / DeepGEMM FP8 block-scaled GEMM.

-
–[FlashInferMxFp4LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.FlashInferMxFp4LinearKernel)MXFP4 W4A4 GEMM via FlashInfer CUTLASS (SM100+).

-
–[FlashInferTrtllmMxfp8LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.FlashInferTrtllmMxfp8LinearKernel)MXFP8 W8A8 GEMM via FlashInfer's TensorRT-LLM wrapper.

-
–[FlashInferTrtllmNvFp4LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.FlashInferTrtllmNvFp4LinearKernel)NVFP4 GEMM via FlashInfer's TensorRT-LLM wrapper.

-
–[HummingMxFp6LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.HummingMxFp6LinearKernel)Humming GEMM for packed MXFP6 E2M3 and E3M2 weights.

-
–[MarlinMxfp8LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.MarlinMxfp8LinearKernel)MXFP8 W8A16 GEMM via Marlin (SM80+).

-
–[MarlinNvFp4LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.MarlinNvFp4LinearKernel)NVFP4 weight-only GEMM via Marlin (W4A16).

-
–[MxFp4LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.MxFp4LinearKernel)Base class for MXFP4 quantized linear kernels.

-
–[MxFp4LinearLayerConfig](https://docs.vllm.ai#vllm.model_executor.kernels.linear.MxFp4LinearLayerConfig)Configuration for an MXFP4 linear layer.

-
–[MxFp6LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.MxFp6LinearKernel)Base class for MXFP6 quantized linear kernels.

-
–[MxFp6LinearLayerConfig](https://docs.vllm.ai#vllm.model_executor.kernels.linear.MxFp6LinearLayerConfig)Configuration for an MXFP6 linear layer.

-
–[Mxfp8LinearLayerConfig](https://docs.vllm.ai#vllm.model_executor.kernels.linear.Mxfp8LinearLayerConfig)Configuration for an MXFP8 linear layer.

-
–[NvFp4LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.NvFp4LinearKernel)Base class for NVFP4 quantized linear kernels.

-
–[NvFp4LinearLayerConfig](https://docs.vllm.ai#vllm.model_executor.kernels.linear.NvFp4LinearLayerConfig)Configuration for an NVFP4 linear layer.

-
–[RDNAHybridW4A16LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.RDNAHybridW4A16LinearKernel)Hybrid W4A16 kernel: HIP skinny for decode, Triton for prefill.

-
–[TorchNvFp4LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.TorchNvFp4LinearKernel)NVFP4 GEMM implemented with PyTorch's native

`torch._scaled_mm`

. -
–[TritonW4A16LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.TritonW4A16LinearKernel)Triton-based W4A16 GEMM kernel for ROCm (MI300 and newer).

-
–[XPUMxFp8LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.XPUMxFp8LinearKernel)MXFP8 W8A8 GEMM on XPU.

-
–[XPUW4A8IntLinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.XPUW4A8IntLinearKernel)XPU kernel for W4A8 integer quantization using oneDNN int4_gemm_w4a8.

-
–[ZentorchInt8ScaledMMLinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.ZentorchInt8ScaledMMLinearKernel) -
–[ZentorchWNA16LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.ZentorchWNA16LinearKernel)W4A16 GPTQ kernel backed by

`torch.ops.zentorch.zentorch_woq_linear`

.

Functions:

-
–[choose_mp_linear_kernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.choose_mp_linear_kernel)Choose an MPLinearKernel that can implement the given config for the given

-
–[init_mxfp4_linear_kernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.init_mxfp4_linear_kernel)Select and instantiate the best MXFP4 linear kernel for the

-
–[init_mxfp6_linear_kernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.init_mxfp6_linear_kernel)Select and instantiate the best MXFP6 linear kernel for the

-
–[init_mxfp8_linear_kernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.init_mxfp8_linear_kernel)Select and instantiate the best MXFP8 linear kernel for the

-
–[init_nvfp4_linear_kernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.init_nvfp4_linear_kernel)Select and instantiate the best NVFP4 linear kernel for the

-
–[register_linear_kernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.register_linear_kernel)Register a new linear kernel class to be considered in kernel selection.


##

`AiterInt8ScaledMMLinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.AiterInt8ScaledMMLinearKernel)

Bases: `CutlassInt8ScaledMMLinearKernel`


Methods:

-
–[apply_weights](https://docs.vllm.ai#vllm.model_executor.kernels.linear.AiterInt8ScaledMMLinearKernel.apply_weights)`AiterInt8ScaledMMLinearKernel`

implements a fused version of

## Source code in `vllm/model_executor/kernels/linear/scaled_mm/aiter.py`


|
|

###

`apply_weights(layer, x, bias=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.AiterInt8ScaledMMLinearKernel.apply_weights)

`AiterInt8ScaledMMLinearKernel`

implements a fused version of `output = torch.mm((scale_a * a), (scale_b * b)).to(out_dtype)`

where scale_a * a and scale_b * b are implemented using numpy-style broadcasting. Currently only support per-tensor-per-tensor GEMM and per-token-per-channel GEMM through AITER w8a8 scaled gemm. `AiterInt8ScaledMMLinearKernel`

also does not support ATIER block scaled GEMM and mix-precision GEMM.

## Source code in `vllm/model_executor/kernels/linear/scaled_mm/aiter.py`


##

`AiterMxfp4LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.AiterMxfp4LinearKernel)

Bases: [MxFp4LinearKernel](https://docs.vllm.ai/mxfp4/base/#vllm.model_executor.kernels.linear.mxfp4.base.MxFp4LinearKernel)

AITER-based native MXFP4 GEMM kernel for ROCm.

## Source code in `vllm/model_executor/kernels/linear/mxfp4/aiter.py`


|
|

##

`B12xFp8BlockScaledMMKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.B12xFp8BlockScaledMMKernel)

Bases: `Fp8BlockScaledMMLinearKernel`


K128 block-FP8 linear through the native B12X SM120 dense GEMM.

## Source code in `vllm/model_executor/kernels/linear/scaled_mm/b12x.py`


|
|

##

`B12xMxFp4LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.B12xMxFp4LinearKernel)

Bases: [MxFp4LinearKernel](https://docs.vllm.ai/mxfp4/base/#vllm.model_executor.kernels.linear.mxfp4.base.MxFp4LinearKernel)

MXFP4 linear through the native B12X SM120 dense GEMM.

## Source code in `vllm/model_executor/kernels/linear/mxfp4/b12x.py`


##

`B12xMxfp8LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.B12xMxfp8LinearKernel)

Bases: [Mxfp8LinearKernel](https://docs.vllm.ai/mxfp8/Mxfp8LinearKernel/#vllm.model_executor.kernels.linear.mxfp8.Mxfp8LinearKernel.Mxfp8LinearKernel)

ModelOpt MXFP8 linear through the native b12x SM120 dense GEMM path.

## Source code in `vllm/model_executor/kernels/linear/mxfp8/b12x.py`


|
|

##

`B12xNvFp4LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.B12xNvFp4LinearKernel)

Bases: [NvFp4LinearKernel](https://docs.vllm.ai/nvfp4/base/#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel)

ModelOpt NVFP4 linear through the native B12X SM120 dense GEMM.

## Source code in `vllm/model_executor/kernels/linear/nvfp4/b12x.py`


##

`B12xTensorFP8ScaledMMLinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.B12xTensorFP8ScaledMMLinearKernel)

Bases: `FP8ScaledMMLinearKernel`


Static per-tensor FP8 linear through the B12X SM12x dense GEMM.

## Source code in `vllm/model_executor/kernels/linear/scaled_mm/b12x.py`


|
|

##

`CutlassFP8ScaledMMLinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.CutlassFP8ScaledMMLinearKernel)

Bases: `FP8ScaledMMLinearKernel`


Methods:

-
–[input_quant_key](https://docs.vllm.ai#vllm.model_executor.kernels.linear.CutlassFP8ScaledMMLinearKernel.input_quant_key)Only static per-tensor activation quantization is supported for external


## Source code in `vllm/model_executor/kernels/linear/scaled_mm/cutlass.py`


|
|

###

`_pad_to_alignment(x, dim, alignment, value=0.0)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.CutlassFP8ScaledMMLinearKernel._pad_to_alignment)

Pad tensor `x`

along `dim`

to the next multiple of `alignment`

.

## Source code in `vllm/model_executor/kernels/linear/scaled_mm/cutlass.py`


###

`input_quant_key()`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.CutlassFP8ScaledMMLinearKernel.input_quant_key)

Only static per-tensor activation quantization is supported for external quantization.

## Source code in `vllm/model_executor/kernels/linear/scaled_mm/cutlass.py`


##

`CutlassNvFp4LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.CutlassNvFp4LinearKernel)

Bases: [NvFp4LinearKernel](https://docs.vllm.ai/nvfp4/base/#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel)

NVFP4 GEMM via the vLLM CUTLASS kernel.

## Source code in `vllm/model_executor/kernels/linear/nvfp4/cutlass.py`


##

`EmulationMxfp4LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.EmulationMxfp4LinearKernel)

Bases: [MxFp4LinearKernel](https://docs.vllm.ai/mxfp4/base/#vllm.model_executor.kernels.linear.mxfp4.base.MxFp4LinearKernel)

Software emulation fallback for OCP MXFP4/MXFP6 (dequant + F.linear).

## Source code in `vllm/model_executor/kernels/linear/mxfp4/emulation.py`


##

`EmulationMxfp6LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.EmulationMxfp6LinearKernel)

Bases: [MxFp6LinearKernel](https://docs.vllm.ai/mxfp6/base/#vllm.model_executor.kernels.linear.mxfp6.base.MxFp6LinearKernel)

Software emulation fallback for OCP MXFP4/MXFP6 (dequant + F.linear).

## Source code in `vllm/model_executor/kernels/linear/mxfp6/emulation.py`


##

`EmulationMxfp8LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.EmulationMxfp8LinearKernel)

Bases: [Mxfp8LinearKernel](https://docs.vllm.ai/mxfp8/Mxfp8LinearKernel/#vllm.model_executor.kernels.linear.mxfp8.Mxfp8LinearKernel.Mxfp8LinearKernel)

Software emulation fallback for MXFP8 (dequant to BF16).

## Source code in `vllm/model_executor/kernels/linear/mxfp8/emulation.py`


##

`EmulationNvFp4LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.EmulationNvFp4LinearKernel)

Bases: [NvFp4LinearKernel](https://docs.vllm.ai/nvfp4/base/#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel)

Software emulation fallback for NVFP4 (dequant → BF16 matmul).

## Source code in `vllm/model_executor/kernels/linear/nvfp4/emulation.py`


##

`FbgemmNvFp4LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.FbgemmNvFp4LinearKernel)

Bases: [NvFp4LinearKernel](https://docs.vllm.ai/nvfp4/base/#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel)

NVFP4 GEMM via FBGEMM.

## Source code in `vllm/model_executor/kernels/linear/nvfp4/fbgemm.py`


##

`FlashInferB12xNvFp4LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.FlashInferB12xNvFp4LinearKernel)

Bases: [NvFp4LinearKernel](https://docs.vllm.ai/nvfp4/base/#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel)

NVFP4 GEMM via FlashInfer's b12x CuTe DSL warp-level MMA kernel (SM120+).

## Source code in `vllm/model_executor/kernels/linear/nvfp4/flashinfer.py`


##

`FlashInferCudnnNvFp4LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.FlashInferCudnnNvFp4LinearKernel)

Bases: [NvFp4LinearKernel](https://docs.vllm.ai/nvfp4/base/#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel)

NVFP4 GEMM via FlashInfer's cuDNN wrapper.

## Source code in `vllm/model_executor/kernels/linear/nvfp4/flashinfer.py`


##

`FlashInferCuteDslNvFp4LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.FlashInferCuteDslNvFp4LinearKernel)

Bases: [NvFp4LinearKernel](https://docs.vllm.ai/nvfp4/base/#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel)

NVFP4 GEMM via FlashInfer's cutedsl backend.

## Source code in `vllm/model_executor/kernels/linear/nvfp4/flashinfer.py`


##

`FlashInferCuteDslNvFp4W4A16LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.FlashInferCuteDslNvFp4W4A16LinearKernel)

Bases: [NvFp4LinearKernel](https://docs.vllm.ai/nvfp4/base/#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel)

BF16 x NVFP4 GEMM via FlashInfer's CuTe-DSL backend.

## Source code in `vllm/model_executor/kernels/linear/nvfp4/flashinfer.py`


##

`FlashInferCutedslMxfp8LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.FlashInferCutedslMxfp8LinearKernel)

Bases: [Mxfp8LinearKernel](https://docs.vllm.ai/mxfp8/Mxfp8LinearKernel/#vllm.model_executor.kernels.linear.mxfp8.Mxfp8LinearKernel.Mxfp8LinearKernel)

MXFP8 W8A8 GEMM via FlashInfer CuTe-DSL (SM100/SM103).

## Source code in `vllm/model_executor/kernels/linear/mxfp8/flashinfer.py`


|
|

##

`FlashInferCutlassMxfp8LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.FlashInferCutlassMxfp8LinearKernel)

Bases: [Mxfp8LinearKernel](https://docs.vllm.ai/mxfp8/Mxfp8LinearKernel/#vllm.model_executor.kernels.linear.mxfp8.Mxfp8LinearKernel.Mxfp8LinearKernel)

MXFP8 W8A8 GEMM via FlashInfer CUTLASS (SM100+).

## Source code in `vllm/model_executor/kernels/linear/mxfp8/flashinfer.py`


##

`FlashInferCutlassNvFp4LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.FlashInferCutlassNvFp4LinearKernel)

Bases: [NvFp4LinearKernel](https://docs.vllm.ai/nvfp4/base/#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel)

NVFP4 GEMM via FlashInfer's CUTLASS wrapper.

Methods:

-
–[input_quant_key](https://docs.vllm.ai#vllm.model_executor.kernels.linear.FlashInferCutlassNvFp4LinearKernel.input_quant_key)This kernel supports dynamic quantization of the input. By


## Source code in `vllm/model_executor/kernels/linear/nvfp4/flashinfer.py`


|
|

###

`input_quant_key()`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.FlashInferCutlassNvFp4LinearKernel.input_quant_key)

This kernel supports dynamic quantization of the input. By convention, pre-quantized blockscales must use the swizzled layout.

##

`FlashInferFp8DeepGEMMDynamicBlockScaledKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.FlashInferFp8DeepGEMMDynamicBlockScaledKernel)

Bases: [Fp8BlockScaledDynamicMMLinearKernel](https://docs.vllm.ai/scaled_mm/BlockScaledMMLinearKernel/#vllm.model_executor.kernels.linear.scaled_mm.BlockScaledMMLinearKernel.Fp8BlockScaledDynamicMMLinearKernel)

Conditional FlashInfer / DeepGEMM FP8 block-scaled GEMM.

Dispatches between two kernels based on input batch size: - Small batches (M < 32): FlashInfer's swapAB trick for better utilisation. - Large batches (M >= 32): DeepGEMM for peak throughput.

apply_input_quant is False because FlashInfer accepts BF16 input and handles FP8 conversion internally. The DeepGEMM branch therefore quantises BF16→FP8 inside apply_mm via a closure before dispatching to the DeepGEMM kernel — keeping both branches compatible with the single BF16 tensor operand list passed by torch.cond.

## Source code in `vllm/model_executor/kernels/linear/scaled_mm/flashinfer.py`


##

`FlashInferMxFp4LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.FlashInferMxFp4LinearKernel)

Bases: [MxFp4LinearKernel](https://docs.vllm.ai/mxfp4/base/#vllm.model_executor.kernels.linear.mxfp4.base.MxFp4LinearKernel)

MXFP4 W4A4 GEMM via FlashInfer CUTLASS (SM100+).

## Source code in `vllm/model_executor/kernels/linear/mxfp4/flashinfer.py`


##

`FlashInferTrtllmMxfp8LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.FlashInferTrtllmMxfp8LinearKernel)

Bases: [Mxfp8LinearKernel](https://docs.vllm.ai/mxfp8/Mxfp8LinearKernel/#vllm.model_executor.kernels.linear.mxfp8.Mxfp8LinearKernel.Mxfp8LinearKernel)

MXFP8 W8A8 GEMM via FlashInfer's TensorRT-LLM wrapper.

## Source code in `vllm/model_executor/kernels/linear/mxfp8/flashinfer.py`


|
|

##

`FlashInferTrtllmNvFp4LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.FlashInferTrtllmNvFp4LinearKernel)

Bases: [NvFp4LinearKernel](https://docs.vllm.ai/nvfp4/base/#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel)

NVFP4 GEMM via FlashInfer's TensorRT-LLM wrapper.

## Source code in `vllm/model_executor/kernels/linear/nvfp4/flashinfer.py`


##

`HummingMxFp6LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.HummingMxFp6LinearKernel)

Bases: [MxFp6LinearKernel](https://docs.vllm.ai/mxfp6/base/#vllm.model_executor.kernels.linear.mxfp6.base.MxFp6LinearKernel)

Humming GEMM for packed MXFP6 E2M3 and E3M2 weights.

## Source code in `vllm/model_executor/kernels/linear/mxfp6/humming.py`


##

`MarlinMxfp8LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.MarlinMxfp8LinearKernel)

Bases: [Mxfp8LinearKernel](https://docs.vllm.ai/mxfp8/Mxfp8LinearKernel/#vllm.model_executor.kernels.linear.mxfp8.Mxfp8LinearKernel.Mxfp8LinearKernel)

MXFP8 W8A16 GEMM via Marlin (SM80+).

## Source code in `vllm/model_executor/kernels/linear/mxfp8/marlin.py`


##

`MarlinNvFp4LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.MarlinNvFp4LinearKernel)

Bases: [NvFp4LinearKernel](https://docs.vllm.ai/nvfp4/base/#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel)

NVFP4 weight-only GEMM via Marlin (W4A16).

## Source code in `vllm/model_executor/kernels/linear/nvfp4/marlin.py`


##

`MxFp4LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.MxFp4LinearKernel)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Base class for MXFP4 quantized linear kernels.

Each subclass implements a specific GEMM backend (CUTLASS, Marlin, etc). The kernel selection mechanism iterates over registered subclasses in priority order,calling `is_supported`

and `can_implement`

to find the best match for the current hardware.

Methods:

-
–[apply_weights](https://docs.vllm.ai#vllm.model_executor.kernels.linear.MxFp4LinearKernel.apply_weights)Run the quantized GEMM.

-
–[can_implement](https://docs.vllm.ai#vllm.model_executor.kernels.linear.MxFp4LinearKernel.can_implement)Return whether this kernel can handle

*config*. -
–[is_supported](https://docs.vllm.ai#vllm.model_executor.kernels.linear.MxFp4LinearKernel.is_supported)Return whether this kernel can run on the current platform.

-
–[process_weights_after_loading](https://docs.vllm.ai#vllm.model_executor.kernels.linear.MxFp4LinearKernel.process_weights_after_loading)Transform weights into the format required by this kernel.


## Source code in `vllm/model_executor/kernels/linear/mxfp4/base.py`


###

`apply_weights(layer, x, bias=None)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.MxFp4LinearKernel.apply_weights)

Run the quantized GEMM.

###

`can_implement(config)`

`abstractmethod`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.MxFp4LinearKernel.can_implement)

Return whether this kernel can handle *config*.

###

`is_supported(compute_capability=None)`

`abstractmethod`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.MxFp4LinearKernel.is_supported)

Return whether this kernel can run on the current platform.

###

`process_weights_after_loading(layer)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.MxFp4LinearKernel.process_weights_after_loading)

Transform weights into the format required by this kernel.

Called once after checkpoint weights have been loaded onto the device. Implementations should repack / swizzle / pad weights and scales in-place on *layer*.

## Source code in `vllm/model_executor/kernels/linear/mxfp4/base.py`


##

`MxFp4LinearLayerConfig`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.MxFp4LinearLayerConfig)

Configuration for an MXFP4 linear layer.

All MXFP4 layers share the same structure: packed uint8 weights (2 FP4 values per byte) and per-block weight scales (group size 32).

Attributes:

-
(`activation_quant_key`


) –[QuantKey](https://docs.vllm.ai/layers/quantization/utils/quant_utils/#vllm.model_executor.layers.quantization.utils.quant_utils.QuantKey)| NoneIdentifies the activation quantization format, or

`None`

when activations must not be quantized.

## Source code in `vllm/model_executor/kernels/linear/mxfp4/base.py`


##

`MxFp6LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.MxFp6LinearKernel)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Base class for MXFP6 quantized linear kernels.

Each subclass implements a specific GEMM backend (CUTLASS, Marlin, etc). The kernel selection mechanism iterates over registered subclasses in priority order,calling `is_supported`

and `can_implement`

to find the best match for the current hardware.

Methods:

-
–[apply_weights](https://docs.vllm.ai#vllm.model_executor.kernels.linear.MxFp6LinearKernel.apply_weights)Run the quantized GEMM.

-
–[can_implement](https://docs.vllm.ai#vllm.model_executor.kernels.linear.MxFp6LinearKernel.can_implement)Return whether this kernel can handle

*config*. -
–[is_supported](https://docs.vllm.ai#vllm.model_executor.kernels.linear.MxFp6LinearKernel.is_supported)Return whether this kernel can run on the current platform.

-
–[process_weights_after_loading](https://docs.vllm.ai#vllm.model_executor.kernels.linear.MxFp6LinearKernel.process_weights_after_loading)Transform weights into the format required by this kernel.


## Source code in `vllm/model_executor/kernels/linear/mxfp6/base.py`


###

`apply_weights(layer, x, bias=None)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.MxFp6LinearKernel.apply_weights)

Run the quantized GEMM.

###

`can_implement(config)`

`abstractmethod`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.MxFp6LinearKernel.can_implement)

Return whether this kernel can handle *config*.

###

`is_supported(compute_capability=None)`

`abstractmethod`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.MxFp6LinearKernel.is_supported)

Return whether this kernel can run on the current platform.

###

`process_weights_after_loading(layer)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.MxFp6LinearKernel.process_weights_after_loading)

Transform weights into the format required by this kernel.

Called once after checkpoint weights have been loaded onto the device. Implementations should repack / swizzle / pad weights and scales in-place on *layer*.

## Source code in `vllm/model_executor/kernels/linear/mxfp6/base.py`


##

`MxFp6LinearLayerConfig`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.MxFp6LinearLayerConfig)

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

## Source code in `vllm/model_executor/kernels/linear/mxfp6/base.py`


##

`Mxfp8LinearLayerConfig`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.Mxfp8LinearLayerConfig)

Configuration for an MXFP8 linear layer.

All MXFP8 layers share the same structure: FP8-E4M3 weights with uint8 (E8M0) per-block scales at block size 32.

## Source code in `vllm/model_executor/kernels/linear/mxfp8/Mxfp8LinearKernel.py`


##

`NvFp4LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.NvFp4LinearKernel)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Base class for NVFP4 quantized linear kernels.

Each subclass implements a specific GEMM backend (CUTLASS, Marlin, etc). The kernel selection mechanism iterates over registered subclasses in priority order,calling `is_supported`

and `can_implement`

to find the best match for the current hardware.

Methods:

-
–[apply_weights](https://docs.vllm.ai#vllm.model_executor.kernels.linear.NvFp4LinearKernel.apply_weights)Run the quantized GEMM.

-
–[can_implement](https://docs.vllm.ai#vllm.model_executor.kernels.linear.NvFp4LinearKernel.can_implement)Return whether this kernel can handle

*config*. -
–[input_quant_key](https://docs.vllm.ai#vllm.model_executor.kernels.linear.NvFp4LinearKernel.input_quant_key)Return the input quantization key supported by this kernel. If the kernel

-
–[is_supported](https://docs.vllm.ai#vllm.model_executor.kernels.linear.NvFp4LinearKernel.is_supported)Return whether this kernel can run on the current platform.

-
–[process_weights_after_loading](https://docs.vllm.ai#vllm.model_executor.kernels.linear.NvFp4LinearKernel.process_weights_after_loading)Transform weights into the format required by this kernel.


## Source code in `vllm/model_executor/kernels/linear/nvfp4/base.py`


###

`apply_weights(layer, x, bias=None)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.NvFp4LinearKernel.apply_weights)

Run the quantized GEMM.

###

`can_implement(config)`

`abstractmethod`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.NvFp4LinearKernel.can_implement)

Return whether this kernel can handle *config*.

###

`input_quant_key()`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.NvFp4LinearKernel.input_quant_key)

Return the input quantization key supported by this kernel. If the kernel does not support input quantization outside of the kernel, return None.

###

`is_supported(compute_capability=None)`

`abstractmethod`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.NvFp4LinearKernel.is_supported)

Return whether this kernel can run on the current platform.

###

`process_weights_after_loading(layer)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.NvFp4LinearKernel.process_weights_after_loading)

Transform weights into the format required by this kernel.

Called once after checkpoint weights have been loaded onto the device. Implementations should repack / swizzle / pad weights and scales in-place on *layer*.

## Source code in `vllm/model_executor/kernels/linear/nvfp4/base.py`


##

`NvFp4LinearLayerConfig`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.NvFp4LinearLayerConfig)

Configuration for an NVFP4 linear layer.

All NVFP4 layers share the same structure: packed uint8 weights (2 FP4 values per byte), FP8-E4M3 per-block weight scales (group size 16), and scalar global scales for both weights and activations.

## Source code in `vllm/model_executor/kernels/linear/nvfp4/base.py`


##

`RDNAHybridW4A16LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.RDNAHybridW4A16LinearKernel)

Bases: `MPLinearKernel`


Hybrid W4A16 kernel: HIP skinny for decode, Triton for prefill.

Stores the weights once as int8 [N, K//2] (ExLlama shuffle packed). The HIP skinny kernel reads it directly; the triton kernel reinterprets the same buffer as int32 [N, K//8] via a view, so there is no dual weight storage.

## Source code in `vllm/model_executor/kernels/linear/mixed_precision/rdna_hybrid_w4a16.py`


|
|

##

`TorchNvFp4LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.TorchNvFp4LinearKernel)

Bases: [NvFp4LinearKernel](https://docs.vllm.ai/nvfp4/base/#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel)

NVFP4 GEMM implemented with PyTorch's native `torch._scaled_mm`

.

Eager execution uses PyTorch's native scaled-matmul implementation. Under `torch.compile`

, TorchInductor may select any enabled scaled-GEMM backend, including NVGEMM on supported Blackwell systems.

## Source code in `vllm/model_executor/kernels/linear/nvfp4/pytorch.py`


##

`TritonW4A16LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.TritonW4A16LinearKernel)

Bases: `MPLinearKernel`


Triton-based W4A16 GEMM kernel for ROCm (MI300 and newer).

Supports GPTQ-format int4 weights (uint4b8 symmetric, uint4 asymmetric) with grouped quantization. Weight tensors are transposed from the compressed-tensors checkpoint layout to the kernel's [K, N//8] layout.

Methods:

-
–[process_weights_after_loading](https://docs.vllm.ai#vllm.model_executor.kernels.linear.TritonW4A16LinearKernel.process_weights_after_loading)Convert compressed-tensors checkpoint layout to kernel layout.


## Source code in `vllm/model_executor/kernels/linear/mixed_precision/triton_w4a16.py`


|
|

###

`process_weights_after_loading(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.TritonW4A16LinearKernel.process_weights_after_loading)

Convert compressed-tensors checkpoint layout to kernel layout.

Checkpoint (from compressed_tensors_wNa16.create_weights): weight_packed: [N, K//8] int32 input_dim=1, output_dim=0, packed_dim=1 weight_scale: [N, K//G] fp16 input_dim=1, output_dim=0 weight_zero_point: [N//8, K//G] int32 output_dim=0, packed_dim=0

## Kernel needs

qweight: [K, N//8] int32 (transpose weight_packed) scales: [K//G, N] fp16 (transpose weight_scale) qzeros: [K//G, N//8] int32 (transpose weight_zero_point)

## Source code in `vllm/model_executor/kernels/linear/mixed_precision/triton_w4a16.py`


|
|

##

`XPUMxFp8LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.XPUMxFp8LinearKernel)

Bases: [Mxfp8LinearKernel](https://docs.vllm.ai/mxfp8/Mxfp8LinearKernel/#vllm.model_executor.kernels.linear.mxfp8.Mxfp8LinearKernel.Mxfp8LinearKernel)

MXFP8 W8A8 GEMM on XPU.

## Source code in `vllm/model_executor/kernels/linear/mxfp8/xpu.py`


###

`_prepare_bmm_params(layer, scale_kn)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.XPUMxFp8LinearKernel._prepare_bmm_params)

Precompute batched weight and scale for grouped fp8_bmm (e.g. wo_a).

Splits scale [K//32, N_total] into [G, K//32, N_per_group] and weight [N_total, K] into contiguous [G, K, N_per_group] for batch GEMM.

## Source code in `vllm/model_executor/kernels/linear/mxfp8/xpu.py`


##

`XPUW4A8IntLinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.XPUW4A8IntLinearKernel)

Bases: `MPLinearKernel`


XPU kernel for W4A8 integer quantization using oneDNN int4_gemm_w4a8.

Weights are symmetric group-quantized int4 packed as uint4. Activations are dynamically quantized per-token to symmetric int8.

## Source code in `vllm/model_executor/kernels/linear/mixed_precision/xpu.py`


|
|

##

`ZentorchInt8ScaledMMLinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.ZentorchInt8ScaledMMLinearKernel)

Bases: `Int8ScaledMMLinearKernel`


Methods:

-
–[process_weights_after_loading](https://docs.vllm.ai#vllm.model_executor.kernels.linear.ZentorchInt8ScaledMMLinearKernel.process_weights_after_loading)Prepare weights for

`zentorch_dynamic_qlinear`

.

## Source code in `vllm/model_executor/kernels/linear/scaled_mm/zentorch.py`


###

`process_weights_after_loading(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.ZentorchInt8ScaledMMLinearKernel.process_weights_after_loading)

Prepare weights for `zentorch_dynamic_qlinear`

.

Keeps weight in [N, K] layout (int8, contiguous) and converts the per-channel weight scale to bf16 with shape `(N,)`

.

## Source code in `vllm/model_executor/kernels/linear/scaled_mm/zentorch.py`


##

`ZentorchWNA16LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.ZentorchWNA16LinearKernel)

Bases: `CPUWNA16LinearKernel`


W4A16 GPTQ kernel backed by `torch.ops.zentorch.zentorch_woq_linear`

.

Methods:

-
–[process_weights_after_loading](https://docs.vllm.ai#vllm.model_executor.kernels.linear.ZentorchWNA16LinearKernel.process_weights_after_loading)Repack CT GPTQ weights into the zentorch WOQ layout.


## Source code in `vllm/model_executor/kernels/linear/mixed_precision/zentorch.py`


|
|

###

`_zentorch_woq_eligible(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.ZentorchWNA16LinearKernel._zentorch_woq_eligible)

Eligibility predicate for the zentorch W4A16 GPTQ fast path.

Constraints (any failure -> `cpu_gemm_wna16`

path via `super()`

with `layer`

untouched).

## Source code in `vllm/model_executor/kernels/linear/mixed_precision/zentorch.py`


###

`process_weights_after_loading(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.ZentorchWNA16LinearKernel.process_weights_after_loading)

Repack CT GPTQ weights into the zentorch WOQ layout.

Falls back to `CPUWNA16LinearKernel.process_weights_after_loading`

via `super()`

when the layer doesn't satisfy `_zentorch_woq_eligible`

.

On success, `layer._zentorch_processed_weights`

is set to `True`


## Source code in `vllm/model_executor/kernels/linear/mixed_precision/zentorch.py`


|
|

##

`_filter_kernels_by_backend(backend, kernels)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear._filter_kernels_by_backend)

Prefer matching kernels, falling back to auto by layer type.

## Source code in `vllm/model_executor/kernels/linear/__init__.py`


##

`_get_linear_backend(*, quantization)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear._get_linear_backend)

Get the linear_backend setting from the current vllm config.

## Source code in `vllm/model_executor/kernels/linear/__init__.py`


##

`_resolve_backend_kernels(kernels, layer_desc, *, quantization)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear._resolve_backend_kernels)

Apply --linear-backend filtering to one layer type's kernel list.

When the requested backend has no kernel for this layer type, fall back to the unfiltered list (with a WARNING log) instead of failing engine startup: an explicitly requested backend usually provides kernels for a single quantization scheme, while a model can contain several linear layer types (e.g. NVFP4 MoE projections next to FP8 attention projections).

## Source code in `vllm/model_executor/kernels/linear/__init__.py`


##

`choose_mp_linear_kernel(config, compute_capability=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.choose_mp_linear_kernel)

Choose an MPLinearKernel that can implement the given config for the given compute capability. Attempts to choose the best kernel in terms of performance.

Parameters:

-

(`config`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.choose_mp_linear_kernel(config))`MPLinearLayerConfig`

) –Description of the linear layer to be implemented.

-

(`compute_capability`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.choose_mp_linear_kernel(compute_capability))`Optional[`

, default:[int](https://docs.python.org/3/builtins/functions.html#int)]`None`

) –The compute capability of the target device, if None uses

`current_platform`

to get the compute capability. Defaults to None.

Raises:

-

–[ValueError](https://docs.python.org/3/builtins/exceptions.html#ValueError)If no kernel can implement the given config.


Returns:

-

–[type](https://docs.python.org/3/builtins/functions.html#type)[[MPLinearKernel](https://docs.vllm.ai/mixed_precision/MPLinearKernel/#vllm.model_executor.kernels.linear.mixed_precision.MPLinearKernel)]type[MPLinearKernel]: Chosen kernel.


## Source code in `vllm/model_executor/kernels/linear/__init__.py`


##

`choose_scaled_mm_linear_kernel(config, possible_kernels, compute_capability=None, force_kernel=None, *, quantization)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.choose_scaled_mm_linear_kernel)

Choose a _KernelT that can implement the given config for the given compute capability. Attempts to choose the best kernel in terms of performance.

Parameters:

-

(`config`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.choose_scaled_mm_linear_kernel(config))`_KernelConfigT`

) –Description of the linear layer to be implemented.

-

(`possible_kernels`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.choose_scaled_mm_linear_kernel(possible_kernels))

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[PlatformEnum](https://docs.vllm.ai/platforms/#vllm.platforms.PlatformEnum),[list](https://docs.python.org/3/builtins/stdtypes.html#list)[_KernelT]]A dictionary of platforms and their list of possible kernels.

-

(`compute_capability`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.choose_scaled_mm_linear_kernel(compute_capability))`Optional[`

, default:[int](https://docs.python.org/3/builtins/functions.html#int)]`None`

) –The compute capability of the target device, if None uses

`current_platform`

to get the compute capability. Defaults to None. -

(`force_kernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.choose_scaled_mm_linear_kernel(force_kernel))`Optional[`

, default:[type](https://docs.python.org/3/builtins/functions.html#type)[_KernelT]]`None`

) –An Optional forced kernel to override the possible_kernels if it can be implemented. If None, it will only try the possible kernels.

-

(`quantization`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.choose_scaled_mm_linear_kernel(quantization))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Quantization scheme used to select a backend override.


Raises:

-

–[ValueError](https://docs.python.org/3/builtins/exceptions.html#ValueError)If no kernel can implement the given config.


Returns:

-
(`_KernelT`


) –[type](https://docs.python.org/3/builtins/functions.html#type)[_KernelT]Chosen kernel.


## Source code in `vllm/model_executor/kernels/linear/__init__.py`


##

`init_mxfp4_linear_kernel(activation_quant_key=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.init_mxfp4_linear_kernel)

Select and instantiate the best MXFP4 linear kernel for the current platform.

## Source code in `vllm/model_executor/kernels/linear/__init__.py`


##

`init_mxfp6_linear_kernel(weight_quant_key, activation_quant_key=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.init_mxfp6_linear_kernel)

Select and instantiate the best MXFP6 linear kernel for the current platform.

## Source code in `vllm/model_executor/kernels/linear/__init__.py`


##

`init_mxfp8_linear_kernel(*, bmm_batch_size=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.init_mxfp8_linear_kernel)

Select and instantiate the best MXFP8 linear kernel for the current platform.

## Source code in `vllm/model_executor/kernels/linear/__init__.py`


##

`init_nvfp4_linear_kernel(use_a16=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.init_nvfp4_linear_kernel)

Select and instantiate the best NVFP4 linear kernel for the current platform.

## Source code in `vllm/model_executor/kernels/linear/__init__.py`


|
|

##

`register_linear_kernel(kernel_class, platform, kernel_type='mp')`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.register_linear_kernel)

Register a new linear kernel class to be considered in kernel selection.

Parameters:

-

(`kernel_class`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.register_linear_kernel(kernel_class))

) –[type](https://docs.python.org/3/builtins/functions.html#type)The kernel class to register.

-

(`platform`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.register_linear_kernel(platform))

) –[PlatformEnum](https://docs.vllm.ai/platforms/#vllm.platforms.PlatformEnum)The platform for which this kernel is applicable.

-

(`kernel_type`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.register_linear_kernel(kernel_type))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'mp'`

) –The type of the kernel, either "mp", "int8", or "fp8". Defaults to "mp".


Raises:

-

–[ValueError](https://docs.python.org/3/builtins/exceptions.html#ValueError)If the kernel_type is not recognized.