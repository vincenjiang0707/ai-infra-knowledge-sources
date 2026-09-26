source: https://rocm.docs.amd.com/projects/install-on-windows/en/latest/

# HIP SDK for Windows[#](https://rocm.docs.amd.com#hip-sdk-for-windows)

2026-02-19

2 min read time

HIP SDK for Windows provides a subset of the ROCm platform to Microsoft Windows as described in
[ROCm component support in HIP SDK](https://rocm.docs.amd.com/conceptual/component-support.html). It provides the runtime,
APIs, and tooling to leverage the computational power of AMD GPUs to create high-performance,
portable applications using the [HIP programming language](https://rocm.docs.amd.com/projects/HIP/en/latest/index.html).

The HIP SDK consists of the AMD GPU Driver, HIP runtime, and HIP Libraries. These three parts are distributed in the HIP SDK installer. The HIP SDK is intended for developer distribution. This is in contrast to the AMD GPU driver, which is intended for all end users.

HIP SDK can run on your Windows system with Microsoft Visual Studio Code, and even includes solutions for use with the tool. However, it also has standalone tools like compilers, profilers, and debuggers for use in your own development environment.

HIP SDK code is open and hosted at [ROCm/rocm-install-on-windows](https://github.com/ROCm/rocm-install-on-windows).

The documentation is structured as follows: