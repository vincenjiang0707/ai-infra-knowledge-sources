source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_convert_batch_to_space.html
lastmod: 

# Class ov::pass::ConvertBatchToSpace[#](https://docs.openvino.ai#class-ov-pass-convertbatchtospace)

-
class ConvertBatchToSpace : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass19ConvertBatchToSpaceE) [ConvertBatchToSpace](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_convert_batch_to_space)transformation decomposes BatchToSpace layer to Reshape->Transpose->Reshape->Crop.- Param convert_by_elements:
- reduces the maximum number of dimensions that arise during the transformation if enabled. Default value: true. false - BatchToSpace decomposes to Reshape->Transpose->Reshape->Crop. During transformation, the number of tensor dimensions can be increased by length of block_shape input of BatchToSpace layer. true - BatchToSpace decomposes to N x (Reshape->Transpose->Reshape)->Crop, where N = length of block_shape input of BatchToSpace layer. During transformation, the number of tensor dimensions can be increased by 1.