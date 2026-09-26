source: https://rocm.docs.amd.com/en/docs-7.2.4/what-is-rocm.html

# What is ROCm?[#](https://rocm.docs.amd.com#what-is-rocm)

2026-03-10

4 min read time

ROCm is a software stack, composed primarily of open-source software, that provides the tools for programming AMD Graphics Processing Units (GPUs), from low-level kernels to high-level end-user applications.


Specifically, ROCm provides the tools for
[HIP](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/index.html),
OpenCL and OpenMP. These include compilers, libraries for high-level
functions, debuggers, profilers and runtimes.

## ROCm components[#](https://rocm.docs.amd.com#rocm-components)

ROCm consists of the following components. For information on the license associated with each component,
see [ROCm licensing](https://rocm.docs.amd.com/about/license.html).

### Libraries[#](https://rocm.docs.amd.com#libraries)

#### Machine Learning & Computer Vision[#](https://rocm.docs.amd.com#machine-learning-computer-vision)

Component |
Description |
|---|---|
Provides a programming model for writing performance critical kernels for machine learning workloads across multiple architectures |
|
Graph inference engine that accelerates machine learning model inference |
|
An open source deep-learning library |
|
Set of comprehensive computer vision and machine learning libraries, utilities, and applications |
|
Comprehensive high-performance computer vision library for AMD processors with HIP/OpenCL/CPU back-ends |
|
An augmentation library designed to decode and process images and videos |
|
High-performance SDK for access to video decoding features on AMD GPUs |
|
Library for decoding JPG images on AMD GPUs |
|
Provides access to rocDecode APIs in both Python and C/C++ languages |

Note

[rocCV](https://rocm.docs.amd.com/projects/rocCV/en/latest/index.html) is an efficient GPU-accelerated library for image pre- and post-processing. rocCV is in an early access state. Using it on production workloads is not recommended.

#### Communication[#](https://rocm.docs.amd.com#communication)

#### Math[#](https://rocm.docs.amd.com#math)

Component |
Description |
|---|---|
C++ header-only library that provides an IEEE 754 conformant, 16-bit half-precision floating-point type, along with corresponding arithmetic operators, type conversions, and common mathematical functions |
|
BLAS-marshaling library that supports |
|
Provides general matrix-matrix operations with a flexible API and extends functionalities beyond traditional BLAS library |
|
Fast Fourier transforms (FFT)-marshalling library that supports rocFFT or cuFFT backends |
|
Fortran interface library for accessing GPU Kernels |
|
Ports CUDA applications that use the cuRAND library into the HIP layer |
|
An LAPACK-marshalling library that supports |
|
SPARSE-marshalling library that supports |
|
SPARSE-marshalling library with multiple supported backends |
|
Sparse linear algebra library for exploring fine-grained parallelism on ROCm runtime and toolchains |
|
BLAS implementation (in the HIP programming language) on the ROCm runtime and toolchains |
|
Software library for computing fast Fourier transforms (FFTs) written in HIP |
|
Provides functions that generate pseudorandom and quasirandom numbers |
|
An implementation of LAPACK routines on ROCm software, implemented in the HIP programming language and optimized for AMD’s latest discrete GPUs |
|
Exposes a common interface that provides BLAS for sparse computation implemented on ROCm runtime and toolchains (in the HIP programming language) |
|
C++ library for accelerating mixed-precision matrix multiply-accumulate (MMA) operations |
|
Creates benchmark-driven backend libraries for GEMMs, GEMM-like problems, and general N-dimensional tensor contractions |

#### Primitives[#](https://rocm.docs.amd.com#primitives)

Component |
Description |
|---|---|
Thin header-only wrapper library on top of |
|
AMD’s C++ library for accelerating tensor primitives based on the composable kernel library |
|
Header-only library for HIP parallel primitives |
|
Parallel algorithm library |

### Tools[#](https://rocm.docs.amd.com#tools)

#### System Management[#](https://rocm.docs.amd.com#system-management)

Component |
Description |
|---|---|
System management interface to control AMD GPU settings, monitor performance, and retrieve device and process information |
|
Simplifies administration and addresses key infrastructure challenges in AMD GPUs in cluster and data-center environments |
|
Reports system information |
|
C library for Linux that provides a user space interface for applications to monitor and control GPU applications |
|
Detects and troubleshoots common problems affecting AMD GPUs running in a high-performance computing environment |

#### Performance[#](https://rocm.docs.amd.com#performance)

Component |
Description |
|---|---|
Captures the performance characteristics of buffer copying and kernel read/write operations |
|
Kernel-level profiling for machine learning and high performance computing (HPC) workloads |
|
Comprehensive profiling and tracing of applications running on the CPU or the CPU and GPU |
|
Profiling tool for HIP applications |
|
Toolkit for developing analysis tools for profiling and tracing GPU compute applications. This toolkit is in beta and subject to change |
|
Intercepts runtime API calls and traces asynchronous activity |

Note

[ROCprof Compute Viewer](https://rocm.docs.amd.com/projects/rocprof-compute-viewer/en/amd-mainline/) is a tool for visualizing and analyzing GPU thread trace data collected using [rocprofv3](https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/docs-7.2.4/index.html). Note that [ROCprof Compute Viewer](https://rocm.docs.amd.com/projects/rocprof-compute-viewer/en/amd-mainline/) is in an early access state. Running production workloads is not recommended.

#### Development[#](https://rocm.docs.amd.com#development)

Component |
Description |
|---|---|
Translates CUDA source code into portable HIP C++ |
|
Collection of CMake modules for common build and development tasks |
|
ROCm debugger API library |
|
Source-level debugger for Linux, based on the GNU Debugger (GDB) |
|
Prints the state of all AMD GPU wavefronts that caused a queue error by sending a SIGQUIT signal to the process while the program is running |

### Compilers[#](https://rocm.docs.amd.com#compilers)

Component |
Description |
|---|---|
Compiler driver utility that calls Clang and passes the appropriate include and library options for the target compiler and HIP infrastructure |
|
ROCm LLVM compiler infrastructure |
|
An out-of-tree Fortran compiler targeting LLVM |

### Runtime API[#](https://rocm.docs.amd.com#runtime-api)

Component |
Description |
|---|---|
HIP is a C++ runtime API and kernel language for AMD GPUs |