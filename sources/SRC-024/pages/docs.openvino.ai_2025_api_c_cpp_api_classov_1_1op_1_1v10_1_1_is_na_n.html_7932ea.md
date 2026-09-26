source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v10_1_1_is_na_n.html
lastmod: 

# Class ov::op::v10::IsNaN[#](https://docs.openvino.ai#class-ov-op-v10-isnan)

-
class IsNaN : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v105IsNaNE) Boolean mask that maps NaN values to true and other values to false.

Public Functions

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v105IsNaN24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual void validate_and_infer_types() override