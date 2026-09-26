source: https://rocm.docs.amd.com/en/latest/reference/hip-programming.html

# AMD GPU programming on ROCm[#](https://rocm.docs.amd.com#amd-gpu-programming-on-rocm)

ROCm provides a robust environment for heterogeneous programs running on CPUs and AMD GPUs. ROCm supports various programming languages and frameworks to help developers access the power of AMD GPUs. The natively supported programming languages are HIP and OpenCL, but HIP bindings are available for Python and Fortran.

Tip

For a complete description of the HIP programming language, see the

[HIP documentation](https://rocm.docs.amd.com/projects/HIP/en/latest/index.html).Developers who require a unified, book-style reference for ROCm and HIP can consult the

[AMD ROCm Programming Guide](https://rocm-handbook.amd.com/projects/amd-rocm-programming-guide/en/latest/). It aggregates documentation from the ROCm portal and organizes it into a structured format optimized for in-depth study and offline access in both PDF and HTML formats.

HIP is an API based on C++ that provides a runtime and kernel language for GPU programming and is the essential ROCm programming language. HIP enables single-source C++ programming with support for templates, C++11 lambdas, classes, and namespaces, letting developers create applications that run on heterogeneous systems using both CPUs and AMD GPUs from a single code base.

HIP provides two components: code that runs on the host (CPU) and code that runs on the device (GPU). Host code manages device buffers, moves data between host and device, launches kernels, and handles streams, events, and synchronization. The kernel language provides access to GPU-specific hardware capabilities for massively parallel execution.

ROCm includes a complete toolchain: compilers ([clang](https://rocm.docs.amd.com/projects/llvm-project/en/latest/index.html),
[hipcc](https://rocm.docs.amd.com/projects/HIPCC/en/latest/index.html)), a code profiler
([rocprofv3](https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/how-to/using-rocprofv3.html)), and a debugger
([rocgdb](https://rocm.docs.amd.com/projects/ROCgdb/en/latest/index.html)). ROCm also provides libraries such as
[hipFFT](https://rocm.docs.amd.com/projects/hipFFT/en/latest/index.html) and [hipBLAS](https://rocm.docs.amd.com/projects/hipBLAS/en/latest/index.html) that offer API
compatibility with equivalent NVIDIA CUDA libraries, making it easier to
integrate into existing workflows.

Developers with CUDA experience will find the HIP API familiar. HIP allows code
written for CUDA to be ported to AMD GPUs. [HIPIFY](https://rocm.docs.amd.com/projects/HIPIFY/en/latest/index.html), based
on the Clang front-end and Perl, can convert CUDA API calls into the
corresponding HIP API calls. However, HIP is not a drop-in replacement for
CUDA, and some manual coding and performance tuning may be required when porting
existing projects to AMD GPUs.

Python bindings can be found at [ROCm/hip-python](https://github.com/ROCm/hip-python).
Python is popular in AI and machine learning applications due to the
availability of frameworks such as PyTorch and TensorFlow.

Fortran bindings can be found at [ROCm/hipfort](https://github.com/ROCm/hipfort).
It enables scientific, academic, and legacy applications, particularly those in
high-performance computing, to run on AMD GPUs via HIP.

OpenCL (Open Computing Language) is an open standard for cross-platform,
parallel programming of diverse processors. ROCm supports OpenCL for developers
who want to use standard frameworks across different hardware platforms,
including CPUs, GPUs, and APUs. For more information, see
[OpenCL](https://www.khronos.org/opencl/).