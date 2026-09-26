source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_einsum_decomposition.html
lastmod: 

# Class ov::pass::EinsumDecomposition[#](https://docs.openvino.ai#class-ov-pass-einsumdecomposition)

-
class EinsumDecomposition : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass19EinsumDecompositionE) [EinsumDecomposition](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_einsum_decomposition)transformation decomposes Einsum-7 operation into a sub-graph with more simple operations: Transpose, Reshape, MatMul, ReduceSum, Unsqueeze, ShapeOf, ReduceProd, StridedSlice, and Concat.