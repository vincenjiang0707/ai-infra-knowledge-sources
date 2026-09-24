# cuda-toolkit-13-4-adds-windows-on-arm-support-and-greater-control-over-shared-gpus

source: https://developer.nvidia.com/blog/cuda-toolkit-13-4-adds-windows-on-arm-support-and-greater-control-over-shared-gpus/

Every NVIDIA [CUDA Toolkit](https://developer.nvidia.com/cuda/toolkit) release adds functionality and performance improvements that help developers get more from NVIDIA GPUs and the broader NVIDIA software platform.

CUDA Toolkit 13.4 adds support for Windows on Arm. CUDA applications have long been supported on Arm platforms through Linux; this release extends that capability to the Windows on Arm platform.

The release also introduces early developer support for the NVIDIA Rubin GPU architecture, enhanced GPU management capabilities, expanded CUDA Python and CCCL functionality, and updates across NVIDIA Nsight developer tools and core math libraries.

## CUDA 13.4 enhancements

Additional enhancements in CUDA 13.4 are detailed in this section.

### Developer access to NVIDIA Rubin as a preview

CUDA Toolkit 13.4 adds functional support for the NVIDIA Rubin architecture (compute capability 107) as a preview, enabling developers to begin porting applications before CUDA support for Rubin reaches general availability in a future release of the CUDA Toolkit. Rubin is the next-generation GPU architecture [powering the era of agentic AI](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/).

### Multi-Process Service V3

Multi-process server (MPS) V3 introduces a modernized control layer for CUDA MPS, simplifying the automation and management of shared GPU resources. This update provides developers and orchestration layers with a scriptable CLI, named server instances, and namespaces to organize concurrent workloads. It also adds TOML configuration support, streaming multiprocessor (SM) partition controls, and cgroup-integrated GPU memory limits. These capabilities enable precise GPU partitioning, where compute performance, memory boundaries, and execution priority are defined programmatically. This release ensures that MPS integrates into containerized environments, maximizing hardware utilization while maintaining strict resource isolation for every process. To get started with MPS V3, see the [quickstart](https://docs.nvidia.com/deploy/mps/latest/quick-start.html) and full [documentation](https://docs.nvidia.com/deploy/mps/latest/mpsv3-interface.html).

## CUDA Compute Fabric Transport

CUDA Compute Fabric Transport (CFT) introduces a transport-centric way for advanced applications and communication libraries to move data across NVIDIA NVLink fabric at scale. Instead of mapping every remote GPU allocation into a process’s virtual address space, software can target named logical endpoints using an endpoint ID and offset, then issue asynchronous put, get, and reduction operations directly from the GPU.

This approach reduces virtual-address pressure in large multi-GPU systems, supports unicast and multicast communication patterns, and reports completion and error status so applications can detect, retry, or reroute failed fabric transfers.

CFT is only available through the CUDA Driver API and is intended for communication-library developers who need very specific functionality not available from higher-level communications libraries. Most application developers are best served using libraries such as NVIDIA [NCCL](https://developer.nvidia.com/nccl) or [NVSHMEM](https://developer.nvidia.com/nvshmem). To learn more, see the [CUDA Programming Guide](https://docs.nvidia.com/cuda/cuda-programming-guide/04-special-topics/compute-fabric-transport.html).

### Locality domains

CUDA 13.4 exposes programmatic access to locality domains. A locality domain is a portion of a GPU that contains streaming multiprocessors (SMs) and device memory. An application can allocate device memory in a locality domain and create a green context with SM resources in the same locality domain. Co-locating computation near the memory it accesses can improve performance on devices with more than one locality domain. For more information about how to query and use locality domains, see the [CUDA Programming Guide.](https://docs.nvidia.com/cuda/cuda-programming-guide/04-special-topics/locality-domains.html)

### Querying the location of unified memory

API support for querying residency information for unified memory gives performance-sensitive libraries and runtimes a direct way to understand where managed or system-allocated data currently resides. Unified memory makes heterogeneous programming simpler, but high-performance software still needs locality awareness to avoid unnecessary page migrations, remote memory accesses, or inefficient staging paths. With residency queries, CUDA applications and libraries make smarter decisions about where and when to schedule computations and data movement. To learn more, see the API reference for [cudaMemGetLocationInfo](https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/group__CUDART__MEMORY.html#_CPPv414cudaMemGetInfoP6size_tP6size_t).

### Decoupling the CUDA driver and the CUDA toolkit

CUDA SDK installers no longer bundle the NVIDIA driver. Install the appropriate `nvidia-open`

driver or `cuda-toolkit`

packages separately, using your preferred package manager.

### Coherent Driver-based Memory Management default for coherent platforms

On NVIDIA coherent platforms like NVIDIA Grace Hopper, NVIDIA Grace Blackwell, and NVIDIA Vera Rubin, the driver now defaults to Coherent Driver-based Memory Management (CDMM) instead of NUMA. NUMA mode remains fully supported and can be selected with a kernel module parameter. If you plan to use it, make the change before upgrading. This is a node-wide setting that requires a driver reload or reboot. The mode should be selected before upgrading. For more info on CDMM, see the post [Understanding Memory Management on Hardware-Coherent Platforms](https://developer.nvidia.com/blog/understanding-memory-management-on-hardware-coherent-platforms/) and [white paper](https://dam-cdn.nvd.orangelogic.com/AssetLink/77dn7clj03ib0kiritw143238xspfu4b.pdf).

### Compilers/NVCC

Host compiler compatibility now includes GCC 16 and Clang 22 on supported host platforms. The new SM_107 architecture target enables compilation for Rubin GPUs.

## CUDA Python

CUDA Python expands Pythonic access to core CUDA APIs and high-performance algorithms, with updates to development tools, memory management, graph workflows, and application portability.

### cuda.core

Following the release of CUDA Python 1.0, cuda.core 1.1.0 has expanded the stable Pythonic CUDA API with texture and surface programming, richer managed-memory control, improved CUDA graph integration, and complete type information for development tools and agents.

For the complete list of changes, [see the cuda.core 1.1.0 release notes](https://nvidia.github.io/cuda-python/cuda-core/1.1.0/release/1.1.0-notes.html).

#### Texture and surface programming

The new `cuda.core.texture`

module provides first-class Python APIs for CUDA texture and surface memory. `OpaqueArray`

and `MipmappedArray`

represent hardware-laid-out GPU allocations, while `TextureObject`

enables bindless, hardware-filtered kernel reads, and `SurfaceObject`

enables typed kernel-side loads and stores. The following example creates an opaque CUDA array and binds it to a texture object for hardware-filtered kernel reads.

`from` `cuda.core ` `import` `Device` `from` `cuda.core.texture ` `import` `(` ` ` `OpaqueArrayOptions,` ` ` `ResourceDescriptor,` ` ` `TextureObjectOptions,` `)` `from` `cuda.core.typing ` `import` `ArrayFormatType, FilterModeType` `dev ` `=` `Device()` `dev.set_current()` `stream ` `=` `dev.create_stream()` `with dev.create_opaque_array(` ` ` `OpaqueArrayOptions(` ` ` `shape` `=` `(` `1024` `, ` `1024` `),` ` ` `format` `=` `ArrayFormatType.FLOAT32,` ` ` `num_channels` `=` `1` `,` ` ` `)` `) as array:` ` ` `array.copy_from(image, stream` `=` `stream)` ` ` `resource ` `=` `ResourceDescriptor.from_opaque_array(array)` ` ` `options ` `=` `TextureObjectOptions(filter_mode` `=` `FilterModeType.LINEAR)` ` ` `with dev.create_texture_object(` ` ` `resource` `=` `resource,` ` ` `options` `=` `options,` ` ` `) as texture:` ` ` `# Pass texture.handle to a CUDA C++ kernel.` ` ` `run_kernel(texture.handle)` |

#### NUMA-aware managed memory

`ManagedMemoryResource.allocate()`

now returns a `ManagedBuffer`

with a property-based interface for CUDA memory advice. Applications can configure read-mostly data, preferred placement, and processor access.

The new `Host`

type complements `Device`

when specifying memory locations. It can represent any host memory, a particular NUMA node, or the NUMA node associated with the calling thread.

The following example configures managed-memory placement and access, prefetches data to a GPU, and then moves the output to host memory.

`from` `cuda.core ` `import` `Device, Host, ManagedMemoryResource` `from` `cuda.core.utils ` `import` `prefetch_batch` `dev ` `=` `Device()` `dev.set_current()` `stream ` `=` `dev.create_stream()` `mr ` `=` `ManagedMemoryResource()` `weights ` `=` `mr.allocate(weights_nbytes, stream` `=` `stream)` `output ` `=` `mr.allocate(output_nbytes, stream` `=` `stream)` `weights.read_mostly ` `=` `True` `weights.preferred_location ` `=` `dev` `weights.accessed_by.add(dev)` `prefetch_batch(stream, [weights, output], dev)` `# Launch GPU work, then move the result to host memory.` `output.prefetch(Host(), stream` `=` `stream)` `stream.sync()` |

### Improved development and graph workflows

`cuda.core 1.1`

provides `.pyi`

type stubs for every public API, giving IDEs autocompletion and coding agent access to type information, function signatures, return types, and more.

Among many CUDA graph workflow improvements, `GraphBuilder.graph_definition`

exposes a captured graph as a `GraphDefinition`

. Developers can use this to combine stream capture with explicit graph construction, including inspecting or extending a captured graph.

Other additions include device-specific NVLink enumeration, expanded green-context workqueue configuration, path-like inputs for Program and ObjectCode, and a public Buffer.size property. The release also strengthens IPC validation, free-threaded Python correctness, and CUDA process checkpoint restoration.

### cuda.compute

`cuda.compute`

provides Pythonic access to NVIDIA CUDA Core Compute Libraries (CCCL) high-performance, customizable GPU algorithms, including sort, scan, reduce, transform, and more.

`cuda.compute 1.1`

enables ahead-of-time (AoT) compilation of algorithm objects for multiple GPU architectures, including on build systems without a GPU. `ProxyArray`

and `ProxyValue`

describe argument types without allocating device memory, while `serialize()`

creates an artifact that can be stored and deployed. On the target system, `deserialize()`

restores the algorithm without recompiling and loads the build matching the current GPU architecture.

The following example compiles a reduction for sm_80 and sm_90 without requiring a GPU, then saves it for later deployment.

`import` `numpy as np` `from` `cuda.compute ` `import` `(` ` ` `OpKind,` ` ` `ProxyArray,` ` ` `ProxyValue,` ` ` `make_reduce_into,` ` ` `serialize,` `)` `reducer ` `=` `make_reduce_into(` ` ` `d_in` `=` `ProxyArray(np.int32),` ` ` `d_out` `=` `ProxyArray(np.int32),` ` ` `op` `=` `OpKind.PLUS,` ` ` `h_init` `=` `ProxyValue(np.int32),` ` ` `compute_capability` `=` `[` `80` `, ` `90` `], ` `# Build for sm_80 and sm_90.` `)` `with ` `open` `(` `"reduce.cclb"` `, ` `"wb"` `) as ` `file` `:` ` ` `file` `.write(serialize(reducer))` |

## CCCL

CUDA 13.4 ships with CCCL 3.4, featuring a faster `cub::DeviceScan`

on NVIDIA Blackwell GPUs, single-call APIs across CUB device-wide algorithms, batched warp reductions, and familiar C++ Standard Library parallel algorithms in `cuda::std`

.

### Faster device-wide scans on NVIDIA Blackwell GPUs

A new warp-specialized implementation of `cub::DeviceScan`

for Blackwell is available. The implementation uses the Tensor Memory Accelerator (TMA) to overlap memory movement and computation while reducing synchronization overhead.

In benchmark results on an NVIDIA Blackwell GPU, the new `cub::DeviceScan::Sum`

implementation reaches up to 92% memory-bandwidth utilization (from up to around 50% in a previous implementation) across the tested data types. The implementation is optimized for large scan workloads while retaining fallbacks for unsupported architectures, data types, iterators, and toolchains.

### Single-call APIs for CUB device-wide algorithms

CCCL 3.4 completes the rollout of environment-based, single-call overloads across CUB device-wide algorithms. Previously, applications typically called a CUB algorithm once to determine its temporary storage requirements, allocated that storage, and then called the algorithm again to perform the operation. The new overloads obtain temporary storage from a memory resource supplied through an execution environment. For more information, see [Streamlining CUB with a Single-Call API](https://developer.nvidia.com/blog/streamlining-cub-with-a-single-call-api/) and the [CUB device-wide primitive documentation](https://nvidia.github.io/cccl/cub/api_docs/device_wide.html).

The following example creates an execution environment with a CUDA stream and memory pool, then runs a reduction without manually managing temporary storage.

`auto device = cuda::devices[0];` `auto stream = cuda::stream{device};` `auto pool = cuda::device_default_memory_pool(device);` `auto env = cuda::std::execution::env{` ` ` `cuda::stream_ref{stream},` ` ` `pool` `};` `cub::DeviceReduce::Sum(d_input, d_output, num_items, env);` |

This reduces boilerplate while centralizing control over how an algorithm executes and obtains temporary storage. The traditional two-phase APIs are not deprecated and remain available to applications that require explicit storage management.

### Batched reductions within a warp

A new CUB warp-wide collective, `cub::WarpReduceBatched`

, is introduced for reducing multiple independent batches of values distributed across a warp. It processes the batches together, minimizing shuffle operations and increasing the amount of useful work performed by each warp.

### Parallel C++ Standard Library algorithms on the GPU

CUDA 13.4 introduces the C++ Standard Library parallel-algorithm model in `cuda::std`

. Developers can invoke dozens of familiar algorithms, including `copy_if`

, `find_if`

, `merge`

, reduce, transform, and scan operations using the `cuda::execution::gpu`

execution policy.

The following example uses the GPU execution policy to copy positive values from one device-accessible range to another.

`#include <cuda/std/algorithm>` `#include <cuda/std/execution>` `struct is_positive` `{` ` ` `__host__ __device__` ` ` `bool operator()(int value) const` ` ` `{` ` ` `return value > 0;` ` ` `}` `};` `cuda::std::copy_if(` ` ` `cuda::execution::gpu,` ` ` `d_first,` ` ` `d_last,` ` ` `d_output,` ` ` `is_positive{}` `);` |

The algorithms operate on device-accessible ranges and use CCCL and CUB implementations underneath. This gives CUDA C++ developers a standard, recognizable interface for GPU execution while retaining access to CUDA-specific features such as streams and memory resources through customizable execution policies. See the [cuda::std parallel-algorithm documentation](https://nvidia.github.io/cccl/unstable/libcudacxx/standard_api/algorithms_library.html) for more details.

## Programmatic Dependent Launch comes to CUDA Tile IR

Support for Programmatic Dependent Launch (PDL) to CUDA Tile IR enables inter-kernel overlap on the same CUDA stream, for a dependent kernel to begin execution before its predecessor completes. See the CUDA Tile IR [Release Notes](https://docs.nvidia.com/cuda/tile-ir/latest/sections/release_notes.html) to learn more about these operations.

## New views in CUDA Tile C++

CUDA Tile C++ introduces additional views for loading and storing data.

[Strided view](https://docs.nvidia.com/cuda/cuda-tile-cpp-api-reference/strided_view.html)creates statically-sized chunks of data where the spacing between chunks is determined by a compile-time striding factor. This facilitates data access patterns often found in stencil-like operations.[Gather scatter view](https://docs.nvidia.com/cuda/cuda-tile-cpp-api-reference/gather_scatter_view.html)supports accessing non-adjacent chunks of an array. This facilitates accessing data with sparse access patterns.

## Developer tools

A number of developer tools enhancements follow.

### Nsight Python

Nsight Python 1.0 is a Python kernel profiling interface that automates performance analysis across multiple kernel configurations using NVIDIA Nsight Tools. A decorator and context manager enable kernel benchmarking, architectural metric collection, GPU-throttling prevention, and performance visualization in one script. No boilerplate. No manual report parsing. Nsight Python delivers scalable architectural metrics—not just wall-clock timings—with minimal code overhead.

### NVIDIA Nsight Compute

Nsight Compute 2026.3 adds Tile IR support for CUDA Tile workloads, for developers to inspect Tile IR in the source page and correlate it with CUDA Tile source and generated code. The release also improves register-spill information for OptiX workloads and enhances Nsight Copilot.

### NVIDIA Nsight Systems

Nsight Systems 2026.5.1 expands platform coverage and workload visibility across CUDA, CPUs, AI frameworks, networking, and storage. The web release adds support for CUDA 13.4, Rubin GPUs, and Windows on Arm. It also projects the NVTX range into an “All Streams” hierarchy, demangles cuTile names, and displays CUDA workloads submitted through CiG streams on the timeline.

CPU metric sets group related hardware counters for collection in a single pass, helping developers progressively isolate bottlenecks through Topdown metric sets. For PyTorch workloads, the new `--pytorch=functions-trace-shapes`

option adds information such as tensor shapes and training parameters to traced functions. Developers can choose between the additional detail provided by shape tracing and the lower overhead of the existing function-tracing option.

#### Network, storage, and cluster profiling

Network profiling adds high-frequency NIC metric collection through the NVIDIA DOCA Telemetry Service, enabling developers to correlate traffic, congestion notifications, and send waits with application activity without requiring elevated privileges. A new NCCL straggler analysis recipe analyzes collective timing to identify ranks that repeatedly delay communicator progress. See the [Nsight Systems User Guide](https://docs.nvidia.com/nsight-systems/UserGuide/index.html) and [Post-Collection Analysis Guide](https://docs.nvidia.com/nsight-systems/AnalysisGuide/index.html) for collection requirements and recipe usage.

Storage profiling now includes an [S3 access summary analysis recipe](https://docs.nvidia.com/nsight-systems/AnalysisGuide/index.html#s3-access-sum-recipe) that aggregates access patterns and I/O statistics across processes and hosts, helping identify hot buckets and objects, frequent small transfers, and workload imbalances. NVIDIA SCADA metrics profiling brings counters and histograms from the SCaled Accelerated Data Access storage architecture into the timeline, where developers can correlate storage-server activity with GPU and CPU events.

For multi-node and cluster profiling and analysis, the experimental vClock plugin improves report alignment without changing system clocks or requiring privileged access when high-precision synchronization such as PTP is unavailable.

#### Binary payloads and plugin development

NVTX binary payloads can now be exported as dynamic relational tables, with payload fields represented as columns for downstream analysis in SQLite, Arrow, and Arrow/Parquet formats. The Nsight Systems plugin framework also adds an initialization stage, a process-exit callback API, and plugin-library loading in subprocesses. Developers can initialize collection before the application begins, capture data generated during shutdown, and extend profiling coverage across child processes.

### NVIDIA Nsight Cloud

Nsight Cloud makes it easier to view and analyze profiling reports on remote, headless systems. Nsight Operator adds improvements for analysis, OpenTelemetry, and NVIDIA Dynamo, along with a new documentation site.

### NVIDIA Nsight AI

Nsight AI brings specialized AI assistance into accelerated computing development workflows. The NVIDIA-hosted CUDA MCP Server connects supported AI coding agents to current CUDA documentation and code examples, while the open-source Nsight Copilot Blueprint provides a self-hosted CUDA AI backend for teams that prefer to deploy and operate it in their own environment.

### NVIDIA Compute Sanitizer

Compute Sanitizer ships with improved shared memory out-of-bounds detection with compile-time patching on Hopper and newer architectures. Initcheck now includes Batched memcpy async support and racecheck support for per-cluster-block filtering.

### NVIDIA Core Math Libraries

Core math libraries in CUDA Toolkit 13.4 now have functional support for the Rubin GPU architecture and Windows on Arm support for the N1X Laptop ecosystem.

Updates to cuBLAS in 13.4 include the following features:

- cuBLAS improves double-precision performance through fixed-point emulation using the Ozaki-II scheme.
- On Blackwell data center GPUs, cuBLASLt dynamically schedules Grouped GEMM computations across streaming multiprocessors (SMs) to minimize load imbalances in common MoE workloads. Compared to earlier toolkit releases, this approach improves performance for Grouped GEMM calls with many groups (e.g., 32). It can also improve performance when Grouped GEMM operations run concurrently with other device kernels.
- cuBLASLt adds experimental scaling modes
`CUBLASLT_MATMUL_MATRIX_SCALE_VEC32_MN_K4_UE8M0`

and`CUBLASLT_MATMUL_MATRIX_SCALE_VEC128_MN_K4_UE8M0`

that use an alternative scaling factor layout supporting`A`

and`B`

FP8-precision tensors. These modes pack scaling factors in groups of 4 and store them in M- or N-major layout. Padding is added whenever the major dimension is not divisible by 4. For more details, refer to the[docs](https://docs.nvidia.com/cuda/cublas/index.html#using-the-cublaslt-api).

## Get started with CUDA Toolkit 13.4

CUDA Toolkit 13.4 expands CUDA development with Windows on Arm support, preview support for the NVIDIA Rubin GPU architecture, updated GPU resource-management and communication capabilities, and enhancements across CUDA Python, CCCL, NVIDIA Nsight developer tools, and core math libraries.

Download [CUDA Toolkit 13.4](https://developer.nvidia.com/cuda-downloads) and review the CUDA Toolkit 13.4 release notes for the complete list of features, supported platforms, and compatibility information.

## Acknowledgments

*Thanks to the following NVIDIA contributors: Andy Terrel, Rob Armstrong, Jackson Marusarz, Mahender Hari, Becca Zandstein, Mridula Prakash, Daniel Rodriguez, Noah Stern.*

## Start the discussion at forums.developer.nvidia.com
