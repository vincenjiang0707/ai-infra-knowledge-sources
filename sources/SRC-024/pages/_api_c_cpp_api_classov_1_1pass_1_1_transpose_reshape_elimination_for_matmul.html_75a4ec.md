source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_transpose_reshape_elimination_for_matmul.html
lastmod: 

# Class ov::pass::TransposeReshapeEliminationForMatmul[#](https://docs.openvino.ai#class-ov-pass-transposereshapeeliminationformatmul)

-
class TransposeReshapeEliminationForMatmul : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass36TransposeReshapeEliminationForMatmulE) [TransposeReshapeEliminationForMatmul](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_transpose_reshape_elimination_for_matmul)transformation eliminates Transpose and Reshape which were created to align input and output dimension ranks before second MatMul input and after MatMul output (for example, after Einsum Decomposition inside TensorFlow 1 and OpenVINO[EinsumDecomposition](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_einsum_decomposition)transformation)