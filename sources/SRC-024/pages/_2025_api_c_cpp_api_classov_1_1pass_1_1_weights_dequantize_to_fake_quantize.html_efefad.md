source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_weights_dequantize_to_fake_quantize.html
lastmod: 

# Class ov::pass::WeightsDequantizeToFakeQuantize[#](https://docs.openvino.ai#class-ov-pass-weightsdequantizetofakequantize)

-
class WeightsDequantizeToFakeQuantize : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass31WeightsDequantizeToFakeQuantizeE) [WeightsDequantizeToFakeQuantize](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_weights_dequantize_to_fake_quantize)transformation replaces Constant (i8) -> Convert (to fp) -> Subtract (zp) -> Multiply (scale) -> with Constant (i8) -> Convert (to fp) -> FakeQuantize -> deducing levels and FakeQuantize limits according to actual values in the weights Constant.