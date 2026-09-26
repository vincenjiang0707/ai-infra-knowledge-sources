source: https://docs.nvidia.com/deploy/cuda-compatibility/frequently-asked-questions.html

# Frequently Asked Questions[#](https://docs.nvidia.com#frequently-asked-questions)

This section includes some FAQs related to CUDA compatibility.

**Does CUDA forward compatible upgrades work intra-branch?**Users can upgrade the kernel mode driver within the same branch. Sometimes this may require updating the

`cuda-compat-*`

package. This use-case is supported only for drivers on LLB and LTS branches of driver for select GPUs.**What’s the minimum required driver version of a toolkit?**Refer to the

[Release notes](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html#cuda-major-component-versions__table-cuda-toolkit-driver-versions).**The developer is using PTX code in the application and seeing some errors or issues. What should we do?**PTX and application compatibility information can be found in

[Binary Compatibility](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#binary-compatibility).**If we build our CUDA application using CUDA 11.0, can it continue to be used with newer NVIDIA drivers (such as CUDA 11.1/R455, 11.x etc.)? Or is it only the other way around?**Drivers have always been backwards compatible with CUDA. This means that a CUDA 11.0 application will be compatible with R450 (11.0), R455 (11.1) and beyond. CUDA applications typically statically include all the libraries (for example cudart, CUDA math libraries such as cuBLAS, cuFFT) they need, so they should work on new drivers or CUDA Toolkit installations.

In other words, since CUDA is backward compatible, existing CUDA applications can continue to be used with newer CUDA versions.

**What about new features introduced in minor releases of CUDA? How does a developer build an application using newer CUDA Toolkits (such as 11.x) work on a system with a CUDA 11.0 driver (R450)?**By using new CUDA versions, users can benefit from new CUDA programming model APIs, compiler optimizations and math library features.

A subset of CUDA APIs don’t need a new driver and they can all be used without any driver dependencies. For example, async copy APIs introduced in 11.1 do not need a new driver.

To use other CUDA APIs introduced in a minor release (that require a new driver), one would have to implement fallbacks or fail gracefully. This situation is not different from what is available today where developers use macros to compile out features based on CUDA versions. Users should refer to the CUDA headers and documentation for new CUDA APIs introduced in a release.


There are some issues that administrators can advise the application developers to accommodate in their code. Please refer to the Best Practices Guide for further information.

**Does CUDA compatibility work with containers?**Yes. CUDA minor version compatibility and CUDA forward compatible upgrade both work when using either NGC Deep Learning Framework containers or using containers that are based on the official CUDA base images. The images include the CUDA compatible upgrade libraries and the NVIDIA Container Toolkit (nvidia-docker2) has logic to correctly load the required libraries.

**I’m running an NGC container and see this error: “This container was built for NVIDIA driver Release 450.51 or later, but version 418.126.02 was detected and compatibility mode is UNAVAILABLE.”. What could be wrong?**It is possible you are either running a wrong version of the NVIDIA driver on the system or your system does not have an NVIDIA Data Center GPU.