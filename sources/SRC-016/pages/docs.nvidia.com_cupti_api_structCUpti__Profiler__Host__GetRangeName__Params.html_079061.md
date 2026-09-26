source: https://docs.nvidia.com/cupti/api/structCUpti__Profiler__Host__GetRangeName__Params.html

# 7.191. CUpti_Profiler_Host_GetRangeName_Params[#](https://docs.nvidia.com#cupti-profiler-host-getrangename-params)

-
struct CUpti_Profiler_Host_GetRangeName_Params
[#](https://docs.nvidia.com#_CPPv439CUpti_Profiler_Host_GetRangeName_Params) Params for cuptiProfilerHostGetRangeName.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N39CUpti_Profiler_Host_GetRangeName_Params10structSizeE) [in] Size of the data structure.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N39CUpti_Profiler_Host_GetRangeName_Params5pPrivE) [in] Assign to NULL


-
const uint8_t *pCounterDataImage
[#](https://docs.nvidia.com#_CPPv4N39CUpti_Profiler_Host_GetRangeName_Params17pCounterDataImageE) [in] the counter data image where profiling data has been decoded


-
size_t counterDataImageSize
[#](https://docs.nvidia.com#_CPPv4N39CUpti_Profiler_Host_GetRangeName_Params20counterDataImageSizeE) [in] size of counter data image


-
size_t rangeIndex
[#](https://docs.nvidia.com#_CPPv4N39CUpti_Profiler_Host_GetRangeName_Params10rangeIndexE) [in] range index for which the range name will be queried


-
const char *delimiter
[#](https://docs.nvidia.com#_CPPv4N39CUpti_Profiler_Host_GetRangeName_Params9delimiterE) [in] used in case of nested ranges, default=”/”. Range1<delimiter>Range2


-
const char *pRangeName
[#](https://docs.nvidia.com#_CPPv4N39CUpti_Profiler_Host_GetRangeName_Params10pRangeNameE) [out] the range name. Note: that the CUPTI allocate the memory internal and its user responsibility to free up the allocated memory


-
size_t structSize