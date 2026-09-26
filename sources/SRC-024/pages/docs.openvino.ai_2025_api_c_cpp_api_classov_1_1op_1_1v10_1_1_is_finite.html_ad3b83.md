source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v10_1_1_is_finite.html
lastmod: 

# Class ov::op::v10::IsFinite[#](https://docs.openvino.ai#class-ov-op-v10-isfinite)

-
class IsFinite : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v108IsFiniteE) Boolean mask that maps NaN and Infinity values to false and other values to true.

Public Functions

-
IsFinite(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v108IsFinite8IsFiniteERK6OutputI4NodeE) Constructs a

[IsFinite](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v10_1_1_is_finite)operation.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)data tensor


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v108IsFinite24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
IsFinite(const