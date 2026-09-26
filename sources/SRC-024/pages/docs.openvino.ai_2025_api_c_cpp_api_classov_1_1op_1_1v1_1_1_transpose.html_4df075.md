source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v1_1_1_transpose.html
lastmod: 

# Class ov::op::v1::Transpose[#](https://docs.openvino.ai#class-ov-op-v1-transpose)

-
class Transpose : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19TransposeE) [Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)transpose operation.Public Types

Public Functions

-
Transpose(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input_order)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19Transpose9TransposeERK6OutputI4NodeERK6OutputI4NodeE) Constructs a transpose operation.


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19Transpose24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v19Transpose12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Transpose(const