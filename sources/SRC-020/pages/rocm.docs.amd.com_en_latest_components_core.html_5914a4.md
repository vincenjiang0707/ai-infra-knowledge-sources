source: https://rocm.docs.amd.com/en/latest/components/core.html

# ROCm Core SDK components[#](https://rocm.docs.amd.com#rocm-core-sdk-components)

The ROCm Core SDK is the foundation of the ROCm software stack. It provides the libraries, runtimes, compilers, and tools needed to develop and run GPU-accelerated applications on AMD hardware.

## Math and compute libraries[#](https://rocm.docs.amd.com#math-and-compute-libraries)

A comprehensive set of GPU-accelerated math libraries covering dense and sparse linear algebra, FFTs, random number generation, and more.

Libraries prefixed with

`roc*`

are native, high-performance implementations written in HIP specifically for AMD GPUs.Libraries prefixed with

`hip*`

are portable wrappers that implement NVIDIA CUDA-equivalent APIs, allowing CUDA applications to be ported to AMD GPUs with minimal code changes.

Libraries include:

[Composable Kernel 1.2.0](https://rocm.docs.amd.com/projects/composable_kernel/en/docs-10.0.0/)– Provides a programming model for writing performance critical kernels for machine learning workloads across multiple architectures.[hipBLAS 3.6.0](https://rocm.docs.amd.com/projects/hipBLAS/en/docs-10.0.0/)– BLAS-marshalling library that supports rocBLAS and cuBLAS backends.[hipBLASLt 1.4.1](https://rocm.docs.amd.com/projects/hipBLASLt/en/docs-10.0.0/)– Provides general matrix-matrix operations with a flexible API and extends functionalities beyond traditional BLAS library.[hipCUB 4.6.0](https://rocm.docs.amd.com/projects/hipCUB/en/docs-10.0.0/)– Thin header-only wrapper library on top of rocPRIM or CUB that allows project porting using the CUB library to the HIP layer.[hipFFT 1.0.25](https://rocm.docs.amd.com/projects/hipFFT/en/docs-10.0.0/)– Fast Fourier Transforms (FFT)-marshalling library that supports rocFFT or cuFFT backends.[hipRAND 3.4.0](https://rocm.docs.amd.com/projects/hipRAND/en/docs-10.0.0/)– Ports CUDA applications that use the cuRAND library into the HIP layer.[hipSOLVER 3.6.0](https://rocm.docs.amd.com/projects/hipSOLVER/en/docs-10.0.0/)– LAPACK-marshalling library that supports rocSOLVER and cuSOLVER backends.[hipSPARSE 4.7.0](https://rocm.docs.amd.com/projects/hipSPARSE/en/docs-10.0.0/)– SPARSE-marshalling library that supports rocSPARSE and cuSPARSE backends.[hipSPARSELt 0.2.9](https://rocm.docs.amd.com/projects/hipSPARSELt/en/docs-10.0.0/)– Sparse matrix-matrix operations library.[MIOpen 3.6.0](https://rocm.docs.amd.com/projects/MIOpen/en/docs-10.0.0/)– An open source deep-learning library.[rocBLAS 5.6.0](https://rocm.docs.amd.com/projects/rocBLAS/en/docs-10.0.0/)– BLAS implementation (in the HIP programming language) on the ROCm runtime and toolchains.[rocFFT 1.0.39](https://rocm.docs.amd.com/projects/rocFFT/en/docs-10.0.0/)– Software library for computing Fast Fourier Transforms (FFTs) written in HIP.[rocPRIM 4.6.0](https://rocm.docs.amd.com/projects/rocPRIM/en/docs-10.0.0/)– Header-only library for HIP parallel primitives.[rocRAND 5.0.0](https://rocm.docs.amd.com/projects/rocRAND/en/docs-10.0.0/)– Provides functions that generate pseudorandom and quasirandom numbers.[rocSOLVER 3.36.0](https://rocm.docs.amd.com/projects/rocSOLVER/en/docs-10.0.0/)– An implementation of LAPACK routines on ROCm software, implemented in the HIP programming language and optimized for AMD’s latest discrete GPUs.[rocSPARSE 5.0.0](https://rocm.docs.amd.com/projects/rocSPARSE/en/docs-10.0.0/)– Exposes a common interface that provides BLAS for sparse computation implemented on ROCm runtime and toolchains (in the HIP programming language).[rocThrust 4.6.0](https://rocm.docs.amd.com/projects/rocThrust/en/docs-10.0.0/)– Parallel algorithm library.[rocWMMA 2.2.1](https://rocm.docs.amd.com/projects/rocWMMA/en/docs-10.0.0/)– C++ library for accelerating mixed-precision matrix multiply-accumulate (MMA) operations.

## Communication libraries[#](https://rocm.docs.amd.com#communication-libraries)

[RCCL 2.30.7](https://rocm.docs.amd.com/projects/rccl/en/docs-10.0.0/)– Standalone library that provides multi-GPU and multi-node collective communication primitives.[rocSHMEM 3.6.0](https://rocm.docs.amd.com/projects/rocSHMEM/en/docs-10.0.0/)– An intra-kernel networking library that provides GPU-centric networking through an OpenSHMEM-like interface.

## Profiling and debugging tools[#](https://rocm.docs.amd.com#profiling-and-debugging-tools)

[ROCdbgapi 0.80.0](https://rocm.docs.amd.com/projects/ROCdbgapi/en/docs-10.0.0/)– ROCm debugger API library.[ROCgdb 16.3](https://rocm.docs.amd.com/projects/ROCgdb/en/docs-10.0.0/)– Source-level debugger for Linux, based on the GNU Debugger (GDB).[ROCm Compute Profiler 3.8.0](https://rocm.docs.amd.com/projects/rocprofiler-compute/en/docs-10.0.0/)– Kernel-level profiling for machine learning and high performance computing (HPC) workloads.[ROCm Systems Profiler 1.8.0](https://rocm.docs.amd.com/projects/rocprofiler-systems/en/docs-10.0.0/)– Comprehensive profiling and tracing of applications running on the CPU or the CPU and GPU.[ROCprofiler-SDK 1.3.5](https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/docs-10.0.0/)– Toolkit for developing analysis tools for profiling and tracing GPU compute applications.[ROCr Debug Agent 2.1.0](https://rocm.docs.amd.com/projects/rocr_debug_agent/en/docs-10.0.0/)– Prints the state of all AMD GPU wavefronts that caused a queue error by sending a SIGQUIT signal to the process while the program is running.

## Control and monitoring tools[#](https://rocm.docs.amd.com#control-and-monitoring-tools)

[AMD SMI 27.0.0](https://rocm.docs.amd.com/projects/amdsmi/en/docs-10.0.0/)– System management interface to control AMD GPU settings, monitor performance, and retrieve device and process information.[ROCm Data Center Tool 1.3.1](https://rocm.docs.amd.com/projects/rdc/en/docs-10.0.0/)– Simplifies administration and addresses key infrastructure challenges in AMD GPUs in cluster and data-center environments.[rocminfo 1.0.0](https://rocm.docs.amd.com/projects/rocminfo/en/docs-10.0.0/)– Reports system information.

## Media libraries[#](https://rocm.docs.amd.com#media-libraries)

[rocDecode 1.9.0](https://rocm.docs.amd.com/projects/rocDecode/en/docs-10.0.0/)– High-performance SDK for access to video decoding features on AMD GPUs.[rocJPEG 1.7.0](https://rocm.docs.amd.com/projects/rocJPEG/en/docs-10.0.0/)– Library for decoding JPEG images on AMD GPUs.

## Runtimes and compilers[#](https://rocm.docs.amd.com#runtimes-and-compilers)

[HIP 10.0.0](https://rocm.docs.amd.com/projects/HIP/en/docs-10.0.0/)– A C++ runtime API and kernel programming language designed for AMD GPUs. By providing an interface closely aligned with NVIDIA CUDA, HIP allows developers to write portable applications and efficiently migrate existing CUDA code to AMD platforms.[HIPIFY 10.0.0](https://rocm.docs.amd.com/projects/HIPIFY/en/docs-10.0.0/)– Translates CUDA source code into portable HIP C++.[LLVM 24.0.0](https://rocm.docs.amd.com/projects/llvm-project/en/docs-10.0.0/)– AMD’s LLVM-based compiler infrastructure, including the ROCm device compiler (amdclang), which compiles HIP and OpenCL code for AMD GPUs.[ROCr Runtime 1.21.0](https://rocm.docs.amd.com/projects/ROCR-Runtime/en/docs-10.0.0/)– AMD’s implementation of the HSA (Heterogeneous System Architecture) runtime, providing the foundation for GPU execution and management in the ROCm software stack.[SPIRV-LLVM-Translator 24.0.0](https://github.com/ROCm/SPIRV-LLVM-Translator/tree/therock-10.0)– Library and tool for bidirectional translation between SPIR-V and LLVM.

## Storage libraries[#](https://rocm.docs.amd.com#storage-libraries)

[hipFile 0.4.0](https://rocm.docs.amd.com/projects/hipFile/en/docs-10.0.0/)– AMD’s Infinity Storage library that provides direct-to-GPU I/O for the ROCm platform.