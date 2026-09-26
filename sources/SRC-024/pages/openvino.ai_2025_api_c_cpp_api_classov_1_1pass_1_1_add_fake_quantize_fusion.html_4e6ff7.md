source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_add_fake_quantize_fusion.html
lastmod: 

# Class ov::pass::AddFakeQuantizeFusion[#](https://docs.openvino.ai#class-ov-pass-addfakequantizefusion)

-
class AddFakeQuantizeFusion : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass21AddFakeQuantizeFusionE) [AddFakeQuantizeFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_add_fake_quantize_fusion)transformation replaces following graph: Add->FakeQuantize to a single FakeQuantize Restrictions:second input to Add is a Constant