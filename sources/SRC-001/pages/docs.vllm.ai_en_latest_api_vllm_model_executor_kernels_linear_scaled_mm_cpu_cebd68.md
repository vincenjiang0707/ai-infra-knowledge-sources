source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/scaled_mm/cpu/
lastmod: 2026-09-23

#

`vllm.model_executor.kernels.linear.scaled_mm.cpu`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.cpu)

Classes:

-
–[CPUFP8W8A8ScaledMMLinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.cpu.CPUFP8W8A8ScaledMMLinearKernel)FP8 W8A8 GEMM with dynamic per-token activation quantization on CPU.

-
–[CPUFp8BlockScaledMMKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.cpu.CPUFp8BlockScaledMMKernel)FP8 W8A16 block-quantized GEMM via AMX BRGEMM on CPU.

-
–[CPUFp8PerTensorScaledMMLinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.cpu.CPUFp8PerTensorScaledMMLinearKernel)FP8 W8A16 per-tensor-scaled GEMM via AMX BRGEMM on CPU.

-
–[CPUFp8W8A8BlockScaledMMKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.cpu.CPUFp8W8A8BlockScaledMMKernel)FP8 W8A8 block-quantized GEMM with dynamic per-token activation quant on CPU.


##

`CPUFP8W8A8ScaledMMLinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.cpu.CPUFP8W8A8ScaledMMLinearKernel)

Bases: `FP8ScaledMMLinearKernel`


FP8 W8A8 GEMM with dynamic per-token activation quantization on CPU.

Methods:

-
–[process_weights_after_loading](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.cpu.CPUFP8W8A8ScaledMMLinearKernel.process_weights_after_loading)Prepack weights with float8_linear_prepack_cpu (VNNI + block layout).


## Source code in `vllm/model_executor/kernels/linear/scaled_mm/cpu.py`


|
|

###

`process_weights_after_loading(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.cpu.CPUFP8W8A8ScaledMMLinearKernel.process_weights_after_loading)

Prepack weights with float8_linear_prepack_cpu (VNNI + block layout).

## Source code in `vllm/model_executor/kernels/linear/scaled_mm/cpu.py`


##

`CPUFp8BlockScaledMMKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.cpu.CPUFp8BlockScaledMMKernel)

Bases: `Fp8BlockScaledMMLinearKernel`


FP8 W8A16 block-quantized GEMM via AMX BRGEMM on CPU.

## Source code in `vllm/model_executor/kernels/linear/scaled_mm/cpu.py`


|
|

##

`CPUFp8PerTensorScaledMMLinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.cpu.CPUFp8PerTensorScaledMMLinearKernel)

Bases: `FP8ScaledMMLinearKernel`


FP8 W8A16 per-tensor-scaled GEMM via AMX BRGEMM on CPU.

Reuses the block-scaled AMX kernel (fp8_scaled_mm_cpu) with a single synthetic block spanning the whole weight, so activations stay BF16/FP32 — no FP8 activation quantization, unlike PerTensorTorchFP8ScaledMMLinearKernel.

## Source code in `vllm/model_executor/kernels/linear/scaled_mm/cpu.py`


|
|

##

`CPUFp8W8A8BlockScaledMMKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.cpu.CPUFp8W8A8BlockScaledMMKernel)

Bases: `Fp8BlockScaledMMLinearKernel`


FP8 W8A8 block-quantized GEMM with dynamic per-token activation quant on CPU.

Methods:

-
–[process_weights_after_loading](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.cpu.CPUFp8W8A8BlockScaledMMKernel.process_weights_after_loading)Prepack block-quantized FP8 weight for W8A8 AMX BRGEMM.


## Source code in `vllm/model_executor/kernels/linear/scaled_mm/cpu.py`


|
|

###

`process_weights_after_loading(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.cpu.CPUFp8W8A8BlockScaledMMKernel.process_weights_after_loading)

Prepack block-quantized FP8 weight for W8A8 AMX BRGEMM.

For block-quant FP8 models weight is stored as [N, K] (NOT transposed, unlike non-block FP8 where vLLM stores [K, N]).

## float8_linear_prepack_cpu expects

weight: [N, K] scales: [N, G] where G = K / block_k

weight_scale_inv from the checkpoint has shape [ceil(N/block_n), G], so we expand rows from ceil(N/block_n) to N via repeat_interleave.