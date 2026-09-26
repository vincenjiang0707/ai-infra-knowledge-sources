source: https://docs.nvidia.com/cupti/api/structCUPTI_1_1PcSamplingUtil_1_1CUptiUtil__GetPcSampDataParams.html

# 8.1.1.4. CUptiUtil_GetPcSampDataParams[#](https://docs.nvidia.com#cuptiutil-getpcsampdataparams)

Fully qualified name: `CUPTI::PcSamplingUtil::CUptiUtil_GetPcSampDataParams`


-
struct CUptiUtil_GetPcSampDataParams
[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil29CUptiUtil_GetPcSampDataParamsE) Params for

[CuptiUtilGetPcSampData](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__UTILITY.html#group__cupti__pcsampling__utility_1ga454395b5da004e96767fa739178431ce).Public Members

-
size_t size
[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil29CUptiUtil_GetPcSampDataParams4sizeE) Size of the data structure i.e.

CUpti_PCSamplingDisableParamsSize CUPTI client should set the size of the structure. It will be used in CUPTI to check what fields are available in the structure. Used to preserve backward compatibility.


-
[CUptiUtil_FileHandle](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__UTILITY.html#_CPPv4N5CUPTI14PcSamplingUtil20CUptiUtil_FileHandleE)fileHandle[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil29CUptiUtil_GetPcSampDataParams10fileHandleE) File handle returned by

[CuptiUtilOpenFile](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__UTILITY.html#group__cupti__pcsampling__utility_1ga7d0b234d2965d9ae3ad8b5945a7073f4).

-
[PcSamplingBufferType](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__UTILITY.html#_CPPv4N5CUPTI14PcSamplingUtil20PcSamplingBufferTypeE)bufferType[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil29CUptiUtil_GetPcSampDataParams10bufferTypeE) Type of buffer to store in file.


-
[BufferInfo](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1BufferInfo.html#_CPPv4N5CUPTI14PcSamplingUtil10BufferInfoE)*pBufferInfoData[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil29CUptiUtil_GetPcSampDataParams15pBufferInfoDataE) Pointer to collected buffer info using

[CuptiUtilGetBufferInfo](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__UTILITY.html#group__cupti__pcsampling__utility_1gae4c397f1c21a9baecdc74d38b1b783dd).

-
void *pSamplingData
[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil29CUptiUtil_GetPcSampDataParams13pSamplingDataE) Pointer to allocated memory to store retrieved data from file.


-
size_t numAttributes
[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil29CUptiUtil_GetPcSampDataParams13numAttributesE) Number of configuration attributes.


-
[CUpti_PCSamplingConfigurationInfo](https://docs.nvidia.com/structCUpti__PCSamplingConfigurationInfo.html#_CPPv433CUpti_PCSamplingConfigurationInfo)*pPCSamplingConfigurationInfo[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil29CUptiUtil_GetPcSampDataParams28pPCSamplingConfigurationInfoE)

-
[PcSamplingStallReasons](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1PcSamplingStallReasons.html#_CPPv4N5CUPTI14PcSamplingUtil22PcSamplingStallReasonsE)*pPcSamplingStallReasons[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil29CUptiUtil_GetPcSampDataParams23pPcSamplingStallReasonsE) Refer

[PcSamplingStallReasons](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1PcSamplingStallReasons.html#structcupti_1_1pcsamplingutil_1_1pcsamplingstallreasons).For stallReasons field of

[PcSamplingStallReasons](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1PcSamplingStallReasons.html#structcupti_1_1pcsamplingutil_1_1pcsamplingstallreasons)it is expected to allocate memory for each string element of array.

-
size_t size