source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_xor.html
lastmod: 

# Class ov::op::v0::Xor[#](https://docs.openvino.ai#class-ov-op-v0-xor)

-
class Xor : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BinaryElementwiseLogical](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_binary_elementwise_logical.html#_CPPv4N2ov2op4util24BinaryElementwiseLogicalE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03XorE) Elementwise logical-xor operation.

Public Functions

-
Xor(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg0, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg1, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)())[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03Xor3XorERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs a logical-xor operation.

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)`[d0, ...]`


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v03Xor12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Xor(const