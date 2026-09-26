source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_region_yolo.html
lastmod: 

# Class ov::op::v0::RegionYolo[#](https://docs.openvino.ai#class-ov-op-v0-regionyolo)

-
class RegionYolo : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v010RegionYoloE) [RegionYolo](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_region_yolo)operation.Public Functions

-
RegionYolo(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input, const size_t coords, const size_t classes, const size_t regions, const bool do_softmax, const std::vector<int64_t> &mask, const int axis, const int end_axis, const std::vector<float> &anchors = std::vector<float>{})[#](https://docs.openvino.ai#_CPPv4N2ov2op2v010RegionYolo10RegionYoloERK6OutputI4NodeEK6size_tK6size_tK6size_tKbRKNSt6vectorI7int64_tEEKiKiRKNSt6vectorIfEE) Constructs a

[RegionYolo](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_region_yolo)operation.- Parameters:
**input**–**[in]**[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)**coords**–**[in]**Number of coordinates for each region**classes**–**[in]**Number of classes for each region**regions**–**[in]**Number of regions**do_softmax**–**[in]**Compute softmax**mask**–**[in]**[Mask](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_mask)**axis**–**[in]**Axis to begin softmax on**end_axis**–**[in]**Axis to end softmax on**anchors**–**[in]**A flattened list of pairs`[width, height]`

that describes prior box sizes.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v010RegionYolo24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
RegionYolo(const