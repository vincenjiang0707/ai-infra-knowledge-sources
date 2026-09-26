source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1util_1_1_convolution_fwd_prop_base.html
lastmod: 

# Class ov::op::util::ConvolutionFwdPropBase[#](https://docs.openvino.ai#class-ov-op-util-convolutionfwdpropbase)

-
class ConvolutionFwdPropBase : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ConvolutionBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_convolution_base.html#_CPPv4N2ov2op4util15ConvolutionBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util22ConvolutionFwdPropBaseE) Base class for operations like back propagation convolution.

Subclassed by

[ov::op::v1::BinaryConvolution](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_binary_convolution),[ov::op::v1::Convolution](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_convolution),[ov::op::v1::GroupConvolution](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_group_convolution)Public Functions

-
ConvolutionFwdPropBase() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util22ConvolutionFwdPropBase22ConvolutionFwdPropBaseEv) Constructs a conversion operation.


-
inline ConvolutionFwdPropBase(const OutputVector &arguments, const
[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&strides, const[CoordinateDiff](https://docs.openvino.ai/classov_1_1_coordinate_diff.html#_CPPv4N2ov14CoordinateDiffE)&pads_begin, const[CoordinateDiff](https://docs.openvino.ai/classov_1_1_coordinate_diff.html#_CPPv4N2ov14CoordinateDiffE)&pads_end, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&dilations, const[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)&auto_pad =[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)::[EXPLICIT](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadType8EXPLICITE))[#](https://docs.openvino.ai#_CPPv4N2ov2op4util22ConvolutionFwdPropBase22ConvolutionFwdPropBaseERK12OutputVectorRK7StridesRK14CoordinateDiffRK14CoordinateDiffRK7StridesRK7PadType) Constructs a conversion operation.

- Parameters:
**strides**– Convolution strides.**pads_begin**– Amount of padding to be added to the beginning along each axis. For example in case of a 2D input the value of (1, 2) means that 1 element will be added to the top and 2 elements to the left.**pads_end**– Amount of padding to be added to the end along each axis.**dilations**– The distance in width and height between the weights in the filters tensor.**auto_pad**– Specifies how the automatic calculation of padding should be done.



-
ConvolutionFwdPropBase() = default