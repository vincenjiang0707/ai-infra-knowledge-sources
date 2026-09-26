source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v10_1_1_is_inf.html
lastmod: 

# Class ov::op::v10::IsInf[#](https://docs.openvino.ai#class-ov-op-v10-isinf)

-
class IsInf : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v105IsInfE) Boolean mask that maps infinite values to true.

Public Functions

-
IsInf(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Attributes](https://docs.openvino.ai#_CPPv4N2ov2op3v105IsInf10AttributesE)&attributes)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v105IsInf5IsInfERK6OutputI4NodeERK10Attributes) Constructs a

[IsInf](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v10_1_1_is_inf)operation.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v105IsInf24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
IsInf(const