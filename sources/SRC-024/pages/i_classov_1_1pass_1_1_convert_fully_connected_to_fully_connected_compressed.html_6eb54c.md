source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_convert_fully_connected_to_fully_connected_compressed.html
lastmod: 

# Class ov::pass::ConvertFullyConnectedToFullyConnectedCompressed[#](https://docs.openvino.ai#class-ov-pass-convertfullyconnectedtofullyconnectedcompressed)

-
class ConvertFullyConnectedToFullyConnectedCompressed : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass47ConvertFullyConnectedToFullyConnectedCompressedE) Public Static Functions

Processes compressed weights from a pattern block and prepares them for compressed operations.

- Parameters:
**weights_block**– The CompressedWeightsBlock pattern containing the weight compression graph**pattern_map**– The pattern value map from the matcher containing matched nodes**convert_u4zp_to_u8**– Flag indicating whether to convert u4 zero points to u8**has_transpose**– Flag indicating whether the weights require transpose operation**grouped**– Flag indicating whether the compression uses grouped quantization**batched_weights**– Flag indicating whether the weights have a batch dimension**result_nodes**–[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)vector to collect intermediate nodes created during processing

- Returns:
A tuple containing processed compressed weights, decompression scales, and decompression zero points.