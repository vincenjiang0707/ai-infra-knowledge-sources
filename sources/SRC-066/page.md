# CUTLASS

source: https://github.com/NVIDIA/cutlass/releases

# Releases: NVIDIA/cutlass

## Release list

## CUTLASS 4.8.0

### CuTe DSL

-
New features

-
Initial Rubin support to accelerate dense GEMMs. The following features are available:

- CuTe DSL and CuTe extensions
- Support for higher-throughput FP8 (MMA_K=64) and FP4 (MMA_K=128) Tensor Core MMA instructions
- B collector reuse
- Extended TMEM size from 512 COL to 576 COL
- Larger shared memory allocations (328KB)
- Enhanced mixed precision throughput (FP8/FP4)
- Softmax acceleration related features

- Primitives
- Support for higher-throughput FP8 (MMA_K=64) and FP4 (MMA_K=128) Tensor Core MMA instructions
- B collector reuse
- Extended TMEM size from 512 COL to 576 COL
- Larger shared memory allocations (328KB)
- Enhanced mixed precision throughput (FP8/FP4)
- Softmax acceleration related feature
- 2:4 sparsity support for FP4


- CuTe DSL and CuTe extensions
-
CuTe DSL extensions has several new features:

- CTA-V maps are now inferred automatically for
`cute_ext`

TMA load, store, multicast, and reduce-store operations. Explicit CTA-V maps remain supported as overrides. - Added asynchronous atomic TMA reduce-store and sparse MMA operations.
- Added reusable
`cute_ext`

GEMM mainloop and TMA epilogue helpers. - Added opt-in TMEM accumulator-buffer planning, including overlapping ping-pong storage for capacity-constrained kernels.
- Improved device-side TMA descriptor updates and grouped GEMM performance through SMEM-staged updates, workspace reuse, and reduced prologue and synchronization overhead.

- CTA-V maps are now inferred automatically for
-
This release includes an opt-in preview of the CuTe DSL extensions (

`cute_ext`

) compiler pipeline for ordinary Cute DSL kernels. This pipeline lets user mix`cute_ext`

APIs directly into`@cute.jit`

and`@cute.kernel`

code and is required for kernels that mix the two API surfaces. You may test this feature with the following:

`CUTE_DSL_USE_EXTENSION_COMPILER=1 python your_program.py`


The pipeline is expected to preserve program behavior and performance, but generated PTX/SASS may differ. Note that this pipeline will become the default in the future, no earlier than 4.10. -
Added examples for better control over Primitives' compiler warnings/errors introduced in 4.7.0. See the

`CuTeDSL/experimental/compiler_diagnostic/`

directory. -
IKET Profiler Tool

- Rubin kernels (sm107) can now be profiled.
- It is now possible to only dump timing data for a specific cluster to reduce profiling overhead. Previously all clusters were profiled.
- Task Scheduling can instrument the schedule with IKET ranges when constructing TaskManager objects (
`iket_enable_profiling=True`

). Task execution will generate an IKET range and individual pipeline stages in a schedule may generate separate ranges (`iket_profiling_stages`

).

-
A number of new examples were added in this release:

- Rubin (CuTe):
- Dense GEMM for legacy data type with B collector reuse as applicable
- Grouped GEMM with B collector reuse
- Dense blockscaled GEMM with FP4/FP6/FP8 mixed precision and UE5M3 / block-32 scale-factor support
- Grouped blockscaled GEMM with B collector reuse as applicable
- Blockwise GEMM

- Rubin (CuTe extension):
- Support for higher-throughput FP8 (MMA_K=64) and FP4 (MMA_K=128) blockscaled GEMM with UE5M3 scale-factor
- Grouped GEMM with B collector reuse

- Blackwell (CuTe extension):
- Dense GEMMs
- Back-to-back GEMM
- Blockscaled GEMM
- Persistent GEMM with alpha/beta scaling
- CLC scheduler/dynamic persistent GEMM
- GLU GEMM
- Mixed input GEMM
- Planar complex GEMM
- Input transform GEMM
- GeForce pingpong dense GEMM
- Blackwell Ultra blockscaled GEMM

- Dense Convolutions
- Implicit-Gemm Fprop Conv
- Blocksclaed Implicit-Gemm Fprop Conv
- GeForce Implicit-Gemm Fprop Conv
- GeForce Blockscaled Implicit-Gemm Fporp Conv

- Attention
- GQA Decode

- Grouped GEMM
- Unscaled and blockscaled grouped GEMM

- Top-K

- Dense GEMMs
- Ampere (CuTe extension):
- SIMT GEMM


- Rubin (CuTe):
-
CuTe DSL now supports x86_64 Windows

-
CuTe DSL AoT now supports new host target: QNX8.0

-
Notebooks are restructured under examples/python/CuTeDSL/cute/notebooks and new notebooks for primitives will be added under examples/python/CuTeDSL/notebooks

-
Numpy is now not a default dependency


-
-
Bug fixes and improvements:

`nvidia-cuda-nvdisasm`

is now an optional dependency of`nvidia-cutlass-dsl`

via the optional`[sass]`

extra. SASS dumping (`CUTE_DSL_KEEP=sass`

/ KeepSASS) now resolves`nvdisasm`

from the bundled wheel (recommended since its version matches the DSL toolchain) or from a local CUDA Toolkit (`CUDA_HOME`

/`CUDA_PATH`

). A locally-provided`nvdisasm`

must come from a CUDA Toolkit at least as new as the toolchain that produced the CUBIN. Installations that never dump SASS are unaffected.- Reduced the protobuf version requirement of IKET profiler from 6.30 to 4.21. This should make protobuf an easier requirement to satisfy in preparation for transioning IKET to an optional extra.
- Improved JAX PyTree input/output aliasing for
`cutlass.jax.cutlass_call`

- Fixed a regression from 4.6.0 where
`cute.autovec_copy`

emitted per-element instead of

vectorized instructions for tensors with a dynamic stride ([!3463](https://github.com/NVIDIA/cutlass/issues/3463)) - Fixed TVM-FFI env stream detection for GPU tensors in tuple

([!3444](https://github.com/NVIDIA/cutlass/issues/3444)) - Fixed GPU
`link-libraries`

compile-option order so it is stable across processes

([!3564](https://github.com/NVIDIA/cutlass/issues/3564)) - Fixed preprocessor
`IndexError`

on staged`bool()`

with no arguments

([!3506](https://github.com/NVIDIA/cutlass/issues/3506)) - Rejected
`cute.compile`

on`@cute.kernel`

with a user error instead of an ICE

([!3429](https://github.com/NVIDIA/cutlass/issues/3429)) - Fixed CuTe DSL crashing the Python interpreter when used in a REPL

([!3413](https://github.com/NVIDIA/cutlass/issues/3413)) - Fixed a cuDNN Frontend FROST SDPA backward compilation failure issue (
[!3594](https://github.com/NVIDIA/cutlass/issues/3594)) - Fixed SIGABRTs in TVM-FFI launch for cuDNN Frontend SM100 ragged SDPA kernel (
[!3595](https://github.com/NVIDIA/cutlass/issues/3595))


This release has been tested against the following packages:

- FlashAttention:
[main (8d3a3b8)](https://github.com/Dao-AILab/flash-attention/commit/8d3a3b80d4758ebde5a867c50d24d4351443cf2b) - Quack:
[main (35266c3)](https://github.com/Dao-AILab/quack/commit/35266c3298f0e9bf6d5f46c30aace2eaeae517e3) - FlashInfer:
[main (5d0c89e)](https://github.com/flashinfer-ai/flashinfer/commit/5d0c89eacae6ca08f2a1ce92eba557bbad7a1bfc) - cuDNN-Frontend:
[deveop (e0317d1)](https://github.com/NVIDIA/cudnn-frontend/commit/e0317d1f6cbc1bb8e50abce5870b6bf59b9d4a74) - Pytorch:
[main (7d5f021)](https://github.com/pytorch/pytorch/commit/7d5f0216450b8253e62d88284d49de725d88bd42) - TensorRT-LLM:
[main (c295dd9)](https://github.com/NVIDIA/TensorRT-LLM/commit/c295dd9fca143a3fdd2769617699fdd4d4a93eb5)

### CUTLASS Operator API

-
Dense and blockscaled GEMMs in Operator API have preliminary Rubin support. These are provided as a preview and may need additional performance tuning.

-
Updated GEMMs include:

- Dense GEMMs: FP8xFP8
- Blockscaled GEMM: {MXFP8}x{MXFP4, MXFP8} and {MXFP4, NVFP4}x{MXFP4, NVFP4} (including support for the new UE5M3 scale factor dtype for NVFP4).

-
These kernels utilize the below new features in Rubin:

- Higher SMEM (328KB) and TMEM capacity (288KB)
- B-buffer reuse
- Enhanced mixed precision throughput


-
-
Operators can now be ranked by their estimated performance when nvMatmulHeuristics is available. See tutorial here. NOTE: This currently only supports Blackwell kernels as nvMatmulHeuristics does not yet support Rubin.

-
Standalone kernel implementations are now exposed through

`cutlass.kernels`

. These kernels can be used directly, in addition to being discoverable and usable via the Operator interface in`cutlass.operators`

. -
Custom Epilogue fusions now support per-row or per-column reductions.

-
`IndexPtrGroupedGemmArguments`

is now used to represent Grouped GEMM with contiguous-offset/index-pointers. Existing`GroupedGemmArguments`

is deprecated and will be removed in a future release.

### C++

- Added initial Rubin support (SM107) with CuTe C++ building blocks:

[Rubin Tensor Core MMA instructions](https://github.com/NVIDIA/cutlass/blob/main/include/cute/arch/mma_sm107_umma.hpp)and corresponding[CuTe MMA traits](https://github.com/NVIDIA/cutlass/blob/main/include/cute/atom/mma_traits_sm107.hpp).

- CuTe examples that demonstrate the use of Rubin SM107 Tensor Core instructions:

[Dense FP8 GEMM](https://github.com/NVIDIA/cutlass/blob/main/examples/cute/rubin/rubin_fp8.cu).[Block-scaled FP8 GEMM](https://github.com/NVIDIA/cutlass/blob/main/examples/cute/rubin/rubin_fp8_blockscaled.cu).[Mixed-precision block-scaled FP8/FP4 GEMM](https://github.com/NVIDIA/cutlass/blob/main/examples/cute/rubin/rubin_fp8_blockscaled.cu).[Block-scaled FP4 GEMM](https://github.com/NVIDIA/cutlass/blob/main/examples/cute/rubin/rubin_fp4_blockscaled.cu).

- Adjusted shared-memory and tensor-memory capacity handling for Rubin SM107:

- Set the
[SM107 shared-memory capacity](https://github.com/NVIDIA/cutlass/blob/main/include/cutlass/arch/arch.h)to 327 KiB and added launch support for oversized shared-memory configurations. - Set the
[SM107 TMEM capacity](https://github.com/NVIDIA/cutlass/blob/main/include/cute/arch/tmem_capacity_sm100.hpp)to 576 columns per SM, updated the [CuTe 1SM and 2SM TMEM allocators]([https://github.com/NVIDIA/cutlass/blob/main/include/cute/arch/tmem_alloc](https://github.com/NVIDIA/cutlass/blob/main/include/cute/arch/tmem_alloc)...

[Read more](https://github.com/NVIDIA/cutlass/releases/tag/v4.8.0)

## CUTLASS 4.8.0 dev

### CuTe DSL

- New features
-
Initial Rubin support to accelerate dense GEMMs. The following features are available:

- CuTe DSL
- Rubin new FP8 and FP4 Tensor Core support
- B collector reuse
- Extended TMEM size from 512 COL to 576 COL
- Larger shared memory allocations (328KB)
- Enhanced mixed precision throughput (FP8/FP4)

- Primitives
- Rubin new FP8 and FP4 Tensor Core support
- Extended TMEM size from 512 COL to 576 COL


NOTE: Executing Rubin kernels (SM107) requires the R615 driver which will be released


with CUDA Toolkit 13.4 GA. R610 from CUDA Toolkit 13.4 Developer Preview is not

sufficient. - CuTe DSL
-
CuTe DSL extensions has several new features:

- CTA-V maps are now inferred automatically for
`cute_ext`

TMA load, store, multicast, and reduce-store operations. Explicit CTA-V maps remain supported as overrides. - Added asynchronous atomic TMA reduce-store and sparse MMA operations.
- Added reusable
`cute_ext`

GEMM mainloop and TMA epilogue helpers. - Added opt-in TMEM accumulator-buffer planning, including overlapping ping-pong storage for capacity-constrained kernels.
- Improved device-side TMA descriptor updates and grouped GEMM performance through SMEM-staged updates, workspace reuse, and reduced prologue and synchronization overhead.

- CTA-V maps are now inferred automatically for
-
This release includes an opt-in preview of the CuTe DSL extensions (

`cute_ext`

) compiler pipeline for ordinary Cute DSL kernels. This pipeline lets user mix`cute_ext`

APIs directly into`@cute.jit`

and`@cute.kernel`

code and is required for kernels that mix the two API surfaces. You may test this feature with the following:

`CUTE_DSL_USE_EXTENSION_COMPILER=1 python your_program.py`


The pipeline is expected to preserve program behavior, but generated PTX/SASS may differ. The pipeline is planned to become the default in a future release. -
Added examples for better control over Primitives' compiler warnings/errors introduced in 4.7.0. See the

`CuTeDSL/experimental/compiler_diagnostic/`

directory. -
IKET Profiler Tool

- Rubin kernels (sm107) can now be profiled.
- It is now possible to only dump timing data for a specific cluster to reduce profiling overhead. Previously all clusters were profiled.
- Task Scheduling can instrument the schedule with IKET ranges when constructing TaskManager objects (
`iket_enable_profiling=True`

). Task execution will generate an IKET range and individual pipeline stages in a schedule may generate separate ranges (`iket_profiling_stages`

).

-
A number of new examples were added in this release:

- Rubin (CuTe):
- Dense GEMM for legacy data type with B collector reuse as applicable
- Grouped GEMM with B collector reuse
- Dense blockscaled GEMM with FP4/FP6/FP8 mixed precision and UE5M3 / block-32 scale-factor support
- Grouped blockscaled GEMM with B collector reuse as applicable
- Blockwise GEMM

- Rubin (CuTe extension):
- FP4 blockscaled GEMM
- Grouped GEMM with B collector reuse

- Blackwell (CuTe extension):
- Dense GEMMs
- Back-to-back GEMM
- Blockscaled GEMM
- Persistent GEMM with alpha/beta scaling
- CLC scheduler/dynamic persistent GEMM
- GLU GEMM
- Mixed input GEMM
- Planar complex GEMM
- Input transform GEMM
- GeForce pingpong dense GEMM
- Blackwell Ultra blockscaled GEMM

- Attention
- GQA Decode

- Grouped GEMM
- Unscaled and blockscaled grouped GEMM

- Top-K

- Dense GEMMs
- Ampere (CuTe extension):
- SIMT GEMM


- Rubin (CuTe):

-
- Bug fixes and improvements:
`nvidia-cuda-nvdisasm`

is now an optional dependency of`nvidia-cutlass-dsl`

via the optional`[sass]`

extra. SASS dumping (`CUTE_DSL_KEEP=sass`

/ KeepSASS) now resolves`nvdisasm`

from the bundled wheel (recommended since its version matches the DSL toolchain) or from a local CUDA Toolkit (`CUDA_HOME`

/`CUDA_PATH`

). A locally-provided`nvdisasm`

must come from a CUDA Toolkit at least as new as the toolchain that produced the CUBIN. Installations that never dump SASS are unaffected.- Reduced the protobuf version requirement of IKET profiler from 6.30 to 4.21. This should make protobuf an easier requirement to satisfy in preparation for transioning IKET to an optional extra.
- Improved JAX PyTree input/output aliasing for
`cutlass.jax.cutlass_call`

- Fixed a regression from 4.6.0 where
`cute.autovec_copy`

emitted per-element instead of

vectorized instructions for tensors with a dynamic stride ([!3463](https://github.com/NVIDIA/cutlass/issues/3463)) - Fixed TVM-FFI env stream detection for GPU tensors in tuple

([!3444](https://github.com/NVIDIA/cutlass/issues/3444))


This release has been tested against the following packages:

- FlashAttention:
[main (0251105)](https://github.com/Dao-AILab/flash-attention/commit/0251105a2fb19d2957484b7f023cd8c115286ced) - Quack:
[main (60d8808)](https://github.com/Dao-AILab/quack/commit/60d88082272a256fa9b3b2ab631c82cfa78337c6) - FlashInfer:
[main (109d44f)](https://github.com/flashinfer-ai/flashinfer/commit/109d44fceea027290d54efcfe927f8a5665b59de) - cuDNN-Frontend:
[deveop (25b3d51)](https://github.com/NVIDIA/cudnn-frontend/commit/25b3d5126b6544afc209e3c2e94a74f5d82db201) - Pytorch:
[main (cf30153)](https://github.com/pytorch/pytorch/commit/cf30153c4c131c8164ee7798e5022d810682e2cb) - TensorRT-LLM:
[main (1cef02e)](https://github.com/NVIDIA/TensorRT-LLM/commit/1cef02e901be43081b1ba6d4981e94ed3bd9c1e8)

### CUTLASS Operator API

- Operator API features and functionality:
-
Dense and blockscaled GEMMs in Operator API have preliminary Rubin support. These are provided as a preview and may need additional performance tuning.

Updated GEMMs include:

- Dense GEMMs: FP8xFP8
- Blockscaled GEMM: {MXFP8}x{MXFP4, MXFP8} and {MXFP4, NVFP4}x{MXFP4, NVFP4} (including support for the new UE5M3 scale factor dtype for NVFP4).

These kernels utilize the below new features in Rubin:


- Higher SMEM (328KB) and TMEM capacity (288KB)

- B-buffer reuse

- Enhanced mixed precision throughput -
Operators can now be ranked by their estimated performance when nvMatmulHeuristics is available. See tutorial

[here](https://docs.nvidia.com/cutlass/latest/media/docs/operators/tutorials/007_heuristics.ipynb)NOTE: This currently only supports Blackwell kernels as nvMatmulHeuristics does not yet support Rubin.

-
Standalone kernel implementations are now exposed through

`cutlass.kernels`

, in addition to those exposed through the Operator interface in`cutlass.operators`

. This allows kernels to be called directly without looking them up first. -
Custom Epilogue fusions now support partial (per-row or per-column) reductions.

-
`IndexPtrGroupedGemmArguments`

is now used to represent Grouped GEMM with contiguous-offset/index-pointers. Existing`GroupedGemmArguments`

is deprecated and will be removed in a future release.

-

### C++

- Added initial Rubin support (SM107) with CuTe C++ building blocks:
[Rubin Tensor Core MMA instructions](https://github.com/NVIDIA/cutlass/blob/main/include/cute/arch/mma_sm107_umma.hpp)and corresponding[CuTe MMA traits](https://github.com/NVIDIA/cutlass/blob/main/include/cute/atom/mma_traits_sm107.hpp).

- CuTe examples that demonstrate the use of Rubin SM107 Tensor Core instructions:
- Adjusted shared-memory and tensor-memory capacity handling for Rubin SM107:
- Set the
[SM107 shared-memory capacity](https://github.com/NVIDIA/cutlass/blob/main/include/cutlass/arch/arch.h)to 327 KiB and added launch support for oversized shared-memory configurations. - Set the
[SM107 TMEM capacity](https://github.com/NVIDIA/cutlass/blob/main/include/cute/arch/tmem_capacity_sm100.hpp)to 576 columns per SM, updated the[CuTe 1SM and 2SM TMEM allocators](https://github.com/NVIDIA/cutlass/blob/main/include/cute/arch/tmem_allocator_sm100.hpp)for Rubin's exclusive allocation path.

- Set the
- Enabled the existing SM100-compatible
[GEMM](https://github.com/NVIDIA/cutlass/tree/main/include/cutlass/gemm/collective/builders)and[convolution](https://github.com/NVIDIA/cutlass/blob/main/include/cutlass/conv/collective/builders/sm100_umma_builder.inl)for the new SM107:`sm_107a`

and`sm_107f`

targets- Set of unit tests for Rubin SM107
[SIMT GEMM](https://github.com/NVIDIA/cutlass/blob/main/test/unit/gemm/device/sm107_gemm_f32_f32_f32_simt_align1_multi_cluster_shape.cu),[dense FP8 GEMM](https://github.com/NVIDIA/cutlass/blob/main/test/unit/gemm/device/sm107_gemm_f8_f8_f8_tensor_op_f32_alignx.cu),[block-scaled FP8 GEMM](https://github.com/NVIDIA/cutlass/blob/main/test/unit/gemm/device/sm107_gemm_f8_f8_f8_tensor_op_f32_blockwise.cu),[block-scaled FP4 GEMM](https://github.com/NVIDIA/cutlass/blob/main/test/unit/gemm/device/sm107_gemm_f4_f4_f32_tensor_op_f32_2sm_256x192.cu), and[mixed-precision, complex, and 9xBF16 GEMM](https://github.com/NVIDIA/cutlass/blob/main/test/unit/gemm/device/sm107_gemm_umma.cu).

- Set of unit tests for Rubin SM107
- Various improvements and fixes from the community and CUTLASS team. Thanks to everyone who submitted PRs!
- Optimal code generation with CUDA toolkit versions 13.4.

NOTE: Executing Rubin kernels (SM107) requires the R615 driver which will be released

with CUDA Toolkit 13.4...

[Read more](https://github.com/NVIDIA/cutlass/releases/tag/v4.8.0dev)

## CUTLASS 4.7.1

### CuTe DSL

- Bug fixing and improvements
- Fixed a failed kernel compilation issue when setmaxnreg is used together with specific warp-specialized patterns

([!3420](https://github.com/NVIDIA/cutlass/issues/3420)) - Fixed a leak with jit/kernel decorator (
[!3421](https://github.com/NVIDIA/cutlass/issues/3421)) - Fixed bugs in cutlass.jax.cutlass_call with tensor aliasing and handling of optional tensors
- Fixed unexpected compile cache-misses with cutlass.jax.cutlass_call
- Reduced the protobuf version requirement of IKET profiler from 6.30 to 4.21
- Fixed import time write to CUTE_DSL_LIBS (
[!3462](https://github.com/NVIDIA/cutlass/issues/3462)) - Fixed export_to_c outputs i32 dynamic shapes in headers for i64 inputs (
[!3447](https://github.com/NVIDIA/cutlass/issues/3447)) - Improved performance of constructing
`cutlass.Numeric`

from Python value ([!3443](https://github.com/NVIDIA/cutlass/issues/3443)) - Fixed TVM-FFI env stream detection for GPU tensors in tuple

([!3444](https://github.com/NVIDIA/cutlass/issues/3444)) - Fixed TVM-FFI error when passed a tensor with non-zero byte offset

([!3450](https://github.com/NVIDIA/cutlass/issues/3450))

- Fixed a failed kernel compilation issue when setmaxnreg is used together with specific warp-specialized patterns

This release has been tested against the following packages:

- FlashAttention:
[main (a369df7)](https://github.com/Dao-AILab/flash-attention/commit/a369df707e1980fb328abcc1733e3457ec10155f) - Quack:
[main (60d8808)](https://github.com/Dao-AILab/quack/commit/60d88082272a256fa9b3b2ab631c82cfa78337c6) - FlashInfer:
[main (145b101)](https://github.com/flashinfer-ai/flashinfer/commit/145b1010051dbfd4bdc41a0ae55d495b08d7a458) - cuDNN-Frontend:
[deveop(66efedf)](https://github.com/NVIDIA/cudnn-frontend/commit/66efedfe806ca2f86c28d123e974204660526ef7)- Pytorch:
[main(cf30153)](https://github.com/pytorch/pytorch/commit/cf30153c4c131c8164ee7798e5022d810682e2cb)

- Pytorch:

## CUTLASS 4.6.3

### CuTe DSL

- Bug fixing and improvements
- Fixed a failed kernel compilation issue when setmaxnreg is used together with specific warp-specialized patterns

([!3382](https://github.com/NVIDIA/cutlass/issues/3420)) - Fixed a leak with jit/kernel decorator (
[!3421](https://github.com/NVIDIA/cutlass/issues/3421)) - Fixed bugs in cutlass.jax.cutlass_call with tensor aliasing and handling of optional tensors
- Reduced the protobuf version requirement of IKET profiler from 6.30 to 4.21
- Fixed import time write to CUTE_DSL_LIBS (
[!3462](https://github.com/NVIDIA/cutlass/issues/3462)) - Fixed export_to_c outputs i32 dynamic shapes in headers for i64 inputs (
[!3447](https://github.com/NVIDIA/cutlass/issues/3447)) - Improved performance of constructing
`cutlass.Numeric`

from Python value ([!3443](https://github.com/NVIDIA/cutlass/issues/3443)) - Fixed TVM-FFI env stream detection for GPU tensors in tuple

([!3444](https://github.com/NVIDIA/cutlass/issues/3444)) - Fixed TVM-FFI error when passed a tensor with non-zero byte offset

([!3450](https://github.com/NVIDIA/cutlass/issues/3450))

- Fixed a failed kernel compilation issue when setmaxnreg is used together with specific warp-specialized patterns

This release has been tested against the following packages:

- FlashAttention:
[main (a369df7)](https://github.com/Dao-AILab/flash-attention/commit/a369df707e1980fb328abcc1733e3457ec10155f) - Quack:
[main (680ef82)](https://github.com/Dao-AILab/quack/commit/680ef8299ab3ff4430e722c6567b0592448e620b) - FlashInfer:
[main (0263dc2)](https://github.com/flashinfer-ai/flashinfer/commit/0263dc2929ccdce84b9989cae4e8ac948bdadf46) - cuDNN-Frontend:
[deveop(ab9efe15)](https://github.com/NVIDIA/cudnn-frontend/commit/ab9efe15e73b13abb63a56bde34fcf6ababdef65) - Pytorch:
[main(cf30153)](https://github.com/pytorch/pytorch/commit/cf30153c4c131c8164ee7798e5022d810682e2cb)

## CUTLASS 4.7.0

### CuTe DSL

- New features:
-
Introduced the Primitives API which provides a lower-level abstraction beneath CuTe enabling Tensor Core programming through SIMT. This provides a stable, thin wrapper over NVVM operations to use where CuTe abstractions reduce development velocity. Primitives are released as experimental and will evolve based on user feedback.

NOTE: Primitives is a transitional API until a CUDA Python-like solution is available.

-
Introduced the Task Scheduling framework. This provides static analysis of execution schedules for warp-specialized kernels. Compilation stops when known concurrency issues are detected. Also provides tools for visualizing resource/task dependencies and analyzing a kernel's schedule.

-
Improved compiler diagnostics. Register spills and use of local memory can now be reported at compile time with source line numbers. Preliminary support for detecting classes of NVVM synchronization and execution hazards at compile-time when using the Primitives API. Better reporting of compiler errors that previously did not include source line numbers.


-

This release has been tested against the following packages:

- FlashAttention:
[main (c75d019)](https://github.com/Dao-AILab/flash-attention/commit/c75d019dea9d910312974417bc28f190dfdda6d9) - Quack:
[main (79517ae)](https://github.com/Dao-AILab/quack/commit/79517ae3063946fc2bb26a41bd45ee550e85cb26) - FlashInfer:
[main (4b964ec)](https://github.com/flashinfer-ai/flashinfer/commit/4b964ec4e147cf06a39e08b08c43188859df2652) - cuDNN-Frontend:
[deveop(5235c2b)](https://github.com/NVIDIA/cudnn-frontend/commit/5235c2bcaa7df095627cf51dcbe53a503d372855) - Pytorch:
[main(cf30153)](https://github.com/pytorch/pytorch/commit/cf30153c4c131c8164ee7798e5022d810682e2cb)

### CUTLASS Operator API

- Custom epilogue fusions enhancements:
- Add support for scalar reductions.
- Add support to specify data movement strategy for each operand being loaded/stored.


### C++

- Add implementation of 2-kernel backward targeting at FP8 in
[FMHA example](https://github.com/NVIDIA/cutlass/tree/main/examples/77_blackwell_fmha/).- Added a backward fused multi-head attention benchmark with multi-precision (FP16/FP8), configurable batch/sequence/head sizes, variable-length and masking options, plus built-in correctness checks and runtime/throughput reporting.
- The 2-kernel backward has approximately 25% improvement compared to 1-kernel implementation at FP8 without mask on Blackwell SM103 chip.

- Support CUDA 12.6 and newer structured bindings headers in NVRTC.
- Add fp32/fp16/bf16/e4m3/e5m2 -> e2m1 (FP4) in NumericArrayConverter.
- Optimize the E2M1 -> FP16 LUT decode helpers
`_e2m1_to_half_x2`

and`_e2m1_to_half_x4`

by merging mask before prmt. - Fix some issues:
- Update streamk heuristic algorithm to optimize some kernels with mix cluster sizes.
- Avoid integer-sequence get ambiguity in CuTe tuple algorithms.
- Fix a TMA creation driver bug: detect if the first 128KiB is mapped in conservatively by checking if the tensor is compact, if so it is valid to flip the bit otherwise zero it.

- Various improvements and fixes from the community and CUTLASS team. Thanks to everyone who submitted PRs!
- Optimal code generation with CUDA toolkit versions 13.3.

## CUTLASS 4.6.2

### CuTe DSL

- Bug fixing and improvements
- Reverted the TMA bulk copy elect_one change from 4.6.0 to reset the behavior to align with 4.5.x releases
- Fixed a vectorized fp32->f8 conversion issue (
[!3382](https://github.com/NVIDIA/cutlass/issues/3382)) - Fixed a CuTe DSL fp8 grouped_gemm_dglu kernel compilation issue (
[!397](https://github.com/NVIDIA/cudnn-frontend/issues/397)) - Fixed opt-level setting issue for ptxas (
[!3389](https://github.com/NVIDIA/cutlass/issues/3389)) - set_name_prefix of kernel now supports full customization on compiled kernel name (
[!3389](https://github.com/NVIDIA/cutlass/issues/3389)) - Fixed issue in (
[!3349](https://github.com/NVIDIA/cutlass/issues/3349)) - Fixed issue in (
[!3351](https://github.com/NVIDIA/cutlass/issues/3351)) - Reduced JIT compile overhead by ~50 ms per cute.compile
- Speed up importing cutlass.cute by 3.8x with Torch installed, 1.25x without.


This release has been tested against the following packages:

- FlashAttention:
[main (00756db)](https://github.com/Dao-AILab/flash-attention/commit/00756db9d921da0846453283ddfbeb7457abd09b) - Quack:
[main (79517ae)](https://github.com/Dao-AILab/quack/commit/79517ae3063946fc2bb26a41bd45ee550e85cb26) - FlashInfer:
[main (766f94b)](https://github.com/flashinfer-ai/flashinfer/commit/766f94b8cdeefc31ffede247683b2389c2667b3b)

## CUTLASS 4.6.1

## CUTLASS 4.6.0

- Release
[documentation](https://docs.nvidia.com/cutlass/latest/media/docs/cpp/gemm_performance_measurement_methodology_guidelines.md)that explains how to accurately profiling GEMM performance.

### CuTe DSL

-
New features

- New fine-grained compilation API: cute.compile_to that gives control over the what stage the compiler outputs. This feature allows customization of the path from compilation to runtime execution. cute.compile_to is considered experimental in 4.6.
- Experimental Feature: Added the IKET (In-Kernel-Event-Tracing) profiler for instrumentation-based intra-kernel activities tracing. This enables fine-grained profiling and makes it easier to understand persistent, warp-specialized kernels' performance. This is a beta feature provided by CUTLASS Python until a NVIDIA DevTools product is released, there is no guarantee that this interface will remain stable!
- Distribute compiler binaries to accompany cute.compile_to allowing users to build customized compile-execute pipelines outside of Python. Both static and shared compiler and executor/runtime libraries will be provided. Compiler binaries will be uploaded to GitHub with each release.
- Supported AoT cross-compilation for aarch64-linux-gnu
- Support for two launch attributes: launch completion events (cudaLaunchAttributeLaunchCompletionEvent), for recording an event once all thread blocks have begun executing, and launch programmatic events (cudaLaunchAttributeProgrammaticEvent), for PDL event-based synchronization
- Supported auto calculating per-kernel shared memory carveout preference, or use new launch option
`preferred_smem_carveout`

to set manually. - Auto-deduced smem size for launching kernels
- Launch config
`smem`

now defaults to`None`

for auto-calculating kernel shared memory usage, which is recommended unless manual control is required. - Warnings will be raised when the manually set shared memory size is insufficient or exceeds the GPU maximum.
- The default shared memory usage calculation aligns with CUDA C++ static shared memory behavior, i.e. summing all allocations additively.
- An additional launch option
`smem_merge_branch_allocs`

is provided to merge shared memory allocations across mutually exclusive code branches, which is recommended for inlined mega-kernels to reduce total footprint.

- Launch config
- SASS dumping in DSL is now supported in a self-contained manner - no CUDA toolkit installation required to get nvdisasm

-
Bug fixing and improvements

- Add the missing elect_one in cute.copy for bulk copy.
- The elect_one required for async bulk copy was missing in cute.copy. It's now generated in cute.copy automatically.
- Nesting elect_one will cause functionality issues. Please remove elect_one around cute.copy with async bulk copy.
- Elect_one around direct async bulk copy instruction should be kept as it bypasses the cute.copy layer and will not be affected by this fix.
- Affected copy atoms are CopyBulkG2SOp, CopyBulkG2SMulticastOp, CopyBulkS2GOp, CopyBulkS2GByteMaskOp, and CopyBulkS2SOp.
- An Example showing changes to avoid nesting
`elect_one`

could be found in this[PR](https://github.com/Dao-AILab/quack/pull/164)

- Improvements on linter support with more type ignores cleaned up
- Improvements on tvm-ffi CUDA runtime error diagnostics
- Improvements on dataclass support for TVM-FFI
- Fixed a regression on compilation time
- Enhancement on compile time checks to reject mis-aligned smem operand for TMA
- Long-deprecated API clean-up, including:
- cute.core.ThrMma, please use cute.ThrMma instead
- cute.core.ThrCopy, please use cute.ThrCopy instead
- cute.make_fragment, please use cute.make_rmem_tensor instead

- Fixed following issues

- Add the missing elect_one in cute.copy for bulk copy.

### CUTLASS Operator API

- CUTLASS Operator API is a new addition to the CUTLASS Python stack, providing easy interfaces

to discover CUTLASS Python DSL kernels & integrate them in your code.`pip install nvidia-cutlass-operators`

to get started

[Operator API Overview](https://docs.nvidia.com/cutlass/latest/media/docs/operators/overview.html)[Basic GEMM tutorial](https://docs.nvidia.com/cutlass/latest/media/docs/operators/tutorials/000_gemm.html)- More tutorials
[here](https://docs.nvidia.com/cutlass/latest/media/docs/operators/tutorials/index.html)

- More tutorials
[GitHub source](https://github.com/NVIDIA/cutlass/tree/main/operators)[API Reference](https://docs.nvidia.com/cutlass/latest/media/docs/operators/api_reference/index.html)

### CUTLASS C++

- Add
[example 113](https://github.com/NVIDIA/cutlass/tree/main/examples/113_hopper_gemm_activation_fusion)for Hopper GEMM with activation fusion.- Supports standard and gated activations (e.g., SiLu) with fp8 and fp16 inputs.
- Covers both regular GEMM and grouped GEMM variants.

- Improve SM90 grouped/ptr-array GEMM with EVT support.
- Adds the EVT (Epilogue Visitor Tree) plumbing required to do activation, bias, and auxiliary-tensor fusion inside SM90 grouped and ptr-array GEMM kernels.

- Add ptr-array TMA collective for tensor/token-scaled FP8 grouped GEMM Blackwell SM120/SM121 kernels.
- Implement
`CollectiveMma`

and`CollectiveBuilder`

specializations for`MainloopSm120ArrayTmaWarpSpecialized`

, enabling ptr-array grouped GEMM (MoE expert dispatch) with tensor- and token-level FP8 scaling. - Corresponding
[unit test](https://github.com/NVIDIA/cutlass/tree/main/test/unit/gemm/device/sm120_tensorop_gemm/sm120_gemm_f8_f8_f32_tensor_op_group_gemm.cu)

- Implement
- Add tileN = 8,16 for Blackwell SM120 blockscale GEMM kernels.
- Fix
`DescriptorIterator::operator+`

in`mma_traits_sm100.hpp`

to use 32-bit arithmetic on CUDA toolkit version <= 13.3, preserving the high half of the smem descriptor. - Fix a CUDA structured bindings header issue.
- Various improvements and fixes from the community and CUTLASS team. Thanks to everyone who submitted PRs!
- Optimal code generation with CUDA toolkit versions 13.3.

## CUTLASS 4.5.3

### CuTe DSL

- Bug fixing and improvements
- Fixed a compilation time regression issue in 4.5.0. Compilation times now match those in the 4.4 and 4.6 branches.


## CUTLASS 4.2.2

### CUTLASS C++

- Make
[version.h](https://github.com/NVIDIA/cutlass/blob/release/4.2/include/cutlass/version.h)NVRTC JIT compilation compatible. - Allow linking large cutlass library on 64bit platform.
- Fix alignment-related miscalculation for pipeline stages of Blackwell blockscaled GEMM.
- Fix for blockwise group gemm nosmem epilogues and no sfd with nosmem group gemm epilogues.