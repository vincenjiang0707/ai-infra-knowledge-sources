source: https://docs.nvidia.com/cupti/api/structCUpti__Profiler__Host__GetConfigImageSize__Params.html

# 7.185. CUpti_Profiler_Host_GetConfigImageSize_Params[#](https://docs.nvidia.com#cupti-profiler-host-getconfigimagesize-params)

-
struct CUpti_Profiler_Host_GetConfigImageSize_Params
[#](https://docs.nvidia.com#_CPPv445CUpti_Profiler_Host_GetConfigImageSize_Params) Params for cuptiProfilerHostGetConfigImageSize.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N45CUpti_Profiler_Host_GetConfigImageSize_Params10structSizeE) [in] Size of the data structure.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N45CUpti_Profiler_Host_GetConfigImageSize_Params5pPrivE) [in] Assign to NULL


-
[CUpti_Profiler_Host_Object](https://docs.nvidia.com/group__CUPTI__PROFILER__HOST__API.html#_CPPv426CUpti_Profiler_Host_Object)*pHostObject[#](https://docs.nvidia.com#_CPPv4N45CUpti_Profiler_Host_GetConfigImageSize_Params11pHostObjectE) [in] reference to the profiler host object allocated by CUPTI in cuptiProfilerHostInitialize


-
size_t configImageSize
[#](https://docs.nvidia.com#_CPPv4N45CUpti_Profiler_Host_GetConfigImageSize_Params15configImageSizeE) [out] the size of config image, users need to allocate the buffer for storing


-
size_t structSize