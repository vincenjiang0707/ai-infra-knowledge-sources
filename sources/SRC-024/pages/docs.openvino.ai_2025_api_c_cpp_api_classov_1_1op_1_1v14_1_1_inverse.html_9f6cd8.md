source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v14_1_1_inverse.html
lastmod: 

# Class ov::op::v14::Inverse[#](https://docs.openvino.ai#class-ov-op-v14-inverse)

-
class Inverse : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v147InverseE) [Inverse](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v14_1_1_inverse)operation computes the inverse of the input tensor.Public Functions

-
Inverse(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const bool adjoint = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v147Inverse7InverseERK6OutputI4NodeEKb) [Inverse](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v14_1_1_inverse)operation computes the inverse of the input matrices. The inverse is computed for each MxM matrix separetely, preserving all batch dimensions.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)matrices to compute the inverse for. Last two tensor dimensions must be of the same size.**adjoint**– Boolean that determines whether to return a normal inverse or adjoint (conjugate transpose) of the input matrices.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v147Inverse24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
Inverse(const