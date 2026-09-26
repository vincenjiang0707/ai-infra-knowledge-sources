source: https://docs.nvidia.com/cupti/api/structCUpti__Profiler__Host__Initialize__Params.html

# 7.195. CUpti_Profiler_Host_Initialize_Params[#](https://docs.nvidia.com#cupti-profiler-host-initialize-params)

-
struct CUpti_Profiler_Host_Initialize_Params
[#](https://docs.nvidia.com#_CPPv437CUpti_Profiler_Host_Initialize_Params) Params for cuptiProfilerHostInitialize.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N37CUpti_Profiler_Host_Initialize_Params10structSizeE) [in] Size of the data structure. CUPTI client should set the size of the structure. It will be used in CUPTI to check what fields are available in the structure. Used to preserve backward compatibility.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N37CUpti_Profiler_Host_Initialize_Params5pPrivE) [in] Assign to NULL


-
[CUpti_ProfilerType](https://docs.nvidia.com/group__CUPTI__PROFILER__HOST__API.html#_CPPv418CUpti_ProfilerType)profilerType[#](https://docs.nvidia.com#_CPPv4N37CUpti_Profiler_Host_Initialize_Params12profilerTypeE) [in] the profiler kind one from CUpti_ProfilerType


-
const char *pChipName
[#](https://docs.nvidia.com#_CPPv4N37CUpti_Profiler_Host_Initialize_Params9pChipNameE) [in] accepted for chips supported at the time-of-release.


-
const uint8_t *pCounterAvailabilityImage
[#](https://docs.nvidia.com#_CPPv4N37CUpti_Profiler_Host_Initialize_Params25pCounterAvailabilityImageE) [in] buffer with counter availability image - required for future chip support


-
[CUpti_Profiler_Host_Object](https://docs.nvidia.com/group__CUPTI__PROFILER__HOST__API.html#_CPPv426CUpti_Profiler_Host_Object)*pHostObject[#](https://docs.nvidia.com#_CPPv4N37CUpti_Profiler_Host_Initialize_Params11pHostObjectE) [out] binary blob allocated by CUPTI and operations associated with this object.


-
const char *pSinglePassMetricSetName
[#](https://docs.nvidia.com#_CPPv4N37CUpti_Profiler_Host_Initialize_Params24pSinglePassMetricSetNameE) [in] the single pass metric set name, single pass metric set supported for a chip can be found using cuptiProfilerHostGetSinglePassSets API. Only valid for PM sampling, this can be set to NULL for range profiler.


-
size_t structSize