source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_clamp.html
lastmod: 

# Class ov::op::v0::Clamp[#](https://docs.openvino.ai#class-ov-op-v0-clamp)

-
class Clamp : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v05ClampE) Performs a clipping operation on all elements of the input node.

All input values that are outside of the <min;max> range are set to ‘min’ or ‘max’ depending on which side of the <min;max> range they are. The values that fall into this range remain unchanged.

Public Functions

-
Clamp(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const double min, const double max)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v05Clamp5ClampERK6OutputI4NodeEKdKd) Constructs a

[Clamp](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_clamp)node.- Parameters:
**data**– -[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the input tensor**min**– - the lower bound of the <min;max> range**max**– - the upper bound of the <min;max> range



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v05Clamp24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v05Clamp12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Clamp(const