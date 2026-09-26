source: https://docs.nvidia.com/cuda/cuda-runtime-api/cuda_runtime_api/deprecated.html

#
8. Deprecated List[](https://docs.nvidia.com#deprecated-list)

-
Member
[cudaD3D10GetDirect3DDevice](https://docs.nvidia.com/group__CUDART__D3D10__DEPRECATED.html#group__cudart__d3d10__deprecated_1ga3f5496b011b2d9dfa9c87d64d5d1d328)(ID3D10Device **ppD3D10Device) -
This function is deprecated as of CUDA 5.0.


-
Member
[cudaD3D10MapResources](https://docs.nvidia.com/group__CUDART__D3D10__DEPRECATED.html#group__cudart__d3d10__deprecated_1ga6c4e7c5d77b0adf3882649cfe97d6790)(int count, ID3D10Resource **ppResources) -
This function is deprecated as of CUDA 3.0.


-
Member
[cudaD3D10RegisterResource](https://docs.nvidia.com/group__CUDART__D3D10__DEPRECATED.html#group__cudart__d3d10__deprecated_1ga81b2fa93f0cbff5d4d9d56732d81822d)(ID3D10Resource *pResource, unsigned int flags) -
This function is deprecated as of CUDA 3.0.


-
Member
[cudaD3D10ResourceGetMappedArray](https://docs.nvidia.com/group__CUDART__D3D10__DEPRECATED.html#group__cudart__d3d10__deprecated_1gab1ebb3509c791bb05c7beae9578223d9)(cudaArray **ppArray, ID3D10Resource *pResource, unsigned int subResource) -
This function is deprecated as of CUDA 3.0.


-
Member
[cudaD3D10ResourceGetMappedPitch](https://docs.nvidia.com/group__CUDART__D3D10__DEPRECATED.html#group__cudart__d3d10__deprecated_1gafdba3211473c1d6a678ead30a6942006)(size_t *pPitch, size_t *pPitchSlice, ID3D10Resource *pResource, unsigned int subResource) -
This function is deprecated as of CUDA 3.0.


-
Member
[cudaD3D10ResourceGetMappedPointer](https://docs.nvidia.com/group__CUDART__D3D10__DEPRECATED.html#group__cudart__d3d10__deprecated_1ga45bdf8d41c3df33aa08acaa6bd3b9d84)(void **pPointer, ID3D10Resource *pResource, unsigned int subResource) -
This function is deprecated as of CUDA 3.0.


-
Member
[cudaD3D10ResourceGetMappedSize](https://docs.nvidia.com/group__CUDART__D3D10__DEPRECATED.html#group__cudart__d3d10__deprecated_1ga5b0aa4e2f3d028f61990a5ebf6604078)(size_t *pSize, ID3D10Resource *pResource, unsigned int subResource) -
This function is deprecated as of CUDA 3.0.


-
Member
[cudaD3D10ResourceGetSurfaceDimensions](https://docs.nvidia.com/group__CUDART__D3D10__DEPRECATED.html#group__cudart__d3d10__deprecated_1ga3fc002b954b6d54414049bb29d443ef3)(size_t *pWidth, size_t *pHeight, size_t *pDepth, ID3D10Resource *pResource, unsigned int subResource) -
This function is deprecated as of CUDA 3.0.


-
Member
[cudaD3D10ResourceSetMapFlags](https://docs.nvidia.com/group__CUDART__D3D10__DEPRECATED.html#group__cudart__d3d10__deprecated_1ga71aaf00e14396d8948d12cd9d4ed68c5)(ID3D10Resource *pResource, unsigned int flags) -
This function is deprecated as of CUDA 3.0.


-
Member
[cudaD3D10SetDirect3DDevice](https://docs.nvidia.com/group__CUDART__D3D10__DEPRECATED.html#group__cudart__d3d10__deprecated_1gaec213424a812636fc03d48442caacea2)(ID3D10Device *pD3D10Device, int device=-1) -
This function is deprecated as of CUDA 5.0.


-
Member
[cudaD3D10UnmapResources](https://docs.nvidia.com/group__CUDART__D3D10__DEPRECATED.html#group__cudart__d3d10__deprecated_1ga5c7ede2f5a346bf0258f3f70061494de)(int count, ID3D10Resource **ppResources) -
This function is deprecated as of CUDA 3.0.


-
Member
[cudaD3D10UnregisterResource](https://docs.nvidia.com/group__CUDART__D3D10__DEPRECATED.html#group__cudart__d3d10__deprecated_1ga6783f43ed84f756ab40ccf16df561667)(ID3D10Resource *pResource) -
This function is deprecated as of CUDA 3.0.


-
Member
[cudaD3D11GetDirect3DDevice](https://docs.nvidia.com/group__CUDART__D3D11__DEPRECATED.html#group__cudart__d3d11__deprecated_1ga6d2eb041986f887ae8ae85ce3f7431fa)(ID3D11Device **ppD3D11Device) -
This function is deprecated as of CUDA 5.0.


-
Member
[cudaD3D11SetDirect3DDevice](https://docs.nvidia.com/group__CUDART__D3D11__DEPRECATED.html#group__cudart__d3d11__deprecated_1ga1d65c1bdcbdd4d0d70e8c9c8a32f38ff)(ID3D11Device *pD3D11Device, int device=-1) -
This function is deprecated as of CUDA 5.0.


-
Member
[cudaD3D9MapResources](https://docs.nvidia.com/group__CUDART__D3D9__DEPRECATED.html#group__cudart__d3d9__deprecated_1ga693b8fef0e3161e63b17f1fa633371a9)(int count, IDirect3DResource9 **ppResources) -
This function is deprecated as of CUDA 3.0.


-
Member
[cudaD3D9RegisterResource](https://docs.nvidia.com/group__CUDART__D3D9__DEPRECATED.html#group__cudart__d3d9__deprecated_1ga81b436ab21219ad7192f2d1d1331a365)(IDirect3DResource9 *pResource, unsigned int flags) -
This function is deprecated as of CUDA 3.0.


-
Member
[cudaD3D9ResourceGetMappedArray](https://docs.nvidia.com/group__CUDART__D3D9__DEPRECATED.html#group__cudart__d3d9__deprecated_1ga96612ee88bdc6d2b13a93108b4838e07)(cudaArray **ppArray, IDirect3DResource9 *pResource, unsigned int face, unsigned int level) -
This function is deprecated as of CUDA 3.0.


-
Member
[cudaD3D9ResourceGetMappedPitch](https://docs.nvidia.com/group__CUDART__D3D9__DEPRECATED.html#group__cudart__d3d9__deprecated_1ga327770001905b9fc6982024520245f72)(size_t *pPitch, size_t *pPitchSlice, IDirect3DResource9 *pResource, unsigned int face, unsigned int level) -
This function is deprecated as of CUDA 3.0.


-
Member
[cudaD3D9ResourceGetMappedPointer](https://docs.nvidia.com/group__CUDART__D3D9__DEPRECATED.html#group__cudart__d3d9__deprecated_1ga1980005bc217f83df499271e73b020df)(void **pPointer, IDirect3DResource9 *pResource, unsigned int face, unsigned int level) -
This function is deprecated as of CUDA 3.0.


-
Member
[cudaD3D9ResourceGetMappedSize](https://docs.nvidia.com/group__CUDART__D3D9__DEPRECATED.html#group__cudart__d3d9__deprecated_1ga61dcf9921a5d23a468d72a99c7fa7194)(size_t *pSize, IDirect3DResource9 *pResource, unsigned int face, unsigned int level) -
This function is deprecated as of CUDA 3.0.


-
Member
[cudaD3D9ResourceGetSurfaceDimensions](https://docs.nvidia.com/group__CUDART__D3D9__DEPRECATED.html#group__cudart__d3d9__deprecated_1ga21d52468018d78c15443c6afd873a312)(size_t *pWidth, size_t *pHeight, size_t *pDepth, IDirect3DResource9 *pResource, unsigned int face, unsigned int level) -
This function is deprecated as of CUDA 3.0.


-
Member
[cudaD3D9ResourceSetMapFlags](https://docs.nvidia.com/group__CUDART__D3D9__DEPRECATED.html#group__cudart__d3d9__deprecated_1gacd74eba2410e0d348864406a123e64bf)(IDirect3DResource9 *pResource, unsigned int flags) -
This function is deprecated as of CUDA 3.0.


-
Member
[cudaD3D9UnmapResources](https://docs.nvidia.com/group__CUDART__D3D9__DEPRECATED.html#group__cudart__d3d9__deprecated_1gae90f331435ae737057add0a618bc9b4d)(int count, IDirect3DResource9 **ppResources) -
This function is deprecated as of CUDA 3.0.


-
Member
[cudaD3D9UnregisterResource](https://docs.nvidia.com/group__CUDART__D3D9__DEPRECATED.html#group__cudart__d3d9__deprecated_1gac26c53ea7f8af2ffe4b23b8e479b5b93)(IDirect3DResource9 *pResource) -
This function is deprecated as of CUDA 3.0.


-
Member
[cudaDeviceBlockingSync](https://docs.nvidia.com/group__CUDART__TYPES.html#group__cudart__types_1ga130ddae663f1873258fee5a6e0808b71) -
This flag was deprecated as of CUDA 4.0 and replaced with

[cudaDeviceScheduleBlockingSync](https://docs.nvidia.com/group__CUDART__TYPES.html#group__cudart__types_1ga057e6912c52708b6aa86e79dd83d007c).

-
Member
[cudaDeviceGetSharedMemConfig](https://docs.nvidia.com/group__CUDART__DEVICE__DEPRECATED.html#group__cudart__device__deprecated_1gafb2038893286a743347dada716bab162)(enum cudaSharedMemConfig *pConfig) -

-
Member
[cudaDeviceSetSharedMemConfig](https://docs.nvidia.com/group__CUDART__DEVICE__DEPRECATED.html#group__cudart__device__deprecated_1gaa4f3f8a422968f9524012f43ba852058)(enum cudaSharedMemConfig config) -

-
Member
[cudaErrorAddressOfConstant](https://docs.nvidia.com/group__CUDART__TYPES.html#group__cudart__types_1gga3f51e3575c2178246db0a94a430e0038ae440746034e7e19674247be7880e42e2) -
This error return is deprecated as of CUDA 3.1. Variables in constant memory may now have their address taken by the runtime via

[cudaGetSymbolAddress()](https://docs.nvidia.com/group__CUDART__MEMORY.html#group__cudart__memory_1ga4f513be54d3794667c2017146b3d6a2b).

-
Member
[cudaErrorInvalidDevicePointer](https://docs.nvidia.com/group__CUDART__TYPES.html#group__cudart__types_1gga3f51e3575c2178246db0a94a430e0038a5fa2f00ab72ab5cf649a0a32351a20bf) -
This error return is deprecated as of CUDA 10.1.


-
Member
[cudaErrorInvalidHostPointer](https://docs.nvidia.com/group__CUDART__TYPES.html#group__cudart__types_1gga3f51e3575c2178246db0a94a430e0038a6b9b87743cdcc5c5de484d96be0bb620) -
This error return is deprecated as of CUDA 10.1.


-
Member
[cudaErrorMemoryValueTooLarge](https://docs.nvidia.com/group__CUDART__TYPES.html#group__cudart__types_1gga3f51e3575c2178246db0a94a430e0038a41fc5a27bf4a65ef07a19d362a9ad0aa) -
This error return is deprecated as of CUDA 3.1. Device emulation mode was removed with the CUDA 3.1 release.


-
Member
[cudaErrorMixedDeviceExecution](https://docs.nvidia.com/group__CUDART__TYPES.html#group__cudart__types_1gga3f51e3575c2178246db0a94a430e0038ae225ea8a6a6b0737b4b270dee133449f) -
This error return is deprecated as of CUDA 3.1. Device emulation mode was removed with the CUDA 3.1 release.


-
Member
[cudaErrorNotYetImplemented](https://docs.nvidia.com/group__CUDART__TYPES.html#group__cudart__types_1gga3f51e3575c2178246db0a94a430e0038a8da8b90f795d15525477cc5e7438bf62) -
This error return is deprecated as of CUDA 4.1.


-
Member
[cudaErrorPriorLaunchFailure](https://docs.nvidia.com/group__CUDART__TYPES.html#group__cudart__types_1gga3f51e3575c2178246db0a94a430e0038ac14f1bebf1cd5d2e44cdfd27e15025e5) -
This error return is deprecated as of CUDA 3.1. Device emulation mode was removed with the CUDA 3.1 release.


-
Member
[cudaErrorProfilerAlreadyStarted](https://docs.nvidia.com/group__CUDART__TYPES.html#group__cudart__types_1gga3f51e3575c2178246db0a94a430e0038abfd977ba87fbe3bd18bf6cb73d4185c2) -
This error return is deprecated as of CUDA 5.0. It is no longer an error to call

[cudaProfilerStart()](https://docs.nvidia.com/group__CUDART__PROFILER.html#group__cudart__profiler_1gaf536d75bb382356e10e3b4e89f4a5374)when profiling is already enabled.

-
Member
[cudaErrorProfilerAlreadyStopped](https://docs.nvidia.com/group__CUDART__TYPES.html#group__cudart__types_1gga3f51e3575c2178246db0a94a430e0038a878c9676e574916a80c621d2637d3311) -
This error return is deprecated as of CUDA 5.0. It is no longer an error to call

[cudaProfilerStop()](https://docs.nvidia.com/group__CUDART__PROFILER.html#group__cudart__profiler_1ga826922d9d1d0090d4a9a6b8b249cebb5)when profiling is already disabled.

-
Member
[cudaErrorProfilerNotInitialized](https://docs.nvidia.com/group__CUDART__TYPES.html#group__cudart__types_1gga3f51e3575c2178246db0a94a430e0038ad8234a288b0a7a8f77a2b6dbd0e8ecb0) -
This error return is deprecated as of CUDA 5.0. It is no longer an error to attempt to enable/disable the profiling via

[cudaProfilerStart](https://docs.nvidia.com/group__CUDART__PROFILER.html#group__cudart__profiler_1gaf536d75bb382356e10e3b4e89f4a5374)or[cudaProfilerStop](https://docs.nvidia.com/group__CUDART__PROFILER.html#group__cudart__profiler_1ga826922d9d1d0090d4a9a6b8b249cebb5)without initialization.

-
Member
[cudaErrorSynchronizationError](https://docs.nvidia.com/group__CUDART__TYPES.html#group__cudart__types_1gga3f51e3575c2178246db0a94a430e0038a2ad9b297541678f164fdecc3f719a4d0) -
This error return is deprecated as of CUDA 3.1. Device emulation mode was removed with the CUDA 3.1 release.


-
Member
[cudaErrorTextureFetchFailed](https://docs.nvidia.com/group__CUDART__TYPES.html#group__cudart__types_1gga3f51e3575c2178246db0a94a430e0038a4eb0c109c8229cecd97abe27959e6376) -
This error return is deprecated as of CUDA 3.1. Device emulation mode was removed with the CUDA 3.1 release.


-
Member
[cudaErrorTextureNotBound](https://docs.nvidia.com/group__CUDART__TYPES.html#group__cudart__types_1gga3f51e3575c2178246db0a94a430e0038af0cc6c30c64f4a9c5f663e99a77d99ba) -
This error return is deprecated as of CUDA 3.1. Device emulation mode was removed with the CUDA 3.1 release.


-
Member
[cudaFuncSetSharedMemConfig](https://docs.nvidia.com/group__CUDART__EXECUTION__DEPRECATED.html#group__cudart__execution__deprecated_1ga3ef735b45b7549e936a60cb084740754)(const void *func, enum cudaSharedMemConfig config) -

-
Member
[cudaGetDriverEntryPoint](https://docs.nvidia.com/group__CUDART__DRIVER__ENTRY__POINT.html#group__cudart__driver__entry__point_1gacf55d143722ccfa9252758181701c876)(const char *symbol, void **funcPtr, unsigned long long flags, enum cudaDriverEntryPointQueryResult *driverStatus=NULL) -
This function is deprecated as of CUDA 13.0


-
Member
[cudaGLMapBufferObject](https://docs.nvidia.com/group__CUDART__OPENGL__DEPRECATED.html#group__cudart__opengl__deprecated_1ga8ec08e48a4d3c657f5cc180451cce7a9)(void **devPtr, GLuint bufObj) -
This function is deprecated as of CUDA 3.0.


-
Member
[cudaGLMapBufferObjectAsync](https://docs.nvidia.com/group__CUDART__OPENGL__DEPRECATED.html#group__cudart__opengl__deprecated_1gae4b2b7979ed1f39c4d930cd86b55420f)(void **devPtr, GLuint bufObj, cudaStream_t stream) -
This function is deprecated as of CUDA 3.0.


-
Member
[cudaGLRegisterBufferObject](https://docs.nvidia.com/group__CUDART__OPENGL__DEPRECATED.html#group__cudart__opengl__deprecated_1gab835a92a340e999f4eaa55a8d57e122c)(GLuint bufObj) -
This function is deprecated as of CUDA 3.0.


-
Member
[cudaGLSetBufferObjectMapFlags](https://docs.nvidia.com/group__CUDART__OPENGL__DEPRECATED.html#group__cudart__opengl__deprecated_1ga28bea930ea5e8e8d717da5ee25bcdc12)(GLuint bufObj, unsigned int flags) -
This function is deprecated as of CUDA 3.0.


-
Member
[cudaGLSetGLDevice](https://docs.nvidia.com/group__CUDART__OPENGL__DEPRECATED.html#group__cudart__opengl__deprecated_1gaee537bf3ac1b9eee5e5da46cf6316ac5)(int device) -
This function is deprecated as of CUDA 5.0.


-
Member
[cudaGLUnmapBufferObject](https://docs.nvidia.com/group__CUDART__OPENGL__DEPRECATED.html#group__cudart__opengl__deprecated_1ga5ce0566e8543a8c7677b619acfefd5b5)(GLuint bufObj) -
This function is deprecated as of CUDA 3.0.


-
Member
[cudaGLUnmapBufferObjectAsync](https://docs.nvidia.com/group__CUDART__OPENGL__DEPRECATED.html#group__cudart__opengl__deprecated_1gad5492a8f632d8b0f3026c10ba21e56d0)(GLuint bufObj, cudaStream_t stream) -
This function is deprecated as of CUDA 3.0.


-
Member
[cudaGLUnregisterBufferObject](https://docs.nvidia.com/group__CUDART__OPENGL__DEPRECATED.html#group__cudart__opengl__deprecated_1ga088f95cd5d5e8b5f4caec8f4d2f92570)(GLuint bufObj) -
This function is deprecated as of CUDA 3.0.


-
Member
[cudaMemcpyArrayToArray](https://docs.nvidia.com/group__CUDART__MEMORY__DEPRECATED.html#group__cudart__memory__deprecated_1ga6e34301a5842491b01404e36da840af7)(cudaArray_t dst, size_t wOffsetDst, size_t hOffsetDst, cudaArray_const_t src, size_t wOffsetSrc, size_t hOffsetSrc, size_t count, enum cudaMemcpyKind kind=cudaMemcpyDeviceToDevice) -

-
Member
[cudaMemcpyFromArray](https://docs.nvidia.com/group__CUDART__MEMORY__DEPRECATED.html#group__cudart__memory__deprecated_1gaade51067f967d3a394533515524fe3fa)(void *dst, cudaArray_const_t src, size_t wOffset, size_t hOffset, size_t count, enum cudaMemcpyKind kind) -

-
Member
[cudaMemcpyFromArrayAsync](https://docs.nvidia.com/group__CUDART__MEMORY__DEPRECATED.html#group__cudart__memory__deprecated_1ga17605b3b9f7512592d492ddabee4bcbf)(void *dst, cudaArray_const_t src, size_t wOffset, size_t hOffset, size_t count, enum cudaMemcpyKind kind, cudaStream_t stream=0) -

-
Member
[cudaMemcpyToArray](https://docs.nvidia.com/group__CUDART__MEMORY__DEPRECATED.html#group__cudart__memory__deprecated_1gacc65e278074cfe8f06aaa25788b7dc25)(cudaArray_t dst, size_t wOffset, size_t hOffset, const void *src, size_t count, enum cudaMemcpyKind kind) -

-
Member
[cudaMemcpyToArrayAsync](https://docs.nvidia.com/group__CUDART__MEMORY__DEPRECATED.html#group__cudart__memory__deprecated_1ga0ab54cd45f0dcd26c9a46c4b0b7fff9b)(cudaArray_t dst, size_t wOffset, size_t hOffset, const void *src, size_t count, enum cudaMemcpyKind kind, cudaStream_t stream=0) -

-
Member
[cudaSharedMemConfig](https://docs.nvidia.com/group__CUDART__TYPES.html#group__cudart__types_1ga6e62d15f3c224625e8c9aa946f1709a6) -