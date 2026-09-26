source: https://docs.nvidia.com/cupti/api/structCUpti__Profiler__Host__GetConfigImage__Params.html

# 7.186. CUpti_Profiler_Host_GetConfigImage_Params[#](https://docs.nvidia.com#cupti-profiler-host-getconfigimage-params)

-
struct CUpti_Profiler_Host_GetConfigImage_Params
[#](https://docs.nvidia.com#_CPPv441CUpti_Profiler_Host_GetConfigImage_Params) Params for cuptiProfilerHostGetConfigImage.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N41CUpti_Profiler_Host_GetConfigImage_Params10structSizeE) [in] Size of the data structure.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N41CUpti_Profiler_Host_GetConfigImage_Params5pPrivE) [in] Assign to NULL


-
[CUpti_Profiler_Host_Object](https://docs.nvidia.com/group__CUPTI__PROFILER__HOST__API.html#_CPPv426CUpti_Profiler_Host_Object)*pHostObject[#](https://docs.nvidia.com#_CPPv4N41CUpti_Profiler_Host_GetConfigImage_Params11pHostObjectE) [in] reference to the profiler host object allocated by CUPTI in cuptiProfilerHostInitialize


-
size_t configImageSize
[#](https://docs.nvidia.com#_CPPv4N41CUpti_Profiler_Host_GetConfigImage_Params15configImageSizeE) [in] Number of bytes allocated for pBuffer


-
uint8_t *pConfigImage
[#](https://docs.nvidia.com#_CPPv4N41CUpti_Profiler_Host_GetConfigImage_Params12pConfigImageE) [out] Buffer receiving the config image


-
size_t structSize