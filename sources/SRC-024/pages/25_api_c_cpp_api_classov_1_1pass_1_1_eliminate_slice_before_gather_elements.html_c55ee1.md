source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_eliminate_slice_before_gather_elements.html
lastmod: 

# Class ov::pass::EliminateSliceBeforeGatherElements[#](https://docs.openvino.ai#class-ov-pass-eliminateslicebeforegatherelements)

-
class EliminateSliceBeforeGatherElements : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass34EliminateSliceBeforeGatherElementsE) [EliminateSliceBeforeGatherElements](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_eliminate_slice_before_gather_elements)eliminates slice before GElements if slicing from 0 It is valid since GatherElements doesn’t support negative indices and Slice won’t affect indexing of elements in the original tensor that GatherElements would like to take.