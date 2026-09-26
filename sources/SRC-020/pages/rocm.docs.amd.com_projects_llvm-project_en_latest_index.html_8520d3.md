source: https://rocm.docs.amd.com/projects/llvm-project/en/latest/index.html

# ROCm LLVM compiler infrastructure[#](https://rocm.docs.amd.com#rocm-llvm-compiler-infrastructure)

The AMD `llvm-project`

is a fork of [llvm/llvm-project](https://github.com/llvm/llvm-project). The AMD code is open and hosted at [ROCm/llvm-project](https://github.com/ROCm/llvm-project).

ROCm includes multiple compilers of varying origins and purposes as described in the following table:

|
|
|
Clang/LLVM-based compiler that is part of |
|
Closed-source clang-based compiler that includes additional CPU optimizations. |
|
Another name for the |
|
Tools used to automatically translate CUDA source code into portable HIP C++, including |
|
HIP compiler driver utility that invokes |

AMD ROCm also provides additional open-source utilities and libraries for building GPU code located in the `llvm-project/amd`

directory:

|
|
|
The Code Object Manager API, designed to simplify linking, compiling, and inspecting code objects. See the |
|
The sources and CMake build system for a set of AMD-specific device-side language runtime libraries. See the |