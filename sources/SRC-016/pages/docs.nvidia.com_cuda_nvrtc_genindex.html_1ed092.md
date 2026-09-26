source: https://docs.nvidia.com/cuda/nvrtc/genindex.html

1. Introduction
2. Getting Started
3. User Interface
4. Language
5. Basic Usage
6. Precompiled Headers (CUDA 12.8+)
7. Tile Programming (CUDA 13.3+)
8. Accessing Lowered Names
9. Interfacing With Template Host Code
10. Versioning Scheme
11. Caching (CUDA 12.9+)
12. Bundled Headers (CUDA 13.3+)
13. Miscellaneous Notes
14. Example: SAXPY
15. Example: Using Lowered Name
16. Example: Using nvrtcGetTypeName
17. Example: Dynamic Parallelism
18. Example: Device LTO (link time optimization)
19. Example: Automatic PCH (CUDA 12.8+)
20. Example: Explicit PCH Create/Use (CUDA 12.8+)
21. Example: PCH Heap Resizing (CUDA 12.8+)
22. Example: Tile compilation (CUDA 13.3+)
23. Example: Bundled Headers (CUDA 13.3+)
NVRTC
»
Index
v13.4 |
PDF
|
Archive
Index
N
N
NVRTC_INSTALL_HEADERS_FORCE_OVERWRITE (C macro)
NVRTC_INSTALL_HEADERS_NO_WAIT (C macro)
NVRTC_INSTALL_HEADERS_SKIP_IF_EXISTS (C macro)
nvrtcAddNameExpression (C++ function)
nvrtcBundledHeadersInfo (C++ struct)
nvrtcBundledHeadersInfo::available (C++ member)
nvrtcBundledHeadersInfo::compressedSize (C++ member)
nvrtcBundledHeadersInfo::cudaVersionMajor (C++ member)
nvrtcBundledHeadersInfo::cudaVersionMinor (C++ member)
nvrtcBundledHeadersInfo::numFiles (C++ member)
nvrtcBundledHeadersInfo::uncompressedSize (C++ member)
nvrtcCompileProgram (C++ function)
nvrtcCreateProgram (C++ function)
nvrtcDestroyProgram (C++ function)
nvrtcGetBundledHeadersInfo (C++ function)
nvrtcGetCUBIN (C++ function)
nvrtcGetCUBINSize (C++ function)
nvrtcGetErrorString (C++ function)
nvrtcGetLoweredName (C++ function)
nvrtcGetLTOIR (C++ function)
nvrtcGetLTOIRSize (C++ function)
nvrtcGetNumSupportedArchs (C++ function)
nvrtcGetOptiXIR (C++ function)
nvrtcGetOptiXIRSize (C++ function)
nvrtcGetPCHCreateStatus (C++ function)
nvrtcGetPCHHeapSize (C++ function)
nvrtcGetPCHHeapSizeRequired (C++ function)
nvrtcGetProgramLog (C++ function)
nvrtcGetProgramLogSize (C++ function)
nvrtcGetPTX (C++ function)
nvrtcGetPTXSize (C++ function)
nvrtcGetSupportedArchs (C++ function)
nvrtcGetTileIR (C++ function)
nvrtcGetTileIRSize (C++ function)
nvrtcGetTypeName (C++ function)
,
[1]
nvrtcInstallBundledHeaders (C++ function)
nvrtcProgram (C++ type)
nvrtcRemoveBundledHeaders (C++ function)
nvrtcResult (C++ enum)
nvrtcResult::NVRTC_ERROR_BUILTIN_OPERATION_FAILURE (C++ enumerator)
nvrtcResult::NVRTC_ERROR_BUSY (C++ enumerator)
nvrtcResult::NVRTC_ERROR_CANCELLED (C++ enumerator)
nvrtcResult::NVRTC_ERROR_COMPILATION (C++ enumerator)
nvrtcResult::NVRTC_ERROR_INTERNAL_ERROR (C++ enumerator)
nvrtcResult::NVRTC_ERROR_INVALID_INPUT (C++ enumerator)
nvrtcResult::NVRTC_ERROR_INVALID_OPTION (C++ enumerator)
nvrtcResult::NVRTC_ERROR_INVALID_PROGRAM (C++ enumerator)
nvrtcResult::NVRTC_ERROR_NAME_EXPRESSION_NOT_VALID (C++ enumerator)
nvrtcResult::NVRTC_ERROR_NO_LOWERED_NAMES_BEFORE_COMPILATION (C++ enumerator)
nvrtcResult::NVRTC_ERROR_NO_NAME_EXPRESSIONS_AFTER_COMPILATION (C++ enumerator)
nvrtcResult::NVRTC_ERROR_NO_PCH_CREATE_ATTEMPTED (C++ enumerator)
nvrtcResult::NVRTC_ERROR_OUT_OF_MEMORY (C++ enumerator)
nvrtcResult::NVRTC_ERROR_PCH_CREATE (C++ enumerator)
nvrtcResult::NVRTC_ERROR_PCH_CREATE_HEAP_EXHAUSTED (C++ enumerator)
nvrtcResult::NVRTC_ERROR_PROGRAM_CREATION_FAILURE (C++ enumerator)
nvrtcResult::NVRTC_ERROR_TIME_FILE_WRITE_FAILED (C++ enumerator)
nvrtcResult::NVRTC_ERROR_TIME_TRACE_FILE_WRITE_FAILED (C++ enumerator)
nvrtcResult::NVRTC_SUCCESS (C++ enumerator)
nvrtcSetFlowCallback (C++ function)
nvrtcSetPCHHeapSize (C++ function)
nvrtcVersion (C++ function)