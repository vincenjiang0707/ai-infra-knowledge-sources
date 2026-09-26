source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v6_1_1_experimental_detectron_generate_proposals_single_image.html
lastmod: 

# Class ov::op::v6::ExperimentalDetectronGenerateProposalsSingleImage[#](https://docs.openvino.ai#class-ov-op-v6-experimentaldetectrongenerateproposalssingleimage)

-
class ExperimentalDetectronGenerateProposalsSingleImage : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v649ExperimentalDetectronGenerateProposalsSingleImageE) An operation

[ExperimentalDetectronGenerateProposalsSingleImage](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_generate_proposals_single_image)computes ROIs and their scores based on input data.Public Functions

-
ExperimentalDetectronGenerateProposalsSingleImage(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &im_info, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &anchors, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &deltas, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &scores, const[Attributes](https://docs.openvino.ai#_CPPv4N2ov2op2v649ExperimentalDetectronGenerateProposalsSingleImage10AttributesE)&attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v649ExperimentalDetectronGenerateProposalsSingleImage49ExperimentalDetectronGenerateProposalsSingleImageERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK10Attributes) Constructs a

[ExperimentalDetectronGenerateProposalsSingleImage](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_generate_proposals_single_image)operation.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v649ExperimentalDetectronGenerateProposalsSingleImage24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
struct Attributes
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v649ExperimentalDetectronGenerateProposalsSingleImage10AttributesE) Structure that specifies attributes of the operation.


-
ExperimentalDetectronGenerateProposalsSingleImage(const