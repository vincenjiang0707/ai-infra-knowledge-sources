source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_subtract_fusion.html
lastmod: 

# Class ov::pass::SubtractFusion[#](https://docs.openvino.ai#class-ov-pass-subtractfusion)

-
class SubtractFusion : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass14SubtractFusionE) [SubtractFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_subtract_fusion)transformation replaces a sub-graph Mul(y, -1) + x or x + Mul(y, -1) with Subtract(x,y)

Site Navigation

Section Navigation

[SubtractFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_subtract_fusion) transformation replaces a sub-graph Mul(y, -1) + x or x + Mul(y, -1) with Subtract(x,y)