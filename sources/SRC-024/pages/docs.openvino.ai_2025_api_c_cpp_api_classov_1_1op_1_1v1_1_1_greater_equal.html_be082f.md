source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v1_1_1_greater_equal.html
lastmod: 

# Class ov::op::v1::GreaterEqual[#](https://docs.openvino.ai#class-ov-op-v1-greaterequal)

-
class GreaterEqual : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BinaryElementwiseComparison](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_binary_elementwise_comparison.html#_CPPv4N2ov2op4util27BinaryElementwiseComparisonE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v112GreaterEqualE) Elementwise greater-than-or-equal operation.

Public Functions

-
inline GreaterEqual()
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v112GreaterEqual12GreaterEqualEv) Constructs a greater-than-or-equal operation.


-
GreaterEqual(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg0, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg1, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)([AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE)))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v112GreaterEqual12GreaterEqualERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs a greater-than-or-equal operation.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v112GreaterEqual12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
inline GreaterEqual()