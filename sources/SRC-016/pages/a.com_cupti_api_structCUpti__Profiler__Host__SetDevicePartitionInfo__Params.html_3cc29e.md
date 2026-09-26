source: https://docs.nvidia.com/cupti/api/structCUpti__Profiler__Host__SetDevicePartitionInfo__Params.html

# 7.196. CUpti_Profiler_Host_SetDevicePartitionInfo_Params[#](https://docs.nvidia.com#cupti-profiler-host-setdevicepartitioninfo-params)

-
struct CUpti_Profiler_Host_SetDevicePartitionInfo_Params
[#](https://docs.nvidia.com#_CPPv449CUpti_Profiler_Host_SetDevicePartitionInfo_Params) Params for cuptiProfilerHostSetDevicePartitionInfo.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N49CUpti_Profiler_Host_SetDevicePartitionInfo_Params10structSizeE) [in] Size of the data structure.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N49CUpti_Profiler_Host_SetDevicePartitionInfo_Params5pPrivE) [in] Assign to NULL


-
[CUpti_Profiler_Host_Object](https://docs.nvidia.com/group__CUPTI__PROFILER__HOST__API.html#_CPPv426CUpti_Profiler_Host_Object)*pHostObject[#](https://docs.nvidia.com#_CPPv4N49CUpti_Profiler_Host_SetDevicePartitionInfo_Params11pHostObjectE) [in] The profiler host object created via cuptiProfilerHostInitialize.


-
uint8_t *pDevicePartitionInfo
[#](https://docs.nvidia.com#_CPPv4N49CUpti_Profiler_Host_SetDevicePartitionInfo_Params20pDevicePartitionInfoE) [in] Buffer containing the device partition information obtained from the target side using cuptiRangeProfilerGetDevicePartitionInfo. This encodes the SM resource allocation for the Green Context being profiled.


-
size_t devicePartitionInfoSize
[#](https://docs.nvidia.com#_CPPv4N49CUpti_Profiler_Host_SetDevicePartitionInfo_Params23devicePartitionInfoSizeE) [in] Size of the device partition info buffer in bytes.


-
size_t structSize