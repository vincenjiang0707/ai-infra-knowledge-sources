source: https://rocm.docs.amd.com/en/docs-7.2.4/about/release-notes.html

# ROCm 7.2.4 release notes[#](https://rocm.docs.amd.com#rocm-7-2-4-release-notes)

2026-05-29

11 min read time

ROCm 7.2.4 is a quality release focused on performance and stability fixes for AI inference workloads on AMD Instinct GPUs.

## Release highlights[#](https://rocm.docs.amd.com#release-highlights)

The following are the notable changes in ROCm 7.2.4.

### Reduced hipGraphLaunch latency for multi-list graphs[#](https://rocm.docs.amd.com#reduced-hipgraphlaunch-latency-for-multi-list-graphs)

The HIP runtime’s graph dispatch mechanism has been optimized, reducing launch latency for workloads using `hipGraphLaunch`

with multi-list graph topologies.

### Fixed H2D memory copy latency regression in CPX mode[#](https://rocm.docs.amd.com#fixed-h2d-memory-copy-latency-regression-in-cpx-mode)

HIP runtime synchronization behavior has been corrected on AMD Instinct MI300 Series GPUs in CPX mode, restoring latency to previous levels for inference workloads that run multiple HIP streams with concurrent memory copies.

### Reduced ROCprofiler-SDK profiling overhead[#](https://rocm.docs.amd.com#reduced-rocprofiler-sdk-profiling-overhead)

Profiling stability has been improved for vLLM workloads traced with PyTorch `torch.profiler`

using the ROCprofiler-SDK backend. The large, sporadic idle gaps that previously appeared between GPU kernels in the trace have been substantially reduced in common configurations, and the traces now more accurately reflect actual runtime behavior. Coverage may vary depending on model and parallelism settings.

### Reduced copy overhead in MIGraphX concat operations[#](https://rocm.docs.amd.com#reduced-copy-overhead-in-migraphx-concat-operations)

MIGraphX now recognizes ONNX models that concatenate the same tensor multiple times and avoids redundant device-side copies, improving inference throughput at small batch sizes for the affected model class on AMD Instinct MI300X GPUs.

### User space, driver, and firmware dependent changes[#](https://rocm.docs.amd.com#user-space-driver-and-firmware-dependent-changes)

The software for AMD Data Center GPU products requires maintaining a hardware and software stack with interdependencies among the GPU and baseboard firmware, AMD GPU drivers, and the ROCm user space software. While AMD publishes drivers and ROCm user space components, your server or infrastructure provider publishes the GPU and baseboard firmware by bundling AMD’s firmware releases via the AMD Platform Level Data Model (PLDM) bundle, which includes the Integrated Firmware Image (IFWI).

GPU and baseboard firmware versioning might differ across GPU families.

|
ROCm Version |
GPU |
PLDM Bundle (Firmware) |
AMD GPU Driver (amdgpu) |
AMD GPU |
|---|---|---|---|---|
| ROCm 7.2.4 | MI355X |
01.26.00.02 01.25.17.07 01.25.16.03 |
30.30.x where x (0-4) 30.20.x where x (0-1) 30.10.x where x (0-2) |
8.7.1.K |
| MI350X |
01.26.00.02 01.25.17.07 01.25.16.03 |
30.30.x where x (0-4) 30.20.x where x (0-1) 30.10.x where x (0-2) |
||
| MI325X
[1] |

01.25.04.02

30.20.x where x (0-1)

[1]30.10.x where x (0-2)

6.4.z where z (0-3)

6.3.3

[2]01.25.03.12

01.25.02.04

30.20.x where x (0-1)

30.10.x where x (0-2)

6.4.z where z (0–3)

6.3.3

[1]: For AMD Instinct MI325X KVM SR-IOV users, don't use AMD GPU driver (amdgpu) 30.20.0.

[2]: AMD Instinct MI300X KVM SR-IOV with Multi-VF (8 VF) support requires a compatible firmware BKC bundle, which will be released in the coming months.

Note

ROCm 7.2.4 doesn’t include any other significant changes or feature additions. For comprehensive changes, new features, and enhancements in ROCm 7.2.3, refer to the [ROCm 7.2.3 release notes](https://rocm.docs.amd.com#rocm-7-2-3-release-notes) below.

## ROCm 7.2.3 release notes[#](https://rocm.docs.amd.com#rocm-7-2-3-release-notes)

The release notes provide a summary of notable changes since the previous ROCm release.

Note

If you’re using AMD Radeon™ GPUs or Ryzen™ for graphics workloads, see the [Use ROCm on Radeon and Ryzen](https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/index.html) documentation to verify compatibility and system requirements.

### Release highlights[#](https://rocm.docs.amd.com#id1)

The following are notable new features and improvements in ROCm 7.2.3. For changes to individual components, see
[Detailed component changes](https://rocm.docs.amd.com#detailed-component-changes).

#### Supported hardware, operating system, and virtualization changes[#](https://rocm.docs.amd.com#supported-hardware-operating-system-and-virtualization-changes)

Hardware, operating system, and virtualization support remains unchanged in this release.

For more information about:

AMD hardware, see

[Supported GPUs (Linux)](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.3/reference/system-requirements.html#supported-gpus).Operating systems, see

[Supported operating systems](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.3/reference/system-requirements.html#supported-operating-systems)and[ROCm installation for Linux](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.3/).Virtualization support, see

[Virtualization support](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.3/reference/system-requirements.html#virtualization-support).

#### User space, driver, and firmware dependent changes[#](https://rocm.docs.amd.com#id2)

The software for AMD Data Center GPU products requires maintaining a hardware and software stack with interdependencies among the GPU and baseboard firmware, AMD GPU drivers, and the ROCm user space software. While AMD publishes drivers and ROCm user space components, your server or infrastructure provider publishes the GPU and baseboard firmware by bundling AMD’s firmware releases via the AMD Platform Level Data Model (PLDM) bundle, which includes the Integrated Firmware Image (IFWI).

GPU and baseboard firmware versioning might differ across GPU families.

|
ROCm Version |
GPU |
PLDM Bundle (Firmware) |
AMD GPU Driver (amdgpu) |
AMD GPU |
|---|---|---|---|---|
| ROCm 7.2.3 | MI355X |
01.26.00.02 01.25.17.07 01.25.16.03 |
30.30.x where x (0-3) 30.20.x where x (0-1) 30.10.x where x (0-2) |
8.7.1.K |
| MI350X |
01.26.00.02 01.25.17.07 01.25.16.03 |
30.30.x where x (0-3) 30.20.x where x (0-1) 30.10.x where x (0-2) |
||
| MI325X
[1] |

01.25.04.02

30.20.x where x (0-1)

[1]30.10.x where x (0-2)

6.4.z where z (0-3)

6.3.3

[2]01.25.03.12

01.25.02.04

30.20.x where x (0-1)

30.10.x where x (0-2)

6.4.z where z (0–3)

6.3.3

[1]: For AMD Instinct MI325X KVM SR-IOV users, don't use AMD GPU driver (amdgpu) 30.20.0.

[2]: AMD Instinct MI300X KVM SR-IOV with Multi-VF (8 VF) support requires a compatible firmware BKC bundle, which will be released in the coming months.

#### Improved profiling accuracy for vLLM workloads[#](https://rocm.docs.amd.com#improved-profiling-accuracy-for-vllm-workloads)

ROCm 7.2.3 improves profiling stability for vLLM workloads traced with PyTorch `torch.profiler`

. The large, sporadic idle gaps that previously appeared between GPU kernels in the trace have been substantially reduced in common configurations, and the traces now more accurately reflect actual runtime behavior. Coverage may vary depending on model and parallelism settings; additional improvements are in progress.

#### MIGraphX update[#](https://rocm.docs.amd.com#migraphx-update)

[MIGraphX](https://rocm.docs.amd.com/projects/AMDMIGraphX/en/docs-7.2.3/index.html) has the following enhancements:

##### Improved performance of the Gather operator[#](https://rocm.docs.amd.com#improved-performance-of-the-gather-operator)

Performance for embedding‑heavy inference workloads is improved by merging multiple independent gather operations from similar embedding tables into a single batched operation. Multi‑gather workloads now run more efficiently with fewer kernel launches and reduced memory traffic by adding horizontal fusion for cross-embedding gather operators. These gather operators have been updated to use `transpose`

/`reshape`

/`broadcast`

/`slice`

, enabling better optimization across different backends and data layouts.

##### ONNX Runtime reliability improvement[#](https://rocm.docs.amd.com#onnx-runtime-reliability-improvement)

ONNX Runtime workloads accelerated with MIGraphX now provide a more reliable experience through external stream support in the MIGraphX Execution Provider, with improved memory allocation and deallocation for multi-stream inference.

#### ROCm documentation updates[#](https://rocm.docs.amd.com#rocm-documentation-updates)

ROCm documentation has been updated with ROCm XIO documentation. ROCm XIO provides an API for Accelerator-Initiated IO (XIO) for an AMD GPU `__device__`

code. It enables AMD GPUs to perform direct IO operations to hardware devices without CPU intervention. ROCm XIO was initially released in April 2026 as an early-access software technology preview. Running production workloads is not recommended.
For more information, see the [ROCm XIO documentation](https://rocm.docs.amd.com/projects/rocm-xio/en/beta-0.1.0/index.html) and [ROCm/rocm-xio](https://github.com/ROCm/rocm-xio) GitHub repository.

### ROCm components[#](https://rocm.docs.amd.com#rocm-components)

The following table lists the versions of ROCm components for ROCm 7.2.3, including any version changes from 7.2.2/7.2.1 to 7.2.3. Click the component’s updated version to go to a list of its changes.

Click to go to the component’s source code on GitHub.

| Category | Group | Name | Version | |
|---|---|---|---|---|
| Libraries | Machine learning and computer vision |
|

[MIGraphX](https://rocm.docs.amd.com/projects/AMDMIGraphX/en/docs-7.2.3/index.html)[2.15.0](https://rocm.docs.amd.com#migraphx-2-15-0)[MIOpen](https://rocm.docs.amd.com/projects/MIOpen/en/docs-7.2.3/index.html)[MIVisionX](https://rocm.docs.amd.com/projects/MIVisionX/en/docs-7.2.3/index.html)[rocAL](https://rocm.docs.amd.com/projects/rocAL/en/docs-7.2.3/index.html)[rocDecode](https://rocm.docs.amd.com/projects/rocDecode/en/docs-7.2.3/index.html)[rocJPEG](https://rocm.docs.amd.com/projects/rocJPEG/en/docs-7.2.3/index.html)[rocPyDecode](https://rocm.docs.amd.com/projects/rocPyDecode/en/docs-7.2.3/index.html)[RPP](https://rocm.docs.amd.com/projects/rpp/en/docs-7.2.3/index.html)[RCCL](https://rocm.docs.amd.com/projects/rccl/en/docs-7.2.3/index.html)[rocSHMEM](https://rocm.docs.amd.com/projects/rocSHMEM/en/docs-7.1.0/index.html)[hipBLAS](https://rocm.docs.amd.com/projects/hipBLAS/en/docs-7.2.3/index.html)[hipBLASLt](https://rocm.docs.amd.com/projects/hipBLASLt/en/docs-7.2.3/index.html)[hipFFT](https://rocm.docs.amd.com/projects/hipFFT/en/docs-7.2.3/index.html)[hipfort](https://rocm.docs.amd.com/projects/hipfort/en/docs-7.2.3/index.html)[hipRAND](https://rocm.docs.amd.com/projects/hipRAND/en/docs-7.2.3/index.html)[hipSOLVER](https://rocm.docs.amd.com/projects/hipSOLVER/en/docs-7.2.3/index.html)[hipSPARSE](https://rocm.docs.amd.com/projects/hipSPARSE/en/docs-7.2.3/index.html)[hipSPARSELt](https://rocm.docs.amd.com/projects/hipSPARSELt/en/docs-7.2.3/index.html)[rocALUTION](https://rocm.docs.amd.com/projects/rocALUTION/en/docs-7.2.3/index.html)[rocBLAS](https://rocm.docs.amd.com/projects/rocBLAS/en/docs-7.2.3/index.html)[rocFFT](https://rocm.docs.amd.com/projects/rocFFT/en/docs-7.2.3/index.html)[rocRAND](https://rocm.docs.amd.com/projects/rocRAND/en/docs-7.2.3/index.html)[rocSOLVER](https://rocm.docs.amd.com/projects/rocSOLVER/en/docs-7.2.3/index.html)[rocSPARSE](https://rocm.docs.amd.com/projects/rocSPARSE/en/docs-7.2.3/index.html)[rocWMMA](https://rocm.docs.amd.com/projects/rocWMMA/en/docs-7.2.3/index.html)[Tensile](https://rocm.docs.amd.com/projects/Tensile/en/docs-7.2.3/src/index.html)[hipCUB](https://rocm.docs.amd.com/projects/hipCUB/en/docs-7.2.3/index.html)[hipTensor](https://rocm.docs.amd.com/projects/hipTensor/en/docs-7.2.3/index.html)[rocPRIM](https://rocm.docs.amd.com/projects/rocPRIM/en/docs-7.2.3/index.html)[rocThrust](https://rocm.docs.amd.com/projects/rocThrust/en/docs-7.2.3/index.html)[AMD SMI](https://rocm.docs.amd.com/projects/amdsmi/en/docs-7.2.3/index.html)[ROCm Data Center Tool](https://rocm.docs.amd.com/projects/rdc/en/docs-7.2.3/index.html)[rocminfo](https://rocm.docs.amd.com/projects/rocminfo/en/docs-7.2.3/index.html)[ROCm SMI](https://rocm.docs.amd.com/projects/rocm_smi_lib/en/docs-7.2.3/index.html)[ROCm Validation Suite](https://rocm.docs.amd.com/projects/ROCmValidationSuite/en/docs-7.2.3/index.html)[ROCm Bandwidth Test](https://rocm.docs.amd.com/projects/rocm_bandwidth_test/en/docs-7.2.3/index.html)[ROCm Compute Profiler](https://rocm.docs.amd.com/projects/rocprofiler-compute/en/docs-7.2.3/index.html)[ROCm Systems Profiler](https://rocm.docs.amd.com/projects/rocprofiler-systems/en/docs-7.2.3/index.html)[ROCProfiler](https://rocm.docs.amd.com/projects/rocprofiler/en/docs-7.2.3/index.html)[ROCprofiler-SDK](https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/docs-7.2.3/index.html)[ROCTracer](https://rocm.docs.amd.com/projects/roctracer/en/docs-7.2.3/index.html)[HIPIFY](https://rocm.docs.amd.com/projects/HIPIFY/en/docs-7.2.3/index.html)[ROCdbgapi](https://rocm.docs.amd.com/projects/ROCdbgapi/en/docs-7.2.3/index.html)[ROCm CMake](https://rocm.docs.amd.com/projects/ROCmCMakeBuildTools/en/docs-7.2.3/index.html)[ROCm Debugger (ROCgdb)](https://rocm.docs.amd.com/projects/ROCgdb/en/docs-7.2.3/index.html)[ROCr Debug Agent](https://rocm.docs.amd.com/projects/rocr_debug_agent/en/docs-7.2.3/index.html)[HIPCC](https://rocm.docs.amd.com/projects/HIPCC/en/docs-7.2.3/index.html)[llvm-project](https://rocm.docs.amd.com/projects/llvm-project/en/docs-7.2.3/index.html)[HIP](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.3/index.html)[ROCr Runtime](https://rocm.docs.amd.com/projects/ROCR-Runtime/en/docs-7.2.3/index.html)### Detailed component changes[#](https://rocm.docs.amd.com#detailed-component-changes)

The following sections describe key changes to ROCm components.

Note

For a historical overview of ROCm component updates, see the [ROCm consolidated changelog](https://rocm.docs.amd.com/release/changelog.html).

**MIGraphX** (2.15.0)[#](https://rocm.docs.amd.com#migraphx-2-15-0)

##### Added[#](https://rocm.docs.amd.com#added)

External stream support to the MIGraphX context, allowing external HIP streams to be used during execution.

Ability to return a vector for output alias, supporting operators like

`make_tuple`

.

##### Changed[#](https://rocm.docs.amd.com#changed)

Refactored

`move_output_instructions_after`

into the module class.Updated rocMLIR to fix

`bert_squad`

and`bert_tf`

regressions.

##### Optimized[#](https://rocm.docs.amd.com#optimized)

Rewrote the

`gather`

operator to use`transpose`

/`reshape`

/`broadcast`

/`slice`

for improved performance.Horizontally fuse cross-embedding

`gather`

operators.Improved tuning for Split-K.

Removed extra assignments and inserts in

`find_nop_reshapes`

to reduce overhead.

##### Resolved issues[#](https://rocm.docs.amd.com#resolved-issues)

The following issues have been fixed:

`int`

to`bf16`

/`fp16`

conversion errors.Comparison logic in

`find_concat_op`

to match the correct I/O.`shape_transform_descriptor::rebase`

when flattening a broadcasted dimension.An error with

`rewrite_reshapes`

.A gather rewrite crash by validating the strided view element count.

A bug in gather rewrite with NHWC shapes.

A crash in rocMLIR with Inception v3 on RDNA3 architecture-based Radeon GPUs.

Filter zero-argument operators during ONNX parsing to prevent errors.

Conflict for missing

`no_broadcast`

parameter on ROCm 7.2.x.

### ROCm known issues[#](https://rocm.docs.amd.com#rocm-known-issues)

ROCm known issues are noted on [GitHub](https://github.com/ROCm/TheRock/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22Verified%20Issue%22). For known
issues related to individual components, review the [Detailed component changes](https://rocm.docs.amd.com#detailed-component-changes).

#### Minor performance regression for MIGraphX with int8-quantized models[#](https://rocm.docs.amd.com#minor-performance-regression-for-migraphx-with-int8-quantized-models)

You might observe a slight performance regression when running int8-quantized models with MIGraphX. This impact is generally minimal and does not affect correctness. However, workloads sensitive to peak throughput might have reduced performance when compared to non-quantized or alternative execution paths. This issue is currently under investigation and will be fixed in a future ROCm release. See [GitHub issue #7894](https://github.com/ROCm/TheRock/issues/7894).

### ROCm upcoming changes[#](https://rocm.docs.amd.com#rocm-upcoming-changes)

The following changes to the ROCm software stack are anticipated for future releases.

#### ROCTracer, ROCProfiler, rocprof, and rocprofv2 deprecation[#](https://rocm.docs.amd.com#roctracer-rocprofiler-rocprof-and-rocprofv2-deprecation)

ROCTracer, ROCProfiler, `rocprof`

, and `rocprofv2`

are deprecated. It’s strongly recommended to upgrade to the latest version of the [ROCprofiler-SDK](https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/) library and the (`rocprofv3`

) tool to ensure continued support and access to new features.

To learn about key feature improvements and benefits of ROCprofiler-SDK over the deprecated ROCProfiler and ROCTracer, see [Comparing ROCprofiler-SDK to legacy ROCm profiling tools](https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/conceptual/comparing-with-legacy-tools.html).

It’s anticipated that ROCTracer, ROCProfiler, `rocprof`

, and `rocprofv2`

will reach end of support (EoS) by the end of 2026 Q2.

#### ROCm SMI deprecation[#](https://rocm.docs.amd.com#rocm-smi-deprecation)

[ROCm SMI](https://github.com/ROCm/rocm_smi_lib) will be phased out in an
upcoming ROCm release and will enter maintenance mode. After this transition,
only critical bug fixes will be addressed and no further feature development
will take place.

It’s strongly recommended to transition your projects to [AMD
SMI](https://github.com/ROCm/rocm-systems/tree/develop/projects/amdsmi), the successor to ROCm SMI. AMD SMI
includes all the features of the ROCm SMI and will continue to receive regular
updates, new functionality, and ongoing support. For more information on AMD
SMI, see the [AMD SMI documentation](https://rocm.docs.amd.com/projects/amdsmi/en/latest/).

#### Changes to ROCm Object Tooling[#](https://rocm.docs.amd.com#changes-to-rocm-object-tooling)

ROCm Object Tooling tools `roc-obj-ls`

, `roc-obj-extract`

, and `roc-obj`

were
deprecated in ROCm 6.4, and will be removed in a future release. Functionality
has been added to the `llvm-objdump --offloading`

tool option to extract all
clang-offload-bundles into individual code objects found within the objects
or executables passed as input. The `llvm-objdump --offloading`

tool option also
supports the `--arch-name`

option, and only extracts code objects found with
the specified target architecture. See [llvm-objdump](https://llvm.org/docs/CommandGuide/llvm-objdump.html)
for more information.