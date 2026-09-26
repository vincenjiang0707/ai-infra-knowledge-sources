source: https://docs.nvidia.com/compute-sanitizer/api/struct_sanitizer___resource_context_data.html

# Sanitizer_ResourceContextData[#](https://docs.nvidia.com#sanitizer-resourcecontextdata)

-
struct Sanitizer_ResourceContextData
[#](https://docs.nvidia.com#_CPPv429Sanitizer_ResourceContextData) Data passed into a context resource callback function.

Data passed into a context resource callback function as the

`cbdata`

argument to[Sanitizer_CallbackFunc](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i.html#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1gac1ae37612d036530e060f1bca8c3ccd8). The`cbdata`

will be this type for`domain`

equal to SANITIZER_CB_DOMAIN_RESOURCE and`cbid`

equal to SANITIZER_CBID_RESOURCE_CONTEXT_CREATION_STARTING, SANITIZER_CBID_RESOURCE_CONTEXT_CREATION_FINISHED, SANITIZER_CBID_RESOURCE_CONTEXT_DESTROY_STARTING or SANITIZER_CBID_RESOURCE_CONTEXT_DESTROY_FINISHED. The callback data is only valid within the invocation of the callback function that is passed the data. If you need to retain some data for use outside of the callback, you must make a copy of it.Public Members

-
CUcontext context
[#](https://docs.nvidia.com#_CPPv4N29Sanitizer_ResourceContextData7contextE) The context being created or destroyed.


-
CUdevice device
[#](https://docs.nvidia.com#_CPPv4N29Sanitizer_ResourceContextData6deviceE) The device on which the context is being created or destroyed.

This field is only valid for SANITIZER_CBID_RESOURCE_CONTEXT_CREATION_* callbacks.


-
CUgreenCtx greenContext
[#](https://docs.nvidia.com#_CPPv4N29Sanitizer_ResourceContextData12greenContextE) The green context being created or destroyed.


-
CUcontext context