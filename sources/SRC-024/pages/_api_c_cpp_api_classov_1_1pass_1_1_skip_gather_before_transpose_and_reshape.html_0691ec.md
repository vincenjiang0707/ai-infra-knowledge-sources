source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_skip_gather_before_transpose_and_reshape.html
lastmod: 

# Class ov::pass::SkipGatherBeforeTransposeAndReshape[#](https://docs.openvino.ai#class-ov-pass-skipgatherbeforetransposeandreshape)

-
class SkipGatherBeforeTransposeAndReshape : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass35SkipGatherBeforeTransposeAndReshapeE) [SkipGatherBeforeTransposeAndReshape](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_skip_gather_before_transpose_and_reshape)transformation removes Gather from the Gather->Transpose->Reshape sequence in case when input has batch=1 and gather has axis=0 and indices={0}. Also, this transformation corrects a transpose constant to save semantic.