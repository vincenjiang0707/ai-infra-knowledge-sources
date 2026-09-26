source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_l_s_t_m_cell_decomposition.html
lastmod: 

# Class ov::pass::LSTMCellDecomposition[#](https://docs.openvino.ai#class-ov-pass-lstmcelldecomposition)

-
class LSTMCellDecomposition : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass21LSTMCellDecompositionE) [LSTMCellDecomposition](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_l_s_t_m_cell_decomposition)transformation decomposes LSTMCell layer with inputs X, H, C, W, R, B to Add, Split, MatMul, Multiply ops according to the formula: (.) - Denotes element-wise multiplication.Denotes dot product. f, g, h - are activation functions.


it = f(Xt*(Wi^T) + Ht-1*(Ri^T) + Wbi + Rbi) ft = f(Xt*(Wf^T) + Ht-1*(Rf^T) + Wbf + Rbf) ct = g(Xt*(Wc^T) + Ht-1*(Rc^T) + Wbc + Rbc) ot = f(Xt*(Wo^T) + Ht-1*(Ro^T) + Wbo + Rbo) Ct = ft (.) Ct-1 + it (.) ct Ht = ot (.) h(Ct)