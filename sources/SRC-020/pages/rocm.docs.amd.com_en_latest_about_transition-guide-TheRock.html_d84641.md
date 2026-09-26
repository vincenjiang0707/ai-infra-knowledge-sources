source: https://rocm.docs.amd.com/en/latest/about/transition-guide-TheRock.html

# Transition guide from legacy ROCm release stream[#](https://rocm.docs.amd.com#transition-guide-from-legacy-rocm-release-stream)

The [ROCm Core SDK](https://rocm.docs.amd.com/en/latest/index.html#rocm-core-sdk) is built on TheRock, AMD’s new build system. The transition from the legacy ROCm release stream began with [ROCm Core SDK 7.14.0](https://rocm.docs.amd.com/en/docs-7.14.0/about/release-notes.html), the first production release. [ROCm 10.0.0](https://rocm.docs.amd.com/en/latest/about/release-notes.html) is the latest production release. For more on the transition, see [ROCm 7.14: TheRock Goes Production and Expands AMD’s AI Software Platform](https://rocm.blogs.amd.com/ecosystems-and-partners/rocm-7.14-blog/README.html).

## Major changes[#](https://rocm.docs.amd.com#major-changes)

| Feature | ROCm Core SDK | ROCm legacy | Description |
|---|---|---|---|
| Installation directory | `/opt/rocm/core-10.0` |
`/opt/rocm-7.2/` |
To support additional release streams downstream of the ROCm Core SDK. |
| Package names | `amdrocm-{component}` |
`rocm-[$component]` or `roc[$component]` or `hip[$component]` |
Unique package prefix to avoid conflicts with upstream packages. |
| Extras directory | `/opt/rocm/extras-10/` |
N/A | Shared install prefix scoped to each ROCm major version for projects built on the ROCm Core SDK. |

## Paths and linking[#](https://rocm.docs.amd.com#paths-and-linking)

For installations using your
Linux distribution’s package manager, the `amdrocm`

meta package configures
`update-alternatives`

and provides backward-compatible symlinks for
`/opt/rocm/bin`

, `/opt/rocm/lib`

, and other `/opt/rocm/`

directories.

## Installation formats[#](https://rocm.docs.amd.com#installation-formats)

ROCm Core SDK is available in the following distribution formats. For step-by-step installation instructions, see [Install ROCm](https://rocm.docs.amd.com/install/rocm.html).

| Format | Details |
|---|---|
DEB / RPM packages |
System-wide install through your package manager (`apt` , `dnf` , or `yum` ). The most familiar install path on a managed Linux system. Available from
|
Tarball archives |
Self-contained install that requires neither root nor a package manager, suited to HPC module systems and custom install locations. Archives follow the naming convention `therock-dist-linux-{FAMILY}-{VERSION}.tar.gz` (for example, `therock-dist-linux-gfx110X-all-{VERSION}.tar.gz` ). For the `{FAMILY}` value for your GPU, see
Extract to any directory, then set `PATH` , `LD_LIBRARY_PATH` , and `ROCM_PATH` to point to the extracted location (default: `/opt/rocm/core` ). Tarballs don't create symlinks or resolve dependencies.Available from
|
Python wheels |
Install ROCm libraries directly into a virtual environment with `pip` , for Python-only workflows. Use the ROCm Python package index:`python -m pip install --index-url <ROCm-package-index> "rocm[libraries,devel]"` Framework wheels such as PyTorch, JAX, and vLLM are distributed separately. |
Runfile installer |
Single-file guided installer with interactive and silent modes. Supports a custom install directory, automatic GPU detection, and optional driver installation. Use it when you want neither a package manager nor manual tarball extraction. |

### Choosing a format[#](https://rocm.docs.amd.com#choosing-a-format)

If you need… |
Use |
|---|---|
Automatic updates and dependency tracking on bare metal |
|
A non-root install or multiple ROCm versions side by side |
|
Only the Python interface to GPU-accelerated libraries in a virtual environment |
|
A guided install without a package manager |
|

## Software packages[#](https://rocm.docs.amd.com#software-packages)

ROCm Core SDK packages are more consolidated than the legacy ROCm release
stream. For example, hipBLAS and rocBLAS are now combined into one package,
`amdrocm-blas`

. The table below lists new packages, their contents, and the
corresponding legacy packages.

### Linux packages available in ROCm 10.0.0[#](https://rocm.docs.amd.com#linux-packages-available-in-rocm-10-0-0)

| ROCm Core SDK package | Package contents | ROCm legacy package |
|---|---|---|
| amdrocm-amdsmi | amd-smi | amd-smi-lib, rocm-smi-lib |
| amdrocm-llvm | amdclang++, hipcc, flang | rocm-llvm, rocm-llvm-dev, Fortran compiler (included in rocm-llvm OpenMP runtime) |
| amdrocm-runtime | HIP, ROCR, runtime compilation | hip-runtime-amd, rocm-hip-runtime, rocm-language-runtime, hsa-rocr, comgr |
| amdrocm-fft | rocFFT, hipFFT, hipFFTW | rocfft, hipfft |
| amdrocm-blas | rocBLAS, hipBLAS, hipBLASLt, hipSPARSELt | rocblas, hipblas, hipblaslt, hipsparselt |
| amdrocm-sparse | rocSPARSE, hipSPARSE | rocsparse, hipsparse |
| amdrocm-solver | rocSOLVER, hipSOLVER | rocsolver, hipsolver, rocalution |
| amdrocm-dnn | hipDNN, MIOpen | miopen-hip |
| amdrocm-rand | rocRAND, hipRAND | rocrand, hiprand |
| amdrocm-ccl | rocPRIM, rocThrust, hipCUB | rocprim, rocthrust, hipcub, rocwmma |
| amdrocm-profiler | rocprofiler-systems, rocprofiler-compute, rocprofiler-sdk, roctracer | rocprofiler, rocprofiler-compute, rocprofiler-systems, rocprofiler-sdk, roctracer |
| amdrocm-profiler-base | rocprofiler-sdk, roctracer | rocprofiler-register, roctracer, hsa-amd-aqlprofile |
| amdrocm-base | rocminfo, rocm-core | rocm-core, rocminfo, rocm-cmake, half |
| amdrocm-ck | Composable Kernel | composablekernel |
| amdrocm-debugger | rocgdb, ROCdbgapi, ROCR Debug Agent | rocm-gdb, rocm-dbgapi, rocm-debug-agent |
| amdrocm-hipify | HIPIFY | hipify-clang |
| amdrocm-opencl | OpenCL runtime and ICD loader | rocm-opencl-runtime, rocm-opencl, hip-opencl |
| amdrocm-decode | rocDecode (newly included in the ROCm Core SDK) | rocdecode |
| amdrocm-jpeg | rocJPEG (newly included in the ROCm Core SDK) | rocjpeg |
| amdrocm-rccl | rccl | rccl |
| amdrocm-rocshmem | rocSHMEM | rocshmem |
| amdrocm-rdc | ROCm Data Center Tool (newly included in the ROCm Core SDK) | rdc |
| amdrocm-sysdeps | Bundled third-party dependencies (libdrm, libelf, numa, libVA) | System dependencies |

Packages are offered in the following variants:

**For all supported GPUs:**Works across all GPUs supported by ROCm (for example,`apt install amdrocm-core-sdk10.0`

).**For a specific GPU architecture:**Smaller install size, but requires you to know the GPU installed in your system (for example,`apt install amdrocm-core-sdk10.0-gfx110x`

).

Installing all GPU architectures is not required. You can install packages for a specific architecture, multiple architectures side by side, or all supported GPU architectures.

When redistributing software built on the ROCm Core SDK (for example, in container images), choose the all-architecture variant for broad hardware support. If disk footprint is a concern, use a single-architecture variant instead.

### Architecture-specific packages available in ROCm 10.0.0[#](https://rocm.docs.amd.com#architecture-specific-packages-available-in-rocm-10-0-0)

Tarball archives use *family* names that differ from the deb/rpm package suffixes. The **Tarball family name** column maps each package suffix to its corresponding tarball family.

| Architecture family | Package suffix | Tarball family name | Product name (not exhaustive) |
|---|---|---|---|
| CDNA4 | -gfx950 | gfx950-dcgpu | AMD Instinct MI355X / MI350X |
| CDNA3 | -gfx942 | gfx94X-dcgpu | AMD Instinct MI325X / MI300X / MI300A |
| CDNA2 | -gfx90a | gfx90a | AMD Instinct MI250X / MI250 / MI210 |
| CDNA | -gfx908 | — | AMD Instinct MI100 |
| RDNA4 | -gfx1200 -gfx1201 |
gfx120X-all | AMD Radeon RX 9070 / AMD Radeon RX 9060 / AMD Radeon RX 9070 XT / AMD Radeon RX 9060 XT / AMD Radeon RX 9070 GRE / AMD Radeon AI PRO R9700S / AMD Radeon AI PRO R9700 / AMD Radeon AI PRO R9600D / AMD Radeon RX 9060 XT LP |
| RDNA3.5 | -gfx1150 -gfx1151 -gfx1152 |
— | AMD Ryzen AI 9 465 / AMD Ryzen AI 9 365 / AMD Ryzen AI 9 HX 475 / AMD Ryzen AI 9 HX 470 / AMD Ryzen AI 9 HX 375 / AMD Ryzen AI 9 HX 370 / AMD Ryzen AI 9 PRO 465 / AMD Ryzen AI 9 PRO HX 475 / AMD Ryzen AI 9 PRO HX 470 / AMD Ryzen AI 9 HX PRO 375 / AMD Ryzen AI 9 HX PRO 370 / AMD Ryzen AI Max 390 / AMD Ryzen AI Max 385 / AMD Ryzen AI Max+ 395 / AMD Ryzen AI Max+ 392 / AMD Ryzen AI Max+ 388 / AMD Ryzen AI Max PRO 390 / AMD Ryzen AI Max PRO 385 / AMD Ryzen AI Max PRO 380 / AMD Ryzen AI Max+ PRO 395 / AMD Ryzen AI 7 450 / AMD Ryzen AI 7 350 / AMD Ryzen AI 7 345 / AMD Ryzen AI 5 340 / AMD Ryzen AI 5 330 / AMD Ryzen AI 7 PRO 450 / AMD Ryzen AI 5 PRO 440 / AMD Ryzen AI 7 PRO 350 / AMD Ryzen AI 5 PRO 340 |
| RDNA3 | -gfx1100 -gfx1101 -gfx1102 -gfx1103 |
gfx110X-all | AMD Radeon RX 7700 / AMD Radeon RX 7600 / AMD Radeon PRO V710 / AMD Radeon PRO W7900 / AMD Radeon PRO W7800 / AMD Radeon PRO W7700 / AMD Radeon RX 7900 XT / AMD Radeon RX 7800 XT / AMD Radeon RX 7700 XT / AMD Radeon RX 7700 XE / AMD Radeon RX 7900 XTX / AMD Radeon RX 7900 GRE / AMD Radeon PRO W7800 48GB / AMD Radeon PRO W7900 Dual Slot |
| RDNA2 | -gfx1030 | — | AMD Radeon PRO V620 / AMD Radeon PRO W6800 |

## ROCm Core SDK component changes (moved or removed)[#](https://rocm.docs.amd.com#rocm-core-sdk-component-changes-moved-or-removed)

### Planned for future releases[#](https://rocm.docs.amd.com#planned-for-future-releases)

ROCm Core SDK: RPP

ROCm-Extras: hipfort, rocPyDecode, rocAL, MIVisionX


### Moved to ROCm-Extras[#](https://rocm.docs.amd.com#moved-to-rocm-extras)

ROCm Validation Suite

TransferBench

ROCm Optiq


### Moved to Standalone/ONNX[#](https://rocm.docs.amd.com#moved-to-standalone-onnx)

ONNX runtime


### Removed[#](https://rocm.docs.amd.com#removed)

[ROCm SMI](https://rocm.docs.amd.com/en/latest/about/release-notes.html#rocm-smi-deprecation)(replaced by AMD SMI)ROCm Bandwidth Test (end-of-life as of the TheRock-based ROCm 7.14.0 release; use TransferBench or RVS instead)


## Notable package relocations[#](https://rocm.docs.amd.com#notable-package-relocations)

rocMLIR (now included in MIGraphX)

HIPCC (now included in

`amdrocm-llvm`

)FLANG (now included in

`amdrocm-llvm`

)ROCm CMake (now in

`amdrocm-base`

)ROCTracer (now in

`amdrocm-profiler-base`

)ROCProfiler (functionality in

`amdrocm-profiler`

)

## Components available in the ROCm Core SDK, ROCm-Extras, and Standalone/ONNX[#](https://rocm.docs.amd.com#components-available-in-the-rocm-core-sdk-rocm-extras-and-standalone-onnx)

| Category | Present | Absent/Moved | |
|---|---|---|---|
ROCm Core SDK |
Math and compute libraries | CK, hipBLAS, hipBLASLt, hipCUB, hipFFT, hipRAND, hipSOLVER, hipSPARSE/SPARSELt, MIOpen, rocBLAS, rocFFT, rocRAND, rocSOLVER, rocSPARSE, rocPRIM, rocThrust, rocWMMA | hipfort, rocALUTION |
| Communication libraries | RCCL, rocSHMEM | — | |
| Media libraries | rocDecode, rocJPEG, ROCm Performance Primitives (RPP planned for a future release) | rocPyDecode, rocAL, MIVisionX, MIGraphX, CK (moved to math and compute) | |
| Storage libraries | hipFile | — | |
| Runtime, compilers, build tools | HIP, HIPIFY, LLVM | HIPCC (moved to `amdrocm-llvm` ), FLANG (moved to `amdrocm-llvm` ), ROCm CMake (moved to `amdrocm-base` ) |
|
| Profiling and debugging tools | ROCm Compute Profiler, ROCm Systems Profiler, ROCprofiler-SDK, ROCdbgapi, ROCm Debugger, ROCR Debug Agent | ROCTracer (moved to `amdrocm-profiler-base` ), ROCProfiler (functionality moved to `amdrocm-profiler` ) |
|
| Control and monitoring tools | AMD SMI, ROCm Data Center Tool, rocminfo | ROCm SMI (removed), ROCm Validation Suite, ROCm Bandwidth Test (removed) | |
ROCm Extras |
— | ROCm Validation Suite, TransferBench, ROCm Optiq | — |
Standalone/ONNX |
— | rocMLIR, ONNX runtime | — |