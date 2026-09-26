source: https://docs.nvidia.com/compute-sanitizer/api/struct_sanitizer___error_logging_data.html

# Sanitizer_ErrorLoggingData[#](https://docs.nvidia.com#sanitizer-errorloggingdata)

-
struct Sanitizer_ErrorLoggingData
[#](https://docs.nvidia.com#_CPPv426Sanitizer_ErrorLoggingData) Data passed into an error logging callback function.

Data passed into an error logging callback function as the

`cbdata`

argument to[Sanitizer_CallbackFunc](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i.html#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1gac1ae37612d036530e060f1bca8c3ccd8). The`cbdata`

will be this type for`domain`

equal tp SANITIZER_CBID_ERROR_LOGGING. The callback data is only valid within the invocation of the callback function that is passed the data. If you need to retain some data for use outside of the callback, you must make a copy of it.