source: https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html

# ROCm 10.0.0 compatibility matrix[#](https://rocm.docs.amd.com#rocm-rocm-version-compatibility-matrix)

2026-08-20

13 min read time

To plan your ROCm 10.0.0 installation, use the following selector to
view ROCm compatibility and system requirements information for your AMD
hardware configuration and system environment. For installation instructions,
see [Install AMD ROCm 10.0.0](https://rocm.docs.amd.com/install/rocm.html).

## System requirements and information[#](https://rocm.docs.amd.com#system-requirements-and-information)

ROCm depends on a coordinated stack of compatible firmware, driver, and user space components. Maintaining version alignment between these layers ensures expected GPU operation and performance, especially for AMD data center products. This table lists GPU details followed by supported operating systems, kernel driver, and firmware versions.

| AMD GPU series | |||||||
|---|---|---|---|---|---|---|---|
| Architecture | CDNA 4 | CDNA 3 | CDNA 2 | CDNA | |||
| LLVM target | gfx950 | gfx942 | gfx90a | gfx908 | |||
| Supported Ubuntu versions | Ubuntu 26.04 (kernel: GA 7.0) Ubuntu 24.04.4 (kernel: GA 6.8) Ubuntu 22.04.5 (kernel: GA 5.15) | Ubuntu 26.04 (kernel: GA 7.0) Ubuntu 24.04.4 (kernel: GA 6.8) | |||||
| Supported Red Hat Enterprise Linux versions | RHEL 10.2 (kernel: 6.12.0-211) RHEL 10.0 (kernel: 6.12.0-55) RHEL 9.8 (kernel: 5.14.0-687) RHEL 9.6 (kernel: 5.14.0-570) RHEL 9.4 (kernel: 5.14.0-427) RHEL 8.10 (kernel: 4.18.0-553) | RHEL 10.2 (kernel: 6.12.0-211) RHEL 9.8 (kernel: 5.14.0-687) RHEL 9.6 (kernel: 5.14.0-570) | RHEL 10.2 (kernel: 6.12.0-211) RHEL 10.0 (kernel: 6.12.0-55) RHEL 9.8 (kernel: 5.14.0-687) RHEL 9.6 (kernel: 5.14.0-570) RHEL 9.4 (kernel: 5.14.0-427) | ||||
| Supported Debian version | Debian 13 (kernel: 6.12) Debian 12 (kernel: 6.1.0) | Debian 13 (kernel: 6.12) | Debian 12 (kernel: 6.1.0) | ||||
| Supported Oracle Linux versions | Oracle Linux 10 (kernel: UEK 8.1) Oracle Linux 9 (kernel: UEK 8) | Oracle Linux 10 (kernel: UEK 8.1) Oracle Linux 9 (kernel: UEK 8) Oracle Linux 8 (kernel: UEK 7) | |||||
| Supported Rocky Linux versions | Rocky Linux 9 (kernel: 5.14.0-570) | ||||||
| Supported SUSE Linux Enterprise Server versions | SLES 16.0 (kernel: 6.12) SLES 15.7 (kernel: 6.4.0-150700.51) | SLES 15.7 (kernel: 6.4.0-150700.51) | |||||
| Supported AMD GPU Driver (amdgpu) versions | |||||||
| Supported PLDM bundle (firmware) versions | 01.26.01.03 (or later) 01.26.00.02 | BKC12.0 (IFWI PRD1000A) or later IFWI 00189939 | 01.26.01.03 (or later) 01.25.06.08 | 01.26.00.04 (or later) 01.25.06.05 | PI100D PI100C | Maintenance update (MU) 5 with IFWI 75 (or later) | VBIOS D3430401-037 |

| AMD GPU series | ||||||
|---|---|---|---|---|---|---|
| Architecture | RDNA 4 | RDNA 3 | RDNA 2 | |||
| LLVM target | gfx1201 | gfx1200 | gfx1100 | gfx1101 | gfx1102 | gfx1030 |
| Supported Ubuntu versions | Ubuntu 26.04 (kernel: GA 7.0) Ubuntu 24.04.4 (kernel: HWE 6.17) Ubuntu 22.04.5 (kernel: HWE 6.8) | |||||
| Supported RHEL versions | RHEL 10.2 (kernel: 6.12.0-211) RHEL 9.8 (kernel: 5.14.0-687) | |||||
| Supported Windows version | Windows 11 25H2 | |||||
| Supported AMD GPU Driver (amdgpu) versions | ||||||
| Supported Adrenalin Driver version | ||||||
| Supported Windows CDE CPR driver version | 26.10.32 |

| AMD APU series | ||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Graphics model (iGPU) | Radeon 8065S | Radeon 8050S | Radeon 8060S | Radeon 8040S | Radeon 890M | Radeon 880M | Radeon 860M | Radeon 840M | Radeon 820M | Radeon 780M | Radeon 760M | Radeon 740M |
| Architecture | RDNA 3.5 | RDNA 3 | ||||||||||
| LLVM target | gfx1151 | gfx1150 | gfx1152 | gfx1153 | gfx1103 | |||||||
| Codename | Gorgon Halo | Strix Halo | Gorgon Point | Strix Point | Krackan Point | Hawk Point | ||||||
| Supported Ubuntu versions | 26.04 (kernel: GA 7.0) 24.04.4 (kernel: OEM 6.17) | |||||||||||
| Supported Windows version | Windows 11 25H2 | |||||||||||
| Supported kernel driver version | Inbox kernel driver in supported Ubuntu version | |||||||||||
| Supported Adrenalin Driver version | ||||||||||||
| Supported Windows CDE CPR driver version | 26.10.32 |

For hardware specifications, see [AMD GPU specifications](https://rocm.docs.amd.com/reference/gpu-specs.html#gpu-specs).

## ROCm Core SDK components[#](https://rocm.docs.amd.com#rocm-core-sdk-components)

The following table lists core components included in the ROCm 10.0.0 release. Expect future releases in this stream to expand the list of components.

| Component group | Component name | ||||||
|---|---|---|---|---|---|---|---|
| Control and monitoring tools | |||||||
| Math and compute libraries | |||||||
| Runtimes and compilers | |||||||
| Storage libraries | |||||||
| Communication libraries | |||||||
| Profiling and debugging tools | |||||||
| Media libraries | |||||||

| Component group | Component name |
|---|---|
| Math and compute libraries | |
| Runtimes and compilers | |

## AI ecosystem compatibility[#](https://rocm.docs.amd.com#ai-ecosystem-compatibility)

ROCm 10.0.0 provides optimized support for popular deep learning frameworks and AI inference engines. The following table lists supported frameworks and libraries, their validated versions, and compatible Python versions.

| Framework | Supported versions | Python versions | |
|---|---|---|---|
| PyTorch | 2.13.0, 2.12.0, 2.11.0 | 2.13.0, 2.12.0 | 3.14, 3.13, 3.12, 3.11 |
| PyTorch | 2.13.0 | 3.14, 3.13, 3.12, 3.11 | |
| JAX | 0.11.0 | 3.14, 3.13, 3.12 | |
| 0.10.2, 0.10.0 | 3.14, 3.13, 3.12, 3.11 | ||
| vLLM | 0.27.0 | 3.14 (requires PyTorch 2.13.0) | |
| SGLang | 0.5.15 | 3.14 (requires PyTorch 2.13.0) | |
| TensorFlow | 2.21, 2.20, 2.19.1 | 3.12 | |
| MIGraphX | 2.17 | 3.14, 3.12 | |
| ONNX Runtime | 1.29.0 | 3.14, 3.12 |