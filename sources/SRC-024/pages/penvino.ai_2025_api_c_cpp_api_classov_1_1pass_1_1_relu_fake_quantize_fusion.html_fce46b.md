source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_relu_fake_quantize_fusion.html
lastmod: 

# Class ov::pass::ReluFakeQuantizeFusion[#](https://docs.openvino.ai#class-ov-pass-relufakequantizefusion)

-
class ReluFakeQuantizeFusion : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass22ReluFakeQuantizeFusionE) [ReluFakeQuantizeFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_relu_fake_quantize_fusion)transformation replaces following graph: Relu -> FakeQuantize to FakeQuantize under following conditions:‘input_low’ input to FakeQuantize is a Constant

’input_low’ has non negative values