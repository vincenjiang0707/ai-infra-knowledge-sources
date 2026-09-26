source: https://docs.nvidia.com/cupti/api/structCUpti__PCSamplingConfigurationInfoParams.html

# 7.144. CUpti_PCSamplingConfigurationInfoParams[#](https://docs.nvidia.com#cupti-pcsamplingconfigurationinfoparams)

-
struct CUpti_PCSamplingConfigurationInfoParams
[#](https://docs.nvidia.com#_CPPv439CUpti_PCSamplingConfigurationInfoParams) PC sampling configuration structure.

This structure configures PC sampling using

[cuptiPCSamplingSetConfigurationAttribute](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__API.html#group__cupti__pcsampling__api_1gaf3e8842fda99b4c1659c2d2f1c18674e)and queries PC sampling default configuration using[cuptiPCSamplingGetConfigurationAttribute](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__API.html#group__cupti__pcsampling__api_1gada8f3c53c8673e56a689a67cae7e8df2)Public Members

-
size_t size
[#](https://docs.nvidia.com#_CPPv4N39CUpti_PCSamplingConfigurationInfoParams4sizeE) [w] Size of the data structure i.e.

CUpti_PCSamplingConfigurationInfoParamsSize CUPTI client should set the size of the structure. It will be used in CUPTI to check what fields are available in the structure. Used to preserve backward compatibility.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N39CUpti_PCSamplingConfigurationInfoParams5pPrivE) [w] Assign to NULL


-
CUcontext ctx
[#](https://docs.nvidia.com#_CPPv4N39CUpti_PCSamplingConfigurationInfoParams3ctxE) [w] CUcontext


-
size_t numAttributes
[#](https://docs.nvidia.com#_CPPv4N39CUpti_PCSamplingConfigurationInfoParams13numAttributesE) [w] Number of attributes to configure using

[cuptiPCSamplingSetConfigurationAttribute](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__API.html#group__cupti__pcsampling__api_1gaf3e8842fda99b4c1659c2d2f1c18674e)or query using[cuptiPCSamplingGetConfigurationAttribute](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__API.html#group__cupti__pcsampling__api_1gada8f3c53c8673e56a689a67cae7e8df2)

-
[CUpti_PCSamplingConfigurationInfo](https://docs.nvidia.com/structCUpti__PCSamplingConfigurationInfo.html#_CPPv433CUpti_PCSamplingConfigurationInfo)*pPCSamplingConfigurationInfo[#](https://docs.nvidia.com#_CPPv4N39CUpti_PCSamplingConfigurationInfoParams28pPCSamplingConfigurationInfoE)

-
size_t size