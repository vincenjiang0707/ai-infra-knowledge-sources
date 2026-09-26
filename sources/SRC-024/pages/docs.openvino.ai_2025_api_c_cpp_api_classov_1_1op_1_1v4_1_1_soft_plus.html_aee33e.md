source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v4_1_1_soft_plus.html
lastmod: 

# Class ov::op::v4::SoftPlus[#](https://docs.openvino.ai#class-ov-op-v4-softplus)

-
class SoftPlus : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v48SoftPlusE) A Self Regularized Non-Monotonic Neural Activation Function f(x) = ln(exp(x) + 1.)

Public Functions

-
SoftPlus(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v48SoftPlus8SoftPlusERK6OutputI4NodeE) Constructs an

[SoftPlus](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_soft_plus)operation.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v48SoftPlus24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v48SoftPlus12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
SoftPlus(const