source: https://docs.nvidia.com/cupti/api/group__CUPTI__PCSAMPLING__UTILITY.html

# 6.6. CUPTI PC Sampling Utility API[#](https://docs.nvidia.com#cupti-pc-sampling-utility-api)

Functions, types, and enums that implement the CUPTI PC Sampling Utility API.

## 6.6.1. Data Structures[#](https://docs.nvidia.com#data-structures)

[CUPTI::PcSamplingUtil::BufferInfo](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1BufferInfo.html#structcupti_1_1pcsamplingutil_1_1bufferinfo)[BufferInfo](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1BufferInfo.html#structcupti_1_1pcsamplingutil_1_1bufferinfo)will be stored in the file for every buffer i.e for every call of UtilDumpPcSamplingBufferInFile() API.[CUPTI::PcSamplingUtil::CUptiUtil_GetBufferInfoParams](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1CUptiUtil__GetBufferInfoParams.html#structcupti_1_1pcsamplingutil_1_1cuptiutil__getbufferinfoparams)Params for

[CuptiUtilGetBufferInfo](https://docs.nvidia.com#group__cupti__pcsampling__utility_1gae4c397f1c21a9baecdc74d38b1b783dd).[CUPTI::PcSamplingUtil::CUptiUtil_GetHeaderDataParams](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1CUptiUtil__GetHeaderDataParams.html#structcupti_1_1pcsamplingutil_1_1cuptiutil__getheaderdataparams)Params for

[CuptiUtilGetHeaderData](https://docs.nvidia.com#group__cupti__pcsampling__utility_1ga873b630c7ec1a2ada140d2f03b6934c4).[CUPTI::PcSamplingUtil::CUptiUtil_GetPcSampDataParams](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1CUptiUtil__GetPcSampDataParams.html#structcupti_1_1pcsamplingutil_1_1cuptiutil__getpcsampdataparams)Params for

[CuptiUtilGetPcSampData](https://docs.nvidia.com#group__cupti__pcsampling__utility_1ga454395b5da004e96767fa739178431ce).[CUPTI::PcSamplingUtil::CUptiUtil_MergePcSampDataParams](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1CUptiUtil__MergePcSampDataParams.html#structcupti_1_1pcsamplingutil_1_1cuptiutil__mergepcsampdataparams)Params for

[CuptiUtilMergePcSampData](https://docs.nvidia.com#group__cupti__pcsampling__utility_1ga4987e223c4132503d622f29ce5a9546e).[CUPTI::PcSamplingUtil::CUptiUtil_PutPcSampDataParams](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1CUptiUtil__PutPcSampDataParams.html#structcupti_1_1pcsamplingutil_1_1cuptiutil__putpcsampdataparams)Params for

[CuptiUtilPutPcSampData](https://docs.nvidia.com#group__cupti__pcsampling__utility_1gab58ca9a7592643aa51e93d938768d754).[CUPTI::PcSamplingUtil::Header](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1Header.html#structcupti_1_1pcsamplingutil_1_1header)[Header](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1Header.html#structcupti_1_1pcsamplingutil_1_1header)info will be stored in file.[CUPTI::PcSamplingUtil::PcSamplingStallReasons](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1PcSamplingStallReasons.html#structcupti_1_1pcsamplingutil_1_1pcsamplingstallreasons)All available stall reasons name and respective indexes will be stored in it.


## 6.6.2. Macros[#](https://docs.nvidia.com#macros)

## 6.6.3. Enumerations[#](https://docs.nvidia.com#enumerations)

[CUPTI::PcSamplingUtil::CUptiUtilResult](https://docs.nvidia.com#group__cupti__pcsampling__utility_1ga14b3e4f5bd78f1abf3b16884c7dfd755)CUPTI PC sampling utility API result codes.

[CUPTI::PcSamplingUtil::PcSamplingBufferType](https://docs.nvidia.com#group__cupti__pcsampling__utility_1ga1dc90a8b2a7ee09a0c230aa6256bba5e)CUPTI PC sampling buffer types.


## 6.6.4. Functions[#](https://docs.nvidia.com#functions)

- CUptiUtilResult
[CUPTI::PcSamplingUtil::CuptiUtilCloseFile](https://docs.nvidia.com#group__cupti__pcsampling__utility_1ga493512247a165cddc2793b376b1d30c1)(CUptiUtil_FileHandle fileHandle) Close a file handle opened by

[CuptiUtilOpenFile](https://docs.nvidia.com#group__cupti__pcsampling__utility_1ga7d0b234d2965d9ae3ad8b5945a7073f4).- CUptiUtilResult
[CUPTI::PcSamplingUtil::CuptiUtilGetBufferInfo](https://docs.nvidia.com#group__cupti__pcsampling__utility_1gae4c397f1c21a9baecdc74d38b1b783dd)(CUptiUtil_GetBufferInfoParams *pParams) Get buffer info data of file.

- CUptiUtilResult
[CUPTI::PcSamplingUtil::CuptiUtilGetHeaderData](https://docs.nvidia.com#group__cupti__pcsampling__utility_1ga873b630c7ec1a2ada140d2f03b6934c4)(CUptiUtil_GetHeaderDataParams *pParams) Get header data of file.

- CUptiUtilResult
[CUPTI::PcSamplingUtil::CuptiUtilGetPcSampData](https://docs.nvidia.com#group__cupti__pcsampling__utility_1ga454395b5da004e96767fa739178431ce)(CUptiUtil_GetPcSampDataParams *pParams) Retrieve PC sampling data from file into allocated buffer.

- CUptiUtilResult
[CUPTI::PcSamplingUtil::CuptiUtilMergePcSampData](https://docs.nvidia.com#group__cupti__pcsampling__utility_1ga4987e223c4132503d622f29ce5a9546e)(CUptiUtil_MergePcSampDataParams *pParams) Merge PC sampling data range id wise.

- CUptiUtilResult
[CUPTI::PcSamplingUtil::CuptiUtilOpenFile](https://docs.nvidia.com#group__cupti__pcsampling__utility_1ga7d0b234d2965d9ae3ad8b5945a7073f4)(const char *fileName, CUptiUtil_FileHandle *pFileHandle) Open a file for reading PC sampling data.

- CUptiUtilResult
[CUPTI::PcSamplingUtil::CuptiUtilPutPcSampData](https://docs.nvidia.com#group__cupti__pcsampling__utility_1gab58ca9a7592643aa51e93d938768d754)(CUptiUtil_PutPcSampDataParams *pParams) Dump PC sampling data into the file.


## 6.6.5. Typedefs[#](https://docs.nvidia.com#typedefs)

[CUPTI::PcSamplingUtil::CUptiUtil_FileHandle](https://docs.nvidia.com#group__cupti__pcsampling__utility_1ga28b4be4be7a01c6e3521dd72ae439785)Opaque file handle for PC sampling utility read APIs.


## 6.6.6. Macros[#](https://docs.nvidia.com#id1)

-
CUptiUtil_GetBufferInfoParamsSize
[#](https://docs.nvidia.com#c.CUptiUtil_GetBufferInfoParamsSize)

-
CUptiUtil_GetHeaderDataParamsSize
[#](https://docs.nvidia.com#c.CUptiUtil_GetHeaderDataParamsSize)

-
CUptiUtil_GetPcSampDataParamsSize
[#](https://docs.nvidia.com#c.CUptiUtil_GetPcSampDataParamsSize)

-
CUptiUtil_MergePcSampDataParamsSize
[#](https://docs.nvidia.com#c.CUptiUtil_MergePcSampDataParamsSize)

-
CUptiUtil_PutPcSampDataParamsSize
[#](https://docs.nvidia.com#c.CUptiUtil_PutPcSampDataParamsSize)

## 6.6.7. Enumerations[#](https://docs.nvidia.com#id2)

-
enum
[CUPTI](https://docs.nvidia.com/namespaceCUPTI.html#_CPPv45CUPTI)::[PcSamplingUtil](https://docs.nvidia.com/namespaceCUPTI_1_1PcSamplingUtil.html#_CPPv4N5CUPTI14PcSamplingUtilE)::CUptiUtilResult[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil15CUptiUtilResultE) CUPTI PC sampling utility API result codes.

Error and result codes returned by CUPTI PC sampling utility API.

*Values:*-
enumerator CUPTI_UTIL_SUCCESS
[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil15CUptiUtilResult18CUPTI_UTIL_SUCCESSE) No error.


-
enumerator CUPTI_UTIL_ERROR_INVALID_PARAMETER
[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil15CUptiUtilResult34CUPTI_UTIL_ERROR_INVALID_PARAMETERE) One or more of the parameters are invalid.


-
enumerator CUPTI_UTIL_ERROR_UNABLE_TO_CREATE_FILE
[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil15CUptiUtilResult38CUPTI_UTIL_ERROR_UNABLE_TO_CREATE_FILEE) Unable to create a new file.


-
enumerator CUPTI_UTIL_ERROR_UNABLE_TO_OPEN_FILE
[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil15CUptiUtilResult36CUPTI_UTIL_ERROR_UNABLE_TO_OPEN_FILEE) Unable to open a file.


-
enumerator CUPTI_UTIL_ERROR_READ_WRITE_OPERATION_FAILED
[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil15CUptiUtilResult44CUPTI_UTIL_ERROR_READ_WRITE_OPERATION_FAILEDE) Read or write operation failed.


-
enumerator CUPTI_UTIL_ERROR_FILE_HANDLE_CORRUPTED
[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil15CUptiUtilResult38CUPTI_UTIL_ERROR_FILE_HANDLE_CORRUPTEDE) Provided file handle is corrupted.


-
enumerator CUPTI_UTIL_ERROR_SEEK_OPERATION_FAILED
[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil15CUptiUtilResult38CUPTI_UTIL_ERROR_SEEK_OPERATION_FAILEDE) seek operation failed.


-
enumerator CUPTI_UTIL_ERROR_OUT_OF_MEMORY
[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil15CUptiUtilResult30CUPTI_UTIL_ERROR_OUT_OF_MEMORYE) Unable to allocate enough memory to perform the requested operation.


-
enumerator CUPTI_UTIL_ERROR_UNKNOWN
[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil15CUptiUtilResult24CUPTI_UTIL_ERROR_UNKNOWNE) An unknown internal error has occurred.


-
enumerator CUPTI_UTIL_ERROR_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil15CUptiUtilResult26CUPTI_UTIL_ERROR_FORCE_INTE)

-
enumerator CUPTI_UTIL_SUCCESS

-
enum
[CUPTI](https://docs.nvidia.com/namespaceCUPTI.html#_CPPv45CUPTI)::[PcSamplingUtil](https://docs.nvidia.com/namespaceCUPTI_1_1PcSamplingUtil.html#_CPPv4N5CUPTI14PcSamplingUtilE)::PcSamplingBufferType[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil20PcSamplingBufferTypeE) CUPTI PC sampling buffer types.

*Values:*-
enumerator PC_SAMPLING_BUFFER_INVALID
[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil20PcSamplingBufferType26PC_SAMPLING_BUFFER_INVALIDE) Invalid buffer type.


-
enumerator PC_SAMPLING_BUFFER_PC_TO_COUNTER_DATA
[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil20PcSamplingBufferType37PC_SAMPLING_BUFFER_PC_TO_COUNTER_DATAE) Refers to

[CUpti_PCSamplingData](https://docs.nvidia.com/structCUpti__PCSamplingData.html#structcupti__pcsamplingdata)buffer.

-
enumerator PC_SAMPLING_BUFFER_INVALID

## 6.6.8. Functions[#](https://docs.nvidia.com#id3)

-
[CUptiUtilResult](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil15CUptiUtilResultE)[CUPTI](https://docs.nvidia.com/namespaceCUPTI.html#_CPPv45CUPTI)::[PcSamplingUtil](https://docs.nvidia.com/namespaceCUPTI_1_1PcSamplingUtil.html#_CPPv4N5CUPTI14PcSamplingUtilE)::CuptiUtilCloseFile( ,[CUptiUtil_FileHandle](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil20CUptiUtil_FileHandleE)fileHandleClose a file handle opened by

[CuptiUtilOpenFile](https://docs.nvidia.com#group__cupti__pcsampling__utility_1ga7d0b234d2965d9ae3ad8b5945a7073f4).- Parameters:
**fileHandle**– The handle to close.- Return values:
**CUPTI_UTIL_SUCCESS**–**CUPTI_UTIL_ERROR_INVALID_PARAMETER**– if fileHandle is NULL.



[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil18CuptiUtilCloseFileE20CUptiUtil_FileHandle)

-
[CUptiUtilResult](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil15CUptiUtilResultE)[CUPTI](https://docs.nvidia.com/namespaceCUPTI.html#_CPPv45CUPTI)::[PcSamplingUtil](https://docs.nvidia.com/namespaceCUPTI_1_1PcSamplingUtil.html#_CPPv4N5CUPTI14PcSamplingUtilE)::CuptiUtilGetBufferInfo( ,[CUptiUtil_GetBufferInfoParams](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1CUptiUtil__GetBufferInfoParams.html#_CPPv4N5CUPTI14PcSamplingUtil29CUptiUtil_GetBufferInfoParamsE)*pParamsGet buffer info data of file.

This API must be called every time before calling CuptiUtilGetPcSampData API.

[BufferInfo](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1BufferInfo.html#structcupti_1_1pcsamplingutil_1_1bufferinfo)structure, it gives info about recordCount and stallReasonCount of every record in the buffer. This will help to allocate exact buffer to retrieve data into it.- Return values:
**CUPTI_UTIL_SUCCESS**–**CUPTI_UTIL_ERROR_INVALID_PARAMETER**– error out if either of pParam or fileHandle is NULL or param struct size is incorrect.**CUPTI_UTIL_ERROR_FILE_HANDLE_CORRUPTED**– file handle is not in good state to read data from file.**CUPTI_UTIL_ERROR_READ_WRITE_OPERATION_FAILED**– failed to read data from file.



[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil22CuptiUtilGetBufferInfoEP29CUptiUtil_GetBufferInfoParams)

-
[CUptiUtilResult](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil15CUptiUtilResultE)[CUPTI](https://docs.nvidia.com/namespaceCUPTI.html#_CPPv45CUPTI)::[PcSamplingUtil](https://docs.nvidia.com/namespaceCUPTI_1_1PcSamplingUtil.html#_CPPv4N5CUPTI14PcSamplingUtilE)::CuptiUtilGetHeaderData( ,[CUptiUtil_GetHeaderDataParams](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1CUptiUtil__GetHeaderDataParams.html#_CPPv4N5CUPTI14PcSamplingUtil29CUptiUtil_GetHeaderDataParamsE)*pParamsGet header data of file.

This API must be called once initially while retrieving data from file.

[Header](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1Header.html#structcupti_1_1pcsamplingutil_1_1header)structure, it gives info about total number of buffers present in the file.- Return values:
**CUPTI_UTIL_SUCCESS**–**CUPTI_UTIL_ERROR_INVALID_PARAMETER**– error out if either of pParam or fileHandle is NULL or param struct size is incorrect.**CUPTI_UTIL_ERROR_FILE_HANDLE_CORRUPTED**– file handle is not in good state to read data from file**CUPTI_UTIL_ERROR_READ_WRITE_OPERATION_FAILED**– failed to read data from file.



[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil22CuptiUtilGetHeaderDataEP29CUptiUtil_GetHeaderDataParams)

-
[CUptiUtilResult](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil15CUptiUtilResultE)[CUPTI](https://docs.nvidia.com/namespaceCUPTI.html#_CPPv45CUPTI)::[PcSamplingUtil](https://docs.nvidia.com/namespaceCUPTI_1_1PcSamplingUtil.html#_CPPv4N5CUPTI14PcSamplingUtilE)::CuptiUtilGetPcSampData( ,[CUptiUtil_GetPcSampDataParams](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1CUptiUtil__GetPcSampDataParams.html#_CPPv4N5CUPTI14PcSamplingUtil29CUptiUtil_GetPcSampDataParamsE)*pParamsRetrieve PC sampling data from file into allocated buffer.

This API must be called after CuptiUtilGetBufferInfo API. It will retrieve data from file into allocated buffer.

- Return values:
**CUPTI_UTIL_SUCCESS**–**CUPTI_UTIL_ERROR_INVALID_PARAMETER**– error out if buffer type is invalid or if either of pSampData, pParams is NULL. If pPcSamplingStallReasons is not NULL then error out if either of stallReasonIndex, stallReasons or stallReasons array element pointer is NULL. or filename is empty.**CUPTI_UTIL_ERROR_READ_WRITE_OPERATION_FAILED**–**CUPTI_UTIL_ERROR_FILE_HANDLE_CORRUPTED**– file handle is not in good state to read data from file.



[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil22CuptiUtilGetPcSampDataEP29CUptiUtil_GetPcSampDataParams)

-
[CUptiUtilResult](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil15CUptiUtilResultE)[CUPTI](https://docs.nvidia.com/namespaceCUPTI.html#_CPPv45CUPTI)::[PcSamplingUtil](https://docs.nvidia.com/namespaceCUPTI_1_1PcSamplingUtil.html#_CPPv4N5CUPTI14PcSamplingUtilE)::CuptiUtilMergePcSampData( ,[CUptiUtil_MergePcSampDataParams](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1CUptiUtil__MergePcSampDataParams.html#_CPPv4N5CUPTI14PcSamplingUtil31CUptiUtil_MergePcSampDataParamsE)*pParamsMerge PC sampling data range id wise.

This API merge PC sampling data range id wise. It allocates memory for merged data and fill data in it and provide buffer pointer in MergedPcSampDataBuffers field. It is expected from user to free merge data buffers after use.

- Return values:
**CUPTI_UTIL_SUCCESS**–**CUPTI_UTIL_ERROR_INVALID_PARAMETER**– error out if param struct size is invalid or count of buffers to merge is invalid i.e less than 1 or either of PcSampDataBuffer, MergedPcSampDataBuffers, numMergedBuffer is NULL**CUPTI_UTIL_ERROR_OUT_OF_MEMORY**– Unable to allocate memory for merged buffer.



[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil24CuptiUtilMergePcSampDataEP31CUptiUtil_MergePcSampDataParams)

-
[CUptiUtilResult](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil15CUptiUtilResultE)[CUPTI](https://docs.nvidia.com/namespaceCUPTI.html#_CPPv45CUPTI)::[PcSamplingUtil](https://docs.nvidia.com/namespaceCUPTI_1_1PcSamplingUtil.html#_CPPv4N5CUPTI14PcSamplingUtilE)::CuptiUtilOpenFile( *const char *fileName*,,[CUptiUtil_FileHandle](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil20CUptiUtil_FileHandleE)*pFileHandleOpen a file for reading PC sampling data.

Opens the file in binary read mode. The returned handle must be passed to the Get* APIs and eventually closed with

[CuptiUtilCloseFile](https://docs.nvidia.com#group__cupti__pcsampling__utility_1ga493512247a165cddc2793b376b1d30c1). All file I/O occurs inside the library, avoiding Windows CRT boundary issues with FILE*.- Parameters:
**fileName**– Path to the .dat file to read.**pFileHandle**– Receives the opaque file handle on success.

- Return values:
**CUPTI_UTIL_SUCCESS**–**CUPTI_UTIL_ERROR_INVALID_PARAMETER**– if fileName or pFileHandle is NULL.**CUPTI_UTIL_ERROR_UNABLE_TO_OPEN_FILE**– if the file cannot be opened.



[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil17CuptiUtilOpenFileEPKcP20CUptiUtil_FileHandle)

-
[CUptiUtilResult](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil15CUptiUtilResultE)[CUPTI](https://docs.nvidia.com/namespaceCUPTI.html#_CPPv45CUPTI)::[PcSamplingUtil](https://docs.nvidia.com/namespaceCUPTI_1_1PcSamplingUtil.html#_CPPv4N5CUPTI14PcSamplingUtilE)::CuptiUtilPutPcSampData( ,[CUptiUtil_PutPcSampDataParams](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1CUptiUtil__PutPcSampDataParams.html#_CPPv4N5CUPTI14PcSamplingUtil29CUptiUtil_PutPcSampDataParamsE)*pParamsDump PC sampling data into the file.

This API can be called multiple times. It will append buffer in the file. For every buffer it will store

[BufferInfo](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1BufferInfo.html#structcupti_1_1pcsamplingutil_1_1bufferinfo)so that before retrieving data it will help to allocate buffer to store retrieved data. This API creates file if file does not present. If stallReasonIndex or stallReasons pointer of[CUptiUtil_PutPcSampDataParams](https://docs.nvidia.com/structCUPTI_1_1PcSamplingUtil_1_1CUptiUtil__PutPcSampDataParams.html#structcupti_1_1pcsamplingutil_1_1cuptiutil__putpcsampdataparams)is NULL then stall reasons data will not be stored in file. It is expected to store all available stall reason data at least once to refer it during offline correlation.- Return values:
**CUPTI_UTIL_SUCCESS**–**CUPTI_UTIL_ERROR_INVALID_PARAMETER**– error out if buffer type is invalid or if either of pSamplingData, pParams pointer is NULL or stall reason configuration details not provided or filename is empty.**CUPTI_UTIL_ERROR_UNABLE_TO_CREATE_FILE**–**CUPTI_UTIL_ERROR_UNABLE_TO_OPEN_FILE**–**CUPTI_UTIL_ERROR_READ_WRITE_OPERATION_FAILED**–



[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil22CuptiUtilPutPcSampDataEP29CUptiUtil_PutPcSampDataParams)

## 6.6.9. Typedefs[#](https://docs.nvidia.com#id4)

-
typedef void *
[CUPTI](https://docs.nvidia.com/namespaceCUPTI.html#_CPPv45CUPTI)::[PcSamplingUtil](https://docs.nvidia.com/namespaceCUPTI_1_1PcSamplingUtil.html#_CPPv4N5CUPTI14PcSamplingUtilE)::CUptiUtil_FileHandle[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil20CUptiUtil_FileHandleE) Opaque file handle for PC sampling utility read APIs.

Returned by

[CuptiUtilOpenFile](https://docs.nvidia.com#group__cupti__pcsampling__utility_1ga7d0b234d2965d9ae3ad8b5945a7073f4)and consumed by the Get* APIs. Must be closed with[CuptiUtilCloseFile](https://docs.nvidia.com#group__cupti__pcsampling__utility_1ga493512247a165cddc2793b376b1d30c1)when done. Using an opaque handle ensures all file I/O stays within the library, which is required on Windows where FILE* cannot be shared across DLL boundaries.