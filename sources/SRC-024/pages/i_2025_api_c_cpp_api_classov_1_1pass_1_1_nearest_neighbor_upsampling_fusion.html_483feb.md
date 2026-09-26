source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_nearest_neighbor_upsampling_fusion.html
lastmod: 

# Class ov::pass::NearestNeighborUpsamplingFusion[#](https://docs.openvino.ai#class-ov-pass-nearestneighborupsamplingfusion)

-
class NearestNeighborUpsamplingFusion : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass31NearestNeighborUpsamplingFusionE) [NearestNeighborUpsamplingFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_nearest_neighbor_upsampling_fusion)transformation fuses subgraph that uses the simpler operations, as ShapeOf, StridedSlice, Concat, Reshape, Mul to calculate Interpolate with mode=’nearest’.