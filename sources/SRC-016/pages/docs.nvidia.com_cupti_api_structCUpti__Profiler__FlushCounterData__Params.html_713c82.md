source: https://docs.nvidia.com/cupti/api/structCUpti__Profiler__FlushCounterData__Params.html

# 7.179. CUpti_Profiler_FlushCounterData_Params[#](https://docs.nvidia.com#cupti-profiler-flushcounterdata-params)

-
struct CUpti_Profiler_FlushCounterData_Params
[#](https://docs.nvidia.com#_CPPv438CUpti_Profiler_FlushCounterData_Params) Params for cuptiProfilerFlushCounterData.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N38CUpti_Profiler_FlushCounterData_Params10structSizeE) [in] CUpti_Profiler_FlushCounterData_Params_STRUCT_SIZE


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N38CUpti_Profiler_FlushCounterData_Params5pPrivE) [in] assign to NULL


-
CUcontext ctx
[#](https://docs.nvidia.com#_CPPv4N38CUpti_Profiler_FlushCounterData_Params3ctxE) [in] if NULL, the current CUcontext is used


-
size_t numRangesDropped
[#](https://docs.nvidia.com#_CPPv4N38CUpti_Profiler_FlushCounterData_Params16numRangesDroppedE) [out] number of ranges whose data was dropped in the processed passes


-
size_t numTraceBytesDropped
[#](https://docs.nvidia.com#_CPPv4N38CUpti_Profiler_FlushCounterData_Params20numTraceBytesDroppedE) [out] number of bytes not written to TraceBuffer due to buffer full


-
size_t structSize