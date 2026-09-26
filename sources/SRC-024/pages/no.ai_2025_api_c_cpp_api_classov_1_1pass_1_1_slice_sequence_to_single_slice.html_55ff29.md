source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_slice_sequence_to_single_slice.html
lastmod: 

# Class ov::pass::SliceSequenceToSingleSlice[#](https://docs.openvino.ai#class-ov-pass-slicesequencetosingleslice)

-
class SliceSequenceToSingleSlice : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass26SliceSequenceToSingleSliceE) [SliceSequenceToSingleSlice](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_slice_sequence_to_single_slice)transformation replaces group of Slice operations with single Slice. All Slice operations must slice data with the different axis.Before: data (shape: 2, 3, 4) -> Slice (axis 0) -> Slice (axis 1) -> Slice (axis 2)

After: data (shape: 2, 3, 4) -> Slice (axes: 0, 1, 2)