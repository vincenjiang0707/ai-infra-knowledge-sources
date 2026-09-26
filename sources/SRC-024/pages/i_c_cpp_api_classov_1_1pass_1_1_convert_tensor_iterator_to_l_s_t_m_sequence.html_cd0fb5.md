source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_convert_tensor_iterator_to_l_s_t_m_sequence.html
lastmod: 

# Class ov::pass::ConvertTensorIteratorToLSTMSequence[#](https://docs.openvino.ai#class-ov-pass-converttensoriteratortolstmsequence)

-
class ConvertTensorIteratorToLSTMSequence : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass35ConvertTensorIteratorToLSTMSequenceE) Finds all TensorIterator layers, detects the pattern Squeeze->LSTMCell->Unsqueeze in the TensorIterator body, converts this pattern to LSTMSequence layer and replaces them TensorIterator.