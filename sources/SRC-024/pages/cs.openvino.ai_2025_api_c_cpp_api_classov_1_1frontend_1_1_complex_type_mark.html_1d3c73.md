source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1frontend_1_1_complex_type_mark.html
lastmod: 

# Class ov::frontend::ComplexTypeMark[#](https://docs.openvino.ai#class-ov-frontend-complextypemark)

-
class ComplexTypeMark : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[FrameworkNode](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_framework_node.html#_CPPv4N2ov2op4util13FrameworkNodeE)[#](https://docs.openvino.ai#_CPPv4N2ov8frontend15ComplexTypeMarkE) Public Functions

-
inline virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov8frontend15ComplexTypeMark24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline virtual void validate_and_infer_types() override