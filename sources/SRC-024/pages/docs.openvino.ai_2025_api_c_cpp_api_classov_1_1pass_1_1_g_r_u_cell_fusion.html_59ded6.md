source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_g_r_u_cell_fusion.html
lastmod: 

# Class ov::pass::GRUCellFusion[#](https://docs.openvino.ai#class-ov-pass-grucellfusion)

-
class GRUCellFusion : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass13GRUCellFusionE) [GRUCellFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_g_r_u_cell_fusion)transformation replaces a sequence of operations with GRUCell op.If BiasAdds are not present in the pattern, then Constants with zero values will be created to match the specification.

Supported activations: Relu, Sigmoid, Tanh Clip attribute is not supported. Linear_before_reset attribute is not supported. Supported weights formats: zr, rz