source: https://docs.openvino.ai/2025/api/c_cpp_api/group__ov__tensor__c__api.html
lastmod: 

# Group Tensor[#](https://docs.openvino.ai#group-tensor)

-
*group*Tensor The definitions & operations about tensor.

Functions

-
ov_tensor_create_from_host_ptr(const
[ov_element_type_e](https://docs.openvino.ai/group__ov__base__c__api.html#_CPPv417ov_element_type_e)type, const[ov_shape_t](https://docs.openvino.ai/structov__shape__t.html#_CPPv410ov_shape_t)shape, void *host_ptr,[ov_tensor_t](https://docs.openvino.ai/structov__tensor__t.html#_CPPv411ov_tensor_t)**tensor)[#](https://docs.openvino.ai#_CPPv430ov_tensor_create_from_host_ptrK17ov_element_type_eK10ov_shape_tPvPP11ov_tensor_t) Constructs Tensor using element type, shape and external host ptr.

- Parameters:
**type**– Tensor element type**shape**– Tensor shape**host_ptr**– Pointer to pre-allocated host memory**tensor**– A point to[ov_tensor_t](https://docs.openvino.ai#structov__tensor__t)

- Returns:
Status code of the operation: OK(0) for success.



-
ov_tensor_create(const
[ov_element_type_e](https://docs.openvino.ai/group__ov__base__c__api.html#_CPPv417ov_element_type_e)type, const[ov_shape_t](https://docs.openvino.ai/structov__shape__t.html#_CPPv410ov_shape_t)shape,[ov_tensor_t](https://docs.openvino.ai/structov__tensor__t.html#_CPPv411ov_tensor_t)**tensor)[#](https://docs.openvino.ai#_CPPv416ov_tensor_createK17ov_element_type_eK10ov_shape_tPP11ov_tensor_t) Constructs Tensor using element type and shape. Allocate internal host storage using default allocator.

- Parameters:
**type**– Tensor element type**shape**– Tensor shape**tensor**– A point to[ov_tensor_t](https://docs.openvino.ai#structov__tensor__t)

- Returns:
Status code of the operation: OK(0) for success.



-
ov_tensor_set_shape(
[ov_tensor_t](https://docs.openvino.ai/structov__tensor__t.html#_CPPv411ov_tensor_t)*tensor, const[ov_shape_t](https://docs.openvino.ai/structov__shape__t.html#_CPPv410ov_shape_t)shape)[#](https://docs.openvino.ai#_CPPv419ov_tensor_set_shapeP11ov_tensor_tK10ov_shape_t) Set new shape for tensor, deallocate/allocate if new total size is bigger than previous one.

- Parameters:
**shape**– Tensor shape**tensor**– A point to[ov_tensor_t](https://docs.openvino.ai#structov__tensor__t)

- Returns:
Status code of the operation: OK(0) for success.



-
ov_tensor_create_from_string_array(const char **string_array, const size_t array_size, const
[ov_shape_t](https://docs.openvino.ai/structov__shape__t.html#_CPPv410ov_shape_t)shape,[ov_tensor_t](https://docs.openvino.ai/structov__tensor__t.html#_CPPv411ov_tensor_t)**tensor)[#](https://docs.openvino.ai#_CPPv434ov_tensor_create_from_string_arrayPPKcK6size_tK10ov_shape_tPP11ov_tensor_t) Constructs a new tensor using a string array.

- Parameters:
**string_array**– An array of strings**array_size**– The size of the string array**shape**– Tensor shape**tensor**– A point to[ov_tensor_t](https://docs.openvino.ai#structov__tensor__t)

- Returns:
Status code of the operation: OK(0) for success.



-
ov_tensor_get_shape(const
[ov_tensor_t](https://docs.openvino.ai/structov__tensor__t.html#_CPPv411ov_tensor_t)*tensor,[ov_shape_t](https://docs.openvino.ai/structov__shape__t.html#_CPPv410ov_shape_t)*shape)[#](https://docs.openvino.ai#_CPPv419ov_tensor_get_shapePK11ov_tensor_tP10ov_shape_t) Get shape for tensor.

- Parameters:
**shape**– Tensor shape**tensor**– A point to[ov_tensor_t](https://docs.openvino.ai#structov__tensor__t)

- Returns:
Status code of the operation: OK(0) for success.



-
ov_tensor_get_element_type(const
[ov_tensor_t](https://docs.openvino.ai/structov__tensor__t.html#_CPPv411ov_tensor_t)*tensor,[ov_element_type_e](https://docs.openvino.ai/group__ov__base__c__api.html#_CPPv417ov_element_type_e)*type)[#](https://docs.openvino.ai#_CPPv426ov_tensor_get_element_typePK11ov_tensor_tP17ov_element_type_e) Get type for tensor.

- Parameters:
**type**– Tensor element type**tensor**– A point to[ov_tensor_t](https://docs.openvino.ai#structov__tensor__t)

- Returns:
Status code of the operation: OK(0) for success.



-
ov_tensor_set_string_data(
[ov_tensor_t](https://docs.openvino.ai/structov__tensor__t.html#_CPPv411ov_tensor_t)*tensor, const char **string_array, const size_t array_size)[#](https://docs.openvino.ai#_CPPv425ov_tensor_set_string_dataP11ov_tensor_tPPKcK6size_t) Set string data for tensor.

- Parameters:
**string_array**– Array of strings**array_size**– Size of the array**tensor**– A point to[ov_tensor_t](https://docs.openvino.ai#structov__tensor__t)



-
ov_tensor_get_size(const
[ov_tensor_t](https://docs.openvino.ai/structov__tensor__t.html#_CPPv411ov_tensor_t)*tensor, size_t *elements_size)[#](https://docs.openvino.ai#_CPPv418ov_tensor_get_sizePK11ov_tensor_tP6size_t) the total number of elements (a product of all the dims or 1 for scalar).

- Parameters:
**elements_size**– number of elements**tensor**– A point to[ov_tensor_t](https://docs.openvino.ai#structov__tensor__t)

- Returns:
Status code of the operation: OK(0) for success.



-
ov_tensor_get_byte_size(const
[ov_tensor_t](https://docs.openvino.ai/structov__tensor__t.html#_CPPv411ov_tensor_t)*tensor, size_t *byte_size)[#](https://docs.openvino.ai#_CPPv423ov_tensor_get_byte_sizePK11ov_tensor_tP6size_t) the size of the current Tensor in bytes.

- Parameters:
**byte_size**– the size of the current Tensor in bytes.**tensor**– A point to[ov_tensor_t](https://docs.openvino.ai#structov__tensor__t)

- Returns:
Status code of the operation: OK(0) for success.



-
ov_tensor_data(const
[ov_tensor_t](https://docs.openvino.ai/structov__tensor__t.html#_CPPv411ov_tensor_t)*tensor, void **data)[#](https://docs.openvino.ai#_CPPv414ov_tensor_dataPK11ov_tensor_tPPv) Provides an access to the underlaying host memory.

- Parameters:
**data**– A point to host memory.**tensor**– A point to[ov_tensor_t](https://docs.openvino.ai#structov__tensor__t)

- Returns:
Status code of the operation: OK(0) for success.



-
ov_tensor_free(
[ov_tensor_t](https://docs.openvino.ai/structov__tensor__t.html#_CPPv411ov_tensor_t)*tensor)[#](https://docs.openvino.ai#_CPPv414ov_tensor_freeP11ov_tensor_t) Free

[ov_tensor_t](https://docs.openvino.ai#structov__tensor__t).- Parameters:
**tensor**– A point to[ov_tensor_t](https://docs.openvino.ai#structov__tensor__t)


-
struct ov_tensor_t
[#](https://docs.openvino.ai#_CPPv411ov_tensor_t) *#include <ov_tensor.h>*type define

[ov_tensor_t](https://docs.openvino.ai#structov__tensor__t)from ov_tensor

-
ov_tensor_create_from_host_ptr(const