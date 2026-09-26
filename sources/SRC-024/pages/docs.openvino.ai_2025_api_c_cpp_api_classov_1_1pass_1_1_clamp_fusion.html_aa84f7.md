source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_clamp_fusion.html
lastmod: 

# Class ov::pass::ClampFusion[#](https://docs.openvino.ai#class-ov-pass-clampfusion)

-
class ClampFusion : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass11ClampFusionE) [ClampFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_clamp_fusion)transformation replaces following graph: Maximum->Minimum to Clamp Restrictions:one of the parameters to Maximum is a scalar constant

one of the parameters to Minimum is a scalar constant