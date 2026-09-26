source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_p_relu_fusion_multiply_sub.html
lastmod: 

# Class ov::pass::PReluFusionMultiplySub[#](https://docs.openvino.ai#class-ov-pass-prelufusionmultiplysub)

-
class PReluFusionMultiplySub : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass22PReluFusionMultiplySubE) [PReluFusionMultiplySub](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_p_relu_fusion_multiply_sub)transformation replaces a sub-graph Op / \ Relu Multiply (-1) | | | Relu | | | Multiply \ / Sub.

Site Navigation

Section Navigation

[PReluFusionMultiplySub](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_p_relu_fusion_multiply_sub) transformation replaces a sub-graph Op / \ Relu Multiply (-1) | | | Relu | | | Multiply \ / Sub.