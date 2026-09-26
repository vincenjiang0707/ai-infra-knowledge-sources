source: https://docs.nvidia.com/compute-sanitizer/api/struct_sanitizer___resource_memory_data.html

# Sanitizer_ResourceMemoryData[#](https://docs.nvidia.com#sanitizer-resourcememorydata)

-
struct Sanitizer_ResourceMemoryData
[#](https://docs.nvidia.com#_CPPv428Sanitizer_ResourceMemoryData) Data passed into a memory resource callback function.

Data passed into a memory resource callback function as the

`cbdata`

argument to[Sanitizer_CallbackFunc](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i.html#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1gac1ae37612d036530e060f1bca8c3ccd8). The`cbdata`

will be this type for`domain`

equal to SANITIZER_CB_DOMAIN_RESOURCE and`cbid`

equal to SANITIZER_CBID_RESOURCE_DEVICE_MEMORY_ALLOC, SANITIZER_CBID_RESOURCE_DEVICE_MEMORY_FREE, SANITIZER_CBID_RESOURCE_HOST_MEMORY_ALLOC, SANITIZER_CBID_RESOURCE_HOST_MEMORY_FREE, SANITIZER_CBID_RESOURCE_MEMORY_ALLOC_ASYNC, SANITIZER_CBID_RESOURCE_MEMORY_FREE_ASYNC or SANITIZER_CBID_RESOURCE_MEMORY_FREE_ASYNC_DONE or SANITIZER_CBID_RESOURCE_MEMPOOL_IMPORT_POINTER. The callback data is only valid within the invocation of the callback function that is passed the data. If you need to retain some data for use outside of the callback, you must make a copy of it.Public Members

-
uint64_t address
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_ResourceMemoryData7addressE) Address of the allocation being created or destroyed.


-
CUcontext context
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_ResourceMemoryData7contextE) Context containing the allocation being created or destroyed.

Can be NULL if the allocation is not attached to a context.


-
CUdevice device
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_ResourceMemoryData6deviceE) Device where the allocation is being created.

Available for all cbid with a driver version of 455 or newer.


-
uint32_t flags
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_ResourceMemoryData5flagsE) Allocation details: use Sanitizer_ResourceMemoryFlags to interpret this field.


-
[Sanitizer_StreamHandle](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___s_t_r_e_a_m___a_p_i.html#_CPPv422Sanitizer_StreamHandle)hStream[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_ResourceMemoryData7hStreamE) Stream containing the allocation being created or destroyed.

Can be NULL if the allocation is not attached to a stream.


-
CUmemoryPool memoryPool
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_ResourceMemoryData10memoryPoolE) Memory pool containing the allocation being created or destroyed.

Can be NULL if the allocation is not attached to a memory pool.


-
uint32_t permissions
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_ResourceMemoryData11permissionsE) Allocation permissions: use Sanitizer_ResourceMemoryPermissions to interpret this field.


-
uint64_t size
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_ResourceMemoryData4sizeE) Size of the allocation being created or destroyed.


-
CUdevice sourceDevice
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_ResourceMemoryData12sourceDeviceE) Source device of this allocation (different from device if SANITIZER_MEMORY_FLAG_PEER is set).


-
CUstream stream
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_ResourceMemoryData6streamE) Public handle for the stream.


-
[Sanitizer_MemoryVisibility](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i.html#_CPPv426Sanitizer_MemoryVisibility)visibility[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_ResourceMemoryData10visibilityE) Visibility of the allocation.


-
uint64_t address