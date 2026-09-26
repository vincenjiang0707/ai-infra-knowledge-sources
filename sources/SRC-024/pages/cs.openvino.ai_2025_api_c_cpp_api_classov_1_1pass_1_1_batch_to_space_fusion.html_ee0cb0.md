source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_batch_to_space_fusion.html
lastmod: 

# Class ov::pass::BatchToSpaceFusion[#](https://docs.openvino.ai#class-ov-pass-batchtospacefusion)

-
class BatchToSpaceFusion : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass18BatchToSpaceFusionE) [BatchToSpaceFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_batch_to_space_fusion)transformation replaces following graph: Transpose (or Reshape) -> DepthToSpace -> StridedSlice -> Transpose (or Reshape) to BatchToSpace Restrictions:input rank must be 4

Transpose permutation must be [1, 0, 2, 3]

DepthToSpaceMode must be BLOCKS_FIRST