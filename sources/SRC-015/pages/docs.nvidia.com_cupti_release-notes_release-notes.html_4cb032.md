source: https://docs.nvidia.com/cupti/release-notes/release-notes.html

# 1. Release Notes[#](https://docs.nvidia.com#release-notes)

CUPTI Release Notes.

Release notes, including new features and important bug fixes. Supported platforms and GPUs.

## 1.1. Release Notes[#](https://docs.nvidia.com#id1)

### 1.1.1. Updates in CUDA 13.4 Update 1[#](https://docs.nvidia.com#updates-in-cuda-13-4-update-1)

**Resolved Issues**

Fixed unbounded CPU utilization growth during long-running activity tracing, improving performance stability for continuous GPU workload tracing.

Fixed a race condition in CUPTI HES mode that caused intermittent crashes during

`cudaGraphInstantiate`

by properly synchronizing related operations.Fixed a memory leak when HES is enabled that caused approximately 100 bytes of host memory to leak per kernel activity record.

Fixed a system crash and intermittent zero-valued timestamps in HES mode during concurrent context destruction.

Fixed a deadlock in kernel latency timestamp collection that could occur when a device buffer was allocated during kernel launch.

Fixed stale kernel names in activity records after module reloads.


### 1.1.2. Updates in CUDA 13.4[#](https://docs.nvidia.com#updates-in-cuda-13-4)

**New Features**

Added support for the Rubin GPU architecture.

Added support for Windows on Arm.

Fixed Clock Rate - Added APIs

`cuptiClockControlLock()`

and`cuptiClockControlUnlock()`

with`CUPTI_CLOCK_CONTROL_MODE_BASE`

or`CUPTI_CLOCK_CONTROL_MODE_BOOST`

to lock GPU clocks and eliminate clock-rate variability during profiling. Refer to the section[Fixed Clock Rate](https://docs.nvidia.com/main/main.html#fixed-clock-rate)for more details.Cache State Reset - Range Profiler can now reset L2 (or all) cache before each replay pass via the

`cacheControlMode`

field in`CUpti_RangeProfiler_Enable_Params`

. Refer to the section[Cache State Reset](https://docs.nvidia.com/main/main.html#cache-state-reset)for more details.Added

`sourceGraphId`

to provide the unique graph ID of the node from which the kernel node was instantiated or last updated and`sourceGraphNodeId`

which provides unique graph node ID of the node from which the kernel node was instantiated or last updated. The activity record`CUpti_ActivityKernel12`

is deprecated and replaced by`CUpti_ActivityKernel13`

.To ensure tracing and profiling accuracy, live vGPU migration is blocked while CUPTI is active and resumes only after

`cuptiFinalize()`

is called or the process exits.Per-cbid filtering for user-defined activity records -

`cuptiActivityEnable_v2`

now accepts a`pKindOptions`

field in`CUpti_ActivityConfig`

pointing to a`CUpti_ActivityApiOptions`

/`CUpti_ActivityApiCbidOptions`

struct to allow or deny specific callback IDs when enabling`CUPTI_ACTIVITY_KIND_RUNTIME`

or`CUPTI_ACTIVITY_KIND_DRIVER`

. The per-subscriber APIs`cuptiActivityEnableRuntimeApi_v2`

and`cuptiActivityEnableDriverApi_v2`

can also be used to dynamically update the filter after the kind has been enabled. Refer to the sample[cupti_user_defined_records](https://docs.nvidia.com/main/main.html#sample-cupti-user-defined-records)for usage.Added

`workqueueChannelCount`

and`workqueueChannelIds`

fields to the green context activity record to report the number of HW channels assigned to a green context’s work queue and their channel IDs, respectively. The activity record`CUpti_ActivityGreenContext2`

is deprecated and replaced by`CUpti_ActivityGreenContext3`

.CUPTI library installation path: For Windows, libraries are now placed under architecture-specific directories instead of the generic lib64 folder to support proper cross-compile support. For ex: on a x86_64 system, the CUPTI libraries are installed under C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA<version>\extras\CUPTI\lib\x64.


**Resolved Issues**

Per-subscriber timestamp callback registration via

`CUPTI_ACTIVITY_ATTR_TIMESTAMP_CALLBACK`

using`cuptiActivitySetAttribute_v2`

is now supported in multi-subscriber mode, allowing tools to register their own callbacks rather than sharing a common callback.Fixed issues that could occur after disabling user-defined records via the

`CUPTI_ACTIVITY_ATTR_USER_DEFINED_RECORDS`

attribute.Fixed an issue that sometimes causes a brief (~2 s) CUPTI block when disabling the

`CUPTI_ACTIVITY_KIND_UNIFIED_MEMORY_COUNTER`

activity.Fixed a host heap corruption issue that could occur when using CUPTI HES trace (

`cuptiActivityEnableHWTrace`

).Fixed CUPTI HES activity so that

`graphNodeId`

field retains the full graphId (upper 32-bits) in CUDA-graph memory copy records.

### 1.1.3. Updates in CUDA 13.3 Update 1[#](https://docs.nvidia.com#updates-in-cuda-13-3-update-1)

**Resolved Issues**

Added the green context ID to device graph trace records for activities executed on green contexts, replacing the primary context ID.

Fixed an issue that caused CUPTI to report incorrect UUIDs and missing metadata for MIG instances not visible to the current process. CUPTI now accurately reports device information for all MIG instances on the system, regardless of

`CUDA_VISIBLE_DEVICES`

settings.Fixed a segmentation fault that occurred when calling the

`cuptiIsTracingSessionEnabled`

API in CUDA Enhanced Compatibility environments.Fixed a potential crash caused by simultaneous GPU activity tracing requests in multi-subscriber mode.


### 1.1.4. Updates in CUDA 13.3[#](https://docs.nvidia.com#updates-in-cuda-13-3)

**New Features**

The

**User-Defined Activity Records**feature is transitioning from Beta to production in this release. For more details, refer to[CUPTI User-Defined Activity Records](https://docs.nvidia.com/main/main.html#activity-user-defined-records)and[CUDA tracing with User-Defined Activity Records](https://docs.nvidia.com/tutorial/tutorial.html#tutorial-activity-user-defined-records).The

**Multiple Subscribers for Activity Tracing**feature is transitioning from Beta to production in this release. For more details, refer to[Multiple Subscribers](https://docs.nvidia.com/main/main.html#multiple-subscribers).Added support for profiling workloads on Green Contexts with the new APIs

`cuptiRangeProfilerGetDevicePartitionInfo`

and`cuptiProfilerHostSetDevicePartitionInfo`

. These APIs enable retrieval and configuration of device partition information, ensuring accurate metric evaluation by accounting for partitioned device resources. The`cuptiRangeProfilerGetDevicePartitionInfo`

API retrieves partition information from the range profiler, while`cuptiProfilerHostSetDevicePartitionInfo`

applies this information to the profiler host for metric scaling.Enhanced the

`cuptiActivityEnableHWTrace`

API to allow invocation before CUDA driver initialization. After driver initialization, CUPTI may switch to semaphore-based tracing if HES based tracing is unsupported, with errors reported via callbacks in the`CUPTI_CB_DOMAIN_STATE`

domain.Added profiling support for previously unsupported SKUs, with reduced metric support, including GPUs such as RTX 6000D BSE (GB202-891), RTX 5090DD (GB202-240), and RTX 5090D (GB202-250). For more details, refer to

[ERR_NVGPU](https://developer.nvidia.com/ERR_NVGPU). To indicate this limited support, CUPTI has added the`CUPTI_PROFILER_CONFIGURATION_LIMITED_SUPPORT`

value to the`CUpti_Profiler_Support_Level`

enum to indicate limited support for these SKUs. When using the counter availability image, CUPTI will list all supported metrics during a query, and report an error for unsupported metrics during config image creation. If no counter availability image is provided, CUPTI will instead return NaN values for unsupported metrics when evaluating the counter data image.

**Resolved Issues**

Fixed an issue where repeatedly calling a CUPTI API could result in an overall performance drop. This issue was introduced in the CUDA 13.2 release.

Fixed a memory leak that occurred when tracing a CUDA graph containing memcpy or memset nodes, even when these activities were not enabled.


### 1.1.5. Updates in CUDA 13.2 Update 1[#](https://docs.nvidia.com#updates-in-cuda-13-2-update-1)

**New Features**

Added three new fields to the green context record:

`workqueueResourceId`

,`workqueueConcurrencyLimit`

and`workqueueSharingScope`

, which provide the resource ID, concurrency limit and sharing scope of the work queue, respectively. The activity record`CUpti_ActivityGreenContext`

has been deprecated and replaced by`CUpti_ActivityGreenContext2`

.

**Resolved Issues**

Removed usage of C++ features in the CUPTI public interface, which caused build issues on some platforms.


### 1.1.6. Updates in CUDA 13.2[#](https://docs.nvidia.com#updates-in-cuda-13-2)

**New Features**

**User-Defined Activity Records (Beta)**: CUPTI now supports user-defined activity records, allowing users to select specific fields for activity records instead of collecting complete predefined records. This feature addresses the limitations of fixed-field records by providing significant memory efficiency through custom field selection tailored to application-specific profiling needs. Key benefits include optimized memory usage by eliminating unused fields and padding, improved performance through compact data structures and faster data access, and improved backward compatibility as new fields can be added in future CUPTI versions without impacting existing user code. The feature is enabled using the`CUPTI_ACTIVITY_ATTR_USER_DEFINED_RECORDS`

attribute, and new APIs have been added to support this functionality. For detailed information, see[CUPTI User-Defined Activity Records](https://docs.nvidia.com/main/main.html#activity-user-defined-records)and[CUDA tracing with User-Defined Activity Records](https://docs.nvidia.com/tutorial/tutorial.html#tutorial-activity-user-defined-records).**Multiple Subscribers for Activity Tracing (Beta)**: CUPTI now supports multiple subscribers tracing CUDA activities simultaneously, enabling multiple CUPTI-based tools to collect independent activity traces from the same application using the new V2 APIs (`cuptiSubscribe_v2`

,`cuptiActivityEnable_v2`

, etc.). For detailed information, see[Multiple Subscribers](https://docs.nvidia.com/main/main.html#multiple-subscribers).Added tracing support for Memory Locality Optimized Partition (MLOPart) devices.

Added

`numTpcs`

parameter to device record to report the total number of Thread Processing Clusters (TPCs) in the device. The activity record`CUpti_ActivityDevice5`

is deprecated and replaced by`CUpti_ActivityDevice6`

.Added activity kind

`CUPTI_ACTIVITY_KIND_GREEN_CONTEXT`

and structure`CUpti_ActivityGreenContext`

to trace green context allocations, which enable GPU resource partitioning by assigning dedicated subsets of SMs and TPCs to specific contexts for fine-grained resource management and isolation. Starting from CUDA 13.2, CUPTI only emits`CUpti_ActivityGreenContext`

for green contexts and no longer emits`CUpti_ActivityContext`

for them.The

`portDev0`

and`portDev1`

fields in NVLink records are now dynamically allocated arrays, via malloc(), sized to`physicalNvLinkCount`

ports. Clients must release this memory using free() when no longer needed. The record`CUpti_ActivityNvLink4`

has been deprecated and replaced by`CUpti_ActivityNvLink5`

. This change is not backward compatible. Clients using CUDA 13.2 or later must update their code to use the new record structure.Introduced

`CUPTI_MAX_DEVICES`

macro in`cupti_common.h`

to represent the theoretical maximum number of devices supported by CUPTI.Added two new APIs to query single-pass metric sets and their constituent metrics for PM sampling:

`cuptiProfilerHostGetSinglePassSets()`

and`cuptiProfilerHostGetMetricsInSinglePassSet()`

. These APIs enable users to programmatically select metrics which can be collected in a single pass for PM sampling.

**Resolved Issues**

Report

`CUPTI_CBID_RESOURCE_GRAPH_NODE_SET_PARAMS`

callback for CUDA Graph nodes like memcpy, memset, host and event.

### 1.1.7. Updates in CUDA 13.1 Update 1[#](https://docs.nvidia.com#updates-in-cuda-13-1-update-1)

**Resolved Issues**

Fixed incorrect correlation IDs for

`cudaGraphLaunch`

API calls and their associated kernel launches in profiling sessions after the first session.Fixed issue where CUPTI graph creation callbacks were not triggered for CUDA device graphs under green context.

Fixed linker error when linking the static CUPTI library from CUDA 13.0 and 13.1 GA releases.

Fixed issue where CUPTI limited activity buffer records to 2GB regardless of the configured activity buffer size.


### 1.1.8. Updates in CUDA 13.1[#](https://docs.nvidia.com#updates-in-cuda-13-1)

**New Features**

Added support for Compute Engine context switch events. For more details, refer to the section

[Compute Engine Context Switch](https://docs.nvidia.com/main/main.html#activity-ce-context-switch).Added tracing for host execution nodes in CUDA Graphs i.e. nodes of type CU_GRAPH_NODE_TYPE_HOST. Enable with the activity kind

`CUPTI_ACTIVITY_KIND_GRAPH_HOST_NODE`

; records are reported as`CUpti_ActivityGraphHostNode`

.Added tracing for host launches done by CUDA through cudaLaunchHostFunc() API. This is important in understanding the device bubbles in the stream timeline. Enable with the activity kind

`CUPTI_ACTIVITY_KIND_HOST_LAUNCH`

; records are reported as`CUpti_ActivityHostLaunch`

.Users can query the collection scope for any metric. The

`CUpti_MetricCollectionScope`

enum lists the possible scopes: context or device. A parameter,`metricCollectionScope`

, is added to`CUpti_Profiler_Host_GetMetricProperties_Params`

to return the collection scope for a metric.By default, the counter availability image stores only context-level metrics in the binary blob. A new parameter,

`bAllowDeviceLevelCounters`

, has been added to the counter availability API struct`CUpti_Profiler_GetCounterAvailability_Params`

to include device-level metrics in the image.Added a new parameter

`sku`

in`CUpti_Profiler_DeviceSupported_Params`

for checking profiling support for a GPU SKU.Added a new parameter

`priority`

in the kernel record to provide the launch priority of the kernel. The`CUpti_ActivityKernel10`

activity record is deprecated and replaced by the new`CUpti_ActivityKernel11`

activity record.

**Resolved Issues**

Fixed an issue that could cause invalid (zero) kernel timestamps when using the function

`cuptiActivityRegisterTimestampCallback`

to register a timestamp callback. This issue was introduced in the CUDA 12.6 Update 2 release.

### 1.1.9. Updates in CUDA 13.0 Update 1[#](https://docs.nvidia.com#updates-in-cuda-13-0-update-1)

**New Features**

Extended Hardware Event System (HES) support for Linux aarch64 SBSA desktop platforms.


**Resolved Issues**

Fixed the issue where synchronization records were not generated for the CUDA APIs

`cudaDeviceSynchronize()`

and`cuCtxSynchronize_v2()`

.Fixed a potential deadlock that could occur while disabling the activity kind

`CUPTI_ACTIVITY_KIND_CONCURRENT_KERNEL`

using the API`cuptiActivityDisable`

.Fixed a potential crash in the API

`cuptiActivityFlushAll`

.Discarded Unified Memory counter records that could not be completed before disabling Unified Memory profiling.

Fixed the crash when NVTX API is called before the CUPTI API. This issue was introduced in the CUDA 13.0 GA release.

Fixed a segmentation fault issue while initializing the device buffer for storing profiling data. This segmentation fault occurs for long running applications using CUDA graphs when the attribute

`CUPTI_ACTIVITY_ATTR_MEM_ALLOCATION_TYPE_HOST_PINNED`

is set to 0.

### 1.1.10. Updates in CUDA 13.0[#](https://docs.nvidia.com#updates-in-cuda-13-0)

**New Features**

Added support for NVLOG, a configurable logging and error-reporting library, enabling detailed logging with various severity levels (Info, Warning, Error, Fatal) and output options including files and stdout. For more details, refer to the section

[Logging Using NVLOG](https://docs.nvidia.com/main/main.html#cupti-logging-using-nvlog).Introduced a new subscriber API,

`cuptiSubscribe_v2`

, which includes additional parameters for the current and previous subscriber’s names (if applicable). This enhancement allows for easier identification of the previous subscriber in cases where the current subscription fails.Added new callbacks

`CUPTI_CBID_RESOURCE_GRAPH_NODE_UPDATED`

for updates to CUDA Graph node and`CUPTI_CBID_RESOURCE_GRAPH_NODE_SET_PARAMS`

for when Graph parameters are set via the`cuGraphExecNodeSetParams()`

API.A new field

`isDeviceLaunched`

is added in the activity records for kernel, memcpy and memset operations to indicate whether operation is a part of the device launched graph. To accommodate this change, activity record`CUpti_ActivityKernel9`

is deprecated and replaced by a new activity record`CUpti_ActivityKernel10`

. With this change, collection of records for device launched graph is enabled by default if HES trace is enabled.A new field,

`isManagedPool`

, has been added to the memory pool record to indicate whether the pool uses managed memory or pinned memory allocation. The`CUpti_ActivityMemoryPool2`

activity record is deprecated and replaced by the new`CUpti_ActivityMemoryPool3`

activity record.Initial support for parsing and decoding NVTX extended payloads via activity records. This enables tools to extract extended payload information from NVTX activity records. Libraries such as NCCL, which emit NVTX annotations using extended payloads, are now decodable via CUPTI. For more information, refer to the section

[NVIDIA Tools Extension (NVTX) Support](https://docs.nvidia.com/main/main.html#nvtx-cupti-support).Added an API

`cuptiActivityEnableCudaEventDeviceTimestamps`

to control collection of device timestamp for the`CUPTI_ACTIVITY_KIND_CUDA_EVENT`

record. By default, the collection of CUDA event device timestamps is disabled.Starting with CUDA Toolkit 13.0, CUPTI API versions follow the format xxyyzz, where:

xx : Major CUDA Toolkit version

yy : Minor CUDA Toolkit version

zz : CUPTI-specific patch or update version (Note: This does not necessarily align with CUDA Toolkit update versions)



For example, version 130000 indicates CUDA Toolkit 13.0.

Ported the following samples from Profiling APIs to the new Range Profiler APIs: cupti_metric_properties, profiling_injection, callback_profiling and concurrent_profiling.

Added a new error code

`CUPTI_ERROR_INVALID_CHIP_NAME`

for invalid chip name passed in the Profiler Host APIs.

**Deprecated and dropped features**

The

[CUPTI Profiling API](https://docs.nvidia.com/main/main.html#cupti-profiling-api)from the header`cupti_profiler_target.h`

and the[Perfworks Metric API](https://docs.nvidia.com/main/main.html#perfworks-metric-api)from the header`nvperf_host.h`

are deprecated in the CUDA 13.0 release and will be removed in a future CUDA release. It is recommended to use the[CUPTI Range Profiling API](https://docs.nvidia.com/main/main.html#range-profiling-api)as an alternative. For more information, refer to the section[Evolution of the profiling APIs](https://docs.nvidia.com/main/main.html#evolution-of-the-profiling-apis). Note that not all APIs from the header`cupti_profiler_target.h`

are deprecated; a few supported APIs are used by other profiling features like Range Profiling and PM Sampling.The CUPTI Event API from the header

`cupti_events.h`

and the CUPTI Metric API from the header`cupti_metrics.h`

are dropped. Calling any Event or Metric API will return the error code`CUPTI_ERROR_LEGACY_PROFILER_NOT_SUPPORTED`

. It is recommended to use the[CUPTI Range Profiling API](https://docs.nvidia.com/main/main.html#range-profiling-api)as an alternative.The PC Sampling Activity API from the header

`cupti_activity.h`

is dropped. It is recommended to move to the[PC Sampling API](https://docs.nvidia.com/main/main.html#cupti-pc-sampling-api)from the header`cupti_pcsampling.h`

.The source/SASS level metrics from the header

`cupti_activity.h`

are dropped. It is recommended to move to the[SASS Metric API](https://docs.nvidia.com/main/main.html#cupti-sass-metric-api)from the header`cupti_sass_metrics.h`

.Removed support for the PowerPC (ppc64le) architecture.

By default, CUPTI will request activity buffers separately for each thread that generates activity records. This will improve the runtime performance of the application as it avoids contention when multiple threads are generating activities concurrently.


**Resolved Issues**

Reduction in the tracing collection overhead for graph launches under HES trace.

Fixed the issue that kernel activity records were showing stale information after updating the params through

`cuGraphExecKernelNodeSetParams()`

.Fixed the hang which can occur when tracing cooperative kernels under MPS. This requires an NVIDIA display driver version of 580 or higher.

Fixed an issue where some public API symbols were set to hidden visibility in the static build of the CUPTI library.

On a WSL2 system, using CLOCK_MONOTONIC_RAW instead of CLOCK_REALTIME because the latter can cause backward jumps due to system time adjustments.


### 1.1.11. Updates in CUDA 12.9 Update 1[#](https://docs.nvidia.com#updates-in-cuda-12-9-update-1)

**Resolved Issues**

Report the green context ID in the graph-level trace when graphs are launched from the host under a green context, instead of reporting the primary context ID.

Update the CUPTI API version

`CUPTI_API_VERSION`

for CUDA Update releases.Include the required NVTX headers in the header file generated_nvtx_meta.h.


### 1.1.12. Updates in CUDA 12.9[#](https://docs.nvidia.com#updates-in-cuda-12-9)

**New Features**

In confidential computing, rotating a key is a high-impact operation that halts all traffic using that key. During the key rotation, channels sharing the key will be drained and will not accept new CUDA work until the rotation completes. However, this process is not directly visible to user applications. CUPTI offers additional feedback to tools, allowing users to account for their impact on application timelines. The struct

`CUpti_ActivityConfidentialComputeRotation`

provides timestamps for each stage of the encryption rotation, while the enum`CUpti_ConfidentialComputeRotationEventType`

lists the supported stages.For Orin+ mobile chips on the Linux aarch64 platform, added metrics (mcc__*) support for memory controller channel (MC Channel) unit which connects to the DRAM.

A new attribute

`CUPTI_ACTIVITY_ATTR_DEVICE_BUFFER_SIZE_DEVICE_GRAPHS`

is added in the activity attribute enum`CUpti_ActivityAttribute`

to set and get the size for the profiling buffer for device graph operations.

**Resolved Issues**

Decoupled activity kinds

`CUPTI_ACTIVITY_KIND_CUDA_EVENT`

and`CUPTI_ACTIVITY_KIND_SYNCHRONIZATION`

. Previously, enabling one of these activities would automatically enable the capturing of records for the other.Fixed a crash when the client fails to provide a buffer in response to the activity buffer request callback issued by CUPTI. This condition is notified to the client using the

`CUPTI_CB_DOMAIN_STATE`

callback.The callback

`CUPTI_CBID_RESOURCE_MODULE_PROFILED`

is issued regardless of whether kernel tracing is enabled.

### 1.1.13. Updates in CUDA 12.8 Update 1[#](https://docs.nvidia.com#updates-in-cuda-12-8-update-1)

**Resolved Issues**

For graph level tracing, fixed the timestamp issue when memcpy node is the first node in the graph.

The PC Sampling API and concurrent kernel tracing have been made compatible, allowing them to be collected in the same pass.

Resolved bloat in the size of the BSS section in the static CUPTI library.


### 1.1.14. Updates in CUDA 12.8[#](https://docs.nvidia.com#updates-in-cuda-12-8)

**New Features**

Added support for the Blackwell architecture.

Blackwell architecture introduces a new hardware method called as Hardware Event System (HES) for collecting CUDA kernel timestamps. This method provides more accurate timestamps compared to the traditional SW instrumentation and semaphore based approach, and it is expected to add minimal overhead to the application. The new API

`cuptiActivityEnableHWTrace`

enables the collection of kernel timestamps through HW events. In CUDA 12.8, this feature is experimental and subject to certain limitations:It is not supported on MPS, WSL, MCDM, MIG, vGPU, or confidential compute setups.

It is supported on Linux x86_64 and Windows x86_64 platforms only.

On Windows, only a single context can be profiled at a time, while Linux allows tracing multiple contexts simultaneously.

Late attach functionality is not supported.


These limitations are expected to be addressed and removed in future releases.

Added support to provide GPU timestamps for the CUDA event record completion. The activity record

`CUpti_ActivityCudaEvent`

is deprecated and has been replaced by the new activity record`CUpti_ActivityCudaEvent2`

. The new field`deviceTimestamp`

provides the device-side timestamp and the field`cudaEventSyncId`

provides a unique ID to associate event synchronization records with the latest CUDA Event record.The activity kind

`CUPTI_ACTIVITY_KIND_SYNCHRONIZATION`

doesn’t provide records for CUDA synchronization operations which return non-zero CUDA status. The API`cuptiActivityEnableAllSyncRecords`

can be used to enable/disable collection of all CUDA synchronization operations which return non-zero CUDA status.Profiling of NVLINK (

`nvl*`

), C2C and PCIe metrics are now supported using[Profiler Host API](https://docs.nvidia.com/main/main.html#profiler-host-api)and[Range Profiler APIs](https://docs.nvidia.com/main/main.html#range-profiling-api). These metrics are collected at the device-level. These can’t be collected with the metrics which are collected at the context-level.Added a new field

`copyCount`

in the memcpy activity record to provide the number of copies performed by the batched memcpy operation. The activity record`CUpti_ActivityMemcpy5`

is replaced by a new activity record`CUpti_ActivityMemcpy6`

.For PM Sampling, users can configure the buffer append mode to either retain the latest or the oldest records in the event of a buffer overflow. Refer to the

`CUpti_PmSampling_HardwareBuffer_AppendMode`

enum for additional details.For unified memory profiling, the bitmask of devices involved in the operation is provided using the field

`processors`

. The activity record`CUpti_ActivityUnifiedMemoryCounter2`

is deprecated and has been replaced by the new activity record`CUpti_ActivityUnifiedMemoryCounter3`

.To provide additional information for graph level trace for device launched graphs, a new activity record

`CUpti_ActivityDeviceGraphTrace`

and activity kind`CUPTI_ACTIVITY_KIND_DEVICE_GRAPH_TRACE`

are introduced. The activity kind`CUPTI_ACTIVITY_KIND_DEVICE_GRAPH_TRACE`

can not be directly enabled or disabled. It is enabled when activity kind`CUPTI_ACTIVITY_KIND_GRAPH_TRACE`

is enabled and device graph trace is enabled through the API`cuptiActivityEnableDeviceGraph()`

.Added a new overhead kind

`CUPTI_ACTIVITY_OVERHEAD_UVM_ACTIVITY_INIT`

to report the overhead incurred while initializing the Unified Memory profiling.Enum

`CUpti_PcieGen`

is extended to include PCIe Gen 6.

**Deprecated and dropped features**

The CUPTI Event API from the header

`cupti_events.h`

and the CUPTI Metric API from the header`cupti_metrics.h`

are deprecated in the CUDA 12.8 release and will be removed in a future CUDA release. It is recommended to use the[CUPTI Range Profiling API](https://docs.nvidia.com/main/main.html#range-profiling-api)as an alternative. For more information, refer to the section[Evolution of the profiling APIs](https://docs.nvidia.com/main/main.html#evolution-of-the-profiling-apis).The PC Sampling Activity API and the source/SASS level metrics from the header

`cupti_activity.h`

will not be supported on Blackwell and future GPU architectures. These features were deprecated in earlier releases.

**Resolved Issues**

Resolved an issue where PM Sampling data was being collected on a different GPU than the intended one in multi-GPU systems.

Fixed the issue that activity records for conditional nodes in the graph were not generated for Ampere and later architectures.

If the device is in MIG mode, the

`uuid`

field in the device and NVLINK records returns the MIG UUID which uniquely identifies the subscribed MIG compute instance. This needs a matching driver from the 12.8 toolkit.CUPTI generates external correlation records for CUDA APIs even when CUDA API tracing is disabled using the

`cuptiActivityEnableRuntimeApi`

or`cuptiActivityEnableDriverApi`

API. This issue is addressed in the CUDA 12.8 release.

### 1.1.15. Updates in CUDA 12.6 Update 2[#](https://docs.nvidia.com#updates-in-cuda-12-6-update-2)

**New Features**

In CUDA 12.6 GA release, CUPTI added a new set of API around Perfworks host API to simplify usage, shield users from low-level concepts, and ease adaptation to changes in Perfworks APIs. The

*host*API was provided in the header`cupti_profiler_host.h`

. Complementing these, a new set of*target*API is added in CUDA 12.6 Update 2 to simplify profiling for new users and align the call structure with other profiling APIs for faster learning and better adaptability. The target API is provided in the header`cupti_range_profiler.h`

, and will be referred to as[Range Profiling API](https://docs.nvidia.com/main/main.html#range-profiling-api). For range profiling, it is strongly recommended that users, especially those new to the field, utilize the new host and target APIs introduced in CUDA 12.6. The[range_profiling](https://docs.nvidia.com/main/main.html#sample-range-profiling)sample shows how to use the host and target range profiling APIs.

Warning

It is important to note that existing [Profiling API](https://docs.nvidia.com/main/main.html#cupti-profiling-api) will be deprecated and
removed in future releases, so transitioning to new [Profiler Host API](https://docs.nvidia.com/main/main.html#profiler-host-api) and
[Range Profiler APIs](https://docs.nvidia.com/main/main.html#range-profiling-api) will ensure continued support and compatibility.

Added support for tracing and profiling on Microsoft Compute Driver Model (MCDM). This requires an NVIDIA display driver version of 565 or higher.


**Resolved Issues**

Improved the conversion accuracy of timestamps which are captured on the GPU and converted to CPU timestamps.

Timestamps reported in the activity records were not always correct for Windows Subsystem for Linux (WSL) systems. This issue has been fixed.

Fixed an issue that resulted in failure to capture the tracing information for kernels inside the body of the conditional node of CUDA Graph. This requires an NVIDIA display driver version of 565 or higher.

PM Sampling trigger mode

`CUPTI_PM_SAMPLING_TRIGGER_MODE_GPU_TIME_INTERVAL`

is supported for all GA10x (GA102+) chips.Fixed issues with Enhanced compatibility (aka minor version compatibility) of a few CUPTI activities with the driver versions shipped with the CUDA 12.2 or prior releases.

Made flushing of activity buffers thread-safe for per-thread activity buffer feature.


### 1.1.16. Updates in CUDA 12.6 Update 1[#](https://docs.nvidia.com#updates-in-cuda-12-6-update-1)

**Resolved Issues**

Disabling all callbacks in a domain using the

`cuptiEnableDomain`

API could unintentionally disable other activities and callbacks. This issue has been addressed and resolved.Fixed issues with Enhanced compatibility (aka minor version compatibility) of a few CUPTI activities with the driver versions shipped with the CUDA 12.2 or prior releases.


### 1.1.17. Updates in CUDA 12.6[#](https://docs.nvidia.com#updates-in-cuda-12-6)

**New Features**

CUPTI introduces PM Sampling APIs for collecting many hardware metrics by sampling the GPU’s performance monitors (PM) periodically at fixed intervals for a CUDA workload. These APIs are provided in the header file

`cupti_pmsampling.h`

. These are supported on Turing and later GPU architectures, i.e. devices with compute capability 7.5 and higher. Refer to the section[PM Sampling API](https://docs.nvidia.com/main/main.html#pm-sampling-api)for more details.The Profiling is split into four main phases - Enumeration, Configuration, Collection and Evaluation. APIs for three phases enumeration, configuration and evaluation are provided directly by the low level Perfworks APIs. CUPTI is adding a new set of APIs around these Perfworks host APIs to simplify usage, shield users from low-level concepts, and ease adaptation to changes in Perfworks APIs. These APIs promote consistency, reduce confusion, and enhance integration with CUPTI APIs. New host APIs are provided in the header

`cupti_profiler_host.h`

. Additionally, new target APIs will be introduced in a future release to simplify profiling for new users and align the call structure with other profiling APIs for faster learning and better adaptability.Added support for identifying the source of the memory allocation. This is useful when memory allocation request is made from a library or shared object which is called from the application. A new field

`source`

is added in the memory activity record. The activity record`CUpti_ActivityMemory3`

is deprecated and it is replaced by a new activity record`CUpti_ActivityMemory4`

. Refer to the section[Device Memory Allocation Source Tracking](https://docs.nvidia.com/main/main.html#activity-allocation-source-tracking)for more details.Added a new overhead kind

`CUPTI_ACTIVITY_OVERHEAD_ACTIVITY_BUFFER_REQUEST`

to report the overhead incurred while requesting activity buffers from the CUPTI client.Added static library

`libcupti_static.a`

for ARM Server (arm64 SBSA).

**Deprecated and dropped features**

Source/SASS level metrics from the header

`cupti_activity.h`

are deprecated on Volta and later GPU architectures and these will be removed in a future release. It includes metrics`CUPTI_ACTIVITY_KIND_GLOBAL_ACCESS`

,`CUPTI_ACTIVITY_KIND_SHARED_ACCESS`

,`CUPTI_ACTIVITY_KIND_BRANCH`

and`CUPTI_ACTIVITY_KIND_INSTRUCTION_EXECUTION`

and related correlation kinds`CUPTI_ACTIVITY_KIND_SOURCE_LOCATOR`

and`CUPTI_ACTIVITY_KIND_INSTRUCTION_CORRELATION`

. It is recommended to move to the[SASS Metric API](https://docs.nvidia.com/main/main.html#cupti-sass-metric-api)from the header`cupti_sass_metrics.h`

which is supported on Volta and later GPU architectures.

**Resolved Issues**

Exported the profiling API

`cuptiProfilerIsPassCollected`

.Reduced the collection overhead for memcpy tracing.

For some activities, duration for the activity buffer request was getting included in the activity duration. This issue is resolved.


### 1.1.18. Updates in CUDA 12.5 Update 1[#](https://docs.nvidia.com#updates-in-cuda-12-5-update-1)

**Resolved Issues**

Fixed a crash for the graph level tracing for CUDA graphs.

Fixed an issue due to which resource callback

`CUPTI_CBID_RESOURCE_MODULE_PROFILED`

might not be issued when no other activity is enabled. This issue was introduced in the CUDA 12.4 Update 1 release.

### 1.1.19. Updates in CUDA 12.5[#](https://docs.nvidia.com#updates-in-cuda-12-5)

**New Features**

Added APIs

`cuptiActivityEnableDriverApi`

and`cuptiActivityEnableRuntimeApi`

to limit the tracing of CUDA APIs that are of interest. This can help in reducing the CUDA API tracing overhead.Added new field

`cigMode`

to communicate the CUDA in Graphics (CIG) mode associated with the CUDA context. The activity record CUpti_ActivityContext2 is deprecated and it is replaced by a new activity record CUpti_ActivityContext3. Enum`CUpti_ContextCigMode`

describes the supported CIG modes.Added new field

`numMultiprocessors`

in the context activity record to communicate the number of multiprocessors assigned to the green context.Tracing is supported for MPS (Multi-Process Service) on Tegra platforms.

Obfuscated symbols are provided for Linux x86_64 platform, it helps us in speeding up the debug process for issues like crash, hang etc. See

[https://developer.nvidia.com/blog/cuda-toolkit-symbol-server/](https://developer.nvidia.com/blog/cuda-toolkit-symbol-server/)for information on how to use obfuscated symbols. Symbol server address is:[https://cudatoolkit-symbols.nvidia.com/](https://cudatoolkit-symbols.nvidia.com/).

**Deprecated and dropped features**

PC Sampling Activity API from the header

`cupti_activity.h`

is deprecated for Volta and later GPU architectures and this will be removed in a future release. It is recommended to move to the[PC Sampling API](https://docs.nvidia.com/main/main.html#cupti-pc-sampling-api)from the header`cupti_pcsampling.h`

which is supported on Volta and later GPU architectures.Removed support for the PowerPC (ppc64le) architecture.


**Resolved Issues**

Fixed Unified memory profiling on Heterogeneous Memory Management (HMM) and Address Translation Service (ATS) systems.


### 1.1.20. Updates in CUDA 12.4 Update 1[#](https://docs.nvidia.com#updates-in-cuda-12-4-update-1)

**Resolved Issues**

Fixed a crash when API

`cuptiFinalize`

is used for applications using CUDA Graph.Fixed a crash which can occur while tracing memcpy and memset nodes in a graph when using graph level tracing.

Skip delivering worker thread buffers on internal flush if the worker thread buffer is not full.


### 1.1.21. Updates in CUDA 12.4[#](https://docs.nvidia.com#updates-in-cuda-12-4)

**New Features**

Added tracing support for applications using Green contexts. Added two new fields

`isGreenContext`

and`parentContextId`

in the context activity record. The activity record`CUpti_ActivityContext`

is deprecated and it is replaced by a new activity record`CUpti_ActivityContext2`

.CUDA API calls are completed asynchronously from the perspective of the host CPU. This is accomplished by queuing the work slated for the GPU into a structure known as a command buffer. If there is insufficient space available in the command buffer when attempting to call a CUDA API, the host call will block until space becomes available. The user should be able to identify when this situation occurs. This is indicated using the new attribute

`CUPTI_ACTIVITY_OVERHEAD_COMMAND_BUFFER_FULL`

added in the activity overhead enum`CUpti_ActivityOverheadKind`

. To provide additional details about the overhead, a new field`overheadData`

is added in the overhead activity record. Activity record`CUpti_ActivityOverhead2`

is deprecated and it is replaced by the new activity record`CUpti_ActivityOverhead3`

.Added process ID and thread ID in the JIT activity record. To accommodate this change, activity record

`CUpti_ActivityJit`

is deprecated and it is replaced by a new activity record`CUpti_ActivityJit2`

.To correlate the sampling data for a kernel with the launch API in the serial mode of the PC Sampling APIs, a new field

`correlationId`

is added in the struct`CUpti_PCSamplingPCData`

.For PC Sampling APIs, total (smsp__pcsamp_sample_count) and dropped (smsp__pcsamp_samples_data_dropped) sample counts are collected by default.


**Resolved Issues**

Fixed the issue for overhead records showing the default thread ID than the one requested using the API

`cuptiSetThreadIdType()`

.Fixed instruction level SASS metrics profiling for CUDA Graph applications.

When a device graph is first launched from the device and it is not launched from the host earlier, end timestamp could be 0 for graph-level tracing on Ampere and later GPU architectures. This issue is fixed.


### 1.1.22. Updates in CUDA 12.3 Update 1[#](https://docs.nvidia.com#updates-in-cuda-12-3-update-1)

**Resolved Issues**

To provide normalized timestamps for all activities, CUPTI uses linear interpolation for conversion from GPU timestamps to CPU timestamps. This was broken with CUDA 12.3 causing spurious gaps or overlap on Tegra platforms. Fixed the issue.


### 1.1.23. Updates in CUDA 12.3[#](https://docs.nvidia.com#updates-in-cuda-12-3)

**New Features**

New attributes

`CUPTI_ACTIVITY_OVERHEAD_RUNTIME_TRIGGERED_MODULE_LOADING`

and`CUPTI_ACTIVITY_OVERHEAD_LAZY_FUNCTION_LOADING`

are added in the activity overhead enum`CUpti_ActivityOverheadKind`

to provide the overhead information for CUDA runtime triggered module loading and lazy function loading respectively.New API

`cuptiGetGraphExecId`

provides the unique ID of the executable graph.Added support for collecting graph level trace for device launched graphs. A new API

`cuptiActivityEnableDeviceGraph`

is added to enable the collection of records for device launched graphs.CUDA Graphs can be executed on multiple devices i.e. the root node could be launched on one device and the leaf node could be launched on the another device. New fields

`endDeviceId`

and`endContextId`

are added to identify the ids of device and context respectively which are used to execute the last node of the graph. To accommodate this change, activity record`CUpti_ActivityGraphTrace`

is deprecated and it is replaced by a new activity record`CUpti_ActivityGraphTrace2`

.Added WSL profiling support on Windows 10 WSL with OS build version 19044 and greater. WSL profiling is not supported on Windows 10 WSL for systems that exceed 1 TB of system memory.

Several performance improvements are done in the tracing path. One of the key improvements is to allow clients to request CUPTI to maintain the activity buffers at the thread level instead of global buffers. This can be achieved by setting the option

`CUPTI_ACTIVITY_ATTR_PER_THREAD_ACTIVITY_BUFFER`

of the enum`CUpti_ActivityAttribute`

. This can help in reducing the collection overhead for applications which launch CUDA activities from multiple host threads.Frame pointers are enabled for Linux x86_64 libraries.

The deprecated Activity APIs and structures have been moved to a new header cupti_activity_deprecated.h, which is included in the header cupti_activity.h. Header cupti_activity.h contains only the latest version of APIs and structures.

CUPTI no longer uses profiling semaphore pool to store the profiling data. Corresponding attributes

`CUPTI_ACTIVITY_ATTR_PROFILING_SEMAPHORE_POOL_SIZE`

,`CUPTI_ACTIVITY_ATTR_PROFILING_SEMAPHORE_POOL_LIMIT`

and`CUPTI_ACTIVITY_ATTR_PROFILING_SEMAPHORE_PRE_ALLOCATE_VALUE`

have been deprecated.

**Resolved Issues**

Fixed SASS metric profiling for cuda graph.

Fixed race condition in the API

`cuptiSetThreadIdType`

for late subscription.

### 1.1.24. Updates in CUDA 12.2 Update 2[#](https://docs.nvidia.com#updates-in-cuda-12-2-update-2)

**New Features**

SASS Metric APIs introduced in the CUDA 12.2 GA release are transitioning from the beta to the production release.

Added support for collecting SASS metrics for CUDA Graphs which are launched from host.

Added a new field

`numOfDroppedRecords`

in the struct`CUpti_SassMetricsDisable_Params`

to indicate the number of dropped records when SASS data is flushed prior to calling the disable API.

Added a new field

`api`

in the struct`CUpti_Profiler_DeviceSupported_Params`

which can be used to check the configuration support level for profiler APIs like Profiling, PC Sampling and SASS Metric APIs.

**Resolved Issues**

Fixed the tracing and profiling support for the GA103 GPU.

Fixed a hang which can occur when activity buffer gets full while collecting the sampling data using the PC Sampling Activity API.

Fixed the issue of incorrect timestamps for graph level trace when a graph node is disabled using the APIs

`cuGraphNodeSetEnabled`

or`cudaGraphNodeSetEnabled`

.

### 1.1.25. Updates in CUDA 12.2 Update 1[#](https://docs.nvidia.com#updates-in-cuda-12-2-update-1)

**Support for Confidential Computing**

CUPTI supports some APIs while running in CC-devtools mode:

Callback API

Activity API


The profiling APIs are not supported in CC-devtools mode with this release. Using these APIs should return an error indicating the configuration is not supported:

Profiling API

PC Sampling API

Checkpoint API

SASS Metrics API


Additionally, CUPTI is not supported at all in full CC mode. CC-devtools mode must be used for tools support.
Some CUDA APIs are not supported or behave differently when running in CC or CC-devtools mode; notably, host pinned memory requests will be traced as managed memory requests, and any CUDA memcopies on these converted pointers are traced as Device to Device copies irrespective of the locality of the source or destination pointers.
For details on how to configure CC or CC-devtools mode, system and software requirements, as well as documentation on CUDA API changes, please see the confidential compute release documentation at [https://docs.nvidia.com/confidential-computing/](https://docs.nvidia.com/confidential-computing/).

**Resolved Issues**

Fixed timestamps for graph-level tracing for CUDA graphs running across multiple GPUs.

Fixed a potential hang when CUPTI is unable to fetch attributes for an activity.


### 1.1.26. Updates in CUDA 12.2[#](https://docs.nvidia.com#updates-in-cuda-12-2)

**New Features**

A new set of CUPTI APIs for collection of SASS metric data at the source level are provided in the header file

`cupti_sass_metrics.h`

. These support a larger set of metrics compared to the CUPTI Activity APIs for source-level analysis. SASS to source correlation can be done in the offline mode, similar to the PC sampling APIs. Hence the runtime overhead during data collection is lower. Refer to the section[CUPTI SASS Metrics API](https://docs.nvidia.com/main/main.html#cupti-sass-metric-api)for more details. Please note that this is a Beta feature, interface and functionality are subject to change in a future release.CUPTI now reports fatal errors, non-fatal errors and warnings instantaneously through callbacks. A new callback domain

`CUPTI_CB_DOMAIN_STATE`

is added for subscribing to the instantaneous error reporting. Corresponding callback ids are provided in the struct`CUpti_CallbackIdState`

.Added support for profiling of device graphs and host graphs that launch device graphs. There are some known limitations, please refer to the Known Issues section for details.

Change in the stream attribute value is communicated by issuing the resource callback. Refer to the struct

`CUpti_StreamAttrData`

and callback id`CUPTI_CBID_RESOURCE_STREAM_ATTRIBUTE_CHANGED`

added in the enum`CUpti_CallbackIdResource`

.New API

`cuptiGetErrorMessage`

provides descriptive message for CUPTI error codes.Removed the deprecated API

`cuptiDeviceGetTimestamp`

from the header`cupti_events.h`

.Added metrics for Tensor core operations to count different types of tensor instructions. These metrics are named as

`sm[sp]__ops_path_tensor_src_{src}[_dst_{dst}[_sparsity_{on,off}]].`

These are available for devices with compute capability 7.0 and higher, except for Turing TU11x GPUs.

**Resolved Issues**

Fixed crash for the graph-level trace for device graphs which are launched from the host.


### 1.1.27. Updates in CUDA 12.1 Update 1[#](https://docs.nvidia.com#updates-in-cuda-12-1-update-1)

**Resolved Issues**

Fixed CUPTI tracing failure when just-in-time compilation of embedded PTX code is disabled using the environment variable

`CUDA_DISABLE_PTX_JIT`

.Fixed a crash in the API

`cuptiFinalize`

.

### 1.1.28. Updates in CUDA 12.1[#](https://docs.nvidia.com#updates-in-cuda-12-1)

**New Features**

Field

`wsl`

is added in the struct`CUpti_Profiler_DeviceSupported_Params`

to indicate whether Profiling API is supported on Windows Subsystem for Linux (WSL) system or not.

### 1.1.29. Updates in CUDA 12.0 Update 1[#](https://docs.nvidia.com#updates-in-cuda-12-0-update-1)

**Resolved Issues**

Reduced the host memory overhead by avoiding caching copies of cubin images at the time of loading CUDA modules. Copies of cubin images are now created only when profiling features that need it are enabled.

By default CUPTI switches back to the device memory, instead of the pinned host memory, for allocation of the profiling buffer for concurrent kernel tracing. This might help in improving the performance of the tracing run. Memory location can be controlled using the attribute

`CUPTI_ACTIVITY_ATTR_MEM_ALLOCATION_TYPE_HOST_PINNED`

of the activity attribute enum`CUpti_ActivityAttribute`

.CUPTI now captures the

`cudaGraphLaunch`

API and its kernels when CUPTI is attached after the graph is instantiated using the API`cudaGraphInstantiate`

but it is attached before the graph is launched using the API`cudaGraphLaunch`

. Some data in the kernel record would be missing i.e.`cacheConfig`

,`sharedMemoryExecuted`

,`partitionedGlobalCacheRequested`

,`partitionedGlobalCacheExecuted`

,`sharedMemoryCarveoutRequested`

etc. This fix requires the matching CUDA driver which ships with the CUDA 12.0 Update 1 release.

### 1.1.30. Updates in CUDA 12.0[#](https://docs.nvidia.com#updates-in-cuda-12-0)

**New Features**

Added new fields

`maxPotentialClusterSize`

and`maxActiveClusters`

to help in calculating the cluster occupancy correctly. These fields are valid for devices with compute capability 9.0 and higher. To accommodate this change, activity record`CUpti_ActivityKernel8`

is deprecated and replaced by a new activity record`CUpti_ActivityKernel9`

.Enhancements for PC Sampling APIs:

CUPTI creates few worker threads to offload certain operations like decoding of the hardware data to the CUPTI PC sampling data and correlation of the PC data to the SASS instructions. CUPTI wakes up these threads periodically. To control the sleep time of the worker threads, a new attribute

`CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_WORKER_THREAD_PERIODIC_SLEEP_SPAN`

is added in the enum`CUpti_PCSamplingConfigurationAttributeType`

.Improved error reporting for hardware buffer overflow. When hardware buffer overflows, CUPTI returns the out of memory error code. And a new field

`hardwareBufferFull`

added in the struct`CUpti_PCSamplingData`

is set to differentiate it from other out of memory cases. User can either increase the hardware buffer size or flush the hardware buffer at a higher frequency to avoid overflow.

Profiling APIs are supported on Windows Subsystem for Linux (WSL) with WSL version 2, NVIDIA display driver version 525 or higher and Windows 11.

CUPTI support for Kepler GPUs is dropped in CUDA Toolkit 12.0.


**Resolved Issues**

Removed minor CUDA version from the SONAME of the CUPTI shared library for compatibility reasons. For example, SONAME of CUPTI library is libcupti.so.12 instead of libcupti.so.12.0 in CUDA 12.0 release.

Activity kinds

`CUPTI_ACTIVITY_KIND_MARKER`

and`CUPTI_ACTIVITY_KIND_MARKER_DATA`

can be enabled together.

### 1.1.31. Older Versions[#](https://docs.nvidia.com#older-versions)

#### 1.1.31.1. Updates in CUDA 11.8[#](https://docs.nvidia.com#updates-in-cuda-11-8)

**New Features**

CUPTI adds tracing and profiling support for Hopper and Ada Lovelace GPU families.

Added new fields

`clusterX`

,`clusterY`

,`clusterZ`

and`clusterSchedulingPolicy`

to output the Thread Block Cluster dimensions and scheduling policy. These fields are valid for devices with compute capability 9.0 and higher. To accommodate this change, activity record`CUpti_ActivityKernel7`

is deprecated and replaced by a new activity record`CUpti_ActivityKernel8`

.A new activity kind

`CUPTI_ACTIVITY_KIND_JIT`

and corresponding activity record`CUpti_ActivityJit`

are introduced to capture the overhead involved in the JIT (just-in-time) compilation and caching of the PTX or NVVM IR code to the binary code. New record also provides the information about the size and path of the compute cache where the binary code is stored.PC Sampling API is supported on Tegra platforms - QNX, Linux (aarch64) and Linux (x86_64) (Drive SDK).


**Resolved Issues**

Resolved an issue that might cause crash when the size of the device buffer is changed, using the attribute

`CUPTI_ACTIVITY_ATTR_DEVICE_BUFFER_SIZE`

, after creation of the CUDA context.

#### 1.1.31.2. Updates in CUDA 11.7 Update 1[#](https://docs.nvidia.com#updates-in-cuda-11-7-update-1)

**Resolved Issues**

Resolved an issue for PC Sampling API

`cuptiPCSamplingGetData`

which might not always return all the samples when called after the PC sampling range defined by using the APIs`cuptiPCSamplingStart`

and`cuptiPCSamplingStop`

. Remaining samples were delivered in the successive call of the API`cuptiPCSamplingGetData`

after the next range.Disabled tracing of nodes in the CUDA Graph when user enables tracing at the Graph level using the activity kind

`CUPTI_ACTIVITY_KIND_GRAPH_TRACE`

.Fixed missing

`channelID`

and`channelType`

information for kernel records. Earlier these fields were populated for CUDA Graph launches only.

#### 1.1.31.3. Updates in CUDA 11.7[#](https://docs.nvidia.com#updates-in-cuda-11-7)

**New Features**

A new activity kind

`CUPTI_ACTIVITY_KIND_GRAPH_TRACE`

and activity record`CUpti_ActivityGraphTrace`

are introduced to represent the execution for a graph without giving visibility about the execution of its nodes. This is intended to reduce overheads involved in tracing each node separately. This activity can only be enabled for drivers of version 515 and above.A new API

`cuptiActivityEnableAndDump`

is added to provide snapshot of certain activities like device, context, stream, NVLink and PCIe at any point during the profiling session.Added sample

[cupti_correlation](https://docs.nvidia.com/main/main.html#sample-cupti-correlation)to show correlation between CUDA APIs and corresponding GPU activities.Added sample

[cupti_trace_injection](https://docs.nvidia.com/main/main.html#sample-cupti-trace-injection)to show how to build an injection library using the activity and callback APIs which can be used to trace any CUDA application.

**Resolved Issues**

Fixed corruption in the function name for PC Sampling API records.

Fixed incorrect timestamps for GPU activities when user calls the API

`cuptiActivityRegisterTimestampCallback`

in the late CUPTI attach scenario.Fixed incomplete records for device to device memcopies in the late CUPTI attach scenario. This issue manifests mainly when application has a mix of CUDA graph and normal kernel launches.


#### 1.1.31.4. Updates in CUDA 11.6 Update 1[#](https://docs.nvidia.com#updates-in-cuda-11-6-update-1)

**Resolved Issues**

Fixed hang for the PC Sampling API

`cuptiPCSamplingStop`

. This issue is seen for the PC sampling start and stop resulting in generation of large number of sampling records.Fixed timing issue for specific device to device memcpy operations.


#### 1.1.31.5. Updates in CUDA 11.6[#](https://docs.nvidia.com#updates-in-cuda-11-6)

**New Features**

Two new fields

`channelID`

and`channelType`

are added in the activity records for kernel, memcpy, peer-to-peer memcpy and memset to output the ID and type of the hardware channel on which these activities happen. Activity records`CUpti_ActivityKernel6`

,`CUpti_ActivityMemcpy4`

,`CUpti_ActivityMemcpyPtoP3`

and`CUpti_ActivityMemset3`

are deprecated and replaced by new activity records`CUpti_ActivityKernel7`

,`CUpti_ActivityMemcpy5`

,`CUpti_ActivityMemcpyPtoP4`

and`CUpti_ActivityMemset4`

.New fields

`isMigEnabled`

,`gpuInstanceId`

,`computeInstanceId`

and`migUuid`

are added in the device activity record to provide MIG information for the MIG enabled GPU. Activity record`CUpti_ActivityDevice3`

is deprecated and replaced by a new activity record`CUpti_ActivityDevice4`

.A new field

`utilizedSize`

is added in the memory pool and memory activity record to provide the utilized size of the memory pool. Activity record`CUpti_ActivityMemoryPool`

and`CUpti_ActivityMemory2`

are deprecated and replaced by a new activity record`CUpti_ActivityMemoryPool2`

and`CUpti_ActivityMemory3`

respectively.API

`cuptiActivityRegisterTimestampCallback`

and callback function`CUpti_TimestampCallbackFunc`

are added to register a callback function to obtain timestamp of user’s choice instead of using CUPTI provided timestamp in activity records.Profiling API supports profiling OptiX application.


**Resolved Issues**

Fixed multi-pass metric collection using the Profiling API in the auto range and kernel replay mode for Cuda Graph.

Fixed the performance issue for the PC sampling API

`cuptiPCSamplingStop`

.Fixed corruption in variable names for OpenACC activity records.

Fixed corruption in the fields of the struct

`memoryPoolConfig`

in the activity record`CUpti_ActivityMemory3`

.Filled the fields of the struct

`memoryPoolConfig`

in the activity record`CUpti_ActivityMemory3`

when a memory pointer allocated via memory pool is released using`cudaFree`

CUDA API.

#### 1.1.31.6. Updates in CUDA 11.5 Update 1[#](https://docs.nvidia.com#updates-in-cuda-11-5-update-1)

**Resolved Issues**

Resolved an issue that causes incorrect range name for NVTX event attributes. The issue was introduced in CUDA 11.4.

Made NVTX initialization APIs

`InitializeInjectionNvtx`

and`InitializeInjectionNvtx2`

thread-safe.

#### 1.1.31.7. Updates in CUDA 11.5[#](https://docs.nvidia.com#updates-in-cuda-11-5)

**New Features**

A new API

`cuptiProfilerDeviceSupported`

is introduced to expose overall Profiling API support and specific requirements for a given device. Profiling API must be initialized by calling`cuptiProfilerInitialize`

before testing device support.PC Sampling struct

`CUpti_PCSamplingData`

introduces a new field`nonUsrKernelsTotalSamples`

to provide information about the number of samples collected for all non-user kernels.Activity record

`CUpti_ActivityDevice2`

for device information has been deprecated and replaced by a new activity record`CUpti_ActivityDevice3`

. New record adds a flag`isCudaVisible`

to indicate whether device is visible to CUDA.Activity record

`CUpti_ActivityNvLink3`

for NVLink information has been deprecated and replaced by a new activity record`CUpti_ActivityNvLink4`

. New record can accommodate NVLink port information up to a maximum of 32 ports.A new

[CUPTI Checkpoint API](https://docs.nvidia.com/main/main.html#cupti-checkpoint-api)is introduced, enabling automatic saving and restoring of device state, and facilitating development of kernel replay tools. This is helpful for User Replay mode of the CUPTI Profiling API, but is not limited to use with CUPTI.Tracing is supported on the Windows Subsystem for Linux version 2 (WSL 2).

CUPTI is not supported on NVIDIA Crypto Mining Processors (CMP). A new error code

`CUPTI_ERROR_CMP_DEVICE_NOT_SUPPORTED`

is introduced to indicate it.

**Resolved Issues**

Resolved an issue that causes crash for tracing of device to device memcopy operations.

Resolved an issue that causes crash for OpenACC activity when it is enabled before other activities.


#### 1.1.31.8. Updates in CUDA 11.4 Update 1[#](https://docs.nvidia.com#updates-in-cuda-11-4-update-1)

**Resolved Issues**

Resolved serialization of CUDA Graph launches for applications which use multiple threads to launch work.

Previously, for applications that use CUDA Dynamic Parallelism (CDP), CUPTI detects the presence of the CDP kernels in the CUDA module. Even if CDP kernels are not called, it fails to trace the application. There is a change in the behavior, CUPTI now traces all the host launched kernels until it encounters a host launched kernel which launches child kernels. Subsequent kernels are not traced.


#### 1.1.31.9. Updates in CUDA 11.4[#](https://docs.nvidia.com#updates-in-cuda-11-4)

**New Features**

Profiling APIs support profiling of the CUDA kernel nodes launched by a CUDA Graph. Auto range profiling with kernel replay mode and user range profiling with user replay and application replay modes are supported. Other combinations of range profiling and replay modes are not supported.

Added support for tracing and profiling on

[NVIDIA virtual GPUs](https://www.nvidia.com/en-us/data-center/virtual-gpu-technology/)(vGPUs) on an upcoming GRID/vGPU release.Added sample

[profiling_injection](https://docs.nvidia.com/main/main.html#sample-profiling-injection)to show how to build injection library using the Profiling API.Added sample

[concurrent_profiling](https://docs.nvidia.com/main/main.html#sample-concurrent-profiling)to show how to retain the kernel concurrency across streams and devices using the Profiling API.

**Resolved Issues**

Resolved the issue of not tracing the device to device memcopy nodes in a CUDA Graph.

Fixed the issue of reporting zero size for local memory pool for mempool creation record.

Resolved the issue of non-collection of samples for the default CUDA context for PC Sampling API.

Enabled tracking of all domains and registered strings in NVTX irrespective of whether the NVTX activity kind or callbacks are enabled. This state tracking is needed for proper working of the tool which creates these NVTX objects before enabling the NVTX activity kind or callback.


#### 1.1.31.10. Updates in CUDA 11.3[#](https://docs.nvidia.com#updates-in-cuda-11-3)

**New Features**

A new set of CUPTI APIs for PC sampling data collection are provided in the header file

`cupti_pcsampling.h`

which support continuous mode data collection without serializing kernel execution and have a lower runtime overhead. Along with these a utility library is provided in the header file`cupti_pcsampling_util.h`

which has APIs for GPU assembly to CUDA-C source correlation and for reading and writing the PC sampling data from/to files. Refer to the section[CUPTI PC Sampling API](https://docs.nvidia.com/main/main.html#cupti-pc-sampling-api)for more details.Enum

`CUpti_PcieGen`

is extended to include PCIe Gen 5.The following functions are deprecated and will be removed in a future release:

Struct

`NVPA_MetricsContext`

and related APIs`NVPW_MetricsContext_*`

from the header`nvperf_host.h`

. It is recommended to use the struct`NVPW_MetricsEvaluator`

and related APIs`NVPW_MetricsEvaluator_*`

instead. Profiling API samples have been updated to show how to use these APIs.`cuptiDeviceGetTimestamp`

from the header`cupti_events.h`

.


**Resolved Issues**

Overhead reduction for tracing of CUDA memcopies.

To provide normalized timestamps for all activities, CUPTI uses linear interpolation for conversion from GPU timestamps to CPU timestamps. This method can cause spurious gaps or overlap on the timeline. CUPTI improves the conversion function to provide more precise timestamps.

Generate overhead activity record for semaphore pool allocation.


#### 1.1.31.11. Updates in CUDA 11.2[#](https://docs.nvidia.com#updates-in-cuda-11-2)

**New Features**

A new activity kind

`CUPTI_ACTIVITY_KIND_MEMORY_POOL`

and activity record`CUpti_ActivityMemoryPool`

are introduced to represent the creation, destruction and trimming of a memory pool. Enum`CUpti_ActivityMemoryPoolType`

lists types of memory pool.A new activity kind

`CUPTI_ACTIVITY_KIND_MEMORY2`

and activity record`CUpti_ActivityMemory2`

are introduced to provide separate records for memory allocation and release operations. This helps in correlation of records of these operations to the corresponding CUDA APIs, which otherwise is not possible using the existing activity record`CUpti_ActivityMemory`

which provides a single record for both the memory operations.Added a new pointer field of type

`CUaccessPolicyWindow`

in the kernel activity record to provide the access policy window which specifies a contiguous region of global memory and a persistence property in the L2 cache for accesses within that region. To accommodate this change, activity record`CUpti_ActivityKernel5`

is deprecated and replaced by a new activity record`CUpti_ActivityKernel6`

. This attribute is not collected by default. To control the collection of launch attributes, a new API`cuptiActivityEnableLaunchAttributes`

is introdcued.New attributes

`CUPTI_ACTIVITY_ATTR_DEVICE_BUFFER_PRE_ALLOCATE_VALUE`

and`CUPTI_ACTIVITY_ATTR_PROFILING_SEMAPHORE_PRE_ALLOCATE_VALUE`

are added in the activity attribute enum`CUpti_ActivityAttribute`

to set and get the number of device buffers and profiling semaphore pools which are preallocated for the context.CUPTI now allocates profiling buffer for concurrent kernel tracing in the pinned host memory in place of device memory. This might help in improving the performance of the tracing run. Memory location can be controlled using the attribute

`CUPTI_ACTIVITY_ATTR_MEM_ALLOCATION_TYPE_HOST_PINNED`

of the activity attribute enum`CUpti_ActivityAttribute`

.The compiler generated line information for inlined functions is improved due to which CUPTI can associate inlined functions with the line information of the function call site that has been inlined.

Removed support for NVLink performance metrics (

`nvlrx__*`

and`nvltx__*`

) from the Profiling API due to a potential application hang during data collection. The metrics will be added back in a future CUDA release.

**Resolved Issues**

Execution overheads introduced by CUPTI in the tracing path is reduced.

For the concurrent kernel activity kind

`CUPTI_ACTIVITY_KIND_CONCURRENT_KERNEL`

, CUPTI instruments the kernel code to collect the timing information. Previously, every kernel in the CUDA module was instrumented, thus the overhead is proportional to the number of different kernels in the module. This is a static overhead which happens at the time of loading the CUDA module. To reduce this overhead, kernels are not instrumented at the module load time, instead a single instrumentation code is generated at the time of loading the CUDA module and it is applied to each kernel during the kernel execution, thus avoiding most of the static overhead at the CUDA module load time.

#### 1.1.31.12. Updates in CUDA 11.1[#](https://docs.nvidia.com#updates-in-cuda-11-1)

**New Features**

CUPTI adds tracing and profiling support for the NVIDIA Ampere GPUs with compute capability 8.6.

Added a new field

`graphId`

in the activity records for kernel, memcpy, peer-to-peer memcpy and memset to output the unique ID of the CUDA graph that launches the activity through CUDA graph APIs. To accommodate this change, activity records`CUpti_ActivityMemcpy3`

,`CUpti_ActivityMemcpyPtoP2`

and`CUpti_ActivityMemset2`

are deprecated and replaced by new activity records`CUpti_ActivityMemcpy4`

,`CUpti_ActivityMemcpyPtoP3`

and`CUpti_ActivityMemset3`

. And kernel activity record`CUpti_ActivityKernel5`

replaces the padding field with`graphId`

. Added a new API`cuptiGetGraphId`

to query the unique ID of the CUDA graph.Added a new API

`cuptiActivityFlushPeriod`

to set the flush period for the worker thread.Added support for profiling cooperative kernels using Profiling APIs.

Added NVLink performance metrics (nvlrx__* and nvltx__*) using the Profiling APIs. These metrics are available on devices with compute capability 7.0, 7.5 and 8.0, and these can be collected at the context level. Refer to the table

[Metrics Mapping Table](https://docs.nvidia.com/main/main.html#metrics-mapping-table)for mapping between earlier CUPTI metrics and the Perfworks NVLink metrics for devices with compute capability 7.0.

**Resolved Issues**

Resolved an issue that causes CUPTI to not return full and completed activity buffers for a long time, CUPTI now attempts to return buffers early.

To reduce the runtime overhead, CUPTI wakes up the worker thread based on certain heuristics instead of waking it up at a regular interval. New API

`cuptiActivityFlushPeriod`

can be used to control the flush period of the worker thread. This setting overrides the CUPTI heurtistics.

#### 1.1.31.13. Updates in CUDA 11.0[#](https://docs.nvidia.com#updates-in-cuda-11-0)

**New Features**

CUPTI adds tracing and profiling support for devices with compute capability 8.0 i.e. NVIDIA A100 GPUs and systems that are based on A100.

Enhancements for CUDA Graph:

Support to correlate the CUDA Graph node with the GPU activities: kernel, memcpy, memset.

Added a new field

`graphNodeId`

for Node Id in the activity records for kernel, memcpy, memset and P2P transfers. Activity records`CUpti_ActivityKernel4`

,`CUpti_ActivityMemcpy2`

,`CUpti_ActivityMemset`

and`CUpti_ActivityMemcpyPtoP`

are deprecated and replaced by new activity records`CUpti_ActivityKernel5`

,`CUpti_ActivityMemcpy3`

,`CUpti_ActivityMemset2`

and`CUpti_ActivityMemcpyPtoP2`

.`graphNodeId`

is the unique ID for the graph node.`graphNodeId`

can be queried using the new CUPTI API`cuptiGetGraphNodeId()`

.Callback

`CUPTI_CBID_RESOURCE_GRAPHNODE_CREATED`

is issued between a pair of the API enter and exit callbacks.

Introduced new callback

`CUPTI_CBID_RESOURCE_GRAPHNODE_CLONED`

to indicate the cloning of the CUDA Graph node.Retain CUDA driver performance optimization in case memset node is sandwiched between kernel nodes. CUPTI no longer disables the conversion of memset nodes into kernel nodes for CUDA graphs.

Added support for cooperative kernels in CUDA graphs.


Added support to trace Optix applications. Refer the

[Optix Profiling](https://docs.nvidia.com/library-support/library-support.html#optix)section.CUPTI overhead is associated with the thread rather than process. Object kind of the overhead record

`CUpti_ActivityOverhead`

is switched to`CUPTI_ACTIVITY_OBJECT_THREAD`

.Added error code

`CUPTI_ERROR_MULTIPLE_SUBSCRIBERS_NOT_SUPPORTED`

to indicate the presence of another CUPTI subscriber. API`cuptiSubscribe()`

returns the new error code than`CUPTI_ERROR_MAX_LIMIT_REACHED`

.Added a new enum

`CUpti_FuncShmemLimitConfig`

to indicate whether user has opted in for maximum dynamic shared memory size on devices with compute capability 7.x by using function attributes`CU_FUNC_ATTRIBUTE_MAX_DYNAMIC_SHARED_SIZE_BYTES`

or`cudaFuncAttributeMaxDynamicSharedMemorySize`

with CUDA driver and runtime respectively. Field`shmemLimitConfig`

in the kernel activity record`CUpti_ActivityKernel5`

shows the user choice. This helps in correct occupancy calculation. Value`FUNC_SHMEM_LIMIT_OPTIN`

in the enum`cudaOccFuncShmemConfig`

is the corresponding option in the CUDA occupancy calculator.

**Resolved Issues**

Resolved an issue that causes incorrect or stale timing for memcopy and serial kernel activities.

Overhead for PC Sampling Activity APIs is reduced by avoiding the reconfiguration of the GPU when PC sampling period doesn’t change between successive kernels. This is applicable for devices with compute capability 7.0 and higher.

Fixed issues in the API

`cuptiFinalize()`

including the issue which may cause the application to crash. This API provides ability for safe and full detach of CUPTI during the execution of the application. More details in the section[Dynamic Detach](https://docs.nvidia.com/main/main.html#dynamic-attach-and-detach).

#### 1.1.31.14. Updates in CUDA 10.2[#](https://docs.nvidia.com#updates-in-cuda-10-2)

**New Features**

CUPTI allows tracing features for non-root and non-admin users on desktop platforms. Note that events and metrics profiling is still restricted for non-root and non-admin users. More details about the issue and the solutions can be found on this

[web page](https://developer.nvidia.com/nvidia-development-tools-solutions-ERR_NVGPUCTRPERM-permission-issue-performance-counters).CUPTI no longer turns off the performance characteristics of CUDA Graph when tracing the application.

CUPTI now shows memset nodes in the CUDA graph.

Fixed the incorrect timing issue for the asynchronous cuMemset/cudaMemset activity.

Several performance improvements are done in the tracing path.


#### 1.1.31.15. Updates in CUDA 10.1 Update 2[#](https://docs.nvidia.com#updates-in-cuda-10-1-update-2)

**New Features**

This release is focused on bug fixes and stability of the CUPTI.

A security vulnerability issue required profiling tools to disable all the features for non-root or non-admin users. As a result, CUPTI cannot profile the application when using a Windows 419.17 or Linux 418.43 or later driver. More details about the issue and the solutions can be found on this

[web page](https://developer.nvidia.com/nvidia-development-tools-solutions-ERR_NVGPUCTRPERM-permission-issue-performance-counters).

#### 1.1.31.16. Updates in CUDA 10.1 Update 1[#](https://docs.nvidia.com#updates-in-cuda-10-1-update-1)

**New Features**

Support for the IBM POWER platform is added for the

Profiling APIs in the header

`cupti_profiler_target.h`

Perfworks metric APIs in the headers

`nvperf_host.h`

and`nvperf_target.h`



#### 1.1.31.17. Updates in CUDA 10.1[#](https://docs.nvidia.com#updates-in-cuda-10-1)

**New Features**

This release is focused on bug fixes and performance improvements.

The new set of profiling APIs and Perfworks metric APIs which were introduced in the CUDA Toolkit 10.0 are now integrated into the CUPTI library distributed in the CUDA Toolkit. Refer to the sections

[CUPTI Profiling API](https://docs.nvidia.com/main/main.html#cupti-profiling-api)and[Perfworks Metric APIs](https://docs.nvidia.com/main/main.html#perfworks-metric-api)for documentation of the new APIs.Event collection mode

`CUPTI_EVENT_COLLECTION_MODE_CONTINUOUS`

is now supported on all device classes including Geforce and Quadro.Support for the NVTX string registration API

`nvtxDomainRegisterStringA().`

Added enum

`CUpti_PcieGen`

to list PCIe generations.

#### 1.1.31.18. Updates in CUDA 10.0[#](https://docs.nvidia.com#updates-in-cuda-10-0)

**New Features**

Added tracing support for devices with compute capability 7.5.

A new set of metric APIs are added for devices with compute capability 7.0 and higher. These provide low and deterministic profiling overhead on the target system. These APIs are currently supported only on Linux x86 64-bit and Windows 64-bit platforms. Refer to the

[CUPTI web page](https://developer.nvidia.com/cupti)for documentation and details to download the package with support for these new APIs. Note that both the old and new metric APIs are supported for compute capability 7.0. This is to enable transition of code to the new metric APIs. But one cannot mix the usage of the old and new metric APIs.CUPTI supports profiling of OpenMP applications. OpenMP profiling information is provided in the form of new activity records

`CUpti_ActivityOpenMp`

. New API`cuptiOpenMpInitialize`

is used to initialize profiling for supported OpenMP runtimes.Activity record for kernel

`CUpti_ActivityKernel4`

provides shared memory size set by the CUDA driver.Tracing support for CUDA kernels, memcpy and memset nodes launched by a CUDA Graph.

Added support for resource callbacks for resources associated with the CUDA Graph. Refer enum

`CUpti_CallbackIdResource`

for new callback IDs.

#### 1.1.31.19. Updates in CUDA 9.2[#](https://docs.nvidia.com#updates-in-cuda-9-2)

**New Features**

Added support to query PCI devices information which can be used to construct the PCIe topology. See activity kind

`CUPTI_ACTIVITY_KIND_PCIE`

and related activity record`CUpti_ActivityPcie`

.To view and analyze bandwidth of memory transfers over PCIe topologies, new set of metrics to collect total data bytes transmitted and received through PCIe are added. Those give accumulated count for all devices in the system. These metrics are collected at the device level for the entire application. And those are made available for devices with compute capability 5.2 and higher.

CUPTI added support for new metrics:

Instruction executed for different types of load and store

Total number of cached global/local load requests from SM to texture cache

Global atomic/non-atomic/reduction bytes written to L2 cache from texture cache

Surface atomic/non-atomic/reduction bytes written to L2 cache from texture cache

Hit rate at L2 cache for all requests from texture cache

Device memory (DRAM) read and write bytes

The utilization level of the multiprocessor function units that execute tensor core instructions for devices with compute capability 7.0


A new attribute

`CUPTI_EVENT_ATTR_PROFILING_SCOPE`

is added under enum`CUpti_EventAttribute`

to query the profiling scope of a event. Profiling scope indicates if the event can be collected at the context level or device level or both. See Enum`CUpti_EventProfilingScope`

for available profiling scopes.A new error code

`CUPTI_ERROR_VIRTUALIZED_DEVICE_NOT_SUPPORTED`

is added to indicate that tracing and profiling on virtualized GPU is not supported.

#### 1.1.31.20. Updates in CUDA 9.1[#](https://docs.nvidia.com#updates-in-cuda-9-1)

**New Features**

Added a field for correlation ID in the activity record

`CUpti_ActivityStream`

.

#### 1.1.31.21. Updates in CUDA 9.0[#](https://docs.nvidia.com#updates-in-cuda-9-0)

**New Features**

CUPTI extends tracing and profiling support for devices with compute capability 7.0.

Usage of compute device memory can be tracked through CUPTI. A new activity record

`CUpti_ActivityMemory`

and activity kind`CUPTI_ACTIVITY_KIND_MEMORY`

are added to track the allocation and freeing of memory. This activity record includes fields like virtual base address, size, PC (program counter), timestamps for memory allocation and free calls.Unified memory profiling adds new events for thrashing, throttling, remote map and device-to-device migration on 64 bit Linux platforms. New events are added under enum

`CUpti_ActivityUnifiedMemoryCounterKind`

. Enum`CUpti_ActivityUnifiedMemoryRemoteMapCause`

lists possible causes for remote map events.PC sampling supports wide range of sampling periods ranging from 2^5 cycles to 2^31 cycles per sample. This can be controlled through new field

`samplingPeriod2`

in the PC sampling configuration struct`CUpti_ActivityPCSamplingConfig`

.Added API

`cuptiDeviceSupported()`

to check support for a compute device.Activity record

`CUpti_ActivityKernel3`

for kernel execution has been deprecated and replaced by new activity record`CUpti_ActivityKernel4`

. New record gives information about queued and submit timestamps which can help to determine software and hardware latencies associated with the kernel launch. These timestamps are not collected by default. Use API`cuptiActivityEnableLatencyTimestamps()`

to enable collection. New field`launchType`

of type`CUpti_ActivityLaunchType`

can be used to determine if it is a cooperative CUDA kernel launch.Activity record

`CUpti_ActivityPCSampling2`

for PC sampling has been deprecated and replaced by new activity record`CUpti_ActivityPCSampling3`

. New record accommodates 64-bit PC Offset supported on devices of compute capability 7.0 and higher.Activity record

`CUpti_ActivityNvLink`

for NVLink attributes has been deprecated and replaced by new activity record`CUpti_ActivityNvLink2`

. New record accommodates increased port numbers between two compute devices.Activity record

`CUpti_ActivityGlobalAccess2`

for source level global accesses has been deprecated and replaced by new activity record`CUpti_ActivityGlobalAccess3`

. New record accommodates 64-bit PC Offset supported on devices of compute capability 7.0 and higher.New attributes

`CUPTI_ACTIVITY_ATTR_PROFILING_SEMAPHORE_POOL_SIZE`

and`CUPTI_ACTIVITY_ATTR_PROFILING_SEMAPHORE_POOL_LIMIT`

are added in the activity attribute enum`CUpti_ActivityAttribute`

to set and get the profiling semaphore pool size and the pool limit.

#### 1.1.31.22. Updates in CUDA 8.0[#](https://docs.nvidia.com#updates-in-cuda-8-0)

**New Features**

Sampling of the program counter (PC) is enhanced to point out the true latency issues, it indicates if the stall reasons for warps are actually causing stalls in the issue pipeline. Field

`latencySamples`

of new activity record`CUpti_ActivityPCSampling2`

provides true latency samples. This field is valid for devices with compute capability 6.0 and higher. See section[PC Sampling](https://docs.nvidia.com/main/main.html#cupti-pc-sampling-api)for more details.Support for NVLink topology information such as the pair of devices connected via NVLink, peak bandwidth, memory access permissions etc is provided through new activity record

`CUpti_ActivityNvLink`

. NVLink performance metrics for data transmitted/received, transmit/receive throughput and respective header overhead for each physical link. See section[NVLink](https://docs.nvidia.com/main/main.html#nvlink)for more details.CUPTI supports profiling of OpenACC applications. OpenACC profiling information is provided in the form of new activity records

`CUpti_ActivityOpenAccData`

,`CUpti_ActivityOpenAccLaunch`

and`CUpti_ActivityOpenAccOther`

. This aids in correlating OpenACC constructs on the CPU with the corresponding activity taking place on the GPU, and mapping it back to the source code. New API`cuptiOpenACCInitialize`

is used to initialize profiling for supported OpenACC runtimes. See section[OpenACC](https://docs.nvidia.com/main/main.html#openacc)for more details.Unified memory profiling provides GPU page fault events on devices with compute capability 6.0 and 64 bit Linux platforms. Enum

`CUpti_ActivityUnifiedMemoryAccessType`

lists memory access types for GPU page fault events and enum`CUpti_ActivityUnifiedMemoryMigrationCause`

lists migration causes for data transfer events.Unified Memory profiling support is extended to Mac platform.

Support for 16-bit floating point (FP16) data format profiling. New metrics inst_fp_16, flop_count_hp_add, flop_count_hp_mul, flop_count_hp_fma, flop_count_hp, flop_hp_efficiency, half_precision_fu_utilization are supported. Peak FP16 flops per cycle for device can be queried using the enum

`CUPTI_DEVICE_ATTR_FLOP_HP_PER_CYCLE`

added to`CUpti_DeviceAttribute`

.Added new activity kinds

`CUPTI_ACTIVITY_KIND_SYNCHRONIZATION`

,`CUPTI_ACTIVITY_KIND_STREAM`

and`CUPTI_ACTIVITY_KIND_CUDA_EVENT`

, to support the tracing of CUDA synchronization constructs such as context, stream and CUDA event synchronization. Synchronization details are provided in the form of new activity record`CUpti_ActivitySynchronization`

. Enum`CUpti_ActivitySynchronizationType`

lists different types of CUDA synchronization constructs.APIs

`cuptiSetThreadIdType()`

/`cuptiGetThreadIdType()`

to set/get the mechanism used to fetch the thread-id used in CUPTI records. Enum`CUpti_ActivityThreadIdType`

lists all supported mechanisms.Added API

`cuptiComputeCapabilitySupported()`

to check the support for a specific compute capability by the CUPTI.Added support to establish correlation between an external API (such as OpenACC, OpenMP) and CUPTI API activity records. APIs

`cuptiActivityPushExternalCorrelationId()`

and`cuptiActivityPopExternalCorrelationId()`

should be used to push and pop external correlation ids for the calling thread. Generated records of type`CUpti_ActivityExternalCorrelation`

contain both external and CUPTI assigned correlation ids.Added containers to store the information of events and metrics in the form of activity records

`CUpti_ActivityInstantaneousEvent`

,`CUpti_ActivityInstantaneousEventInstance`

,`CUpti_ActivityInstantaneousMetric`

and`CUpti_ActivityInstantaneousMetricInstance`

. These activity records are not produced by the CUPTI, these are included for completeness and ease-of-use. Profilers built on top of CUPTI that sample events may choose to use these records to store the collected event data.Support for domains and annotation of synchronization objects added in NVTX v2. New activity record

`CUpti_ActivityMarker2`

and enums to indicate various stages of synchronization object i.e.`CUPTI_ACTIVITY_FLAG_MARKER_SYNC_ACQUIRE`

,`CUPTI_ACTIVITY_FLAG_MARKER_SYNC_ACQUIRE_SUCCESS`

,`CUPTI_ACTIVITY_FLAG_MARKER_SYNC_ACQUIRE_FAILED`

and`CUPTI_ACTIVITY_FLAG_MARKER_SYNC_RELEASE`

are added.Unused field

`runtimeCorrelationId`

of the activity record`CUpti_ActivityMemset`

is broken into two fields`flags`

and`memoryKind`

to indicate the asynchronous behavior and the kind of the memory used for the memset operation. It is supported by the new flag`CUPTI_ACTIVITY_FLAG_MEMSET_ASYNC`

added in the enum`CUpti_ActivityFlag`

.Added flag

`CUPTI_ACTIVITY_MEMORY_KIND_MANAGED`

in the enum`CUpti_ActivityMemoryKind`

to indicate managed memory.API

`cuptiGetStreamId`

has been deprecated. A new API`cuptiGetStreamIdEx`

is introduced to provide the stream id based on the legacy or per-thread default stream flag.

#### 1.1.31.23. Updates in CUDA 7.5[#](https://docs.nvidia.com#updates-in-cuda-7-5)

**New Features**

Device-wide sampling of the program counter (PC) is enabled by default. This was a preview feature in the CUDA Toolkit 7.0 release and it was not enabled by default.

Ability to collect all events and metrics accurately in presence of multiple contexts on the GPU is extended for devices with compute capability 5.x.

API

`cuptiGetLastError`

is introduced to return the last error that has been produced by any of the CUPTI API calls or the callbacks in the same host thread.Unified memory profiling is supported with MPS (Multi-Process Service)

Callback is provided to collect replay information after every kernel run during kernel replay. See API

`cuptiKernelReplaySubscribeUpdate`

and callback type`CUpti_KernelReplayUpdateFunc`

.Added new attributes in enum

`CUpti_DeviceAttribute`

to query maximum shared memory size for different cache preferences for a device function.

#### 1.1.31.24. Updates in CUDA 7.0[#](https://docs.nvidia.com#updates-in-cuda-7-0)

**New Features**

CUPTI supports device-wide sampling of the program counter (PC). Program counters along with the stall reasons from all active warps are sampled at a fixed frequency in the round robin order. Activity record

`CUpti_ActivityPCSampling`

enabled using activity kind`CUPTI_ACTIVITY_KIND_PC_SAMPLING`

outputs stall reason along with PC and other related information. Enum`CUpti_ActivityPCSamplingStallReason`

lists all the stall reasons. Sampling period is configurable and can be tuned using API`cuptiActivityConfigurePCSampling`

. This feature is available on devices with compute capability 5.2.Added new activity record

`CUpti_ActivityInstructionCorrelation`

which can be used to dump source locator records for all the PCs of the function.All events and metrics for devices with compute capability 3.x and 5.0 can be collected accurately in presence of multiple contexts on the GPU. In previous releases only some events and metrics could be collected accurately when multiple contexts were executing on the GPU.

Unified memory profiling is enhanced by providing fine grain data transfers to and from the GPU, coupled with more accurate timestamps with each transfer. This information is provided through new activity record

`CUpti_ActivityUnifiedMemoryCounter2`

, deprecating old record`CUpti_ActivityUnifiedMemoryCounter`

.MPS tracing and profiling support is extended on multi-gpu setups.

Activity record

`CUpti_ActivityDevice`

for device information has been deprecated and replaced by new activity record`CUpti_ActivityDevice2`

. New record adds device UUID which can be used to uniquely identify the device across profiler runs.Activity record

`CUpti_ActivityKernel2`

for kernel execution has been deprecated and replaced by new activity record`CUpti_ActivityKernel3`

. New record gives information about Global Partitioned Cache Configuration requested and executed. Partitioned global caching has an impact on occupancy calculation. If it is ON, then a CTA can only use a half SM, and thus a half of the registers available per SM. The new fields apply for devices with compute capability 5.2 and higher. Note that this change was done in CUDA 6.5 release with support for compute capability 5.2.

#### 1.1.31.25. Updates in CUDA 6.5[#](https://docs.nvidia.com#updates-in-cuda-6-5)

**New Features**

Instruction classification is done for source-correlated Instruction Execution activity

`CUpti_ActivityInstructionExecution`

. See`CUpti_ActivityInstructionClass`

for instruction classes.Two new device attributes are added to the activity

`CUpti_DeviceAttribute`

:`CUPTI_DEVICE_ATTR_FLOP_SP_PER_CYCLE`

gives peak single precision flop per cycle for the GPU.`CUPTI_DEVICE_ATTR_FLOP_DP_PER_CYCLE`

gives peak double precision flop per cycle for the GPU.

Two new metric properties are added:

`CUPTI_METRIC_PROPERTY_FLOP_SP_PER_CYCLE`

gives peak single precision flop per cycle for the GPU.`CUPTI_METRIC_PROPERTY_FLOP_DP_PER_CYCLE`

gives peak double precision flop per cycle for the GPU.

Activity record

`CUpti_ActivityGlobalAccess`

for source level global access information has been deprecated and replaced by new activity record`CUpti_ActivityGlobalAccess2`

. New record additionally gives information needed to map SASS assembly instructions to CUDA C source code. And it also provides ideal L2 transactions count based on the access pattern.Activity record

`CUpti_ActivityBranch`

for source level branch information has been deprecated and replaced by new activity record`CUpti_ActivityBranch2`

. New record additionally gives information needed to map SASS assembly instructions to CUDA C source code.Sample

`sass_source_map`

is added to demonstrate the mapping of SASS assembly instructions to CUDA C source code.Default event collection mode is changed to Kernel (

`CUPTI_EVENT_COLLECTION_MODE_KERNEL`

) from Continuous (`CUPTI_EVENT_COLLECTION_MODE_CONTINUOUS`

). Also Continuous mode is supported only on Tesla devices.Profiling results might be inconsistent when auto boost is enabled. Profiler tries to disable auto boost by default, it might fail to do so in some conditions, but profiling will continue. A new API

`cuptiGetAutoBoostState`

is added to query the auto boost state of the device. This API returns error`CUPTI_ERROR_NOT_SUPPORTED`

on devices that don’t support auto boost. Note that auto boost is supported only on certain Tesla devices from the Kepler+ family.Activity record

`CUpti_ActivityKernel2`

for kernel execution has been deprecated and replaced by new activity record`CUpti_ActivityKernel3`

. New record additionally gives information about Global Partitioned Cache Configuration requested and executed. The new fields apply for devices with 5.2 Compute Capability.

#### 1.1.31.26. Updates in CUDA 6.0[#](https://docs.nvidia.com#updates-in-cuda-6-0)

**New Features**

Two new CUPTI activity kinds have been introduced to enable two new types of source-correlated data collection. The

`Instruction Execution`

kind collects SASS-level instruction execution counts, divergence data, and predication data. The`Shared Access`

kind collects source correlated data indication inefficient shared memory accesses.CUPTI provides support for CUDA applications using Unified Memory. A new activity record reports Unified Memory activity such as transfers to and from a GPU and the number of Unified Memory related page faults.

CUPTI recognized and reports the special MPS context that is used by CUDA applications running on a system with MPS enabled.

The CUpti_ActivityContext activity record

`CUpti_ActivityContext`

has been updated to introduce a new field into the structure in a backwards compatible manner. The 32-bit`computeApiKind`

field was replaced with two 16 bit fields,`computeApiKind`

and`defaultStreamId`

. Because all valid`computeApiKind`

values fit within 16 bits, and because all supported CUDA platforms are little-endian, persisted context record data read with the new structure will have the correct value for`computeApiKind`

and have a value of zero for`defaultStreamId`

. The CUPTI client is responsible for versioning the persisted context data to recognize when the`defaultStreamId`

field is valid.To ensure that metric values are calculated as accurately as possible, a new metric API is introduced. Function

`cuptiMetricGetRequiredEventGroupSets`

can be used to get the groups of events that should be collected at the same time.Execution overheads introduced by CUPTI have been dramatically decreased.

The new activity buffer API introduced in CUDA Toolkit 5.5 is required. The legacy

`cuptiActivityEnqueueBuffer`

and`cuptiActivityDequeueBuffer`

functions have been removed.

#### 1.1.31.27. Updates in CUDA 5.5[#](https://docs.nvidia.com#updates-in-cuda-5-5)

**New Features**

Applications that use CUDA Dynamic Parallelism can be profiled using CUPTI. Device-side kernel launches are reported using a new activity kind.

Device attributes such as power usage, clocks, thermals, etc. are reported via a new activity kind.

A new activity buffer API uses callbacks to request and return buffers of activity records. The existing

`cuptiActivityEnqueueBuffer`

and`cuptiActivityDequeueBuffer`

functions are still supported but are deprecated and will be removed in a future release.The Event API supports kernel replay so that any number of events can be collected during a single run of the application.

A new metric API

`cuptiMetricGetValue2`

allows metric values to be calculated for any device, even if that device is not available on the system.CUDA peer-to-peer memory copies are reported explicitly via the activity API. In previous releases these memory copies were only partially reported.


## 1.2. Known Issues[#](https://docs.nvidia.com#known-issues)

The following are known issues with the current release.

A security vulnerability issue required profiling tools to disable features using GPU performance counters for non-root or non-admin users when using a Windows 419.17 or Linux 418.43 or later driver. By default, NVIDIA drivers require elevated permissions to access GPU performance counters. On Tegra platforms, profile as root or using sudo. On other platforms, you can either start profiling as root or using sudo, or by enabling non-admin profiling. On Windows, when in MCDM mode, a different set of steps is required for display driver versions prior to 570. More details about the issue and the solutions can be found on the ERR_NVGPUCTRPERM

[web page](https://developer.nvidia.com/ERR_NVGPUCTRPERM).Note

CUPTI allows tracing features for non-root and non-admin users on desktop platforms only, Tegra platforms require root or sudo access.

Profiling results might be inconsistent when auto boost is enabled. Profiler tries to disable auto boost by default. But it might fail to do so in some conditions and profiling will continue and results will be inconsistent. API

`cuptiGetAutoBoostState()`

can be used to query the auto boost state of the device. This API returns error`CUPTI_ERROR_NOT_SUPPORTED`

on devices that don’t support auto boost. Note that auto boost is supported only on certain Tesla devices with compute capability 3.0 and higher.CUPTI doesn’t populate the activity structures which are deprecated, instead the newer version of the activity structure is filled with the information.

Because of the low resolution of the timer on Windows, the start and end timestamps can be same for activities having short execution duration on Windows.

The application which calls CUPTI APIs cannot be used with Nvidia tools like

`nvprof`

,`Nvidia Visual Profiler`

,`Nsight Compute`

,`Nsight Systems`

,`Nvidia Nsight Visual Studio Edition`

,`cuda-gdb`

and`cuda-memcheck`

.PCIe and NVLink records, when enabled using the API

`cuptiActivityEnable`

, are not captured when CUPTI is initialized lazily after the CUDA initialization. API`cuptiActivityEnableAndDump`

can be used to dump the records for these activities at any point during the profiling session.CUPTI fails to profile the OpenACC application when the OpenACC library linked with the application has missing definition of the OpenACC API routine/s. This is indicated by the error code

`CUPTI_ERROR_OPENACC_UNDEFINED_ROUTINE`

.OpenACC profiling might fail when OpenACC library is linked statically in the user application. This happens due to the missing definition of the OpenACC API routines needed for the OpenACC profiling, as compiler might ignore definitions for the functions not used in the application. This issue can be mitigated by linking the OpenACC library dynamically.

Unified memory profiling is not supported on the ARM architecture.

Profiling a C++ application which overloads the new operator at the global scope and uses any CUDA APIs like cudaMalloc() or cudaMallocManaged() inside the overloaded new operator will result in a hang.

Devices with compute capability 6.0 and higher introduce a new feature, compute preemption, to give fair chance for all compute contexts while running long tasks. With compute preemption feature-

If multiple contexts are running in parallel it is possible that long kernels will get preempted.

Some kernels may get preempted occasionally due to timeslice expiry for the context.


If kernel has been preempted, the time the kernel spends preempted is still counted towards kernel duration.

To avoid compute preemption affecting profiler results try to isolate the context being profiled:

Run the application on secondary GPU where display is not connected.

On Linux if the application is running on the primary GPU where the display driver is connected then unload the display driver.

Run only one process that uses GPU at one time.


Devices with compute capability 6.0 and higher support demand paging. When the kernel is scheduled for the first time, all the pages allocated using cudaMallocManaged and that are required for execution of the kernel are fetched in the global memory when GPU faults are generated. Profiler requires multiple passes to collect all the metrics required for kernel analysis. The kernel state needs to be saved and restored for each kernel replay pass. For devices with compute capability 6.0 and higher and platforms supporting Unified memory, in the first kernel iteration the GPU faults will be generated and all pages will be fetched in the global memory. Second iteration onwards GPU page faults will not occur. This will significantly affect the memory related events and timing. The time taken from trace will include the time required to fetch the pages but most of the metrics profiled in multiple iterations will not include time/cycles required to fetch the pages. This causes inconsistency in the profiler results.

When profiling an application that uses CUDA Dynamic Parallelism (CDP) there are several limitations to the profiling tools. CUDA 12.0 adds support for revamped CUDA Dynamic Parallelism APIs (referred to as CDP2), offering substantial performance improvements vs. the legacy CUDA Dynamic Parallelism APIs (referred to as CDP1).

For Legacy CUDA Dynamic Parallelism (CDP1), CUPTI supports tracing of all host and device kernels for devices with compute capability 5.x and 6.x. For devices with compute capability 7.0 and higher, CUPTI traces all the host launched kernels until it encounters a host launched kernel which launches child kernels; subsequent kernels are not traced.

For CUDA Dynamic Parallelism (CDP2), CUPTI supports tracing of host launched kernels only, it can’t trace device launched kernels.

CUPTI doesn’t report CUDA API calls for device launched kernels.

CUPTI doesn’t support profiling of device launched kernels i.e. it doesn’t report detailed event, metric, and source-level results for device launched kernels. Event, metric, and source-level results collected for CPU-launched kernels will include event, metric, and source-level results for the entire call-tree of kernels launched from within that kernel.


Compilation of samples autorange_profiling and userrange_profiling requires a host compiler which supports C++11 features. For some g++ compilers, it is required to use the flag -std=c++11 to turn on C++11 features.

As of CUDA 11.4 and R470 TRD1 driver release, CUPTI is supported in a vGPU environment which requires a vGPU license. If the license is not obtained after 20 minutes, the reported performance data including metrics from the GPU will be inaccurate. This is because of a feature in vGPU environment which reduces performance but retains functionality as specified

[here](https://docs.nvidia.com/grid/latest/grid-licensing-user-guide/index.html#software-enforcement-grid-licensing).CUPTI is not supported on NVIDIA Crypto Mining Processors (CMP). This is reported using the error code

`CUPTI_ERROR_CMP_DEVICE_NOT_SUPPORTED`

. For more information, please visit the[web page](https://developer.nvidia.com/ERR_NVCMPGPU).CUPTI versions shipped in the CUDA Toolkit 11.7 and CUDA Toolkit 11.8 don’t support Kepler (sm_35 and sm_37) devices. Refer to the webpages

[CUPTI 11.7](https://developer.nvidia.com/cupti-ctk11_7)and[CUPTI 11.8](https://developer.nvidia.com/cupti-ctk11_8)for location of the CUPTI packages having the support for these Kepler devices.Support for the GA103 GPU was added in the CUDA 11.6 release but it was broken for releases from CUDA 11.8 to CUDA 12.2 Update 1.

For confidential computing devices, allocation of pinned (page-locked) host memory for profiling buffer for concurrent kernel tracing is not supported. Setting attribute

`CUPTI_ACTIVITY_ATTR_MEM_ALLOCATION_TYPE_HOST_PINNED`

of the activity attribute enum`CUpti_ActivityAttribute`

will return the error code`CUPTI_ERROR_NOT_SUPPORTED`

.With the new PC Sampling APIs CUPTI doesn’t report any pc sampling data for cuda graph launches in serialized mode.

There can be a long delay in attaching CUPTI to a running process. It is possible that the thread might starve if it is unable to access the resources it needs to perform the attach operation, as other threads have higher priority or hold locks on these resources.

Concurrent kernel tracing is not supported for cooperative kernel launches under MPS for pre-Hopper archs, and it can cause hang.

The latency timestamps i.e. queued and submitted timestamps are not supported for the HW events based kernel tracing.

NVTX versions 3.2.0 and 3.2.1 do not work for developer tools (including CUPTI) that do not handle the NVTX API

`nvtxDomainIsEnabled`

. This issue has been resolved in NVTX version 3.2.2.Since kernel launches in CUDA Graphs may not be serializable,

`CUPTI_ACTIVITY_KIND_KERNEL`

does not support serialized kernel tracing for graph-executed kernels; as a result, their start and end timestamps are reported as zero or invalid.

### 1.2.1. Profiling[#](https://docs.nvidia.com#profiling)

#### 1.2.1.1. Range Profiling API and Profiling API[#](https://docs.nvidia.com#range-profiling-api-and-profiling-api)

The following are common known issues for the Range Profiling API and the Profiling API:

Profiling may significantly change the overall performance characteristics of the application. Refer to the section

[CUPTI Overhead](https://docs.nvidia.com/main/main.html#cupti-overhead)for more details.Profiling a kernel while other contexts are active on the same device (e.g. X server, or secondary CUDA or graphics application) can result in varying metric values for L2/FB (Device Memory) related metrics. Specifically, L2/FB traffic from non-profiled contexts cannot be excluded from the metric results. To completely avoid this issue, profile the application on a GPU without secondary contexts accessing the same device (e.g. no X server on Linux).

Profiling is not supported for multidevice cooperative kernels, that is, kernels launched by using the API functions

`cudaLaunchCooperativeKernelMultiDevice`

or`cuLaunchCooperativeKernelMultiDevice`

.Enabling certain events can cause GPU kernels to run longer than the driver’s watchdog time-out limit. In these cases the driver will terminate the GPU kernel resulting in an application error and profiling data will not be available. Please disable the driver watchdog time out before profiling such long running CUDA kernels

On Linux, setting the X Config option Interactive to false is recommended.

For Windows, detailed information about TDR (Timeout Detection and Recovery) and how to disable it is available at

[https://docs.microsoft.com/en-us/windows-hardware/drivers/display/timeout-detection-and-recovery](https://docs.microsoft.com/en-us/windows-hardware/drivers/display/timeout-detection-and-recovery)

The values of operations/second calculated from this NVIDIA developer tools site and generated by using the data center monitoring tools are not calculated in the same way as the operations/second used for export control purposes and should not be relied upon to assess performance against the export control limits.

Profiling a kernel while any other GPU work is executing on the same MIG compute instance can result in varying metric values for all units. Care should be taken to serialize, or otherwise prevent concurrent CUDA launches within the target application to ensure those kernels do not influence each other. Be aware that GPU work issued through other APIs in the target process or workloads created by non-target processes running simultaneously in the same MIG compute instance will influence the collected metrics. Note that it is acceptable to run CUDA processes in other MIG compute instances as they will not influence the profiled MIG compute instance.

NVLink performance metrics (

`nvlrx__*`

and`nvltx__*`

) are supported by the Range Profiling API but not by the Profiling API.Profiling is not supported under MPS (Multi-Process Service).

For profiling the CUDA kernel nodes launched by a CUDA Graph, not all combinations of range profiling and replay modes are supported. Here are some limitations:

User replay and application replay modes with auto range are not supported.

In the user range mode, entire graph is profiled as one workload i.e. all the kernel nodes launched by the CUDA Graph will be profiled and single result will be provided, user can’t do the profiling for a range of kernels.

For Device Graph profiling in the auto range and kernel replay mode, each kernel node will be profiled except for the nodes which launch device graphs.


Profiling kernels executed on a device that is part of an SLI group is not supported.

Profiling on Windows Subsystem for Linux (WSL) is only supported with WSL version 2, NVIDIA display driver version 525 or higher and Windows 11.

Profiling support for applications using Green Contexts is unavailable in CUPTI versions prior to 13.3.

Profiling is not supported for device graphs which have been updated after instantiation.

When NVLink-centric scheduling is enabled, some SM resources may not be available to the workload, which can result in lower-than-expected measured utilization.


## 1.3. Support[#](https://docs.nvidia.com#support)

Information on supported platforms and GPUs.

### 1.3.1. Platform Support[#](https://docs.nvidia.com#platform-support)

Platform |
Support |
|---|---|
Windows (x86_64) |
Yes |
Windows (arm64) |
Yes |
Windows Subsystem for Linux version 2 (WSL 2) |
Yes |
Linux (x86_64) |
Yes |
Linux (aarch64 sbsa) |
Yes |
Linux (x86_64) (Drive SDK) |
Yes |
Linux (aarch64) |
Yes |
Linux (ppc64le) |
No |
QNX |
Yes |
Mac OSX |
No |
Android |
No |

Tracing and profiling of 32-bit processes is not supported.

### 1.3.2. GPU Support[#](https://docs.nvidia.com#gpu-support)

CUPTI API |
Supported GPU architectures |
|---|---|
Activity |
Turing and later GPU architectures, i.e. devices with compute capability 7.5 and higher |
Callback |
Turing and later GPU architectures, i.e. devices with compute capability 7.5 and higher |
Host Profiling |
Turing and later GPU architectures, i.e. devices with compute capability 7.5 and higher |
Range Profiling |
Turing and later GPU architectures, i.e. devices with compute capability 7.5 and higher |
PC Sampling |
Turing and later GPU architectures, i.e. devices with compute capability 7.5 and higher |
SASS Metric |
Turing and later GPU architectures, i.e. devices with compute capability 7.5 and higher |
PM Sampling |
Turing and later GPU architectures, i.e. devices with compute capability 7.5 and higher |
Profiling |
Turing through Blackwell GPU architectures. Not supported on Rubin and later GPU architectures |
Checkpoint |
Turing and later GPU architectures, i.e. devices with compute capability 7.5 and higher |