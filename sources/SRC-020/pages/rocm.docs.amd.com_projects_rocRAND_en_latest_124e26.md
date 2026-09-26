source: https://rocm.docs.amd.com/projects/rocRAND/en/latest

# rocRAND documentation[#](https://rocm.docs.amd.com#rocrand-documentation)

rocRAND provides functions that generate pseudo-random and quasi-random numbers.
The rocRAND library is implemented in the [HIP](https://rocm.docs.amd.com/projects/HIP/en/latest/index.html)
programming language and optimized for the latest discrete AMD GPUs. It is designed to run on top
of the AMD ROCm platform.

rocRAND integrates with a wrapper library called hipRAND, which you can use to easily port
NVIDIA CUDA applications that use the CUDA cuRAND library to the
[HIP](https://rocm.docs.amd.com/projects/HIP/en/latest/index.html) layer. In a
ROCm environment, hipRAND uses the rocRAND library.

The rocRAND public repository is located at [ROCm/rocm-libraries](https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocrand).

Note

The rocRAND repository for ROCm 6.4 and earlier is located at [ROCm/rocRAND](https://github.com/ROCm/rocRAND).

To contribute to the documentation, see [Contributing to ROCm](https://rocm.docs.amd.com/en/latest/contribute/contributing.html).

You can find licensing information on the [Licensing](https://rocm.docs.amd.com/en/latest/about/license.html) page.