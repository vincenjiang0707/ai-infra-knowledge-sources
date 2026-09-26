source: https://docs.nvidia.com/compute-sanitizer/api/group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i.html

# Sanitizer Patching API[#](https://docs.nvidia.com#sanitizer-patching-api)

Functions, types, and enums that implement the Sanitizer Patching API.

## Typedefs[#](https://docs.nvidia.com#typedefs)

[SanitizerCallbackAsyncReduction](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gad620cec6f0d41934acbe5f1ad9262bd9)Function type for an asynchronous reduction operation on shared memory.

[SanitizerCallbackAsyncStore](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga504dcd9a3fffd84b14dd46ee751a9555)Function type for an asynchronous store operation on shared memory.

[SanitizerCallbackBarrier](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaa62d7a8432bc9e0844bcf742f9f9b011)Function type for a barrier callback.

[SanitizerCallbackBlockEnter](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga44dab03d6994ad49f52593d891899006)Function type for a CUDA block enter callback.

[SanitizerCallbackBlockExit](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaa9a0bc3a199e07f75c2bfe62a37ffd69)Function type for a CUDA block exit callback.

[SanitizerCallbackBulkCopyGlobalToShared](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga79cb32f5fe0b1064d2aab770b4e7376e)Function type for a async bulk copy from global to shared memory.

[SanitizerCallbackBulkCopySharedToGlobal](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga77f4056eb632d5a842e545ade1079a83)Function type for a async bulk copy from shared to global memory.

[SanitizerCallbackBulkCopySharedToShared](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga538085c8f2108d13a6ba9cac64aaecf3)Function type for a async bulk copy from shared to shered memory.

[SanitizerCallbackBulkReductionSharedToGlobal](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga0dcaed943c8b50367df500fb8ee7311c)Function type for a async bulk reduction from shared to global memory.

[SanitizerCallbackBulkReductionSharedToShared](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaa3f72083e8d38005581ced3866eede71)Function type for a async bulk reduction from shared to shered memory.

[SanitizerCallbackCacheControl](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gab88689ebe67ea8a61c07652b736ddec8)Function type for a cache control instruction callback.

[SanitizerCallbackCall](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga5a5866bef614d94825c786a6c724c4b2)Function type for a function call callback.

[SanitizerCallbackClusterBarrierArrive](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga7890db85704a47a51045a2a2694207e1)Function type for a cluster barrier arrive.

[SanitizerCallbackClusterBarrierWait](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga30a1f63e88780a5d0b5b73c9a72ff3df)Function type for a cluster barrier wait.

[SanitizerCallbackCudaBarrier](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gae7014a0fcaf412a25cb5cbf85818e357)Function type for a CUDA Barrier action callback.

[SanitizerCallbackCudaBarrierAttempt](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga7d391123826657aca834e2130981e81c)Function type for a CUDA Barrier action callback.

[SanitizerCallbackDeviceSideFree](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga130489e7e21fcdd5b8dc6382090d9e13)Function type for a device-side free call.

[SanitizerCallbackDeviceSideMalloc](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga06bda752ce9da191c0c780fd2330b479)Function type for a device-side malloc call.

[SanitizerCallbackMatrixMemoryAccess](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga2f254af064064938362861a073fcafa8)Function type for a matrix shared memory access callback.

[SanitizerCallbackMemcpyAsync](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga523e5d920cb4c8c49eb46c1b2cd17087)Function type for a global to shared memory asynchronous copy.

[SanitizerCallbackMemcpyAsyncBarrier](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga26b3790de61869b7a190a24a3dca220e)Function type for a cuda barrier used for mbarrier completion.

[SanitizerCallbackMemoryAccess](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga6ba3aa1fae45f8b70c5289ac11c49a6a)Function type for a memory access callback.

[SanitizerCallbackMemsetShared](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga42f02e0e258c42ef8cac1b06fffa8c69)Function type for a memset on shared memory.

[SanitizerCallbackPipelineCommit](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaaac734ca1642efc475c934c8f406539a)Function type for a pipeline commit.

[SanitizerCallbackPipelineWait](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga3e78dbc028a8c8d9005ff2c4a6deb35b)Function type for a pipeline wait.

[SanitizerCallbackRet](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga7ed18503ba41529ba07b153ac03ba730)Function type for a function return callback.

[SanitizerCallbackSetSmemSize](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga91fbc129b2da327140646c217aa3a435)Function type for setting the shared memory size allocated to a block.

[SanitizerCallbackShfl](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaf95531eeb610479d4b672a7c1b7df039)Function type for a shfl callback.

[SanitizerCallbackSyncwarp](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gab99b4cd8171ad761a59ef900517c733a)Function type for a syncwarp callback.

[SanitizerCallbackTensorCoreBarrier](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga51188689b2be1e27139afb8f3b96080c)Function type for a Blackwell tensor core barrier.

[SanitizerCallbackTensorMemoryLoad](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gac0120457fecc40f4308c92f82aa58f22)[SanitizerCallbackWarpgroupFence](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga7ae0bc634fb431477f925b557d2c3f70)Function type for a warpgroup MMA fence.

[SanitizerCallbackWarpgroupMMAAsync](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga23ba635b8af1d84e5ef1d3363b4709a9)Function type for a warpgroup aligned async MMA.

[SanitizerCallbackWarpgroupWaitGroup](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga5c987165a25ab95edce4b35723abb8c1)Function type for a warpgroup MMA wait group.

[Sanitizer_LaunchHandle](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga89c4c004dbeee79636f6696c408cf1aa)

## Enumerations[#](https://docs.nvidia.com#enumerations)

[SanitizerPatchResult](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga3db35bcf534fa726680c73ba242b2e70)Sanitizer patch result codes.

[Sanitizer_BarrierFlags](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga22dc34eb2f89b61aa2a8535c8c089209)Flags describing a barrier.

[Sanitizer_CacheControlInstructionKind](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gad3bcfc1a9d22465613ada149c757b5db)Cache control action.

[Sanitizer_CallFlags](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga2c82c2446853ee79b55d71b098181ca1)Flags describing a function call.

[Sanitizer_CudaBarrierFlags](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaffcd643218914203431781ba3ae46b70)Flags describing a CUDA Barrier action.

[Sanitizer_CudaBarrierInstructionKind](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga505b1abbfde6d1d66fba877f5ce9b5f3)CUDA Barrier action kind.

[Sanitizer_DeviceMemoryFlags](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaa177905ebbb1a243f0784662d6de9c0e)Flags describing a memory access.

[Sanitizer_FunctionLoadedStatus](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga7378dfd4f3c8d5f315e733e0243ae46d)[Sanitizer_InstructionId](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga25af2e64f4c5e2a4e012edb4bb991dcf)Instrumentation.

[Sanitizer_LoadMode](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga93a84fa745a4ea64f57e49e154b59e7b)[Sanitizer_WarpgroupMMAAsyncFlags](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gacec4a303dd18b91d32ba1bcabf7296e9)Flags describing a warpgroup aligned MMA async.


## Functions[#](https://docs.nvidia.com#functions)

- SanitizerResult
[sanitizerAddPatches](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga9c3e7ff615f89534d674989679f2f0f5)(const void *image, CUcontext ctx) Load a module containing patches that can be used by the patching API.

- SanitizerResult
[sanitizerAddPatchesFromFile](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga1dd8a6a6700a156fabb0f96dba61dd97)(const char *filename, CUcontext ctx) Load a module containing patches that can be used by the patching API.

- SanitizerResult
[sanitizerGetCallbackPcAndSize](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gab14ad83bbb1b53e433b297a71dc9add4)(CUcontext ctx, const char *deviceCallbackName, uint64_t *pc, uint64_t *size) Get PC and size of a device callback.

- SanitizerResult
[sanitizerGetFunctionLoadedStatus](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga15652426721721917c39e3f26f50bf11)(CUfunction func, Sanitizer_FunctionLoadedStatus *loadingStatus) Get the loading status of a function.

- SanitizerResult
[sanitizerGetFunctionPcAndSize](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gae65131f0c6b17318db16e618501e761f)(CUmodule module, const char *functionName, uint64_t *pc, uint64_t *size) Get PC and size of a CUDA function.

- SanitizerResult
[sanitizerPatchInstructions](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaaa4c241c599f34d0010c2b3a9bc64678)(const Sanitizer_InstructionId instructionId, CUmodule module, const char *deviceCallbackName) Set instrumentation points and patches to be applied in a module.

- SanitizerResult
[sanitizerPatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92)(CUmodule module) Perform the actual instrumentation of a module.

- SanitizerResult
[sanitizerSetCallbackData](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gad7d6a3be98248bcf8b75376fb63f4928)(CUfunction kernel, const void *userdata) Specifies the user data pointer for callbacks.

- SanitizerResult
[sanitizerSetDeviceGraphData](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga4785e22e74662e75a8540424ca6c8306)(CUgraphExec graphExec, Sanitizer_StreamHandle stream, const void *userdata) Specifies the user data pointer accessible from callbacks in the device-launched graphs launched by the specified host-launched graphExec.

- SanitizerResult
[sanitizerSetLaunchCallbackData](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga20e623843fd96ae221e7225d5e5369b9)(Sanitizer_LaunchHandle launch, CUfunction kernel, Sanitizer_StreamHandle stream, const void *userdata) Specifies the user data pointer for callbacks.

- SanitizerResult
[sanitizerUnpatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga384d2828ad1eb631eff4df8cbbbcba43)(CUmodule module) Remove existing instrumentation of a module.


## Typedefs[#](https://docs.nvidia.com#id1)

-
typedef
[SanitizerPatchResult](https://docs.nvidia.com#_CPPv420SanitizerPatchResult)(*SanitizerCallbackAsyncReduction)(void *userdata, uint64_t pc, uint32_t address, uint32_t mbarAddress, uint32_t accessSize)[#](https://docs.nvidia.com#_CPPv431SanitizerCallbackAsyncReduction) Function type for an asynchronous reduction operation on shared memory.

This can be generated by a red.async PTX instruction.

- Param userdata:
Pointer to user data. See

[sanitizerPatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92).- Param pc:
Program counter of the patched instruction.

- Param address:
Destination address in shared memory.

- Param mbarAddress:
Address of the mbarrier object.

- Param accessSize:
Size of the access in bytes. Valid values are 4 and 8.



-
typedef
[SanitizerPatchResult](https://docs.nvidia.com#_CPPv420SanitizerPatchResult)(*SanitizerCallbackAsyncStore)(void *userdata, uint64_t pc, uint32_t address, uint32_t mbarAddress, void *pNewValue, uint32_t accessSize)[#](https://docs.nvidia.com#_CPPv427SanitizerCallbackAsyncStore) Function type for an asynchronous store operation on shared memory.

This can be generated by a st.async PTX instruction.

- Param userdata:
Pointer to user data. See

[sanitizerPatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92).- Param pc:
Program counter of the patched instruction.

- Param address:
Destination address in shared memory.

- Param mbarAddress:
Address of the mbarrier object.

- Param pNewValue:
Pointer to the new value being written.

- Param accessSize:
Size of the access in bytes. Valid values are 4 and 8.



-
typedef
[SanitizerPatchResult](https://docs.nvidia.com#_CPPv420SanitizerPatchResult)(*SanitizerCallbackBarrier)(void *userdata, uint64_t pc, uint32_t barIndex, uint32_t threadCount, uint32_t flags)[#](https://docs.nvidia.com#_CPPv424SanitizerCallbackBarrier) Function type for a barrier callback.

- Param userdata:
Pointer to user data. See

[sanitizerPatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92).- Param pc:
Program counter of the patched instruction.

- Param barIndex:
Barrier index.

- Param threadCount:
Number of expected threads (must be a multiple of the warp size).

- Param flags:
Contains information about the barrier. See Sanitizer_BarrierFlags to interpret this value. 0 means that all threads are participating in the barrier.



-
typedef
[SanitizerPatchResult](https://docs.nvidia.com#_CPPv420SanitizerPatchResult)(*SanitizerCallbackBlockEnter)(void *userdata, uint64_t pc)[#](https://docs.nvidia.com#_CPPv427SanitizerCallbackBlockEnter) Function type for a CUDA block enter callback.

- Param userdata:
Pointer to user data. See

[sanitizerPatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92).- Param pc:
Program counter of the entry point of the block.



-
typedef
[SanitizerPatchResult](https://docs.nvidia.com#_CPPv420SanitizerPatchResult)(*SanitizerCallbackBlockExit)(void *userdata, uint64_t pc)[#](https://docs.nvidia.com#_CPPv426SanitizerCallbackBlockExit) Function type for a CUDA block exit callback.

- Param userdata:
Pointer to user data. See

[sanitizerPatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92).- Param pc:
Program counter of the patched instruction.



Function type for a async bulk copy from global to shared memory.

This can be generated by a cp.async.bulk.shared::cluster.global instruction.

All the active threads in a warp have the same parameter values.

- Param userdata:
Pointer to user data. See

[sanitizerPatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92).- Param pc:
Program counter of the patched instruction.

- Param src:
Source global memory address.

- Param dst:
Destination DSMEM address.

- Param barrier:
DSMEM address for the associated mbarrier completion mechanism.

- Param maskAndSize:
is: bits 0:15 - number of 16 bytes blocks requested to be copied bits 16:31 - multicast mask if multicast is in use.

- Param isMulticast:
Boolean value indicating if the operation is a multicast.



Function type for a async bulk copy from shared to global memory.

This can be generated by a cp.async.bulk.global.shared::cta instruction.

All the active threads in a warp have the same parameter values.

- Param userdata:
Pointer to user data. See

[sanitizerPatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92).- Param pc:
Program counter of the patched instruction.

- Param dst:
Destination global memory address.

- Param src:
Source DSMEM address.

- Param maskAndSize:
is bits 0:15 - number of 16 bytes blocks requested to be copied bits 16:31 - byte mask if the cp mask is in use.

- Param hasCpMask:
Boolean value indicating if the operation uses a byte mask.



Function type for a async bulk copy from shared to shered memory.

This can be generated by a cp.async.bulk.shared::cluster.shared::cta instruction.

All the active threads in a warp have the same parameter values.

- Param userdata:
Pointer to user data. See

[sanitizerPatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92).- Param pc:
Program counter of the patched instruction.

- Param src:
Source DSMEM address.

- Param dst:
Destination DSMEM address.

- Param barrier:
DSMEM address for the associated mbarrier completion mechanism.

- Param numBlocks:
Contains the number of 16 bytes blocks requested to be copied.



Function type for a async bulk reduction from shared to global memory.

This can be generated by a cp.reduce.async.bulk.global.shared::cta.bulk_group instruction.

All the active threads in a warp have the same parameter values.

- Param userdata:
Pointer to user data. See

[sanitizerPatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92).- Param pc:
Program counter of the patched instruction.

- Param dst:
Destination DSMEM address.

- Param src:
Source DSMEM address.

- Param barrier:
DSMEM address for the associated mbarrier completion mechanism.

- Param numBlocks:
Contains the number of 16 bytes blocks requested to be copied.



Function type for a async bulk reduction from shared to shered memory.

This can be generated by a cp.reduce.async.bulk.shared::cluster.shared::cta.mbarrier::complete_tx::bytes instruction.

All the active threads in a warp have the same parameter values.

- Param userdata:
Pointer to user data. See

[sanitizerPatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92).- Param pc:
Program counter of the patched instruction.

- Param src:
Source DSMEM address.

- Param dst:
Destination DSMEM address.

- Param barrier:
DSMEM address for the associated mbarrier completion mechanism.

- Param numBlocks:
Contains the number of 16 bytes blocks requested to be copied.



-
typedef
[SanitizerPatchResult](https://docs.nvidia.com#_CPPv420SanitizerPatchResult)(*SanitizerCallbackCacheControl)(void *userdata, uint64_t pc, void *address,[Sanitizer_CacheControlInstructionKind](https://docs.nvidia.com#_CPPv437Sanitizer_CacheControlInstructionKind)kind)[#](https://docs.nvidia.com#_CPPv429SanitizerCallbackCacheControl) Function type for a cache control instruction callback.

- Param userdata:
Pointer to user data. See

[sanitizerPatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92).- Param pc:
Program counter of the patched instruction.

- Param address:
Address of the memory being controlled.

- Param kind:
Type of cache control. See

[Sanitizer_CacheControlInstructionKind](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gad3bcfc1a9d22465613ada149c757b5db).


-
typedef
[SanitizerPatchResult](https://docs.nvidia.com#_CPPv420SanitizerPatchResult)(*SanitizerCallbackCall)(void *userdata, uint64_t pc, uint64_t targetPc, uint32_t flags)[#](https://docs.nvidia.com#_CPPv421SanitizerCallbackCall) Function type for a function call callback.

- Param userdata:
Pointer to user data. See

[sanitizerPatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92).- Param pc:
Program counter of the patched instruction.

- Param targetPc:
PC where the called function is located.

- Param flags:
Contains information about the function call.



-
typedef
[SanitizerPatchResult](https://docs.nvidia.com#_CPPv420SanitizerPatchResult)(*SanitizerCallbackClusterBarrierArrive)(void *userdata, uint64_t pc)[#](https://docs.nvidia.com#_CPPv437SanitizerCallbackClusterBarrierArrive) Function type for a cluster barrier arrive.

This can be generated by a cg::this_cluster().sync() (C++ API), or a barrier.cluster.arrive (PTX API).

- Param userdata:
Pointer to user data. See

[sanitizerPatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92).- Param pc:
Program counter of the patched instruction.



-
typedef
[SanitizerPatchResult](https://docs.nvidia.com#_CPPv420SanitizerPatchResult)(*SanitizerCallbackClusterBarrierWait)(void *userdata, uint64_t pc)[#](https://docs.nvidia.com#_CPPv435SanitizerCallbackClusterBarrierWait) Function type for a cluster barrier wait.

This can be generated by a cg::this_cluster().sync() (C++ API), or a barrier.cluster.wait (PTX API).

- Param userdata:
Pointer to user data. See

[sanitizerPatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92).- Param pc:
Program counter of the patched instruction.

- Retval SANITIZER_PATCH_SUCCESS:
Warp execution continues.

- Retval SANITIZER_PATCH_ERROR:
Warp should be exited.



-
typedef
[SanitizerPatchResult](https://docs.nvidia.com#_CPPv420SanitizerPatchResult)(*SanitizerCallbackCudaBarrier)(void *userdata, uint64_t pc, void *barrier, uint32_t kind, uint32_t data, uint32_t result, uint32_t flags, uint32_t multicastMask)[#](https://docs.nvidia.com#_CPPv428SanitizerCallbackCudaBarrier) Function type for a CUDA Barrier action callback.

- Param userdata:
Pointer to user data. See

[sanitizerPatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92).- Param pc:
Program counter of the patched instruction.

- Param barrier:
Barrier address which can be used as a unique identifier.

- Param kind:
Barrier action type. See

[Sanitizer_CudaBarrierInstructionKind](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga505b1abbfde6d1d66fba877f5ce9b5f3).- Param data:
Kind-specific payload. See

[Sanitizer_CudaBarrierInstructionKind](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga505b1abbfde6d1d66fba877f5ce9b5f3)for the meaning of this field per`kind`

(for example arrival count for arrive-family kinds).- Param result:
Unused for this callback type.

- Param flags:
Contains additional information about the barrier action. See

[Sanitizer_CudaBarrierFlags](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaffcd643218914203431781ba3ae46b70)to interpret this value.- Param multicastMask:
When the SANITIZER_CUDA_BARRIER_FLAG_MULTICAST bit is set in

`flags`

, this is the multicast target mask for the operation. Zero otherwise.


-
typedef
[SanitizerPatchResult](https://docs.nvidia.com#_CPPv420SanitizerPatchResult)(*SanitizerCallbackCudaBarrierAttempt)(void *userdata, uint64_t pc, void *barrier, uint32_t kind, uint32_t data, uint32_t result, uint32_t flags, uint32_t multicastMask)[#](https://docs.nvidia.com#_CPPv435SanitizerCallbackCudaBarrierAttempt) Function type for a CUDA Barrier action callback.

- Param userdata:
Pointer to user data. See

[sanitizerPatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92).- Param pc:
Program counter of the patched instruction.

- Param barrier:
Barrier address which can be used as a unique identifier.

- Param kind:
Barrier action type. See

[Sanitizer_CudaBarrierInstructionKind](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga505b1abbfde6d1d66fba877f5ce9b5f3).- Param data:
Kind-specific payload. See

[Sanitizer_CudaBarrierInstructionKind](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1ga505b1abbfde6d1d66fba877f5ce9b5f3)for the meaning of this field per`kind`

(for example arrival count for arrive-family kinds).- Param result:
In case of a barrier wait, this indicates whether the wait was successful or not.

- Param flags:
Contains additional information about the barrier action. See

[Sanitizer_CudaBarrierFlags](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaffcd643218914203431781ba3ae46b70)to interpret this value.- Param multicastMask:
When the SANITIZER_CUDA_BARRIER_FLAG_MULTICAST bit is set in

`flags`

, this is the multicast target mask for the operation. Zero otherwise.


-
typedef
[SanitizerPatchResult](https://docs.nvidia.com#_CPPv420SanitizerPatchResult)(*SanitizerCallbackDeviceSideFree)(void *userdata, uint64_t pc, void *ptr)[#](https://docs.nvidia.com#_CPPv431SanitizerCallbackDeviceSideFree) Function type for a device-side free call.

Note

This is called prior to the actual call.

- Param userdata:
Pointer to user data. See

[sanitizerPatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92).- Param pc:
Program counter of the patched instruction.

- Param ptr:
Pointer passed to device-side free.



-
typedef
[SanitizerPatchResult](https://docs.nvidia.com#_CPPv420SanitizerPatchResult)(*SanitizerCallbackDeviceSideMalloc)(void *userdata, uint64_t pc, void *allocatedPtr, uint64_t allocatedSize)[#](https://docs.nvidia.com#_CPPv433SanitizerCallbackDeviceSideMalloc) Function type for a device-side malloc call.

Note

This is called after the call has completed.

- Param userdata:
Pointer to user data. See

[sanitizerPatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92).- Param pc:
Program counter of the patched instruction.

- Param allocatedPtr:
Pointer returned by device-side malloc.

- Param allocatedSize:
Size requested by the user to device-side malloc.



-
typedef
[SanitizerPatchResult](https://docs.nvidia.com#_CPPv420SanitizerPatchResult)(*SanitizerCallbackMatrixMemoryAccess)(void *userdata, uint64_t pc, uint32_t address, uint32_t accessSize, uint32_t flags, uint32_t count, const void *pNewValue)[#](https://docs.nvidia.com#_CPPv435SanitizerCallbackMatrixMemoryAccess) Function type for a matrix shared memory access callback.

- Param userdata:
Pointer to user data. See

[sanitizerPatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92).- Param pc:
Program counter of the patched instruction.

- Param address:
Address of the shared memory being read or written. This is an offset within the shared memory window.

- Param accessSize:
Size of the access in bytes. Valid value is 16.

- Param flags:
Contains information about the type of access. See Sanitizer_DeviceMemoryFlags to interpret this value.

- Param count:
Number of matrices accessed.

- Param pNewValue:
Pointer to the new value being written if the access is a write. If the access is a read or an atomic, the pointer will be NULL.



-
typedef
[SanitizerPatchResult](https://docs.nvidia.com#_CPPv420SanitizerPatchResult)(*SanitizerCallbackMemcpyAsync)(void *userdata, uint64_t pc, void *src, uint32_t dst, uint32_t accessSize)[#](https://docs.nvidia.com#_CPPv428SanitizerCallbackMemcpyAsync) Function type for a global to shared memory asynchronous copy.

- Param userdata:
Pointer to user data. See

[sanitizerPatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92).- Param pc:
Program counter of the patched instruction.

- Param src:
Address of the global memory being read. This can be NULL if src-size is 0.

- Param dst:
Address of the shared memory being written. This is an offset within the shared memory window.

- Param accessSize:
Size of the access in bytes. Valid values are 4, 8 and 16.



-
typedef
[SanitizerPatchResult](https://docs.nvidia.com#_CPPv420SanitizerPatchResult)(*SanitizerCallbackMemcpyAsyncBarrier)(void *userdata, uint64_t pc, uint32_t barrier)[#](https://docs.nvidia.com#_CPPv435SanitizerCallbackMemcpyAsyncBarrier) Function type for a cuda barrier used for mbarrier completion.

This can be generated by cp.async.mbarrier.arrive.

- Param userdata:
Pointer to user data. See

[sanitizerPatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92).- Param pc:
Program counter of the patched instruction.

- Param barrier:
Shared memory address of the barrier.



-
typedef
[SanitizerPatchResult](https://docs.nvidia.com#_CPPv420SanitizerPatchResult)(*SanitizerCallbackMemoryAccess)(void *userdata, uint64_t pc, void *ptr, uint32_t accessSize, uint32_t flags, const void *pData)[#](https://docs.nvidia.com#_CPPv429SanitizerCallbackMemoryAccess) Function type for a memory access callback.

- Param userdata:
Pointer to user data. See

[sanitizerPatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92).- Param pc:
Program counter of the patched instruction.

- Param ptr:
Address of the memory being accessed. For local or shared memory access, this is the offset within the local or shared memory window.

- Param accessSize:
Size of the access in bytes. Valid values are 1, 2, 4, 8, and 16.

- Param flags:
Contains information about the type of access. See Sanitizer_DeviceMemoryFlags to interpret this value.

- Param pData:
Pointer which value depends on the type of access:

If the access is a write,

`pData`

points to the new value being written.If the access is a read and

`pData`

is not`NULL`

, then it points to a 32-bit mask of loaded bytes being used (padding bytes will not appear).If the access is an atomic, the pointer will be

`NULL`

.



Function type for a memset on shared memory.

This can be generated by st.bulk.

All the active threads in a warp have the same parameter values.

- Param userdata:
Pointer to user data. See

[sanitizerPatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92).- Param pc:
Program counter of the patched instruction.

- Param dst:
Destination shared memory address.

- Param numBlocks:
Number of 8 byte blocks to be set to zero.



-
typedef
[SanitizerPatchResult](https://docs.nvidia.com#_CPPv420SanitizerPatchResult)(*SanitizerCallbackPipelineCommit)(void *userdata, uint64_t pc)[#](https://docs.nvidia.com#_CPPv431SanitizerCallbackPipelineCommit) Function type for a pipeline commit.

This can be generated by a pipeline::producer_commit (C++ API), a pipeline_commit (C API) or a cp.async.commit_group (PTX API).

- Param userdata:
Pointer to user data. See

[sanitizerPatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92).- Param pc:
Program counter of the patched instruction.



-
typedef
[SanitizerPatchResult](https://docs.nvidia.com#_CPPv420SanitizerPatchResult)(*SanitizerCallbackPipelineWait)(void *userdata, uint64_t pc, uint32_t groups)[#](https://docs.nvidia.com#_CPPv429SanitizerCallbackPipelineWait) Function type for a pipeline wait.

This can be generated by a pipeline::consumer_wait (C++ API), a pipeline_wait_prior (C API), cp.async.wait_group or cp.async.wait_all (PTX API).

- Param userdata:
Pointer to user data. See

[sanitizerPatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92).- Param pc:
Program counter of the patched instruction.

- Param groups:
Number of groups the pipeline will wait for. 0 is used to wait for all groups.



-
typedef
[SanitizerPatchResult](https://docs.nvidia.com#_CPPv420SanitizerPatchResult)(*SanitizerCallbackRet)(void *userdata, uint64_t pc)[#](https://docs.nvidia.com#_CPPv420SanitizerCallbackRet) Function type for a function return callback.

- Param userdata:
Pointer to user data. See

[sanitizerPatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92).- Param pc:
Program counter of the patched instruction.



-
typedef
[SanitizerPatchResult](https://docs.nvidia.com#_CPPv420SanitizerPatchResult)(*SanitizerCallbackSetSmemSize)(void *userdata, uint64_t pc, uint32_t size)[#](https://docs.nvidia.com#_CPPv428SanitizerCallbackSetSmemSize) Function type for setting the shared memory size allocated to a block.

This can be generated by a setsmemsize.sync instruction.

- Param userdata:
Pointer to user data. See

[sanitizerPatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92).- Param pc:
Program counter of the patched instruction.

- Param size:
Requested size in bytes.



-
typedef
[SanitizerPatchResult](https://docs.nvidia.com#_CPPv420SanitizerPatchResult)(*SanitizerCallbackShfl)(void *userdata, uint64_t pc)[#](https://docs.nvidia.com#_CPPv421SanitizerCallbackShfl) Function type for a shfl callback.

- Param userdata:
Pointer to user data. See

[sanitizerPatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92).- Param pc:
Program counter of the patched instruction.



-
typedef
[SanitizerPatchResult](https://docs.nvidia.com#_CPPv420SanitizerPatchResult)(*SanitizerCallbackSyncwarp)(void *userdata, uint64_t pc, uint32_t mask)[#](https://docs.nvidia.com#_CPPv425SanitizerCallbackSyncwarp) Function type for a syncwarp callback.

- Param userdata:
Pointer to user data. See

[sanitizerPatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92).- Param pc:
Program counter of the patched instruction.

- Param mask:
Thread mask passed to __syncwarp().



-
typedef
[SanitizerPatchResult](https://docs.nvidia.com#_CPPv420SanitizerPatchResult)(*SanitizerCallbackTensorCoreBarrier)(void *userdata, uint64_t pc, uint32_t barrier, uint32_t isMulticast, uint32_t multicastMask)[#](https://docs.nvidia.com#_CPPv434SanitizerCallbackTensorCoreBarrier) Function type for a Blackwell tensor core barrier.

This can be generated by a tcgen05.commit instruction.

All the active threads in a warp have the same parameter values.

- Param userdata:
Pointer to user data. See

[sanitizerPatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92).- Param pc:
Program counter of the patched instruction.

- Param barrier:
DSMEM address for the associated mbarrier completion mechanism.

- Param isMulticast:
Boolean value indicating if the operation is a multicast.

- Param multicastMask:
Multicast mask, if isMulticast is true.



-
typedef
[SanitizerPatchResult](https://docs.nvidia.com#_CPPv420SanitizerPatchResult)(*SanitizerCallbackTensorMemoryLoad)(void *pUserData, uint64_t pc, uint64_t pTensorMap, uint32_t dst, uint32_t barrier, int32_t coord0, int32_t coord1, int32_t coord2, int32_t coord3, int32_t coord4, uint32_t dim, uint32_t isMulticast, uint32_t maskAndIm2ColArgs, uint32_t loadMode)[#](https://docs.nvidia.com#_CPPv433SanitizerCallbackTensorMemoryLoad)

-
typedef
[SanitizerPatchResult](https://docs.nvidia.com#_CPPv420SanitizerPatchResult)(*SanitizerCallbackWarpgroupFence)(void *userdata, uint64_t pc, uint32_t warpMask)[#](https://docs.nvidia.com#_CPPv431SanitizerCallbackWarpgroupFence) Function type for a warpgroup MMA fence.

This can be generated by a wgmma.fence in PTX.

- Param userdata:
Pointer to user data. See

[sanitizerPatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92).- Param pc:
Program counter of the patched instruction.

- Param warpMask:
Mask of threads that will perform the fence operation. Expected values are either 0x0 or 0xffffffff (full). The value is expected to be the same across the warpgroup. Other values can be reported but signal a programming error in the target application.



-
typedef
[SanitizerPatchResult](https://docs.nvidia.com#_CPPv420SanitizerPatchResult)(*SanitizerCallbackWarpgroupMMAAsync)(void *userdata, uint64_t pc, uint32_t addressMatrixA, uint32_t sizeMatrixA, uint32_t addressMatrixB, uint32_t sizeMatrixB, uint32_t flags, uint32_t warpMask)[#](https://docs.nvidia.com#_CPPv434SanitizerCallbackWarpgroupMMAAsync) Function type for a warpgroup aligned async MMA.

This can be generated by a wgmma.mma_async in PTX.

- Param userdata:
Pointer to user data. See

[sanitizerPatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92).- Param pc:
Program counter of the patched instruction.

- Param addressMatrixA:
Address in shared memory of the matrix A being read. This field is only valid if sizeMatrixA is non-zero and warpMask is full.

- Param sizeMatrixA:
Size of the matrix A in shared memory. A value of 0 means that the matrix A is read from registers instead.

- Param addressMatrixB:
Address in shared memory of the matrix B being read. This field is only valid if warpMask is full.

- Param sizeMatrixB:
Size of the matrix B in shared memory. The value will always be non-zero.

- Param flags:
Type is

`Sanitizer_WarpgroupMMAAsyncFlags`

. Provide information about the access. These flags are to be taken into account even if the warpMask is zero.- Param warpMask:
Mask of threads that will perform the operation and read the operands. Expected values are either 0x0 or 0xffffffff (full). The value is expected to be the same across the warpgroup. Other values can be reported but signal a programming error in the target application.



-
typedef
[SanitizerPatchResult](https://docs.nvidia.com#_CPPv420SanitizerPatchResult)(*SanitizerCallbackWarpgroupWaitGroup)(void *userdata, uint64_t pc, uint32_t numGroups, uint32_t warpMask)[#](https://docs.nvidia.com#_CPPv435SanitizerCallbackWarpgroupWaitGroup) Function type for a warpgroup MMA wait group.

This can be generated by a wgmma.wait_group in PTX.

- Param userdata:
Pointer to user data. See

[sanitizerPatchModule](https://docs.nvidia.com#group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i_1gaacc3ec25dd89f46c9bfbc3ae4ee94c92).- Param pc:
Program counter of the patched instruction.

- Param numGroups:
Maximum number of group that will be left pending after the operation. A value of zero means that all MMA async of the warpgroup are guaranteed to have completed after the operation.

- Param warpMask:
Mask of threads for which the expected values are either 0x0 or 0xffffffff (full). The value is expected to be the same across the warpgroup. Other values can be reported but signal a programming error in the target application. If the value is valid, the value has no influence on the operation.



-
typedef struct Sanitizer_Launch_st *Sanitizer_LaunchHandle
[#](https://docs.nvidia.com#_CPPv422Sanitizer_LaunchHandle)

## Enumerations[#](https://docs.nvidia.com#id2)

-
enum SanitizerPatchResult
[#](https://docs.nvidia.com#_CPPv420SanitizerPatchResult) Sanitizer patch result codes.

Error and result codes returned by Sanitizer patches. If a patch returns SANITIZER_PATCH_ERROR, the full warp which the thread belongs to will be exited.

*Values:*-
enumerator SANITIZER_PATCH_SUCCESS
[#](https://docs.nvidia.com#_CPPv4N20SanitizerPatchResult23SANITIZER_PATCH_SUCCESSE) No error.


-
enumerator SANITIZER_PATCH_ERROR
[#](https://docs.nvidia.com#_CPPv4N20SanitizerPatchResult21SANITIZER_PATCH_ERRORE) An error was detected in the patch.


-
enumerator SANITIZER_PATCH_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N20SanitizerPatchResult25SANITIZER_PATCH_FORCE_INTE)

-
enumerator SANITIZER_PATCH_SUCCESS

-
enum Sanitizer_BarrierFlags
[#](https://docs.nvidia.com#_CPPv422Sanitizer_BarrierFlags) Flags describing a barrier.

Flags describing a barrier. These values are to be or-combined in the value of

**flags**for a SanitizerCallbackBarrier callback.*Values:*-
enumerator SANITIZER_BARRIER_FLAG_NONE
[#](https://docs.nvidia.com#_CPPv4N22Sanitizer_BarrierFlags27SANITIZER_BARRIER_FLAG_NONEE) Empty flag.


-
enumerator SANITIZER_BARRIER_FLAG_UNALIGNED_ALLOWED
[#](https://docs.nvidia.com#_CPPv4N22Sanitizer_BarrierFlags40SANITIZER_BARRIER_FLAG_UNALIGNED_ALLOWEDE) Specifies that the barrier can be called unaligned.

This flag is only valid on SM 7.0 and above.


-
enumerator SANITIZER_BARRIER_FLAG_IS_SYNCHRONIZING
[#](https://docs.nvidia.com#_CPPv4N22Sanitizer_BarrierFlags39SANITIZER_BARRIER_FLAG_IS_SYNCHRONIZINGE) Specifies that the barrier is synchronizing (i.e., it is not a non-blocking barrier).


-
enumerator SANITIZER_BARRIER_FLAG_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N22Sanitizer_BarrierFlags32SANITIZER_BARRIER_FLAG_FORCE_INTE)

-
enumerator SANITIZER_BARRIER_FLAG_NONE

-
enum Sanitizer_CacheControlInstructionKind
[#](https://docs.nvidia.com#_CPPv437Sanitizer_CacheControlInstructionKind) Cache control action.

*Values:*-
enumerator SANITIZER_CACHE_CONTROL_INVALID
[#](https://docs.nvidia.com#_CPPv4N37Sanitizer_CacheControlInstructionKind31SANITIZER_CACHE_CONTROL_INVALIDE) Invalid action ID.


-
enumerator SANITIZER_CACHE_CONTROL_L1_PREFETCH
[#](https://docs.nvidia.com#_CPPv4N37Sanitizer_CacheControlInstructionKind35SANITIZER_CACHE_CONTROL_L1_PREFETCHE) Prefetch to L1.


-
enumerator SANITIZER_CACHE_CONTROL_L2_PREFETCH
[#](https://docs.nvidia.com#_CPPv4N37Sanitizer_CacheControlInstructionKind35SANITIZER_CACHE_CONTROL_L2_PREFETCHE) Prefetch to L2.


-
enumerator SANITIZER_CACHE_CONTROL_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N37Sanitizer_CacheControlInstructionKind33SANITIZER_CACHE_CONTROL_FORCE_INTE)

-
enumerator SANITIZER_CACHE_CONTROL_INVALID

-
enum Sanitizer_CallFlags
[#](https://docs.nvidia.com#_CPPv419Sanitizer_CallFlags) Flags describing a function call.

Flags describing a function call. These values are to be or-combined in the value of

**flags**for a SanitizerCallbackCall callback.*Values:*-
enumerator SANITIZER_CALL_FLAG_NONE
[#](https://docs.nvidia.com#_CPPv4N19Sanitizer_CallFlags24SANITIZER_CALL_FLAG_NONEE) Empty flag.


-
enumerator SANITIZER_CALL_FLAG_UNALIGNED_ALLOWED
[#](https://docs.nvidia.com#_CPPv4N19Sanitizer_CallFlags37SANITIZER_CALL_FLAG_UNALIGNED_ALLOWEDE) Specifies that barriers within this function call can be called unaligned.

This flag is only valid on SM 7.0 and above.


-
enumerator SANITIZER_CALL_FLAG_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N19Sanitizer_CallFlags29SANITIZER_CALL_FLAG_FORCE_INTE)

-
enumerator SANITIZER_CALL_FLAG_NONE

-
enum Sanitizer_CudaBarrierFlags
[#](https://docs.nvidia.com#_CPPv426Sanitizer_CudaBarrierFlags) Flags describing a CUDA Barrier action.

Flags describing a CUDA Barrier action. These values are to be or-combined in the value of

**flags**for a SanitizerCallbackCudaBarrier or SanitizerCallbackCudaBarrierAttempt callback.*Values:*-
enumerator SANITIZER_CUDA_BARRIER_FLAG_NONE
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CudaBarrierFlags32SANITIZER_CUDA_BARRIER_FLAG_NONEE) Empty flag.


-
enumerator SANITIZER_CUDA_BARRIER_FLAG_UNIFORM
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CudaBarrierFlags35SANITIZER_CUDA_BARRIER_FLAG_UNIFORME) Set when the arrive operation is issued once for the whole warp rather than once per thread.

All participating threads in the warp share the same

**barrier**address.

-
enumerator SANITIZER_CUDA_BARRIER_FLAG_MULTICAST
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CudaBarrierFlags37SANITIZER_CUDA_BARRIER_FLAG_MULTICASTE) Set when the arrive operation is a multicast variant.

The multicast target mask is provided in

**multicastMask**of the callback.

-
enumerator SANITIZER_CUDA_BARRIER_FLAG_USE_POP_COUNT
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CudaBarrierFlags41SANITIZER_CUDA_BARRIER_FLAG_USE_POP_COUNTE) Specifies that

`data`

is a per-thread arrival count rather than a per-warp total.Can only be set when SANITIZER_CUDA_BARRIER_FLAG_UNIFORM is also set.


-
enumerator SANITIZER_CUDA_BARRIER_FLAG_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N26Sanitizer_CudaBarrierFlags37SANITIZER_CUDA_BARRIER_FLAG_FORCE_INTE)

-
enumerator SANITIZER_CUDA_BARRIER_FLAG_NONE

-
enum Sanitizer_CudaBarrierInstructionKind
[#](https://docs.nvidia.com#_CPPv436Sanitizer_CudaBarrierInstructionKind) CUDA Barrier action kind.

Refer to the CUDA Barrier interface section of the CUDA toolkit documentation for a more extensive description of these actions. The

**data**argument passed to SanitizerCallbackCudaBarrier and SanitizerCallbackCudaBarrierAttempt carries kind-specific information, as documented per-value below. Action kinds that do not document a use of**data**should treat its value as unspecified.*Values:*-
enumerator SANITIZER_CUDA_BARRIER_INVALID
[#](https://docs.nvidia.com#_CPPv4N36Sanitizer_CudaBarrierInstructionKind30SANITIZER_CUDA_BARRIER_INVALIDE) Invalid action ID.


-
enumerator SANITIZER_CUDA_BARRIER_INIT
[#](https://docs.nvidia.com#_CPPv4N36Sanitizer_CudaBarrierInstructionKind27SANITIZER_CUDA_BARRIER_INITE) Barrier initialization.


-
enumerator SANITIZER_CUDA_BARRIER_ARRIVE
[#](https://docs.nvidia.com#_CPPv4N36Sanitizer_CudaBarrierInstructionKind29SANITIZER_CUDA_BARRIER_ARRIVEE) Barrier arrive operation.

On Hopper and newer architectures, Barrier data is the count argument to the arrive-on operation.


-
enumerator SANITIZER_CUDA_BARRIER_ARRIVE_DROP
[#](https://docs.nvidia.com#_CPPv4N36Sanitizer_CudaBarrierInstructionKind34SANITIZER_CUDA_BARRIER_ARRIVE_DROPE) Barrier arrive and drop operation.

On Hopper and newer architectures, Barrier data is the count argument to the arrive-on operation.


-
enumerator SANITIZER_CUDA_BARRIER_ARRIVE_NOCOMPLETE
[#](https://docs.nvidia.com#_CPPv4N36Sanitizer_CudaBarrierInstructionKind40SANITIZER_CUDA_BARRIER_ARRIVE_NOCOMPLETEE) Barrier arrive operation without phase completion.

Barrier data is the count argument to the arrive-on operation.


-
enumerator SANITIZER_CUDA_BARRIER_ARRIVE_DROP_NOCOMPLETE
[#](https://docs.nvidia.com#_CPPv4N36Sanitizer_CudaBarrierInstructionKind45SANITIZER_CUDA_BARRIER_ARRIVE_DROP_NOCOMPLETEE) Barrier arrive and drop operation without phase completion.

Barrier data is the count argument to the arrive-on operation.


-
enumerator SANITIZER_CUDA_BARRIER_WAIT
[#](https://docs.nvidia.com#_CPPv4N36Sanitizer_CudaBarrierInstructionKind27SANITIZER_CUDA_BARRIER_WAITE) Barrier wait operation.


-
enumerator SANITIZER_CUDA_BARRIER_INVALIDATE
[#](https://docs.nvidia.com#_CPPv4N36Sanitizer_CudaBarrierInstructionKind33SANITIZER_CUDA_BARRIER_INVALIDATEE) Barrier invalidation.


-
enumerator SANITIZER_CUDA_BARRIER_CP_ASYNC_ARRIVE
[#](https://docs.nvidia.com#_CPPv4N36Sanitizer_CudaBarrierInstructionKind38SANITIZER_CUDA_BARRIER_CP_ASYNC_ARRIVEE) Barrier arrive operation issued from cp.async.mbarrier.arrive.

Barrier data is the count argument to the arrive-on operation.


-
enumerator SANITIZER_CUDA_BARRIER_CP_ASYNC_ARRIVE_NO_INC
[#](https://docs.nvidia.com#_CPPv4N36Sanitizer_CudaBarrierInstructionKind45SANITIZER_CUDA_BARRIER_CP_ASYNC_ARRIVE_NO_INCE) Barrier arrive operation issued from cp.async.mbarrier.arrive.noinc.

Barrier data is the count argument to the arrive-on operation.


-
enumerator SANITIZER_CUDA_BARRIER_COMPLETE_TX
[#](https://docs.nvidia.com#_CPPv4N36Sanitizer_CudaBarrierInstructionKind34SANITIZER_CUDA_BARRIER_COMPLETE_TXE) Barrier complete transaction operation.

Barrier data is the transaction count argument to the arrive-on operation.


-
enumerator SANITIZER_CUDA_BARRIER_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N36Sanitizer_CudaBarrierInstructionKind32SANITIZER_CUDA_BARRIER_FORCE_INTE)

-
enumerator SANITIZER_CUDA_BARRIER_INVALID

-
enum Sanitizer_DeviceMemoryFlags
[#](https://docs.nvidia.com#_CPPv427Sanitizer_DeviceMemoryFlags) Flags describing a memory access.

Flags describing a memory access. These values are to be or-combined in the value of

**flags**for a SanitizerCallbackMemoryAccess callback.*Values:*-
enumerator SANITIZER_MEMORY_DEVICE_FLAG_NONE
[#](https://docs.nvidia.com#_CPPv4N27Sanitizer_DeviceMemoryFlags33SANITIZER_MEMORY_DEVICE_FLAG_NONEE) Empty flag.


-
enumerator SANITIZER_MEMORY_DEVICE_FLAG_READ
[#](https://docs.nvidia.com#_CPPv4N27Sanitizer_DeviceMemoryFlags33SANITIZER_MEMORY_DEVICE_FLAG_READE) Specifies that the access is a read.


-
enumerator SANITIZER_MEMORY_DEVICE_FLAG_WRITE
[#](https://docs.nvidia.com#_CPPv4N27Sanitizer_DeviceMemoryFlags34SANITIZER_MEMORY_DEVICE_FLAG_WRITEE) Specifies that the access is a write.


-
enumerator SANITIZER_MEMORY_DEVICE_FLAG_ATOMSYS
[#](https://docs.nvidia.com#_CPPv4N27Sanitizer_DeviceMemoryFlags36SANITIZER_MEMORY_DEVICE_FLAG_ATOMSYSE) Specifies that the access is a system-scoped atomic.


-
enumerator SANITIZER_MEMORY_DEVICE_FLAG_PREFETCH
[#](https://docs.nvidia.com#_CPPv4N27Sanitizer_DeviceMemoryFlags37SANITIZER_MEMORY_DEVICE_FLAG_PREFETCHE) Specifies that the access is a cache prefetch.


-
enumerator SANITIZER_MEMORY_DEVICE_FLAG_SCOPE_CTA
[#](https://docs.nvidia.com#_CPPv4N27Sanitizer_DeviceMemoryFlags38SANITIZER_MEMORY_DEVICE_FLAG_SCOPE_CTAE) Specifies that the access is strong with CTA scope.


-
enumerator SANITIZER_MEMORY_DEVICE_FLAG_SCOPE_SM
[#](https://docs.nvidia.com#_CPPv4N27Sanitizer_DeviceMemoryFlags37SANITIZER_MEMORY_DEVICE_FLAG_SCOPE_SME) Specifies that the access is strong with SM scope.


-
enumerator SANITIZER_MEMORY_DEVICE_FLAG_SCOPE_GPU
[#](https://docs.nvidia.com#_CPPv4N27Sanitizer_DeviceMemoryFlags38SANITIZER_MEMORY_DEVICE_FLAG_SCOPE_GPUE) Specifies that the access is strong with GPU scope.


-
enumerator SANITIZER_MEMORY_DEVICE_FLAG_SCOPE_SYS
[#](https://docs.nvidia.com#_CPPv4N27Sanitizer_DeviceMemoryFlags38SANITIZER_MEMORY_DEVICE_FLAG_SCOPE_SYSE) Specifies that the access is strong with system scope.


-
enumerator SANITIZER_MEMORY_DEVICE_FLAG_ATOMIC_WRITE_ONLY
[#](https://docs.nvidia.com#_CPPv4N27Sanitizer_DeviceMemoryFlags46SANITIZER_MEMORY_DEVICE_FLAG_ATOMIC_WRITE_ONLYE) Specifies that the access is atomic but it only writes the memory.


-
enumerator SANITIZER_MEMORY_DEVICE_FLAG_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N27Sanitizer_DeviceMemoryFlags38SANITIZER_MEMORY_DEVICE_FLAG_FORCE_INTE)

-
enumerator SANITIZER_MEMORY_DEVICE_FLAG_NONE

-
enum Sanitizer_FunctionLoadedStatus
[#](https://docs.nvidia.com#_CPPv430Sanitizer_FunctionLoadedStatus) *Values:*-
enumerator SANITIZER_FUNCTION_NOT_LOADED
[#](https://docs.nvidia.com#_CPPv4N30Sanitizer_FunctionLoadedStatus29SANITIZER_FUNCTION_NOT_LOADEDE) The function is not loaded.


-
enumerator SANITIZER_FUNCTION_PARTIALLY_LOADED
[#](https://docs.nvidia.com#_CPPv4N30Sanitizer_FunctionLoadedStatus35SANITIZER_FUNCTION_PARTIALLY_LOADEDE) The function is being loaded.


-
enumerator SANITIZER_FUNCTION_LOADED
[#](https://docs.nvidia.com#_CPPv4N30Sanitizer_FunctionLoadedStatus25SANITIZER_FUNCTION_LOADEDE) The function is fully loaded.


-
enumerator SANITIZER_FUNCTION_LOADED_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N30Sanitizer_FunctionLoadedStatus35SANITIZER_FUNCTION_LOADED_FORCE_INTE)

-
enumerator SANITIZER_FUNCTION_NOT_LOADED

-
enum Sanitizer_InstructionId
[#](https://docs.nvidia.com#_CPPv423Sanitizer_InstructionId) Instrumentation.

Instrumentation. Every entry represent an instruction type or a function call where a callback patch can be inserted.

*Values:*-
enumerator SANITIZER_INSTRUCTION_INVALID
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId29SANITIZER_INSTRUCTION_INVALIDE) Invalid instruction ID.


-
enumerator SANITIZER_INSTRUCTION_BLOCK_ENTER
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId33SANITIZER_INSTRUCTION_BLOCK_ENTERE) CUDA block enter.

This is called prior to any user code. The type of the callback must be SanitizerCallbackBlockEnter.


-
enumerator SANITIZER_INSTRUCTION_BLOCK_EXIT
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId32SANITIZER_INSTRUCTION_BLOCK_EXITE) CUDA block exit.

This is called after all user code has executed. The type of the callback must be SanitizerCallbackBlockExit.


-
enumerator SANITIZER_INSTRUCTION_GLOBAL_MEMORY_ACCESS
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId42SANITIZER_INSTRUCTION_GLOBAL_MEMORY_ACCESSE) Global Memory Access.

This can be a store, load or atomic operation. The type of the callback must be SanitizerCallbackMemoryAccess.


-
enumerator SANITIZER_INSTRUCTION_SHARED_MEMORY_ACCESS
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId42SANITIZER_INSTRUCTION_SHARED_MEMORY_ACCESSE) Shared Memory Access.

This can be a store, load or atomic operation. The type of the callback must be SanitizerCallbackMemoryAccess.


-
enumerator SANITIZER_INSTRUCTION_LOCAL_MEMORY_ACCESS
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId41SANITIZER_INSTRUCTION_LOCAL_MEMORY_ACCESSE) Local Memory Access.

This can be a store or load operation. The type of the callback must be SanitizerCallbackMemoryAccess.


-
enumerator SANITIZER_INSTRUCTION_BARRIER
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId29SANITIZER_INSTRUCTION_BARRIERE) Barrier.

The type of the callback must be SanitizerCallbackBarrier.


-
enumerator SANITIZER_INSTRUCTION_SYNCWARP
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId30SANITIZER_INSTRUCTION_SYNCWARPE) Syncwarp.

The type of the callback must be SanitizerCallbackSyncwarp.


-
enumerator SANITIZER_INSTRUCTION_SHFL
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId26SANITIZER_INSTRUCTION_SHFLE) Shfl.

The type of the callback must be SanitizerCallbackShfl.


-
enumerator SANITIZER_INSTRUCTION_CALL
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId26SANITIZER_INSTRUCTION_CALLE) Function call.

The type of the callback must be SanitizerCallbackCall.


-
enumerator SANITIZER_INSTRUCTION_RET
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId25SANITIZER_INSTRUCTION_RETE) Function return.

The type of the callback must be SanitizerCallbackRet.


-
enumerator SANITIZER_INSTRUCTION_DEVICE_SIDE_MALLOC
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId40SANITIZER_INSTRUCTION_DEVICE_SIDE_MALLOCE) Device-side malloc.

The type of the callback must be SanitizerCallbackDeviceSideMalloc.


-
enumerator SANITIZER_INSTRUCTION_DEVICE_SIDE_FREE
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId38SANITIZER_INSTRUCTION_DEVICE_SIDE_FREEE) Device-side free.

The type of the callback must be SanitizerCallbackDeviceSideFree.


-
enumerator SANITIZER_INSTRUCTION_CUDA_BARRIER
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId34SANITIZER_INSTRUCTION_CUDA_BARRIERE) CUDA Barrier operation.

The type of the callback must be SanitizerCallbackCudaBarrier.


-
enumerator SANITIZER_INSTRUCTION_MEMCPY_ASYNC
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId34SANITIZER_INSTRUCTION_MEMCPY_ASYNCE) Global to shared memory asynchronous copy.

The type of the callback must be SanitizerCallbackMemcpyAsync.


-
enumerator SANITIZER_INSTRUCTION_PIPELINE_COMMIT
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId37SANITIZER_INSTRUCTION_PIPELINE_COMMITE) Pipeline commit.

The type of the callback must be SanitizerCallbackPipelineCommit.


-
enumerator SANITIZER_INSTRUCTION_PIPELINE_WAIT
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId35SANITIZER_INSTRUCTION_PIPELINE_WAITE) Pipeline wait.

The type of the callback must be SanitizerCallbackPipelineWait.


-
enumerator SANITIZER_INSTRUCTION_REMOTE_SHARED_MEMORY_ACCESS
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId49SANITIZER_INSTRUCTION_REMOTE_SHARED_MEMORY_ACCESSE) Remote Shared Memory Access.

This can be a store or load operation. The type of the callback must be SanitizerCallbackMemoryAccess.


-
enumerator SANITIZER_INSTRUCTION_DEVICE_ALIGNED_MALLOC
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId43SANITIZER_INSTRUCTION_DEVICE_ALIGNED_MALLOCE) Device-side aligned malloc.

The type of the callback must be SanitizerCallbackDeviceSideMalloc.


-
enumerator SANITIZER_INSTRUCTION_MATRIX_MEMORY_ACCESS
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId42SANITIZER_INSTRUCTION_MATRIX_MEMORY_ACCESSE) Matrix shared memory access.

The type of the callback must be SanitizerCallbackMatrixMemoryAccess.


-
enumerator SANITIZER_INSTRUCTION_CACHE_CONTROL
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId35SANITIZER_INSTRUCTION_CACHE_CONTROLE) Cache control instruction.

The type of the callback must be SanitizerCallbackCacheControl.


-
enumerator SANITIZER_INSTRUCTION_CLUSTER_BARRIER_ARRIVE
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId44SANITIZER_INSTRUCTION_CLUSTER_BARRIER_ARRIVEE) Cluster barrier arrive instruction.

The type of the callback must be SanitizerCallbackClusterBarrierArrive.


-
enumerator SANITIZER_INSTRUCTION_CLUSTER_BARRIER_WAIT
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId42SANITIZER_INSTRUCTION_CLUSTER_BARRIER_WAITE) Cluster barrier wait instruction.

The type of the callback must be SanitizerCallbackClusterBarrierWait.


-
enumerator SANITIZER_INSTRUCTION_WARPGROUP_MMA_ASYNC
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId41SANITIZER_INSTRUCTION_WARPGROUP_MMA_ASYNCE) Warpgroup aligned async MMA instruction.

The type of the callback must be SanitizerCallbackWarpgroupMMAAsync.


-
enumerator SANITIZER_INSTRUCTION_WARPGROUP_WAIT_GROUP
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId42SANITIZER_INSTRUCTION_WARPGROUP_WAIT_GROUPE) Warpgroup wait MMA group instruction.

The type of the callback must be SanitizerCallbackWarpgroupWaitGroup.


-
enumerator SANITIZER_INSTRUCTION_WARPGROUP_FENCE
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId37SANITIZER_INSTRUCTION_WARPGROUP_FENCEE) Warpgroup fence instruction.

The type of the callback must be SanitizerCallbackWarpgroupFence.


-
enumerator SANITIZER_INSTRUCTION_ASYNC_STORE
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId33SANITIZER_INSTRUCTION_ASYNC_STOREE) Asynchronous store instruction.

The type of the callback must be SanitizerCallbackAsyncStore.


-
enumerator SANITIZER_INSTRUCTION_ASYNC_REDUCTION
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId37SANITIZER_INSTRUCTION_ASYNC_REDUCTIONE) Asynchronous reduction instruction.

The type of the callback must be SanitizerCallbackAsyncReduction.


-
enumerator SANITIZER_INSTRUCTION_SET_SHARED_MEMORY_SIZE
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId44SANITIZER_INSTRUCTION_SET_SHARED_MEMORY_SIZEE) Set the shared memory size allocated to a block instruction.

The type of the callback must be SanitizerCallbackSetSmemSize.


-
enumerator SANITIZER_INSTRUCTION_BARRIER_RELEASE
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId37SANITIZER_INSTRUCTION_BARRIER_RELEASEE) Barrier after it is released.

The type of the callback must be SanitizerCallbackBarrier.


-
enumerator SANITIZER_INSTRUCTION_BULK_COPY_GLOBAL_TO_SHARED
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId48SANITIZER_INSTRUCTION_BULK_COPY_GLOBAL_TO_SHAREDE) Bulk copy instruction from global to shared memory.

The type of the callback must be SanitizerCallbackBulkCopyGlobalToShared.


-
enumerator SANITIZER_INSTRUCTION_TENSOR_CORE_BARRIER
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId41SANITIZER_INSTRUCTION_TENSOR_CORE_BARRIERE) Tensor Core barrier.

The type of the callback must be SanitizerCallbackTensorCoreBarrier.


-
enumerator SANITIZER_INSTRUCTION_MEMSET_SHARED
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId35SANITIZER_INSTRUCTION_MEMSET_SHAREDE) Bulk copy instruction from global to shared memory.

The type of the callback must be SanitizerCallbackMemsetShared.


-
enumerator SANITIZER_INSTRUCTION_SYNCWARP_RELEASE
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId38SANITIZER_INSTRUCTION_SYNCWARP_RELEASEE) Syncwarp after it is released.

The type of the callback must be SanitizerCallbackSyncwarp.


-
enumerator SANITIZER_INSTRUCTION_MEMCPY_ASYNC_BARRIER
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId42SANITIZER_INSTRUCTION_MEMCPY_ASYNC_BARRIERE) Usage of a Cuda Barrier for memcpy async completion.

The type of the callback must be SanitizerCallbackMemcpyAsyncBarrier.


-
enumerator SANITIZER_INSTRUCTION_BULK_COPY_SHARED_TO_GLOBAL
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId48SANITIZER_INSTRUCTION_BULK_COPY_SHARED_TO_GLOBALE) Bulk copy instruction from shared to global memory.

The type of the callback must be SanitizerCallbackBulkCopySharedToGlobal.


-
enumerator SANITIZER_INSTRUCTION_BULK_COPY_SHARED_TO_SHARED
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId48SANITIZER_INSTRUCTION_BULK_COPY_SHARED_TO_SHAREDE) Bulk copy instruction from shared to shared memory.

The type of the callback must be SanitizerCallbackBulkCopySharedToShared.


-
enumerator SANITIZER_INSTRUCTION_BULK_REDUCTION_SHARED_TO_GLOBAL
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId53SANITIZER_INSTRUCTION_BULK_REDUCTION_SHARED_TO_GLOBALE) Bulk reduction instruction from shared to global memory.

The type of the callback must be SanitizerCallbackBulkReductionSharedToGlobal.


-
enumerator SANITIZER_INSTRUCTION_BULK_REDUCTION_SHARED_TO_SHARED
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId53SANITIZER_INSTRUCTION_BULK_REDUCTION_SHARED_TO_SHAREDE) Bulk reduction instruction from shared to shared memory.

The type of the callback must be SanitizerCallbackBulkReductionSharedToShared.


-
enumerator SANITIZER_INSTRUCTION_CUDA_BARRIER_ATTEMPT
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId42SANITIZER_INSTRUCTION_CUDA_BARRIER_ATTEMPTE) CUDA Barrier operation (potentially unsuccessful).

The type of the callback must be SanitizerCallbackCudaBarrierAttempt.


-
enumerator SANITIZER_INSTRUCTION_CLUSTER_BARRIER_WAIT_ENTRY
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId48SANITIZER_INSTRUCTION_CLUSTER_BARRIER_WAIT_ENTRYE) Entering cluster barrier wait instruction.

The type of the callback must be SanitizerCallbackClusterBarrierWait.


-
enumerator SANITIZER_INSTRUCTION_WARPGROUP_FENCE_RELEASE
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId45SANITIZER_INSTRUCTION_WARPGROUP_FENCE_RELEASEE) Warpgroup fence instruction.

The type of the callback must be SanitizerCallbackWarpgroupFence.


-
enumerator SANITIZER_INSTRUCTION_WARPGROUP_MMA_ASYNC_RELEASE
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId49SANITIZER_INSTRUCTION_WARPGROUP_MMA_ASYNC_RELEASEE) Warpgroup aligned async MMA instruction release.

The type of the callback must be SanitizerCallbackWarpgroupMMAAsync.


-
enumerator SANITIZER_INSTRUCTION_TMA_LOAD
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId30SANITIZER_INSTRUCTION_TMA_LOADE) TMA load instruction.

Copy data from Tensor in global memory to shared memory The type of the callback must be SanitizerCallbackTensorMemoryLoad.


-
enumerator SANITIZER_INSTRUCTION_TMA_STORE
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId31SANITIZER_INSTRUCTION_TMA_STOREE) TMA store instruction.

Copy data from shared memory to Tensor in global memory The type of the callback must be SanitizerCallbackTensorMemoryStore.


-
enumerator SANITIZER_INSTRUCTION_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_InstructionId31SANITIZER_INSTRUCTION_FORCE_INTE)

-
enumerator SANITIZER_INSTRUCTION_INVALID

-
enum Sanitizer_LoadMode
[#](https://docs.nvidia.com#_CPPv418Sanitizer_LoadMode) *Values:*-
enumerator SANITIZER_LOAD_TILED
[#](https://docs.nvidia.com#_CPPv4N18Sanitizer_LoadMode20SANITIZER_LOAD_TILEDE)

-
enumerator SANITIZER_LOAD_IM2COL
[#](https://docs.nvidia.com#_CPPv4N18Sanitizer_LoadMode21SANITIZER_LOAD_IM2COLE)

-
enumerator SANITIZER_LOAD_W128
[#](https://docs.nvidia.com#_CPPv4N18Sanitizer_LoadMode19SANITIZER_LOAD_W128E)

-
enumerator SANITIZER_LOAD_W
[#](https://docs.nvidia.com#_CPPv4N18Sanitizer_LoadMode16SANITIZER_LOAD_WE)

-
enumerator SANITIZER_LOAD_GATHER4
[#](https://docs.nvidia.com#_CPPv4N18Sanitizer_LoadMode22SANITIZER_LOAD_GATHER4E)

-
enumerator SANITIZER_LOAD_TILED

-
enum Sanitizer_WarpgroupMMAAsyncFlags
[#](https://docs.nvidia.com#_CPPv432Sanitizer_WarpgroupMMAAsyncFlags) Flags describing a warpgroup aligned MMA async.

Flags describing a warpgroup aligned MMA async. These values are to be or-combined in the value of

**flags**for a SanitizerCallbackWarpgroupMMAAsync callback.*Values:*-
enumerator SANITIZER_WARPGROUP_MMA_ASYNC_FLAG_NONE
[#](https://docs.nvidia.com#_CPPv4N32Sanitizer_WarpgroupMMAAsyncFlags39SANITIZER_WARPGROUP_MMA_ASYNC_FLAG_NONEE) Empty flag.


-
enumerator SANITIZER_WARPGROUP_MMA_ASYNC_FLAG_COMMIT_GROUP
[#](https://docs.nvidia.com#_CPPv4N32Sanitizer_WarpgroupMMAAsyncFlags47SANITIZER_WARPGROUP_MMA_ASYNC_FLAG_COMMIT_GROUPE) Specifies that the MMA async delimits a MMA async group of which it is the last instruction.

Please refer to the PTX documentation for wgmma_async.commit_group for more details. This property is valid even if the warpMask is zero.


-
enumerator SANITIZER_WARPGROUP_MMA_ASYNC_FLAG_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N32Sanitizer_WarpgroupMMAAsyncFlags44SANITIZER_WARPGROUP_MMA_ASYNC_FLAG_FORCE_INTE)

-
enumerator SANITIZER_WARPGROUP_MMA_ASYNC_FLAG_NONE

## Functions[#](https://docs.nvidia.com#id3)

-
[SanitizerResult](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___r_e_s_u_l_t___a_p_i.html#_CPPv415SanitizerResult)sanitizerAddPatches(*const void *image*,*CUcontext ctx*)[#](https://docs.nvidia.com#_CPPv419sanitizerAddPatchesPKv9CUcontext) Load a module containing patches that can be used by the patching API.

Note

**Thread-safety**: an API user must serialize access to sanitizerAddPatchesFromFile, sanitizerAddPatches, sanitizerPatchInstructions, and sanitizerPatchModule. For example if sanitizerAddPatches(image) and sanitizerPatchInstruction(*, *, cbName) are called concurrently and cbName is intended to be found in the loaded image, the results are undefined.Note

The patches loaded are only valid for the specified CUDA context.

- Parameters:
**image**– Pointer to module data to load. This API supports the same module formats as the cuModuleLoadData and cuModuleLoadFatBinary functions from the CUDA driver API.**ctx**– CUDA context in which to load the patches. If ctx is NULL, the current context will be used.

- Return values:
**SANITIZER_SUCCESS**– on success.**SANITIZER_ERROR_NOT_INITIALIZED**– if unable to initialize the sanitizer.**SANITIZER_ERROR_INVALID_PARAMETER**– if`image`

does not point to a valid CUDA module.



-
[SanitizerResult](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___r_e_s_u_l_t___a_p_i.html#_CPPv415SanitizerResult)sanitizerAddPatchesFromFile( *const char *filename*,*CUcontext ctx*,Load a module containing patches that can be used by the patching API.

Note

**Thread-safety**: an API user must serialize access to sanitizerAddPatchesFromFile, sanitizerAddPatches, sanitizerPatchInstructions, and sanitizerPatchModule. For example if sanitizerAddPatchesFromFile(filename) and sanitizerPatchInstruction(*, *, cbName) are called concurrently and cbName is intended to be found in the loaded module, the results are undefined.Note

The patches loaded are only valid for the specified CUDA context.

- Parameters:
**filename**– Path to the module file. This API supports the same module formats as the cuModuleLoad function from the CUDA driver API.**ctx**– CUDA context in which to load the patches. If ctx is NULL, the current context will be used.

- Return values:
**SANITIZER_SUCCESS**– on success**SANITIZER_ERROR_NOT_INITIALIZED**– if unable to initialize the sanitizer**SANITIZER_ERROR_INVALID_PARAMETER**– if`filename`

is not a path to a valid CUDA module.



[#](https://docs.nvidia.com#_CPPv427sanitizerAddPatchesFromFilePKc9CUcontext)

-
[SanitizerResult](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___r_e_s_u_l_t___a_p_i.html#_CPPv415SanitizerResult)sanitizerGetCallbackPcAndSize( *CUcontext ctx*,*const char *deviceCallbackName*,*uint64_t *pc*,*uint64_t *size*,Get PC and size of a device callback.

- Parameters:
**ctx**–**[in]**CUDA context in which the patches were loaded. If ctx is NULL, the current context will be used.**deviceCallbackName**–**[in]**device function callback name.**pc**–**[out]**Callback PC returned.**size**–**[out]**Callback size returned.

- Return values:
**SANITIZER_SUCCESS**– on success.**SANITIZER_ERROR_INVALID_PARAMETER**– if`deviceCallbackName`

function cannot be located, if pc is NULL or if size is NULL.



[#](https://docs.nvidia.com#_CPPv429sanitizerGetCallbackPcAndSize9CUcontextPKcP8uint64_tP8uint64_t)

-
[SanitizerResult](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___r_e_s_u_l_t___a_p_i.html#_CPPv415SanitizerResult)sanitizerGetFunctionLoadedStatus( *CUfunction func*,,[Sanitizer_FunctionLoadedStatus](https://docs.nvidia.com#_CPPv430Sanitizer_FunctionLoadedStatus)*loadingStatusGet the loading status of a function.

Requires a driver version >=515.

- Parameters:
**func**–**[in]**CUDA function for which the loading status is queried.**loadingStatus**–**[out]**Loading status returned.

- Return values:
**SANITIZER_SUCCESS**– on success.**SANITIZER_ERROR_INVALID_PARAMETER**– if`func`

is NULL or if loadingStatus is NULL.**SANITIZER_ERROR_NOT_SUPPORTED**– if the loading status cannot be queried with this driver version.



[#](https://docs.nvidia.com#_CPPv432sanitizerGetFunctionLoadedStatus10CUfunctionP30Sanitizer_FunctionLoadedStatus)

-
[SanitizerResult](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___r_e_s_u_l_t___a_p_i.html#_CPPv415SanitizerResult)sanitizerGetFunctionPcAndSize( *CUmodule module*,*const char *functionName*,*uint64_t *pc*,*uint64_t *size*,Get PC and size of a CUDA function.

- Parameters:
**module**–**[in]**CUDA module containing the function.**functionName**–**[in]**CUDA function name.**pc**–**[out]**Function start program counter (PC) returned.**size**–**[out]**Function size in bytes returned.

- Return values:
**SANITIZER_SUCCESS**– on success.**SANITIZER_ERROR_INVALID_PARAMETER**– if`functionName`

function. cannot be located, if pc is NULL or if size is NULL.



[#](https://docs.nvidia.com#_CPPv429sanitizerGetFunctionPcAndSize8CUmodulePKcP8uint64_tP8uint64_t)

-
[SanitizerResult](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___r_e_s_u_l_t___a_p_i.html#_CPPv415SanitizerResult)sanitizerPatchInstructions( *const*,[Sanitizer_InstructionId](https://docs.nvidia.com#_CPPv423Sanitizer_InstructionId)instructionId*CUmodule module*,*const char *deviceCallbackName*,Set instrumentation points and patches to be applied in a module.

Mark that all instrumentation points matching instructionId are to be patched in order to call the device function identified by deviceCallbackName. It is up to the API client to ensure that this device callback exists and match the correct callback format for this instrumentation point.

Note

**Thread-safety**: an API user must serialize access to sanitizerAddPatchesFromFile, sanitizerAddPatches, sanitizerPatchInstructions, and sanitizerPatchModule. For example if sanitizerAddPatches(fileName) and sanitizerPatchInstruction(*, *, cbName) are called concurrently and cbName is intended to be found in the loaded module, the results are undefined.- Parameters:
**instructionId**– Instrumentation point for which to insert patches**module**– CUDA module to instrument**deviceCallbackName**– Name of the device function callback that the inserted patch will call at the instrumented points. This function is expected to be found in code previously loaded by sanitizerAddPatchesFromFile or sanitizerAddPatches.

- Return values:
**SANITIZER_SUCCESS**– on success.**SANITIZER_ERROR_NOT_INITIALIZED**– if unable to initialize the sanitizer.**SANITIZER_ERROR_INVALID_PARAMETER**– if`module`

is not a CUDA module or if`deviceCallbackName`

function cannot be located.



[#](https://docs.nvidia.com#_CPPv426sanitizerPatchInstructionsK23Sanitizer_InstructionId8CUmodulePKc)

-
[SanitizerResult](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___r_e_s_u_l_t___a_p_i.html#_CPPv415SanitizerResult)sanitizerPatchModule(*CUmodule module*)[#](https://docs.nvidia.com#_CPPv420sanitizerPatchModule8CUmodule) Perform the actual instrumentation of a module.

Perform the instrumentation of a CUDA module based on previous calls to sanitizerPatchInstructions. This function also specifies the device memory buffer to be passed in as userdata to all callback functions.

Note

**Thread-safety**: an API user must serialize access to sanitizerAddPatchesFromFile, sanitizerAddPatches, sanitizerPatchInstructions, and sanitizerPatchModule. For example if sanitizerPatchModule(mod, *) and sanitizerPatchInstruction(*, mod, *) are called concurrently, the results are undefined.- Parameters:
**module**– CUDA module to instrument.- Return values:
**SANITIZER_SUCCESS**– on success.**SANITIZER_ERROR_INVALID_PARAMETER**– if`module`

is not a CUDA module.



-
[SanitizerResult](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___r_e_s_u_l_t___a_p_i.html#_CPPv415SanitizerResult)sanitizerSetCallbackData( *CUfunction kernel*,*const void *userdata*,Specifies the user data pointer for callbacks.

Mark all subsequent launches of

`kernel`

to use`userdata`

pointer as the device memory buffer to pass in to callback functions.- Parameters:
**kernel**– CUDA function to link to user data. Callbacks in subsequent launches on this kernel will use`userdata`

as callback data.**userdata**– Device memory buffer. This data will be passed to callback functions via the`userdata`

parameter.

- Return values:
**SANITIZER_SUCCESS**– on success.


[#](https://docs.nvidia.com#_CPPv424sanitizerSetCallbackData10CUfunctionPKv)

-
[SanitizerResult](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___r_e_s_u_l_t___a_p_i.html#_CPPv415SanitizerResult)sanitizerSetDeviceGraphData( *CUgraphExec graphExec*,,[Sanitizer_StreamHandle](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___s_t_r_e_a_m___a_p_i.html#_CPPv422Sanitizer_StreamHandle)stream*const void *userdata*,Specifies the user data pointer accessible from callbacks in the device-launched graphs launched by the specified host-launched graphExec.

Mark all subsequent launch of

`graphExec`

to make available`userdata`

in device callbacks from device-launched graphs.`userdata`

will not be set in the callback userdata parameter but must be accessed through another mean instead. Please refer to the Sanitizer API reference manual. This function is only available if the driver version is 535 or newer.- Parameters:
**graphExec**– CUDA graphExec that will launch CUDA graphs from the device.**stream**– CUDA stream associated with the stream launch.**userdata**– Device memory buffer.

- Return values:
**SANITIZER_SUCCESS**– on success.


[#](https://docs.nvidia.com#_CPPv427sanitizerSetDeviceGraphData11CUgraphExec22Sanitizer_StreamHandlePKv)

-
[SanitizerResult](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___r_e_s_u_l_t___a_p_i.html#_CPPv415SanitizerResult)sanitizerSetLaunchCallbackData( ,[Sanitizer_LaunchHandle](https://docs.nvidia.com#_CPPv422Sanitizer_LaunchHandle)launch*CUfunction kernel*,,[Sanitizer_StreamHandle](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___s_t_r_e_a_m___a_p_i.html#_CPPv422Sanitizer_StreamHandle)stream*const void *userdata*,Specifies the user data pointer for callbacks.

Mark

`launch`

to use`userdata`

pointer as the device memory buffer to pass in to callback functions. This function is only available if the driver version is 455 or newer.- Parameters:
**launch**– Kernel launch to link to user data. Callbacks in this kernel launch will use`userdata`

as callback data.**kernel**– CUDA function associated with the kernel launch.**stream**– CUDA stream associated with the stream launch.**userdata**– Device memory buffer. This data will be passed to callback functions via the`userdata`

parameter.

- Return values:
**SANITIZER_SUCCESS**– on success.


[#](https://docs.nvidia.com#_CPPv430sanitizerSetLaunchCallbackData22Sanitizer_LaunchHandle10CUfunction22Sanitizer_StreamHandlePKv)

-
[SanitizerResult](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___r_e_s_u_l_t___a_p_i.html#_CPPv415SanitizerResult)sanitizerUnpatchModule(*CUmodule module*)[#](https://docs.nvidia.com#_CPPv422sanitizerUnpatchModule8CUmodule) Remove existing instrumentation of a module.

Remove any instrumentation of a CUDA module performed by previous calls to sanitizerPatchModule.

Note

**Thread-safety**: an API user must serialize access to sanitizerPatchModule and sanitizerUnpatchModule on the same module. For example, if sanitizerPatchModule(mod) and sanitizerUnpatchModule(mod) are called concurrently, the results are undefined.- Parameters:
**module**– CUDA module on which to remove instrumentation.- Return values:
**SANITIZER_SUCCESS**– on success.