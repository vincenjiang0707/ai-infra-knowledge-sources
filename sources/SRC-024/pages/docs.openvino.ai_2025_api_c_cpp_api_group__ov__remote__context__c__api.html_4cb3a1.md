source: https://docs.openvino.ai/2025/api/c_cpp_api/group__ov__remote__context__c__api.html
lastmod: 

# Group Remote Context[#](https://docs.openvino.ai#group-remote-context)

-
*group*Remote Context Set of functions representing of RemoteContext.

Functions

-
ov_remote_context_create_tensor(const ov_remote_context_t *context, const
[ov_element_type_e](https://docs.openvino.ai/group__ov__base__c__api.html#_CPPv417ov_element_type_e)type, const[ov_shape_t](https://docs.openvino.ai/structov__shape__t.html#_CPPv410ov_shape_t)shape, const size_t object_args_size,[ov_tensor_t](https://docs.openvino.ai/structov__tensor__t.html#_CPPv411ov_tensor_t)**remote_tensor, ...)[#](https://docs.openvino.ai#_CPPv431ov_remote_context_create_tensorPK19ov_remote_context_tK17ov_element_type_eK10ov_shape_tK6size_tPP11ov_tensor_tz) Allocates memory tensor in device memory or wraps user-supplied memory handle using the specified tensor description and low-level device-specific parameters. Returns a pointer to the object that implements the RemoteTensor interface.

- Parameters:
**context**– A pointer to the ov_remote_context_t instance.**type**– Defines the element type of the tensor.**shape**– Defines the shape of the tensor.**object_args_size**– Size of the low-level tensor object parameters.**remote_tensor**– Pointer to returned[ov_tensor_t](https://docs.openvino.ai/group__ov__tensor__c__api.html#structov__tensor__t)that contains remote tensor instance.**...**– variadic params Contains low-level tensor object parameters.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_remote_context_get_params(const ov_remote_context_t *context, size_t *size, char **params)
[#](https://docs.openvino.ai#_CPPv428ov_remote_context_get_paramsPK19ov_remote_context_tP6size_tPPc) Returns a string contains device-specific parameters required for low-level operations with the underlying object. Parameters include device/context handles, access flags, etc. Content of the returned map depends on a remote execution context that is currently set on the device (working scenario). One actaul example: “CONTEXT_TYPE OCL OCL_CONTEXT 0x5583b2ec7b40 OCL_QUEUE 0x5583b2e98ff0”.

- Parameters:
**context**– A pointer to the ov_remote_context_t instance.**size**– The size of param pairs.**params**– Param name:value list.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_remote_context_create_host_tensor(const ov_remote_context_t *context, const
[ov_element_type_e](https://docs.openvino.ai/group__ov__base__c__api.html#_CPPv417ov_element_type_e)type, const[ov_shape_t](https://docs.openvino.ai/structov__shape__t.html#_CPPv410ov_shape_t)shape,[ov_tensor_t](https://docs.openvino.ai/structov__tensor__t.html#_CPPv411ov_tensor_t)**tensor)[#](https://docs.openvino.ai#_CPPv436ov_remote_context_create_host_tensorPK19ov_remote_context_tK17ov_element_type_eK10ov_shape_tPP11ov_tensor_t) This method is used to create a host tensor object friendly for the device in current context. For example, GPU context may allocate USM host memory (if corresponding extension is available), which could be more efficient than regular host memory.

- Parameters:
**context**– A pointer to the ov_remote_context_t instance.**type**– Defines the element type of the tensor.**shape**– Defines the shape of the tensor.**tensor**– Pointer to[ov_tensor_t](https://docs.openvino.ai/group__ov__tensor__c__api.html#structov__tensor__t)that contains host tensor.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_remote_context_free(ov_remote_context_t *context)
[#](https://docs.openvino.ai#_CPPv422ov_remote_context_freeP19ov_remote_context_t) Release the memory allocated by ov_remote_context_t.

- Parameters:
**context**– A pointer to the ov_remote_context_t to free memory.- Returns:
Status code of the operation: OK(0) for success.



-
ov_remote_tensor_get_params(
[ov_tensor_t](https://docs.openvino.ai/structov__tensor__t.html#_CPPv411ov_tensor_t)*tensor, size_t *size, char **params)[#](https://docs.openvino.ai#_CPPv427ov_remote_tensor_get_paramsP11ov_tensor_tP6size_tPPc) Returns a string contains device-specific parameters required for low-level operations with underlying object. Parameters include device/context/surface/buffer handles, access flags, etc. Content of the returned map depends on remote execution context that is currently set on the device (working scenario). One example: “MEM_HANDLE:0x559ff6904b00;OCL_CONTEXT:0x559ff71d62f0;SHARED_MEM_TYPE:OCL_BUFFER;”.

- Parameters:
**tensor**– Pointer to[ov_tensor_t](https://docs.openvino.ai/group__ov__tensor__c__api.html#structov__tensor__t)that contains host tensor.**size**– The size of param pairs.**params**– Param name:value list.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_remote_context_create_tensor(const ov_remote_context_t *context, const