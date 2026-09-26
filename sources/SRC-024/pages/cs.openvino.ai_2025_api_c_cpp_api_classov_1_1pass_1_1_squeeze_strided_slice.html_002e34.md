source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_squeeze_strided_slice.html
lastmod: 

# Class ov::pass::SqueezeStridedSlice[#](https://docs.openvino.ai#class-ov-pass-squeezestridedslice)

-
class SqueezeStridedSlice : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass19SqueezeStridedSliceE) [StridedSliceSqueeze](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_strided_slice_squeeze)transformation looks for Squeeze -> SSe and corrects SS inputs and attributes for SS output to be squeeze-able.

Site Navigation

Section Navigation

[StridedSliceSqueeze](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_strided_slice_squeeze) transformation looks for Squeeze -> SSe and corrects SS inputs and attributes for SS output to be squeeze-able.