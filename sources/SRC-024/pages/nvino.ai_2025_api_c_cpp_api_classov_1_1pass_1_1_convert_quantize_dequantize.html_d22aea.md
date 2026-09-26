source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_convert_quantize_dequantize.html
lastmod: 

# Class ov::pass::ConvertQuantizeDequantize[#](https://docs.openvino.ai#class-ov-pass-convertquantizedequantize)

-
class ConvertQuantizeDequantize : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass25ConvertQuantizeDequantizeE) [ConvertQuantizeDequantize](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_convert_quantize_dequantize)transformation replaces following graph: FakeQuantize->Convert->Convert->Subtract->Multiply with a single FakeQuantize. Restrictions:quantized data type must be i8 or u8

’levels’ attribute to FakeQuantize must be equal to 256

(output_low, output_high) must be (-128, 127) or (0, 256) (depends on sign of quantized data type)

’zero_point’ and ‘scale’ must be broadcastable to FakeQuantize’s output