source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_fake_quantize_decomposition.html
lastmod: 

# Class ov::pass::FakeQuantizeDecomposition[#](https://docs.openvino.ai#class-ov-pass-fakequantizedecomposition)

-
class FakeQuantizeDecomposition : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass25FakeQuantizeDecompositionE) [FakeQuantizeDecomposition](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_fake_quantize_decomposition)transformation decomposes FakeQuantize layer.Expression from specification: if x <= min(input_low, input_high): output = output_low elif x > max(input_low, input_high): output = output_high else: output = round((x - input_low) / (input_high - input_low) * (levels-1)) / (levels-1) * (output_high - output_low) + output_low

expand brackets into round: round(x * (levels-1) / (input_high - input_low) - input_low * (levels-1) / (input_high - input_low)) div on (levels-1) and mult on (output_high - output_low) => mult on (output_high - output_low) / (levels-1)

=> round(x * (levels-1) / (input_high - input_low) - input_low * (levels-1) / (input_high - input_low)) * (output_high - output_low) / (levels-1) + output_low

This transformation doesn’t support following cases:

At least one ‘range’ input is not Constant

At least one ‘input_low’ input value greater or equal than ‘input_high’ input value