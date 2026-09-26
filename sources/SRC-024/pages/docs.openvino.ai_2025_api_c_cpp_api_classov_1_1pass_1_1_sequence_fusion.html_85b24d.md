source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_sequence_fusion.html
lastmod: 

# Class ov::pass::SequenceFusion[#](https://docs.openvino.ai#class-ov-pass-sequencefusion)

-
class SequenceFusion : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass14SequenceFusionE) [SequenceFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_sequence_fusion)transformation replaces a chain of Cells operations with single Sequence op.Supported cells: GRUCell, LSTMCell, RNNCell, AUGRUCell Prerequisites: the source of W,R,B inputs must be the same or it can be different Constants with the same type, shape and value.