source: https://docs.nvidia.com/compute-sanitizer/api/struct_sanitizer___resource_module_data.html

# Sanitizer_ResourceModuleData[#](https://docs.nvidia.com#sanitizer-resourcemoduledata)

-
struct Sanitizer_ResourceModuleData
[#](https://docs.nvidia.com#_CPPv428Sanitizer_ResourceModuleData) Data passed into a module resource callback function.

Data passed into a module resource callback function as the

`cbdata`

argument to[Sanitizer_CallbackFunc](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i.html#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1gac1ae37612d036530e060f1bca8c3ccd8). The`cbdata`

will be this type for`domain`

equal to SANITIZER_CB_DOMAIN_RESOURCE and`cbid`

equal to SANITIZER_CBID_RESOURCE_MODULE_LOADED or SANITIZER_CBID_RESOURCE_MODULE_UNLOAD_STARTING. The callback data is only valid within the invocation of the callback function that is passed the data. If you need to retain some data for use outside of the callback, you must make a copy of it.