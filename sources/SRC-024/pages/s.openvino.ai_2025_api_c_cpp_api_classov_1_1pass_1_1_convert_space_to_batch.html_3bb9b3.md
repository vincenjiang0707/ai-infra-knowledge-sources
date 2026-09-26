source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_convert_space_to_batch.html
lastmod: 

# Class ov::pass::ConvertSpaceToBatch[#](https://docs.openvino.ai#class-ov-pass-convertspacetobatch)

-
class ConvertSpaceToBatch : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass19ConvertSpaceToBatchE) [ConvertSpaceToBatch](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_convert_space_to_batch)transformation decomposes SpaceToBatch layer to Pad->Reshape->Transpose->Reshape.- Param convert_by_elements:
- reduces the maximum number of dimensions that arise during the transformation if enabled. Default value: true. false - SpaceToBatch decomposes to Pad->Reshape->Transpose->Reshape. During transformation, the number of tensor dimensions can be increased by length of block_shape input of SpaceToBatch layer. true - SpaceToBatch decomposes to Pad-> N x (Reshape->Transpose->Reshape), where N = length of block_shape input of SpaceToBatch layer. During transformation, the number of tensor dimensions can be increased by 1.