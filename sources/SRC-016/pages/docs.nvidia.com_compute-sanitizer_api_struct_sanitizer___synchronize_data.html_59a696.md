source: https://docs.nvidia.com/compute-sanitizer/api/struct_sanitizer___synchronize_data.html

# Sanitizer_SynchronizeData[#](https://docs.nvidia.com#sanitizer-synchronizedata)

-
struct Sanitizer_SynchronizeData
[#](https://docs.nvidia.com#_CPPv425Sanitizer_SynchronizeData) Data passed into a synchronization callback function.

Data passed into a synchronization callback function as the

`cbdata`

argument to[Sanitizer_CallbackFunc](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i.html#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1gac1ae37612d036530e060f1bca8c3ccd8). The`cbdata`

will be this type for`domain`

equal to SANITIZER_CB_DOMAIN_SYNCHRONIZE. The callback data is only valid within the invocation of the callback function that is passed the data. If you need to retain some data for use outside of the callback, you must make a copy of it.Public Members

-
CUcontext context
[#](https://docs.nvidia.com#_CPPv4N25Sanitizer_SynchronizeData7contextE) For SANITIZER_CBID_SYNCHRONIZE_CONTEXT_SYNCHRONIZED, this is the context being synchronized.

For SANITIZER_CBID_SYNCHRONIZE_STREAM_SYNCHRONIZED, this is the context of the stream being synchronized.


-
CUgreenCtx greenContext
[#](https://docs.nvidia.com#_CPPv4N25Sanitizer_SynchronizeData12greenContextE) The green context being synchronized.


-
[Sanitizer_StreamHandle](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___s_t_r_e_a_m___a_p_i.html#_CPPv422Sanitizer_StreamHandle)hStream[#](https://docs.nvidia.com#_CPPv4N25Sanitizer_SynchronizeData7hStreamE) Unique handle for the stream.


-
CUstream stream
[#](https://docs.nvidia.com#_CPPv4N25Sanitizer_SynchronizeData6streamE) This field is only valid for SANITIZER_CBID_SYNCHRONIZE_STREAM_SYNCHRONIZED.

This is the stream being synchronized.


-
CUcontext context