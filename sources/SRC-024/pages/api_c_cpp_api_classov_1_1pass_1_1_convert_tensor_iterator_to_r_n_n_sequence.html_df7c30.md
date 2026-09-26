source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_convert_tensor_iterator_to_r_n_n_sequence.html
lastmod: 

# Class ov::pass::ConvertTensorIteratorToRNNSequence[#](https://docs.openvino.ai#class-ov-pass-converttensoriteratortornnsequence)

-
class ConvertTensorIteratorToRNNSequence : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass34ConvertTensorIteratorToRNNSequenceE) Finds all TensorIterator layers, detects the pattern Squeeze->RNNCell->Unsqueeze in the TensorIterator body, converts this pattern to RNNSequence layer and replaces them TensorIterator.