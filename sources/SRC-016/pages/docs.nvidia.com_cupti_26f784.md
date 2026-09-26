source: https://docs.nvidia.com/cupti/

# CUPTI[#](https://docs.nvidia.com#cupti)

The CUDA Profiling Tools Interface (CUPTI) provides C and Python APIs for building profiling and tracing tools for CUDA applications, providing detailed insight into how code executes on both the CPU and GPU.

## Overview[#](https://docs.nvidia.com#id1)

CUPTI exposes several APIs: Activity, Callback, Host Profiling, Range Profiling, PC Sampling, SASS Metric, PM Sampling, Checkpoint,
and Profiling APIs. These APIs let you build tools that capture execution timelines, correlate CPU and GPU work, and collect
performance metrics for CUDA applications. CUPTI is distributed as a dynamic library on all CUDA-supported platforms, and on
Linux (x86_64) and ARM server (arm64 SBSA) it is also available as a static library.
The CUPTI package includes several [samples](https://docs.nvidia.com/main/main.html#samples) that demonstrate the use of these APIs.
For step-by-step guidance on API usage, see the tutorial section of the documentation [tutorial](https://docs.nvidia.com/tutorial/tutorial.html),
which walks through common profiling and tracing workflows.

**Tracing**In this CUPTI documentation, tracing means collecting timestamps and associated metadata for CUDA activities such as runtime and driver API calls, kernel launches, and memory copy operations during application execution. Tracing highlights where time is spent in CUDA code and helps identify performance bottlenecks by showing which operations and code regions dominate execution time. Tracing data is gathered primarily through the Activity and Callback APIs. Activity records describe executed work (for example, kernels and memory operations), while callbacks notify your tool when specific CUDA events occur, enabling low-overhead, event-driven trace collection.

**Profiling**In this CUPTI documentation, profiling refers to collecting GPU performance metrics for individual kernels or sets of kernels, often in isolation from the rest of the workload. Profiling may require replaying kernels or even the full application multiple times to gather all desired metrics under controlled conditions. These metrics can be collected with the Range Profiling and Host Profiling APIs, which allow you to define ranges and associate metrics with specific kernel launches or code regions. Refer to the section

[Evolution of the profiling APIs](https://docs.nvidia.com/main/main.html#evolution-of-the-profiling-apis)for more details. Additional mechanisms include the SASS Metric API for source- and instruction-level metrics, the PM Sampling API for periodically sampling hardware performance monitors, and the PC Sampling API for periodic sampling of warp program counters and scheduler state to reveal stall reasons and control-flow behavior.

CUPTI API |
Feature Description |
Header |
|---|---|---|
Asynchronously record CUDA activities, e.g. CUDA API, Kernel, memory copy |
cupti_activity.h |
|
CUDA event callback mechanism to notify subscriber that a specific CUDA event executed e.g. “Entering CUDA runtime memory copy” |
cupti_callbacks.h |
|
Host APIs for enumeration, configuration and evaluation of performance metrics |
cupti_profiler_host.h |
|
Target APIs for collection of performance metrics for a range of execution |
cupti_range_profiler.h |
|
Sampling of the warp program counter and warp scheduler state (stall reasons) |
cupti_pcsampling.h |
|
Collect kernel performance metrics at the source level using SASS patching |
cupti_sass_metrics.h |
|
Collect hardware metrics by sampling the GPU performance monitors (PM) periodically at fixed intervals |
cupti_pmsampling.h |
|
Target APIs for collection of performance metrics for a range of execution. Host operations - enumeration, configuration and evaluation of metrics are supported by the Perfworks Metrics API. The Profiling API is deprecated in the CUDA 13.0 release, it is recommended to use the Range Profiling API. |
cupti_profiler_target.h nvperf_host.h |
|
Provides support for automatically saving and restoring the functional state of the CUDA device |
cupti_checkpoint.h |

CUPTI Python

CUPTI Python is a library that provides Python APIs for creating profiling and tracing tools specifically designed for CUDA Python applications.
The current release supports a subset of CUPTI C Activity and Callback APIs. It’s important to note that this library is available only for Linux (x86_64)
and Linux (aarch64 sbsa) platforms.
For developers interested in utilizing CUPTI Python, it’s recommended to refer to the official documentation at [https://pypi.org/project/cupti-python/](https://pypi.org/project/cupti-python/)
for more detailed information on its capabilities and usage instructions.

CUPTI Profiling API vs. NVIDIA Nsight Perf SDK

[CUPTI Profiling API](https://docs.nvidia.com/main/main.html#cupti-profiling-api) and [CUPTI Range Profiling API](https://docs.nvidia.com/main/main.html#range-profiling-api)
support profiling of CUDA kernels and these allow collection of GPU performance metrics for a particular kernel or range of kernels at
the CUDA context level. [NVIDIA Nsight Perf SDK](https://developer.nvidia.com/nsight-perf-sdk) supports graphics APIs
(i.e. DirectX, Vulkan, OpenGL) allowing collection of GPU performance metrics at graphics device, context and queue levels.
Both NVIDIA Nsight PerfSDK and CUPTI Profiling API share the host APIs (i.e. metrics enumeration, configuration and evaluation)
but differ in which GPU APIs they target on the device.

CUPTI Installation

The CUPTI SDK is included with the CUDA Toolkit and is installed alongside the other CUDA libraries.

Default installation locations:

Linux:

`/usr/local/cuda-<version>/extras/CUPTI/`

Windows:

`C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v<version>\extras\CUPTI\`


On Windows, CUPTI libraries (dll) are located as follows:

Before CUDA 13.4: in the

`lib64`

directory.CUDA 13.4 and later: in architecture-specific subdirectories. For example, x86-64 libraries are located in

`lib\x64\`

.

These directories are not added to the system runtime library search path by default. To use CUPTI at runtime, add the directory containing the CUPTI libraries to the appropriate environment variable:

On Linux, add the directory to

`LD_LIBRARY_PATH`

.On Windows, add the directory to

`PATH`

.