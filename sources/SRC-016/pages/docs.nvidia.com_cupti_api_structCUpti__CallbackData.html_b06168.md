source: https://docs.nvidia.com/cupti/api/structCUpti__CallbackData.html

# 7.136. CUpti_CallbackData[#](https://docs.nvidia.com#cupti-callbackdata)

-
struct CUpti_CallbackData
[#](https://docs.nvidia.com#_CPPv418CUpti_CallbackData) Data passed into a runtime or driver API callback function.

Data passed into a runtime or driver API callback function as the

`cbdata`

argument to[CUpti_CallbackFunc](https://docs.nvidia.com/group__CUPTI__CALLBACK__API.html#group__cupti__callback__api_1ga21bab4f7f7e04488b0e7edcea9f5a49c). The`cbdata`

will be this type for`domain`

equal to CUPTI_CB_DOMAIN_DRIVER_API or CUPTI_CB_DOMAIN_RUNTIME_API. The callback data is valid only within the invocation of the callback function that is passed the data. If you need to retain some data for use outside of the callback, you must make a copy of that data. For example, if you make a shallow copy of[CUpti_CallbackData](https://docs.nvidia.com#structcupti__callbackdata)within a callback, you cannot dereference`functionParams`

outside of that callback to access the function parameters.`functionName`

is an exception: the string pointed to by`functionName`

is a global constant and so may be accessed outside of the callback.Public Members

-
[CUpti_ApiCallbackSite](https://docs.nvidia.com/group__CUPTI__CALLBACK__API.html#_CPPv421CUpti_ApiCallbackSite)callbackSite[#](https://docs.nvidia.com#_CPPv4N18CUpti_CallbackData12callbackSiteE) Point in the runtime or driver function from where the callback was issued.


-
const char *functionName
[#](https://docs.nvidia.com#_CPPv4N18CUpti_CallbackData12functionNameE) Name of the runtime or driver API function which issued the callback.

This string is a global constant and so may be accessed outside of the callback.


-
const void *functionParams
[#](https://docs.nvidia.com#_CPPv4N18CUpti_CallbackData14functionParamsE) Pointer to the arguments passed to the runtime or driver API call.

See generated_cuda_runtime_api_meta.h and generated_cuda_meta.h for structure definitions for the parameters for each runtime and driver API function.


-
void *functionReturnValue
[#](https://docs.nvidia.com#_CPPv4N18CUpti_CallbackData19functionReturnValueE) Pointer to the return value of the runtime or driver API call.

This field is only valid within the exit::CUPTI_API_EXIT callback. For a runtime API

`functionReturnValue`

points to a`cudaError_t`

. For a driver API`functionReturnValue`

points to a`CUresult`

.

-
const char *symbolName
[#](https://docs.nvidia.com#_CPPv4N18CUpti_CallbackData10symbolNameE) Name of the symbol operated on by the runtime or driver API function which issued the callback.

This entry is valid only for driver and runtime launch callbacks, where it returns the name of the kernel.


-
CUcontext context
[#](https://docs.nvidia.com#_CPPv4N18CUpti_CallbackData7contextE) Driver context current to the thread, or null if no context is current.

This value can change from the entry to exit callback of a runtime API function if the runtime initializes a context.


-
uint32_t contextUid
[#](https://docs.nvidia.com#_CPPv4N18CUpti_CallbackData10contextUidE) Unique ID for the CUDA context associated with the thread.

The UIDs are assigned sequentially as contexts are created and are unique within a process.


-
uint64_t *correlationData
[#](https://docs.nvidia.com#_CPPv4N18CUpti_CallbackData15correlationDataE) Pointer to data shared between the entry and exit callbacks of a given runtime or drive API function invocation.

This field can be used to pass 64-bit values from the entry callback to the corresponding exit callback.


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N18CUpti_CallbackData13correlationIdE) The activity record correlation ID for this callback.

For a driver domain callback (i.e.

`domain`

CUPTI_CB_DOMAIN_DRIVER_API) this ID will equal the correlation ID in the[CUpti_ActivityAPI](https://docs.nvidia.com/structCUpti__ActivityAPI.html#structcupti__activityapi)record corresponding to the CUDA driver function call. For a runtime domain callback (i.e.`domain`

CUPTI_CB_DOMAIN_RUNTIME_API) this ID will equal the correlation ID in the[CUpti_ActivityAPI](https://docs.nvidia.com/structCUpti__ActivityAPI.html#structcupti__activityapi)record corresponding to the CUDA runtime function call. Within the callback, this ID can be recorded to correlate user data with the activity record. This field is new in 4.1.

-