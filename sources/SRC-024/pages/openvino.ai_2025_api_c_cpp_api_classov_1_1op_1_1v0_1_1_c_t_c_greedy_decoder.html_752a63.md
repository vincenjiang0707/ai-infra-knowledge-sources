source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_c_t_c_greedy_decoder.html
lastmod: 

# Class ov::op::v0::CTCGreedyDecoder[#](https://docs.openvino.ai#class-ov-op-v0-ctcgreedydecoder)

-
class CTCGreedyDecoder : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v016CTCGreedyDecoderE) [CTCGreedyDecoder](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_c_t_c_greedy_decoder)operation.Public Functions

-
CTCGreedyDecoder(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &seq_len, const bool ctc_merge_repeated)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v016CTCGreedyDecoder16CTCGreedyDecoderERK6OutputI4NodeERK6OutputI4NodeEKb) Constructs a

[CTCGreedyDecoder](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_c_t_c_greedy_decoder)operation.- Parameters:
**input**– Logits on which greedy decoding is performed**seq_len**– Sequence lengths**ctc_merge_repeated**– Whether to merge repeated labels



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v016CTCGreedyDecoder24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
CTCGreedyDecoder(const