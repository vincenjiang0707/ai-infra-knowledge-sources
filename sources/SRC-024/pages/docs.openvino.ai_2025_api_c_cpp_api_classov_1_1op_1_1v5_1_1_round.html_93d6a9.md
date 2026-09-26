source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v5_1_1_round.html
lastmod: 

# Class ov::op::v5::Round[#](https://docs.openvino.ai#class-ov-op-v5-round)

-
class Round : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v55RoundE) Elementwise round operation. The output is round to the nearest integer for each value. In case of halfs, the rule is defined in attribute ‘mode’: ‘HALF_TO_EVEN’ - round halfs to the nearest even integer. ‘HALF_AWAY_FROM_ZERO’: - round in such a way that the result heads away from zero.

Public Functions

-
Round() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v55Round5RoundEv) Constructs a round operation.


-
Round(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const RoundMode mode)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v55Round5RoundERK6OutputI4NodeEK9RoundMode) Constructs a round operation.

- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.**mode**– Rule to resolve halfs



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v55Round24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v55Round12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Round() = default