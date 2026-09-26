source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v13_1_1_n_m_s_rotated.html
lastmod: 

# Class ov::op::v13::NMSRotated[#](https://docs.openvino.ai#class-ov-op-v13-nmsrotated)

-
class NMSRotated : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1310NMSRotatedE) [NMSRotated](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v13_1_1_n_m_s_rotated)operation.Public Functions

-
NMSRotated(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &boxes, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &scores, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &max_output_boxes_per_class, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &iou_threshold, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &score_threshold, const bool sort_result_descending = true, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&output_type =[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i64](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i64EN6Type_t3i64E), const bool clockwise = true)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1310NMSRotated10NMSRotatedERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeEKbRKN2ov7element4TypeEKb) Constructs a

[NMSRotated](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v13_1_1_n_m_s_rotated)operation.- Parameters:
**boxes**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)containing the coordinates of the bounding boxes**scores**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)containing the scores of the bounding boxes**max_output_boxes_per_class**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)containing maximum number of boxes to be selected per class**iou_threshold**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)containing intersection over union threshold**score_threshold**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)containing minimum score threshold**sort_result_descending**– Specifies whether it is necessary to sort selected boxes across batches**output_type**– Specifies the output type of the first and third output**clockwise**– Specifies the direction of the rotation



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1310NMSRotated24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
NMSRotated(const