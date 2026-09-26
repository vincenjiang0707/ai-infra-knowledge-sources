source: https://docs.nvidia.com/compute-sanitizer/api/struct_sanitizer___callback_data.html

# Sanitizer_CallbackData[#](https://docs.nvidia.com#sanitizer-callbackdata)

-
struct Sanitizer_CallbackData
[#](https://docs.nvidia.com#_CPPv422Sanitizer_CallbackData) Data passed into a runtime or driver API callback function.

Data passed into a runtime or driver API callback function as the

`cbdata`

argument to[Sanitizer_CallbackFunc](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i.html#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1gac1ae37612d036530e060f1bca8c3ccd8). The`cbdata`

will be this type for`domain`

equal to SANITIZER_CB_DOMAIN_DRIVER_API or SANITIZER_CB_DOMAIN_RUNTIME_API. The callback data is valid only within the invocation of the callback function that is passed the data. If you need to retain some data for use outside of the callback, you must make of a copy of that data. For example, if you make a shallow copy of[Sanitizer_CallbackData](https://docs.nvidia.com#struct_sanitizer___callback_data)within a callback, you cannot dereference`functionParams`

outside of that callback to access the function parameters.`functionName`

is an exception: the string pointed to by`functionName`

is a global constant and so may be accessed outside of the callback.Public Members

-
[Sanitizer_ApiCallbackSite](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i.html#_CPPv425Sanitizer_ApiCallbackSite)callbackSite[#](https://docs.nvidia.com#_CPPv4N22Sanitizer_CallbackData12callbackSiteE) Point in the runtime or driver function from where the callback was issued.


-
CUcontext context
[#](https://docs.nvidia.com#_CPPv4N22Sanitizer_CallbackData7contextE) Driver context current to the thread, or null if no context is current.

This value can change from the entry to exit callback of a runtime API function if the runtime initialized a context.


-
const char *functionName
[#](https://docs.nvidia.com#_CPPv4N22Sanitizer_CallbackData12functionNameE) Name of the runtime or driver API function which issued the callback.

This string is a global constant and so may be accessed outside of the callback.


-
const void *functionParams
[#](https://docs.nvidia.com#_CPPv4N22Sanitizer_CallbackData14functionParamsE) Pointer to the arguments passed to the runtime or driver API call.

See generated_cuda_runtime_api_meta.h and generated_cuda_meta.h for structure definitions for the parameters for each runtime and driver API function.


-
const void *functionReturnValue
[#](https://docs.nvidia.com#_CPPv4N22Sanitizer_CallbackData19functionReturnValueE) Pointer to the return value of the runtime or driver API call.

This field is only valid within the SANITIZER_API_EXIT callback. For a runtime API

`functionReturnValue`

points to a`cudaError_t`

. For a driver API`functionReturnValue`

points to a`CUresult`

.

-
const char *symbolName
[#](https://docs.nvidia.com#_CPPv4N22Sanitizer_CallbackData10symbolNameE) Name of the symbol operated on by the runtime or driver API function which issued the callback.

This entry is valid only for driver and runtime launch callbacks, where it returns the name of the kernel.


-