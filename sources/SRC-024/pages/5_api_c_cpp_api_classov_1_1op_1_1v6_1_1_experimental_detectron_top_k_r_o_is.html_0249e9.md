source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v6_1_1_experimental_detectron_top_k_r_o_is.html
lastmod: 

# Class ov::op::v6::ExperimentalDetectronTopKROIs[#](https://docs.openvino.ai#class-ov-op-v6-experimentaldetectrontopkrois)

-
class ExperimentalDetectronTopKROIs : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v629ExperimentalDetectronTopKROIsE) An operation

[ExperimentalDetectronTopKROIs](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_top_k_r_o_is), according to the repository is TopK operation applied to probabilities of input ROIs.Public Functions

-
ExperimentalDetectronTopKROIs(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input_rois, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &rois_probs, size_t max_rois = 0)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v629ExperimentalDetectronTopKROIs29ExperimentalDetectronTopKROIsERK6OutputI4NodeERK6OutputI4NodeE6size_t) Constructs a

[ExperimentalDetectronTopKROIs](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_top_k_r_o_is)operation.- Parameters:
**input_rois**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)rois**rois_probs**– Probabilities for input rois**max_rois**– Maximal numbers of output rois



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v629ExperimentalDetectronTopKROIs24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
ExperimentalDetectronTopKROIs(const