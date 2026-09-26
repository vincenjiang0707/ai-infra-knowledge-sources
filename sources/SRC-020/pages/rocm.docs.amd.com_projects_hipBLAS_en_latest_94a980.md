source: https://rocm.docs.amd.com/projects/hipBLAS/en/latest

# hipBLAS documentation[#](https://rocm.docs.amd.com#hipblas-documentation)

hipBLAS is a Basic Linear Algebra Subprograms (BLAS) marshaling library that
supports multiple backends. It lies between the application and a “worker” BLAS library,
marshalling inputs into the backend library and results back to the application.
hipBLAS exports an interface that does not require client changes, regardless of the
chosen backend. Currently, it supports [rocBLAS](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/index.html) and
NVIDIA CUDA [cuBLAS](https://developer.nvidia.com/cublas) as backends.

The hipBLAS public repository is located at
[ROCm/rocm-libraries](https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipblas).

Note

The hipBLAS repository for ROCm 6.4.3 and earlier is located at [ROCm/hipBLAS](https://github.com/ROCm/hipBLAS).

To contribute to the documentation, see
[Contributing to ROCm](https://rocm.docs.amd.com/en/latest/contribute/contributing.html).
For information on contributing to the hipBLAS code base, see [Contribute to hipBLAS](https://rocm.docs.amd.com/contribute.html).

You can find licensing information on the
[Licensing](https://rocm.docs.amd.com/en/latest/about/license.html) page.