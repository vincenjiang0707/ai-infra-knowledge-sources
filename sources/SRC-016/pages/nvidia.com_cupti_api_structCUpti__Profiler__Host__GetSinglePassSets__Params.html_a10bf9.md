source: https://docs.nvidia.com/cupti/api/structCUpti__Profiler__Host__GetSinglePassSets__Params.html

# 7.192. CUpti_Profiler_Host_GetSinglePassSets_Params[#](https://docs.nvidia.com#cupti-profiler-host-getsinglepasssets-params)

-
struct CUpti_Profiler_Host_GetSinglePassSets_Params
[#](https://docs.nvidia.com#_CPPv444CUpti_Profiler_Host_GetSinglePassSets_Params) Params for cuptiProfilerHostGetSinglePassSets.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N44CUpti_Profiler_Host_GetSinglePassSets_Params10structSizeE) [in] Size of the data structure.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N44CUpti_Profiler_Host_GetSinglePassSets_Params5pPrivE) [in] Assign to NULL


-
const char *pChipName
[#](https://docs.nvidia.com#_CPPv4N44CUpti_Profiler_Host_GetSinglePassSets_Params9pChipNameE) [in] the chip name for which the single pass metric sets will be queried


-
size_t numOfSinglePassSets
[#](https://docs.nvidia.com#_CPPv4N44CUpti_Profiler_Host_GetSinglePassSets_Params19numOfSinglePassSetsE) [out] number of single pass metric sets


-
const char **ppSinglePassSets
[#](https://docs.nvidia.com#_CPPv4N44CUpti_Profiler_Host_GetSinglePassSets_Params16ppSinglePassSetsE) [out] list of single pass metric sets.


-
size_t structSize