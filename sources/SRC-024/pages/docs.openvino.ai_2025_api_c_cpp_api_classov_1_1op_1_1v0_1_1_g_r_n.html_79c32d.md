source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_g_r_n.html
lastmod: 

# Class ov::op::v0::GRN[#](https://docs.openvino.ai#class-ov-op-v0-grn)

-
class GRN : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03GRNE) Global Response Normalization with L2 norm (across channels only).

Public Functions

-
GRN(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, float bias)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03GRN3GRNERK6OutputI4NodeEf) Constructs a

[GRN](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_g_r_n)operation.- Parameters:
**data**– -[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the input tensor**bias**– - The bias added to the variance.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03GRN24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
GRN(const