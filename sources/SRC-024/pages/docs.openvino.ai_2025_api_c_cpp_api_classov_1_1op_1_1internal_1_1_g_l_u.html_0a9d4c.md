source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1internal_1_1_g_l_u.html
lastmod: 

# Class ov::op::internal::GLU[#](https://docs.openvino.ai#class-ov-op-internal-glu)

-
class GLU : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op8internal3GLUE) Operator performing Gated Linear Unit Activation This operation performs gated linear unit activation that combines swish or gelu activation function.

Public Functions

-
GLU(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, int64_t axis, int64_t split_lengths, const GluType glu_type, const size_t split_to_glu_idx, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)output_type =[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::dynamic)[#](https://docs.openvino.ai#_CPPv4N2ov2op8internal3GLU3GLUERK6OutputI4NodeE7int64_t7int64_tK7GluTypeK6size_tKN2ov7element4TypeE) Constructs an

[GLU](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1internal_1_1_g_l_u)operation.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor with data**axis**– The index of an axis in “data” along which to perform the split**split_lenghts**– A list containing the sizes of each output tensor along the split “axis”**glu_type**–[GLU](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1internal_1_1_g_l_u)type, one of Swish, Gelu and Gelu_Tanh**split_to_glu_idx**–[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)index of variadic split, which is connected to[GLU](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1internal_1_1_g_l_u)**output_type**–[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)element type



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op8internal3GLU24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
GLU(const