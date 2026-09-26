source: https://docs.nvidia.com/cuda/cuda-debugger-api/release-notes.html

# Release Notes[](https://docs.nvidia.com#release-notes)

## CUDA 13.4 Release[](https://docs.nvidia.com#cuda-13-4-release)

### Deprecated APIs[](https://docs.nvidia.com#deprecated-apis)

CUDBG_EVENT_KERNEL_READY and CUDBG_EVENT_KERNEL_FINISHED are deprecated because they are not reliable and can’t be sent for all kernel executions.

kernelReady_st, kernelFinished_st and their legacy versions are deprecated.


### Dropped APIs[](https://docs.nvidia.com#dropped-apis)

parentGridId is no longer exposed. To keep ABI compatibility, it has been replaced with reserved0 in kernelReady_st, CUDBGGridInfo and their legacy versions.


## CUDA 13.3 Release[](https://docs.nvidia.com#cuda-13-3-release)

### New APIs[](https://docs.nvidia.com#new-apis)

CUDBG_EXCEPTION_TMA_SYSCALL: Report TMA syscall errors.

CUDBG_COREDUMP_FAULTED_CONTEXTS_ONLY: Include only faulted contexts in CUDA core dumps.


## CUDA 13.2 Release[](https://docs.nvidia.com#cuda-13-2-release)

### Major changes[](https://docs.nvidia.com#major-changes)

Added handle-based breakpoint management.

Added coordinated multi-device suspension and resumption.

Added non-blocking single-step support.


### New APIs[](https://docs.nvidia.com#id1)

insertBreakpoint(), removeBreakpoint(), enableBreakpoint(), disableBreakpoint(), isBreakpointEnabled(), getWarpHitBreakpoint(): Manage and query breakpoints using CUDBGBreakpointHandle.

CUDBG_DEBUGGER_CAPABILITY_BREAK_ON_LAUNCH: Enable break on launch.

resumeWarpsUntilPC(): Add a flags parameter, including non-blocking operation with CUDBG_SINGLE_STEP_FLAGS_NON_BLOCKING.

CUDBG_EVENT_SINGLE_STEP_COMPLETE: Report completion of non-blocking stepping.

suspendAllDevices(), resumeAllDevices(): Suspend or resume all CUDA devices.

readRegisterRange(): Add an optional numRegistersRead output parameter that reports the number of registers read.


### Deprecated APIs[](https://docs.nvidia.com#id2)

resumeWarpsUntilPC60(); use resumeWarpsUntilPC() instead.

readRegisterRange60(); use readRegisterRange() instead.


## CUDA 13.1 Release[](https://docs.nvidia.com#cuda-13-1-release)

### Major changes[](https://docs.nvidia.com#id3)

Removed memcheck-specific exceptions and CUDBG_ERROR_MEMCHECK_NOT_ENABLED, reserving their values for ABI compatibility.

Added hardware barrier, warp and cluster exception reporting, gzip core dumps, and file-descriptor-based debugger attach.


### New APIs[](https://docs.nvidia.com#id4)

getHardwareBarrierInfo(): Get hardware barrier information for a thread.

CUDBG_INITIATE_DEBUGGER_ATTACH_PROCEDURE_FD, CUDBG_REPORT_ATTACH_PROCEDURE_FINISHED: Initiate debugger attach through a file descriptor and report completion.

CUDBG_DEBUGGER_CAPABILITY_FLUSH_PRINTF_ON_SUSPEND: Flush CUDA printf output when a device is suspended.

CUDBG_COREDUMP_GZIP_COMPRESS: Compress CUDA core dumps with gzip.

CudbgWarpTableEntry::barrierScope, CudbgWarpTableEntry::additionalBarrierInfo (cudacoredump.h): Record hardware barrier information in core dumps.


### Deprecated APIs[](https://docs.nvidia.com#id5)

readCCRegister()

writeCCRegister()


### Dropped APIs[](https://docs.nvidia.com#id6)

cudbgMain(); use CUDBG_PRE_INIT instead.

CUDBG_DETACH_SUSPENDED_DEVICES_MASK, CUDBG_ENABLE_INTEGRATED_MEMCHECK, and CUDBG_ENABLE_PREEMPTION_DEBUGGING


## CUDA 13.0 Release[](https://docs.nvidia.com#cuda-13-0-release)

### Major changes[](https://docs.nvidia.com#id7)

Removed support for Maxwell, Pascal and Volta architectures.

Removed support for CUDA_ENABLE_LIGHTWEIGHT_COREDUMP.

Reduced CPU call stack collection overhead and disabled it by default.

Bugfixes and performance improvements.


### New APIs[](https://docs.nvidia.com#id8)

The following APIs were added in this release. Please refer to the Modules documentation for more details about the new methods.

- getCudaExceptionString(uint32_t dev, uint32_t sm, uint32_t wp, uint32_t ln, char *buf, uint32_t bufSz, uint32_t *msgSz)
-
Get error string for CUDA Exceptions.

- setNotifyNewEventCallback(CUDBGNotifyNewEventCallback callback, void* userData)
-
Provides the API with the function to call to notify the debugger of a new application or device event.

- CUDBG_DEBUGGER_CAPABILITY_COLLECT_CPU_CALL_STACK_FOR_KERNEL_LAUNCHES
-
New capability to collect CPU call stack for kernel launches. The readCPUCallStack cann only be used when this capability is enabled.


### Deprecated APIs[](https://docs.nvidia.com#id9)

readConstMemory(uint32_t dev, uint64_t addr, void *buf, uint32_t sz)


## CUDA 12.9 Release[](https://docs.nvidia.com#cuda-12-9-release)

### Major changes[](https://docs.nvidia.com#major-changes-1)

Suport late attach on WSL.

Bugfixes and performance improvements.


### New APIs[](https://docs.nvidia.com#new-apis-1)

The following APIs were added in this release. Please refer to the Modules documentation for more details about the new methods.

- getCbuWarpState(uint32_t dev, uint32_t sm, uint64_t warpMask, CUDBGCbuWarpState* warpStates, uint32_t numWarpStates)
-
Gets CBU state of a given warp.

- consumeCudaLogs(CUDBGCudaLogMessage* logMessages, uint32_t numMessages, uint32_t* numConsumed)
-
Get CUDA error log entries. This consumes the log entries, so they will not be available in subsequent calls.

- readCPUCallStack(uint32_t dev, uint64_t gridId64, uint64_t *addrs, uint32_t numAddrs, uint32_t* totalNumAddrs)
-
Read CPU call stack captured at the time of kernel launch.


### Updated APIs[](https://docs.nvidia.com#updated-apis)

The following APIs were updated in this release. Please refer to the method documentation for the details. The old code, compiled for the older versions of the API will still work.

readWarpState(uint32_t dev, uint32_t sm, uint32_t wp, CUDBGWarpState *state)


## CUDA 12.8 Release[](https://docs.nvidia.com#cuda-12-8-release)

### Major changes[](https://docs.nvidia.com#major-changes-2)

Support late attach on Jetson targets.

Bugfixes and performance improvements.


### New APIs[](https://docs.nvidia.com#new-apis-2)

The following APIs were added in this release. Please refer to the Modules documentation for more details about the new methods.

- readWarpResources(uint32_t dev, uint32_t sm, uint32_t wp, CUDBGWarpResources *resources)
-
Get the resources assigned to a given warp.


## CUDA 12.7 Release[](https://docs.nvidia.com#cuda-12-7-release)

### Major changes[](https://docs.nvidia.com#major-changes-3)

Bugfixes and performance improvements.


### New APIs[](https://docs.nvidia.com#new-apis-3)

The following APIs were added in this release. Please refer to the Modules documentation for more details about the new methods.

- getClusterExceptionTargetBlock(uint32_t dev, uint32_t sm, uint32_t wp, CuDim3 *blockIdx, bool *blockIdxValid)
-
Retrieves the target block index and validity status for a given device, streaming multiprocessor, and warp for cluster exceptions.


### Updated APIs[](https://docs.nvidia.com#updated-apis-1)

The following APIs were updated in this release. Please refer to the method documentation for the details. The old code, compiled for the older versions of the API will still work.

getGridInfo(uint32_t dev, uint64_t gridId64, CUDBGGridInfo *gridInfo)

getClusterDim(uint32_t dev, uint32_t sm, uint32_t wp, CuDim3 *clusterDim)

readWarpState(uint32_t dev, uint32_t sm, uint32_t wp, CUDBGWarpState *state)


## CUDA 12.6 Release[](https://docs.nvidia.com#cuda-12-6-release)

### Major changes[](https://docs.nvidia.com#major-changes-4)

Reduced overhead for batch breakpoint updates.

Moved constbank memory dump control to a separate flag.

Bugfixes and performance improvements.


### New APIs[](https://docs.nvidia.com#new-apis-4)

- CUDBG_COREDUMP_SKIP_CONSTBANK_MEMORY flag for coredump generation (generateCoredump).
-
In the previous API versions the CUDBG_COREDUMP_SKIP_GLOBAL_MEMORY controlled both the global and the constant memory. Since CUDA 12.6 the constbank memory is controlled by a separate flag (the constbank memory is usually smaller than global memory, so it is feasible to dump it by default even if the global memory is skipped).


## CUDA 12.5 Release[](https://docs.nvidia.com#cuda-12-5-release)

### Major changes[](https://docs.nvidia.com#major-changes-5)

Significant performance improvements for memory accessing operations and stepping.

Bugfixes and stability improvements.


### New APIs[](https://docs.nvidia.com#new-apis-5)

The following APIs were added in this release. Please refer to the Modules documentation for more details about the new methods.

- readAllVirtualReturnAddresses(uint32_t dev, uint32_t sm, uint32_t wp, uint32_t ln, uint64_t *addrs, uint32_t numAddrs, uint32_t* callDepth, uint32_t* syscallCallDepth)
-
Reads all the virtual return addresses.

- getSupportedDebuggerCapabilities(CUDBGCapabilityFlags* capabilities)
-
Returns debugger capabilities that are supported by this version of the API.

- readSmException(uint32_t dev, uint32_t sm, CUDBGException_t *exception, uint64_t *errorPC, bool *errorPCValid)
-
Get the SM exception status if it exists.


### Deprecated APIs[](https://docs.nvidia.com#deprecated-apis-1)

- CUDBG_COREDUMP_SKIP_ABORT
-
The generateCoredump API no longer accepts the CUDBG_COREDUMP_SKIP_ABORT flag. Note that this flag was ignored in the previous versions of the API.


## CUDA 12.4 Release[](https://docs.nvidia.com#cuda-12-4-release)

### Major changes[](https://docs.nvidia.com#major-changes-6)

Made CUDA ELF file handling more robust and performant.

Bugfixes and performance improvements.


### New APIs[](https://docs.nvidia.com#new-apis-6)

The following APIs were added in this release. Please refer to the Modules documentation for more details about the new methods.

- getDeviceInfoSizes(uint32_t dev, CUDBGDeviceInfoSizes* sizes)
-
Returns sizes for device info structs and defined attributes.

- getDeviceInfo(uint32_t dev, CUDBGDeviceInfoQueryType_t type, void *buffer, uint32_t length, uint32_t *dataLength)
-
Returns full or changed device info.


### Updated APIs[](https://docs.nvidia.com#updated-apis-2)

The following APIs were updated in this release. Please refer to the method documentation for the details. The old code, compiled for the older versions of the API will still work.

getConstBankAddress(uint32_t dev, uint64_t gridId64, uint32_t bank, uint64_t* address, uint32_t* size)

singleStepWarp(uint32_t dev, uint32_t sm, uint32_t wp, uint32_t laneHint, uint32_t nsteps, uint32_t flags, uint64_t *warpMask)


## CUDA 12.3 Release[](https://docs.nvidia.com#cuda-12-3-release)

### Major changes[](https://docs.nvidia.com#major-changes-7)

Support generating coredumps after the debugger has attached.

Bugfixes and performance improvements.


### New APIs[](https://docs.nvidia.com#new-apis-7)

- getConstBankAddress(uint32_t dev, uint32_t sm, uint32_t wp, uint32_t bank, uint32_t offset, uint64_t* address)
-
Returns sizes for device info structs and defined attributes.

- generateCoredump(const char* filename, CUDBGCoredumpGenerationFlags flags)
-
Generates a coredump for the current GPU state.


### Updated APIs[](https://docs.nvidia.com#updated-apis-3)

The following APIs were updated in this release. Please refer to the method documentation for the details. The old code, compiled for the older versions of the API will still work.

getLoadedFunctionInfo(uint32_t devId, uint64_t handle, CUDBGLoadedFunctionInfo *info, uint32_t startIndex, uint32_t numEntries)


### Deprecated APIs[](https://docs.nvidia.com#deprecated-apis-2)

- disassemble() deprecation notice
-
The disassemble() API function is deprecated. It will be dropped in an upcoming release. API consumers should use the nvdisasm utility instead.


## CUDA 12.2 Release[](https://docs.nvidia.com#cuda-12-2-release)

### Major changes[](https://docs.nvidia.com#major-changes-8)

Switch to the new debugger back-end (Unified Debugger) on WSL.

Switch to the new debugger back-end (Unified Debugger) on Jetson.

Bugfixes and performance improvements.


### New APIs[](https://docs.nvidia.com#new-apis-8)

The following APIs were added in this release. Please refer to the Modules documentation for more details about the new methods.

- getErrorStringEx(char *buf, uint32_t bufSz, uint32_t *msgSz)
-
Fills a user-provided buffer with an error message encoded as a null-terminated ASCII string. The error message is specific to the last failed API call and is invalidated after every API call.


## CUDA 12.1 Release[](https://docs.nvidia.com#cuda-12-1-release)

### Major changes[](https://docs.nvidia.com#major-changes-9)

Improved support for single stepping.

Bugfixes and performance improvements.


## CUDA 12.0 Release[](https://docs.nvidia.com#cuda-12-0-release)

### Major changes[](https://docs.nvidia.com#major-changes-10)

Debugging support for application using CUDA Dynamic Parallelism V2.

Improved support for latest GPU architectures.

Bugfixes and performance improvements.


### New APIs[](https://docs.nvidia.com#new-apis-9)

The following APIs were added in this release. Please refer to the Modules documentation for more details about the new methods.

- getClusterDim(uint32_t dev, uint64_t gridId64, CuDim3 *clusterDim)
-
Get the number of blocks in the given cluster.

- readClusterIdx(uint32_t dev, uint32_t sm, uint32_t wp, CuDim3 *clusterIdx)
-
Get the number of blocks in the given cluster.


### Updated APIs[](https://docs.nvidia.com#updated-apis-4)

The following APIs were updated in this release. Please refer to the method documentation for the details. The old code, compiled for the older versions of the API will still work.

getGridInfo(uint32_t dev, uint64_t gridId64, CUDBGGridInfo *gridInfo)

readWarpState(uint32_t dev, uint32_t sm, uint32_t wp, CUDBGWarpState *state)


## CUDA 11.8 Release[](https://docs.nvidia.com#cuda-11-8-release)

- New Unified Debugger backend
-
A new debugger backend named the Unified Debugger (UD) has been introduced on Linux platforms with this release. UD is supported across multiple platforms including both Windows and Linux. The UD should mostly be transparent to existing clients of the API. The previous debugger backend, known as the classic debugger backend, can still be used by setting the environment variable CUDBG_USE_LEGACY_DEBUGGER to 1. UD is not supported on Maxwell GPUs. The clients of the API shall switch to the classic backend if Maxwell support is required.

- Device side cudaDeviceSynchronize() undefined behavior
-
The clients of the API shall prevent the use of SingleStepWarp in the deprecated cudaDeviceSynchronize() function. Instead, revert to stepping over the call with a BP set and resume.

- CUDBG_EVENT_KERNEL_READY events are no longer delivered for GPU-launched grids
-
CUDBG_EVENT_KERNEL_READY events for GPU-launched grids that were delivered over the ASYNC event pipe will no longer be sent. GPU-launched here refers to codes making use of CUDA Dynamic Parallelism. The existing implementation for this use case was imprecise. The callback did not report all GPU-launched grids before execution has begun, only those found on the deivce currently executing that were not previously reported during their launch. This functionality may be reintroduced in a future release. If this functionality is strictly required, the classic debugger backend can be used.

- getLoadedFunctionInfo
-
Added a new getLoadedFunctionInfo call to obtain the section number and address of loaded functions for a given module.


## CUDA 7.0 Release[](https://docs.nvidia.com#cuda-7-0-release)

Stability improvements. No API additions or changes.

## CUDA 6.5 Release[](https://docs.nvidia.com#cuda-6-5-release)

- Predicate registers
-
The per-thread predicate registers can be accessed and modified via the readPredicates() and writePredicates() calls. Each of these calls expects a buffer of sufficient size to cover all predicates for the current GPU architecture. The number of current predicate registers can be read back via the getNumPredicates() API call.

- Condition code register
-
The per-thread condition code register can be accessed and modified via the readCCRegister() and writeCCRegister() calls. The condition code register is a unsigned 32-bit register, whose format may vary by GPU architecture.

- Device Name
-
The getDeviceName() API returns a string containing the publically exposed product name of the GPU.

- API Error Reporting Improvement
-
The symbol CUDBG_REPORT_DRIVER_API_ERROR_FLAGS points to an unsigned 32-bit integer in the application’s process space that controls API error reporting. The values that can be written into this flag are specified in the CUDBGReportDriverApiErrorFlags enum. In 6.5, setting the bit corresponding to CUDBG_REPORT_DRIVER_API_ERROR_FLAGS_SUPPRESS_NOT_READY in the variable CUDBG_REPORT_DRIVER_API_ERROR_FLAGS is supported. This will prevent CUDA API calls that return the runtime API error code cudaErrorNotReady or the driver API error code cuErrorNotReady from executing the CUDA API error reporting function.