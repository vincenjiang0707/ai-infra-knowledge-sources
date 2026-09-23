source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/scaled_mm/
lastmod: 2026-09-23

#

`vllm.model_executor.kernels.linear.scaled_mm`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm)

Modules:

-
–[BlockScaledMMLinearKernel](https://docs.vllm.ai/BlockScaledMMLinearKernel/#vllm.model_executor.kernels.linear.scaled_mm.BlockScaledMMLinearKernel) -
–[ScaledMMLinearKernel](https://docs.vllm.ai/ScaledMMLinearKernel/#vllm.model_executor.kernels.linear.scaled_mm.ScaledMMLinearKernel) -
–[aiter](https://docs.vllm.ai/aiter/#vllm.model_executor.kernels.linear.scaled_mm.aiter) -
–[b12x](https://docs.vllm.ai/b12x/#vllm.model_executor.kernels.linear.scaled_mm.b12x) -
–[cpu](https://docs.vllm.ai/cpu/#vllm.model_executor.kernels.linear.scaled_mm.cpu) -
–[cutlass](https://docs.vllm.ai/cutlass/#vllm.model_executor.kernels.linear.scaled_mm.cutlass) -
–[flashinfer](https://docs.vllm.ai/flashinfer/#vllm.model_executor.kernels.linear.scaled_mm.flashinfer) -
–[humming](https://docs.vllm.ai/humming/#vllm.model_executor.kernels.linear.scaled_mm.humming) -
–[marlin](https://docs.vllm.ai/marlin/#vllm.model_executor.kernels.linear.scaled_mm.marlin) -
–[pytorch](https://docs.vllm.ai/pytorch/#vllm.model_executor.kernels.linear.scaled_mm.pytorch) -
–[xpu](https://docs.vllm.ai/xpu/#vllm.model_executor.kernels.linear.scaled_mm.xpu) -
–[zentorch](https://docs.vllm.ai/zentorch/#vllm.model_executor.kernels.linear.scaled_mm.zentorch)Zentorch dynamic-symmetric W8A8 int8 linear kernel for AMD Zen CPUs.


Classes:

-
–[AiterInt8ScaledMMLinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.AiterInt8ScaledMMLinearKernel) -
–[CPUFP8W8A8ScaledMMLinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.CPUFP8W8A8ScaledMMLinearKernel)FP8 W8A8 GEMM with dynamic per-token activation quantization on CPU.

-
–[CPUFp8BlockScaledMMKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.CPUFp8BlockScaledMMKernel)FP8 W8A16 block-quantized GEMM via AMX BRGEMM on CPU.

-
–[CPUFp8PerTensorScaledMMLinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.CPUFp8PerTensorScaledMMLinearKernel)FP8 W8A16 per-tensor-scaled GEMM via AMX BRGEMM on CPU.

-
–[CutlassFP8ScaledMMLinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.CutlassFP8ScaledMMLinearKernel) -
–[MarlinFP8ScaledMMLinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.MarlinFP8ScaledMMLinearKernel)FP8 Marlin kernel for GPUs that lack FP8 hardware support.

-
–[XPUFp8BlockScaledMMKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.XPUFp8BlockScaledMMKernel) -
–[ZentorchInt8ScaledMMLinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.ZentorchInt8ScaledMMLinearKernel)

##

`AiterInt8ScaledMMLinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.AiterInt8ScaledMMLinearKernel)

Bases: `CutlassInt8ScaledMMLinearKernel`


Methods:

-
–[apply_weights](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.AiterInt8ScaledMMLinearKernel.apply_weights)`AiterInt8ScaledMMLinearKernel`

implements a fused version of

## Source code in `vllm/model_executor/kernels/linear/scaled_mm/aiter.py`


|
|

###

`apply_weights(layer, x, bias=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.AiterInt8ScaledMMLinearKernel.apply_weights)

`AiterInt8ScaledMMLinearKernel`

implements a fused version of `output = torch.mm((scale_a * a), (scale_b * b)).to(out_dtype)`

where scale_a * a and scale_b * b are implemented using numpy-style broadcasting. Currently only support per-tensor-per-tensor GEMM and per-token-per-channel GEMM through AITER w8a8 scaled gemm. `AiterInt8ScaledMMLinearKernel`

also does not support ATIER block scaled GEMM and mix-precision GEMM.

## Source code in `vllm/model_executor/kernels/linear/scaled_mm/aiter.py`


##

`CPUFP8W8A8ScaledMMLinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.CPUFP8W8A8ScaledMMLinearKernel)

Bases: `FP8ScaledMMLinearKernel`


FP8 W8A8 GEMM with dynamic per-token activation quantization on CPU.

Methods:

-
–[process_weights_after_loading](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.CPUFP8W8A8ScaledMMLinearKernel.process_weights_after_loading)Prepack weights with float8_linear_prepack_cpu (VNNI + block layout).


## Source code in `vllm/model_executor/kernels/linear/scaled_mm/cpu.py`


|
|

###

`process_weights_after_loading(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.CPUFP8W8A8ScaledMMLinearKernel.process_weights_after_loading)

Prepack weights with float8_linear_prepack_cpu (VNNI + block layout).

## Source code in `vllm/model_executor/kernels/linear/scaled_mm/cpu.py`


##

`CPUFp8BlockScaledMMKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.CPUFp8BlockScaledMMKernel)

Bases: `Fp8BlockScaledMMLinearKernel`


FP8 W8A16 block-quantized GEMM via AMX BRGEMM on CPU.

## Source code in `vllm/model_executor/kernels/linear/scaled_mm/cpu.py`


|
|

##

`CPUFp8PerTensorScaledMMLinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.CPUFp8PerTensorScaledMMLinearKernel)

Bases: `FP8ScaledMMLinearKernel`


FP8 W8A16 per-tensor-scaled GEMM via AMX BRGEMM on CPU.

Reuses the block-scaled AMX kernel (fp8_scaled_mm_cpu) with a single synthetic block spanning the whole weight, so activations stay BF16/FP32 — no FP8 activation quantization, unlike PerTensorTorchFP8ScaledMMLinearKernel.

## Source code in `vllm/model_executor/kernels/linear/scaled_mm/cpu.py`


|
|

##

`CutlassFP8ScaledMMLinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.CutlassFP8ScaledMMLinearKernel)

Bases: `FP8ScaledMMLinearKernel`


Methods:

-
–[input_quant_key](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.CutlassFP8ScaledMMLinearKernel.input_quant_key)Only static per-tensor activation quantization is supported for external


## Source code in `vllm/model_executor/kernels/linear/scaled_mm/cutlass.py`


|
|

###

`_pad_to_alignment(x, dim, alignment, value=0.0)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.CutlassFP8ScaledMMLinearKernel._pad_to_alignment)

Pad tensor `x`

along `dim`

to the next multiple of `alignment`

.

## Source code in `vllm/model_executor/kernels/linear/scaled_mm/cutlass.py`


###

`input_quant_key()`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.CutlassFP8ScaledMMLinearKernel.input_quant_key)

Only static per-tensor activation quantization is supported for external quantization.

## Source code in `vllm/model_executor/kernels/linear/scaled_mm/cutlass.py`


##

`MarlinFP8ScaledMMLinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.MarlinFP8ScaledMMLinearKernel)

Bases: `FP8ScaledMMLinearKernel`


FP8 Marlin kernel for GPUs that lack FP8 hardware support. Leverages the Marlin kernel for fast weight-only FP8 quantization.

## Source code in `vllm/model_executor/kernels/linear/scaled_mm/marlin.py`


##

`XPUFp8BlockScaledMMKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.XPUFp8BlockScaledMMKernel)

Bases: `Fp8BlockScaledMMLinearKernel`


## Source code in `vllm/model_executor/kernels/linear/scaled_mm/xpu.py`


|
|

###

`_prepare_bmm_params(layer, scale_kn)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.XPUFp8BlockScaledMMKernel._prepare_bmm_params)

Precompute batched weight and scale for grouped fp8_bmm (e.g. wo_a).

Splits scale [k_blocks, n_blocks] into [G, k_blocks, n_blocks_per_group] and weight [N_total, K] into [G, K, N_per_group] for batch GEMM.

## Source code in `vllm/model_executor/kernels/linear/scaled_mm/xpu.py`


##

`ZentorchInt8ScaledMMLinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.ZentorchInt8ScaledMMLinearKernel)

Bases: `Int8ScaledMMLinearKernel`


Methods:

-
–[process_weights_after_loading](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.ZentorchInt8ScaledMMLinearKernel.process_weights_after_loading)Prepare weights for

`zentorch_dynamic_qlinear`

.

## Source code in `vllm/model_executor/kernels/linear/scaled_mm/zentorch.py`


###

`process_weights_after_loading(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.ZentorchInt8ScaledMMLinearKernel.process_weights_after_loading)

Prepare weights for `zentorch_dynamic_qlinear`

.

Keeps weight in [N, K] layout (int8, contiguous) and converts the per-channel weight scale to bf16 with shape `(N,)`

.