source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v15_1_1_bitwise_right_shift.html
lastmod: 

# Class ov::op::v15::BitwiseRightShift[#](https://docs.openvino.ai#class-ov-op-v15-bitwiserightshift)

-
class BitwiseRightShift : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BinaryElementwiseBitwise](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_binary_elementwise_bitwise.html#_CPPv4N2ov2op4util24BinaryElementwiseBitwiseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1517BitwiseRightShiftE) Elementwise bitwise

[BitwiseRightShift](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_bitwise_right_shift)operation.Public Functions

-
BitwiseRightShift() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1517BitwiseRightShift17BitwiseRightShiftEv) Constructs a bitwise

[BitwiseRightShift](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_bitwise_right_shift)operation.

-
BitwiseRightShift(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg0, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg1, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)([AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE)))[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1517BitwiseRightShift17BitwiseRightShiftERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs a bitwise

[BitwiseRightShift](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_bitwise_right_shift)operation.[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)`[d0, ...]`


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1517BitwiseRightShift24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op3v1517BitwiseRightShift12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
BitwiseRightShift() = default