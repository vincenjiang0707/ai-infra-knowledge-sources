source: https://docs.nvidia.com/cuda/cuda-driver-api/cuda_driver_api/deprecated.html

#
8. Deprecated List[](https://docs.nvidia.com#deprecated-list)

-
Member
[CU_CTX_BLOCKING_SYNC](https://docs.nvidia.com/group__CUDA__TYPES.html#group__cuda__types_1gga9f889e28a45a295b5c8ce13aa05f6cd4ab5bf395cc60a8cbded4c329ae9430b91) -
This flag was deprecated as of CUDA 4.0 and was replaced with

[CU_CTX_SCHED_BLOCKING_SYNC](https://docs.nvidia.com/group__CUDA__TYPES.html#group__cuda__types_1gga9f889e28a45a295b5c8ce13aa05f6cd4a62aebfe6432ade3feb32f1a409027852).

-
Member
[CU_CTX_MAP_HOST](https://docs.nvidia.com/group__CUDA__TYPES.html#group__cuda__types_1gga9f889e28a45a295b5c8ce13aa05f6cd4a08c822db270f4322af6e6bb0a7786514) -
This flag was deprecated as of CUDA 11.0 and it no longer has any effect. All contexts as of CUDA 3.2 behave as though the flag is enabled.


-
Member
[CU_DEVICE_P2P_ATTRIBUTE_ACCESS_ACCESS_SUPPORTED](https://docs.nvidia.com/group__CUDA__TYPES.html#group__cuda__types_1gga578d7cf687ce20f7e99468e8c14e22dea07a4ae30f555b208dcb2065320c9e2e1) -
use CU_DEVICE_P2P_ATTRIBUTE_CUDA_ARRAY_ACCESS_SUPPORTED instead


-
Member
[CU_JIT_FMA](https://docs.nvidia.com/group__CUDA__TYPES.html#group__cuda__types_1gga5527fa8030d5cabedc781a04dbd1997da46035377c25603cc13fba201de2d811e) -
Enable/Disable the contraction of floating-point multiplies and adds/subtracts into floating-point multiply-add (-fma) operations (1: Enable, default; 0: Disable). Option type: int Applies to: link-time optimization specified with CU_JIT_LTO


-
Member
[CU_JIT_FTZ](https://docs.nvidia.com/group__CUDA__TYPES.html#group__cuda__types_1gga5527fa8030d5cabedc781a04dbd1997daf795815997b847691ea359224674d123) -
Control single-precision denormals (-ftz) support (0: false, default). 1 : flushes denormal values to zero 0 : preserves denormal values Option type: int Applies to: link-time optimization specified with CU_JIT_LTO


-
Member
[CU_JIT_INPUT_NVVM](https://docs.nvidia.com/group__CUDA__TYPES.html#group__cuda__types_1ggac78e5cb421c428676861189048888958a89597124c00247ef55cd93d9bd9c58b8) -
High-level intermediate code for link-time optimization Applicable options: NVVM compiler options, PTX compiler options


-
Member
[CU_JIT_LTO](https://docs.nvidia.com/group__CUDA__TYPES.html#group__cuda__types_1gga5527fa8030d5cabedc781a04dbd1997da79765f13b0a4984259dc24c1815bcf20) -
Enable link-time optimization (-dlto) for device code (Disabled by default). This option is not supported on 32-bit platforms. Option type: int Applies to: compiler and linker


-
Member
[CU_JIT_NEW_SM3X_OPT](https://docs.nvidia.com/group__CUDA__TYPES.html#group__cuda__types_1gga5527fa8030d5cabedc781a04dbd1997daebad5c7548c843de9041fb7b007c3a75) -
This jit option is deprecated and should not be used.


-
Member
[CU_JIT_OPTIMIZE_UNUSED_DEVICE_VARIABLES](https://docs.nvidia.com/group__CUDA__TYPES.html#group__cuda__types_1gga5527fa8030d5cabedc781a04dbd1997da81222b676086e77fab0d65751339259a) -
This option serves as a hint to enable the JIT compiler/linker to remove constant (

**constant**) and device (**device**) variables unreferenced in device code (Disabled by default). Note that host references to constant and device variables using APIs like cuModuleGetGlobal() with this option specified may result in undefined behavior unless the variables are explicitly specified using[CU_JIT_REFERENCED_VARIABLE_NAMES](https://docs.nvidia.com/group__CUDA__TYPES.html#group__cuda__types_1gga5527fa8030d5cabedc781a04dbd1997dae3b8c7b5417b4c1719a56ecfbed28d08). Option type: int Applies to: link-time optimization specified with CU_JIT_LTO

-
Member
[CU_JIT_PREC_DIV](https://docs.nvidia.com/group__CUDA__TYPES.html#group__cuda__types_1gga5527fa8030d5cabedc781a04dbd1997dabe9439a7e6e21df8b9db9a5652bdc623) -
Control single-precision floating-point division and reciprocals (-prec-div) support (1: true, default). 1 : Enables the IEEE round-to-nearest mode 0 : Enables the fast approximation mode Option type: int Applies to: link-time optimization specified with CU_JIT_LTO


-
Member
[CU_JIT_PREC_SQRT](https://docs.nvidia.com/group__CUDA__TYPES.html#group__cuda__types_1gga5527fa8030d5cabedc781a04dbd1997da0ed05132fe1349db7e3366abf1ffba12) -
Control single-precision floating-point square root (-prec-sqrt) support (1: true, default). 1 : Enables the IEEE round-to-nearest mode 0 : Enables the fast approximation mode Option type: int Applies to: link-time optimization specified with CU_JIT_LTO


-
Member
[CU_JIT_REFERENCED_KERNEL_COUNT](https://docs.nvidia.com/group__CUDA__TYPES.html#group__cuda__types_1gga5527fa8030d5cabedc781a04dbd1997da70d0672317491b398f27bac394b9f66d) -
Number of entries in

[CU_JIT_REFERENCED_KERNEL_NAMES](https://docs.nvidia.com/group__CUDA__TYPES.html#group__cuda__types_1gga5527fa8030d5cabedc781a04dbd1997dacccfb079541213dc65880ade3de8e2d5)array. Option type: unsigned int Applies to: dynamic linker only

-
Member
[CU_JIT_REFERENCED_KERNEL_NAMES](https://docs.nvidia.com/group__CUDA__TYPES.html#group__cuda__types_1gga5527fa8030d5cabedc781a04dbd1997dacccfb079541213dc65880ade3de8e2d5) -
Array of kernel names that should be preserved at link time while others can be removed. Must contain

[CU_JIT_REFERENCED_KERNEL_COUNT](https://docs.nvidia.com/group__CUDA__TYPES.html#group__cuda__types_1gga5527fa8030d5cabedc781a04dbd1997da70d0672317491b398f27bac394b9f66d)entries. Note that kernel names can be mangled by the compiler in which case the mangled name needs to be specified. Wildcard “*” can be used to represent zero or more characters instead of specifying the full or mangled name. It is important to note that the wildcard “*” is also added implicitly. For example, specifying “foo” will match “foobaz”, “barfoo”, “barfoobaz” and thus preserve all kernels with those names. This can be avoided by providing a more specific name like “barfoobaz”. Option type: const char ** Applies to: dynamic linker only

-
Member
[CU_JIT_REFERENCED_VARIABLE_COUNT](https://docs.nvidia.com/group__CUDA__TYPES.html#group__cuda__types_1gga5527fa8030d5cabedc781a04dbd1997daca302462528cbe24cb45574450033a0b) -
Number of entries in

[CU_JIT_REFERENCED_VARIABLE_NAMES](https://docs.nvidia.com/group__CUDA__TYPES.html#group__cuda__types_1gga5527fa8030d5cabedc781a04dbd1997dae3b8c7b5417b4c1719a56ecfbed28d08)array. Option type: unsigned int Applies to: link-time optimization specified with CU_JIT_LTO

-
Member
[CU_JIT_REFERENCED_VARIABLE_NAMES](https://docs.nvidia.com/group__CUDA__TYPES.html#group__cuda__types_1gga5527fa8030d5cabedc781a04dbd1997dae3b8c7b5417b4c1719a56ecfbed28d08) -
Array of variable names (

**device**and/or**constant**) that should be preserved at link time while others can be removed. Must contain[CU_JIT_REFERENCED_VARIABLE_COUNT](https://docs.nvidia.com/group__CUDA__TYPES.html#group__cuda__types_1gga5527fa8030d5cabedc781a04dbd1997daca302462528cbe24cb45574450033a0b)entries. Note that variable names can be mangled by the compiler in which case the mangled name needs to be specified. Wildcard “*” can be used to represent zero or more characters instead of specifying the full or mangled name. It is important to note that the wildcard “*” is also added implicitly. For example, specifying “foo” will match “foobaz”, “barfoo”, “barfoobaz” and thus preserve all variables with those names. This can be avoided by providing a more specific name like “barfoobaz”. Option type: const char ** Applies to: link-time optimization specified with CU_JIT_LTO

-
Member
[cuCtxAttach](https://docs.nvidia.com/group__CUDA__CTX__DEPRECATED.html#group__cuda__ctx__deprecated_1ga37ec990b2a75ed46f25a48b1a425b4f0)(CUcontext *pctx, unsigned int flags) -

-
Member
[cuCtxDetach](https://docs.nvidia.com/group__CUDA__CTX__DEPRECATED.html#group__cuda__ctx__deprecated_1ga3136efc315abd4c4455e875b9dbb65a1)(CUcontext ctx) -

-
Member
[cuCtxGetSharedMemConfig](https://docs.nvidia.com/group__CUDA__CTX__DEPRECATED.html#group__cuda__ctx__deprecated_1ga17153a1b8b8c756f7ab8505686a4ad74)(CUsharedconfig *pConfig) -

-
Member
[cuCtxSetSharedMemConfig](https://docs.nvidia.com/group__CUDA__CTX__DEPRECATED.html#group__cuda__ctx__deprecated_1ga2574235fa643f8f251bf7bc28fac3692)(CUsharedconfig config) -

-
Member
[cuD3D10CtxCreate](https://docs.nvidia.com/group__CUDA__D3D10__DEPRECATED.html#group__cuda__d3d10__deprecated_1ga82e98ad151a9190cea9627a67d44c1c7)(CUcontext *pCtx, CUdevice *pCudaDevice, unsigned int Flags, ID3D10Device *pD3DDevice) -
This function is deprecated as of CUDA 5.0.


-
Member
[cuD3D10CtxCreateOnDevice](https://docs.nvidia.com/group__CUDA__D3D10__DEPRECATED.html#group__cuda__d3d10__deprecated_1gabe14aa89a02ab377de1c0b611aeb2c1e)(CUcontext *pCtx, unsigned int flags, ID3D10Device *pD3DDevice, CUdevice cudaDevice) -
This function is deprecated as of CUDA 5.0.


-
Member
[cuD3D10GetDirect3DDevice](https://docs.nvidia.com/group__CUDA__D3D10__DEPRECATED.html#group__cuda__d3d10__deprecated_1ga5c8842f9517e493e130ec67d1035ba8a)(ID3D10Device **ppD3DDevice) -
This function is deprecated as of CUDA 5.0.


-
Member
[cuD3D10MapResources](https://docs.nvidia.com/group__CUDA__D3D10__DEPRECATED.html#group__cuda__d3d10__deprecated_1ga3f1c5c5c1e8c0b02af277075d260fa72)(unsigned int count, ID3D10Resource **ppResources) -
This function is deprecated as of CUDA 3.0.


-
Member
[cuD3D10RegisterResource](https://docs.nvidia.com/group__CUDA__D3D10__DEPRECATED.html#group__cuda__d3d10__deprecated_1ga7a46ea2fdda68d85e09499c750c872d0)(ID3D10Resource *pResource, unsigned int Flags) -
This function is deprecated as of CUDA 3.0.


-
Member
[cuD3D10ResourceGetMappedArray](https://docs.nvidia.com/group__CUDA__D3D10__DEPRECATED.html#group__cuda__d3d10__deprecated_1gad9c2f1803809bfa616127ee88df54478)(CUarray *pArray, ID3D10Resource *pResource, unsigned int SubResource) -
This function is deprecated as of CUDA 3.0.


-
Member
[cuD3D10ResourceGetMappedPitch](https://docs.nvidia.com/group__CUDA__D3D10__DEPRECATED.html#group__cuda__d3d10__deprecated_1gac760eb925462d7ed911a804ac801d437)(size_t *pPitch, size_t *pPitchSlice, ID3D10Resource *pResource, unsigned int SubResource) -
This function is deprecated as of CUDA 3.0.


-
Member
[cuD3D10ResourceGetMappedPointer](https://docs.nvidia.com/group__CUDA__D3D10__DEPRECATED.html#group__cuda__d3d10__deprecated_1ga8b6ea4e4b561d6497f0210d9bbc1a7fc)(CUdeviceptr *pDevPtr, ID3D10Resource *pResource, unsigned int SubResource) -
This function is deprecated as of CUDA 3.0.


-
Member
[cuD3D10ResourceGetMappedSize](https://docs.nvidia.com/group__CUDA__D3D10__DEPRECATED.html#group__cuda__d3d10__deprecated_1ga37f0928f531e12f642084c0ff6ed15f5)(size_t *pSize, ID3D10Resource *pResource, unsigned int SubResource) -
This function is deprecated as of CUDA 3.0.


-
Member
[cuD3D10ResourceGetSurfaceDimensions](https://docs.nvidia.com/group__CUDA__D3D10__DEPRECATED.html#group__cuda__d3d10__deprecated_1gaca78cef7510dc3375215878b185eb30f)(size_t *pWidth, size_t *pHeight, size_t *pDepth, ID3D10Resource *pResource, unsigned int SubResource) -
This function is deprecated as of CUDA 3.0.


-
Member
[cuD3D10ResourceSetMapFlags](https://docs.nvidia.com/group__CUDA__D3D10__DEPRECATED.html#group__cuda__d3d10__deprecated_1ga21ee183ac71b99048ff8e9ce9bfc1f4b)(ID3D10Resource *pResource, unsigned int Flags) -
This function is deprecated as of CUDA 3.0.


-
Member
[cuD3D10UnmapResources](https://docs.nvidia.com/group__CUDA__D3D10__DEPRECATED.html#group__cuda__d3d10__deprecated_1gaa3b5e7426130a24a8aa2900a766d3a45)(unsigned int count, ID3D10Resource **ppResources) -
This function is deprecated as of CUDA 3.0.


-
Member
[cuD3D10UnregisterResource](https://docs.nvidia.com/group__CUDA__D3D10__DEPRECATED.html#group__cuda__d3d10__deprecated_1ga820664c48e2dbac37979a21c21d6561d)(ID3D10Resource *pResource) -
This function is deprecated as of CUDA 3.0.


-
Member
[cuD3D11CtxCreate](https://docs.nvidia.com/group__CUDA__D3D11__DEPRECATED.html#group__cuda__d3d11__deprecated_1gae4af5a512b035287636a04d10e8a9c45)(CUcontext *pCtx, CUdevice *pCudaDevice, unsigned int Flags, ID3D11Device *pD3DDevice) -
This function is deprecated as of CUDA 5.0.


-
Member
[cuD3D11CtxCreateOnDevice](https://docs.nvidia.com/group__CUDA__D3D11__DEPRECATED.html#group__cuda__d3d11__deprecated_1gaddec8b1c7e19569c93426e5de6c5fc2d)(CUcontext *pCtx, unsigned int flags, ID3D11Device *pD3DDevice, CUdevice cudaDevice) -
This function is deprecated as of CUDA 5.0.


-
Member
[cuD3D11GetDirect3DDevice](https://docs.nvidia.com/group__CUDA__D3D11__DEPRECATED.html#group__cuda__d3d11__deprecated_1ga5de097eb7ea7fb3721e9c7f79528113e)(ID3D11Device **ppD3DDevice) -
This function is deprecated as of CUDA 5.0.


-
Member
[cuD3D9MapResources](https://docs.nvidia.com/group__CUDA__D3D9__DEPRECATED.html#group__cuda__d3d9__deprecated_1ga4dd775efbe77be0830dd552ca9d06415)(unsigned int count, IDirect3DResource9 **ppResource) -
This function is deprecated as of CUDA 3.0.


-
Member
[cuD3D9RegisterResource](https://docs.nvidia.com/group__CUDA__D3D9__DEPRECATED.html#group__cuda__d3d9__deprecated_1ga4b02e7838e47b8fc5df73f43969f0373)(IDirect3DResource9 *pResource, unsigned int Flags) -
This function is deprecated as of CUDA 3.0.


-
Member
[cuD3D9ResourceGetMappedArray](https://docs.nvidia.com/group__CUDA__D3D9__DEPRECATED.html#group__cuda__d3d9__deprecated_1gad57f23104b028fb8b4d9a18a85b9440e)(CUarray *pArray, IDirect3DResource9 *pResource, unsigned int Face, unsigned int Level) -
This function is deprecated as of CUDA 3.0.


-
Member
[cuD3D9ResourceGetMappedPitch](https://docs.nvidia.com/group__CUDA__D3D9__DEPRECATED.html#group__cuda__d3d9__deprecated_1gabd6bcc011d54d5d9386b8fa6b62d0d80)(size_t *pPitch, size_t *pPitchSlice, IDirect3DResource9 *pResource, unsigned int Face, unsigned int Level) -
This function is deprecated as of CUDA 3.0.


-
Member
[cuD3D9ResourceGetMappedPointer](https://docs.nvidia.com/group__CUDA__D3D9__DEPRECATED.html#group__cuda__d3d9__deprecated_1ga5cdb639c75d3d83bca49ed0757a774e3)(CUdeviceptr *pDevPtr, IDirect3DResource9 *pResource, unsigned int Face, unsigned int Level) -
This function is deprecated as of CUDA 3.0.


-
Member
[cuD3D9ResourceGetMappedSize](https://docs.nvidia.com/group__CUDA__D3D9__DEPRECATED.html#group__cuda__d3d9__deprecated_1ga41cbdd62092a4f5074e1a8556a749a47)(size_t *pSize, IDirect3DResource9 *pResource, unsigned int Face, unsigned int Level) -
This function is deprecated as of CUDA 3.0.


-
Member
[cuD3D9ResourceGetSurfaceDimensions](https://docs.nvidia.com/group__CUDA__D3D9__DEPRECATED.html#group__cuda__d3d9__deprecated_1gada5ebceca91b3660e2cd64bde32f3bf5)(size_t *pWidth, size_t *pHeight, size_t *pDepth, IDirect3DResource9 *pResource, unsigned int Face, unsigned int Level) -
This function is deprecated as of CUDA 3.0.


-
Member
[cuD3D9ResourceSetMapFlags](https://docs.nvidia.com/group__CUDA__D3D9__DEPRECATED.html#group__cuda__d3d9__deprecated_1ga4c70858f65c9f6613284201e2d726d06)(IDirect3DResource9 *pResource, unsigned int Flags) -
This function is deprecated as of Cuda 3.0.


-
Member
[cuD3D9UnmapResources](https://docs.nvidia.com/group__CUDA__D3D9__DEPRECATED.html#group__cuda__d3d9__deprecated_1ga8182c672e1423ecba7dad98b54be18ac)(unsigned int count, IDirect3DResource9 **ppResource) -
This function is deprecated as of CUDA 3.0.


-
Member
[cuD3D9UnregisterResource](https://docs.nvidia.com/group__CUDA__D3D9__DEPRECATED.html#group__cuda__d3d9__deprecated_1ga12e2ef50f8993a414d670a63773b6760)(IDirect3DResource9 *pResource) -
This function is deprecated as of CUDA 3.0.


-
Member
[CUDA_ERROR_CONTEXT_ALREADY_CURRENT](https://docs.nvidia.com/group__CUDA__TYPES.html#group__cuda__types_1ggac6c391505e117393cc2558fff6bfc2e9ae176089800b8c21a84f1e8318d688f1d) -
This error return is deprecated as of CUDA 3.2. It is no longer an error to attempt to push the active context via cuCtxPushCurrent().


-
Member
[CUDA_ERROR_PROFILER_ALREADY_STARTED](https://docs.nvidia.com/group__CUDA__TYPES.html#group__cuda__types_1ggac6c391505e117393cc2558fff6bfc2e9ab39b7696161bed9e1bc447ba699bf799) -
This error return is deprecated as of CUDA 5.0. It is no longer an error to call

[cuProfilerStart()](https://docs.nvidia.com/group__CUDA__PROFILER.html#group__cuda__profiler_1ga8a5314de2292c2efac83ac7fcfa9190e)when profiling is already enabled.

-
Member
[CUDA_ERROR_PROFILER_ALREADY_STOPPED](https://docs.nvidia.com/group__CUDA__TYPES.html#group__cuda__types_1ggac6c391505e117393cc2558fff6bfc2e9a0e8858d89f258b64a19003318673d6ee) -
This error return is deprecated as of CUDA 5.0. It is no longer an error to call

[cuProfilerStop()](https://docs.nvidia.com/group__CUDA__PROFILER.html#group__cuda__profiler_1ga4d8edef6174fd90165e6ac838f320a5f)when profiling is already disabled.

-
Member
[CUDA_ERROR_PROFILER_NOT_INITIALIZED](https://docs.nvidia.com/group__CUDA__TYPES.html#group__cuda__types_1ggac6c391505e117393cc2558fff6bfc2e9ab29d2209136a0e8b27c4d14aada28b97) -
This error return is deprecated as of CUDA 5.0. It is no longer an error to attempt to enable/disable the profiling via

[cuProfilerStart](https://docs.nvidia.com/group__CUDA__PROFILER.html#group__cuda__profiler_1ga8a5314de2292c2efac83ac7fcfa9190e)or[cuProfilerStop](https://docs.nvidia.com/group__CUDA__PROFILER.html#group__cuda__profiler_1ga4d8edef6174fd90165e6ac838f320a5f)without initialization.

-
Member
[cuDeviceComputeCapability](https://docs.nvidia.com/group__CUDA__DEVICE__DEPRECATED.html#group__cuda__device__deprecated_1gae2091bbac7e1fb18c2821612115607ea)(int *major, int *minor, CUdevice dev) -

-
Member
[cuDeviceGetProperties](https://docs.nvidia.com/group__CUDA__DEVICE__DEPRECATED.html#group__cuda__device__deprecated_1ga65a5b4e25186bd257df80b98c98cffe6)(CUdevprop *prop, CUdevice dev) -

-
Member
[cuFuncSetBlockShape](https://docs.nvidia.com/group__CUDA__EXEC__DEPRECATED.html#group__cuda__exec__deprecated_1ga61e4450eaedf5159547e75199fe1c447)(CUfunction hfunc, int x, int y, int z) -

-
Member
[cuFuncSetSharedMemConfig](https://docs.nvidia.com/group__CUDA__EXEC__DEPRECATED.html#group__cuda__exec__deprecated_1ga430b913f24970e63869635395df6d9f5)(CUfunction hfunc, CUsharedconfig config) -

-
Member
[cuFuncSetSharedSize](https://docs.nvidia.com/group__CUDA__EXEC__DEPRECATED.html#group__cuda__exec__deprecated_1ga440dbf66d2e977528779527f3eaadab1)(CUfunction hfunc, unsigned int bytes) -

-
Member
[cuGLCtxCreate](https://docs.nvidia.com/group__CUDA__GL__DEPRECATED.html#group__cuda__gl__deprecated_1ga923988b9596911c39bb55fd848015a3d)(CUcontext *pCtx, unsigned int Flags, CUdevice device) -
This function is deprecated as of Cuda 5.0.


-
Member
[cuGLInit](https://docs.nvidia.com/group__CUDA__GL__DEPRECATED.html#group__cuda__gl__deprecated_1ga1eb69794b494f2908664737e3386aec4)(void) -
This function is deprecated as of Cuda 3.0.


-
Member
[cuGLMapBufferObject](https://docs.nvidia.com/group__CUDA__GL__DEPRECATED.html#group__cuda__gl__deprecated_1ga6fc2c6a0d217eab602155311b8bfc404)(CUdeviceptr *dptr, size_t *size, GLuint buffer) -
This function is deprecated as of Cuda 3.0.


-
Member
[cuGLMapBufferObjectAsync](https://docs.nvidia.com/group__CUDA__GL__DEPRECATED.html#group__cuda__gl__deprecated_1ga2f7b5a7b8b201d3638f7251fdb00d0ae)(CUdeviceptr *dptr, size_t *size, GLuint buffer, CUstream hStream) -
This function is deprecated as of Cuda 3.0.


-
Member
[cuGLRegisterBufferObject](https://docs.nvidia.com/group__CUDA__GL__DEPRECATED.html#group__cuda__gl__deprecated_1ga5d6e3dcc56ee510d153551b8e949615f)(GLuint buffer) -
This function is deprecated as of Cuda 3.0.


-
Member
[cuGLSetBufferObjectMapFlags](https://docs.nvidia.com/group__CUDA__GL__DEPRECATED.html#group__cuda__gl__deprecated_1gab37c21f676303914a3e7151910aabeb2)(GLuint buffer, unsigned int Flags) -
This function is deprecated as of Cuda 3.0.


-
Member
[cuGLUnmapBufferObject](https://docs.nvidia.com/group__CUDA__GL__DEPRECATED.html#group__cuda__gl__deprecated_1ga5beb89f35d0d12ad60313b183bef7ac4)(GLuint buffer) -
This function is deprecated as of Cuda 3.0.


-
Member
[cuGLUnmapBufferObjectAsync](https://docs.nvidia.com/group__CUDA__GL__DEPRECATED.html#group__cuda__gl__deprecated_1ga9254e4e0c99f4769c2d423a6f8d7ca9f)(GLuint buffer, CUstream hStream) -
This function is deprecated as of Cuda 3.0.


-
Member
[cuGLUnregisterBufferObject](https://docs.nvidia.com/group__CUDA__GL__DEPRECATED.html#group__cuda__gl__deprecated_1ga465091301c2e92756c98c4c184c90da1)(GLuint buffer) -
This function is deprecated as of Cuda 3.0.


-
Member
[cuLaunch](https://docs.nvidia.com/group__CUDA__EXEC__DEPRECATED.html#group__cuda__exec__deprecated_1gab6a42f735d8ddd3b5059ddb6d2bd9a63)(CUfunction f) -

-
Member
[cuLaunchCooperativeKernelMultiDevice](https://docs.nvidia.com/group__CUDA__EXEC__DEPRECATED.html#group__cuda__exec__deprecated_1gac4ae8a24130e1e7938514f7e28c76bad)(CUDA_LAUNCH_PARAMS *launchParamsList, unsigned int numDevices, unsigned int flags) -
This function is deprecated as of CUDA 11.3.


-
Member
[cuLaunchGrid](https://docs.nvidia.com/group__CUDA__EXEC__DEPRECATED.html#group__cuda__exec__deprecated_1ga39d9904389fa9594622f8b0ec25b4016)(CUfunction f, int grid_width, int grid_height) -

-
Member
[cuLaunchGridAsync](https://docs.nvidia.com/group__CUDA__EXEC__DEPRECATED.html#group__cuda__exec__deprecated_1gaf554b88508bf9d68a6c8ba6c9115c9fc)(CUfunction f, int grid_width, int grid_height, CUstream hStream) -

-
Member
[cuModuleGetSurfRef](https://docs.nvidia.com/group__CUDA__MODULE__DEPRECATED.html#group__cuda__module__deprecated_1ga71c19dab9374e8481d8d8629a77377b1)(CUsurfref *pSurfRef, CUmodule hmod, const char *name) -

-
Member
[cuModuleGetTexRef](https://docs.nvidia.com/group__CUDA__MODULE__DEPRECATED.html#group__cuda__module__deprecated_1ga9607dcbf911c16420d5264273f2b5608)(CUtexref *pTexRef, CUmodule hmod, const char *name) -

-
Member
[cuParamSetf](https://docs.nvidia.com/group__CUDA__EXEC__DEPRECATED.html#group__cuda__exec__deprecated_1ga793176d32b0bf9ad842d4fc157d07e80)(CUfunction hfunc, int offset, float value) -

-
Member
[cuParamSeti](https://docs.nvidia.com/group__CUDA__EXEC__DEPRECATED.html#group__cuda__exec__deprecated_1ga183700c3c8934cf46077355c39247c14)(CUfunction hfunc, int offset, unsigned int value) -

-
Member
[cuParamSetSize](https://docs.nvidia.com/group__CUDA__EXEC__DEPRECATED.html#group__cuda__exec__deprecated_1gadf689dac0db8f6c1232c339d3f923554)(CUfunction hfunc, unsigned int numbytes) -

-
Member
[cuParamSetTexRef](https://docs.nvidia.com/group__CUDA__EXEC__DEPRECATED.html#group__cuda__exec__deprecated_1ga6318a800689fce0fa4babb06c0544919)(CUfunction hfunc, int texunit, CUtexref hTexRef) -

-
Member
[cuParamSetv](https://docs.nvidia.com/group__CUDA__EXEC__DEPRECATED.html#group__cuda__exec__deprecated_1gacc446977269d74db8fdd341959409ea7)(CUfunction hfunc, int offset, void *ptr, unsigned int numbytes) -

-
Member
[cuProfilerInitialize](https://docs.nvidia.com/group__CUDA__PROFILER__DEPRECATED.html#group__cuda__profiler__deprecated_1gad5d346ef62db53032948f387650d1a18)(const char *configFile, const char *outputFile, CUoutput_mode outputMode) -

-
Member
[CUsharedconfig](https://docs.nvidia.com/group__CUDA__TYPES.html#group__cuda__types_1ga92d66e95f602cb9fdaf0682c260c241b) -

-
Member
[cuSurfRefGetArray](https://docs.nvidia.com/group__CUDA__SURFREF__DEPRECATED.html#group__cuda__surfref__deprecated_1gac3b9c5794f67a897ae85ebd235c971ed)(CUarray *phArray, CUsurfref hSurfRef) -

-
Member
[cuSurfRefSetArray](https://docs.nvidia.com/group__CUDA__SURFREF__DEPRECATED.html#group__cuda__surfref__deprecated_1ga19e4cf8fc0cdcd914e01ecf12fdc5faf)(CUsurfref hSurfRef, CUarray hArray, unsigned int Flags) -

-
Member
[cuTexRefCreate](https://docs.nvidia.com/group__CUDA__TEXREF__DEPRECATED.html#group__cuda__texref__deprecated_1ga0084fabe2c6d28ffcf9d9f5c7164f16c)(CUtexref *pTexRef) -

-
Member
[cuTexRefDestroy](https://docs.nvidia.com/group__CUDA__TEXREF__DEPRECATED.html#group__cuda__texref__deprecated_1gaea8edbd6cf9f97e6ab2b41fc6785519d)(CUtexref hTexRef) -

-
Member
[cuTexRefGetAddress](https://docs.nvidia.com/group__CUDA__TEXREF__DEPRECATED.html#group__cuda__texref__deprecated_1ga4e4674ce0b20a8951b65dead94a338e1)(CUdeviceptr *pdptr, CUtexref hTexRef) -

-
Member
[cuTexRefGetAddressMode](https://docs.nvidia.com/group__CUDA__TEXREF__DEPRECATED.html#group__cuda__texref__deprecated_1gafb367d93dc1d20aab0cf8ce70d543b33)(CUaddress_mode *pam, CUtexref hTexRef, int dim) -

-
Member
[cuTexRefGetArray](https://docs.nvidia.com/group__CUDA__TEXREF__DEPRECATED.html#group__cuda__texref__deprecated_1ga388250d826d74c075b51d0c1648aa6d1)(CUarray *phArray, CUtexref hTexRef) -

-
Member
[cuTexRefGetBorderColor](https://docs.nvidia.com/group__CUDA__TEXREF__DEPRECATED.html#group__cuda__texref__deprecated_1ga33c56ad2b999c59adce2bfba709ab292)(float *pBorderColor, CUtexref hTexRef) -

-
Member
[cuTexRefGetFilterMode](https://docs.nvidia.com/group__CUDA__TEXREF__DEPRECATED.html#group__cuda__texref__deprecated_1ga2439e069746f69b940f2f4dbc78cdf87)(CUfilter_mode *pfm, CUtexref hTexRef) -

-
Member
[cuTexRefGetFlags](https://docs.nvidia.com/group__CUDA__TEXREF__DEPRECATED.html#group__cuda__texref__deprecated_1ga71310eec5c196aa85674b079dea88a04)(unsigned int *pFlags, CUtexref hTexRef) -

-
Member
[cuTexRefGetFormat](https://docs.nvidia.com/group__CUDA__TEXREF__DEPRECATED.html#group__cuda__texref__deprecated_1ga90936eb6c7c4434a609e1160c278ae53)(CUarray_format *pFormat, int *pNumChannels, CUtexref hTexRef) -

-
Member
[cuTexRefGetMaxAnisotropy](https://docs.nvidia.com/group__CUDA__TEXREF__DEPRECATED.html#group__cuda__texref__deprecated_1ga56f52273c1b456d5a2cf7a85d86d0205)(int *pmaxAniso, CUtexref hTexRef) -

-
Member
[cuTexRefGetMipmapFilterMode](https://docs.nvidia.com/group__CUDA__TEXREF__DEPRECATED.html#group__cuda__texref__deprecated_1ga60d45fe9ff9be6f92ea20e37a03e06d7)(CUfilter_mode *pfm, CUtexref hTexRef) -

-
Member
[cuTexRefGetMipmapLevelBias](https://docs.nvidia.com/group__CUDA__TEXREF__DEPRECATED.html#group__cuda__texref__deprecated_1gae32365ea560887c59be72ccd431e5c04)(float *pbias, CUtexref hTexRef) -

-
Member
[cuTexRefGetMipmapLevelClamp](https://docs.nvidia.com/group__CUDA__TEXREF__DEPRECATED.html#group__cuda__texref__deprecated_1ga3dc6275f3b0d6f0b2adc7bb7e489f8d2)(float *pminMipmapLevelClamp, float *pmaxMipmapLevelClamp, CUtexref hTexRef) -

-
Member
[cuTexRefGetMipmappedArray](https://docs.nvidia.com/group__CUDA__TEXREF__DEPRECATED.html#group__cuda__texref__deprecated_1gaed9eaa907457a9bbb0d244b93a42dd79)(CUmipmappedArray *phMipmappedArray, CUtexref hTexRef) -

-
Member
[cuTexRefSetAddress](https://docs.nvidia.com/group__CUDA__TEXREF__DEPRECATED.html#group__cuda__texref__deprecated_1ga44ef7e5055192d52b3d43456602b50a8)(size_t *ByteOffset, CUtexref hTexRef, CUdeviceptr dptr, size_t bytes) -

-
Member
[cuTexRefSetAddress2D](https://docs.nvidia.com/group__CUDA__TEXREF__DEPRECATED.html#group__cuda__texref__deprecated_1ga26f709bbe10516681913d1ffe8756ee2)(CUtexref hTexRef, const CUDA_ARRAY_DESCRIPTOR *desc, CUdeviceptr dptr, size_t Pitch) -

-
Member
[cuTexRefSetAddressMode](https://docs.nvidia.com/group__CUDA__TEXREF__DEPRECATED.html#group__cuda__texref__deprecated_1ga85f4a13eeb94c8072f61091489349bcb)(CUtexref hTexRef, int dim, CUaddress_mode am) -

-
Member
[cuTexRefSetArray](https://docs.nvidia.com/group__CUDA__TEXREF__DEPRECATED.html#group__cuda__texref__deprecated_1ga34435b306682531716243239f0084fed)(CUtexref hTexRef, CUarray hArray, unsigned int Flags) -

-
Member
[cuTexRefSetBorderColor](https://docs.nvidia.com/group__CUDA__TEXREF__DEPRECATED.html#group__cuda__texref__deprecated_1gaf1dbbdef278be3592780b0a7cc2e1c67)(CUtexref hTexRef, float *pBorderColor) -

-
Member
[cuTexRefSetFilterMode](https://docs.nvidia.com/group__CUDA__TEXREF__DEPRECATED.html#group__cuda__texref__deprecated_1ga595d0af02c55576f8c835e4efd1f39c0)(CUtexref hTexRef, CUfilter_mode fm) -

-
Member
[cuTexRefSetFlags](https://docs.nvidia.com/group__CUDA__TEXREF__DEPRECATED.html#group__cuda__texref__deprecated_1ga554ffd896487533c36810f2e45bb7a28)(CUtexref hTexRef, unsigned int Flags) -

-
Member
[cuTexRefSetFormat](https://docs.nvidia.com/group__CUDA__TEXREF__DEPRECATED.html#group__cuda__texref__deprecated_1ga05585ef8ea2fec728a03c6c8f87cf07a)(CUtexref hTexRef, CUarray_format fmt, int NumPackedComponents) -

-
Member
[cuTexRefSetMaxAnisotropy](https://docs.nvidia.com/group__CUDA__TEXREF__DEPRECATED.html#group__cuda__texref__deprecated_1ga623f5c00b1b2a883f3bddfc1792c85da)(CUtexref hTexRef, unsigned int maxAniso) -

-
Member
[cuTexRefSetMipmapFilterMode](https://docs.nvidia.com/group__CUDA__TEXREF__DEPRECATED.html#group__cuda__texref__deprecated_1gae6238426775fa672a1518fe9828f2d76)(CUtexref hTexRef, CUfilter_mode fm) -

-
Member
[cuTexRefSetMipmapLevelBias](https://docs.nvidia.com/group__CUDA__TEXREF__DEPRECATED.html#group__cuda__texref__deprecated_1ga3be1de86e98d39c3a6b59c11cca5b77d)(CUtexref hTexRef, float bias) -

-
Member
[cuTexRefSetMipmapLevelClamp](https://docs.nvidia.com/group__CUDA__TEXREF__DEPRECATED.html#group__cuda__texref__deprecated_1gaf7354fa837b181a8b094b99654b14086)(CUtexref hTexRef, float minMipmapLevelClamp, float maxMipmapLevelClamp) -

-
Member
[cuTexRefSetMipmappedArray](https://docs.nvidia.com/group__CUDA__TEXREF__DEPRECATED.html#group__cuda__texref__deprecated_1ga8a550f19ff84858a396f79a526fd3406)(CUtexref hTexRef, CUmipmappedArray hMipmappedArray, unsigned int Flags) -