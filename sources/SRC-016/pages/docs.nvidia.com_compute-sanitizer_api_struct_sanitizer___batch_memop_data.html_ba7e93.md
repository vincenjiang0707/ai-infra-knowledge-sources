source: https://docs.nvidia.com/compute-sanitizer/api/struct_sanitizer___batch_memop_data.html

# Sanitizer_BatchMemopData[#](https://docs.nvidia.com#sanitizer-batchmemopdata)

-
struct Sanitizer_BatchMemopData
[#](https://docs.nvidia.com#_CPPv424Sanitizer_BatchMemopData) Data passed into a batch memop callback function.

Data passed into a batch memop callback function as the

`cbdata`

argument to[Sanitizer_CallbackFunc](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i.html#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1gac1ae37612d036530e060f1bca8c3ccd8). The`cbdata`

will be this type for`domain`

equal to SANITIZER_CB_DOMAIN_BATCH_MEMOP. The callback data is only valid within the invocation of the callback function that is passed the data. If you need to retain some data for use outside of the callback, you must make a copy of it.Public Members

-
uint64_t address
[#](https://docs.nvidia.com#_CPPv4N24Sanitizer_BatchMemopData7addressE) The address of the operation.


-
[Sanitizer_BatchMemopAtomicOp](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i.html#_CPPv428Sanitizer_BatchMemopAtomicOp)atomicOperation[#](https://docs.nvidia.com#_CPPv4N24Sanitizer_BatchMemopData15atomicOperationE) The operation used for the atomic reduction.

Only valid for SANITIZER_CBID_BATCH_MEMOP_ATOMIC_REDUCTION.


-
CUcontext context
[#](https://docs.nvidia.com#_CPPv4N24Sanitizer_BatchMemopData7contextE) The context where the allocation is located.


-
[Sanitizer_StreamHandle](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___s_t_r_e_a_m___a_p_i.html#_CPPv422Sanitizer_StreamHandle)hStream[#](https://docs.nvidia.com#_CPPv4N24Sanitizer_BatchMemopData7hStreamE) Unique handle for the stream.


-
CUstream stream
[#](https://docs.nvidia.com#_CPPv4N24Sanitizer_BatchMemopData6streamE) The stream where the batch memop is executed.


-
[Sanitizer_BatchMemopType](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i.html#_CPPv424Sanitizer_BatchMemopType)type[#](https://docs.nvidia.com#_CPPv4N24Sanitizer_BatchMemopData4typeE) Size of the value used in the operation.


-
uint64_t value
[#](https://docs.nvidia.com#_CPPv4N24Sanitizer_BatchMemopData5valueE) The value used in the operation.


-
uint64_t address