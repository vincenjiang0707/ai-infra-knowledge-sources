source: https://docs.nvidia.com/cupti/api/structCUpti__Profiler__PushRange__Params.html

# 7.200. CUpti_Profiler_PushRange_Params[#](https://docs.nvidia.com#cupti-profiler-pushrange-params)

-
struct CUpti_Profiler_PushRange_Params
[#](https://docs.nvidia.com#_CPPv431CUpti_Profiler_PushRange_Params) Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N31CUpti_Profiler_PushRange_Params10structSizeE) [in] CUpti_Profiler_PushRange_Params_STRUCT_SIZE


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N31CUpti_Profiler_PushRange_Params5pPrivE) [in] assign to NULL


-
CUcontext ctx
[#](https://docs.nvidia.com#_CPPv4N31CUpti_Profiler_PushRange_Params3ctxE) [in] if NULL, the current CUcontext is used


-
const char *pRangeName
[#](https://docs.nvidia.com#_CPPv4N31CUpti_Profiler_PushRange_Params10pRangeNameE) [in] specifies the range for subsequent launches; must not be NULL


-
size_t rangeNameLength
[#](https://docs.nvidia.com#_CPPv4N31CUpti_Profiler_PushRange_Params15rangeNameLengthE) [in] assign to strlen(pRangeName) if known; if set to zero, the library will call strlen()


-
size_t structSize