source: https://rocm.docs.amd.com/en/latest/about/release-notes.html

# ROCm Core SDK 10.0.0 release notes[#](https://rocm.docs.amd.com#rocm-core-sdk-10-0-0-release-notes)

2026-08-26

60 min read time

These release notes describe notable changes since the previous ROCm release.

Note

Since ROCm 7.14, ROCm uses [TheRock](https://github.com/ROCm/TheRock) as its build and release system. For more information, see the [transition guide](https://rocm.docs.amd.com/transition-guide-TheRock.html).

## Release highlights[#](https://rocm.docs.amd.com#release-highlights)

This release focuses on AI inference, developer tooling, and profiling across AMD Instinct™, Radeon™, and Ryzen™ AI platforms. Highlights include expanded framework support for AI inference, new HIP APIs and performance improvements, ROCprofiler-SDK adoption across AI profiling workflows, and updates to math, sparse, and communication libraries.

### Platform and hardware support[#](https://rocm.docs.amd.com#platform-and-hardware-support)

This release expands GPU, operating system, virtualization, and partitioning support.

#### Expanded AMD GPU support[#](https://rocm.docs.amd.com#expanded-amd-gpu-support)

ROCm 10.0.0 adds support for the following AMD Radeon GPUs:

For the complete list of supported AMD hardware, see [AMD hardware support](https://rocm.docs.amd.com#amd-hardware-support).

#### Operating system support update[#](https://rocm.docs.amd.com#operating-system-support-update)

Operating system support remains unchanged in this release.

For the full list of supported Linux distributions, see [Operating system support](https://rocm.docs.amd.com#operating-system-support).

#### Expanded GPU virtualization support for Instinct GPUs[#](https://rocm.docs.amd.com#expanded-gpu-virtualization-support-for-instinct-gpus)

ROCm 10.0.0 adds support for the following virtualization configurations on AMD Instinct GPUs:

On AMD Instinct MI355X and MI350X:

KVM Passthrough Ubuntu 22.04 host OS with Ubuntu 22.04 guest OS.


On AMD Instinct MI350P:

ESXi Passthrough VMware ESXi 9.1 with Ubuntu 24.04 guest OS.


On AMD Instinct MI325X:

KVM Passthrough Ubuntu 24.04 host OS with Ubuntu 24.04 guest OS.

KVM Passthrough Ubuntu 22.04 host OS with Ubuntu 22.04 guest OS.

KVM Passthrough Ubuntu 24.04 host OS with RHEL 9.4 guest OS.

KVM Passthrough RHEL 9.4 host OS with RHEL 9.4 guest OS.

KVM SR-IOV RHEL 10.2 host OS with RHEL 10.2 guest OS.


On AMD Instinct MI300X:

KVM Passthrough Ubuntu 24.04 host OS with Ubuntu 24.04 guest OS.

KVM Passthrough Ubuntu 24.04 host OS with RHEL 9.4 guest OS.

KVM Passthrough RHEL 9.4 host OS with RHEL 9.4 guest OS.

KVM Passthrough ESXi 8 U3 with Ubuntu 24.04 and Ubuntu 22.04 guest OS.

KVM SR-IOV RHEL 10.2 host OS with RHEL 10.2 guest OS.


On AMD Instinct MI210:

KVM Passthrough Ubuntu 24.04 host OS with Ubuntu 24.04 guest OS.

KVM Passthrough Ubuntu 22.04 host OS with Ubuntu 22.04 guest OS.



Supported Single Root I/O Virtualization (SR-IOV) configurations require the [AMD GPU Virtualization Driver (GIM) 9.2.0.K](https://github.com/amd/MxGPU-Virtualization/releases/tag/9.2.0.K). For details, see [GPU virtualization support](https://rocm.docs.amd.com#gpu-virtualization-support).

#### GPU partitioning support update[#](https://rocm.docs.amd.com#gpu-partitioning-support-update)

GPU partitioning support remains unchanged in this release. For details, see [GPU partitioning support](https://rocm.docs.amd.com#gpu-partitioning-support).

### AI inference and frameworks[#](https://rocm.docs.amd.com#ai-inference-and-frameworks)

This release enables support for the following frameworks:

PyTorch 2.13.0

JAX 0.11.0

JAX 0.10.2

vLLM 0.27.0

SGLang 0.5.15

TensorFlow 2.21

MIGraphX 2.17

ONNX Runtime 1.27.0


The updated framework support replaces the previous PyTorch 2.10.0, JAX 0.9.1, vLLM 0.23.0, SGLang 0.5.13, MIGraphX 2.16, and ONNX Runtime 1.23.2 support.

For details, see [AI ecosystem support](https://rocm.docs.amd.com#ai-ecosystem-support).

### Developer tools and profiling[#](https://rocm.docs.amd.com#developer-tools-and-profiling)

This release improves ROCm developer workflows with new HIP APIs, expanded profiling and tracing capabilities, and broader telemetry coverage.

#### HIP feature highlights[#](https://rocm.docs.amd.com#hip-feature-highlights)

The following are notable enhancements to HIP:

##### Improved HIP performance[#](https://rocm.docs.amd.com#improved-hip-performance)

Improved `hipEventRecord`

performance by using the `hipEventDisableTiming`

flag to avoid unnecessary profiling when timing information is not required. Event operations are now coalesced to eliminate redundant barrier submissions, reducing runtime overhead and improving execution efficiency.

##### HIP cooperative groups exclusive and inclusive scan support[#](https://rocm.docs.amd.com#hip-cooperative-groups-exclusive-and-inclusive-scan-support)

HIP `cooperative_groups`

library adds [cooperative_groups::inclusive_scan](https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_runtime_api/cooperative_groups.html#inclusive-scan) and [cooperative_groups::exclusive_scan](https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_runtime_api/cooperative_groups.html#exclusive-scan) scan APIs in parity with CUDA. Both accept any cooperative group type and an optional custom binary operator, defaulting to summation when none is given.

##### ROCr Runtime core dump support with attached debuggers[#](https://rocm.docs.amd.com#rocr-runtime-core-dump-support-with-attached-debuggers)

The ROCr Runtime now generates a valid GPU core dump even when a debugger such as [ROCm Debugger (ROCgdb)](https://rocm.docs.amd.com/projects/ROCgdb/en/latest/index.html) or [ROCR Debug Agent](https://rocm.docs.amd.com/projects/rocr_debug_agent/en/latest/index.html) is already attached to the process. The runtime now captures the triggering GPU exception from its own internal state, so debugging sessions and core dump collection no longer need to be mutually exclusive.

##### HIP API addition for CUDA parity[#](https://rocm.docs.amd.com#hip-api-addition-for-cuda-parity)

HIP adds `hipMemGetDefaultMemPool`

, which returns the default memory pool for a given memory location and allocation type.

For more information, see the [HIP section](https://rocm.docs.amd.com#hip-10-0-0) in the ROCm component changelogs.

#### ROCprofiler-SDK feature highlights[#](https://rocm.docs.amd.com#rocprofiler-sdk-feature-highlights)

The following are notable enhancements to ROCprofiler-SDK:

##### Expanded tracing domains[#](https://rocm.docs.amd.com#expanded-tracing-domains)

ROCprofiler-SDK and `rocprofv3`

add three new first-class tracing domains:

**rocSHMEM API tracing:**Host-stream APIs, including`rocshmem_putmem_on_stream`

,`rocshmem_getmem_on_stream`

, and`rocshmem_alltoallmem_on_stream`

are now intercepted and emitted as per-call trace records. These records appear inline with HIP, HSA, RCCL, and other runtime traces, enabling you to see rocSHMEM communication activity in the same timeline as GPU compute and understand its contribution to overall application performance. Enable with the`--rocshmem-trace`

flag (or`ROCPROF_ROCSHMEM_API_TRACE`

environment variable).**hipFile tracing support:**hipFile API calls are intercepted via dispatch-table wrapping and emitted as per-call trace records alongside HIP, HSA, and other runtime activity. This allows you to see file I/O operations in the same profiling timeline as GPU kernels and memory copies, making it straightforward to quantify storage overhead and its impact on end-to-end application performance. Enable with the`--hipfile-trace`

flag (or`ROCPROF_HIPFILE_API_TRACE`

environment variable).**OpenMP (OMPT) tracing:**`rocprofv3`

exposes OpenMP Tools (OMPT) tracing as a first-class command-line flag. The`--ompt-trace`

option accepts a bare Boolean or a space-separated category list (for example`--ompt-trace parallel task target sync`

), following the same style as`--pmc`

and`--output-format`

. ROCprofiler-SDK has supported the OMPT callback layer since an earlier release; this change makes it accessible without writing a custom tool.

All records from these tracing domains are output in JSON (hipFile, rocSHMEM) and rocpd (hipFile, rocSHMEM, OpenMP) formats. The rocpd output can then be converted to CSV, Perfetto, and OTF2 using post-processing conversion scripts.

##### Enhanced graph and profiling output[#](https://rocm.docs.amd.com#enhanced-graph-and-profiling-output)

**HIP Graph per-node attribution:**ROCprofiler-SDK and`rocprofv3`

now add full per-graph-node attribution for HIP graph kernels and memory copies. Each dispatch record produced by a graph launch is tagged with the identity of the graph and the specific node within it that produced it. This allows profiling tools to group dispatches by source node across many launches, compute per-node timing and counter aggregates, and correlate graph-level summary records with their individual dispatch records. Enable with the`--hip-graph-trace`

flag, automatically included in`--hip-trace`

or`--hip-runtime-trace`

.**SPM ROCpd output support:**ROCprofiler-SDK extends the rocpd output format to include Streaming Performance Monitor (SPM) counter data. SPM records are stored as`rocpd_track`

rows with a`"SPM"`

label, with counter values grouped by timestamp into`rocpd_sample`

rows and per-dimension data in`rocpd_pmc_event`

rows. The rocpd schema is updated to include`sample_id`

,`xcc`

,`shader_engine`

, and`instance`

columns. SPM data can now be consumed by any tool that reads the rocpd database, or converted to other output formats such as Perfetto. Known Issue: SPM sessions can remain in a stale state after abrupt termination. See[GitHub issue #6489](https://github.com/ROCm/ROCm/issues/6489)for details.

##### Improved attach capabilities[#](https://rocm.docs.amd.com#improved-attach-capabilities)

**Live Attach with Advanced Thread Trace (ATT) support:**ROCprofiler-SDK extends the live attach workflow to include Advanced Thread Trace (ATT). When`rocprofv3`

attaches to a running process, it now registers for code-object iteration and creation callbacks so that thread trace can operate correctly on code objects that were loaded before the attach occurred. This makes ATT available for already-running production workloads without requiring an application restart.**Container-aware rocattach symbol resolution:**`rocprofv3`

improves attach support when the target process is running inside a container. ROCprofiler-SDK now resolves attach entry points directly from the target process mapped ELF, and validates tool paths from the target’s perspective before injection. This allows attaching from a host to a containerized process without manually copying .so files. Previously,`rocattach`

calculated symbol offsets from the host’s`librocprofiler-register.so`

and applied them to the target’s mapping, which failed when the host and container libraries differ in ELF layout or path.**Python API for rocprof-trace-decoder:**`rocprof-trace-decoder`

now ships a Python API that allows you to decode Advanced Thread Trace (ATT) / SQTT data directly from Python without writing a C++ consumer. The API wraps the decoder library and exposes thread trace decoding as a first-class Python interface, with samples included to demonstrate common workflows. Integration tests for the decoder have been migrated to Python, simplifying test authoring and making it easier for downstream tools to validate their trace-decoding pipelines. This is particularly useful for analysis scripts, Jupyter notebooks, and custom profiling tools that need to process ATT output programmatically.**SQTT quick scan support for thread trace path (Experimental):**ROCprofiler-SDK introduces an experimental SQTT quick scan mode for thread trace, accessible through a new CMake flag. The quick scan path collects thread trace data without packet insertion or HSA signal manipulation, removing the queue interception overhead that the standard ATT path requires. Individual kernels can be traced without serialization, and the approach is independent of the ROCm runtime version. This is an experimental feature intended to validate the new collection path and pave the way for out-of-process thread trace and long-kernel tracing in future releases.

##### Build and dependency improvements[#](https://rocm.docs.amd.com#build-and-dependency-improvements)

ROCprofiler-SDK no longer depends on `libatomic`

. The library was previously linked unconditionally through the `rocprofiler-sdk-atomic`

interface target, causing link failures on toolchains and container images where `libatomic1`

is not installed. The single `std::atomic`

use that required the library has been replaced with explicit memory-ordering synchronization, removing the dependency without changing behavior.

##### Quality and stability improvements[#](https://rocm.docs.amd.com#quality-and-stability-improvements)

This release includes a range of quality and stability improvements across ROCprofiler-SDK and `rocprofv3`

:

**Thread trace stall issue fixed:**Resolved a GPU stall that occurred when device thread trace was started before`hsa_init()`

.**Counter collection stall issue fixed:**Corrected an`InterceptQueue`

ordering bug that caused counter-collection sessions to stall, and fixed an out-of-bounds write in`Submit()`

.**Thread trace autoflush disabled:**Disabled autoflush in thread trace to prevent premature buffer flushes that caused incomplete or corrupted traces.**roctxMark kernel rename issue fixed:**`roctxMark`

calls no longer propagate as kernel rename labels, fixing spurious kernel name changes in traces that contained ROCTx markers.**Queue interposition bypass:**Idle inline queues with no active profiling consumers now bypass interposition entirely, reducing overhead for applications that create queues but do not immediately dispatch work.**AQLprofile gfx11xx counter issue fixed:**Corrected SQ aliasing on harvested WGPs and multi-counter desync on gfx11xx targets. Also fixed the`GcEaSeCounterBlockMaxEvent`

value in AQLprofile.**PC sampling service check:**Added a guard to prevent double-initialization of the PC sampling service.**Attach output flush:**`rocprofv3`

attach sessions now correctly block until all buffered output is flushed before exiting.**Code object callback ordering:**Corrected the ordering of code object callbacks during attach to prevent race conditions with tools that depend on ordered delivery.**DWARF parsing:**DWARF information is now parsed lazily, reducing startup overhead for attach and tracing sessions on large binaries.**Build and CI improvements:**Fixed`fmt/format.h`

include path,`fpic`

flag for samples, OMP lookup in CI, and clang-tidy quickscan enablement.

#### ROCm Compute Profiler feature highlights[#](https://rocm.docs.amd.com#rocm-compute-profiler-feature-highlights)

The following are notable enhancements to the ROCm Compute Profiler (rocprofiler-compute):

##### Triton operator tracing (experimental)[#](https://rocm.docs.amd.com#triton-operator-tracing-experimental)

Operator tracing now covers Triton and `torch.compile`

kernels in addition to PyTorch, and a single option traces every supported machine learning framework in one run. For details, see [Triton trace](https://rocm.docs.amd.com/projects/rocprofiler-compute/en/docs-10.0.0/how-to/profile/mode.html#triton-trace), [ML API trace](https://rocm.docs.amd.com/projects/rocprofiler-compute/en/docs-10.0.0/how-to/profile/mode.html#ml-api-trace), and [Operator filtering](https://rocm.docs.amd.com/projects/rocprofiler-compute/en/docs-10.0.0/how-to/analyze/cli.html#operator-filtering).

##### Improved roofline support on gfx1150 (Strix Point), gfx1151 (Strix Halo and Gorgon Halo), and gfx1152 (Krackan Point)[#](https://rocm.docs.amd.com#improved-roofline-support-on-gfx1150-strix-point-gfx1151-strix-halo-and-gorgon-halo-and-gfx1152-krackan-point)

Roofline benchmarking and analysis on these GPUs now report the correct set of supported precisions, so `--roofline-data-type`

no longer offers precisions that cannot be measured. Machine specification reporting for APUs is corrected as well. Roofline benchmarking on gfx1153 is not yet supported. For details, see [Standalone roofline](https://rocm.docs.amd.com/projects/rocprofiler-compute/en/docs-10.0.0/how-to/profile/mode.html#standalone-roofline) and [Roofline HTML generation](https://rocm.docs.amd.com/projects/rocprofiler-compute/en/docs-10.0.0/how-to/analyze/cli.html#roofline-html-generation).

For more information, see the [ROCm Compute Profiler section](https://rocm.docs.amd.com#rocm-compute-profiler-3-8-0) in the ROCm component changelogs.

#### ROCm Systems Profiler feature highlights[#](https://rocm.docs.amd.com#rocm-systems-profiler-feature-highlights)

The following are notable enhancements to ROCm Systems Profiler:

##### hipFILE (GPU-direct storage) API tracing[#](https://rocm.docs.amd.com#hipfile-gpu-direct-storage-api-tracing)

ROCm Systems Profiler can now trace hipFile GPU-direct storage API calls, giving you visibility into storage I/O paths that move data directly between storage and GPU memory. Enable it by adding `hipfile_api`

(shorthand: `hipfile`

) to `ROCPROFSYS_ROCM_DOMAINS`

. This capability requires ROCprofiler-SDK 1.3.5 or later. For details, see the ROCm domains section in [Configuring runtime options](https://rocm.docs.amd.com/projects/rocprofiler-systems/en/docs-10.0.0/how-to/configuring-runtime-options.html#configuring-runtime-options).

##### rocSHMEM host-stream API tracing[#](https://rocm.docs.amd.com#rocshmem-host-stream-api-tracing)

ROCm Systems Profiler now captures the nine host-stream rocSHMEM API calls (`putmem_on_stream`

, `getmem_on_stream`

, `putmem_signal_on_stream`

, `signal_wait_until_on_stream`

, `broadcastmem_on_stream`

, `alltoallmem_on_stream`

, `barrier_all_on_stream`

, `sync_all_on_stream`

, and `quiet_on_stream`

) as `rocm_rocshmem_api`

spans in both Perfetto traces and rocpd databases. Enable it with `ROCPROFSYS_ROCM_DOMAINS=rocshmem_api`

. This capability requires ROCprofiler-SDK 1.3.5 or later and rocSHMEM 3.6.0 or later (included in ROCm 10.0.0). Since rocSHMEM 3.6.0 enables USE_ROCPROFILER_REGISTER by default, package installations include this support automatically. A rocshmem example demonstrating two-PE usage of all nine APIs is included under examples/rocshmem. For details, see the ROCm domains section in [Configuring runtime options](https://rocm.docs.amd.com/projects/rocprofiler-systems/en/docs-10.0.0/how-to/configuring-runtime-options.html#configuring-runtime-options).

##### Finer-grained instrumentation control[#](https://rocm.docs.amd.com#finer-grained-instrumentation-control)

The `rocprof-sys-instrument`

tool adds several options to reduce instrumentation overhead and scope collection more precisely. The `--exe-only`

flag excludes every shared library from instrumentation, leaving only the main executable. The `--exclude-internal-lib-paths`

flag excludes every on-disk path that matches an internal library’s filename, rather than only the path linked at startup. The `--max-library-functions`

option skips shared libraries whose procedure count exceeds a specified threshold, keeping overhead manageable; the target executable is never gated by this threshold, and the check is bypassed for modules and functions selected through the include/restrict regexes (`--module-include/-MI`

, `--module-restrict/-MR`

, `--function-include/-I`

, and `--function-restrict/-R`

). For details, see [Binary instrumentation](https://rocm.docs.amd.com/projects/rocprofiler-systems/en/latest/how-to/instrumenting-rewriting-binary-application.html#instrumenting-and-rewriting-a-binary-application).

##### New profiler-hub writer backend[#](https://rocm.docs.amd.com#new-profiler-hub-writer-backend)

ROCm Systems Profiler introduces the new profiler-hub writer backend for trace persistence, which replaces the existing SQLite3/rocpd backend for writing trace data.

##### AI-NIC telemetry sampling[#](https://rocm.docs.amd.com#ai-nic-telemetry-sampling)

ROCm Systems Profiler now supports periodic sampling of AI NIC (RDMA) network metrics, including unicast byte/packet counts, congestion notifications, and packet-sequence error counters. Select interfaces with the `--ai-nics`

flag on `rocprof-sys-run`

or `rocprof-sys-sample`

(or via `ROCPROFSYS_SAMPLING_AINICS`

), and view the results as Perfetto or rocpd tracks alongside your existing CPU/GPU sampling data. See the [Network performance profiling](https://rocm.docs.amd.com/projects/rocprofiler-systems/en/latest/how-to/nic-profiling.html) how-to for setup, configuration, and visualization details.

For more information, see the [ROCm Systems Profiler section](https://rocm.docs.amd.com#rocm-systems-profiler-1-8-0) in the ROCm component changelogs.

### Libraries[#](https://rocm.docs.amd.com#libraries)

This release introduces new algorithms and optimizations across the math, sparse, and primitives libraries. Updates to hipFile improve I/O performance for NVMe-backed storage.

#### Composable Kernel improves a8w8 GEMM performance[#](https://rocm.docs.amd.com#composable-kernel-improves-a8w8-gemm-performance)

Composable Kernel improves a8w8 GEMM performance on AMD Instinct MI355X GPUs, delivering measurable throughput gains over the prior AITER implementation for FP8 and int8 GEMM problem shapes used in long-sequence inference workloads (sequence lengths from 6K to 1M tokens). The optimizations are built on CK Tile and are accessible through the AITER GEMM interface.

#### rocFFT supports multi-GPU RCCL backend[#](https://rocm.docs.amd.com#rocfft-supports-multi-gpu-rccl-backend)

rocFFT adds an optional RCCL backend for single-node, multi-GPU FFT communication within a single process, enabled via the `-DROCFFT_RCCL_ENABLE=ON`

CMake build option. RCCL’s GPU topology-awareness targets help improve communication performance over rocFFT’s existing memory-copy-based transport in this configuration.

#### Symmetric memory support updated in RCCL[#](https://rocm.docs.amd.com#symmetric-memory-support-updated-in-rccl)

RCCL extends its symmetric memory support with a new Reduce-Scatter kernel and expanded memory registration options for collective operations. This implementation enables:

**Reduce-Scatter symmetric kernel:**RCCL adds a symmetric-memory kernel for Reduce-Scatter on AMD Instinct MI300 Series and MI350 Series GPUs, extending symmetric-memory execution to a collective that previously required the default communication path. The kernel also adds support for the AVG reduction operation.**GPU-only multi-segment registration:**Symmetric memory windows can register multi-segment GPU memory ranges without host involvement, currently supported for single-node configurations.**Elastic buffers:**Symmetric memory collectives support tensors residing in either device or host memory, currently supported for single-node configurations.

#### hipSPARSE and rocSPARSE feature highlights[#](https://rocm.docs.amd.com#hipsparse-and-rocsparse-feature-highlights)

The following are notable enhancements to hipSPARSE and rocSPARSE:

##### rocSPARSE and hipSPARSE add Blocked ELL format support[#](https://rocm.docs.amd.com#rocsparse-and-hipsparse-add-blocked-ell-format-support)

rocSPARSE and hipSPARSE now support Blocked ELL format in their dense-to-sparse conversion routines, `rocsparse_dense_to_sparse`

and `hipsparseDenseToSparse`

. Each library adds a companion pointer-setter function, `rocsparse_bell_set_pointers`

and `hipsparseBlockedEllSetPointers`

respectively, to configure the Blocked ELL array pointers.

##### CSC format support for sparse triangular solves in rocSPARSE and hipSPARSE[#](https://rocm.docs.amd.com#csc-format-support-for-sparse-triangular-solves-in-rocsparse-and-hipsparse)

rocSPARSE and hipSPARSE sparse triangular solve routines now accept matrices in Compressed Sparse Column (CSC) format directly, removing the need to convert to Compressed Sparse Row (CSR) first. CSC support extends to `rocsparse_spsv/rocsparse_sptrsv`

and `rocsparse_spsm/rocsparse_sptrsm`

in rocSPARSE, and to `hipsparseSpSV`

and `hipsparseSpS`

in hipSPARSE.

##### hipSPARSE adds the SpMV nnz-split algorithm[#](https://rocm.docs.amd.com#hipsparse-adds-the-spmv-nnz-split-algorithm)

hipSPARSE adds the `HIPSPARSE_SPMV_CSR_ALG3`

algorithm to `hipsparseSpMV`

, exposing the rocSPARSE’s analysis-free `nnz-split`

CSR algorithm (`rocsparse_spmv_alg_csr_nnzsplit`

) for sparse matrix-vector multiplication. The algorithm distributes work across threads based on the number of non-zero entries per row and requires no preliminary analysis step before execution.

##### rocSPARSE improves default SpMM algorithm selection[#](https://rocm.docs.amd.com#rocsparse-improves-default-spmm-algorithm-selection)

rocSPARSE’s default `rocsparse_spmm`

algorithm now switches to a nnz-split kernel for strongly skewed CSR/CSC matrices (a single long row or column). This avoids the throughput loss the previous row-split default caused on such matrices. Non-skewed matrices and explicitly chosen algorithms are unaffected.

##### rocSPARSE removes rocsparse_indextype_u16 index type[#](https://rocm.docs.amd.com#rocsparse-removes-rocsparse-indextype-u16-index-type)

The `rocsparse_indextype_u16`

field of the `rocsparse_indextype`

enumerator is now removed; and only `rocsparse_indextype_i32`

and `rocsparse_indextype_i64`

remain. `rocsparse_indextype_u16`

was deprecated in ROCm 7.14.0; code that still references it will now fail to compile.

#### rocPRIM adds parallel top-K algorithms[#](https://rocm.docs.amd.com#rocprim-adds-parallel-top-k-algorithms)

rocPRIM adds `rocprim::device_topk`

and `rocprim::device_segmented_topk`

, parallel device-level algorithms that find the largest or smallest K elements from an input array or from segmented groups, respectively. To enable this feature, add the `-DROCPRIM_ENABLE_TOPK=ON`

CMake build option. The default variant is hipGraph-compatible; a stable-ordering variant is also available for callers that need guaranteed ordering.

#### hipFile fastpath I/O support for LVM volumes[#](https://rocm.docs.amd.com#hipfile-fastpath-i-o-support-for-lvm-volumes)

hipFile now supports fastpath I/O to files on Logical Volume Manager (LVM) volumes backed by NVMe devices, resolving a previous ENODEV error caused by the underlying PCI device not being resolvable through the volume manager.

#### AMD SMI feature highlights[#](https://rocm.docs.amd.com#amd-smi-feature-highlights)

The following are notable changes to AMD SMI:

##### AMD SMI VCN busy metric on Radeon RX GPUs[#](https://rocm.docs.amd.com#amd-smi-vcn-busy-metric-on-radeon-rx-gpus)

AMD SMI now correctly reports the VCN busy percentage for Radeon RX GPUs in the `amd-smi metric --usage`

output. On affected devices where GPU metrics lacked VCN activity data, the value previously displayed as `N/A`

. AMD SMI now reads the metric from the available sysfs source and reports it correctly.

##### AMD SMI API removals[#](https://rocm.docs.amd.com#amd-smi-api-removals)

The AMD SMI library has removed several APIs, types, defines, and enums, and changed the Application Binary Interface (ABI) of `amdsmi_gpu_metrics_t`

in this release. For details, see [AMD SMI API and ABI changes](https://rocm.docs.amd.com#amd-smi-breaking-changes).

## AMD hardware support[#](https://rocm.docs.amd.com#amd-hardware-support)

The following table lists supported AMD Instinct GPUs, Radeon GPUs, and Ryzen APUs. Each supported device is listed with its corresponding GPU microarchitecture and LLVM target.

Note

If your GPU is not listed, it might be community-enabled through TheRock nightly builds. For more information, see [TheRock supported GPUs](https://github.com/ROCm/TheRock/blob/main/SUPPORTED_GPUS.md). For installation guidance, see [TheRock releases](https://github.com/ROCm/TheRock/blob/main/RELEASES.md).

Device series |
Device |
LLVM target |
Architecture |
|---|---|---|---|
|

**gfx950**[CDNA 4](https://www.amd.com/en/technologies/cdna.html#cdna4)[AMD Instinct MI300 Series](https://www.amd.com/en/products/accelerators/instinct/mi300.html)**gfx942**[CDNA 3](https://www.amd.com/en/technologies/cdna.html#cdna3)[AMD Instinct MI200 Series](https://www.amd.com/en/products/accelerators/instinct/mi200.html)**gfx90a**[CDNA 2](https://www.amd.com/en/technologies/cdna.html#cdna2)[AMD Instinct MI100 Series](https://www.amd.com/en/products/accelerators/instinct/mi100.html)**gfx908**[CDNA](https://www.amd.com/en/technologies/cdna.html#cdna)Device series |
Device |
LLVM target |
Architecture |
|---|---|---|---|
|

**gfx1201**[RDNA 4](https://www.amd.com/en/technologies/rdna.html#tabs-1fabb91c39-item-330ee548f0-tab)[AMD Radeon RX 9000 Series](https://www.amd.com/en/products/graphics/desktops/radeon.html#tabs-ff9c5c3863-item-37fb38a236-tab)**gfx1201****gfx1200**[AMD Radeon PRO W7000 Series](https://www.amd.com/en/products/graphics/workstations/radeon-pro.html#tabs-990fdead92-item-20daa37284-tab)**gfx1100**[RDNA 3](https://www.amd.com/en/technologies/rdna.html#tabs-1fabb91c39-item-05915f6044-tab)**gfx1101**[AMD Radeon RX 7000 Series](https://www.amd.com/en/products/graphics/desktops/radeon.html#tabs-ff9c5c3863-item-b55a56bf12-tab)**gfx1100****gfx1101****gfx1102**[AMD Radeon PRO V Series](https://www.amd.com/en/products/accelerators/radeon-pro.html)**gfx1101****gfx1030**[RDNA 2](https://www.amd.com/en/technologies/rdna.html#tabs-1fabb91c39-item-9ed969eddf-tab)[AMD Radeon PRO W6000 Series](https://www.amd.com/en/products/graphics/workstations/radeon-pro/w6800.html)**gfx1030**Device series |
Device |
LLVM target / codename |
Architecture |
|---|---|---|---|
|

[Ryzen AI Max+ PRO 495](https://www.amd.com/en/products/processors/laptop/ryzen-pro/ai-max-pro-400-series/amd-ryzen-ai-max-plus-pro-495.html) (Radeon 8065S)

[Ryzen AI Max PRO 490](https://www.amd.com/en/products/processors/laptop/ryzen-pro/ai-max-pro-400-series/amd-ryzen-ai-max-pro-490.html) (Radeon 8050S)

[Ryzen AI Max PRO 485](https://www.amd.com/en/products/processors/laptop/ryzen-pro/ai-max-pro-400-series/amd-ryzen-ai-max-pro-485.html) (Radeon 8050S)

**gfx1151**Gorgon Halo

[AMD Ryzen AI Max PRO 300 Series](https://www.amd.com/en/products/processors/workstations/mobile.html#tabs-7f0c432fb2-item-5116ab7a74-tab)[Ryzen AI Max+ PRO 395](https://www.amd.com/en/products/processors/laptop/ryzen-pro/ai-max-pro-300-series/amd-ryzen-ai-max-plus-pro-395.html) (Radeon 8060S)

[Ryzen AI Max PRO 390](https://www.amd.com/en/products/processors/laptop/ryzen-pro/ai-max-pro-300-series/amd-ryzen-ai-max-pro-390.html) (Radeon 8050S)

[Ryzen AI Max PRO 385](https://www.amd.com/en/products/processors/laptop/ryzen-pro/ai-max-pro-300-series/amd-ryzen-ai-max-pro-385.html) (Radeon 8050S)

[Ryzen AI Max PRO 380](https://www.amd.com/en/products/processors/laptop/ryzen-pro/ai-max-pro-300-series/amd-ryzen-ai-max-pro-380.html) (Radeon 8040S)

**gfx1151**Strix Halo

[AMD Ryzen AI Max 300 Series](https://www.amd.com/en/products/processors/laptop/ryzen.html#tabs-1181ea0b44-item-6ccfea5f65-tab)[Ryzen AI Max+ 395](https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-max-plus-395.html) (Radeon 8060S)

[Ryzen AI Max+ 392](https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-max-plus-392.html) (Radeon 8060S)

[Ryzen AI Max+ 388](https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-max-plus-388.html) (Radeon 8060S)

[Ryzen AI Max 390](https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-max-390.html) (Radeon 8050S)

[Ryzen AI Max 385](https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-max-385.html) (Radeon 8050S)

**gfx1151**Strix Halo

[AMD Ryzen AI PRO 400 Series](https://www.amd.com/en/products/processors/laptop/ryzen-for-business.html#tabs-0d174caf43-item-87690677fc-tab)[Ryzen AI 9 HX PRO 475](https://www.amd.com/en/products/processors/laptop/ryzen-pro/ai-400-series/amd-ryzen-ai-9-hx-pro-475.html) (Radeon 890M)

[Ryzen AI 9 HX PRO 470](https://www.amd.com/en/products/processors/laptop/ryzen-pro/ai-400-series/amd-ryzen-ai-9-hx-pro-470.html) (Radeon 890M)

[Ryzen AI 9 PRO 465](https://www.amd.com/en/products/processors/laptop/ryzen-pro/ai-400-series/amd-ryzen-ai-9-pro-465.html) (Radeon 880M)

**gfx1150**Gorgon Point

[Ryzen AI 7 PRO 450](https://www.amd.com/en/products/processors/laptop/ryzen-pro/ai-400-series/amd-ryzen-ai-7-pro-450.html) (Radeon 860M)

[Ryzen AI 5 PRO 440](https://www.amd.com/en/products/processors/laptop/ryzen-pro/ai-400-series/amd-ryzen-ai-5-pro-440.html) (Radeon 840M)

**gfx1152**Gorgon Point

[Ryzen AI 5 PRO 435](https://www.amd.com/en/products/processors/laptop/ryzen-pro/ai-400-series/amd-ryzen-ai-5-pro-435.html) (Radeon 840M)

**gfx1153**Gorgon Point

[AMD Ryzen AI 400 Series](https://www.amd.com/en/products/processors/consumer/ryzen-ai.html#tabs-f556098628-item-808b56dca3-tab)[Ryzen AI 9 HX 475](https://www.amd.com/en/products/processors/laptop/ryzen/ai-400-series/amd-ryzen-ai-9-hx-475.html) (Radeon 890M)

[Ryzen AI 9 HX 470](https://www.amd.com/en/products/processors/laptop/ryzen/ai-400-series/amd-ryzen-ai-9-hx-470.html) (Radeon 890M)

[Ryzen AI 9 465](https://www.amd.com/en/products/processors/laptop/ryzen/ai-400-series/amd-ryzen-ai-9-465.html) (Radeon 880M)

**gfx1150**Gorgon Point

[Ryzen AI 7 450](https://www.amd.com/en/products/processors/laptop/ryzen/ai-400-series/amd-ryzen-ai-7-450.html) (Radeon 860M)

**gfx1152**Gorgon Point

[Ryzen AI 5 435](https://www.amd.com/en/products/processors/laptop/ryzen/ai-400-series/amd-ryzen-ai-5-435.html) (Radeon 840M)

[Ryzen AI 5 430](https://www.amd.com/en/products/processors/laptop/ryzen/ai-400-series/amd-ryzen-ai-5-430.html) (Radeon 840M)

[Ryzen AI 7 445](https://www.amd.com/en/products/processors/laptop/ryzen/ai-400-series/amd-ryzen-ai-7-445.html) (Radeon 840M)

**gfx1153**Gorgon Point

[AMD Ryzen AI PRO 300 Series](https://www.amd.com/en/products/processors/workstations/mobile.html#tabs-7f0c432fb2-item-387526c6cc-tab)[Ryzen AI 9 HX PRO 375](https://www.amd.com/en/products/processors/laptop/ryzen-pro/ai-300-series/amd-ryzen-ai-9-hx-pro-375.html) (Radeon 890M)

[Ryzen AI 9 HX PRO 370](https://www.amd.com/en/products/processors/laptop/ryzen-pro/ai-300-series/amd-ryzen-ai-9-hx-pro-370.html) (Radeon 890M)

**gfx1150**Strix Point

[Ryzen AI 7 PRO 350](https://www.amd.com/en/products/processors/laptop/ryzen-pro/ai-300-series/amd-ryzen-ai-7-pro-350.html) (Radeon 860M)

[Ryzen AI 5 PRO 340](https://www.amd.com/en/products/processors/laptop/ryzen-pro/ai-300-series/amd-ryzen-ai-5-pro-340.html) (Radeon 840M)

**gfx1152**Krackan Point

[AMD Ryzen AI 300 Series](https://www.amd.com/en/products/processors/consumer/ryzen-ai.html#tabs-f556098628-item-54e149d850-tab)[Ryzen AI 9 HX 375](https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-9-hx-375.html) (Radeon 890M)

[Ryzen AI 9 HX 370](https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-9-hx-370.html) (Radeon 890M)

[Ryzen AI 9 365](https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-9-365.html) (Radeon 880M)

**gfx1150**Strix Point

[Ryzen AI 7 350](https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-7-350.html) (Radeon 860M)

[Ryzen AI 7 345](https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-7-345.html) (Radeon 840M)

[Ryzen AI 5 340](https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-5-340.html) (Radeon 840M)

[Ryzen AI 5 330](https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-5-330.html) (Radeon 820M)

**gfx1152**Krackan Point

[AMD Ryzen PRO 200 Series](https://www.amd.com/en/products/processors/laptop/ryzen-for-business.html#tabs-0d174caf43-item-a8ec88d07e-tab)[Ryzen 7 PRO 250](https://www.amd.com/en/products/processors/laptop/ryzen-pro/200-series/amd-ryzen-7-pro-250.html) (Radeon 780M)

[Ryzen 5 PRO 230](https://www.amd.com/en/products/processors/laptop/ryzen-pro/200-series/amd-ryzen-5-pro-230.html) (Radeon 760M)

[Ryzen 5 PRO 220](https://www.amd.com/en/products/processors/laptop/ryzen-pro/200-series/amd-ryzen-5-pro-220.html) (Radeon 740M)

[Ryzen 5 PRO 215](https://www.amd.com/en/products/processors/laptop/ryzen-pro/200-series/amd-ryzen-5-pro-215.html) (Radeon 740M)

[Ryzen 3 PRO 210](https://www.amd.com/en/products/processors/laptop/ryzen-pro/200-series/amd-ryzen-3-pro-210.html) (Radeon 740M)

**gfx1103**Hawk Point

[RDNA 3](https://www.amd.com/en/technologies/rdna.html#tabs-1fabb91c39-item-05915f6044-tab)[AMD Ryzen 200 Series](https://www.amd.com/en/products/processors/laptop/ryzen.html#tabs-1181ea0b44-item-895d56feed-tab)[Ryzen 9 270](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-9-270.html) (Radeon 780M)

[Ryzen 7 260](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-7-260.html) (Radeon 780M)

[Ryzen 7 250](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-7-250.html) (Radeon 780M)

[Ryzen 5 240](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-5-240.html) (Radeon 760M)

[Ryzen 5 230](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-5-230.html) (Radeon 760M)

[Ryzen 5 220](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-5-220.html) (Radeon 740M)

[Ryzen 3 210](https://www.amd.com/en/products/processors/laptop/ryzen/200-series/amd-ryzen-3-210.html) (Radeon 740M)

**gfx1103**Hawk Point

## Operating system support[#](https://rocm.docs.amd.com#operating-system-support)

ROCm supports the following Linux distributions and Microsoft Windows versions. If you’re running ROCm on Linux, ensure your system is using a supported kernel version.

Important

The following table is a general overview of supported operating systems. Actual support might vary by AMD GPU or APU. Use the [Compatibility matrix](https://rocm.docs.amd.com/compatibility/compatibility-matrix.html) to verify support for your specific setup before installation.

Linux distribution |
Supported versions |
Linux kernel version |
|---|---|---|
Ubuntu |
26.04 |
GA 7.0 |
24.04.4 |
GA 6.8 |
|
22.04.5 |
GA 5.15 |
|
Debian |
13 |
6.12 |
12 |
6.1.0 |
|
Red Hat Enterprise Linux (RHEL) |
10.2 |
6.12.0-211 |
10.0 |
6.12.0-55 |
|
9.8 |
5.14.0-687 |
|
9.6 |
5.14.0-570 |
|
9.4 |
5.14.0-427 |
|
8.10 |
4.18.0-553 |
|
Oracle Linux |
10 |
UEK 8.1 |
9 |
UEK 8 |
|
8 |
UEK 7 |
|
SUSE Linux Enterprise Server (SLES) |
16.0 |
6.12 |
15.7 |
6.4.0-150700.51 |
|
Rocky Linux |
9 |
5.14.0-570 |

Operating system |
Supported versions |
Linux kernel version |
|---|---|---|
Ubuntu |
26.04 |
GA 7.0 |
24.04.4 |
HWE 6.17 |
|
22.04.5 |
HWE 6.8 |
|
Red Hat Enterprise Linux (RHEL) |
10.2 |
6.12.0-211 |
9.8 |
5.14.0-687 |
|
Windows |
11 25H2 |
— |

Operating system |
Supported versions |
Linux kernel version |
|---|---|---|
Ubuntu |
26.04 |
GA 7.0 |
24.04.4 |
OEM 6.17 |
|
Windows |
11 25H2 |
— |

## Installation updates[#](https://rocm.docs.amd.com#installation-updates)

ROCm 10.0.0 adds support for new GPUs and APUs and fixes minor issues in the Runfile Installer.

## Kernel driver and firmware bundle support[#](https://rocm.docs.amd.com#kernel-driver-and-firmware-bundle-support)

ROCm requires a coordinated stack of compatible firmware, driver, and user-space components. Maintaining version alignment between these layers ensures correct GPU operation and performance, especially for AMD data center products. While AMD publishes the AMD GPU driver and ROCm user space components, your server OEM (original equipment manufacturer) or infrastructure provider distributes the firmware packages. AMD supplies those firmware images (platform level data model (PLDM) bundles), which the OEM integrates and distributes.

AMD device |
PLDM Bundle (Firmware) |
Linux driver |
|---|---|---|
Instinct MI355X |
01.26.01.03 (or later) |
|
Instinct MI350X |
||
Instinct MI350P |
BKC12.0 (IFWI PRD1000A) or later |
|
Instinct MI325X |
01.26.01.03 (or later) |
|
Instinct MI300X |
01.26.00.04 (or later) |
|
Instinct MI300A |
PI100D |
|
Instinct MI250X |
Maintenance update (MU) 5 with IFWI 75 (or later) |
|
Instinct MI250 |
||
Instinct MI210 |
||
Instinct MI100 |
VBIOS D3430401-037 |

Linux driver |
Windows driver |
|---|---|
|
|
|

Linux driver |
Windows driver |
|---|---|
|
Ubuntu 26.04: use inbox kernel driver |
|

## GPU virtualization support[#](https://rocm.docs.amd.com#gpu-virtualization-support)

AMD Instinct and Radeon GPUs support virtualization in the following configurations. Supported SR-IOV configurations require the AMD GPU Virtualization Driver (GIM) 9.2.0.K—see the [AMD Instinct Virtualization Driver documentation](https://instinct.docs.amd.com/projects/virt-drv/en/mainline-9.2.0.k/) for more information.

AMD GPU |
Hypervisor |
Virtualization technology |
Virtualization driver |
Host OS |
Guest OS |
|---|---|---|---|---|---|
Instinct MI355X |
KVM |
Passthrough |
— |
Ubuntu 26.04 |
Ubuntu 26.04 |
Ubuntu 24.04 |
Ubuntu 24.04 |
||||
Ubuntu 22.04 |
Ubuntu 22.04 |
||||
SR-IOV |
|

Ubuntu 24.04

Ubuntu 24.04

RHEL 10.0

RHEL 9.6

ESXi

SR-IOV

—

VMware ESXi 9.1

Ubuntu 24.04

Instinct MI350X

KVM

Passthrough

—

Ubuntu 26.04

Ubuntu 26.04

Ubuntu 24.04

Ubuntu 24.04

Ubuntu 22.04

Ubuntu 22.04

SR-IOV

[GIM 9.2.0.K](https://github.com/amd/MxGPU-Virtualization/releases/tag/9.2.0.K)Ubuntu 24.04

Ubuntu 24.04

RHEL 10.0

RHEL 9.6

ESXi

SR-IOV

—

VMware ESXi 9.1

Ubuntu 24.04

Instinct MI350P

KVM

Passthrough

—

Debian 13

Ubuntu 24.04

ESXi

Passthrough

—

VMware ESXi 9.1

Ubuntu 24.04

Instinct MI325X

KVM

Passthrough

—

Ubuntu 26.04

Ubuntu 26.04

Ubuntu 24.04

Ubuntu 24.04

RHEL 9.4

Ubuntu 22.04

Ubuntu 22.04

RHEL 9.4

RHEL 9.4

SR-IOV

[GIM 9.2.0.K](https://github.com/amd/MxGPU-Virtualization/releases/tag/9.2.0.K)Ubuntu 22.04

Ubuntu 22.04

RHEL 10.2

RHEL 10.2

Instinct MI300X

KVM

Passthrough

—

Ubuntu 26.04

Ubuntu 26.04

Ubuntu 24.04

Ubuntu 24.04

RHEL 9.4

Ubuntu 22.04

Ubuntu 22.04

RHEL 9.4

RHEL 9.4

ESXi 8 U3

Ubuntu 24.04

Ubuntu 22.04

SR-IOV

[GIM 9.2.0.K](https://github.com/amd/MxGPU-Virtualization/releases/tag/9.2.0.K)Ubuntu 24.04

Ubuntu 24.04

Ubuntu 22.04

Ubuntu 22.04

RHEL 10.2

RHEL 10.2

RHEL 9.4

RHEL 9.4

RHEL 9.4

Ubuntu 24.04

Instinct MI210

KVM

Passthrough

—

Ubuntu 26.04

Ubuntu 26.04

Ubuntu 24.04

Ubuntu 24.04

Ubuntu 22.04

Ubuntu 22.04

RHEL 9.4

Ubuntu 22.04

SR-IOV

[GIM 9.2.0.K](https://github.com/amd/MxGPU-Virtualization/releases/tag/9.2.0.K)RHEL 9.4

Ubuntu 22.04

RHEL 9.4

AMD GPU |
Hypervisor |
Virtualization technology |
Virtualization driver |
Host OS |
Guest OS |
|---|---|---|---|---|---|
Radeon AI PRO R9700S |
KVM |
Passthrough |
— |
Ubuntu 24.04 |
Ubuntu 24.04 |
Radeon PRO V710 |
KVM |
SR-IOV |
|

Ubuntu 24.04

Ubuntu 24.04

RHEL 9.6

## GPU partitioning support[#](https://rocm.docs.amd.com#gpu-partitioning-support)

The following compute partition and NUMA-per-socket (NPS) configurations are available on AMD Instinct GPUs in bare-metal deployments.

Deployment |
Device |
Compute partition mode |
Memory partition mode |
|---|---|---|---|
Bare metal |
Instinct MI355X, Instinct MI350X |
SPX |
NPS1 |
DPX |
NPS2 |
||
CPX |
NPS2 |
||
QPX |
NPS2 |
||
Instinct MI350P |
SPX |
NPS1 |
|
DPX |
NPS1 |
||
CPX |
NPS1 |
||
Instinct MI325X |
SPX |
NPS1 |
|
Instinct MI300X |
SPX |
NPS1 |
|
DPX |
NPS2 |
||
CPX |
NPS4 |

The following configurations are available on AMD Instinct GPUs in passthrough deployments.

Deployment |
Device |
Compute partition mode |
Memory partition mode |
|---|---|---|---|
KVM Passthrough |
Instinct MI355X, Instinct MI350X, Instinct MI325X, Instinct MI300X |
SPX |
NPS1 |
ESXi Passthrough |
Instinct MI350P, Instinct MI300X |
SPX |
NPS1 |

The following configurations are available on AMD Instinct GPUs in SR-IOV
deployments. See [GPU virtualization support](https://rocm.docs.amd.com#release-virtualization-support) for driver support
information.

Deployment |
Device |
VFs per GPU |
Compute partition mode |
Memory partition mode |
|---|---|---|---|---|
KVM SR-IOV |
Instinct MI355X, Instinct MI350X |
1 |
SPX |
NPS1 |
2 |
DPX |
NPS2 |
||
8 |
CPX |
NPS2 |
||
Instinct MI325X |
1 |
SPX |
NPS1 |
|
Instinct MI300X |
1 |
SPX |
NPS1 |
|
8 |
CPX |
NPS4 |
||
ESXi SR-IOV |
Instinct MI355X, Instinct MI350X |
1 |
SPX |
NPS1 |

See the [AMD GPU partitioning](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/gpu-partitioning/index.html) topic in the AMD GPU Driver documentation to learn more.

## AI ecosystem support[#](https://rocm.docs.amd.com#ai-ecosystem-support)

ROCm 10.0.0 provides optimized support for popular deep learning frameworks and AI inference engines. The following table lists supported frameworks and libraries, their compatible operating systems, and validated versions.

Important

The following table is a general overview of supported frameworks and AI inference engines. Actual support might vary by AMD GPU or APU. Use the [Compatibility matrix](https://rocm.docs.amd.com/compatibility/compatibility-matrix.html) to verify support for your specific setup.

|
Framework |
Supported versions |
Supported OS |
Supported Python versions |
|---|---|---|---|
|
|

2.13.0, 2.12.0, 2.11.0

Linux

3.14, 3.13, 3.12, 3.11

2.13.0

Windows

[JAX](https://rocm.docs.amd.com/projects/ai-ecosystem/en/latest/frameworks/jax/install.html)0.11.0

Linux

3.14, 3.13, 3.12

0.10.2, 0.10.0

3.14, 3.13, 3.12, 3.11

[vLLM](https://rocm.docs.amd.com/projects/ai-ecosystem/en/latest/inference/vllm.html)0.27.0

([gfx950, gfx942, gfx1200,gfx1201, gfx1100, gfx1101,gfx1102, gfx1152, gfx1151,gfx1150 GPUs only](https://rocm.docs.amd.com#release-supported-hw))

Linux

3.14 (requires PyTorch 2.13.0)

[SGLang](https://rocm.docs.amd.com/projects/ai-ecosystem/en/latest/inference/sglang.html)0.5.15

([gfx950, gfx942, gfx1200,gfx1201, gfx1100, gfx1101, gfx1102 GPUs only](https://rocm.docs.amd.com#release-supported-hw))

Linux

3.14 (requires PyTorch 2.13.0)

[TensorFlow](https://rocm.docs.amd.com/projects/ai-ecosystem/en/latest/frameworks/tensorflow/install.html)2.21, 2.20, 2.19.1

([gfx950, gfx942, gfx90a GPUs only](https://rocm.docs.amd.com#release-supported-hw))

Linux

3.12

[MIGraphX](https://rocm.docs.amd.com/projects/ai-ecosystem/en/latest/inference/migraphx.html)2.17

([gfx950, gfx942, gfx1200,gfx1201, gfx1100, gfx1101, gfx1102 GPUs only](https://rocm.docs.amd.com#release-supported-hw))

Linux

3.14, 3.12

[ONNX Runtime](https://rocm.docs.amd.com/projects/ai-ecosystem/en/latest/inference/onnxruntime.html)1.29.0

([gfx950, gfx942, gfx1200,gfx1201, gfx1100, gfx1101, gfx1102 GPUs only](https://rocm.docs.amd.com#release-supported-hw))

Linux

3.14, 3.12

## ROCm Core SDK components[#](https://rocm.docs.amd.com#rocm-core-sdk-components)

The following table lists core tools and libraries included in the ROCm 10.0.0 release.

Important

The following table is a general overview of ROCm Core SDK components. Actual support for these libraries and tools can vary by GPU and OS. Use the [Compatibility matrix](https://rocm.docs.amd.com/compatibility/compatibility-matrix.html) to verify support for your specific setup.

Component group |
Component name |
Version |
Supported platforms |
|
|---|---|---|---|---|
Math and compute libraries |
|

[1.2.0](https://rocm.docs.amd.com#composable-kernel-1-2-0)[hipBLAS](https://rocm.docs.amd.com/projects/hipBLAS/en/docs-10.0.0/index.html)[3.6.0](https://rocm.docs.amd.com#hipblas-3-6-0)[hipBLASLt](https://rocm.docs.amd.com/projects/hipBLASLt/en/docs-10.0.0/index.html)[hipCUB](https://rocm.docs.amd.com/projects/hipCUB/en/docs-10.0.0/index.html)[4.6.0](https://rocm.docs.amd.com#hipcub-4-6-0)[hipFFT](https://rocm.docs.amd.com/projects/hipFFT/en/docs-10.0.0/index.html)[1.0.25](https://rocm.docs.amd.com#hipfft-1-0-25)[hipRAND](https://rocm.docs.amd.com/projects/hipRAND/en/docs-10.0.0/index.html)[hipSOLVER](https://rocm.docs.amd.com/projects/hipSOLVER/en/docs-10.0.0/index.html)[3.6.0](https://rocm.docs.amd.com#hipsolver-3-6-0)[hipSPARSE](https://rocm.docs.amd.com/projects/hipSPARSE/en/docs-10.0.0/index.html)[4.7.0](https://rocm.docs.amd.com#hipsparse-4-7-0)[hipSPARSELt](https://rocm.docs.amd.com/projects/hipSPARSELt/en/docs-10.0.0/index.html)[MIOpen](https://rocm.docs.amd.com/projects/MIOpen/en/docs-10.0.0/index.html)[3.6.0](https://rocm.docs.amd.com#miopen-3-6-0)[rocBLAS](https://rocm.docs.amd.com/projects/rocBLAS/en/docs-10.0.0/index.html)[5.6.0](https://rocm.docs.amd.com#rocblas-5-6-0)[rocFFT](https://rocm.docs.amd.com/projects/rocFFT/en/docs-10.0.0/index.html)[1.0.39](https://rocm.docs.amd.com#rocfft-1-0-39)[rocPRIM](https://rocm.docs.amd.com/projects/rocPRIM/en/docs-10.0.0/index.html)[4.6.0](https://rocm.docs.amd.com#rocprim-4-6-0)[rocRAND](https://rocm.docs.amd.com/projects/rocRAND/en/docs-10.0.0/index.html)[5.0.0](https://rocm.docs.amd.com#rocrand-5-0-0)[rocSOLVER](https://rocm.docs.amd.com/projects/rocSOLVER/en/docs-10.0.0/index.html)[3.36.0](https://rocm.docs.amd.com#rocsolver-3-36-0)[rocSPARSE](https://rocm.docs.amd.com/projects/rocSPARSE/en/docs-10.0.0/index.html)[5.0.0](https://rocm.docs.amd.com#rocsparse-5-0-0)[rocThrust](https://rocm.docs.amd.com/projects/rocThrust/en/docs-10.0.0/index.html)[4.6.0](https://rocm.docs.amd.com#rocthrust-4-6-0)[rocWMMA](https://rocm.docs.amd.com/projects/rocWMMA/en/docs-10.0.0/index.html)Communication libraries

[RCCL](https://rocm.docs.amd.com/projects/rccl/en/docs-10.0.0/index.html)[2.30.7](https://rocm.docs.amd.com#rccl-2-30-7)[rocSHMEM](https://rocm.docs.amd.com/projects/rocSHMEM/en/docs-10.0.0/index.html)[3.6.0](https://rocm.docs.amd.com#rocshmem-3-6-0)Media libraries

[rocDecode](https://rocm.docs.amd.com/projects/rocDecode/en/docs-10.0.0/index.html)[1.9.0](https://rocm.docs.amd.com#rocdecode-1-9-0)[rocJPEG](https://rocm.docs.amd.com/projects/rocJPEG/en/docs-10.0.0/index.html)[1.7.0](https://rocm.docs.amd.com#rocjpeg-1-7-0)Storage libraries

[hipFile](https://rocm.docs.amd.com/projects/hipFile/en/docs-10.0.0/index.html)[0.4.0](https://rocm.docs.amd.com#hipfile-0-4-0)Runtimes and compilers

[HIP](https://rocm.docs.amd.com/projects/HIP/en/docs-10.0.0/index.html)[10.0.0](https://rocm.docs.amd.com#hip-10-0-0)[HIPIFY](https://rocm.docs.amd.com/projects/HIPIFY/en/docs-10.0.0/index.html)[LLVM](https://rocm.docs.amd.com/projects/llvm-project/en/docs-10.0.0/index.html)[ROCr Runtime](https://rocm.docs.amd.com/projects/ROCR-Runtime/en/docs-10.0.0/index.html)[SPIRV-LLVM-Translator](https://github.com/ROCm/SPIRV-LLVM-Translator/tree/therock-10.0)Profiling and debugging tools

[ROCdbgapi](https://rocm.docs.amd.com/projects/ROCdbgapi/en/docs-10.0.0/index.html)[ROCgdb](https://rocm.docs.amd.com/projects/ROCgdb/en/docs-10.0.0/index.html)[16.3](https://rocm.docs.amd.com#rocgdb-16-3)[ROCm Compute Profiler](https://rocm.docs.amd.com/projects/rocprofiler-compute/en/docs-10.0.0/index.html)[3.8.0](https://rocm.docs.amd.com#rocm-compute-profiler-3-8-0)[ROCm Systems Profiler](https://rocm.docs.amd.com/projects/rocprofiler-systems/en/docs-10.0.0/index.html)[1.8.0](https://rocm.docs.amd.com#rocm-systems-profiler-1-8-0)[ROCprofiler-SDK](https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/docs-10.0.0/index.html)[1.3.5](https://rocm.docs.amd.com#rocprofiler-sdk-1-3-5)[ROCr Debug Agent](https://rocm.docs.amd.com/projects/rocr_debug_agent/en/docs-10.0.0/index.html)Control and monitoring tools

[AMD SMI](https://rocm.docs.amd.com/projects/amdsmi/en/docs-10.0.0/index.html)[27.0.0](https://rocm.docs.amd.com#amd-smi-27-0-0)[ROCm Data Center Tool](https://rocm.docs.amd.com/projects/rdc/en/docs-10.0.0/index.html)[rocminfo](https://rocm.docs.amd.com/projects/rocminfo/en/docs-10.0.0/index.html)### ROCm component changelogs[#](https://rocm.docs.amd.com#rocm-component-changelogs)

The following sections describe key changes to ROCm Core SDK components.

Note

For a historical overview of ROCm component updates, see the [ROCm consolidated changelog](https://rocm.docs.amd.com/release/changelog.html).

**AMD SMI** (27.0.0)[#](https://rocm.docs.amd.com#amd-smi-27-0-0)

##### Changed[#](https://rocm.docs.amd.com#changed)

Bumped the library major version to 27.0.0 (breaking).

The shared library SONAME is now

`libamd_smi.so.27`

. Consumers linked against`libamd_smi.so.26`

must relink; no source changes are required beyond the API changes listed elsewhere in this release.

Restructured AMD SMI C++ tests into unit and functional suites.

The

`amdsmitst`

source tree now separates unit tests from hardware-backed functional tests under`tests/amd_smi_test/unit/`

and`tests/amd_smi_test/functional/`

.GTest suite names now follow a

`<Component><Type>[<Operation>]`

scheme: functional tests are`<Component>FunctionalReadOnly`

/`<Component>FunctionalReadWrite`

(e.g.`GpuFunctionalReadOnly`

) and unit tests are`<Component>Unit`

(e.g.`GpuUnit`

). This replaces the old`amdsmitstReadOnly`

/`amdsmitstReadWrite`

and`AmdSmiDynamicMetricTest`

names.Consumers that pass explicit

`--gtest_filter`

values should update those filters to the new suite names.See the

[AMD SMI test design](https://rocm.docs.amd.com/projects/amdsmi/en/docs-10.0.0/conceptual/test-design.html#naming-conventions)for the suite naming convention and`--gtest_filter`

usage.


##### Optimized[#](https://rocm.docs.amd.com#optimized)

Optimized

`amdsmi_get_gpu_process_list()`

to skip redundant KFD topology discovery.The per-process KFD lookup rebuilt the entire KFD node topology (an expensive sysfs walk) on every call just to translate the device BDF into its KFD GPU id.

The caller already knows this value, so it is now passed through to

`gpuvsmi_get_pid_info()`

, eliminating one full topology discovery per process per refresh. Falls back to the original discovery path when the id is unavailable.


##### Resolved issues[#](https://rocm.docs.amd.com#resolved-issues)

Fixed

`amd-smi ras --cper --json`

emitting nothing when there are no CPER entries.The common no-entries case printed empty output, so consumers feeding stdout to

`json.loads`

failed with`Expecting value: line 1 column 1 (char 0)`

. The command now always emits exactly one valid JSON document:`[]`

when there are no entries, or a single aggregated array across all GPUs when there are.`--follow`

mode stays silent until entries appear. The human-readable primary-partition warning is also suppressed in JSON mode so it no longer corrupts the output.

Fixed

`amd-smi set --ptl-status`

silently failing to change PTL state.The set path wrote

`"1"`

/`"0"`

to the`ptl/ptl_enable`

sysfs node, which only accepts`"enabled"`

/`"disabled"`

; the driver ignored the numeric write while the API still reported success. The state now changes as expected, and a rejected write returns a real error instead of a generic success.

Fixed

`amd-smi process`

hiding compute processes owned by other users.A caller without permission to read another process’s

`/proc/<pid>/fd`

was misdetected as running in a separate PID namespace, which caused the whole compute-process list to come back empty. Such processes are now listed with a redacted (`N/A`

) name instead of being dropped.

Fixed CU%/SDMA column alignment in the

`amd-smi`

process table.The

`SDMA`

header no longer sits a column left of its values, and valid`CU %`

/`SDMA`

values are no longer truncated.

Fixed compute processes being reported on every GPU.

A process was attributed to a GPU whenever it had a KFD context on that GPU, so a job with queues on a single GPU appeared under every GPU. Attribution now uses the process’s active KFD queues plus any GPU where it holds a non-zero VRAM allocation, so a process is listed only against the GPUs it actually uses.


Fixed

`amd-smi`

hanging in`amdsmi_init()`

on UALink systems when the IFoE driver is unresponsive.`amdsmi_init()`

(and every CLI command) opened a per-GPU IFoE/UALoE fabric session up front, so it blocked indefinitely when the Broadcom IFoE driver was unresponsive, even for queries that never use fabric data.The fabric session is now opened only on the first fabric query, so initialization and non-fabric queries no longer touch the IFoE driver.


Fixed ctypes

`DeprecationWarning`

from`amdsmi_wrapper.py`

on Python 3.14.Python 3.14 deprecates the implicit ctypes structure layout when

`_pack_`

is set (slated to become an error in 3.19). Each packed structure/union in the generated wrapper now sets`_layout_ = 'ms'`

, preserving the existing MSVC-compatible layout (no ABI change) while silencing the warning.


**Composable Kernel** (1.2.0)[#](https://rocm.docs.amd.com#composable-kernel-1-2-0)

##### Added[#](https://rocm.docs.amd.com#added)

Multiple D (bias) and large tensor support to the CK Tile quantized GEMM kernel for row-column quantization.


##### Changed[#](https://rocm.docs.amd.com#id1)

Improved performance of row-column quantized a8w8 GEMM through better instruction scheduling in the eight-waves pipeline, wider epilogue stores, and nontemporal C/D memory access.


**HIP** (10.0.0)[#](https://rocm.docs.amd.com#hip-10-0-0)

##### Added[#](https://rocm.docs.amd.com#id2)

New HIP APIs

Stream Ordered Memory Allocator: support for API parity with corresponding CUDA API.

`hipMemGetDefaultMemPool`

returns the default memory pool for the specified location and allocation type

Cooperative Groups scan functions are now supported, providing feature parity with CUDA.

`cooperative_groups::exclusive_scan`

performs an exclusive prefix scan across the threads in a cooperative group. For each thread, the result is computed from the values of all preceding threads using a binary operation (addition by default), excluding the current thread’s own value.`cooperative_groups::inclusive_scan`

performs an inclusive prefix scan across the threads in a cooperative group. For each thread, the result includes the current thread’s value in addition to the values of all preceding threads.


Stream capture support for the following APIs, enabling

`BatchMemOp`

operations to be captured as graph nodes instead of executing immediately. Also improved`BatchMemOp`

graph replay reliability through fixes to parameter handling and operation ordering, aligning behavior more closely with CUDA.`hipStreamWaitValue32`

`hipStreamWaitValue64`

`hipStreamWriteValue32`

`hipStreamWriteValue64`

`hipStreamBatchMemOp`


Support Non-Uniform Memory Access (NUMA) in

`hipMemCreate`

related APIs. HIP runtime added virtual memory support for`hipMemLocationTypeHostNuma`

and`hipMemLocationTypeHostNumaCurrent`

APIs. This enables NUMA-aware memory allocations backed by host CPU NUMA pools and aligns HIP virtual memory management behavior with CUDA host and host-NUMA VMM expectations.

##### Optimized[#](https://rocm.docs.amd.com#id3)

Improved

`hipMemcpy2D()`

and`hipMemcpy2DAsync()`

performance for copy operations with very small row widths and large row counts. Previously, non-4-byte-aligned row or slice pitches could cause the runtime to issue a separate copy for each row, resulting in significant performance degradation for workloads such as 1-byte-wide transfers with millions of rows. These transfers are now handled using a single shader-based copy operation, significantly reducing transfer times. Copy operations at or below the 256-row threshold are unchanged.Improved

`hipEventRecord`

performance by using the`hipEventDisableTiming`

flag to avoid unnecessary profiling when timing information is not required. Event operations are now coalesced to eliminate redundant barrier submissions, reducing runtime overhead and improving execution efficiency.Improved batch copy performance: optimized

`hipMemcpyBatchAsync`

by splitting batch operations into per-device commands.Simplified

`rocrCopyBufferBatch`

by using a single`src_agent`

per engine group (H2D, D2H, and D2D).Streamlined batch grouping:

Removed the

`AgentGroup/src_agent`

mapping for D2D broadcasts.Processed

`H2D`

and`D2H`

LINEAR operations directly, bypassing the broadcast map.



##### Resolved issues[#](https://rocm.docs.amd.com#id4)

Resolved library loading error messages thrown by

`rocminfo`

during driver initialization in WSL (Windows Subsystem for Linux) environment due to failure in loading the HSA runtime library`libhsa-runtime64.so`

since it is not available in the dynamic linker search path. Since`rocminfo`

already links against`libhsa-runtime64.so`

, the runtime now correctly locates and loads the HSA runtime library using`RTLD_NOLOAD`

option, enabling successful ROCm initialization, HSA agent discovery, and subsequent ROCm operations.Fixed a segmentation fault in HIP queue idle detection caused by referencing a recycled completion signal. Idle state is now derived from a queue-owned signal with a safe lifetime.

Resolved incorrect NaN handling in the ordered not-equal comparison intrinsics

`__hne`

(for`__half`

) and`__hne`

(for`__hip_bfloat16`

), along with their vector forms. Being*ordered*predicates, they now correctly return`false`

when either operand is NaN.Resolved memory-safety issues in the ROCm code object and ELF loader by adding validation checks during code object module loading, preventing segmentation faults and improving runtime stability.

Resolved a memory leak affecting mipmapped arrays when using

`hipMemcpy2DToArray`

with levels obtained via`hipGetMipmappedArrayLevel`

. Mipmap level references are now properly released, ensuring that memory is correctly freed when`hipFreeMipmappedArray`

is called.Fixed a deadlock that could occur when using ROCprofiler-sdk with ROCm-aware MVAPICH and MPICH. HIP runtime now performs profiler registration after dispatch table initialization, ensuring proper initialization ordering and guard release. This prevents hangs caused by reentrant initialization during profiler startup.

Fixed a deadlock caused by

`hipMemMap`

/`hipMemUnmap`

operations on the null stream that could lead to hangs. The HIP runtime now implements proper synchronization to all devices with access to a mapped pointer before unmapping it.Fixed an issue in

`cooperative_groups::reduce()`

that could cause incorrect results or kernel launch failures when block dimensions had .y or .z components not equal to 1.

**hipBLAS** (3.6.0)[#](https://rocm.docs.amd.com#hipblas-3-6-0)

##### Added[#](https://rocm.docs.amd.com#id5)

Per-batch

`alpha`

/`beta`

support for Level 2 batched and strided-batched forms of`symv`

,`hemv`

,`sbmv`

and`spmv`

via`hipblasSetBatchAlphaStride`

and/or`hipblasSetBatchBetaStride`

(device pointer mode).Per-batch

`alpha`

support for Level 2 batched and strided-batched forms of`syr`

via`hipblasSetBatchAlphaStride`

(device pointer mode).Per-batch

`alpha`

(scalar vector) API support for Level 1 batched and strided-batched forms of`scal`

and the`_ex`

forms through`hipblasSetBatchAlphaStride`

when`hipblasHandle_t`

is in mode`HIPBLAS_POINTER_MODE_DEVICE`

.

##### Resolved issues[#](https://rocm.docs.amd.com#id6)

PyTorch users can avoid user-constraint-based memory allocation failures (

`HIPBLAS_STATUS_ALLOC_FAILED`

) by exporting`HIPBLAS_WORKSPACE_CONFIG=:0:0`

to allow rocBLAS managed memory to grow automatically.

**hipCUB** (4.6.0)[#](https://rocm.docs.amd.com#hipcub-4-6-0)

##### Added[#](https://rocm.docs.amd.com#id7)

Feature parity with CCCL/CUB 3.0.0.

`::hip::std`

support.

##### Changed[#](https://rocm.docs.amd.com#id8)

Changed

`CCCL_MINIMUM_VERSION`

to`3.0.0`

to align with CUB.Add support for large num_items

`DeviceMerge`

and`DeviceSegmentedSort`

.Replace

`#pragma unroll`

by`_CCCL_PRAGMA_UNROLL_FULL()`

and`_CCCL_PRAGMA_NOUNROLL()`

by`_CCCL_PRAGMA_NOUNROLL()`

.Add

`_CCCL_SORT_MAYBE_UNROLL()`

in block merge sort and thread sort.Update

`WarpExchange`

template parameters for CUB compatibility.

##### Removed[#](https://rocm.docs.amd.com#removed)

hipCUB compatibility with PyTorch v2.9 and v2.10 has been removed in this release. Use PyTorch v2.11 or later.

Removed

`hipcub::BaseTraits::CATEGORY`

,`hipcub::BaseTraits::nullptr_TYPE`

and`hipcub::BaseTraits::PRIMITIVE`

.Removed

`ConstantInputIterator`

,`CountingInputIterator`

,`DiscardOutputIterator`

and`TransformInputIterator`

, which were deprecated in hipCUB-4.1.0.Removed

`DeviceSpmv`

, which was removed from CUB after CCCL’s 2.8.0 release. Use`hipSPARSE`

or`rocSPARSE`

libraries instead.Removed

`GridBarrier`

.Removed

`HIPCUB_MIN`

,`HIPCUB_MAX`

,`HIPCUB_QUOTIENT_FLOOR`

,`HIPCUB_QUOTIENT_CEILING`

,`HIPCUB_ROUND_UP_NEAREST`

and`HIPCUB_ROUND_DOWN_NEAREST`

which were deprecated in hipCUB-4.1.0.Removed

`LEGACY_PTX_ARCH`

.Removed

`hipcub:max`

and`hipcub:min`

, which were deprecated. Use`hip::std::max`

and`hip::std::min`

instead.Deprecated

`hipcub::Swap`

, use`rocprim::swap`

instead.Deprecated

`HIPCUB_IS_INT128_ENABLED`

, use`_CCCL_HAS_INT128()`

instead.Deprecated

`hipcub::Equality`

,`hipcub::Inequality`

,`hipcub::InequalityWrapper`

,`hipcub::Sum`

,`hipcub::Difference`

,`hipcub::Division`

,`hipcub::Max`

and`hipcub::Min`

operators. Use`hip::std::equal_to`

,`hip::std::not_equal_to`

,`hip::std::plus`

,`hip::std::minus`

,`hip::std::divides`

,`hip::maximum`

, and`hip::minimum`

operators instead.

**hipFFT** (1.0.25)[#](https://rocm.docs.amd.com#hipfft-1-0-25)

##### Changed[#](https://rocm.docs.amd.com#id9)

Minor internal changes.


**hipFile** (0.4.0)[#](https://rocm.docs.amd.com#hipfile-0-4-0)

##### Added[#](https://rocm.docs.amd.com#id10)

A KFD-based alternative check for P2P DMA support was added to

`ais-check`

. This inspects the`capability`

property under`/sys/class/kfd/kfd/topology/nodes/*/properties`

.Guides for setting up storage targets to the documentation.


##### Changed[#](https://rocm.docs.amd.com#id11)

`ais-check`

now lists the AIS-capable file system mounts detected on the system and fails if none are found.Fastpath-only tests are now automatically skipped on systems that do not support the AIS fastpath instead of failing. Running ctest in verbose mode (

`ctest -V`

) will provide the reason the test was skipped.Updated INSTALL.md to point to official install docs.


**hipSOLVER** (3.6.0)[#](https://rocm.docs.amd.com#hipsolver-3-6-0)

##### Changed[#](https://rocm.docs.amd.com#id12)

Minor internal changes.


**hipSPARSE** (4.7.0)[#](https://rocm.docs.amd.com#hipsparse-4-7-0)

##### Added[#](https://rocm.docs.amd.com#id13)

Blocked ELL format support to the

`hipsparseDenseToSparse`

routine, along with the new`hipsparseBlockedEllSetPointers`

function.The

`HIPSPARSE_SPMV_CSR_ALG3`

algorithm to`hipsparseSpMV`

, which exposes the rocSPARSE CSR nnz split algorithm (`rocsparse_spmv_alg_csr_nnzsplit`

).CSC format support to

`hipsparseSpSV`

and`hipsparseSpSM`

.

##### Resolved issues[#](https://rocm.docs.amd.com#id14)

Fixed an issue with

`hipsparseSpMM`

, which produced incorrect results for the Blocked ELL sparse format.

**MIOpen** (3.6.0)[#](https://rocm.docs.amd.com#miopen-3-6-0)

##### Added[#](https://rocm.docs.amd.com#id15)

Gfx950 (MI350X/MI355X) 7x7 depthwise forward and backward-data convolution support (fp16/bf16), fixing a slow fallback-to-naive-kernel regression in ConvNeXt-style depthwise convolutions.


##### Changed[#](https://rocm.docs.amd.com#id16)

Restored gfx12x support in the Winograd Rage solver, recovering performance that regressed when earlier gfx12 support was reverted.

Refreshed the gfx1100, gfx1102, and gfx1201 (Navi) SystemDBs with updated tuned find/perf-database entries.

Refreshed the gfx950 SystemDB with additional tuned entries to cover more models.


##### Removed[#](https://rocm.docs.amd.com#id17)

Removed the OpenCL (OCL) backend; MIOpen now supports the HIP backend only.


##### Resolved Issues[#](https://rocm.docs.amd.com#id18)

Fixed an off-by-stride indexing bug in the backward CalcStats mean/variance remainder loop that caused a ~1% systematic bias in NCHW batch normalization backward results.

Fixed an integer overflow in tensor operation kernels for large allocations that could cause memory access faults.

Fixed a naive convolution solver failure mode where a global work size of 2^32 or more work-items silently failed to launch and left a stale HIP error visible after Find returned success; such launches are now rejected up front.


**RCCL** (2.30.7)[#](https://rocm.docs.amd.com#rccl-2-30-7)

##### Added[#](https://rocm.docs.amd.com#id19)

Compatibility with NCCL 2.30.7.

Scalable AllGatherV pattern: grouped

`ncclBroadcast`

calls with distinct roots are fused into a single ring kernel, improving performance at large scale. Gated by`NCCL_ALLGATHERV_ENABLE`

(default off).GPU-only multi-segment registration for symmetric memory windows, enabling contiguous VA ranges backed by multiple physical segments (single-node validated).

Elastic Buffer support for symmetric windows spanning device and host/

`HOST_NUMA`

memory segments (`NCCL_ELASTIC_BUFFER_REGISTER`

,`NCCL_SYM_REUSE_SYSMEM_HANDLES`

). Single-node path validated; multi-node registration remains limited pending HIP/HSA multi-segment DMA-BUF export support.

##### Changed[#](https://rocm.docs.amd.com#id20)

Adapted the device-initiated GIN backends (Anvil SDMA and rocSHMEM GDA) to the NCCL 2.30.7 GIN API v14:

Added the new

`getGinProperties`

host op.Dropped the data-path ops (

`iput`

/`iputSignal`

/`iget`

/`iflush`

/`test`

) that moved out of GIN under the GIN/RMA split.Switched

`createContext`

to`ncclGinConfig_v14_t`

.Updated the device dispatch signatures, and matched the GIN type renumbering (

`ROCSHMEM_GDA`

and`ANVIL_SDMA`

shifted after the new`GIN_GPI`

type).The plugins now use the generic (unversioned)

`ncclGin_t`

/`ncclGinConfig_t`

/`ncclGinProperties_t`

typedefs so future ABI bumps do not require touching call sites.

Updated the ROCSHMEM GIN plugin registration to the v14 layout (corrected struct field names and the conditional that previously only compiled without ROCSHMEM GIN).

Adapted the InfiniBand transports (

`net_ib`

and`net_ib_cast`

) to the v14 GIN/RMA split: the host/proxy backend is now registered as an`ncclRma_t`

vtable (`RMA_IB_PROXY`

) that owns the`iput`

/`iputSignal`

/`iget`

/`iflush`

/`test`

data-path ops, with GIN layered on top through the generic`ncclGinProxy`

.

##### Known issues[#](https://rocm.docs.amd.com#known-issues)

The improved AllGatherV support breaks the NCCL profiler support for ncclBroadcast operations, limiting visibility to API events.

`NCCL_ALLGATHERV_ENABLE=0`

can be used as a workaround until it is fixed in a future release.Multi-node multi-segment and Elastic Buffer symmetric-window registration is not yet enabled; NET and LSA+GIN multi-segment paths depend on runtime support for exporting contiguous DMA-BUF handles across all physical segments.


**rocBLAS** (5.6.0)[#](https://rocm.docs.amd.com#rocblas-5-6-0)

##### Added[#](https://rocm.docs.amd.com#id21)

Per-batch

`alpha`

/`beta`

support for Level 2 batched and strided-batched`symv`

,`hemv`

,`sbmv`

, and`spmv`

via`rocblas_set_batch_alpha_stride`

and`rocblas_set_batch_beta_stride`

(device pointer mode).Per-batch

`alpha`

support for Level 2 batched and strided-batched`syr`

via`rocblas_set_batch_alpha_stride`

(device pointer mode).Per-batch

`alpha`

(scalar vector) API support for Level 1`scal_batched`

,`scal_strided_batched`

, and their`_ex`

forms through`rocblas_set_batch_alpha_stride`

when`rocblas_handle`

is in`rocblas_pointer_mode_device`

.Support custom build with CMake arguments

`BUILD_WITH_HIPBLASLT_ONLY=ON`

that bypasses legacy Tensile.

##### Upcoming changes[#](https://rocm.docs.amd.com#upcoming-changes)

Deprecated the

`ROCBLAS_USE_HIPBLASLT_BATCHED`

environment variable. Recent optimizations mean hipBLASLt no longer needs to be disabled for batched operations only. This environment variable is planned for removal in a future release.

**rocDecode** (1.9.0)[#](https://rocm.docs.amd.com#rocdecode-1-9-0)

##### Added[#](https://rocm.docs.amd.com#id22)

Invalid video size handling for AVC/HEVC.


##### Resolved issues[#](https://rocm.docs.amd.com#id23)

Fixed decode errors of some AVC interlaced container streams by adding support for the picture data packet from the demuxer which contains multiple pictures.

Corrected fake CTest passes.


**rocFFT** (1.0.39)[#](https://rocm.docs.amd.com#rocfft-1-0-39)

##### Added[#](https://rocm.docs.amd.com#id24)

Optional ROCm Communication Collectives Library (RCCL) backend for single-node multi-GPU communication, enabled via

`-DROCFFT_RCCL_ENABLE=ON`

.

##### Changed[#](https://rocm.docs.amd.com#id25)

Relaxed the usage requirements for

`rocfft_setup`

and`rocfft_cleanup`

.Removed the ROCFFT_RTC_PROCESS_HELPER debug environment variable.


##### Optimized[#](https://rocm.docs.amd.com#id26)

Improved performance of unit-strided, interleaved, real-to-complex FFTs on gfx1201, gfx90a, gfx942, and gfx950 for the following lengths:

(100,100,100)

(192,96,96)

(200,96,96)

(128,128,256)

(160,168,168)

(160,168,192)

(168,168,192)

(168,192,192)

(192,192,192)

(192,192,200)

(192,200,200)

(200,200,200)

(216,216,216)

(216,104,100)

(216,104,104)

(224,104,104)

(224,108,104)

(224,108,108)



##### Resolved issues[#](https://rocm.docs.amd.com#id27)

Addressed internal issues causing multi-device plans to fall back to the least-performant code path for certain 3D real transforms (e.g., multi-device single-precision real out-of-place 3D of size 320x320x320 using slab decomposition).

Fixed a thread-safety issue that could cause

`rocfft_plan_create`

to crash when called concurrently from many threads.

**ROCgdb** (16.3)[#](https://rocm.docs.amd.com#rocgdb-16-3)

##### Added[#](https://rocm.docs.amd.com#id28)

The address space operator

`#`

is recognized in Fortran programs too. This allows evaluating expressions like`private_lane#0x08`

in Fortran applications that offload kernels to an AMD GPU.

**rocJPEG** (1.7.0)[#](https://rocm.docs.amd.com#rocjpeg-1-7-0)

##### Added[#](https://rocm.docs.amd.com#id29)

`rocJpegDecodeAsync`

and`rocJpegDecodeSync`

APIs to support asynchronous single-image JPEG decoding, allowing decode submission and completion to be separated across threads for improved pipeline throughput.

**ROCm Compute Profiler** (3.8.0)[#](https://rocm.docs.amd.com#rocm-compute-profiler-3-8-0)

##### Added[#](https://rocm.docs.amd.com#id30)

`--pc-sampling-rows`

analyze option to cap the PC sampling table at the top N rows (default 10); set`0`

to show all. Must be non-negative.`--overwrite`

profile mode option to explicitly allow replacing existing workload output.Experimental Triton support to ML API tracing. Profile with

`--experimental --triton-trace`

to emit a ROCTX marker per Triton/Inductor kernel launch attributed to the user call site, and analyze with`--experimental --list-triton-operators`

or`--experimental --triton-operator <pattern>`

to list or filter Triton operators independently of Torch.Support for GPU metrics on gfx1153 hardware.


##### Changed[#](https://rocm.docs.amd.com#id31)

Split Python version requirements by mode. Profile mode now runs on Python 3.8+ (standard library only). Analyze mode requires Python 3.9+ and exits with a clear message on older interpreters instead of failing with an import error.

`--pc-sampling-sorting-type`

now defaults to`count`

(was`offset`

), so the PC sampling table shows the most-sampled instructions first.Renamed the

`Pct of Peak`

/`PoP`

analysis column to`Percent of Peak`

in analysis output.`--torch-trace`

now wraps the tensor methods`to`

,`cpu`

,`cuda`

, and`contiguous`

by default. Previously these wraps were enabled by setting`ROCPROFCOMPUTE_ROCTX_DEEP_TENSOR_WRAPS=1`

. Set`ROCPROFCOMPUTE_ROCTX_DEEP_TENSOR_WRAPS=0`

(or`false`

,`no`

,`off`

) to disable them.Renamed the torch-trace output files and directory from

`torch_trace_*`

to`ml_api_trace_*`

.Profile mode now errors when the target workload directory is non-empty unless

`--overwrite`

is passed.`--bench-only`

likewise requires`--overwrite`

before replacing an existing`roofline.csv`

.Renamed

`num_hbm_channels`

to`num_memory_channels`

in machine specifications to unify memory channel reporting across GPU families.

##### Removed[#](https://rocm.docs.amd.com#id32)

Removed the multi-node analysis options

`--nodes`

,`--list-nodes`

(analyze mode) and the experimental`--spatial-multiplexing`

option (profile and analyze modes). These features did not work as expected and will be redesigned in a future release.

##### Optimized[#](https://rocm.docs.amd.com#id33)

Improved GPU Benchmarking and Roofline profiling/analysis support for gfx1150/gfx1151/gfx1152 architectures.

gfx11xx supports Wave Matrix Multiply Accumulate (WMMA), replacing MFMA operations.



##### Resolved issues[#](https://rocm.docs.amd.com#id34)

The Dual VALU (VOPD) instruction mix metric is now reported for gfx115x in the WGP panel.

Fixed multi-user roofline benchmarking on shared systems: the per-GPU lock file under

`/tmp/rocprof-compute-benchmark/`

is now created world-readable/writable (0666) so any user can acquire it, regardless of which user created it first or the active umask. Stale unreadable lock files left by older versions in a sticky`/tmp`

cannot be repaired automatically and must be removed manually by their owner or an administrator.Fixed CDNA memory chart CLI output to show the numbered

`3. Memory Chart`

header without repeating the default per-kernel normalization label.

##### Known issues[#](https://rocm.docs.amd.com#id35)

Workloads profiled with earlier versions must be re-profiled before analysis. The sysinfo schema changed and older workload directories are not compatible.

CLI mode block 4 Roofline plot’s legend will not appear if there are too many kernels to list, in relation to the user’s terminal size. Same per-kernel roofline rate metrics and AI plot point details can be read in block 4’s preceding tables.


**ROCm Systems Profiler** (1.8.0)[#](https://rocm.docs.amd.com#rocm-systems-profiler-1-8-0)

##### Added[#](https://rocm.docs.amd.com#id36)

hipFile (GPU-direct storage) API tracing. Add

`hipfile_api`

to`ROCPROFSYS_ROCM_DOMAINS`

(shorthand:`hipfile`

) to capture hipFile API traces. Requires ROCprofiler-SDK version 1.3.5 or later.`--exe-only`

flag for`rocprof-sys-instrument`

: shorthand for excluding every shared library from instrumentation, leaving only the main executable.`--exclude-internal-lib-paths`

flag for`rocprof-sys-instrument`

: by default, each internal library is excluded only at the path linked at startup; when enabled, every on-disk path matching an internal library’s filename is excluded.`--max-library-functions`

option for`rocprof-sys-instrument`

: skips shared libraries whose procedure count exceeds the given threshold, keeping instrumentation overhead manageable. The target executable is never gated by this, and the check is bypassed by the module include/restrict (`--module-include`

/`-MI`

,`--module-restrict`

/`-MR`

) and function include/restrict (`--function-include`

/`-I`

,`--function-restrict`

/`-R`

) regexes.rocSHMEM host-stream API tracing via

`ROCPROFSYS_ROCM_DOMAINS=rocshmem_api`

. ROCm Systems Profiler now captures the nine host-stream rocSHMEM API calls (`putmem_on_stream`

,`getmem_on_stream`

,`putmem_signal_on_stream`

,`signal_wait_until_on_stream`

,`broadcastmem_on_stream`

,`alltoallmem_on_stream`

,`barrier_all_on_stream`

,`sync_all_on_stream`

,`quiet_on_stream`

) as`rocm_rocshmem_api`

spans in Perfetto traces and rocpd databases. Requires rocprofiler-sdk >= 1.3.4 and rocSHMEM >= 3.6.0 (included in ROCm 10.0.0). As of rocSHMEM 3.6.0,`USE_ROCPROFILER_REGISTER`

defaults to`ON`

, so package installations automatically include this support. A`rocshmem`

example demonstrating two-PE usage of all nine APIs is included under`examples/rocshmem`

.

##### Changed[#](https://rocm.docs.amd.com#id37)

`ROCPROFSYS_BUILD_TESTING`

no longer implies`ROCPROFSYS_BUILD_EXAMPLES`

.Introduced the new

`profiler-hub`

writer backend for trace persistence, as a replacement for the existing SQLite3/rocpd backend.

##### Removed[#](https://rocm.docs.amd.com#id38)

Removed the

`-p`

/`--pid`

option from`rocprof-sys-instrument`

for attaching to an already running process. Use the`rocprof-sys-attach`

executable instead, which attaches to and profiles running processes via the ROCprofiler-SDK`rocattach`

API.Removed

`--parse-all-modules`

from`rocprof-sys-instrument`

. The tool iterates through objects and modules to extract the functions by default.

**rocPRIM** (4.6.0)[#](https://rocm.docs.amd.com#rocprim-4-6-0)

##### Added[#](https://rocm.docs.amd.com#id39)

A parallel

`device_topk`

, which finds the largest/smallest K elements from an input array of keys.A parallel

`device_segmented_topk`

, which finds the largest/smallest K elements from segmented groups.`device_topk`

and`device_segmented_topk`

are now controlled by the CMake flag`ROCPRIM_ENABLE_TOPK`

. Set`-DROCPRIM_ENABLE_TOPK=ON`

to enable these features.

##### Changed[#](https://rocm.docs.amd.com#id40)

Combined and simplified separate assertion templates using

`std::is_floating_point`

,`rocprim::half`

, and`rocprim::bfloat16`

to use`rocprim::is_floating_point`

.

**ROCprofiler-SDK** (1.3.5)[#](https://rocm.docs.amd.com#rocprofiler-sdk-1-3-5)

##### Added[#](https://rocm.docs.amd.com#id41)

**API:**

rocSHMEM host-stream API interception for the rocSHMEM tracing domain introduced in 1.3.0:

`rocshmem_putmem_on_stream`

,`rocshmem_getmem_on_stream`

, and`rocshmem_alltoallmem_on_stream`

are intercepted and emitted as per-call trace records.Records are interleaved with HIP, HSA, RCCL, and other runtime traces so rocSHMEM communication activity can be viewed on the same timeline as GPU compute.


hipFile API tracing as a first-class tracing domain:

hipFile API calls are intercepted through dispatch-table wrapping and emitted as per-call trace records alongside HIP, HSA, and other runtime activity.

Enables file I/O operations to be correlated with GPU kernels and memory copies in a single profiling timeline.


Streaming Performance Monitor (SPM) counter data in the rocpd output format:

SPM records are stored as

`rocpd_track`

rows labelled`SPM`

, with counter values grouped by timestamp into`rocpd_sample`

rows and per-dimension data in`rocpd_pmc_event`

rows.The rocpd schema gains the

`sample_id`

,`xcc`

,`shader_engine`

, and`instance`

columns.SPM data is consumable by any tool that reads the rocpd database and is convertible to CSV via

`rocpd convert`

. Conversion to the other output formats, such as Perfetto and OTF2, is not yet supported.


**rocprofv3 (CLI):**

OpenMP (OMPT) tracing via the new

`--ompt-trace`

flag:Accepts a bare boolean or a space-separated category list (

`all`

`thread`

`parallel`

`task`

`sync`

`mutex`

`target`

`device`

`error`

), following the same style as`--pmc`

and`--output-format`

; for example,`--ompt-trace parallel task target sync`

. Categories must be space-separated; comma-separated tokens are rejected. Also folded into`--sys-trace`

/`--runtime-trace`

.rocpd-only trace: records go to the rocpd database (the default output format) and are exported via

`rocpd convert`

.The OMPT callback layer is already supported by ROCprofiler-SDK; this flag makes it accessible without writing a custom tool.


hipFile API tracing via the new

`--hipfile-trace`

flag (or the`ROCPROF_HIPFILE_API_TRACE`

environment variable):Automatically included in

`--runtime-trace`

and`--sys-trace`

.Records are emitted across all supported output backends: CSV, JSON, Perfetto, OTF2, and rocpd.


Container-aware

`rocattach`

symbol resolution: attach entry points are resolved directly from the target process mapped ELF, and tool paths are validated from the target’s perspective before injection. This allows attaching from a host to a containerized process without manually copying`.so`

files.

##### Changed[#](https://rocm.docs.amd.com#id42)

Previously,

`rocattach`

calculated symbol offsets from the host’s`librocprofiler-register.so`

and applied them to the target’s mapping, which failed when the host and container libraries differ in ELF layout or path. Offsets are now resolved from the target process itself.Idle inline queues with no active profiling consumers now bypass queue interposition entirely, reducing overhead for applications that create queues but do not immediately dispatch work.

DWARF information is now parsed lazily, reducing startup overhead for attach and tracing sessions on large binaries.

Disabled autoflush in thread trace to prevent premature buffer flushes that produced incomplete or corrupted traces.

Bump rocpd schema to version 3.0.1 which supports NIC agent types.

Bump rocpd schema to version 3.0.2 for HIP graph per-node attribution (

`graph_exec_id`

/`graph_node_id`

columns on`rocpd_kernel_dispatch`

/`rocpd_memory_copy`

and the new`rocpd_graph_launch`

table). The pre-graph-attribution 3.0.1 schema is now frozen under`versions/3.0.1/`

per the rocpd schema versioning scheme.Bump rocpd schema to version 3.0.3 for SPM support. The pre-spm-support 3.0.2 schema is now frozen under

`versions/3.0.2/`

per the rocpd schema versioning scheme.

##### Removed[#](https://rocm.docs.amd.com#id43)

Dependency on

`libatomic`

. The library was previously linked unconditionally through the`rocprofiler-sdk-atomic`

interface target, which caused link failures on toolchains and container images where`libatomic1`

is not installed. The single`std::atomic`

use that required it has been replaced with explicit memory-ordering synchronization; behavior is unchanged.

##### Resolved issues[#](https://rocm.docs.amd.com#id44)

A GPU stall in device thread trace that occurred when thread trace was started before

`hsa_init()`

.A counter-collection stall caused by an

`InterceptQueue`

ordering bug, and fixed an out-of-bounds write in`Submit()`

.`roctxMark`

calls propagating as kernel rename labels, which caused spurious kernel name changes in traces containing ROCTx markers.SQ aliasing on harvested WGPs and multi-counter desync on gfx11xx targets in AQLprofile, and corrected the

`GcEaSeCounterBlockMaxEvent`

value.A guard to prevent double-initialization of the PC sampling service.

`rocprofv3`

attach sessions exiting before all buffered output was flushed; attach sessions now block until the flush completes.The ordering of code object callbacks during attach, which could race with tools that depend on ordered delivery.

The

`fmt/format.h`

include path, the`fpic`

flag for samples, OMP lookup in CI, and clang-tidy quickscan enablement.

##### Known issues[#](https://rocm.docs.amd.com#id45)

SPM sessions can remain in a stale state after abrupt termination. See

[GitHub issue #6489](https://github.com/ROCm/rocm-systems/issues/6489)for details.

**rocRAND** (5.0.0)[#](https://rocm.docs.amd.com#rocrand-5-0-0)

##### Removed[#](https://rocm.docs.amd.com#id46)

Removed

`h_scrambled_sobol(32|64)_constants`

,`rocrand_h_scrambled_sobol(32|64)_direction_vectors`

,`rocrand_h_sobol(32|64)_direction_vectors`

from public namespace.

**rocSHMEM** (3.6.0)[#](https://rocm.docs.amd.com#rocshmem-3-6-0)

##### Added[#](https://rocm.docs.amd.com#id47)

New APIs:

`rocshmem_broadcast_wave`

`rocshmem_fcollect_wave`

`rocshmem_alltoall_wave`

`rocshmem_reduce_wave`

`rocshmem_reducescatter_wave`


Support for some tile-granular collectives for the IPC backend:

`rocshmem_tile_broadcast`

`rocshmem_tile_broadcast_wave`

`rocshmem_tile_broadcast_wg`

`rocshmem_ctx_tile_broadcast`

`rocshmem_ctx_tile_broadcast_wave`

`rocshmem_ctx_tile_broadcast_wg`

`rocshmem_tile_allgather`

`rocshmem_tile_allgather_wave`

`rocshmem_tile_allgather_wg`

`rocshmem_ctx_tile_allgather`

`rocshmem_ctx_tile_allgather_wave`

`rocshmem_ctx_tile_allgather_wg`


Single node support for gfx1250 / MI455X.

Support for HIP Fabric Handles.


##### Changed[#](https://rocm.docs.amd.com#id48)

Dropped LLC dependency when compiling HSCO objects.


**rocSOLVER** (3.36.0)[#](https://rocm.docs.amd.com#rocsolver-3-36-0)

##### Added[#](https://rocm.docs.amd.com#id49)

64-bit APIs for the symmetric/Hermitian eigensolvers:

SYEV_64 and HEEV_64 (with batched and strided_batched versions)

SYEVD_64 and HEEVD_64 (with batched and strided_batched versions)


Support added for the gfx1250 architecture.


##### Changed[#](https://rocm.docs.amd.com#id50)

Clarified the

`geblttrf_npvt`

API documentation to accurately describe the in-place LU block-factorization storage.

##### Known issues[#](https://rocm.docs.amd.com#id51)

The 64-bit eigensolver APIs (SYEV_64, HEEV_64, SYEVD_64, HEEVD_64) require the matrix dimensions

`n`

and`lda`

to fit within a 32-bit integer, because their internal tridiagonal reduction and back-transformation steps remain 32-bit.

**rocSPARSE** (5.0.0)[#](https://rocm.docs.amd.com#rocsparse-5-0-0)

##### Added[#](https://rocm.docs.amd.com#id52)

Blocked ELL format support to the

`rocsparse_dense_to_sparse`

routine, including the new`rocsparse_bell_set_pointers`

function to set the Blocked ELL array pointers.CSC format support to

`rocsparse_spsv`

and`rocsparse_sptrsv`

.CSC format support to

`rocsparse_spsm`

and`rocsparse_sptrsm`

.`rocsparse_handle_create`

to create a handle associated with a user-provided stream. All internal device memory allocation and initialization are stream-ordered on that stream, so handle creation never blocks the calling thread or other GPU streams.`rocsparse_handle_destroy`

to destroy a handle created by`rocsparse_handle_create`

, with an optional error descriptor argument.

##### Changed[#](https://rocm.docs.amd.com#id53)

`rocsparse_spmm`

with CSR/CSC and the default algorithm (`rocsparse_spmm_alg_default`

or`rocsparse_spmm_alg_csr`

) now automatically selects a load-balanced (nnz-split) kernel for strongly skewed matrices (those containing a single very long row for CSR, or column for transposed CSC). Behavior is unchanged for non-skewed matrices and for explicit algorithm choices (`rocsparse_spmm_alg_csr_row_split`

,`rocsparse_spmm_alg_csr_nnz_split`

,`rocsparse_spmm_alg_csr_merge_path`

).

##### Removed[#](https://rocm.docs.amd.com#id54)

The deprecated

`rocsparse_indextype_u16`

enum.

##### Resolved issues[#](https://rocm.docs.amd.com#id55)

Fixed an issue with

`rocsparse_spmm`

, which produced incorrect results for the Blocked ELL sparse format.

##### Upcoming changes[#](https://rocm.docs.amd.com#id56)

Deprecated the

`rocsparse_spildlt0_input_diag`

enum value. It was used to dump the diagonal`D`

of the ILDLT(0) factorization, which is now stored in-place on the diagonal entries of the`L`

factor. It will be removed in a future release.

**rocThrust** (4.6.0)[#](https://rocm.docs.amd.com#rocthrust-4-6-0)

##### Added[#](https://rocm.docs.amd.com#id57)

Largely in feature parity with CCCL/thrust v3.0.3.

`thrust::tuple`

,`thrust::pair`

and`thrust::zip_iterator`

fall back to rocThrust 4.4.0 implementations when a libhipcxx counterpart corresponding to CCCL/libcudacxx >= v3.0.3 is unavailable.`thrust::tuple`

and`thrust::pair`

: some features may differ from CCCL/thrust v3.0.3.`thrust::zip_iterator`

: some iterator concepts present in CCCL/thrust v3.0.3 are missing.



##### Removed[#](https://rocm.docs.amd.com#id58)

rocThrust compatibility with PyTorch v2.9 and v2.10 has been removed in this release. Use PyTorch v2.11 or later.


## ROCm breaking changes[#](https://rocm.docs.amd.com#rocm-breaking-changes)

### AMD SMI API and ABI changes[#](https://rocm.docs.amd.com#amd-smi-api-and-abi-changes)

The AMD SMI library introduced the following breaking changes in the 10.0.0 release: API-incompatible changes, which require source code changes before your code will compile, and ABI-incompatible changes, which require recompilation even if your code doesn’t change. It also deprecated several APIs and enums that remain functional in ROCm 10.0 but are scheduled for removal in a future release.

#### ABI-incompatible changes[#](https://rocm.docs.amd.com#abi-incompatible-changes)

##### Library SONAME[#](https://rocm.docs.amd.com#library-soname)

Change |
Impact |
|---|---|
The library major version is now 27.0.0, so the shared library SONAME is |
Consumers linked against |

`amdsmi_gpu_metrics_t`

field type widening[#](https://rocm.docs.amd.com#amdsmi-gpu-metrics-t-field-type-widening)

The following fields in `amdsmi_gpu_metrics_t`

changed from `uint32_t`

to `uint64_t`

to support next generation AMD Instinct counter ranges:

`gfx_activity_acc`

`mem_activity_acc`

`pcie_nak_sent_count_acc`

`pcie_nak_rcvd_count_acc`

`pcie_lc_perf_other_end_recovery`


Recompile any code that reads these fields. Any assignments into fixed-width 32-bit variables must be updated to use 64-bit types.

#### API-incompatible changes[#](https://rocm.docs.amd.com#api-incompatible-changes)

The AMD SMI library removed or changed the following APIs, types, and defines in this release. Certain items have been removed with or without a replacement; see the following tables for details.

##### Removed APIs[#](https://rocm.docs.amd.com#removed-apis)

Removed |
Replacement |
|---|---|
|
No replacement. Reload the driver out of band with |
|
|
|
|

##### Removed Python output fields[#](https://rocm.docs.amd.com#removed-python-output-fields)

Removed |
Replacement |
|---|---|
|
|

##### Changed signatures[#](https://rocm.docs.amd.com#changed-signatures)

API |
Change |
|---|---|
|
Returns |

##### Types[#](https://rocm.docs.amd.com#types)

Removed |
Replacement |
|---|---|
|
Moved inside |
|
|

##### Renamed defines[#](https://rocm.docs.amd.com#renamed-defines)

Public preprocessor macros in `amdsmi.h`

are now prefixed with `AMDSMI_`

. The Python interface
constant `MAX_NUMBER_OF_AFIDS_PER_RECORD`

is renamed to match.

Old name |
New name |
|---|---|
|
|
|
|
|
|
|
|
|
|

##### Removed defines[#](https://rocm.docs.amd.com#removed-defines)

These macros were unreferenced by any API or structure and have no replacement.

Removed |
|---|
|
|
|
|
|
|
|
|
|
|

#### AMD SMI deprecations[#](https://rocm.docs.amd.com#amd-smi-deprecations)

These APIs and enums are still present in ROCm 10.0 and are slated for removal in a future release. The Python bindings emit a `DeprecationWarning`

where applicable.

##### Deprecated APIs[#](https://rocm.docs.amd.com#deprecated-apis)

Deprecated |
Replacement |
|---|---|
|
|
|
|
|
|
|
|
|
|
|
|
|
|

##### Deprecated enums and enumerators[#](https://rocm.docs.amd.com#deprecated-enums-and-enumerators)

The old names are retained as aliases with unchanged values and are slated for removal in a future release.

Deprecated |
Replacement |
|---|---|
|
|
|
|
|
|
|
|
|
|
|
|

## ROCm known issues[#](https://rocm.docs.amd.com#rocm-known-issues)

ROCm known issues are noted on [GitHub](https://github.com/ROCm/TheRock/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22Verified%20Issue%22). These issues will be fixed in a future ROCm release. For known issues related to individual components, review the [ROCm component changelogs](https://rocm.docs.amd.com#rocm-component-changelogs).

### HuggingFace model training throughput might regress on AMD Instinct MI350X[#](https://rocm.docs.amd.com#huggingface-model-training-throughput-might-regress-on-amd-instinct-mi350x)

HuggingFace model training workloads might see 9–25% lower training throughput on AMD Instinct MI350X (gfx950) GPUs, including BART, GPT-2, DiT (Diffusion Transformers), BERT, Llama 2 70B Chat, and RoBERTa-large. This occurs because AOTriton 0.13b selects a suboptimal flash-attention backward kernel instead of the faster 3-kernel split used in AOTriton 0.11.2b. As a workaround, rebuild PyTorch and pin AOTriton to version 0.11.2b. See [GitHub issue #7696](https://github.com/ROCm/TheRock/issues/7696).

### JAX BERT FP16 training might encounter a segmentation fault on some Radeon GPUs[#](https://rocm.docs.amd.com#jax-bert-fp16-training-might-encounter-a-segmentation-fault-on-some-radeon-gpus)

JAX BERT FP16 training workloads might encounter a segmentation fault on some AMD Radeon graphics products, such as the Radeon PRO W7900, causing training to terminate unexpectedly. As a workaround, disable XLA GPU command buffers by setting the `XLA_FLAGS="--xla_gpu_enable_command_buffer="`

environment variable before launching the workload. See [GitHub issue #7697](https://github.com/ROCm/TheRock/issues/7697).

### PyTorch training and fine-tuning workloads might experience GPU resets or crashes on some Radeon GPUs[#](https://rocm.docs.amd.com#pytorch-training-and-fine-tuning-workloads-might-experience-gpu-resets-or-crashes-on-some-radeon-gpus)

PyTorch training and fine-tuning workloads using Llama-Factory or Unsloth might experience GPU resets or application crashes on some AMD Radeon graphics products, such as the Radeon RX 9070 Series and Radeon AI PRO R9700. As a workaround, set the `TORCH_BLAS_PREFER_HIPBLASLT=0`

environment variable to disable hipBLASLt for training and fine-tuning workloads. This workaround might result in performance degradation. See [GitHub issue #7699](https://github.com/ROCm/TheRock/issues/7699).

### SGLang inference might fail with the default AITER attention backend on some Radeon GPUs[#](https://rocm.docs.amd.com#sglang-inference-might-fail-with-the-default-aiter-attention-backend-on-some-radeon-gpus)

SGLang inference workloads using the default AITER attention backend might fail on some AMD Radeon graphics products, such as the Radeon PRO W7900, Radeon AI PRO R9700, and Radeon RX 9070 XT. As a workaround, configure SGLang to use the Triton attention backend (`--attention-backend triton`

) or disable AITER:

```
export SGLANG_USE_AITER=0
export SGLANG_USE_AITER_AR=0
```

See [GitHub issue #7700](https://github.com/ROCm/TheRock/issues/7700).

### TensorFlow ROCm v2.21 might fail to start with a libhipsparse ImportError on some Radeon GPUs[#](https://rocm.docs.amd.com#tensorflow-rocm-v2-21-might-fail-to-start-with-a-libhipsparse-importerror-on-some-radeon-gpus)

TensorFlow ROCm v2.21 workloads might fail to start with an `ImportError: libhipsparse.so.4`

on some AMD Radeon graphics products, such as Radeon AI PRO R9700, when ROCm is installed using pip packages. As a workaround, add `$(hipconfig -R)/lib`

and `$(hipconfig -R)/lib/rocm_sysdeps/lib`

to `LD_LIBRARY_PATH`

before launching TensorFlow. See [GitHub issue #7701](https://github.com/ROCm/TheRock/issues/7701).

### vLLM or ComfyUI workloads might crash on some Ryzen AI systems[#](https://rocm.docs.amd.com#vllm-or-comfyui-workloads-might-crash-on-some-ryzen-ai-systems)

Intermittent segmentation faults or GPU hangs might be observed when running some vLLM or ComfyUI workloads on Ryzen AI systems using gfx1103 (RDNA3) GPUs. See [GitHub issue #7702](https://github.com/ROCm/TheRock/issues/7702).

### Concurrent rocprofv3 profiling causes node reset on AMD Instinct MI300A GPUs[#](https://rocm.docs.amd.com#concurrent-rocprofv3-profiling-causes-node-reset-on-amd-instinct-mi300a-gpus)

Running `rocprofv3 --pmc`

or `--kernel-trace`

concurrently across multiple GPUs of a single AMD Instinct MI300A node might hard-reset the node, terminating all co-resident jobs and requiring a manual power cycle to recover. As a workaround, rebuild ROCprofiler-SDK from the [ROCm/rocm-systems](https://github.com/ROCm/rocm-systems/tree/develop/projects/rocprofiler-sdk)`develop`

branch, which includes the fix. See [GitHub issue #8229](https://github.com/ROCm/TheRock/issues/8229).

## ROCm resolved issues[#](https://rocm.docs.amd.com#rocm-resolved-issues)

The following notable issues have been fixed in ROCm 10.0.0.

### ASAN produced incorrect results with ternary operators on struct kernel arguments[#](https://rocm.docs.amd.com#asan-produced-incorrect-results-with-ternary-operators-on-struct-kernel-arguments)

Previously, when compiling GPU kernels with ASAN enabled, ternary operators with struct kernel arguments could produce incorrect results, masking real bugs and producing false-positive results during memory-safety validation.

### GPU kernels failed to launch in ASAN builds with large thread counts[#](https://rocm.docs.amd.com#gpu-kernels-failed-to-launch-in-asan-builds-with-large-thread-counts)

Previously, when building GPU libraries with ASAN enabled, kernels configured with large thread counts could fail to launch, returning the `HSA_STATUS_ERROR_INVALID_ISA`

error.

### Multi-target GPU builds produced larger binary sizes[#](https://rocm.docs.amd.com#multi-target-gpu-builds-produced-larger-binary-sizes)

Previously, applications targeting multiple AMD GPU architectures could produce significantly larger binaries. Multi-target builds could increase binary size by up to 54%, and single-target builds added approximately 8 MB per GPU target.

### HIP applications stalls on Windows during high-volume memory pool allocation and deallocation[#](https://rocm.docs.amd.com#hip-applications-stalls-on-windows-during-high-volume-memory-pool-allocation-and-deallocation)

Previously, HIP applications on Windows that performed many memory pool allocation and deallocation cycles could stall indefinitely while waiting for a memory-mapping operation to complete on the GPU. This was most commonly observed while running the rocBLAS test suite on Windows.

## ROCm upcoming changes[#](https://rocm.docs.amd.com#rocm-upcoming-changes)

Future releases will add support for:

Additional ROCm Core SDK components.

Domain-specific expansion toolkits (data science, life sciences, finance, simulation, and other HPC domains).

More AMD hardware support.