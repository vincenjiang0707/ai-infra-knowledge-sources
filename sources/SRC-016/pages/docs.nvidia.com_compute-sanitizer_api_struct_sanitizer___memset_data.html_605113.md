source: https://docs.nvidia.com/compute-sanitizer/api/struct_sanitizer___memset_data.html

# Sanitizer_MemsetData[#](https://docs.nvidia.com#sanitizer-memsetdata)

-
struct Sanitizer_MemsetData
[#](https://docs.nvidia.com#_CPPv420Sanitizer_MemsetData) Data passed into a memset callback function.

Data passed into a launch callback function as the

`cbdata`

argument to[Sanitizer_CallbackFunc](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i.html#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1gac1ae37612d036530e060f1bca8c3ccd8). The`cbdata`

will be this type for`domain`

equal to SANITIZER_CB_DOMAIN_MEMSET. The callback data is only valid within the invocation of the callback function that is passed the data. If you need to retain some data for use outside of the callback, you must make a copy of it.Public Members

-
uint64_t address
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_MemsetData7addressE) The address of the memset start.


-
CUcontext context
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_MemsetData7contextE) The context where the allocation is located.


-
uint32_t elementSize
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_MemsetData11elementSizeE)

-
uint64_t height
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_MemsetData6heightE)

-
[Sanitizer_StreamHandle](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___s_t_r_e_a_m___a_p_i.html#_CPPv422Sanitizer_StreamHandle)hStream[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_MemsetData7hStreamE) Unique handle for the stream.


-
uint32_t isAsync
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_MemsetData7isAsyncE) Boolean value indicating if the transfer is asynchronous.


-
uint64_t pitch
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_MemsetData5pitchE)

-
CUstream stream
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_MemsetData6streamE) The stream where the memset is executed.


-
uint32_t value
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_MemsetData5valueE) Value to be written.


-
uint64_t width
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_MemsetData5widthE) Memset size configuration.


-
uint64_t address