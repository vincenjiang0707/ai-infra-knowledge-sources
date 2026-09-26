source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/mixed_precision/
lastmod: 2026-09-24

#

`vllm.model_executor.kernels.linear.mixed_precision`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision)

Modules:

-
–[humming](https://docs.vllm.ai/humming/#vllm.model_executor.kernels.linear.mixed_precision.humming)Humming GEMM as a mixed-precision WNA16Int linear kernel.

-
–[rdna3_w4a16](https://docs.vllm.ai/rdna3_w4a16/#vllm.model_executor.kernels.linear.mixed_precision.rdna3_w4a16)W4A16 GPTQ kernel for AMD RDNA3 (gfx1100) — fp16 + bf16.

-
–[rdna_hybrid_w4a16](https://docs.vllm.ai/rdna_hybrid_w4a16/#vllm.model_executor.kernels.linear.mixed_precision.rdna_hybrid_w4a16)Hybrid W4A16 kernel: Triton for prefill, HIP skinny for decode.

-
–[triton_w4a16](https://docs.vllm.ai/triton_w4a16/#vllm.model_executor.kernels.linear.mixed_precision.triton_w4a16)Triton-based W4A16 GEMM kernel for ROCm MI300.

-
–[xpu](https://docs.vllm.ai/xpu/#vllm.model_executor.kernels.linear.mixed_precision.xpu) -
–[zentorch](https://docs.vllm.ai/zentorch/#vllm.model_executor.kernels.linear.mixed_precision.zentorch)Zentorch W4A16 GPTQ weight-only-quantized linear kernel for AMD Zen CPUs.


Classes:

-
–[RDNAHybridW4A16LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.RDNAHybridW4A16LinearKernel)Hybrid W4A16 kernel: HIP skinny for decode, Triton for prefill.

-
–[TritonW4A16LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.TritonW4A16LinearKernel)Triton-based W4A16 GEMM kernel for ROCm (MI300 and newer).

-
–[XPUW4A8IntLinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.XPUW4A8IntLinearKernel)XPU kernel for W4A8 integer quantization using oneDNN int4_gemm_w4a8.

-
–[ZentorchWNA16LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.ZentorchWNA16LinearKernel)W4A16 GPTQ kernel backed by

`torch.ops.zentorch.zentorch_woq_linear`

.

##

`RDNAHybridW4A16LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.RDNAHybridW4A16LinearKernel)

Bases: `MPLinearKernel`


Hybrid W4A16 kernel: HIP skinny for decode, Triton for prefill.

Stores the weights once as int8 [N, K//2] (ExLlama shuffle packed). The HIP skinny kernel reads it directly; the triton kernel reinterprets the same buffer as int32 [N, K//8] via a view, so there is no dual weight storage.

## Source code in `vllm/model_executor/kernels/linear/mixed_precision/rdna_hybrid_w4a16.py`


|
|

##

`TritonW4A16LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.TritonW4A16LinearKernel)

Bases: `MPLinearKernel`


Triton-based W4A16 GEMM kernel for ROCm (MI300 and newer).

Supports GPTQ-format int4 weights (uint4b8 symmetric, uint4 asymmetric) with grouped quantization. Weight tensors are transposed from the compressed-tensors checkpoint layout to the kernel's [K, N//8] layout.

Methods:

-
–[process_weights_after_loading](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.TritonW4A16LinearKernel.process_weights_after_loading)Convert compressed-tensors checkpoint layout to kernel layout.


## Source code in `vllm/model_executor/kernels/linear/mixed_precision/triton_w4a16.py`


|
|

###

`process_weights_after_loading(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.TritonW4A16LinearKernel.process_weights_after_loading)

Convert compressed-tensors checkpoint layout to kernel layout.

Checkpoint (from compressed_tensors_wNa16.create_weights): weight_packed: [N, K//8] int32 input_dim=1, output_dim=0, packed_dim=1 weight_scale: [N, K//G] fp16 input_dim=1, output_dim=0 weight_zero_point: [N//8, K//G] int32 output_dim=0, packed_dim=0

## Kernel needs

qweight: [K, N//8] int32 (transpose weight_packed) scales: [K//G, N] fp16 (transpose weight_scale) qzeros: [K//G, N//8] int32 (transpose weight_zero_point)

## Source code in `vllm/model_executor/kernels/linear/mixed_precision/triton_w4a16.py`


|
|

##

`XPUW4A8IntLinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.XPUW4A8IntLinearKernel)

Bases: `MPLinearKernel`


XPU kernel for W4A8 integer quantization using oneDNN int4_gemm_w4a8.

Weights are symmetric group-quantized int4 packed as uint4. Activations are dynamically quantized per-token to symmetric int8.

## Source code in `vllm/model_executor/kernels/linear/mixed_precision/xpu.py`


|
|

##

`ZentorchWNA16LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.ZentorchWNA16LinearKernel)

Bases: `CPUWNA16LinearKernel`


W4A16 GPTQ kernel backed by `torch.ops.zentorch.zentorch_woq_linear`

.

Methods:

-
–[process_weights_after_loading](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.ZentorchWNA16LinearKernel.process_weights_after_loading)Repack CT GPTQ weights into the zentorch WOQ layout.


## Source code in `vllm/model_executor/kernels/linear/mixed_precision/zentorch.py`


|
|

###

`_zentorch_woq_eligible(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.ZentorchWNA16LinearKernel._zentorch_woq_eligible)

Eligibility predicate for the zentorch W4A16 GPTQ fast path.

Constraints (any failure -> `cpu_gemm_wna16`

path via `super()`

with `layer`

untouched).

## Source code in `vllm/model_executor/kernels/linear/mixed_precision/zentorch.py`


###

`process_weights_after_loading(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.ZentorchWNA16LinearKernel.process_weights_after_loading)

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