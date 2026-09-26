source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_mark_floating_point_range.html
lastmod: 

# Class ov::pass::MarkFloatingPointRange[#](https://docs.openvino.ai#class-ov-pass-markfloatingpointrange)

-
class MarkFloatingPointRange : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass22MarkFloatingPointRangeE) This transformation markups the marks paths that involve Range operations with floating point output data types, as well as their users allowed for propagation. This pass is needed to prevent accuracy data loss in cases of high range generation, which could suffer due to lowered precision.