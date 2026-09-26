source: https://docs.nvidia.com/compute-sanitizer/api/struct_sanitizer___external_memory_data.html

# Sanitizer_ExternalMemoryData[#](https://docs.nvidia.com#sanitizer-externalmemorydata)

-
struct Sanitizer_ExternalMemoryData
[#](https://docs.nvidia.com#_CPPv428Sanitizer_ExternalMemoryData) Data passed into an external memory callback function.

Data passed into an event callback function as the

`cbdata`

argument to[Sanitizer_CallbackFunc](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i.html#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1gac1ae37612d036530e060f1bca8c3ccd8). The`cbdata`

will be this type for`domain`

equal tp SANITIZER_CB_DOMAIN_EXTERNAL_MEMORY. The callback data is only valid within the invocation of the callback function that is passed the data. If you need to retain some data for use outside of the callback, you must make a copy of it.Public Members

-
uint64_t address
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_ExternalMemoryData7addressE) Address of the mapped memory.

This field is only valid for SANITIZER_CBID_EXTERNAL_MEMORY_MAPPED.


-
CUcontext context
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_ExternalMemoryData7contextE) Context containing the external memory.


-
CUdevice device
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_ExternalMemoryData6deviceE) Device containing the external memory.


-
CUexternalMemory extMemory
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_ExternalMemoryData9extMemoryE) External memory object.


-
uint64_t size
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_ExternalMemoryData4sizeE) Size of the memory imported or mapped.

This field is only valid for SANITIZER_CBID_EXTERNAL_MEMORY_IMPORT and SANITIZER_CBID_EXTERNAL_MEMORY_MAPPED.


-
uint64_t address