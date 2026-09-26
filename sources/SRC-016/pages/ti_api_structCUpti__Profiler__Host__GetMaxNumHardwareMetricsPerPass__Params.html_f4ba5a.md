source: https://docs.nvidia.com/cupti/api/structCUpti__Profiler__Host__GetMaxNumHardwareMetricsPerPass__Params.html

# 7.187. CUpti_Profiler_Host_GetMaxNumHardwareMetricsPerPass_Params[#](https://docs.nvidia.com#cupti-profiler-host-getmaxnumhardwaremetricsperpass-params)

-
struct CUpti_Profiler_Host_GetMaxNumHardwareMetricsPerPass_Params
[#](https://docs.nvidia.com#_CPPv458CUpti_Profiler_Host_GetMaxNumHardwareMetricsPerPass_Params) Params for cuptiProfilerHostGetMaxNumHardwareMetricsPerPass.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N58CUpti_Profiler_Host_GetMaxNumHardwareMetricsPerPass_Params10structSizeE) [in] Size of the data structure.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N58CUpti_Profiler_Host_GetMaxNumHardwareMetricsPerPass_Params5pPrivE) [in] Assign to NULL


-
[CUpti_ProfilerType](https://docs.nvidia.com/group__CUPTI__PROFILER__HOST__API.html#_CPPv418CUpti_ProfilerType)profilerType[#](https://docs.nvidia.com#_CPPv4N58CUpti_Profiler_Host_GetMaxNumHardwareMetricsPerPass_Params12profilerTypeE) [in] the profiler kind one from CUpti_ProfilerType


-
const char *pChipName
[#](https://docs.nvidia.com#_CPPv4N58CUpti_Profiler_Host_GetMaxNumHardwareMetricsPerPass_Params9pChipNameE) [in] accepted for chips supported at the time-of-release.


-
uint8_t *pCounterAvailabilityImage
[#](https://docs.nvidia.com#_CPPv4N58CUpti_Profiler_Host_GetMaxNumHardwareMetricsPerPass_Params25pCounterAvailabilityImageE) [in] buffer with counter availability image - required for future chip support


-
size_t maxMetricsPerPass
[#](https://docs.nvidia.com#_CPPv4N58CUpti_Profiler_Host_GetMaxNumHardwareMetricsPerPass_Params17maxMetricsPerPassE) [out] maximum number of metrics that can be scheduled in a pass


-
size_t structSize