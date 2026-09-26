source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_a_u_g_r_u_cell_fusion.html
lastmod: 

# Class ov::pass::AUGRUCellFusion[#](https://docs.openvino.ai#class-ov-pass-augrucellfusion)

-
class AUGRUCellFusion : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass15AUGRUCellFusionE) [AUGRUCellFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_a_u_g_r_u_cell_fusion)transformation replaces a sequence of operations with AUGRUCell op.Supported activations: 1st is Sigmoid, 2nd is Tanh Clip attribute is not supported. Linear_before_reset attribute is not supported. Supported weights format: ‘rzh’