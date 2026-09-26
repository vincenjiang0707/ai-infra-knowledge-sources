source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v4_1_1_c_t_c_loss.html
lastmod: 

# Class ov::op::v4::CTCLoss[#](https://docs.openvino.ai#class-ov-op-v4-ctcloss)

-
class CTCLoss : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v47CTCLossE) [CTCLoss](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_c_t_c_loss)operation.Public Functions

-
CTCLoss(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &logits, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &logit_length, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &labels, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &label_length, const bool preprocess_collapse_repeated = false, const bool ctc_merge_repeated = true, const bool unique = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v47CTCLoss7CTCLossERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeEKbKbKb) Constructs a

[CTCLoss](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_c_t_c_loss)operation.- Parameters:
**logits**– 3-D tensor of logits**logit_length**– 1-D tensor of length for each object from a batch**labels**– 2-D tensor of labels for which likelyhood is estimated using logist**label_length**– 1-D tensor of length for each label sequence**blank_index**– Scalar used to mark a blank index**preprocess_collapse_repeated**– Flag for preprocessing labels before loss calculation**ctc_merge_repeated**– Flag for merging repeated characters in a potential alignment**unique**– Flag to find unique elements in a target before matching with alignment



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v47CTCLoss24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
CTCLoss(const