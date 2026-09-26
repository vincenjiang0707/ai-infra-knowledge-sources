source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v1_1_1_floor_mod.html
lastmod: 

# Class ov::op::v1::FloorMod[#](https://docs.openvino.ai#class-ov-op-v1-floormod)

-
class FloorMod : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BinaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_binary_elementwise_arithmetic.html#_CPPv4N2ov2op4util27BinaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v18FloorModE) Elementwise

[FloorMod](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_floor_mod)operation.Public Functions

-
inline FloorMod()
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v18FloorMod8FloorModEv) Constructs an uninitialized addition operation.


-
FloorMod(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg0, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg1, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v18FloorMod8FloorModERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs an Floor

[Mod](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_mod)operation.[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)`[d0, ...]`


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v18FloorMod12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
inline FloorMod()