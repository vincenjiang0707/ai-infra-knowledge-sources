source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/scaled_mm/flashinfer/
lastmod: 2026-09-24

#

`vllm.model_executor.kernels.linear.scaled_mm.flashinfer`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.flashinfer)

Classes:

-
–[FlashInferFp8DeepGEMMDynamicBlockScaledKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.flashinfer.FlashInferFp8DeepGEMMDynamicBlockScaledKernel)Conditional FlashInfer / DeepGEMM FP8 block-scaled GEMM.


##

`FlashInferFp8DeepGEMMDynamicBlockScaledKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.flashinfer.FlashInferFp8DeepGEMMDynamicBlockScaledKernel)

Bases: [Fp8BlockScaledDynamicMMLinearKernel](https://docs.vllm.ai/BlockScaledMMLinearKernel/#vllm.model_executor.kernels.linear.scaled_mm.BlockScaledMMLinearKernel.Fp8BlockScaledDynamicMMLinearKernel)

Conditional FlashInfer / DeepGEMM FP8 block-scaled GEMM.

Dispatches between two kernels based on input batch size: - Small batches (M < 32): FlashInfer's swapAB trick for better utilisation. - Large batches (M >= 32): DeepGEMM for peak throughput.

apply_input_quant is False because FlashInfer accepts BF16 input and handles FP8 conversion internally. The DeepGEMM branch therefore quantises BF16→FP8 inside apply_mm via a closure before dispatching to the DeepGEMM kernel — keeping both branches compatible with the single BF16 tensor operand list passed by torch.cond.

## Source code in `vllm/model_executor/kernels/linear/scaled_mm/flashinfer.py`


##

`_dynamic_flashinfer_deepgemm_blockscale_gemm_fake(input, weight, weight_scale, group_size, use_deep_gemm_e8m0)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.flashinfer._dynamic_flashinfer_deepgemm_blockscale_gemm_fake)

Required fake/meta implementation for torch.compile graph tracing.

## Source code in `vllm/model_executor/kernels/linear/scaled_mm/flashinfer.py`


##

`_dynamic_flashinfer_deepgemm_blockscale_gemm_impl(input, weight, weight_scale, group_size, use_deep_gemm_e8m0)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.flashinfer._dynamic_flashinfer_deepgemm_blockscale_gemm_impl)

Conditional FlashInfer FP8 blockscale GEMM with batch-size-dependent selection.

This function switches between two optimized kernels based on the input batch size: - For small batches (M < 32): Uses FlashInfer's DeepGEMM swapAB optimization. - For larger batches (M >= 32): Uses the official DeepGEMM kernel.

The conditional logic must use torch.cond() instead of a simple if-else statement to maintain compatibility with torch.compile graph compilation.

This batch-size-dependent selection is essential for maintaining model accuracy. Benchmarks on GSM8K show a significant accuracy gap (88% vs 95%) for DeepSeek-V3.1 when using FlashInfer's DeepGEMM on M>=32. The M < 32 strategy fixes the accuracy drop.

Parameters:

-

(`input`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.flashinfer._dynamic_flashinfer_deepgemm_blockscale_gemm_impl(input))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input tensor of shape (batch_size, input_dim) in FP8 format

-

(`weight`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.flashinfer._dynamic_flashinfer_deepgemm_blockscale_gemm_impl(weight))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Weight tensor of shape (output_dim, input_dim) in FP8 format

-

(`weight_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.flashinfer._dynamic_flashinfer_deepgemm_blockscale_gemm_impl(weight_scale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Scale factors for weight quantization (per-group)

-

(`group_size`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.flashinfer._dynamic_flashinfer_deepgemm_blockscale_gemm_impl(group_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Quantization group size for the weight tensor

-

(`use_deep_gemm_e8m0`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.flashinfer._dynamic_flashinfer_deepgemm_blockscale_gemm_impl(use_deep_gemm_e8m0))

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to use the E8M0 format in DeepGEMM quantization


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Output tensor of shape (batch_size, output_dim) in bfloat16 format


## Source code in `vllm/model_executor/kernels/linear/scaled_mm/flashinfer.py`


|
|

##

`_flashinfer_fp8_blockscale_gemm_fake(input, weight, weight_scale)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.flashinfer._flashinfer_fp8_blockscale_gemm_fake)

Required fake/meta implementation for torch.compile graph tracing.