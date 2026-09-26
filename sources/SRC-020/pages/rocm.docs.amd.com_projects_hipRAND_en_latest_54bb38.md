source: https://rocm.docs.amd.com/projects/hipRAND/en/latest

# hipRAND documentation[#](https://rocm.docs.amd.com#hiprand-documentation)

The hipRAND library is a wrapper library that lets you easily port NVIDIA CUDA applications that use the CUDA cuRAND library to the HIP layer. It sits between your application and the backend RAND library, where it marshals inputs to the backend and results to the application. hipRAND exports an interface that doesn’t require the client to change, regardless of the chosen backend. It uses rocRAND in a ROCm environment and provides C, C++, and Python API wrappers.

The hipRAND public repository is located at [ROCm/rocm-libraries](https://github.com/ROCm/rocm-libraries/tree/develop/projects/hiprand).

Note

The hipRAND repository for ROCm 6.4 and earlier is located at [ROCm/hipRAND](https://github.com/ROCm/hipRAND).

To contribute to the documentation, see [Contributing to ROCm](https://rocm.docs.amd.com/en/latest/contribute/contributing.html).

You can find licensing information on the [Licensing](https://rocm.docs.amd.com/en/latest/about/license.html) page.