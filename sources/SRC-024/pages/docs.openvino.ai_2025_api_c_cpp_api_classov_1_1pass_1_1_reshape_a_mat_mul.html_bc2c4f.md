source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_reshape_a_mat_mul.html
lastmod: 

# Class ov::pass::ReshapeAMatMul[#](https://docs.openvino.ai#class-ov-pass-reshapeamatmul)

-
class ReshapeAMatMul : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass14ReshapeAMatMulE) [ReshapeAMatMul](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_reshape_a_mat_mul)and[ReshapeBMatMul](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_reshape_b_mat_mul)transformations relax hard-coded Reshape followed by MatMul operation For 2D Reshape search patterns are:MatMul(Reshape(any_input, any_input), any_input)

MatMul(any_input, Reshape(any_input, any_input))