# [Issue #252] Tensor Pipe metrics are inconsistent and have holes

source: https://github.com/NVIDIA/DCGM/issues/252
state: open | updated: 2025-09-17T07:52:42Z
labels: 

## 正文

### Is this a new feature, an improvement, or a change to existing functionality?

New Feature

### Please provide a clear description of the problem this feature solves

We have:

- `DCGM_FI_PROF_PIPE_TENSOR_DFMA_ACTIVE` (f64 - Fused Multiply Add)
- `DCGM_FI_PROF_PIPE_TENSOR_HMMA_ACTIVE` (f16 - Matrix Multiply Accumulate)
- `DCGM_FI_PROF_PIPE_TENSOR_IMMA_ACTIVE` (i8 - Matrix Multiply Accumulate)

Why is the f64 one FMA, and the f16 and f8 ones are MMA?

Why is there no f32 one (neither FMA nor MMA)?

Why is there no f8 one?

### Feature Description

Fix all the gaps:

- `DCGM_FI_PROF_PIPE_TENSOR_DFMA_ACTIVE` (f64 - Fused Multiply Add)
- `DCGM_FI_PROF_PIPE_TENSOR_DMMA_ACTIVE` (f64 - Matrix Multiply Accumulate)
- `DCGM_FI_PROF_PIPE_TENSOR_FFMA_ACTIVE` (f32 - Fused Multiply Add)
- `DCGM_FI_PROF_PIPE_TENSOR_FMMA_ACTIVE` (f32 - Matrix Multiply Accumulate)
- `DCGM_FI_PROF_PIPE_TENSOR_HFMA_ACTIVE` (f16 - Fused Multiply Add)
- `DCGM_FI_PROF_PIPE_TENSOR_HMMA_ACTIVE` (f16 - Matrix Multiply Accumulate)
- `DCGM_FI_PROF_PIPE_TENSOR_QMMA_ACTIVE` (f8 - Matrix Multiply Accumulate)
- `DCGM_FI_PROF_PIPE_TENSOR_IMMA_ACTIVE` (i8 - Matrix Multiply Accumulate)

### Additional context

_No response_

## 评论 (1)

### LWisteria · 2025-09-17

>  DCGM_FI_PROF_PIPE_TENSOR_DFMA_ACTIVE (f64 - Fused Multiply Add)
>  DCGM_FI_PROF_PIPE_TENSOR_HMMA_ACTIVE (f16 - Matrix Multiply Accumulate)
>  DCGM_FI_PROF_PIPE_TENSOR_IMMA_ACTIVE (i8 - Matrix Multiply Accumulate)

I believe there might be a misunderstanding in the premise here.

The "H" in HMMA doesn't strictly stand for "Half" (f16). Instead, it appears to be a broader category for Tensor Core MMA (Matrix Multiply-Accumulate) operations that are not double-precision (DMMA) or integer (IMMA).

While I don't have a link to a definitive official document that states this, it's supported by evidence from other NVIDIA tools and libraries:

* SASS Instructions: At the GPU assembly level, you can find instructions like HMMA.1688.F32, which indicates an HMMA operation being performed on F32 data.
* cuBLAS Documentation: https://docs.nvidia.com/cuda/cublas/#cublasltnumericalimplflags-t categorizes the numerical implementation flags as follows, grouping multiple precisions under HMMA:
    * `CUBLASLT_NUMERICAL_IMPL_FLAGS_HMMA`: Specify that the implementation is based on HMMA (tensor operation) family instructions.
    * `CUBLASLT_NUMERICAL_IMPL_FLAGS_IMMA`: Specify that the implementation is based on IMMA (integer tensor operation) family instructions.
    * `CUBLASLT_NUMERICAL_IMPL_FLAGS_DMMA`: Specify that the implementation is based on DMMA (double precision tensor operation) family instructions.

Given this, the underlying hardware counters that NVML (and therefore DCGM) queries likely do not differentiate between f32, f16, and f8 MMA operations. They are all aggregated into the single HMMA metric.

Therefore, it may not be possible to implement separate counters for f32, f16, and f8 as requested, because the hardware itself doesn't seem to expose that level of granularity.
