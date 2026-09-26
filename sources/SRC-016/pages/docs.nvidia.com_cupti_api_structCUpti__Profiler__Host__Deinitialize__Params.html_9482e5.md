source: https://docs.nvidia.com/cupti/api/structCUpti__Profiler__Host__Deinitialize__Params.html

# 7.182. CUpti_Profiler_Host_Deinitialize_Params[#](https://docs.nvidia.com#cupti-profiler-host-deinitialize-params)

-
struct CUpti_Profiler_Host_Deinitialize_Params
[#](https://docs.nvidia.com#_CPPv439CUpti_Profiler_Host_Deinitialize_Params) Params for cuptiProfilerHostDeinitialize.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N39CUpti_Profiler_Host_Deinitialize_Params10structSizeE) [in] Size of the data structure. CUPTI client should set the size of the structure. It will be used in CUPTI to check what fields are available in the structure. Used to preserve backward compatibility.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N39CUpti_Profiler_Host_Deinitialize_Params5pPrivE) [in] Assign to NULL


-
struct
[CUpti_Profiler_Host_Object](https://docs.nvidia.com/group__CUPTI__PROFILER__HOST__API.html#_CPPv426CUpti_Profiler_Host_Object)*pHostObject[#](https://docs.nvidia.com#_CPPv4N39CUpti_Profiler_Host_Deinitialize_Params11pHostObjectE) [in] reference to the profiler host object allocated by CUPTI in cuptiProfilerHostInitialize


-
size_t structSize