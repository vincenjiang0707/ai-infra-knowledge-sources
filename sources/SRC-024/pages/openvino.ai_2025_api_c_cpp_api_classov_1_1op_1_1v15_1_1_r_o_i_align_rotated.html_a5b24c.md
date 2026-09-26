source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v15_1_1_r_o_i_align_rotated.html
lastmod: 

# Class ov::op::v15::ROIAlignRotated[#](https://docs.openvino.ai#class-ov-op-v15-roialignrotated)

-
class ROIAlignRotated : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ROIAlignBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_r_o_i_align_base.html#_CPPv4N2ov2op4util12ROIAlignBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1515ROIAlignRotatedE) [ROIAlignRotated](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_r_o_i_align_rotated)operation.Public Functions

-
ROIAlignRotated(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &rois, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &batch_indices, const int pooled_h, const int pooled_w, const int sampling_ratio, const float spatial_scale, const bool clockwise_mode)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1515ROIAlignRotated15ROIAlignRotatedERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeEKiKiKiKfKb) Constructs a

[ROIAlignRotated](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_r_o_i_align_rotated)operation.- Parameters:
**input**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)feature map {N, C, H, W}**rois**– Regions of interest to pool over**batch_indices**– Indices of images in the batch matching the number or ROIs**pooled_h**– Height of the ROI output features**pooled_w**– Width of the ROI output features**sampling_ratio**– Number of sampling points used to compute an output element**spatial_scale**– Spatial scale factor used to translate ROI coordinates**clockwise_mode**– If true, rotation angle is interpreted as clockwise, otherwise as counterclockwise



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1515ROIAlignRotated24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
ROIAlignRotated(const