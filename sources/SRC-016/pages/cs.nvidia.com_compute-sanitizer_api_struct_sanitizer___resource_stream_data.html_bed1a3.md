source: https://docs.nvidia.com/compute-sanitizer/api/struct_sanitizer___resource_stream_data.html

# Sanitizer_ResourceStreamData[#](https://docs.nvidia.com#sanitizer-resourcestreamdata)

-
struct Sanitizer_ResourceStreamData
[#](https://docs.nvidia.com#_CPPv428Sanitizer_ResourceStreamData) Data passed into a stream resource callback function.

Data passed into a stream resource callback function as the

`cbdata`

argument to[Sanitizer_CallbackFunc](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i.html#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1gac1ae37612d036530e060f1bca8c3ccd8). The`cbdata`

will be this type for`domain`

equal to SANITIZER_CB_DOMAIN_RESOURCE and`cbid`

equal to SANITIZER_CBID_RESOURCE_STREAM_CREATED, SANITIZER_CBID_RESOURCE_STREAM_DESTROY_STARTING or SANITIZER_CBID_RESOURCE_STREAM_DESTROY_FINISHED. The callback data is only valid within the invocation of the callback function that is passed the data. If you need to retain some data for use outside of the callback, you must make a copy of it.Public Members

-
CUcontext context
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_ResourceStreamData7contextE) The context containing the stream being created or destroyed.


-
CUgreenCtx greenContext
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_ResourceStreamData12greenContextE) The green context containing the stream being created or destroyed.


-
[Sanitizer_StreamHandle](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___s_t_r_e_a_m___a_p_i.html#_CPPv422Sanitizer_StreamHandle)hStream[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_ResourceStreamData7hStreamE) Unique handle for the stream.


-
CUstream stream
[#](https://docs.nvidia.com#_CPPv4N28Sanitizer_ResourceStreamData6streamE) The stream being created or destroyed.

This handle will be NULL for the STREAM_DESTROY_FINISHED cbid.


-
CUcontext context