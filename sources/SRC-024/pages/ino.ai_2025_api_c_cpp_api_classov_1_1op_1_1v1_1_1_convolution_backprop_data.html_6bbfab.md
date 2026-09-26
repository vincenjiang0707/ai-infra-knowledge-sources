source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v1_1_1_convolution_backprop_data.html
lastmod: 

# Class ov::op::v1::ConvolutionBackpropData[#](https://docs.openvino.ai#class-ov-op-v1-convolutionbackpropdata)

-
class ConvolutionBackpropData : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ConvolutionBackPropBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_convolution_back_prop_base.html#_CPPv4N2ov2op4util23ConvolutionBackPropBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v123ConvolutionBackpropDataE) Data batch backprop for batched convolution operation.

Public Functions

-
ConvolutionBackpropData() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v123ConvolutionBackpropData23ConvolutionBackpropDataEv) Constructs a batched-convolution data batch-backprop operation.


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v123ConvolutionBackpropData24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
const
[PartialShape](https://docs.openvino.ai/classov_1_1_partial_shape.html#_CPPv4N2ov12PartialShapeE)get_output_shape() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v123ConvolutionBackpropData16get_output_shapeEv) - Returns:
The output spatial dimensions shape.



-
ConvolutionBackpropData() = default