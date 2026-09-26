source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_dilated_convolution_converter.html
lastmod: 

# Class ov::pass::DilatedConvolutionConverter[#](https://docs.openvino.ai#class-ov-pass-dilatedconvolutionconverter)

-
class DilatedConvolutionConverter : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass27DilatedConvolutionConverterE) [DilatedConvolutionConverter](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_dilated_convolution_converter)transformation replaces following graph: SpaceToBatch -> Convolution(GroupConvolution) -> BatchToSpace to a single Convolution(GroupConvolution) node with updated pads and dilations Restrictions:pads in SpaceToBatch must have 0 on first and second position