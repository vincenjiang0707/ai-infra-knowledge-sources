source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_prepare_shape_ops_for_elimination_around_b_e.html
lastmod: 

# Class ov::pass::PrepareShapeOpsForEliminationAroundBE[#](https://docs.openvino.ai#class-ov-pass-prepareshapeopsforeliminationaroundbe)

-
class PrepareShapeOpsForEliminationAroundBE : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass37PrepareShapeOpsForEliminationAroundBEE) [PrepareShapeOpsForEliminationAroundBE](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_prepare_shape_ops_for_elimination_around_b_e)works on the subgraph like Reshape/Squeeze/Unsqueeze -> BinaryElementwiseOperation -> Reshape/Squeeze/Unsqueeze and prepares it for the following optimizations by moving bottom op up through Binary op.