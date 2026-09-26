source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v1_1_1_binary_convolution.html
lastmod: 

# Class ov::op::v1::BinaryConvolution[#](https://docs.openvino.ai#class-ov-op-v1-binaryconvolution)

-
class BinaryConvolution : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ConvolutionFwdPropBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_convolution_fwd_prop_base.html#_CPPv4N2ov2op4util22ConvolutionFwdPropBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v117BinaryConvolutionE) [BinaryConvolution](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_binary_convolution)operation.Public Functions

-
BinaryConvolution() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v117BinaryConvolution17BinaryConvolutionEv) Constructs a binary convolution operation.


-
BinaryConvolution(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &kernel, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&strides, const[CoordinateDiff](https://docs.openvino.ai/classov_1_1_coordinate_diff.html#_CPPv4N2ov14CoordinateDiffE)&pads_begin, const[CoordinateDiff](https://docs.openvino.ai/classov_1_1_coordinate_diff.html#_CPPv4N2ov14CoordinateDiffE)&pads_end, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&dilations, BinaryConvolutionMode mode, float pad_value, const[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)&auto_pad =[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)::[EXPLICIT](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadType8EXPLICITE))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v117BinaryConvolution17BinaryConvolutionERK6OutputI4NodeERK6OutputI4NodeERK7StridesRK14CoordinateDiffRK14CoordinateDiffRK7Strides21BinaryConvolutionModefRK7PadType) Constructs a binary convolution operation.

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)`[N, C_OUT, R1, ... Rf]`

- Parameters:
**data**– The node producing the input data batch tensor.**kernel**– The node producing the filters tensor.**strides**– The strides.**pads_begin**– The beginning of padding shape.**pads_end**– The end of padding shape.**dilations**– The dilations.**mode**– Defines how input tensor 0/1 values and weights 0/1 are interpreted.**pad_value**– Floating-point value used to fill pad area.**auto_pad**– The pad type for automatically computing padding sizes.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v117BinaryConvolution24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline const BinaryConvolutionMode &get_mode() const
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v117BinaryConvolution8get_modeEv) - Returns:
The mode of convolution.



-
inline float get_pad_value() const
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v117BinaryConvolution13get_pad_valueEv) - Returns:
The pad value.



-
BinaryConvolution() = default