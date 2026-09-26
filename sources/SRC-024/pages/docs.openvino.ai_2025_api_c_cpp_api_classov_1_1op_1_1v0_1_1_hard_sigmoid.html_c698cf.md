source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_hard_sigmoid.html
lastmod: 

# Class ov::op::v0::HardSigmoid[#](https://docs.openvino.ai#class-ov-op-v0-hardsigmoid)

-
class HardSigmoid : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v011HardSigmoidE) Parameterized, bounded sigmoid-like, piecewise linear function. min(max(alpha*x + beta, 0), 1)

Public Functions

-
HardSigmoid(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &alpha, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &beta)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v011HardSigmoid11HardSigmoidERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) Constructs a

[HardSigmoid](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_hard_sigmoid)operation.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor.**alpha**–**[in]**A scalar value representing the alpha parameter.**beta**–**[in]**A scalar value representing the beta parameter.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v011HardSigmoid24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
HardSigmoid(const