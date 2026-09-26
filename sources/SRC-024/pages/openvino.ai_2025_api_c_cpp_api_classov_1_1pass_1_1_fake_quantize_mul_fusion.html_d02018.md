source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_fake_quantize_mul_fusion.html
lastmod: 

# Class ov::pass::FakeQuantizeMulFusion[#](https://docs.openvino.ai#class-ov-pass-fakequantizemulfusion)

-
class FakeQuantizeMulFusion : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass21FakeQuantizeMulFusionE) This transformation looks for a FQ + Mul pair in the graph and moves the Mul operation above the FQ node. The last two inputs of FQ are multiplied by the value that was originally below the FQ node.