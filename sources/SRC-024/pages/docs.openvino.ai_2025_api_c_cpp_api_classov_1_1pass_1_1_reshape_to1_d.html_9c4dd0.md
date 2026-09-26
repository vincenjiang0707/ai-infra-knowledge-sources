source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_reshape_to1_d.html
lastmod: 

# Class ov::pass::ReshapeTo1D[#](https://docs.openvino.ai#class-ov-pass-reshapeto1d)

-
class ReshapeTo1D : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass11ReshapeTo1DE) [ReshapeTo1D](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_reshape_to1_d)transformation looks for Reshape from nD to 1D tensor and replaces its pattern to [-1].

Site Navigation

Section Navigation

[ReshapeTo1D](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_reshape_to1_d) transformation looks for Reshape from nD to 1D tensor and replaces its pattern to [-1].