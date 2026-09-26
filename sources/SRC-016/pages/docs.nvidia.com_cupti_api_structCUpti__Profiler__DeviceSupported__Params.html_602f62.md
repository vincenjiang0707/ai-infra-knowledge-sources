source: https://docs.nvidia.com/cupti/api/structCUpti__Profiler__DeviceSupported__Params.html

# 7.174. CUpti_Profiler_DeviceSupported_Params[#](https://docs.nvidia.com#cupti-profiler-devicesupported-params)

-
struct CUpti_Profiler_DeviceSupported_Params
[#](https://docs.nvidia.com#_CPPv437CUpti_Profiler_DeviceSupported_Params) Params for cuptiProfilerDeviceSupported.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N37CUpti_Profiler_DeviceSupported_Params10structSizeE) [in] Must be CUpti_Profiler_DeviceSupported_Params_STRUCT_SIZE


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N37CUpti_Profiler_DeviceSupported_Params5pPrivE) [in] assign to NULL


-
CUdevice cuDevice
[#](https://docs.nvidia.com#_CPPv4N37CUpti_Profiler_DeviceSupported_Params8cuDeviceE) [in] if NULL, the current CUcontext is used


-
[CUpti_Profiler_Support_Level](https://docs.nvidia.com/group__CUPTI__PROFILER__API.html#_CPPv428CUpti_Profiler_Support_Level)isSupported[#](https://docs.nvidia.com#_CPPv4N37CUpti_Profiler_DeviceSupported_Params11isSupportedE) [out] overall SUPPORTED / UNSUPPORTED flag representing whether Profiling and PC Sampling APIs work on the given device and configuration. SUPPORTED if all following flags are SUPPORTED, UNSUPPORTED otherwise.


-
[CUpti_Profiler_Support_Level](https://docs.nvidia.com/group__CUPTI__PROFILER__API.html#_CPPv428CUpti_Profiler_Support_Level)architecture[#](https://docs.nvidia.com#_CPPv4N37CUpti_Profiler_DeviceSupported_Params12architectureE) [out] SUPPORTED if the device architecture level supports the Profiling API (Compute Capability >= 7.0), UNSUPPORTED otherwise


-
[CUpti_Profiler_Support_Level](https://docs.nvidia.com/group__CUPTI__PROFILER__API.html#_CPPv428CUpti_Profiler_Support_Level)sli[#](https://docs.nvidia.com#_CPPv4N37CUpti_Profiler_DeviceSupported_Params3sliE) [out] SUPPORTED if SLI is not enabled, UNSUPPORTED otherwise


-
[CUpti_Profiler_Support_Level](https://docs.nvidia.com/group__CUPTI__PROFILER__API.html#_CPPv428CUpti_Profiler_Support_Level)vGpu[#](https://docs.nvidia.com#_CPPv4N37CUpti_Profiler_DeviceSupported_Params4vGpuE) [out] SUPPORTED if vGPU is supported and profiling is enabled, DISABLED if profiling is supported but not enabled, UNSUPPORTED otherwise


-
[CUpti_Profiler_Support_Level](https://docs.nvidia.com/group__CUPTI__PROFILER__API.html#_CPPv428CUpti_Profiler_Support_Level)confidentialCompute[#](https://docs.nvidia.com#_CPPv4N37CUpti_Profiler_DeviceSupported_Params19confidentialComputeE) [out] SUPPORTED if confidential compute is not enabled, UNSUPPORTED otherwise


-
[CUpti_Profiler_Support_Level](https://docs.nvidia.com/group__CUPTI__PROFILER__API.html#_CPPv428CUpti_Profiler_Support_Level)cmp[#](https://docs.nvidia.com#_CPPv4N37CUpti_Profiler_DeviceSupported_Params3cmpE) [out] SUPPORTED if not NVIDIA Crypto Mining Processors (CMP), UNSUPPORTED otherwise


-
[CUpti_Profiler_Support_Level](https://docs.nvidia.com/group__CUPTI__PROFILER__API.html#_CPPv428CUpti_Profiler_Support_Level)wsl[#](https://docs.nvidia.com#_CPPv4N37CUpti_Profiler_DeviceSupported_Params3wslE) [out] SUPPORTED if WSL supported, UNSUPPORTED otherwise


-
[CUpti_Profiler_API](https://docs.nvidia.com/group__CUPTI__PROFILER__API.html#_CPPv418CUpti_Profiler_API)api[#](https://docs.nvidia.com#_CPPv4N37CUpti_Profiler_DeviceSupported_Params3apiE) [in] the CUPTI API type for which device support will be checked


-
[CUpti_Profiler_Support_Level](https://docs.nvidia.com/group__CUPTI__PROFILER__API.html#_CPPv428CUpti_Profiler_Support_Level)sku[#](https://docs.nvidia.com#_CPPv4N37CUpti_Profiler_DeviceSupported_Params3skuE) [out] SUPPORTED if SKU supported, UNSUPPORTED otherwise


-
size_t structSize