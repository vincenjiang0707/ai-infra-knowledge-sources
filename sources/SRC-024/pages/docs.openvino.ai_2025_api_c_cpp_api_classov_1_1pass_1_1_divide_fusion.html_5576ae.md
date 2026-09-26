source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_divide_fusion.html
lastmod: 

# Class ov::pass::DivideFusion[#](https://docs.openvino.ai#class-ov-pass-dividefusion)

-
class DivideFusion : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass12DivideFusionE) [DivideFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_divide_fusion)transformation replaces a sub-graph Pow(y, -1) * x or x * Pow(y, -1) with Divide(x,y)

Site Navigation

Section Navigation

[DivideFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_divide_fusion) transformation replaces a sub-graph Pow(y, -1) * x or x * Pow(y, -1) with Divide(x,y)