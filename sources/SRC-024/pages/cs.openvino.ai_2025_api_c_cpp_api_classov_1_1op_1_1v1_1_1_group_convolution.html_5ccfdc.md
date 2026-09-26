source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v1_1_1_group_convolution.html
lastmod: 

# Class ov::op::v1::GroupConvolution[#](https://docs.openvino.ai#class-ov-op-v1-groupconvolution)

-
class GroupConvolution : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ConvolutionFwdPropBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_convolution_fwd_prop_base.html#_CPPv4N2ov2op4util22ConvolutionFwdPropBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v116GroupConvolutionE) Batched convolution operation, with optional window dilation and stride.

Public Functions

-
GroupConvolution() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v116GroupConvolution16GroupConvolutionEv) Constructs a batched convolution operation.


-
GroupConvolution(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data_batch, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &filters, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&strides, const[CoordinateDiff](https://docs.openvino.ai/classov_1_1_coordinate_diff.html#_CPPv4N2ov14CoordinateDiffE)&pads_begin, const[CoordinateDiff](https://docs.openvino.ai/classov_1_1_coordinate_diff.html#_CPPv4N2ov14CoordinateDiffE)&pads_end, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&dilations, const[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)&auto_pad =[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)::[EXPLICIT](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadType8EXPLICITE))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v116GroupConvolution16GroupConvolutionERK6OutputI4NodeERK6OutputI4NodeERK7StridesRK14CoordinateDiffRK14CoordinateDiffRK7StridesRK7PadType) Constructs a batched convolution operation.

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)`[N, FC_OUT * GROUPS, R1, ... Rf]`

- Parameters:
**data_batch**– The node producing the input data batch tensor.`[N, C_IN, D1, ... Df]`

**filters**– The node producing the filters tensor.`[GROUPS, FC_OUT, FC_IN, F1, ... Ff]`

**strides**– The strides.`[f]`

**dilations**– The dilations.`[f]`

**pads_begin**– The beginning of padding shape.`[f]`

**pads_end**– The end of padding shape.`[f]`

**auto_pad**– The pad type for automatically computing padding sizes.`[f]`




-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v116GroupConvolution24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
GroupConvolution() = default