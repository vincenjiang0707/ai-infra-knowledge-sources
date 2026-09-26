source: https://docs.nvidia.com/cupti/api/structCUpti__Profiler__IsPassCollected__Params.html

# 7.198. CUpti_Profiler_IsPassCollected_Params[#](https://docs.nvidia.com#cupti-profiler-ispasscollected-params)

-
struct CUpti_Profiler_IsPassCollected_Params
[#](https://docs.nvidia.com#_CPPv437CUpti_Profiler_IsPassCollected_Params) Params for cuptiProfilerIsPassCollected.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N37CUpti_Profiler_IsPassCollected_Params10structSizeE) [in] CUpti_Profiler_IsPassCollected_Params_STRUCT_SIZE


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N37CUpti_Profiler_IsPassCollected_Params5pPrivE) [in] assign to NULL


-
CUcontext ctx
[#](https://docs.nvidia.com#_CPPv4N37CUpti_Profiler_IsPassCollected_Params3ctxE) [in] if NULL, the current CUcontext is used


-
size_t numRangesDropped
[#](https://docs.nvidia.com#_CPPv4N37CUpti_Profiler_IsPassCollected_Params16numRangesDroppedE) [out] number of ranges whose data was dropped in the processed pass


-
size_t numTraceBytesDropped
[#](https://docs.nvidia.com#_CPPv4N37CUpti_Profiler_IsPassCollected_Params20numTraceBytesDroppedE) [out] number of bytes not written to TraceBuffer due to buffer full


-
uint8_t onePassCollected
[#](https://docs.nvidia.com#_CPPv4N37CUpti_Profiler_IsPassCollected_Params16onePassCollectedE) [out] true if a pass was successfully decoded


-
uint8_t allPassesCollected
[#](https://docs.nvidia.com#_CPPv4N37CUpti_Profiler_IsPassCollected_Params18allPassesCollectedE) [out] becomes true when the last pass has been decoded


-
size_t structSize