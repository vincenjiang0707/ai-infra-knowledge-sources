source: https://rocm.docs.amd.com/projects/hipSOLVER/en/latest

# hipSOLVER documentation[#](https://rocm.docs.amd.com#hipsolver-documentation)

hipSOLVER is a LAPACK marshalling library with multiple supported backends. It sits between the application and a “worker” LAPACK library, marshalling inputs into the backend library and results back to the application. hipSOLVER supports rocSOLVER and NVIDIA CUDA cuSOLVER as backends. It exports an interface that does not require the client to change, regardless of the chosen backend.

The hipSOLVER public repository is located at [ROCm/rocm-libraries](https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipsolver).

The hipSOLVER repository for ROCm 7.0.2 and earlier is located at [ROCm/hipSOLVER](https://github.com/ROCm/hipSOLVER).

Install

How to

Examples

To contribute to the documentation, see [Contributing to ROCm](https://rocm.docs.amd.com/en/latest/contribute/contributing.html).

You can find licensing information on the [Licensing](https://rocm.docs.amd.com/en/latest/about/license.html) page.