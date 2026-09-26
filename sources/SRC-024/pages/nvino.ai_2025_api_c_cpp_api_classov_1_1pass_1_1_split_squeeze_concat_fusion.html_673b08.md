source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_split_squeeze_concat_fusion.html
lastmod: 

# Class ov::pass::SplitSqueezeConcatFusion[#](https://docs.openvino.ai#class-ov-pass-splitsqueezeconcatfusion)

-
class SplitSqueezeConcatFusion : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass24SplitSqueezeConcatFusionE) [SplitSqueezeConcatFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_split_squeeze_concat_fusion)transformation replaces group of operations: Split -> Squeeze (multiple) -> Concat to Transpose -> Reshape ops.