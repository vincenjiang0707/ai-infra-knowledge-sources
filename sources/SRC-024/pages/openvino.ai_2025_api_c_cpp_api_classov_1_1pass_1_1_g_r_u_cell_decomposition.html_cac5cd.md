source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_g_r_u_cell_decomposition.html
lastmod: 

# Class ov::pass::GRUCellDecomposition[#](https://docs.openvino.ai#class-ov-pass-grucelldecomposition)

-
class GRUCellDecomposition : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass20GRUCellDecompositionE) [GRUCellDecomposition](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_g_r_u_cell_decomposition)transformation decomposes GRUCell layer with inputs X, H, W, R, B to Add, Split, MatMul, Multiply and Subtract ops according to the formula: (.) - Denotes element-wise multiplication.Denotes dot product. f, g - are activation functions


zt = f(Xt*(Wz^T) + Ht-1*(Rz^T) + Wbz + Rbz) rt = f(Xt*(Wr^T) + Ht-1*(Rr^T) + Wbr + Rbr) ht = g(Xt*(Wh^T) + (rt (.) Ht-1)*(Rh^T) + Rbh + Wbh) # when linear_before_reset := false # (default) ht = g(Xt*(Wh^T) + (rt (.) (Ht-1*(Rh^T) + Rbh)) + Wbh) # when linear_before_reset:= true Ht = (1 - zt) (.) ht + zt (.) Ht-1