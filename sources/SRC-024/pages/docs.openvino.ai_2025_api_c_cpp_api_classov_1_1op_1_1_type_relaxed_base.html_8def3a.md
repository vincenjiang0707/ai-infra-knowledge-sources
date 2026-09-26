source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1_type_relaxed_base.html
lastmod: 

# Class ov::op::TypeRelaxedBase[#](https://docs.openvino.ai#class-ov-op-typerelaxedbase)

-
class TypeRelaxedBase
[#](https://docs.openvino.ai#_CPPv4N2ov2op15TypeRelaxedBaseE) A base class for templated

[TypeRelaxed](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1_type_relaxed)that maintains overridden input types and output types for an operation.Subclassed by

[ov::op::TypeRelaxed< BaseOp >](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1_type_relaxed)Public Functions

-
inline const
[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&get_overridden_output_type(size_t outputIndex = 0) const[#](https://docs.openvino.ai#_CPPv4NK2ov2op15TypeRelaxedBase26get_overridden_output_typeE6size_t) This method may look similar to

[Node::get_output_element_type](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node_1acd5df9fde324e8808120b7c21cae14ee), but it is not the same thing, because get_output_element_type returns the result of type inference, so it is completely deduced from an operation inputs and attributes, and get_overridden_output_type returns value of the attribute that is used to deduce output type. In some cases they don’t match: get_overridden_output_type may return[element::dynamic](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__element__cpp__api_1ga65a44781c293f3559c2e037eb29c0f14)for some index i, and get_output_element_type will return some real type for the same index i.- Returns:
Data type that will be set for output with a given index outputIndex. If output with a specified index outputIndex hasn’t been set before,

[element::dynamic](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__element__cpp__api_1ga65a44781c293f3559c2e037eb29c0f14)will returned. Undefined means no type override happens for a given outputIndex and it will deduced as original operation defineds in its infer function.


-
inline void set_overridden_output_type(const
[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&element_type, size_t outputIndex = 0)[#](https://docs.openvino.ai#_CPPv4N2ov2op15TypeRelaxedBase26set_overridden_output_typeERKN7element4TypeE6size_t) Set data type that overrides the original data type for output port with outputIndex index In case if outputIndex is out of range of known outputs (and this class cannot detect the real number of outputs for original operation), the number of overridden outputs is changed according to a given outputIndex value.


-
inline const
[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&get_origin_input_type(size_t inputIndex = 0) const[#](https://docs.openvino.ai#_CPPv4NK2ov2op15TypeRelaxedBase21get_origin_input_typeE6size_t) - Returns:
Data type that will be set for input when original shape/type inference function is called. If index inputIndex hasn’t been set before,

[element::dynamic](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__element__cpp__api_1ga65a44781c293f3559c2e037eb29c0f14)will returned. Undefined means that the type from input tensor descriptor is used for a given index.


-
inline void set_origin_input_type(const
[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&element_type, size_t inputIndex = 0)[#](https://docs.openvino.ai#_CPPv4N2ov2op15TypeRelaxedBase21set_origin_input_typeERKN7element4TypeE6size_t) Set data type that overrides the original data type for input port with inputIndex index. In case if inputIndex is out of range of known inputs (and this class cannot detect the real number of inputs for original operation), the number of overridden inputs is changed according to a given inputIndex value. All new entries except one added at inputIndex position are undefined.


-
inline const