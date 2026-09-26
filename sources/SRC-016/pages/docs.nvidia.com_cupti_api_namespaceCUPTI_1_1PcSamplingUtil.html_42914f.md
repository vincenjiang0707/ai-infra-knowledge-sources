source: https://docs.nvidia.com/cupti/api/namespaceCUPTI_1_1PcSamplingUtil.html

# 8.1.1. PcSamplingUtil[#](https://docs.nvidia.com#pcsamplingutil)

Fully qualified name: `CUPTI::PcSamplingUtil`


-
namespace PcSamplingUtil
[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtilE)

## 8.1.1.9. Data Structures[#](https://docs.nvidia.com#data-structures)

[BufferInfo](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1BufferInfo.html#structcupti_1_1pcsamplingutil_1_1bufferinfo)[BufferInfo](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1BufferInfo.html#structcupti_1_1pcsamplingutil_1_1bufferinfo)will be stored in the file for every buffer i.e for every call of UtilDumpPcSamplingBufferInFile() API.[CUptiUtil_GetBufferInfoParams](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1CUptiUtil__GetBufferInfoParams.html#structcupti_1_1pcsamplingutil_1_1cuptiutil__getbufferinfoparams)Params for

[CuptiUtilGetBufferInfo](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__UTILITY.html#group__cupti__pcsampling__utility_1gae4c397f1c21a9baecdc74d38b1b783dd).[CUptiUtil_GetHeaderDataParams](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1CUptiUtil__GetHeaderDataParams.html#structcupti_1_1pcsamplingutil_1_1cuptiutil__getheaderdataparams)Params for

[CuptiUtilGetHeaderData](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__UTILITY.html#group__cupti__pcsampling__utility_1ga873b630c7ec1a2ada140d2f03b6934c4).[CUptiUtil_GetPcSampDataParams](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1CUptiUtil__GetPcSampDataParams.html#structcupti_1_1pcsamplingutil_1_1cuptiutil__getpcsampdataparams)Params for

[CuptiUtilGetPcSampData](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__UTILITY.html#group__cupti__pcsampling__utility_1ga454395b5da004e96767fa739178431ce).[CUptiUtil_MergePcSampDataParams](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1CUptiUtil__MergePcSampDataParams.html#structcupti_1_1pcsamplingutil_1_1cuptiutil__mergepcsampdataparams)Params for

[CuptiUtilMergePcSampData](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__UTILITY.html#group__cupti__pcsampling__utility_1ga4987e223c4132503d622f29ce5a9546e).[CUptiUtil_PutPcSampDataParams](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1CUptiUtil__PutPcSampDataParams.html#structcupti_1_1pcsamplingutil_1_1cuptiutil__putpcsampdataparams)Params for

[CuptiUtilPutPcSampData](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__UTILITY.html#group__cupti__pcsampling__utility_1gab58ca9a7592643aa51e93d938768d754).[Header](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1Header.html#structcupti_1_1pcsamplingutil_1_1header)[Header](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1Header.html#structcupti_1_1pcsamplingutil_1_1header)info will be stored in file.[PcSamplingStallReasons](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1PcSamplingStallReasons.html#structcupti_1_1pcsamplingutil_1_1pcsamplingstallreasons)All available stall reasons name and respective indexes will be stored in it.


## 8.1.1.10. Enumerations[#](https://docs.nvidia.com#enumerations)

[CUptiUtilResult](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__UTILITY.html#group__cupti__pcsampling__utility_1ga14b3e4f5bd78f1abf3b16884c7dfd755)CUPTI PC sampling utility API result codes.

[PcSamplingBufferType](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__UTILITY.html#group__cupti__pcsampling__utility_1ga1dc90a8b2a7ee09a0c230aa6256bba5e)CUPTI PC sampling buffer types.


## 8.1.1.11. Functions[#](https://docs.nvidia.com#functions)

- CUptiUtilResult
[CuptiUtilCloseFile](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__UTILITY.html#group__cupti__pcsampling__utility_1ga493512247a165cddc2793b376b1d30c1)(CUptiUtil_FileHandle fileHandle) Close a file handle opened by

[CuptiUtilOpenFile](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__UTILITY.html#group__cupti__pcsampling__utility_1ga7d0b234d2965d9ae3ad8b5945a7073f4).- CUptiUtilResult
[CuptiUtilGetBufferInfo](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__UTILITY.html#group__cupti__pcsampling__utility_1gae4c397f1c21a9baecdc74d38b1b783dd)(CUptiUtil_GetBufferInfoParams *pParams) Get buffer info data of file.

- CUptiUtilResult
[CuptiUtilGetHeaderData](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__UTILITY.html#group__cupti__pcsampling__utility_1ga873b630c7ec1a2ada140d2f03b6934c4)(CUptiUtil_GetHeaderDataParams *pParams) Get header data of file.

- CUptiUtilResult
[CuptiUtilGetPcSampData](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__UTILITY.html#group__cupti__pcsampling__utility_1ga454395b5da004e96767fa739178431ce)(CUptiUtil_GetPcSampDataParams *pParams) Retrieve PC sampling data from file into allocated buffer.

- CUptiUtilResult
[CuptiUtilMergePcSampData](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__UTILITY.html#group__cupti__pcsampling__utility_1ga4987e223c4132503d622f29ce5a9546e)(CUptiUtil_MergePcSampDataParams *pParams) Merge PC sampling data range id wise.

- CUptiUtilResult
[CuptiUtilOpenFile](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__UTILITY.html#group__cupti__pcsampling__utility_1ga7d0b234d2965d9ae3ad8b5945a7073f4)(const char *fileName, CUptiUtil_FileHandle *pFileHandle) Open a file for reading PC sampling data.

- CUptiUtilResult
[CuptiUtilPutPcSampData](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__UTILITY.html#group__cupti__pcsampling__utility_1gab58ca9a7592643aa51e93d938768d754)(CUptiUtil_PutPcSampDataParams *pParams) Dump PC sampling data into the file.


## 8.1.1.12. Typedefs[#](https://docs.nvidia.com#typedefs)

[CUptiUtil_FileHandle](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__UTILITY.html#group__cupti__pcsampling__utility_1ga28b4be4be7a01c6e3521dd72ae439785)Opaque file handle for PC sampling utility read APIs.