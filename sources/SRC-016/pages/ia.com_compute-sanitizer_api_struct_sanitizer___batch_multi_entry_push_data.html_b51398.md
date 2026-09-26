source: https://docs.nvidia.com/compute-sanitizer/api/struct_sanitizer___batch_multi_entry_push_data.html

# Sanitizer_BatchMultiEntryPushData[#](https://docs.nvidia.com#sanitizer-batchmultientrypushdata)

-
struct Sanitizer_BatchMultiEntryPushData
[#](https://docs.nvidia.com#_CPPv433Sanitizer_BatchMultiEntryPushData) Data passed into a batch memcpy multientry push begin/end function.

Public Members

-
CUcontext apiContext
[#](https://docs.nvidia.com#_CPPv4N33Sanitizer_BatchMultiEntryPushData10apiContextE) The context on which the operation was requested.


-
CUstream apiStream
[#](https://docs.nvidia.com#_CPPv4N33Sanitizer_BatchMultiEntryPushData9apiStreamE) The stream on which the operation was requested.


-
[Sanitizer_StreamHandle](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___s_t_r_e_a_m___a_p_i.html#_CPPv422Sanitizer_StreamHandle)hApiStream[#](https://docs.nvidia.com#_CPPv4N33Sanitizer_BatchMultiEntryPushData10hApiStreamE) Unique handle for the API stream.


-
CUcontext apiContext