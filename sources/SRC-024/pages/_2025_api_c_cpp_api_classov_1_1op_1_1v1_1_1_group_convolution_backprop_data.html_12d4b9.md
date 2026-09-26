source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v1_1_1_group_convolution_backprop_data.html
lastmod: 

# Class ov::op::v1::GroupConvolutionBackpropData[#](https://docs.openvino.ai#class-ov-op-v1-groupconvolutionbackpropdata)

-
class GroupConvolutionBackpropData : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ConvolutionBackPropBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_convolution_back_prop_base.html#_CPPv4N2ov2op4util23ConvolutionBackPropBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v128GroupConvolutionBackpropDataE) Data batch backprop for batched convolution operation.

Public Functions

-
GroupConvolutionBackpropData()
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v128GroupConvolutionBackpropData28GroupConvolutionBackpropDataEv) Constructs a batched-convolution data batch-backprop operation.


-
void infer_conv_backprop_output_spatial_shape(const std::vector<
[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)> &input_data_shape, const std::vector<[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)> &filters_shape, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&strides, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&dilations, const[CoordinateDiff](https://docs.openvino.ai/classov_1_1_coordinate_diff.html#_CPPv4N2ov14CoordinateDiffE)&pads_begin, const[CoordinateDiff](https://docs.openvino.ai/classov_1_1_coordinate_diff.html#_CPPv4N2ov14CoordinateDiffE)&pads_end, const[CoordinateDiff](https://docs.openvino.ai/classov_1_1_coordinate_diff.html#_CPPv4N2ov14CoordinateDiffE)&output_padding, std::vector<[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)> &output_spatial_shape)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v128GroupConvolutionBackpropData40infer_conv_backprop_output_spatial_shapeERKNSt6vectorI9DimensionEERKNSt6vectorI9DimensionEERK7StridesRK7StridesRK14CoordinateDiffRK14CoordinateDiffRK14CoordinateDiffRNSt6vectorI9DimensionEE) Calculates output spatial features size.

- Parameters:
**input_data_shape**–**[in]**The input data partial shape**filters_shape**–**[in]**The filters partial shape**strides**–**[in]**The strides values.**dilations**–**[in]**The dilations values.**pads_begin**–**[in]**The paddings at the beginning of axis.**pads_end**–**[in]**The paddings at the end of axis.**output_padding**–**[in]**The output padding values.**output_spatial_shape**– The placeholder for computed output spatial partial shape.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v128GroupConvolutionBackpropData24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
const
[PartialShape](https://docs.openvino.ai/classov_1_1_partial_shape.html#_CPPv4N2ov12PartialShapeE)get_convolution_output_shape() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v128GroupConvolutionBackpropData28get_convolution_output_shapeEv) - Returns:
The spatial shape of the output.



-
GroupConvolutionBackpropData()