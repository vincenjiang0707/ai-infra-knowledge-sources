source: https://docs.nvidia.com/cupti/api/structCUPTI_1_1PcSamplingUtil_1_1CUptiUtil__PutPcSampDataParams.html

# 8.1.1.6. CUptiUtil_PutPcSampDataParams[#](https://docs.nvidia.com#cuptiutil-putpcsampdataparams)

Fully qualified name: `CUPTI::PcSamplingUtil::CUptiUtil_PutPcSampDataParams`


-
struct CUptiUtil_PutPcSampDataParams
[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil29CUptiUtil_PutPcSampDataParamsE) Params for

[CuptiUtilPutPcSampData](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__UTILITY.html#group__cupti__pcsampling__utility_1gab58ca9a7592643aa51e93d938768d754).Public Members

-
size_t size
[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil29CUptiUtil_PutPcSampDataParams4sizeE) Size of the data structure i.e.

CUpti_PCSamplingDisableParamsSize CUPTI client should set the size of the structure. It will be used in CUPTI to check what fields are available in the structure. Used to preserve backward compatibility.


-
[PcSamplingBufferType](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__UTILITY.html#_CPPv4N5CUPTI14PcSamplingUtil20PcSamplingBufferTypeE)bufferType[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil29CUptiUtil_PutPcSampDataParams10bufferTypeE) Type of buffer to store in file.


-
void *pSamplingData
[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil29CUptiUtil_PutPcSampDataParams13pSamplingDataE) PC sampling buffer.


-
size_t numAttributes
[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil29CUptiUtil_PutPcSampDataParams13numAttributesE) Number of configured attributes.


-
[CUpti_PCSamplingConfigurationInfo](https://docs.nvidia.com/structCUpti__PCSamplingConfigurationInfo.html#_CPPv433CUpti_PCSamplingConfigurationInfo)*pPCSamplingConfigurationInfo[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil29CUptiUtil_PutPcSampDataParams28pPCSamplingConfigurationInfoE) Refer

[CUpti_PCSamplingConfigurationInfo](https://docs.nvidia.com/structCUpti__PCSamplingConfigurationInfo.html#structcupti__pcsamplingconfigurationinfo)It is expected to provide configuration details of at least CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_STALL_REASON attribute.

-
[PcSamplingStallReasons](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1PcSamplingStallReasons.html#_CPPv4N5CUPTI14PcSamplingUtil22PcSamplingStallReasonsE)*pPcSamplingStallReasons[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil29CUptiUtil_PutPcSampDataParams23pPcSamplingStallReasonsE) Refer

[PcSamplingStallReasons](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1PcSamplingStallReasons.html#structcupti_1_1pcsamplingutil_1_1pcsamplingstallreasons).

-
const char *fileName
[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil29CUptiUtil_PutPcSampDataParams8fileNameE) File name to store buffer into it.


-
size_t size