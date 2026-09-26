source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v4_1_1_proposal.html
lastmod: 

# Class ov::op::v4::Proposal[#](https://docs.openvino.ai#class-ov-op-v4-proposal)

-
class Proposal : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[v0](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op2v0E)::[Proposal](https://docs.openvino.ai/classov_1_1op_1_1v0_1_1_proposal.html#_CPPv4N2ov2op2v08ProposalE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v48ProposalE) [Proposal](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_proposal)operation.Public Functions

-
Proposal(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &class_probs, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &bbox_deltas, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &image_shape, const Attributes &attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v48Proposal8ProposalERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK10Attributes) Constructs a

[Proposal](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_proposal)operation.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v48Proposal24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
Proposal(const