source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_p_relu_fusion_negative_add.html
lastmod: 

# Class ov::pass::PReluFusionNegativeAdd[#](https://docs.openvino.ai#class-ov-pass-prelufusionnegativeadd)

-
class PReluFusionNegativeAdd : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass22PReluFusionNegativeAddE) [PReluFusionNegativeAdd](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_p_relu_fusion_negative_add)transformation replaces a sub-graph Op / \ Relu Negative | | | Relu | | | Negative | | | Multiply \ / Add.

Site Navigation

Section Navigation

[PReluFusionNegativeAdd](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_p_relu_fusion_negative_add) transformation replaces a sub-graph Op / \ Relu Negative | | | Relu | | | Negative | | | Multiply \ / Add.