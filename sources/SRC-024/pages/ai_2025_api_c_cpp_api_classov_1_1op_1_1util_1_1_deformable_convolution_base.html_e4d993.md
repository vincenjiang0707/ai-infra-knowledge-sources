source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1util_1_1_deformable_convolution_base.html
lastmod: 

# Class ov::op::util::DeformableConvolutionBase[#](https://docs.openvino.ai#class-ov-op-util-deformableconvolutionbase)

-
class DeformableConvolutionBase : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ConvolutionBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_convolution_base.html#_CPPv4N2ov2op4util15ConvolutionBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util25DeformableConvolutionBaseE) Base class for operations DeformableConvolution

[v1](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1op_1_1v1)and DeformableConvolution[v8](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1op_1_1v8).Subclassed by

[ov::op::v1::DeformableConvolution](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_deformable_convolution),[ov::op::v8::DeformableConvolution](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_deformable_convolution)Public Functions

-
DeformableConvolutionBase() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util25DeformableConvolutionBase25DeformableConvolutionBaseEv) Constructs a conversion operation.


-
DeformableConvolutionBase(const OutputVector &arguments, const
[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&strides, const[CoordinateDiff](https://docs.openvino.ai/classov_1_1_coordinate_diff.html#_CPPv4N2ov14CoordinateDiffE)&pads_begin, const[CoordinateDiff](https://docs.openvino.ai/classov_1_1_coordinate_diff.html#_CPPv4N2ov14CoordinateDiffE)&pads_end, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&dilations, const[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)&auto_pad =[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)::[EXPLICIT](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadType8EXPLICITE), int64_t group = 1, int64_t deformable_group = 1)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util25DeformableConvolutionBase25DeformableConvolutionBaseERK12OutputVectorRK7StridesRK14CoordinateDiffRK14CoordinateDiffRK7StridesRK7PadType7int64_t7int64_t) Constructs a conversion operation.

- Parameters:
**strides**– Convolution strides.**pads_begin**– Amount of padding to be added to the beginning along each axis. For example in case of a 2D input the value of (1, 2) means that 1 element will be added to the top and 2 elements to the left.**pads_end**– Amount of padding to be added to the end along each axis.**dilations**– The distance in width and height between the weights in the filters tensor.**auto_pad**– Specifies how the automatic calculation of padding should be done.**group**– The number of groups which both output and input should be split into.**deformable_group**– The number of groups which deformable values and output should be split into along the channel axis.



-
DeformableConvolutionBase() = default