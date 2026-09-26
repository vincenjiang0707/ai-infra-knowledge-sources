source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_convert_tensor_iterator_to_g_r_u_sequence.html
lastmod: 

# Class ov::pass::ConvertTensorIteratorToGRUSequence[#](https://docs.openvino.ai#class-ov-pass-converttensoriteratortogrusequence)

-
class ConvertTensorIteratorToGRUSequence : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass34ConvertTensorIteratorToGRUSequenceE) Finds all TensorIterator layers, detects the pattern Squeeze->GRUCell->Unsqueeze in the TensorIterator body, converts this pattern to GRUSequence layer and replaces them TensorIterator.