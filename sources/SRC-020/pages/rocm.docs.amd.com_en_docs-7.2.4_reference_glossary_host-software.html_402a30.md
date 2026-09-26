source: https://rocm.docs.amd.com/en/docs-7.2.4/reference/glossary/host-software.html

# Host software glossary[#](https://rocm.docs.amd.com#host-software-glossary)

2026-02-20

2 min read time

This section provides brief definitions of development tools, compilers, libraries, and runtime environments for programming AMD GPUs.

- AMD SMI
[#](https://rocm.docs.amd.com#term-AMD-SMI) The

`amd-smi`

command-line utility queries, monitors, and manages AMD GPU state, providing hardware information and performance metrics. See[AMD SMI documentation](https://rocm.docs.amd.com/projects/amdsmi/en/docs-7.2.4/index.html)for detailed usage.- HIP C++ language extension
[#](https://rocm.docs.amd.com#term-HIP-C-language-extension) HIP extends the C++ language with additional features designed for programming heterogeneous applications. These extensions mostly relate to the kernel language, but some can also be applied to host functionality. See

[HIP C++ language extensions](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/how-to/hip_cpp_language_extensions.html)for language fundamentals.- HIP compiler
[#](https://rocm.docs.amd.com#term-HIP-compiler) The HIP compiler

`amdclang++`

compiles HIP C++ programs into binaries that contain both host CPU and device GPU code. See[ROCm compiler reference](https://rocm.docs.amd.com/projects/llvm-project/en/docs-7.2.4/reference/rocmcc.html)for compiler flags and options.- HIP runtime API
[#](https://rocm.docs.amd.com#term-HIP-runtime-API) The HIP runtime API provides an interface for GPU programming, offering functions for memory management, kernel launches, and synchronization. See

[Using HIP runtime API](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/how-to/hip_runtime_api.html#hip-runtime-api-how-to)for API overview.- HIP runtime compiler
[#](https://rocm.docs.amd.com#term-HIP-runtime-compiler) The HIP Runtime Compiler (HIPRTC) compiles HIP source code at runtime into

[AMDGPU](https://rocm.docs.amd.com/device-software.html#term-AMDGPU-assembly)binary code objects, enabling just-in-time kernel generation, device-specific optimization, and dynamic code creation for different GPUs. See[Programming for HIP runtime compiler (RTC)](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/how-to/hip_rtc.html#hip-runtime-compiler-how-to)for API details.- ROCgdb
[#](https://rocm.docs.amd.com#term-ROCgdb) ROCgdb is AMD’s source-level debugger for HIP and ROCm applications, enabling debugging of both host CPU and GPU device code, including kernel breakpoints, stepping, and variable inspection. See

[ROCgdb documentation](https://rocm.docs.amd.com/projects/ROCgdb/en/docs-7.2.4/index.html)for usage and command reference.- ROCm and LLVM binary utilities
[#](https://rocm.docs.amd.com#term-ROCm-and-LLVM-binary-utilities) ROCm and LLVM binary utilities are command-line tools for examining and manipulating GPU binaries and code objects. See

[ROCm binary utilities](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/compilers.html#binary-utilities)for utility details.- ROCm software platform
[#](https://rocm.docs.amd.com#term-ROCm-software-platform) ROCm is AMD’s GPU software stack, providing compiler toolchains, runtime environments, and performance libraries for HPC and AI applications. See

[What is ROCm?](https://rocm.docs.amd.com/what-is-rocm.html)for a complete component overview.- rocprofv3
[#](https://rocm.docs.amd.com#term-rocprofv3) `rocprofv3`

is AMD’s primary performance analysis tool, providing profiling, tracing, and performance counter collection. See[Using rocprofv3](https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/docs-7.2.4/how-to/using-rocprofv3.html#using-rocprofv3)for profiling workflows.