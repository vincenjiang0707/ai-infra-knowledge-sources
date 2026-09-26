source: https://docs.nvidia.com/compute-sanitizer/api/struct_sanitizer___memcpy_data.html

# Sanitizer_MemcpyData[#](https://docs.nvidia.com#sanitizer-memcpydata)

-
struct Sanitizer_MemcpyData
[#](https://docs.nvidia.com#_CPPv420Sanitizer_MemcpyData) Data passed into a memcpy callback function.

Data passed into a launch callback function as the

`cbdata`

argument to[Sanitizer_CallbackFunc](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i.html#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1gac1ae37612d036530e060f1bca8c3ccd8). The`cbdata`

will be this type for`domain`

equal to SANITIZER_CB_DOMAIN_MEMCPY. The callback data is only valid within the invocation of the callback function that is passed the data. If you need to retain some data for use outside of the callback, you must make a copy of it.Public Members

-
CUcontext apiContext
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_MemcpyData10apiContextE) The context on which the operation was requested.


-
CUstream apiStream
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_MemcpyData9apiStreamE) The stream on which the operation was requested.


-
uint64_t depth
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_MemcpyData5depthE)

-
[Sanitizer_MemcpyDirection](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i.html#_CPPv425Sanitizer_MemcpyDirection)direction[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_MemcpyData9directionE) The direction of the transfer.


-
uint64_t dstAddress
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_MemcpyData10dstAddressE) The destination allocation address.


-
CUcontext dstContext
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_MemcpyData10dstContextE) The context where the destination allocation is located.


-
uint64_t dstPitch
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_MemcpyData8dstPitchE) The destination allocation pitch.


-
CUstream dstStream
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_MemcpyData9dstStreamE) The stream where the memcpy is executed on the destination context.


-
[Sanitizer_StreamHandle](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___s_t_r_e_a_m___a_p_i.html#_CPPv422Sanitizer_StreamHandle)hApiStream[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_MemcpyData10hApiStreamE) Unique handle for the API stream.


-
[Sanitizer_StreamHandle](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___s_t_r_e_a_m___a_p_i.html#_CPPv422Sanitizer_StreamHandle)hDstStream[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_MemcpyData10hDstStreamE) Unique handle for the destination context stream.


-
uint64_t height
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_MemcpyData6heightE)

-
[Sanitizer_StreamHandle](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___s_t_r_e_a_m___a_p_i.html#_CPPv422Sanitizer_StreamHandle)hSrcStream[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_MemcpyData10hSrcStreamE) Unique handle for the source context stream.


-
uint32_t isAsync
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_MemcpyData7isAsyncE) Boolean value indicating if the transfer is asynchronous.


-
uint64_t size
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_MemcpyData4sizeE) Size of the transfer in bytes.


-
uint64_t srcAddress
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_MemcpyData10srcAddressE) The source allocation address.


-
CUcontext srcContext
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_MemcpyData10srcContextE) The context where the source allocation is located.


-
uint64_t srcPitch
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_MemcpyData8srcPitchE) The source allocation pitch.


-
CUstream srcStream
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_MemcpyData9srcStreamE) The stream where the memcpy is executed on the source context.


-
uint64_t width
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_MemcpyData5widthE) Memcpy size configuration.


-
CUcontext apiContext