source: https://docs.nvidia.com/cuda/cusparselt/index.html

# cuSPARSELt: A High-Performance CUDA Library for Sparse Matrix-Matrix Multiplication[#](https://docs.nvidia.com#cusparselt-a-high-performance-cuda-library-for-sparse-matrix-matrix-multiplication)

**NVIDIA cuSPARSELt** is a high-performance CUDA library dedicated to general matrix-matrix operations in which at least one operand is a structured sparse matrix with 50% sparsity ratio:

where refers to in-place operations such as transpose/non-transpose, and are scalars or vectors.

The *cuSPARSELt APIs* allow flexibility in the algorithm/operation selection, epilogue, and matrix characteristics, including memory layout, alignment, and data types.

**Download:** [developer.nvidia.com/cusparselt/downloads](https://developer.nvidia.com/cusparselt/downloads)

**Provide Feedback:** [Math-Libs-Feedback@nvidia.com](mailto:Math-Libs-Feedback%40nvidia.com?subject=cuSPARSELt-Feedback)

**Examples**:
[cuSPARSELt Example 1](https://github.com/NVIDIA/CUDALibrarySamples/tree/main/cuSPARSELt/matmul),
[cuSPARSELt Example 2](https://github.com/NVIDIA/CUDALibrarySamples/tree/main/cuSPARSELt/matmul_advanced)

**Blog post**:

[Exploiting NVIDIA Ampere Structured Sparsity with cuSPARSELt](https://developer.nvidia.com/blog/exploiting-ampere-structured-sparsity-with-cusparselt/)[Structured Sparsity in the NVIDIA Ampere Architecture and Applications in Search Engines](https://developer.nvidia.com/blog/structured-sparsity-in-the-nvidia-ampere-architecture-and-applications-in-search-engines/)[Making the Most of Structured Sparsity in the NVIDIA Ampere Architecture](https://www.nvidia.com/en-us/on-demand/session/gtcspring21-s31552/)

## Key Features[#](https://docs.nvidia.com#key-features)

*NVIDIA Sparse MMA tensor core*supportMixed-precision computation support:

Input A/B

Input C

Output D

Compute

Block scaled

Support SM arch

`FP32`

`FP32`

`FP32`

`FP32`

No

`8.0, 8.6, 8.7`

`9.0, 10.0, 10.3`

`11.0, 12.0, 12.1`

`BF16`

`BF16`

`BF16`

`FP32`

`FP16`

`FP16`

`FP16`

`FP32`

`FP16`

`FP16`

`FP16`

`FP16`

No

`9.0`

`INT8`

`INT8`

`INT8`

`INT32`

No

`8.0, 8.6, 8.7`

`9.0, 10.0, 11.0`

`12.0, 12.1`

`INT32`

`INT32`

`FP16`

`FP16`

`BF16`

`BF16`

`INT8`

`INT8`

`INT8`

`INT32`

No

`8.0, 8.6, 8.7`

`9.0, 10.0, 11.0`

`12.0, 12.1`

`INT32`

`INT32`

`FP16`

`FP16`

`BF16`

`BF16`

`E4M3`

`FP16`

`E4M3`

`FP32`

No

`9.0, 10.0, 10.3`

`11.0, 12.0, 12.1`

`BF16`

`E4M3`

`FP16`

`FP16`

`BF16`

`BF16`

`FP32`

`FP32`

`E5M2`

`FP16`

`E5M2`

`FP32`

No

`9.0, 10.0, 10.3`

`11.0, 12.0, 12.1`

`BF16`

`E5M2`

`FP16`

`FP16`

`BF16`

`BF16`

`FP32`

`FP32`

`E4M3`

`FP16`

`E4M3`

`FP32`

A/B/D_OUT_SCALE =

`VEC64_UE8M0`

D_SCALE =

`32F`

`10.0, 10.3, 11.0`

`12.0, 12.1`

`BF16`

`E4M3`

`FP16`

`FP16`

A/B_SCALE =

`VEC64_UE8M0`

`BF16`

`BF16`

`FP32`

`FP32`

`E2M1`

`FP16`

`E2M1`

`FP32`

A/B/D_SCALE =

`VEC32_UE4M3`

D_SCALE =

`32F`

`10.0, 10.3, 11.0`

`12.0, 12.1`

`BF16`

`E2M1`

`FP16`

`FP16`

A/B_SCALE =

`VEC32_UE4M3`

`BF16`

`BF16`

`FP32`

`FP32`

Matrix pruning and compression functionalities

Activation functions, bias vector, and output scaling

Batched computation (multiple matrices in a single run)

GEMM Split-K mode

Auto-tuning functionality (see

[cusparseLtMatmulSearch()](https://docs.nvidia.com/functions.html#cusparseltmatmulsearch-label))NVTX ranging and Logging functionalities


## Support[#](https://docs.nvidia.com#support)

*Supported SM Architectures*:`SM 8.0`

,`SM 8.6`

,`SM 8.7`

,`SM 8.9`

,`SM 9.0`

,`SM 10.0`

,`SM 10.3`

,`SM 11.0`

,`SM 12.0`

,`SM 12.1`

*Supported CPU architectures and operating systems*:

OS |
CPU archs |
|---|---|
|
|
|
|

## Index[#](https://docs.nvidia.com#index)

[Release Notes](https://docs.nvidia.com/release_notes.html)[cuSPARSELt v0.9.1](https://docs.nvidia.com/release_notes.html#cusparselt-v0-9-1)[cuSPARSELt v0.9.0](https://docs.nvidia.com/release_notes.html#cusparselt-v0-9-0)[cuSPARSELt v0.8.1](https://docs.nvidia.com/release_notes.html#cusparselt-v0-8-1)[cuSPARSELt v0.8.0](https://docs.nvidia.com/release_notes.html#cusparselt-v0-8-0)[cuSPARSELt v0.7.1](https://docs.nvidia.com/release_notes.html#cusparselt-v0-7-1)[cuSPARSELt v0.7.0](https://docs.nvidia.com/release_notes.html#cusparselt-v0-7-0)[cuSPARSELt v0.6.3](https://docs.nvidia.com/release_notes.html#cusparselt-v0-6-3)[cuSPARSELt v0.6.2](https://docs.nvidia.com/release_notes.html#cusparselt-v0-6-2)[cuSPARSELt v0.6.1](https://docs.nvidia.com/release_notes.html#cusparselt-v0-6-1)[cuSPARSELt v0.6.0](https://docs.nvidia.com/release_notes.html#cusparselt-v0-6-0)[cuSPARSELt v0.5.2](https://docs.nvidia.com/release_notes.html#cusparselt-v0-5-2)[cuSPARSELt v0.5.0](https://docs.nvidia.com/release_notes.html#cusparselt-v0-5-0)[cuSPARSELt v0.4.0](https://docs.nvidia.com/release_notes.html#cusparselt-v0-4-0)[cuSPARSELt v0.3.0](https://docs.nvidia.com/release_notes.html#cusparselt-v0-3-0)[cuSPARSELt v0.2.0](https://docs.nvidia.com/release_notes.html#cusparselt-v0-2-0)[cuSPARSELt v0.1.0](https://docs.nvidia.com/release_notes.html#cusparselt-v0-1-0)[cuSPARSELt v0.0.1](https://docs.nvidia.com/release_notes.html#cusparselt-v0-0-1)

[Getting Started](https://docs.nvidia.com/getting_started.html)[cuSPARSELt Data Types](https://docs.nvidia.com/types.html)[cuSPARSELt Functions](https://docs.nvidia.com/functions.html)[cuSPARSELt Logging Features](https://docs.nvidia.com/logging.html)[Software License Agreement](https://docs.nvidia.com/license.html)