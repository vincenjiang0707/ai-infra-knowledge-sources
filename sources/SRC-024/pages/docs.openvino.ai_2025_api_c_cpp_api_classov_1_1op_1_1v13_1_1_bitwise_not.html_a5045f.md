source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v13_1_1_bitwise_not.html
lastmod: 

# Class ov::op::v13::BitwiseNot[#](https://docs.openvino.ai#class-ov-op-v13-bitwisenot)

-
class BitwiseNot : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1310BitwiseNotE) Elementwise bitwise negation operation.

Public Functions

-
BitwiseNot() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1310BitwiseNot10BitwiseNotEv) Constructs a bitwise negation operation.


-
BitwiseNot(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1310BitwiseNot10BitwiseNotERK6OutputI4NodeE) Constructs a bitwise negation operation.

- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1310BitwiseNot24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
BitwiseNot() = default