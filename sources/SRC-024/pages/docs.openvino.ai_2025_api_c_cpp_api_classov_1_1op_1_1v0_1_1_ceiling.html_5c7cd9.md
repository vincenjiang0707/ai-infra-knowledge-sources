source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_ceiling.html
lastmod: 

# Class ov::op::v0::Ceiling[#](https://docs.openvino.ai#class-ov-op-v0-ceiling)

-
class Ceiling : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v07CeilingE) Elementwise ceiling operation.

Public Functions

-
Ceiling() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v07Ceiling7CeilingEv) Constructs a ceiling operation.


-
Ceiling(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v07Ceiling7CeilingERK6OutputI4NodeE) Constructs a ceiling operation.

- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v07Ceiling12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Ceiling() = default