source: https://rocm.docs.amd.com/en/docs-7.2.4/compatibility/ml-compatibility/jax-compatibility.html

# JAX compatibility[#](https://rocm.docs.amd.com#jax-compatibility)

2026-03-02

7 min read time

[JAX](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html) is a library
for array-oriented numerical computation (similar to NumPy), with automatic differentiation
and just-in-time (JIT) compilation to enable high-performance machine learning research.

JAX provides an API that combines automatic differentiation and the Accelerated Linear Algebra (XLA) compiler to achieve high-performance machine learning at scale. JAX uses composable transformations of Python and NumPy through JIT compilation, automatic vectorization, and parallelization.

## Support overview[#](https://rocm.docs.amd.com#support-overview)

The ROCm-supported version of JAX is maintained in the official

[ROCm/rocm-jax](https://github.com/ROCm/rocm-jax)repository, which differs from the[jax-ml/jax](https://github.com/jax-ml/jax)upstream repository.To get started and install JAX on ROCm, use the prebuilt

[Docker images](https://rocm.docs.amd.com#jax-docker-compat), which include ROCm, JAX, and all required dependencies.See the

[ROCm JAX installation guide](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.4/install/3rd-party/jax-install.html)for installation and setup instructions.You can also consult the upstream

[Installation guide](https://jax.readthedocs.io/en/latest/installation.html#amd-gpu-linux)for additional context.


### Version support[#](https://rocm.docs.amd.com#version-support)

AMD releases official [ROCm JAX Docker images](https://hub.docker.com/r/rocm/jax/tags)
quarterly alongside new ROCm releases. These images undergo full AMD testing.
[Community ROCm JAX Docker images](https://hub.docker.com/r/rocm/jax-community/tags)
follow upstream JAX releases and use the latest available ROCm version.

## JAX Plugin-PJRT with JAX/JAXLIB compatibility[#](https://rocm.docs.amd.com#jax-plugin-pjrt-with-jax-jaxlib-compatibility)

Portable JIT Runtime (PJRT) is an open, stable interface for device runtime and compiler. The following table details the ROCm version compatibility matrix between JAX Plugin–PJRT and JAX/JAXLIB.

JAX Plugin-PJRT |
JAX/JAXLIB |
ROCm |
|---|---|---|
0.8.2 |
0.8.2 |
7.2.1 |
0.8.0 |
0.8.0 |
7.2.0 |
0.7.1 |
0.7.1 |
7.1.1, 7.1.0 |

## Use cases and recommendations[#](https://rocm.docs.amd.com#use-cases-and-recommendations)

The

[nanoGPT in JAX](https://rocm.blogs.amd.com/artificial-intelligence/nanoGPT-JAX/README.html)blog explores the implementation and training of a Generative Pre-trained Transformer (GPT) model in JAX, inspired by Andrej Karpathy’s JAX-based nanoGPT. Comparing how essential GPT components—such as self-attention mechanisms and optimizers—are realized in JAX and JAX, also highlights JAX’s unique features.The

[Optimize GPT Training: Enabling Mixed Precision Training in JAX using ROCm on AMD GPUs](https://rocm.blogs.amd.com/artificial-intelligence/jax-mixed-precision/README.html)blog post provides a comprehensive guide on enhancing the training efficiency of GPT models by implementing mixed precision techniques in JAX, specifically tailored for AMD GPUs utilizing the ROCm platform.The

[Supercharging JAX with Triton Kernels on AMD GPUs](https://rocm.blogs.amd.com/artificial-intelligence/jax-triton/README.html)blog demonstrates how to develop a custom fused dropout-activation kernel for matrices using Triton, integrate it with JAX, and benchmark its performance using ROCm.The

[Distributed fine-tuning with JAX on AMD GPUs](https://rocm.blogs.amd.com/artificial-intelligence/distributed-sft-jax/README.html)outlines the process of fine-tuning a Bidirectional Encoder Representations from Transformers (BERT)-based large language model (LLM) using JAX for a text classification task. The blog post discusses techniques for parallelizing the fine-tuning across multiple AMD GPUs and assess the model’s performance on a holdout dataset. During the fine-tuning, a BERT-base-cased transformer model and the General Language Understanding Evaluation (GLUE) benchmark dataset was used on a multi-GPU setup.The

[MI300X workload optimization guide](https://rocm.docs.amd.com/en/latest/how-to/tuning-guides/mi300x/workload.html)provides detailed guidance on optimizing workloads for the AMD Instinct MI300X GPU using ROCm. The page is aimed at helping users achieve optimal performance for deep learning and other high-performance computing tasks on the MI300X GPU.

For more use cases and recommendations, see [ROCm JAX blog posts](https://rocm.blogs.amd.com/blog/tag/jax.html).

## Docker image compatibility[#](https://rocm.docs.amd.com#docker-image-compatibility)

AMD validates and publishes [JAX images](https://hub.docker.com/r/rocm/jax/tags)
with ROCm backends on Docker Hub.

For `jax-community`

images, see [rocm/jax-community](https://hub.docker.com/r/rocm/jax-community/tags) on Docker Hub.

To find the right image tag, see the [JAX on ROCm installation
documentation](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.4/install/3rd-party/jax-install.html#jax-docker-support) for a list of
available `rocm/jax`

images.

## Key ROCm libraries for JAX[#](https://rocm.docs.amd.com#key-rocm-libraries-for-jax)

The following ROCm libraries represent potential targets that could be utilized by JAX on ROCm for various computational tasks. The actual libraries used will depend on the specific implementation and operations performed.

ROCm library |
Version |
Purpose |
|---|---|---|
3.2.0 |
Provides GPU-accelerated Basic Linear Algebra Subprograms (BLAS) for matrix and vector operations. |
|
1.2.2 |
hipBLASLt is an extension of hipBLAS, providing additional features like epilogues fused into the matrix multiplication kernel or use of integer tensor cores. |
|
4.2.0 |
Provides a C++ template library for parallel algorithms for reduction, scan, sort and select. |
|
1.0.22 |
Provides GPU-accelerated Fast Fourier Transform (FFT) operations. |
|
3.1.0 |
Provides fast random number generation for GPUs. |
|
3.2.0 |
Provides GPU-accelerated solvers for linear systems, eigenvalues, and singular value decompositions (SVD). |
|
4.2.0 |
Accelerates operations on sparse matrices, such as sparse matrix-vector or matrix-matrix products. |
|
0.2.6 |
Accelerates operations on sparse matrices, such as sparse matrix-vector or matrix-matrix products. |
|
3.5.1 |
Optimized for deep learning primitives such as convolutions, pooling, normalization, and activation functions. |
|
2.27.7 |
Optimized for multi-GPU communication for operations like all-reduce, broadcast, and scatter. |
|
4.2.0 |
Provides a C++ template library for parallel algorithms like sorting, reduction, and scanning. |

Note

This table shows ROCm libraries that could potentially be utilized by JAX. Not all libraries may be used in every configuration, and the actual library usage will depend on the specific operations and implementation details.

## Supported data types and modules[#](https://rocm.docs.amd.com#supported-data-types-and-modules)

The following tables lists the supported public JAX API data types and modules.

### Supported data types[#](https://rocm.docs.amd.com#supported-data-types)

ROCm supports all the JAX data types of [jax.dtypes](https://docs.jax.dev/en/latest/jax.dtypes.html)
module, [jax.numpy.dtype](https://docs.jax.dev/en/latest/_autosummary/jax.numpy.dtype.html)
and [default_dtype](https://docs.jax.dev/en/latest/default_dtypes.html) .
The ROCm supported data types in JAX are collected in the following table.

Data type |
Description |
|---|---|
|
16-bit bfloat (brain floating point). |
|
Boolean. |
|
128-bit complex. |
|
64-bit complex. |
|
16-bit (half precision) floating-point. |
|
32-bit (single precision) floating-point. |
|
64-bit (double precision) floating-point. |
|
16-bit (half precision) floating-point. |
|
Signed 16-bit integer. |
|
Signed 32-bit integer. |
|
Signed 64-bit integer. |
|
Signed 8-bit integer. |
|
Unsigned 16-bit (word) integer. |
|
Unsigned 32-bit (dword) integer. |
|
Unsigned 64-bit (qword) integer. |
|
Unsigned 8-bit (byte) integer. |

Note

JAX data type support is affected by the [Key ROCm libraries for JAX](https://rocm.docs.amd.com#key-rocm-libraries) and it’s
collected on [ROCm data types and precision support](https://rocm.docs.amd.com/en/docs-7.2.4/reference/precision-support.html)
page.

### Supported modules[#](https://rocm.docs.amd.com#supported-modules)

For a complete and up-to-date list of JAX public modules (for example, `jax.numpy`

,
`jax.scipy`

, `jax.lax`

), their descriptions, and usage, please refer directly to the
[official JAX API documentation](https://jax.readthedocs.io/en/latest/jax.html).

Note

Since version 0.1.56, JAX has full support for ROCm, and the
[Known issues and important notes](https://rocm.docs.amd.com#jax-comp-known-issues) section
contains details about limitations specific to the ROCm backend. The list of
JAX API modules are maintained by the JAX project and is subject to change.
Refer to the official Jax documentation for the most up-to-date information.

## Key features and enhancements for ROCm 7.1[#](https://rocm.docs.amd.com#key-features-and-enhancements-for-rocm-7-1)

Enabled compilation of multihost HLO runner Python bindings.

Backported multihost HLO runner bindings and some related changes to

`FunctionalHloRunner`

.Added

`requirements_lock_3_12`

to enable building for Python 3.12.

Removed hardcoded NHWC convolution layout for

`fp16`

precision to address the performance drops for`fp16`

precision on gfx12xx GPUs.ROCprofiler-SDK integration:

Integrated ROCprofiler-SDK (v3) to XLA to improve profiling of GPU events, support both time-based and step-based profiling.

Added unit tests for

`rocm_collector`

and`rocm_tracer`

.

Added Triton unsupported conversion from

`f8E4M3FNUZ`

to`fp16`

with rounding mode.Introduced

`CudnnFusedConvDecomposer`

to revert fused convolutions when`ConvAlgorithmPicker`

fails to find a fused algorithm, and removed unfused fallback paths from`RocmFusedConvRunner`

.

## Key features and enhancements for ROCm 7.0[#](https://rocm.docs.amd.com#key-features-and-enhancements-for-rocm-7-0)

Upgraded XLA backend: Integrates a newer XLA version, enabling better optimizations, broader operator support, and potential performance gains.

RNN support: Native RNN support (including LSTMs via

`jax.experimental.rnn`

) now available on ROCm, aiding sequence model development.Comprehensive linear algebra capabilities: Offers robust

`jax.linalg`

operations, essential for scientific and machine learning tasks.Expanded AMD GPU architecture support: Provides ongoing support for gfx1101 GPUs and introduces support for gfx950 and gfx12xx GPUs.

Mixed FP8 precision support: Enables

`lax.dot_general`

operations with mixed FP8 types, offering pathways for memory and compute efficiency.Streamlined PyPi packaging: Provides reliable PyPi wheels for JAX on ROCm, simplifying the installation process.

Pallas experimental kernel development: Continued Pallas framework enhancements for custom GPU kernels, including new intrinsics (specific kernel behaviors under review).

Improved build system and CI: Enhanced ROCm build system and CI for greater reliability and maintainability.

Enhanced distributed computing setup: Improved JAX setup in multi-GPU distributed environments.


## Known issues and notes for ROCm 7.0[#](https://rocm.docs.amd.com#known-issues-and-notes-for-rocm-7-0)

`nn.dot_product_attention`

: Certain configurations of`jax.nn.dot_product_attention`

may cause segmentation faults, though the majority of use cases work correctly.SVD with dynamic shapes: SVD on inputs with dynamic/symbolic shapes might result in an error. SVD with static shapes is unaffected.

QR decomposition with symbolic shapes: QR decomposition operations may fail when using symbolic/dynamic shapes in shape polymorphic contexts.

Pallas kernels: Specific advanced Pallas kernels may exhibit variations in numerical output or resource usage. These are actively reviewed as part of Pallas’s experimental development.