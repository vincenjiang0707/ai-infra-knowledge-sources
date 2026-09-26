source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_h_sigmoid_fusion_with_relu_mul.html
lastmod: 

# Class ov::pass::HSigmoidFusionWithReluMul[#](https://docs.openvino.ai#class-ov-pass-hsigmoidfusionwithrelumul)

-
class HSigmoidFusionWithReluMul : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass25HSigmoidFusionWithReluMulE) [HSigmoidFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_h_sigmoid_fusion)transformation replaces a sub-graph ((min(Relu(x + 3), 6)) * const(1/6)) with a HSigmoid op.

Site Navigation

Section Navigation

[HSigmoidFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_h_sigmoid_fusion) transformation replaces a sub-graph ((min(Relu(x + 3), 6)) * const(1/6)) with a HSigmoid op.