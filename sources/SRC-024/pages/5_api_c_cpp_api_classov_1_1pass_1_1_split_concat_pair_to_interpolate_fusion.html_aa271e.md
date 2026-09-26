source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_split_concat_pair_to_interpolate_fusion.html
lastmod: 

# Class ov::pass::SplitConcatPairToInterpolateFusion[#](https://docs.openvino.ai#class-ov-pass-splitconcatpairtointerpolatefusion)

-
class SplitConcatPairToInterpolateFusion : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass34SplitConcatPairToInterpolateFusionE) [SplitConcatPairToInterpolateFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_split_concat_pair_to_interpolate_fusion)transformation replaces group of operations: Split -> Concat to Interpolate op.