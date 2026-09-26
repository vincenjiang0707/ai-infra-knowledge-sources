source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_fake_convert_decomposition.html
lastmod: 

# Class ov::pass::FakeConvertDecomposition[#](https://docs.openvino.ai#class-ov-pass-fakeconvertdecomposition)

-
class FakeConvertDecomposition : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass24FakeConvertDecompositionE) [FakeConvertDecomposition](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_fake_convert_decomposition)transformation decomposes FakeConvert layer. f8: f8e4m3, f8e5m2 downconvert: f32->f8, f16->f8, bf16->f8 upconvert: f8->f32, f8->f16, f8->bf16 output = (upconvert(downconvert(input * scale - shift)) + shift) / scale.