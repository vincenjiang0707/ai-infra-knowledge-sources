source: https://docs.nvidia.com/compute-sanitizer/api/struct_sanitizer___resource_logical_endpoint_data.html

# Sanitizer_ResourceLogicalEndpointData[#](https://docs.nvidia.com#sanitizer-resourcelogicalendpointdata)

-
struct Sanitizer_ResourceLogicalEndpointData
[#](https://docs.nvidia.com#_CPPv437Sanitizer_ResourceLogicalEndpointData) Data passed into a logical endpoint resource callback function.

Data passed into a logical endpoint resource callback function as the

`cbdata`

argument to[Sanitizer_CallbackFunc](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i.html#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1gac1ae37612d036530e060f1bca8c3ccd8). The`cbdata`

will be this type for`domain`

equal to SANITIZER_CB_DOMAIN_RESOURCE and`cbid`

equal to SANITIZER_CBID_RESOURCE_LOGICAL_ENDPOINT_CREATED or SANITIZER_CBID_RESOURCE_LOGICAL_ENDPOINT_DESTROYED. The callback data is only valid within the invocation of the callback function that is passed the data. If you need to retain some data for use outside of the callback, you must make a copy of it.