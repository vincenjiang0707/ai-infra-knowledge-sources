source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v9_1_1_r_o_i_align.html
lastmod: 

# Class ov::op::v9::ROIAlign[#](https://docs.openvino.ai#class-ov-op-v9-roialign)

-
class ROIAlign : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ROIAlignBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_r_o_i_align_base.html#_CPPv4N2ov2op4util12ROIAlignBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v98ROIAlignE) Public Functions

-
ROIAlign(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &rois, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &batch_indices, const int pooled_h, const int pooled_w, const int sampling_ratio, const float spatial_scale, const PoolingMode mode, const AlignedMode aligned_mode = AlignedMode::ASYMMETRIC)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v98ROIAlign8ROIAlignERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeEKiKiKiKfK11PoolingModeK11AlignedMode) Constructs a

[ROIAlign](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v9_1_1_r_o_i_align)operation.- Parameters:
**input**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)feature map {N, C, H, W}**rois**– Regions of interest to pool over**batch_indices**– Indices of images in the batch matching the number or ROIs**pooled_h**– Height of the ROI output features**pooled_w**– Width of the ROI output features**sampling_ratio**– Number of sampling points used to compute an output element**spatial_scale**– Spatial scale factor used to translate ROI coordinates**mode**– Method of pooling - ‘avg’ or ‘max’**aligned_mode**– Method of coordinates alignment - ‘asymmetric’, ‘half_pixel_for_nn’ or ‘half_pixel’



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v98ROIAlign24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
ROIAlign(const