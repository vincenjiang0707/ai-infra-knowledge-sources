source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_total_sequence_length_pattern_qwen.html
lastmod: 

# Class ov::pass::TotalSequenceLengthPatternQwen[#](https://docs.openvino.ai#class-ov-pass-totalsequencelengthpatternqwen)

-
class TotalSequenceLengthPatternQwen : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass30TotalSequenceLengthPatternQwenE) Qwen model has a specific pattern for TotalSequenceLen place detection.

common pattern: Add (PrevSeqLen, CurrentSeqLen)

The CurrentSeqLen is presented in this form: CurrentSeqLen: Parameter(name: input_ids) -> ShapeOf -> Gather

Before applying this transformation, we already detected the PrevSeqLen place in the

[PrevSequenceLengthPattern](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_prev_sequence_length_pattern)and replaced it with the next subgraph: PrevSeqLen: Subtract (in: Parameter(name: max_context_len), in: CurrentSeqLen)