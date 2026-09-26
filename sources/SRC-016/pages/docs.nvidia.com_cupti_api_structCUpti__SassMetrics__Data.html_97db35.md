source: https://docs.nvidia.com/cupti/api/structCUpti__SassMetrics__Data.html

# 7.224. CUpti_SassMetrics_Data[#](https://docs.nvidia.com#cupti-sassmetrics-data)

-
struct CUpti_SassMetrics_Data
[#](https://docs.nvidia.com#_CPPv422CUpti_SassMetrics_Data) Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N22CUpti_SassMetrics_Data10structSizeE) [in] equal to CUpti_SassMetricsFlushData_Params_STRUCT_SIZE


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N22CUpti_SassMetrics_Data5pPrivE) [in] assign to NULL


-
uint32_t cubinCrc
[#](https://docs.nvidia.com#_CPPv4N22CUpti_SassMetrics_Data8cubinCrcE) [out] Unique cubin id


-
uint32_t functionIndex
[#](https://docs.nvidia.com#_CPPv4N22CUpti_SassMetrics_Data13functionIndexE) [out] function’s unique symbol index in the module.


-
const char *functionName
[#](https://docs.nvidia.com#_CPPv4N22CUpti_SassMetrics_Data12functionNameE) [out] The function name


-
uint32_t pcOffset
[#](https://docs.nvidia.com#_CPPv4N22CUpti_SassMetrics_Data8pcOffsetE) [out] pc offset for the function in a module


-
[CUpti_SassMetrics_InstanceValue](https://docs.nvidia.com/structCUpti__SassMetrics__InstanceValue.html#_CPPv431CUpti_SassMetrics_InstanceValue)*pInstanceValues[#](https://docs.nvidia.com#_CPPv4N22CUpti_SassMetrics_Data15pInstanceValuesE) [out] array of size equal to number of instances per metric, which contains the metric ID and metric value.


-
size_t structSize