source: https://docs.nvidia.com/compute-sanitizer/ReleaseNotes/index.html

# Release Notes[#](https://docs.nvidia.com#release-notes)

## Release Notes[#](https://docs.nvidia.com#id1)

### Updates in 2026.3[#](https://docs.nvidia.com#updates-in-2026-3)

Added support for the Rubin architecture.

Added support for Windows on ARM.

Added initcheck support for

`cudaMemcpyBatchAsync`

APIs.Added detection for out-of-bounds accesses outside of static and dynamic shared memory boundaries when using compile-time patching on Hopper and newer.

Added the

`--racecheck-filter-cluster-id`

option to limit Racecheck checks to select clusters, or blocks when clusters are not in use.Improved support for the

`ignore_oob`

modifier of`cp.async.bulk`

.Fixed potential false positives in racecheck when using

`mbarrier complete-tx`

operations.Fixed an issue where python applications could crash or have an incorrect host backtrace in some environments.

Fixed an issue where initcheck could destroy the context when reporting an error in some cases.

Fixed a potential false positive in initcheck when using

`atom.exch`

.Fixed a crash on aarch64 when reporting

`tcmma`

guardrails errors.Fixed a number of device crashes on Blackwell in various situations.

Reduced the occurrence of duplicated error reports on L4T and QNX.


### Updates in 2026.2.1[#](https://docs.nvidia.com#updates-in-2026-2-1)

Added memcheck support for fabric operations.

Fixed a false positive with memcheck when using

`cp.async.bulk`

with the`ignore_oob`

modifier.Fixed potential false positives in initcheck on shared memory.

Fixed a rare hang in racecheck on Windows when the program is exiting.


### Updates in 2026.2[#](https://docs.nvidia.com#updates-in-2026-2)

Added memcheck support for TMA load operations.

Silenced some CUDA API error reports that are not user actionable.

Fixed an issue where the sanitizer may crash during program termination on L4T.

Fixed a memcheck false positive with

`cp.async.bulk`

when using`cp_mask`

.Fixed an issue where tensor memory guardrail error reporting may lead to the program crashing.


### Updates in 2026.1.1[#](https://docs.nvidia.com#updates-in-2026-1-1)

Silenced non-actionable extended CUDA API error reports.


### Updates in 2026.1[#](https://docs.nvidia.com#updates-in-2026-1)

Added support for extended CUDA API error reporting. This option is enabled by default and may result in newly-displayed error reports. See

[CUDA API Error Checking](https://docs.nvidia.com/ComputeSanitizer/index.html#api-error-checking).Added support for the

`.ignore_oob`

qualifier of the`cp.async.bulk`

PTX instruction.Fixed an issue with device backtraces on generic memory accesses.

Fixed an issue with coredump generation in synccheck and initcheck for shared memory (requires a driver version superior or equal to 595).

Fixed false positives and false negatives in racecheck involving indirect barrier synchronization dependencies across clusters.

Fixed false positives in racecheck when using warpgroup-level synchronizations on Hopper.

Fixed other false positives in racecheck.

Fixed potential false positives in memcheck and initcheck.

Fixed a false positive in initcheck when using

`cp.async.bulk`

.

### Updates in 2025.4.1[#](https://docs.nvidia.com#updates-in-2025-4-1)

Fixed a false positive with memcheck stream-ordered allocation race detection when using memory allocated with

`cudaMallocAsync`

on the null stream from another stream created after the allocation.Fixed a memory leak when using Python to launch CUDA kernels.


### Updates in 2025.4[#](https://docs.nvidia.com#updates-in-2025-4)

Added support for the

`-fdevice-sanitize=memcheck`

compiler option. See[Compile-time patching](https://docs.nvidia.com/ComputeSanitizer/index.html#compile-time-patching).Added support for initcheck on shared memory using the

`--initcheck-address-space`

option. See[Initcheck address space selection](https://docs.nvidia.com/ComputeSanitizer/index.html#initcheck-as).Added initcheck support for the PTX instruction

`cp.async.bulk`

and`cp.async.red`

.Added support for atomic reduction stream memory operations in initcheck and the sanitizer API.

Added support stream-ordered allocations race detection for green contexts. The stream-ordered allocations race detection is now enabled by default.

Added the

`--report-device-side-allocation-failure`

option for memcheck to report device-side`malloc()`

returning`NULL`

.Added

`SANITIZER_CUDA_BARRIER_CP_ASYNC_ARRIVE`

and`SANITIZER_CUDA_BARRIER_CP_ASYNC_ARRIVE_NO_INC`

cuda barrier type in the public API. These were both reported as`SANITIZER_CUDA_BARRIER_ARRIVE`

previously. A compiler from the 13.1 CUDA Toolkit or more recent is required for full accuracy.Fixed an issue where synccheck would report false positives when using

`cp.arrive.async`

without`.noinc`

. It is required to recompile applications with the compiler included in the 13.1 CUDA Toolkit or more recent to benefit from the fix.Fixed an issue where the device backtrace would be incomplete or corrupted when reporting errors on generic memory accesses.

Fixed multiple false-positives in racecheck involving

`mbarrier`

usage.Fixed an issue where some applications may crash during the program exit on Windows.

Fixed an issue where some applications may hang during the program exit on Windows. This requires a driver version of 590 or more recent.


### Updates in 2025.3.1[#](https://docs.nvidia.com#updates-in-2025-3-1)

Fixed an issue where racecheck on Windows may hang at the end of the program in some cases.


### Updates in 2025.3[#](https://docs.nvidia.com#updates-in-2025-3)

Removed support for Maxwell, Pascal and Volta GPUs.

Added support for PTX instructions

`st.async`

and`red.async`

with`.release`

semantics on Blackwell.Added additional types of deadlock detection with the

`--racecheck-deadlock-timeout`

.Fixed potential false positives in racecheck related to warpsync on Blackwell.

Fixed an issue where some events were not reported when the first lane of a warp was not active when using the

`racecheck-trace-sync`

option.Fixed potential false positives or negatives in racecheck when using

`mbarrier`

with different addresses within a warp.Fixed potential false negatives in

`synccheck`

when using a barrier from different function calls across warps.Fixed an issue on Blackwell where

`--num-cuda-barriers`

would require a larger number than expected to function properly.

### Updates in 2025.2.1[#](https://docs.nvidia.com#updates-in-2025-2-1)

Fixed an issue where using

`cp.async.mbarrier.arrive`

synchronization for`cp.async`

would lead to corruption, crash or invalid results when using racecheck.Fixed potential false positives in memcheck when using a device-side malloc heap size superior to 4GB.


### Updates in 2025.2[#](https://docs.nvidia.com#updates-in-2025-2)

Added public API and memcheck support for all previously unimplemented directions of the PTX

`cp.async.bulk`

and`cp.reduce.async.bulk`

.Added racecheck deadlock detection with the

`--racecheck-deadlock-timeout`

option. See the[racecheck deadlock detection documentation](https://docs.nvidia.com/ComputeSanitizer/index.html#deadlock-detection).Added the

`--racecheck-trace-sync`

option to trace synchronization information in racecheck. See the[racecheck synchronization tracing documentation](https://docs.nvidia.com/ComputeSanitizer/index.html#synclog).Added extra reporting for tensor memory leak detection.

Added support for new vector and sizes configurations for

`ld`

and`st`

on Blackwell.Added

`SANITIZER_INSTRUCTION_CUDA_BARRIER_ATTEMPT`

callback to the patching API for all attempts at waiting on PTX`mbarrier`

.Fixed an issue with mbarrier arrive on transactional barrier in racecheck and synccheck in Hopper+.

Fixed a crash when using

`cudaMallocAsync`

and`cuMemmap`

in the same program with enabled peer-GPU access in memcheck.Fixed issues in racecheck and synccheck when using PTX

`mbarrier`

with different addresses in the same warp.Fixed a potential crash with the error suppression option when using reference files without host backtrace.


### Updates in 2025.1[#](https://docs.nvidia.com#updates-in-2025-1)

Added support for additional Blackwell GPUs.

Modified the way backtraces are displayed: By default, strip paths from files, and avoid displaying frames below main and extra CUDA runtime frames. Added the

`--strip-path`

and`--backtrace-short`

options to control this behavior.Added support for native Python host backtraces.

Added guardrails support for the PTX

`tcgen05`

instructions. See the[Tensor Core MMA guardrails documentation](https://docs.nvidia.com/ComputeSanitizer/index.html#tensor-core-mma-guardrails)for more information.Added reports when encountering user-issued breakpoints.

Added support for OptiX 9.0.

Added Sanitizer API patching support for the PTX

`cp.async.mbarrier.arrive`

asynchronous join operation.Added Sanitizer API patching support for post-release

`syncwarp`

.Fixed a potential false positive in racecheck when using

`cp.async.mbarrier.arrive`

to synchronize memcpy async operations and using the same thread to immediately access the copy destination.Fixed a potential false positive in racecheck when using

`syncwarp`

.Fixed excessive synccheck and racecheck device and host memory consumption in some circumstances with programs initializing PTX

`mbarrier`

in a loop.Fixed potentially wrong block coordinates being displayed in racecheck reports when having multiple clusters.


### Updates in 2024.4[#](https://docs.nvidia.com#updates-in-2024-4)

Added support for the Blackwell architecture.

Added support for Tensor core barriers.

Added public API and memcheck support for the

`st.bulk`

PTX instruction.Added racecheck support for the

`cp.async.bulk`

PTX instruction from global to shared memory.Improved performance of racecheck indirect barrier dependency option and enabled it by default.

Fixed issues where device callbacks would in some cases be called with the wrong threads for a limited set of instructions.

Fixed racecheck and synccheck issues with

`cuda::barrier`

tracking overflow.Fixed racecheck and synccheck issues with cluster barriers.

Fixed memcheck and public API issues when importing memory from other processes and having

`CUDA_VISIBLE_DEVICES`

set.Fixed potential false positives with initcheck when doing 3D memcpy/memset operations.


### Updates in 2024.3[#](https://docs.nvidia.com#updates-in-2024-3)

Fixed potential invalid results on Ampere with synccheck and racecheck relating to

`cuda::barrier`

.`cuda::barrier`

wait events are now called after the wait as completed in the same fashion as Hopper. This may require target applications to be recompiled with a CUDA 12.4 or more recent compiler.Fixed multiple issues with coredump generation that resulted in failures or hangs.

Fixed potential false positives in memcheck with the PTX instruction

`st.async`

on the barrier address.Fixed a potential hang when using per-thread default streams or green contexts and synchronous

`cudaMemcpy`

from device to host.Fixed potential issues with host backtraces on Windows.

Fixed potential false positives misaligned accesses in memcheck with the PTX instruction

`cp.async.bulk`

.

### Updates in 2024.2[#](https://docs.nvidia.com#updates-in-2024-2)

Added public API and memcheck support for PTX cp.async.bulk operations from global to shared memory on Hopper.

Added support for OptiX 8.1.

Dropped support for Linux ppc64le: this platform is no longer supported.

Fixed an issue where memcheck would report misaligned or out of bounds false positives with accesses of a larger size than the actual operation in specific cases.

Fixed potential issues when using Heterogeneous Memory Management.

Fixed potential crashes or false results in racecheck when using clusters on Hopper.

Added a warning when clearing unsupported coredump-related environment variables.

Clarified in documentation when leak errors are reported.


### Updates in 2024.1.1[#](https://docs.nvidia.com#updates-in-2024-1-1)

Fixed an issue where errors would not be reported in libraries called from .NET applications.


### Updates in 2024.1[#](https://docs.nvidia.com#updates-in-2024-1)

Enable shared addressing support by default: removed option

`--hmm-support`

and replaced it with environment variable`NV_COMPUTE_SANITIZER_SHARED_ADDRESSING_SUPPORT`

. See the[environment variables documentation](https://docs.nvidia.com/ComputeSanitizer/index.html#environment-variables)for more information.Changed default value for option

`--target-processes`

to`all`

.Added detection for

`cuda::barrier`

initialization race conditions in racecheck on Hopper.Added support for initcheck API errors suppression.

Added memcheck support for

`cuMemPoolImportPointer`

.Added support for CUDA green contexts.

Added support for CUDA graph device-side node update.

Fixed potential false positives with synccheck when using different

`cuda::barrier`

in a single warp.Fixed potential false negatives with memcheck when using floating point atomics on Hopper.


### Updates in 2023.1.1[#](https://docs.nvidia.com#updates-in-2023-1-1)

Fixed error output for WGMMA instructions.


### Updates in 2023.3[#](https://docs.nvidia.com#updates-in-2023-3)

Added support for Heterogeneous Memory Management (HMM) and Address Translation Service (ATS). The feature is opt-in using the

`--hmm-support`

command-line option.Added racecheck support for device graph launches.

Added the ability to suppress known issues using the

`--suppressions`

command-line option. See the[suppressions documentation](https://docs.nvidia.com/ComputeSanitizer/index.html#error-suppression)for more information.Added support for

[external memory objects](https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__EXTRES__INTEROP.html#group__CUDART__EXTRES__INTEROP). This effectively adds support for Vulkan and D3D12 interop.Added device backtrace support for WSL.

Improve PC offset output. It is now printed next to the function name to clarify it is an assembly offset within that function.

Several command-line options no longer require to explicitly specify “yes” or “no” when they are used.

Renamed the options

`--kernel-regex`

and`--kernel-regex-exclude`

to`--kernel-name`

and`--kernel-name-exclude`

.Added the regex filtering key to

`--kernel-name`

and`--kernel-name-exclude`

.Added new command-line option

`--racecheck-indirect-barrier-dependency`

to enable indirect`cuda::barrier`

tracking in racecheck.Added new command-line option

`--coredump-behavior`

to control the target application behavior after generating a GPU coredump.Added new command-line option

`--detect-missing-module-unload`

to detect missing calls to the`cuModuleUnload`

driver API.Added new command-line option

`--preload-library`

to make the target application load a shared library before the injection libraries.Fix initcheck false positive when memory loads are widened and include padding bytes.

Fix potential hang in racecheck and synccheck tools when the

`bar.arrive`

instruction is used.Added patching API support for the

`setsmemsize`

instruction.Added patching API support for

`__syncthreads()`

after the barrier is released.

### Updates in 2023.2.2[#](https://docs.nvidia.com#updates-in-2023-2-2)

Updated version print output to include build and config information.

Fix potential hang on QNX when capturing the host backtrace.


### Updates in 2023.2.1[#](https://docs.nvidia.com#updates-in-2023-2-1)

Fixed potential racecheck hang on H100 when using thread block clusters.

Compute Sanitizer 2023.2.1 is incorrectly versioned as 2023.2.0 and need to be differentiated by its build ID 33053471.


### Updates in 2023.2[#](https://docs.nvidia.com#updates-in-2023-2)

Added support for CUDA device graph launches.

Added racecheck support for cluster entry and exit race detection for remote shared memory accesses. See the

[cluster entry and exit race detection documentation](https://docs.nvidia.com/ComputeSanitizer/index.html#racecheck-cluster-races)for more information.Added support for CUDA lazy loading when device heap checking is enabled. Requires CUDA driver version 535 or newer.

Added support for tracking child processes launched with

`system()`

or`posix_spawn(p)`

when using`--target-processes all`

.Added support for

`st.async`

and`red.async`

instructions.Improved support for partial warp synchronization using cooperative groups in racecheck.

Improved support for

`cuda::barrier::wait()`

on SM 9.x.Added coredump support for Pascal architecture and multi-context applications.

Added support for OptiX 8.0.

Improved performance when using initcheck in OptiX applications in some cases. Using initcheck to track OptiX applications now requires the option

`--check-optix yes`

.

### Updates in 2023.1.1[#](https://docs.nvidia.com#id2)

Fixed bug where memcheck would report out-of-bound accesses when loading user parameter values using a ternary operator.

Fixed potential crash when using leakcheck with applications using CUBLAS.

Fixed potential false positives when using synccheck or racecheck with applications using CUDA barriers.


### Updates in 2023.1[#](https://docs.nvidia.com#updates-in-2023-1)

Added racecheck support for distributed shared memory.

Extended stream-ordered race detection to

`cudaMemcpy`

APIs.Added memcheck, synccheck and patching API support for warpgroup operations.

Added

`--coredump-name`

CLI option to set the coredump file name.Added support for Unicode file paths.

Added support for OptiX 7.7.


### Updates in 2022.4.1[#](https://docs.nvidia.com#updates-in-2022-4-1)

Fixed bug where synccheck would incorrectly report illegal instructions for code using

`cluster.sync()`

and compiled with`--device-debug`

Fixed incorrect address reports in SanitizerCallbackMemcpyAsync in some specific cases, leading to potential invalid results in memcheck and racecheck.

Fixed potential hangs and invalid results with racecheck on OptiX applications.

Fixed potential crash or invalid results when using CUDA Lazy Module Loading with memcheck or initcheck if

`--check-device-heap`

is enabled. Lazy Module Loading will be automatically disabled in these cases.

### Updates in 2022.4[#](https://docs.nvidia.com#updates-in-2022-4)

Added support for

`__nv_aligned_device_malloc`

.Added support for

`ldmatrix`

and`stmatrix`

instructions.Added support for cache control operations when using the

`--check-cache-control`

command-line option.Added new command-line option

`--unused-memory-threshold`

to control the threshold for unused memory reports.Improved support for CUDA pipeline memcpy-async related hazards in racecheck.


### Updates in 2022.3[#](https://docs.nvidia.com#updates-in-2022-3)

Added support for the NVIDIA GH100/SM 9.x GPU architecture.

Added support for the NVIDIA AD10x/SM 8.9 GPU architecture.

Added support for lazy kernel loading.

Added memcheck support for distributed shared memory.

Added new options

`--num-callers-device`

and`--num-callers-host`

to control the number of callers to print in stack traces.Added support for OptiX 7.6 applications.

Fix bug on Linux ppc64le where the host stack trace was incomplete.


### Updates in 2022.2.1[#](https://docs.nvidia.com#updates-in-2022-2-1)

Fixed incorrect device backtrace for applications compiled with

`-lineinfo`

.

### Updates in 2022.2[#](https://docs.nvidia.com#updates-in-2022-2)

Added memcheck support for use-before-alloc and use-after-free race detection. See the

[stream-ordered race detection documentation](https://docs.nvidia.com/ComputeSanitizer/index.html#stream-ordered-races)for more information.Added leakcheck support for asynchronous allocations, OptiX resources and CUDA memmap (on Linux only for the latter).

Added option to ignore

`CUDA_ERROR_NOT_FOUND`

error codes returned by the`cuGetProcAddress`

API.Added new sanitizer API functions to allocate and free page-locked host memory.

Added sanitizer API callbacks for the

[event management](https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__EVENT.html)API.

### Updates in 2022.1.1[#](https://docs.nvidia.com#updates-in-2022-1-1)

Fixed initcheck issue where the tool would incorrectly abort a CUDA kernel launch after reporting an uninitialized access on Windows with hardware scheduling enabled.


### Updates in 2022.1[#](https://docs.nvidia.com#updates-in-2022-1)

Added support for generating coredumps.

Improved support for stack overflow detection.

Added new option

`--target-processes-filter`

to filter the processes being tracked by name.Added initcheck support for asynchronous allocations. Requires CUDA driver version 510 or newer.

Added initcheck support for accesses on peer devices. Requires CUDA driver version 510 or newer.

Added support for OptiX 7 applications.

Added support for tracking the child processes of 32-bit processes in multi-process applications on Linux and Windows x86_64.


### Updates in 2021.3.1[#](https://docs.nvidia.com#updates-in-2021-3-1)

Fixed intermittent issue on vGPU where synccheck would incorrectly detect divergent threads.

Fixed potential hang when tracking several graph launches.


### Updates in 2021.3[#](https://docs.nvidia.com#updates-in-2021-3)

Improved Linux host backtrace.

Removed requirement to call

`cudaDeviceReset()`

for accurate reporting of memory leaks and unused memory features.Fixed synccheck potential hang when calling

`__syncthreads`

in divergent code paths on Volta GPUs or newer.Added print of nearest allocation information for memcheck precise errors in global memory.

Added warning when calling device-side

`malloc`

with an empty size.Added separate sanitizer API device callback for

`cuda::memcpy_async`

.Added new command-line option

`--num-cuda-barriers`

to override the expected number of`cuda::barrier`

used by the target application.Added new command-line options

`--print-session-details`

to print session information and`--save-session-details`

to save it to the output file.Added support for WSL2.


### Updates in 2021.2.3[#](https://docs.nvidia.com#updates-in-2021-2-3)

Enabled SLS hardening and branch protection for L4T builds.


### Updates in 2021.2.2[#](https://docs.nvidia.com#updates-in-2021-2-2)

Enabled stack canaries with random canary values for L4T builds.


### Updates in 2021.2.1[#](https://docs.nvidia.com#updates-in-2021-2-1)

Added device backtrace for malloc/free errors in CUDA kernels.

Improved racecheck host memory footprint.


### Updates in 2021.2[#](https://docs.nvidia.com#updates-in-2021-2)

Added racecheck and synccheck support for

`cuda::barrier`

on Ampere GPUs or newer.Added racecheck support for

`__syncwarp`

with partial mask.Added

`--launch-count`

and`--launch-skip`

filtering options. See the[Command Line Options documentation](https://docs.nvidia.com/ComputeSanitizer/index.html#command-line-options)for more information.`--filter`

and`--exclude`

options have been respectively renamed to`--kernel-regex`

and`--kernel-regex-exclude`

.Added support for QNX and Linux aarch64 platforms.

Added support for CUDA graphs memory nodes.


### Updates in 2021.1.1[#](https://docs.nvidia.com#updates-in-2021-1-1)

Fixed an issue where incorrect line numbers could be shown in errors reports.


### Updates in 2021.1[#](https://docs.nvidia.com#updates-in-2021-1)

Added support for allocation padding via the

`--padding`

option.Added experimental support for NVTX memory API using option

`--nvtx yes`

. Please refer to[NVTX API for Compute Sanitizer Reference Manual](https://docs.nvidia.com/SanitizerNvtxGuide/index.html#about-nvtx)for more information.

### Updates in 2020.3.1[#](https://docs.nvidia.com#updates-in-2020-3-1)

Fixed issue when launching a CUDA graph multiple times.

Fixed false positives when using cooperative groups synchronization primitives with initcheck and synccheck.


### Updates in 2020.3[#](https://docs.nvidia.com#updates-in-2020-3)

Added support for CUDA memory pools and CUDA API reduced serialization.

Added host backtrace for unused memory reports.


### Updates in 2020.2.1[#](https://docs.nvidia.com#updates-in-2020-2-1)

Fixed crash when loading cubins of size larger than 2 GiB.

Fixed error detection on systems with multiple GPUs.

Fixed issue when using CUDA Virtual Memory Management API

`cuMemSetAccess`

to remove access to a subset of devices on a system with multiple GPUs.Added sanitizer API to translate between sanitizer and CUDA stream handles.


### Updates in 2020.2[#](https://docs.nvidia.com#updates-in-2020-2)

Added support for CUDA graphs and CUDA memmap APIs.

The memory access callback of the sanitizer API has been split into three distinct callbacks corresponding to global, shared and local memory accesses.


### Updates in 2020.1.2[#](https://docs.nvidia.com#updates-in-2020-1-2)

Added sanitizer stream API. This fixes tool crashes when per-thread streams are being used.


### Updates in 2020.1.1[#](https://docs.nvidia.com#updates-in-2020-1-1)

Added support for Windows Hardware-accelerated GPU scheduling

Added support for tracking child processes spawned by the application launched under the tool via the

`--target-processes`

CLI option.

### Updates in 2020.1[#](https://docs.nvidia.com#updates-in-2020-1)

Initial release of the Compute Sanitizer (with CUDA 11.0)


Updates to the Sanitizer API :

Added support for per-thread streams

Added APIs to retrieve the PC and size of a CUDA function or patch

Added callback for

`cudaStreamAttachMemAsync`

Added direction to memcpy callback data

Added stream to memcpy and memset callbacks data

Added launch callback after syscall setup

Added visibility field to allocation callback data

Added PC argument to block entry callback

Added incoming value to memory access callbacks

Added threadCount to barrier callbacks

Added cooperative group flags for barrier and function callbacks


### Updates in 2019.1[#](https://docs.nvidia.com#updates-in-2019-1)

Initial release of the Compute Sanitizer API (with CUDA 10.1)


## Known Limitations[#](https://docs.nvidia.com#known-limitations)

Applications run much slower under the Compute Sanitizer tools. This may cause some kernel launches to fail with a launch timeout error when running with the Compute Sanitizer enabled.

Compute Sanitizer does not support checking host-side memory access violations and leaks for accesses made outside of CUDA API calls (e.g. accessing a buffer from the CPU).

Compute Sanitizer tools do not support coredumps on WSL2.

The memcheck tool does not support CUDA API error checking for API calls made on the GPU using dynamic parallelism.

The racecheck, synccheck and initcheck tools do not support CUDA dynamic parallelism.

CUDA dynamic parallelism is not supported when Windows Hardware-accelerated GPU scheduling is enabled.

Compute Sanitizer tools cannot interoperate with other CUDA developer tools. This includes CUDA coredumps which are automatically disabled by the Compute Sanitizer. They can be enabled instead by using the

`--generate-coredump`

option.The initcheck tool does not support IPC allocations. Using it will result in false positives.

Compute Sanitizer tools are not supported when SLI is enabled.

The racecheck tool is not supported under Confidential Computing.

The memcheck tool does not detect out-of-bounds accesses into the reserved shared memory region. For more information on reserved shared memory, refer to the

[Special Registers Reserved for Shared Memory](https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#special-registers-reserved-smem)section of the PTX documentation.Some

`tensormap`

and`tcgen05`

instructions accessing global memory are not currently supported, which may result in initcheck false positives.When using memcheck with compile-time patching (

`-fdevice-sanitize=memcheck`

), overflow errors between different shared memory variables within the same allocation are not detected.When using memcheck with compile-time patching (

`-fdevice-sanitize=memcheck`

), function-level hybrid instrumentation is not supported. When a module contains both instrumented and non-instrumented functions, functions that are not instrumented by the compiler will not be binary instrumented. To ensure full coverage, compile all functions in a module with`-fdevice-sanitize=memcheck`

.When using memcheck with compile-time patching (

`-fdevice-sanitize=memcheck`

), Heterogeneous Memory Management (HMM) is not supported. Using it will result in false positives.When using memcheck with compile-time patching (

`-fdevice-sanitize=memcheck`

), the resource usage of a kernel may change, which can lead to the error: “RuntimeError: CUDA error: too many resources requested for launch”. To validate resource usage and maintain forward compatibility, the`__launch_bounds__()`

qualifier can be used as described in the[CUDA C Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html?highlight=launch%2520bound#launch-bounds).

## Known Issues[#](https://docs.nvidia.com#known-issues)

When using a driver version between 615.00 and 615.70 on Linux or 616.65 on Windows, and running

`compute-sanitizer`

on an application compiled with a toolkit older than CUDA 13.4, the following error may be reported:`CUDA API Error: Fabric handle support is dependent on IMEX channels`

.On QNX, the host backtrace may not be displayed correctly. Proper line information can be retrieved using

`addr2line`

with the offsets provided in the brackets.On L4T, error reports may be duplicated. In some cases some malformed reports may also appear after reporting the originally found error.

The

`--fdevice-sanitize=memcheck`

nvcc option does not apply compile-time patching for memcheck to JIT-compiled programs. To enable memcheck with compile-time patching in a JIT-compiled program, use the`-Xptxas=-sanitize=memcheck`

option instead.When using memcheck with compile-time patching (

`-fdevice-sanitize=memcheck`

), shared memory accesses when using clusters are not currently supported. Using this feature will result in false positives.When using memcheck with compile-time patching (

`-fdevice-sanitize=memcheck`

), use of the sink operator (`_`

) in`ld`

or`stg`

PTX instructions is not currently supported and may result in false positives.The synccheck tool may incorrectly emit divergence in block errors in applications compiled with the 13.0 CUDA toolkit using cooperative group synchronizations.

The racecheck tool may print incorrect data for “Current value” when reporting a hazard on a shared memory location where the last access was an atomic operation. This can also impact the severity of this hazard.

On QNX, when using the

`--target-processes all`

option, analyzing shell scripts may hang after the script has completed. End the application using Ctrl-C on the command line in that case.The initcheck tool might report false positives for device-to-host cudaMemcpy operations on padded structs that were initialized by a CUDA kernel. The

`#pragma pack`

directive can be used to disable the padding as a workaround.When a hardware exception occur during a kernel launch that was skipped due to the usage of the

`kernel-name`

,`kernel-name-exclude`

,`launch-count`

or`launch-skip`

options, the memcheck tool will not be able to report additional details as an imprecise error.

## Support[#](https://docs.nvidia.com#support)

Information on supported platforms and GPUs.

### Platform Support[#](https://docs.nvidia.com#platform-support)

Platform |
Support |
|---|---|
Windows (x86_64) |
Yes |
Windows (ARM64) |
Yes |
Linux (x86_64) |
Yes |
Linux (ppc64le) |
No |
Linux (aarch64sbsa) |
Yes |
Linux (aarch64) |
Yes |
QNX |
Yes |
MacOSX |
No |

### GPU Support[#](https://docs.nvidia.com#gpu-support)

The compute-sanitizer tools are supported on all CUDA capable GPUs with SM versions 7.5 and above.

Notices

Notice

ALL NVIDIA DESIGN SPECIFICATIONS, REFERENCE BOARDS, FILES, DRAWINGS, DIAGNOSTICS, LISTS, AND OTHER DOCUMENTS (TOGETHER AND SEPARATELY, “MATERIALS”) ARE BEING PROVIDED “AS IS.” NVIDIA MAKES NO WARRANTIES, EXPRESSED, IMPLIED, STATUTORY, OR OTHERWISE WITH RESPECT TO THE MATERIALS, AND EXPRESSLY DISCLAIMS ALL IMPLIED WARRANTIES OF NONINFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A PARTICULAR PURPOSE.

Information furnished is believed to be accurate and reliable. However, NVIDIA Corporation assumes no responsibility for the consequences of use of such information or for any infringement of patents or other rights of third parties that may result from its use. No license is granted by implication of otherwise under any patent rights of NVIDIA Corporation. Specifications mentioned in this publication are subject to change without notice. This publication supersedes and replaces all other information previously supplied. NVIDIA Corporation products are not authorized as critical components in life support devices or systems without express written approval of NVIDIA Corporation.

Trademarks

NVIDIA and the NVIDIA logo are trademarks and/or registered trademarks of NVIDIA Corporation in the United States and other countries. Other company and product names may be trademarks of the respective companies with which they are associated.