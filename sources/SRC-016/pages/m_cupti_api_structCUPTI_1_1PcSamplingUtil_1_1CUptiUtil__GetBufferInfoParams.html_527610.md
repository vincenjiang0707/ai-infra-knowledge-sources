source: https://docs.nvidia.com/cupti/api/structCUPTI_1_1PcSamplingUtil_1_1CUptiUtil__GetBufferInfoParams.html

# 8.1.1.2. CUptiUtil_GetBufferInfoParams[#](https://docs.nvidia.com#cuptiutil-getbufferinfoparams)

Fully qualified name: `CUPTI::PcSamplingUtil::CUptiUtil_GetBufferInfoParams`


-
struct CUptiUtil_GetBufferInfoParams
[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil29CUptiUtil_GetBufferInfoParamsE) Params for

[CuptiUtilGetBufferInfo](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__UTILITY.html#group__cupti__pcsampling__utility_1gae4c397f1c21a9baecdc74d38b1b783dd).Public Members

-
size_t size
[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil29CUptiUtil_GetBufferInfoParams4sizeE) Size of the data structure i.e.

CUpti_PCSamplingDisableParamsSize CUPTI client should set the size of the structure. It will be used in CUPTI to check what fields are available in the structure. Used to preserve backward compatibility.


-
[CUptiUtil_FileHandle](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__UTILITY.html#_CPPv4N5CUPTI14PcSamplingUtil20CUptiUtil_FileHandleE)fileHandle[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil29CUptiUtil_GetBufferInfoParams10fileHandleE) File handle returned by

[CuptiUtilOpenFile](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__UTILITY.html#group__cupti__pcsampling__utility_1ga7d0b234d2965d9ae3ad8b5945a7073f4).

-
[BufferInfo](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1BufferInfo.html#_CPPv4N5CUPTI14PcSamplingUtil10BufferInfoE)bufferInfoData[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil29CUptiUtil_GetBufferInfoParams14bufferInfoDataE) Buffer Info.


-
size_t size