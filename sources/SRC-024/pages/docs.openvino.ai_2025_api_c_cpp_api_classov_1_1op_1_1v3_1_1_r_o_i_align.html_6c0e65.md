source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v3_1_1_r_o_i_align.html
lastmod: 

# Class ov::op::v3::ROIAlign[#](https://docs.openvino.ai#class-ov-op-v3-roialign)

-
class ROIAlign : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ROIAlignBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_r_o_i_align_base.html#_CPPv4N2ov2op4util12ROIAlignBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v38ROIAlignE) [ROIAlign](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_r_o_i_align)operation.Public Functions

-
ROIAlign(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &rois, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &batch_indices, const int pooled_h, const int pooled_w, const int sampling_ratio, const float spatial_scale, const std::string &mode)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v38ROIAlign8ROIAlignERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeEKiKiKiKfRKNSt6stringE) Constructs a

[ROIAlign](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_r_o_i_align)node matching the ONNX[ROIAlign](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_r_o_i_align)specification Check[util::ROIAlignBase](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_r_o_i_align_base)for description of common params.- Parameters:
**mode**– Method of pooling - ‘avg’ or ‘max’


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v38ROIAlign24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v38ROIAlign12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
ROIAlign(const