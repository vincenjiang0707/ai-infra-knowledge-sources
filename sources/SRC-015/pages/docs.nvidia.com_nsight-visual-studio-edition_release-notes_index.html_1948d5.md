source: https://docs.nvidia.com/nsight-visual-studio-edition/release-notes/index.html

# Release Notes[#](https://docs.nvidia.com#release-notes)

See the latest features and updates for this version of NVIDIA Nsight Visual Studio Edition.

## New in NVIDIA Nsight Visual Studio Edition 2026.3.0[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2026-3-0)

General

Supports CUDA Toolkit 13.4.

Recommended NVIDIA Display Driver: 615.01 or newer


CUDA Debugger

Bug fixes and performance improvements.

**(Preview)**Adds support for combined CPU/GPU call stacks with the launching CPU stack frames appearing under the GPU stack frames.

Note

The CPU call stack frames are captured at kernel launch time. Because the host may continue executing asynchronously with the GPU, some frames may have already returned or diverged by the time execution breaks. For those frames, locals, registers, and watches are unavailable.


## New in NVIDIA Nsight Visual Studio Edition 2026.2.0[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2026-2-0)

General

Supports CUDA Toolkit 13.3.

Recommended NVIDIA Display Driver: 610.01 or newer


CUDA Debugger

Bug fixes and performance improvements.

Break On Launch now supports CUDA Graphs. Execution will be halted when kernels are launched by graph nodes. This applies to graphs launched from device code.

Break On Launch now supports OptiX. Execution will be halted when the raygen function is called. Please note that Shader Entry Reordering is not supported.



## New in NVIDIA Nsight Visual Studio Edition 2026.1.0[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2026-1-0)

General

Supports CUDA Toolkit 13.2.

Supports Visual Studio 2026.

Recommended NVIDIA Display Driver: 595.01 or newer


CUDA Debugger

Bug fixes and performance improvements.

Break On Launch now supports CUDA Dynamic Parallelism. Execution will be halted when kernels are launched from device code. See the

[CUDA Programming Guide](https://docs.nvidia.com/cuda/cuda-programming-guide/index.html)for more information on CUDA Dynamic Parallelism.


## NVIDIA Nsight Visual Studio Edition 2025.5.0 with Early Access Support for Microsoft Visual Studio 2026[#](https://docs.nvidia.com#nvidia-nsight-visual-studio-edition-2025-5-0-with-early-access-support-for-microsoft-visual-studio-2026)

Enables experimental, early access support for Microsoft Visual Studio 2026.

Note

**This is an early access feature and may not be fully stable.**Users are encouraged to provide feedback to help improve this feature in future releases. Refer to the[Known Issues](https://docs.nvidia.com/known-issues/index.html)page for a list of known issues.Drops support for Microsoft Visual Studio 2019.

General

Supports CUDA Toolkit 13.1.

Recommended NVIDIA Display Driver: 591.39 or newer



## New in NVIDIA Nsight Visual Studio Edition 2025.4.0[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2025-4-0)

General

Supports CUDA Toolkit 13.1.

Recommended NVIDIA Display Driver: 591.39 or newer


CUDA Debugger

Bug fixes and performance improvements.



## New in NVIDIA Nsight Visual Studio Edition 2025.3.1[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2025-3-1)

General

Supports CUDA Toolkit 13.0 Update 1.

Recommended NVIDIA Display Driver: 581.15 or newer


CUDA Debugger

Bug fixes and performance improvements.



## New in NVIDIA Nsight Visual Studio Edition 2025.3.0[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2025-3-0)

General

Supports CUDA Toolkit 13.0.

Recommended NVIDIA Display Driver: 580.88 or newer


CUDA Debugger

The legacy debugger as well as support for Maxwell, Pascal and Volta architectures, deprecated as of version 2025.1, has been dropped.

Bug fixes and performance improvements.

Known issues in CUDA debugging on Blackwell GPUs. See items 2 and 3 under

[Known Issues](https://docs.nvidia.com/known-issues/index.html)for more details.


## New in NVIDIA Nsight Visual Studio Edition 2025.2.1[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2025-2-1)

General

Supports CUDA Toolkit 12.9 Update 1.

Recommended NVIDIA Display Driver: 576.02 or newer


CUDA Debugger

Bug fixes and performance improvements.



## New in NVIDIA Nsight Visual Studio Edition 2025.2.0[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2025-2-0)

General

Supports CUDA Toolkit 12.9.

Recommended NVIDIA Display Driver: 576.02 or newer


CUDA Debugger

Support for Visual Studio 2019 has been deprecated as of version 2025.1, and will be dropped in a future release.

The legacy debugger as well as support for Maxwell, Pascal and Volta architectures has been deprecated as of version 2025.1 and will be dropped in a future release.

Bug fixes and performance improvements.



## New in NVIDIA Nsight Visual Studio Edition 2025.1.0[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2025-1-0)

General

Supports CUDA Toolkit 12.8.

Recommended NVIDIA Display Driver: 571.96 or newer

Adds support for the latest NVIDIA Blackwell GPUs, including B100, B200, GB202, and GB203.


CUDA Debugger

Support for Visual Studio 2017 which has been deprecated since 2024.2.0, has been removed in version 2025.1.0.

Support for Visual Studio 2019 is deprecated as of this release, and will be dropped in a future release.

The legacy debugger as well as support for Maxwell, Pascal and Volta architectures are being deprecated in this release and will be dropped in a future release.

Bug fixes and performance improvements.



## New in NVIDIA Nsight Visual Studio Edition 2024.4.0[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2024-4-0)

General

Non-public release for ISVs and OEMs only.

Supports CUDA Toolkit 12.7.

Recommended NVIDIA Display Driver: 565.90 or newer

Adds support for the latest NVIDIA Blackwell GPU, B100


CUDA Debugger

Bug fixes and performance improvements.



## New in NVIDIA Nsight Visual Studio Edition 2024.3.0[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2024-3-0)

General

Supports CUDA Toolkit 12.6, with recommended NVIDIA Display Driver: 560.70 or newer.

Supports CUDA Toolkit 12.6 Update 1, with recommended NVIDIA Display Driver: 560.94 or newer (There was no Nsight VSE 2024.3.1 release associated with the CTK12.6u1).

Supports CUDA Toolkit 12.6 Update 2, with recommended NVIDIA Display Driver: 560.94 or newer (There was no Nsight VSE 2024.3.2 release associated with the CTK12.6u2).


Resolved Issues

Fixed issue with MCDM driver mode debugging on Hopper GPU architectures.

r560 WDDM now generates coredumps when CUDA_ENABLE_COREDUMP_ON_EXCEPTION=1, which was an issue with the r555 driver.



## New in NVIDIA Nsight Visual Studio Edition 2024.2.1[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2024-2-1)

General

Supports CUDA Toolkit 12.5 Update 1.

Recommended NVIDIA Display Driver: 555.85 or newer


CUDA Debugger

Bug fixes and performance improvements.



## New in NVIDIA Nsight Visual Studio Edition 2024.2.0[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2024-2-0)

General

Supports CUDA Toolkit 12.5.

Recommended NVIDIA Display Driver: 555.85 or newer


CUDA Debugger

Microsoft Compute Driver Model (MCDM) is supported as of version 2024.2.0.

Support for Visual Studio 2017 has been deprecated as of version 2024.2.0 and will be dropped in a future release. Visual Studio versions 2019 and 2022 will continue to be supported.

Bug fixes and performance improvements.



## New in NVIDIA Nsight Visual Studio Edition 2024.1.1[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2024-1-1)

General

Recommended NVIDIA Display Driver: 551.82 or newer.

Supports CUDA Toolkit 12.4 Update 1.


CUDA Debugger

Bug fixes and performance improvements.



## New in NVIDIA Nsight Visual Studio Edition 2024.1.0[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2024-1-0)

General

Recommended NVIDIA Display Driver: 551.61 or newer.

Supports CUDA Toolkit 12.4.

Support for Windows Server 2019, deprecated since Nsight VSE 2023.3.0 and CTK 12.3.0, has been dropped as of 2024.1.0 and 12.4.0



CUDA Debugger

Bug fixes and performance improvements.



## New in NVIDIA Nsight Visual Studio Edition 2023.3.1[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2023-3-1)

General

Supports CUDA Toolkit 12.3 Update 1.

Recommended NVIDIA Display Driver: 545.12 or newer


CUDA Debugger

Bug fixes and performance improvements.



## New in NVIDIA Nsight Visual Studio Edition 2023.3.0[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2023-3-0)

General

Recommended NVIDIA Display Driver: 545.84 or newer

Supports CUDA Toolkit 12.3. - Supports new

[Extended Split Compilation](https://docs.nvidia.com/cuda-build-run/index.html#cuda-properties-device)NVCC compiler option, as an NVCC preview feature. - Support for Windows Server 2019 is deprecated as of CTK 12.3.0 and Nsight VSE 2023.3.0, and will be dropped in a future release.

CUDA Debugger

Added support for debugging CUDA CMake Projects with Next-gen and Legacy Debuggers.

Bug fixes and performance improvements.



## New in NVIDIA Nsight Visual Studio Edition 2023.2.2[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2023-2-2)

General

Supports CUDA Toolkit 12.2 Update 2.

Recommended NVIDIA Display Driver: 537.13 or newer


CUDA Debugger

Bug fixes and performance improvements.



## New in NVIDIA Nsight Visual Studio Edition 2023.2.1[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2023-2-1)

General

Supports CUDA Toolkit 12.2 Update 1.

Recommended NVIDIA Display Driver: 536.67 or newer


CUDA Debugger

Bug fixes and performance improvements.



## New in NVIDIA Nsight Visual Studio Edition 2023.2.0[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2023-2-0)

General

Supports CUDA Toolkit 12.2.

Recommended NVIDIA Display Driver: 36.23 or newer


CUDA Debugger

Bug fixes and performance improvements.



## New in NVIDIA Nsight Visual Studio Edition 2023.1.1[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2023-1-1)

General

Supports CUDA Toolkit 12.1 Update 1.

Recommended NVIDIA Display Driver: 531.14 or newer


CUDA Debugger

Bug fixes and performance improvements.



## New in NVIDIA Nsight Visual Studio Edition 2023.1.0[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2023-1-0)

General

Recommended NVIDIA Display Driver: 531.14 or newer

Supports CUDA Toolkit 12.1.

Supports new

[Split Compilation](https://docs.nvidia.com/cuda-build-run/index.html#cuda-properties-device)NVCC compiler option, as an NVCC preview feature.


CUDA Debugger

Bug fixes and performance improvements.



## New in NVIDIA Nsight Visual Studio Edition 2022.4.1[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2022-4-1)

General

Supports CUDA Toolkit 12.0 Update 1.

Recommended NVIDIA Display Driver: 528.33 or newer

Adds support for the latest NVIDIA GPUs, including AD104, AD106, and AD107.


CUDA Debugger

Bug fixes and performance improvements.


Important Fixes

Fixed user induced coredump issue on A100 and H100 GPUs.

Fixed issue where Registers View may show error messages for PTX registers.

Fixed issue where projects failed to build with the CUDA build customization in recent updates of Visual Studio 2022 if the project path contains a space.



## New in NVIDIA Nsight Visual Studio Edition 2022.4.0[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2022-4-0)

General

Recommended NVIDIA Display Driver: 527.27 or newer

Supports CUDA Toolkit 12.0.

While WSL2 is supported by the CUDA Toolkit 12.0, Nsight Visual Studio Edition doesn’t support debugging in the Linux subsystem.

Supports CNPv2.

Resource View now shows CUDA Stream Priority Attribute.


Adds support for the latest NVIDIA GPUs, including AD104.


CUDA Debugger

Bug fixes and performance improvements.



## New in NVIDIA Nsight Visual Studio Edition 2022.3.0[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2022-3-0)

General

Supports CUDA Toolkit 11.8.

Recommended NVIDIA Display Driver: 521.98 or newer

Adds support for the latest NVIDIA GPUs, including AD102, AD103, and GH100.

NVIDIA Tools Extension (NVTX) will not be installed by the Nsight Visual Studio installer starting with the next release. Please refer to

[https://docs.nvidia.com/nvtx](https://docs.nvidia.com/nvtx)and[NVIDIA/NVTX](https://github.com/NVIDIA/NVTX)for set up instructions.

CUDA Debugger

Supports lazy function loading, which shortens time to first breakpoint. Resource view indicates if each function has been loaded.

Bug fixes and performance improvements.



## New in NVIDIA Nsight Visual Studio Edition 2022.2.1[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2022-2-1)

General

Supports CUDA Toolkit 11.7 Update 1.

Recommended NVIDIA Display Driver: 516.31 or newer



## New in NVIDIA Nsight Visual Studio Edition 2022.2.0[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2022-2-0)

General

Supports CUDA Toolkit 11.7.

Recommended NVIDIA Display Driver: 516.01 or newer

Adds support for the latest NVIDIA Ampere GPUs, including GA103.



## New in NVIDIA Nsight Visual Studio Edition 2022.1.1[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2022-1-1)

General

New support for Visual Studio 2022, in addition to previous support for VS2017 and VS2019.

Recommended NVIDIA Display Driver: 511.23 or newer


CUDA Debugger

System Info window is not available when using Visual Studio 2022.

Core dump files (.nvcudmp) are not recognized when using Visual Studio 2022.



## New in NVIDIA Nsight Visual Studio Edition 2022.1.0[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2022-1-0)

General

Supports CUDA Toolkit 11.6.

Recommended NVIDIA Display Driver: 511.23 or newer


CUDA Debugger

Improved coredump and exception handling.

Bug fixes and performance improvements.



## New in NVIDIA Nsight Visual Studio Edition 2021.3.1[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2021-3-1)

General

Supports CUDA Toolkit 11.5 Update 1.

Recommended NVIDIA Display Driver: 495.01 or newer


CUDA Debugger

Next-Gen Debugger supports the latest compiler enhancements in CUDA Toolkit 11.5 Update 1, improving optimized code debugging.

Bug fixes and performance improvements.



## New in NVIDIA Nsight Visual Studio Edition 2021.3.0[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2021-3-0)

General

Supports CUDA Toolkit 11.5.

Recommended NVIDIA Display Driver: 495.00 or newer

Supports Microsoft Windows 11.


CUDA Debugger

Bug fixes and performance improvements.



## New in NVIDIA Nsight Visual Studio Edition 2021.2.1[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2021-2-1)

General

Supports CUDA Toolkit 11.4 Update 1.

Recommended NVIDIA Display Driver: 471.41 or newer


CUDA Debugger

Bug fixes and performance improvements.



## New in NVIDIA Nsight Visual Studio Edition 2021.2.0[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2021-2-0)

General

Supports CUDA Toolkit 11.4.

Recommended NVIDIA Display Driver: 471.11 or newer


CUDA Debugger

Next-Gen Debugger supports the latest compiler enhancements in CUDA Toolkit 11.4, improving optimized code debugging.

Bug fixes and performance improvements.



## New in NVIDIA Nsight Visual Studio Edition 2021.1.1[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2021-1-1)

General

Supports CUDA Toolkit 11.3 Update 1.

Recommended NVIDIA Display Driver: 465.01 or newer


CUDA Debugger

Bug fixes and performance improvements.



## New in NVIDIA Nsight Visual Studio Edition 2021.1.0[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2021-1-0)

General

Supports the latest NVIDIA Ampere GPUs, including GA106.

Supports CUDA Toolkit 11.3.

Recommended NVIDIA Display Driver: 465.00 or newer


CUDA Debugger

Allow viewing of SASS Indexed Constants.

Added Memory Allocations to the Resources view.

Bug fixes and performance improvements.



## New in NVIDIA Nsight Visual Studio Edition 2020.3.1[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2020-3-1)

General

Supports CUDA Toolkit 11.2 Update 1.

Recommended NVIDIA Display Driver: 460.79 or newer


CUDA Debugger

Bug fixes and performance improvements.



## New in NVIDIA Nsight Visual Studio Edition 2020.3.0[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2020-3-0)

General

Supports CUDA Toolkit 11.2.

Recommended NVIDIA Display Driver: 460.78 or newer

Support for Visual Studio 2015, which has been deprecated since 2020.2.0, has been removed. Current Visual Studio support still includes versions 2017 and 2019.


CUDA Debugger

Supports CUDA Parallel Launch.

Supports Visual Studio breakpoint hit count.

New Memory Allocations view, providing information on CUDA global memory allocations.



## New in NVIDIA Nsight Visual Studio Edition 2020.2.1[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-edition-2020-2-1)

General

Supports CUDA Toolkit 11.1 Update 1.

Recommended NVIDIA Display Driver: 457.09 or newer


Important Fixes

Some builds of Visual Studio 2019 had performance impacts when Nsight Visual Studio Edition 2020.2.0 was installed (possibly from CUDA Toolkit 11.1).



## New in NVIDIA Nsight Visual Studio 2020.2.0[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-2020-2-0)

General

Support for GA102 and GA104.

Support CUDA Toolkit 11.1.

Recommended NVIDIA Display Driver: 456.33 or newer

Support for Microsoft Windows 10 Hardware Scheduling.

Support for Visual Studio 2015 is being deprecated and will be dropped in an upcoming release. Current Visual Studio support still includes versions 2015, 2017, and 2019.


CUDA Debugger

Debugger Performance improvements, especially when loading modules.

New debugger option to ‘Break on API Errors’.

New debugger option to ‘Break on Launch’.


Analysis

Integrated

**Analysis Trace**, deprecated since NVIDIA Nsight Visual Studio Edition 2019.2, has been removed. The replacement, stand-alone[Nsight Systems](http://developer.nvidia.com/nsight-systems)tool is currently available and works with[NVIDIA Nsight Integration](https://developer.nvidia.com/nsight-tools-visual-studio-integration)for Visual Studio.


## New in NVIDIA Nsight Visual Studio 2020.1.2[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-2020-1-2)

This was a bug fix release, primarily for fixing Debugger core dump issues.

Recommended NVIDIA Display Driver: 451.82 or newer.


## New in NVIDIA Nsight Visual Studio 2020.1.1[#](https://docs.nvidia.com#new-in-nvidia-nsight-visual-studio-2020-1-1)

General

Support for GA100.

Supports CUDA Toolkit 11.0

Recommended NVIDIA Display Driver: 451.48 or newer

Support for Microsoft Windows 10 Hardware Scheduling.

Windows 7 (and WinServer through 2012R2) support, deprecated since 2019.4 release, has been removed.

Support for sm_30 and sm_32 architectures have been dropped and sm_35, sm_37, sm_50 support has been deprecated as of the 2020.1 release. The default compilation target is now sm_52 in NVIDIA Nsight™ VSE build customizations. (CTK-865)

Support for Visual Studio 2013 has been dropped. NVIDIA Nsight™ VSE 2020.1.1 Visual Studio support includes versions 2015, 2017, and 2019.

[NVIDIA Nsight Integration](https://developer.nvidia.com/nsight-tools-visual-studio-integration), a Visual Studio extension, has been introduced to allow next generation, standalone, Nsight tool integration into Visual Studio. In particular:Integrated

**Graphics Debugging**, deprecated since NVIDIA Nsight Visual Studio Edition 2019.2, has been removed and replaced by[Nsight Graphics](https://developer.nvidia.com/nsight-graphics).Integrated

**CUDA profiling**, deprecated since NVIDIA Nsight Visual Studio Edition 2019.2, has been removed from the Performance Analysis tools and replaced by:[Nsight Compute](https://developer.nvidia.com/nsight-compute)for Volta and later family GPUs[nvprof](https://docs.nvidia.com/cuda/profiler-users-guide/index.html#nvprof-overview)and[Visual Profiler](https://developer.nvidia.com/nvidia-visual-profiler)for Pascal and early family GPUs (not participating tools for NVIDIA Nsight Integration)

Integrated

**Analysis Trace**, deprecated since NVIDIA Nsight Visual Studio Edition 2019.2, has not been removed, but will be in an upcoming release of NVIDIA Nsight™ VSE. The replacement, stand-alone[Nsight Systems](http://developer.nvidia.com/nsight-systems)tool is currently available and works with[NVIDIA Nsight Integration](https://developer.nvidia.com/nsight-tools-visual-studio-integration)for Visual Studio.


CUDA Debugger

Added support for the NVIDIA GA100 GPU.

Supports for the CUDA 11.0 Toolkit.

Added ability to control breaking on and reporting CUDA API errors.

The Warp Watch view is now available in the Next-Gen Nsight Debugger.

The Resources view is now available in the Next-Gen Nsight Debugger.

CUDA Task Graph support has been added to the Next-Gen Nsight Debugger.

Support for Pascal has been dropped from the Legacy Nsight Debugger, but is fully supported by the Next-Gen Nsight Debugger.


Graphics

Integrated

**Graphics Debugging**, deprecated since NVIDIA Nsight Visual Studio Edition 2019.2, has been removed and replaced by[Nsight Graphics](https://developer.nvidia.com/nsight-graphics).Note that

[NVIDIA Nsight Integration](https://developer.nvidia.com/nsight-tools-visual-studio-integration), a Visual Studio extension, has been introduced to allow[Nsight Graphics](https://developer.nvidia.com/nsight-graphics)integration into Visual Studio under the Nsight menu.

Analysis

Integrated

**CUDA profiling**, deprecated since NVIDIA Nsight Visual Studio Edition 2019.2, has been removed from the Performance Analysis tools and replaced by:[Nsight Compute](https://developer.nvidia.com/nsight-compute)for Volta and later family GPUs.Note that

[NVIDIA Nsight Integration](https://developer.nvidia.com/nsight-tools-visual-studio-integration), a Visual Studio extension, has been introduced to allow[Nsight Compute](https://developer.nvidia.com/nsight-compute)integration into Visual Studio under the Nsight menu.[nvprof](https://docs.nvidia.com/cuda/profiler-users-guide/index.html#nvprof-overview)and[Visual Profiler](https://developer.nvidia.com/nvidia-visual-profiler)for Pascal and earlier family GPUs (not participating tools for NVIDIA Nsight Integration).

Integrated

**Analysis Trace**, which has been deprecated since NVIDIA Nsight Visual Studio Edition 2019.2, has not been removed, but will be in an upcoming release of NVIDIA Nsight™ VSE. However, the replacement, stand-alone[Nsight Systems](http://developer.nvidia.com/nsight-systems)tool is currently available and works with[NVIDIA Nsight Integration](https://developer.nvidia.com/nsight-tools-visual-studio-integration)for Visual Studio integration.OpenCL profiling support in NVIDIA Nsight Visual Studio Edition, deprecated as of NVIDIA Nsight™ VSE 2019.3, has been removed.