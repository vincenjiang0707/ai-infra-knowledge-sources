source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_normalize_l2.html
lastmod: 

# Class ov::op::v0::NormalizeL2[#](https://docs.openvino.ai#class-ov-op-v0-normalizel2)

-
class NormalizeL2 : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v011NormalizeL2E) Normalization with L2 norm.

Public Functions

-
NormalizeL2(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axes, float eps,[EpsMode](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7EpsModeE)eps_mode)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v011NormalizeL211NormalizeL2ERK6OutputI4NodeERK6OutputI4NodeEf7EpsMode) Constructs a

[NormalizeL2](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_normalize_l2)operation.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v011NormalizeL224validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
NormalizeL2(const