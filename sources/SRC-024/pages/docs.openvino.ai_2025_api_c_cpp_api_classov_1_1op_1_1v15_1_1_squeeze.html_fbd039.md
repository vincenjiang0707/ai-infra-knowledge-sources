source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v15_1_1_squeeze.html
lastmod: 

# Class ov::op::v15::Squeeze[#](https://docs.openvino.ai#class-ov-op-v15-squeeze)

-
class Squeeze : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[SqueezeBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_squeeze_base.html#_CPPv4N2ov2op4util11SqueezeBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v157SqueezeE) [Squeeze](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_squeeze)operation.Public Functions

-
Squeeze(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const bool allow_axis_skip = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v157Squeeze7SqueezeERK6OutputI4NodeEKb) Constructs a squeeze

[v15](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1op_1_1v15)operation.

-
Squeeze(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axes, const bool allow_axis_skip = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v157Squeeze7SqueezeERK6OutputI4NodeERK6OutputI4NodeEKb) Constructs a squeeze

[v15](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1op_1_1v15)operation.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v157Squeeze24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
Squeeze(const