source: https://docs.nvidia.com/cupti/api/structCUpti__Profiler__Host__GetNumOfPasses__Params.html

# 7.190. CUpti_Profiler_Host_GetNumOfPasses_Params[#](https://docs.nvidia.com#cupti-profiler-host-getnumofpasses-params)

-
struct CUpti_Profiler_Host_GetNumOfPasses_Params
[#](https://docs.nvidia.com#_CPPv441CUpti_Profiler_Host_GetNumOfPasses_Params) Params for cuptiProfilerHostGetNumOfPasses.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N41CUpti_Profiler_Host_GetNumOfPasses_Params10structSizeE) [in] Size of the data structure.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N41CUpti_Profiler_Host_GetNumOfPasses_Params5pPrivE) [in] Assign to NULL


-
size_t configImageSize
[#](https://docs.nvidia.com#_CPPv4N41CUpti_Profiler_Host_GetNumOfPasses_Params15configImageSizeE) [in] Number of bytes allocated for pConfigImage


-
uint8_t *pConfigImage
[#](https://docs.nvidia.com#_CPPv4N41CUpti_Profiler_Host_GetNumOfPasses_Params12pConfigImageE) [in] the config image buffer


-
size_t numOfPasses
[#](https://docs.nvidia.com#_CPPv4N41CUpti_Profiler_Host_GetNumOfPasses_Params11numOfPassesE) [out] number of passes required for profiling scheduled metrics in the config image


-
size_t structSize