source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_proposal.html
lastmod: 

# Class ov::op::v0::Proposal[#](https://docs.openvino.ai#class-ov-op-v0-proposal)

-
class Proposal : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08ProposalE) [Proposal](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_proposal)operation.Subclassed by

[ov::op::v4::Proposal](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_proposal)Unnamed Group

-
void set_attrs(
[Attributes](https://docs.openvino.ai/structov_1_1op_1_1v0_1_1_proposal_1_1_attributes.html#_CPPv4N2ov2op2v08Proposal10AttributesE)&&attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08Proposal9set_attrsERR10Attributes) Set the

[Proposal](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_proposal)operator attributes.- Parameters:
**attrs**–[Attributes](https://docs.openvino.ai/group__ov__transformation__common__api.html#structov_1_1op_1_1v0_1_1_proposal_1_1_attributes)to be set.


Public Functions

-
Proposal(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &class_probs, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &bbox_deltas, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &image_shape, const[Attributes](https://docs.openvino.ai/structov_1_1op_1_1v0_1_1_proposal_1_1_attributes.html#_CPPv4N2ov2op2v08Proposal10AttributesE)&attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08Proposal8ProposalERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK10Attributes) Constructs a

[Proposal](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_proposal)operation.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08Proposal24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
struct Attributes
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08Proposal10AttributesE)

-
void set_attrs(