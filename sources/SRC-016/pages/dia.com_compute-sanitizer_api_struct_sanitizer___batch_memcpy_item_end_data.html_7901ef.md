source: https://docs.nvidia.com/compute-sanitizer/api/struct_sanitizer___batch_memcpy_item_end_data.html

# Sanitizer_BatchMemcpyItemEndData[#](https://docs.nvidia.com#sanitizer-batchmemcpyitemenddata)

-
struct Sanitizer_BatchMemcpyItemEndData
[#](https://docs.nvidia.com#_CPPv432Sanitizer_BatchMemcpyItemEndData) Data passed into a item batch memcpy end callback function.

Public Members

-
CUcontext apiContext
[#](https://docs.nvidia.com#_CPPv4N32Sanitizer_BatchMemcpyItemEndData10apiContextE) The context on which the operation was requested.


-
CUstream apiStream
[#](https://docs.nvidia.com#_CPPv4N32Sanitizer_BatchMemcpyItemEndData9apiStreamE) The stream on which the operation was requested.


-
[Sanitizer_StreamHandle](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___s_t_r_e_a_m___a_p_i.html#_CPPv422Sanitizer_StreamHandle)hApiStream[#](https://docs.nvidia.com#_CPPv4N32Sanitizer_BatchMemcpyItemEndData10hApiStreamE) Unique handle for the API stream.


-
CUcontext apiContext