source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v9_1_1_grid_sample.html
lastmod: 

# Class ov::op::v9::GridSample[#](https://docs.openvino.ai#class-ov-op-v9-gridsample)

-
class GridSample : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v910GridSampleE) Operator performing interpolated sampling of the input tensor.

Public Functions

-
GridSample(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &grid, const[Attributes](https://docs.openvino.ai/structov_1_1op_1_1v9_1_1_grid_sample_1_1_attributes.html#_CPPv4N2ov2op2v910GridSample10AttributesE)&attributes)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v910GridSample10GridSampleERK6OutputI4NodeERK6OutputI4NodeERK10Attributes) Constructs a

[GridSample](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v9_1_1_grid_sample)operation.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)data tensor (input image)**grid**– Normalized interpolation coordinates**attrs**–[GridSample](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v9_1_1_grid_sample)attributes



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v910GridSample24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v910GridSample12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
struct Attributes
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v910GridSample10AttributesE) A Structure which contains all

[GridSample](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v9_1_1_grid_sample)attributes.

-
GridSample(const