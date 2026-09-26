source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_reverse_sequence.html
lastmod: 

# Class ov::op::v0::ReverseSequence[#](https://docs.openvino.ai#class-ov-op-v0-reversesequence)

-
class ReverseSequence : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v015ReverseSequenceE) [ReverseSequence](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_reverse_sequence)operation.Public Functions

-
ReverseSequence(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &seq_lengths, int64_t batch_axis = 0, int64_t seq_axis = 1)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v015ReverseSequence15ReverseSequenceERK6OutputI4NodeERK6OutputI4NodeE7int64_t7int64_t) Constructs a

[ReverseSequence](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_reverse_sequence)operation.- Parameters:
**arg**– tensor with input data to reverse**seq_lengths**– 1D tensor of integers with sequence lengths in the input tensor.**batch_axis**– index of the batch dimension.**seq_axis**– index of the sequence dimension.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v015ReverseSequence24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
ReverseSequence(const