source: https://docs.nvidia.com/cupti/api/structCUpti__RangeProfiler__GetDevicePartitionInfo__Params.html

# 7.210. CUpti_RangeProfiler_GetDevicePartitionInfo_Params[#](https://docs.nvidia.com#cupti-rangeprofiler-getdevicepartitioninfo-params)

-
struct CUpti_RangeProfiler_GetDevicePartitionInfo_Params
[#](https://docs.nvidia.com#_CPPv449CUpti_RangeProfiler_GetDevicePartitionInfo_Params) Params for cuptiRangeProfilerGetDevicePartitionInfo.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N49CUpti_RangeProfiler_GetDevicePartitionInfo_Params10structSizeE) [in] Size of the data structure.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N49CUpti_RangeProfiler_GetDevicePartitionInfo_Params5pPrivE) [in] Set to NULL.


-
[CUpti_RangeProfiler_Object](https://docs.nvidia.com/group__CUPTI__RANGE__PROFILER__API.html#_CPPv426CUpti_RangeProfiler_Object)*pRangeProfilerObject[#](https://docs.nvidia.com#_CPPv4N49CUpti_RangeProfiler_GetDevicePartitionInfo_Params20pRangeProfilerObjectE) [in] Range profiler object created via cuptiRangeProfilerEnable on a Green Context.


-
size_t devicePartitionInfoSize
[#](https://docs.nvidia.com#_CPPv4N49CUpti_RangeProfiler_GetDevicePartitionInfo_Params23devicePartitionInfoSizeE) [inout] If

`pDevicePartitionInfo`

is NULL, then the required buffer size is returned in`devicePartitionInfoSize`

. Otherwise,`devicePartitionInfoSize`

should be set to the allocated buffer size of`pDevicePartitionInfo`

.

-
uint8_t *pDevicePartitionInfo
[#](https://docs.nvidia.com#_CPPv4N49CUpti_RangeProfiler_GetDevicePartitionInfo_Params20pDevicePartitionInfoE) [inout] Buffer to store the device partition information. Set to NULL in the first call to query the required buffer size. In the second call, pass an allocated buffer of size

`devicePartitionInfoSize`

to receive the partition information encoding the SM resource allocation for the Green Context.

-
size_t structSize