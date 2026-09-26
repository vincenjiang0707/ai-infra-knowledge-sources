source: https://docs.nvidia.com/compute-sanitizer/api/struct_sanitizer___uvm_data.html

# Sanitizer_UvmData[#](https://docs.nvidia.com#sanitizer-uvmdata)

-
struct Sanitizer_UvmData
[#](https://docs.nvidia.com#_CPPv417Sanitizer_UvmData) Data passed into a managed memory callback function.

Data passed into a managed memory callback function as the

`cbdata`

argument to[Sanitizer_CallbackFunc](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i.html#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1gac1ae37612d036530e060f1bca8c3ccd8). The`cbdata`

will be this type for`domain`

equal to SANITIZER_CB_DOMAIN_UVM. The callback data is only valid within the invocation of the callback function that is passed the data. If you need to retain some data for use outside of the callback, you must make a copy of it.Public Members

-
uint64_t address
[#](https://docs.nvidia.com#_CPPv4N17Sanitizer_UvmData7addressE) The address of the allocation.


-
CUcontext context
[#](https://docs.nvidia.com#_CPPv4N17Sanitizer_UvmData7contextE) The context where the allocation is located.


-
[Sanitizer_StreamHandle](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___s_t_r_e_a_m___a_p_i.html#_CPPv422Sanitizer_StreamHandle)hStream[#](https://docs.nvidia.com#_CPPv4N17Sanitizer_UvmData7hStreamE) Unique handle for the stream.


-
CUstream stream
[#](https://docs.nvidia.com#_CPPv4N17Sanitizer_UvmData6streamE) The stream on which the memory is attached.

This is only valid if visibility is SANITIZER_MEMORY_VISIBILITY_STREAM.


-
[Sanitizer_MemoryVisibility](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i.html#_CPPv426Sanitizer_MemoryVisibility)visibility[#](https://docs.nvidia.com#_CPPv4N17Sanitizer_UvmData10visibilityE) New visibility for the allocation.


-
uint64_t address