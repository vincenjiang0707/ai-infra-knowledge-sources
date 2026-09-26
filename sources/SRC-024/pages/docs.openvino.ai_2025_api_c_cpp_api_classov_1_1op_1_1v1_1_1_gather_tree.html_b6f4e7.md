source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v1_1_1_gather_tree.html
lastmod: 

# Class ov::op::v1::GatherTree[#](https://docs.openvino.ai#class-ov-op-v1-gathertree)

-
class GatherTree : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v110GatherTreeE) Generates the complete beams from the ids per each step and the parent beam ids.

Public Functions

-
GatherTree(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &step_ids, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &parent_idx, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &max_seq_len, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &end_token)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v110GatherTree10GatherTreeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) - Parameters:
**step_ids**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)of shape [MAX_TIME, BATCH_SIZE, BEAM_WIDTH] with indices from per each step**parent_idx**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)of shape [MAX_TIME, BATCH_SIZE, BEAM_WIDTH] with parent beam indices**max_seq_len**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)of shape [BATCH_SIZE] with maximum lengths for each sequence in the batch**end_token**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)of shape [MAX_TIME, BATCH_SIZE, BEAM_WIDTH]



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v110GatherTree24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
GatherTree(const