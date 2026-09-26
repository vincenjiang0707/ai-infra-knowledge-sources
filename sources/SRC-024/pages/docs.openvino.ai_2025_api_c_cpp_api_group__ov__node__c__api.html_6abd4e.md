source: https://docs.openvino.ai/2025/api/c_cpp_api/group__ov__node__c__api.html
lastmod: 

# Group Node[#](https://docs.openvino.ai#group-node)

-
*group*Node The definitions & operations about node.

Functions

-
ov_const_port_get_shape(const
[ov_output_const_port_t](https://docs.openvino.ai/structov__output__const__port__t.html#_CPPv422ov_output_const_port_t)*port,[ov_shape_t](https://docs.openvino.ai/structov__shape__t.html#_CPPv410ov_shape_t)*tensor_shape)[#](https://docs.openvino.ai#_CPPv423ov_const_port_get_shapePK22ov_output_const_port_tP10ov_shape_t) Get the shape of port object.

- Parameters:
**port**– A pointer to[ov_output_const_port_t](https://docs.openvino.ai#structov__output__const__port__t).**tensor_shape**– tensor shape.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_port_get_shape(const
[ov_output_port_t](https://docs.openvino.ai/structov__output__port__t.html#_CPPv416ov_output_port_t)*port,[ov_shape_t](https://docs.openvino.ai/structov__shape__t.html#_CPPv410ov_shape_t)*tensor_shape)[#](https://docs.openvino.ai#_CPPv417ov_port_get_shapePK16ov_output_port_tP10ov_shape_t) Get the shape of port object.

- Parameters:
**port**– A pointer to[ov_output_port_t](https://docs.openvino.ai#structov__output__port__t).**tensor_shape**– tensor shape.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_port_get_any_name(const
[ov_output_const_port_t](https://docs.openvino.ai/structov__output__const__port__t.html#_CPPv422ov_output_const_port_t)*port, char **tensor_name)[#](https://docs.openvino.ai#_CPPv420ov_port_get_any_namePK22ov_output_const_port_tPPc) Get the tensor name of port.

- Parameters:
**port**– A pointer to the[ov_output_const_port_t](https://docs.openvino.ai#structov__output__const__port__t).**tensor_name**– A pointer to the tensor name.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_port_get_partial_shape(const
[ov_output_const_port_t](https://docs.openvino.ai/structov__output__const__port__t.html#_CPPv422ov_output_const_port_t)*port, ov_partial_shape_t *partial_shape)[#](https://docs.openvino.ai#_CPPv425ov_port_get_partial_shapePK22ov_output_const_port_tP18ov_partial_shape_t) Get the partial shape of port.

- Parameters:
**port**– A pointer to the[ov_output_const_port_t](https://docs.openvino.ai#structov__output__const__port__t).**partial_shape**– Partial shape.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_port_get_element_type(const
[ov_output_const_port_t](https://docs.openvino.ai/structov__output__const__port__t.html#_CPPv422ov_output_const_port_t)*port,[ov_element_type_e](https://docs.openvino.ai/group__ov__base__c__api.html#_CPPv417ov_element_type_e)*tensor_type)[#](https://docs.openvino.ai#_CPPv424ov_port_get_element_typePK22ov_output_const_port_tP17ov_element_type_e) Get the tensor type of port.

- Parameters:
**port**– A pointer to the[ov_output_const_port_t](https://docs.openvino.ai#structov__output__const__port__t).**tensor_type**– tensor type.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_output_port_free(
[ov_output_port_t](https://docs.openvino.ai/structov__output__port__t.html#_CPPv416ov_output_port_t)*port)[#](https://docs.openvino.ai#_CPPv419ov_output_port_freeP16ov_output_port_t) free port object

- Parameters:
**port**– The pointer to the instance of the[ov_output_port_t](https://docs.openvino.ai#structov__output__port__t)to free.


-
ov_output_const_port_free(
[ov_output_const_port_t](https://docs.openvino.ai/structov__output__const__port__t.html#_CPPv422ov_output_const_port_t)*port)[#](https://docs.openvino.ai#_CPPv425ov_output_const_port_freeP22ov_output_const_port_t) free const port

- Parameters:
**port**– The pointer to the instance of the[ov_output_const_port_t](https://docs.openvino.ai#structov__output__const__port__t)to free.


-
struct ov_output_const_port_t
[#](https://docs.openvino.ai#_CPPv422ov_output_const_port_t) *#include <ov_node.h>*type define

[ov_output_const_port_t](https://docs.openvino.ai#structov__output__const__port__t)from ov_output_const_port

-
struct ov_output_port_t
[#](https://docs.openvino.ai#_CPPv416ov_output_port_t) *#include <ov_node.h>*type define

[ov_output_port_t](https://docs.openvino.ai#structov__output__port__t)from ov_output_port

-
ov_const_port_get_shape(const