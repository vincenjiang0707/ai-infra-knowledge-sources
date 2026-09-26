source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v8_1_1_deformable_convolution.html
lastmod: 

# Class ov::op::v8::DeformableConvolution[#](https://docs.openvino.ai#class-ov-op-v8-deformableconvolution)

-
class DeformableConvolution : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[DeformableConvolutionBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_deformable_convolution_base.html#_CPPv4N2ov2op4util25DeformableConvolutionBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v821DeformableConvolutionE) [DeformableConvolution](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_deformable_convolution)operation.Public Functions

-
DeformableConvolution() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v821DeformableConvolution21DeformableConvolutionEv) Constructs a conversion operation.


-
DeformableConvolution(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &offsets, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &filters, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&strides, const[CoordinateDiff](https://docs.openvino.ai/classov_1_1_coordinate_diff.html#_CPPv4N2ov14CoordinateDiffE)&pads_begin, const[CoordinateDiff](https://docs.openvino.ai/classov_1_1_coordinate_diff.html#_CPPv4N2ov14CoordinateDiffE)&pads_end, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&dilations, const[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)&auto_pad =[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)::[EXPLICIT](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadType8EXPLICITE), const int64_t group = 1, const int64_t deformable_group = 1, const bool bilinear_interpolation_pad = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v821DeformableConvolution21DeformableConvolutionERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK7StridesRK14CoordinateDiffRK14CoordinateDiffRK7StridesRK7PadTypeK7int64_tK7int64_tKb) Constructs a conversion operation.

- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.**offsets**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the deformable values tensor.**filters**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the filters(kernels) tensor with OIZYX layout.**strides**– Convolution strides.**pads_begin**– Amount of padding to be added to the beginning along each axis. For example in case of a 2D input the value of (1, 2) means that 1 element will be added to the top and 2 elements to the left.**pads_end**– Amount of padding to be added to the end along each axis.**dilations**– The distance in width and height between the weights in the filters tensor.**auto_pad**– Specifies how the automatic calculation of padding should be done.**group**– The number of groups which both output and input should be split into.**deformable_group**– The number of groups which deformable values and output should be split into along the channel axis.**bilinear_interpolation_pad**– The flag that determines the mode of bilinear interpolation execution.[If](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_if)the flag is`true`

and the sampling location is within one pixel outside of the feature map boundary, then bilinear interpolation is performed on the zero padded feature map.[If](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_if)the flag is`false`

and the sampling location is within one pixel outside of the feature map boundary, then the sampling location shifts to the inner boundary of the feature map.`



-
DeformableConvolution(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &offsets, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &filters, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &mask, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&strides, const[CoordinateDiff](https://docs.openvino.ai/classov_1_1_coordinate_diff.html#_CPPv4N2ov14CoordinateDiffE)&pads_begin, const[CoordinateDiff](https://docs.openvino.ai/classov_1_1_coordinate_diff.html#_CPPv4N2ov14CoordinateDiffE)&pads_end, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&dilations, const[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)&auto_pad =[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)::[EXPLICIT](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadType8EXPLICITE), const int64_t group = 1, const int64_t deformable_group = 1, const bool bilinear_interpolation_pad = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v821DeformableConvolution21DeformableConvolutionERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK7StridesRK14CoordinateDiffRK14CoordinateDiffRK7StridesRK7PadTypeK7int64_tK7int64_tKb) Constructs a conversion operation.

- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.**offsets**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the deformable values tensor.**filters**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the filters(kernels) tensor with OIZYX layout.**mask**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the mask(mask) tensor.**strides**– Convolution strides.**pads_begin**– Amount of padding to be added to the beginning along each axis. For example in case of a 2D input the value of (1, 2) means that 1 element will be added to the top and 2 elements to the left.**pads_end**– Amount of padding to be added to the end along each axis.**dilations**– The distance in width and height between the weights in the filters tensor.**auto_pad**– Specifies how the automatic calculation of padding should be done.**group**– The number of groups which both output and input should be split into.**deformable_group**– The number of groups which deformable values and output should be split into along the channel axis.**bilinear_interpolation_pad**– The flag that determines the mode of bilinear interpolation execution.[If](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_if)the flag is`true`

and the sampling location is within one pixel outside of the feature map boundary, then bilinear interpolation is performed on the zero padded feature map.[If](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_if)the flag is`false`

and the sampling location is within one pixel outside of the feature map boundary, then the sampling location shifts to the inner boundary of the feature map.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v821DeformableConvolution24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
DeformableConvolution() = default