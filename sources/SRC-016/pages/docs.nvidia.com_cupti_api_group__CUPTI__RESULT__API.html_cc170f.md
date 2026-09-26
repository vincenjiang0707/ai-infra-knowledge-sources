source: https://docs.nvidia.com/cupti/api/group__CUPTI__RESULT__API.html

# 6.11. CUPTI Result Codes[#](https://docs.nvidia.com#cupti-result-codes)

Error and result codes returned by CUPTI functions.

## 6.11.1. Enumerations[#](https://docs.nvidia.com#enumerations)

[CUptiResult](https://docs.nvidia.com#group__cupti__result__api_1ga8c54bf95108e67d858f37fcf76c88714)CUPTI result codes.


## 6.11.2. Functions[#](https://docs.nvidia.com#functions)

- CUptiResult
[cuptiGetErrorMessage](https://docs.nvidia.com#group__cupti__result__api_1ga457c9a7058749ae118bd2247d9722041)(CUptiResult result, const char **str) Get the descriptive message corresponding to error codes returned by CUPTI.

- CUptiResult
[cuptiGetResultString](https://docs.nvidia.com#group__cupti__result__api_1ga6d5275dd8f127592c1fe3033bb73a751)(CUptiResult result, const char **str) Get the descriptive string for a CUptiResult.


## 6.11.3. Enumerations[#](https://docs.nvidia.com#id1)

-
enum CUptiResult
[#](https://docs.nvidia.com#_CPPv411CUptiResult) CUPTI result codes.

Error and result codes returned by CUPTI functions.

*Values:*-
enumerator CUPTI_SUCCESS
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult13CUPTI_SUCCESSE) No error.


-
enumerator CUPTI_ERROR_INVALID_PARAMETER
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult29CUPTI_ERROR_INVALID_PARAMETERE) One or more of the parameters is invalid.


-
enumerator CUPTI_ERROR_INVALID_DEVICE
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult26CUPTI_ERROR_INVALID_DEVICEE) The device does not correspond to a valid CUDA device.


-
enumerator CUPTI_ERROR_INVALID_CONTEXT
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult27CUPTI_ERROR_INVALID_CONTEXTE) The context is NULL or not valid.


-
enumerator CUPTI_ERROR_INVALID_EVENT_DOMAIN_ID
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult35CUPTI_ERROR_INVALID_EVENT_DOMAIN_IDE) The event domain id is invalid.


-
enumerator CUPTI_ERROR_INVALID_EVENT_ID
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult28CUPTI_ERROR_INVALID_EVENT_IDE) The event id is invalid.


-
enumerator CUPTI_ERROR_INVALID_EVENT_NAME
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult30CUPTI_ERROR_INVALID_EVENT_NAMEE) The event name is invalid.


-
enumerator CUPTI_ERROR_INVALID_OPERATION
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult29CUPTI_ERROR_INVALID_OPERATIONE) The current operation cannot be performed due to dependency on other factors.


-
enumerator CUPTI_ERROR_OUT_OF_MEMORY
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult25CUPTI_ERROR_OUT_OF_MEMORYE) Unable to allocate enough memory to perform the requested operation.


-
enumerator CUPTI_ERROR_HARDWARE
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult20CUPTI_ERROR_HARDWAREE) An error occurred on the performance monitoring hardware.


-
enumerator CUPTI_ERROR_PARAMETER_SIZE_NOT_SUFFICIENT
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult41CUPTI_ERROR_PARAMETER_SIZE_NOT_SUFFICIENTE) The output buffer size is not sufficient to return all requested data.


-
enumerator CUPTI_ERROR_API_NOT_IMPLEMENTED
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult31CUPTI_ERROR_API_NOT_IMPLEMENTEDE) API is not implemented.


-
enumerator CUPTI_ERROR_MAX_LIMIT_REACHED
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult29CUPTI_ERROR_MAX_LIMIT_REACHEDE) The maximum limit is reached.


-
enumerator CUPTI_ERROR_NOT_READY
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult21CUPTI_ERROR_NOT_READYE) The object is not yet ready to perform the requested operation.


-
enumerator CUPTI_ERROR_NOT_COMPATIBLE
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult26CUPTI_ERROR_NOT_COMPATIBLEE) The current operation is not compatible with the current state of the object.


-
enumerator CUPTI_ERROR_NOT_INITIALIZED
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult27CUPTI_ERROR_NOT_INITIALIZEDE) CUPTI is unable to initialize its connection to the CUDA driver.

When returned from the profiling APIs (such as cuptiProfilerInitialize or cuptiProfilerHostInitialize), it may also indicate that CUPTI could not dynamically load the nvperf* libraries; ensure libnvperf_host.so and libnvperf_target.so, which ship alongside libcupti.so, are discoverable by the dynamic linker.


-
enumerator CUPTI_ERROR_INVALID_METRIC_ID
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult29CUPTI_ERROR_INVALID_METRIC_IDE) The metric id is invalid.


-
enumerator CUPTI_ERROR_INVALID_METRIC_NAME
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult31CUPTI_ERROR_INVALID_METRIC_NAMEE) The metric name is invalid.


-
enumerator CUPTI_ERROR_QUEUE_EMPTY
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult23CUPTI_ERROR_QUEUE_EMPTYE) The queue is empty.


-
enumerator CUPTI_ERROR_INVALID_HANDLE
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult26CUPTI_ERROR_INVALID_HANDLEE) Invalid handle (internal?).


-
enumerator CUPTI_ERROR_INVALID_STREAM
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult26CUPTI_ERROR_INVALID_STREAME) Invalid stream.


-
enumerator CUPTI_ERROR_INVALID_KIND
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult24CUPTI_ERROR_INVALID_KINDE) Invalid kind.


-
enumerator CUPTI_ERROR_INVALID_EVENT_VALUE
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult31CUPTI_ERROR_INVALID_EVENT_VALUEE) Invalid event value.


-
enumerator CUPTI_ERROR_DISABLED
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult20CUPTI_ERROR_DISABLEDE) CUPTI is disabled due to conflicts with other enabled profilers.


-
enumerator CUPTI_ERROR_INVALID_MODULE
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult26CUPTI_ERROR_INVALID_MODULEE) Invalid module.


-
enumerator CUPTI_ERROR_INVALID_METRIC_VALUE
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult32CUPTI_ERROR_INVALID_METRIC_VALUEE) Invalid metric value.


-
enumerator CUPTI_ERROR_HARDWARE_BUSY
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult25CUPTI_ERROR_HARDWARE_BUSYE) The performance monitoring hardware is in use by other client.


-
enumerator CUPTI_ERROR_NOT_SUPPORTED
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult25CUPTI_ERROR_NOT_SUPPORTEDE) The attempted operation is not supported on the current system or device.


-
enumerator CUPTI_ERROR_UM_PROFILING_NOT_SUPPORTED
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult38CUPTI_ERROR_UM_PROFILING_NOT_SUPPORTEDE) Unified memory profiling is not supported on the system.

Potential reason could be unsupported OS or architecture.


-
enumerator CUPTI_ERROR_UM_PROFILING_NOT_SUPPORTED_ON_DEVICE
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult48CUPTI_ERROR_UM_PROFILING_NOT_SUPPORTED_ON_DEVICEE) Unified memory profiling is not supported on the device.


-
enumerator CUPTI_ERROR_UM_PROFILING_NOT_SUPPORTED_ON_NON_P2P_DEVICES
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult57CUPTI_ERROR_UM_PROFILING_NOT_SUPPORTED_ON_NON_P2P_DEVICESE) Unified memory profiling is not supported on a multi-GPU configuration without P2P support between any pair of devices.


-
enumerator CUPTI_ERROR_UM_PROFILING_NOT_SUPPORTED_WITH_MPS
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult47CUPTI_ERROR_UM_PROFILING_NOT_SUPPORTED_WITH_MPSE) Unified memory profiling is not supported under the Multi-Process Service (MPS) environment.

CUDA 7.5 removes this restriction.


-
enumerator CUPTI_ERROR_CDP_TRACING_NOT_SUPPORTED
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult37CUPTI_ERROR_CDP_TRACING_NOT_SUPPORTEDE) In CUDA 9.0, devices with compute capability 7.0 don’t support CDP tracing.


-
enumerator CUPTI_ERROR_VIRTUALIZED_DEVICE_NOT_SUPPORTED
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult44CUPTI_ERROR_VIRTUALIZED_DEVICE_NOT_SUPPORTEDE) Profiling on virtualized GPU is not supported.


-
enumerator CUPTI_ERROR_CUDA_COMPILER_NOT_COMPATIBLE
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult40CUPTI_ERROR_CUDA_COMPILER_NOT_COMPATIBLEE) Profiling results might be incorrect for CUDA applications compiled with nvcc version older than 9.0 for devices with compute capability 6.0 and 6.1.

Profiling session will continue and CUPTI will notify it using this error code. User is advised to recompile the application code with nvcc version 9.0 or later. Ignore this warning if code is already compiled with the recommended nvcc version.


-
enumerator CUPTI_ERROR_INSUFFICIENT_PRIVILEGES
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult35CUPTI_ERROR_INSUFFICIENT_PRIVILEGESE) User doesn’t have sufficient privileges which are required to start the profiling session.

One possible reason for this may be that the NVIDIA driver or your system administrator may have restricted access to the NVIDIA GPU performance counters. To learn how to resolve this issue and find more information, please visit

[https://developer.nvidia.com/CUPTI_ERROR_INSUFFICIENT_PRIVILEGES](https://developer.nvidia.com/CUPTI_ERROR_INSUFFICIENT_PRIVILEGES)

-
enumerator CUPTI_ERROR_OLD_PROFILER_API_INITIALIZED
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult40CUPTI_ERROR_OLD_PROFILER_API_INITIALIZEDE) Legacy CUPTI Profiling API i.e.

event API from the header cupti_events.h and metric API from the header cupti_metrics.h are not compatible with the Profiling API in the header cupti_profiler_target.h and Perfworks metrics API in the headers nvperf_host.h and nvperf_target.h.


-
enumerator CUPTI_ERROR_OPENACC_UNDEFINED_ROUTINE
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult37CUPTI_ERROR_OPENACC_UNDEFINED_ROUTINEE) Missing definition of the OpenACC API routine in the linked OpenACC library.

One possible reason is that OpenACC library is linked statically in the user application, which might not have the definition of all the OpenACC API routines needed for the OpenACC profiling, as compiler might ignore definitions for the functions not used in the application. This issue can be mitigated by linking the OpenACC library dynamically.


-
enumerator CUPTI_ERROR_LEGACY_PROFILER_NOT_SUPPORTED
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult41CUPTI_ERROR_LEGACY_PROFILER_NOT_SUPPORTEDE) Legacy CUPTI Profiling API i.e.

event API from the header cupti_events.h and metric API from the header cupti_metrics.h are not supported on devices with compute capability 7.5 and higher (i.e. Turing and later GPU architectures). These APIs were deprecated in CUDA 12.8 and removed in CUDA 13.0. These are replaced by the host profiling API in the header cupti_profiler_host.h and target profiling API in the header cupti_range_profiler.h which are supported on devices with compute capability 7.5 and higher (i.e. Turing and later GPU architectures). Further, the PC Sampling Activity API and the source/SASS level metrics from the header cupti_activity.h are removed in CUDA 13.0. Additionally, the legacy range profiling API i.e. the cuptiProfiler* APIs from the header cupti_profiler_target.h are not supported on Rubin and newer GPU architectures. Use the new cuptiRangeProfiler* APIs from the header cupti_range_profiler.h as a substitute on these architectures.


-
enumerator CUPTI_ERROR_MULTIPLE_SUBSCRIBERS_NOT_SUPPORTED
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult46CUPTI_ERROR_MULTIPLE_SUBSCRIBERS_NOT_SUPPORTEDE) CUPTI doesn’t allow multiple callback subscribers.

Only a single subscriber can be registered at a time. Same error code is used when application is launched using NVIDIA tools like Nsight Systems, Nsight Compute, and cuda-gdb.


-
enumerator CUPTI_ERROR_VIRTUALIZED_DEVICE_INSUFFICIENT_PRIVILEGES
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult54CUPTI_ERROR_VIRTUALIZED_DEVICE_INSUFFICIENT_PRIVILEGESE) Profiling on virtualized GPU is not allowed by hypervisor.


-
enumerator CUPTI_ERROR_CONFIDENTIAL_COMPUTING_NOT_SUPPORTED
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult48CUPTI_ERROR_CONFIDENTIAL_COMPUTING_NOT_SUPPORTEDE) Profiling and tracing are not allowed when confidential computing mode is enabled.


-
enumerator CUPTI_ERROR_CMP_DEVICE_NOT_SUPPORTED
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult36CUPTI_ERROR_CMP_DEVICE_NOT_SUPPORTEDE) CUPTI does not support NVIDIA Crypto Mining Processors (CMP).

For more information, please visit

[https://developer.nvidia.com/ERR_NVCMPGPU](https://developer.nvidia.com/ERR_NVCMPGPU)

-
enumerator CUPTI_ERROR_MIG_DEVICE_NOT_SUPPORTED
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult36CUPTI_ERROR_MIG_DEVICE_NOT_SUPPORTEDE) Profiling on Multi-instance GPU (MIG) is not supported.


-
enumerator CUPTI_ERROR_SLI_DEVICE_NOT_SUPPORTED
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult36CUPTI_ERROR_SLI_DEVICE_NOT_SUPPORTEDE) Profiling on SLI device is not supported.


-
enumerator CUPTI_ERROR_WSL_DEVICE_NOT_SUPPORTED
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult36CUPTI_ERROR_WSL_DEVICE_NOT_SUPPORTEDE) Profiling on WSL device is not supported.


-
enumerator CUPTI_ERROR_INVALID_CHIP_NAME
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult29CUPTI_ERROR_INVALID_CHIP_NAMEE) For invalid or unsupported chip name passed to cuptiProfilerHostInitialize.


-
enumerator CUPTI_ERROR_HES_TRACE_NOT_SUPPORTED_ON_MPS
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult42CUPTI_ERROR_HES_TRACE_NOT_SUPPORTED_ON_MPSE) Hardware Event System (HES) trace is not supported on MPS.


-
enumerator CUPTI_ERROR_UNKNOWN
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult19CUPTI_ERROR_UNKNOWNE) An unknown internal error has occurred.


-
enumerator CUPTI_ERROR_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N11CUptiResult21CUPTI_ERROR_FORCE_INTE)

-
enumerator CUPTI_SUCCESS

## 6.11.4. Functions[#](https://docs.nvidia.com#id2)

-
[CUptiResult](https://docs.nvidia.com#_CPPv411CUptiResult)cuptiGetErrorMessage( ,[CUptiResult](https://docs.nvidia.com#_CPPv411CUptiResult)result*const char **str*,Get the descriptive message corresponding to error codes returned by CUPTI.

Return the descriptive error message for a CUptiResult in

`*str`

.Note

**Thread-safety**: this function is thread safe.- Parameters:
**result**– The result to get the descriptive error message for**str**– Returns the error message string

- Return values:
**CUPTI_SUCCESS**– on success**CUPTI_ERROR_INVALID_PARAMETER**– if`str`

is NULL or`result`

is not a valid CUptiResult



[#](https://docs.nvidia.com#_CPPv420cuptiGetErrorMessage11CUptiResultPPKc)

-
[CUptiResult](https://docs.nvidia.com#_CPPv411CUptiResult)cuptiGetResultString( ,[CUptiResult](https://docs.nvidia.com#_CPPv411CUptiResult)result*const char **str*,Get the descriptive string for a CUptiResult.

Return the descriptive string for a CUptiResult in

`*str`

.Note

**Thread-safety**: this function is thread safe.- Parameters:
**result**– The result to get the string for**str**– Returns the string

- Return values:
**CUPTI_SUCCESS**– on success**CUPTI_ERROR_INVALID_PARAMETER**– if`str`

is NULL or`result`

is not a valid CUptiResult



[#](https://docs.nvidia.com#_CPPv420cuptiGetResultString11CUptiResultPPKc)