source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1util_1_1_r_o_i_align_base.html
lastmod: 

# Class ov::op::util::ROIAlignBase[#](https://docs.openvino.ai#class-ov-op-util-roialignbase)

-
class ROIAlignBase : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util12ROIAlignBaseE) Base class for ROIAlignXXX operators.

Subclassed by

[ov::op::v15::ROIAlignRotated](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_r_o_i_align_rotated),[ov::op::v3::ROIAlign](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_r_o_i_align),[ov::op::v9::ROIAlign](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v9_1_1_r_o_i_align)Public Functions

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util12ROIAlignBase24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual void validate_and_infer_types() override