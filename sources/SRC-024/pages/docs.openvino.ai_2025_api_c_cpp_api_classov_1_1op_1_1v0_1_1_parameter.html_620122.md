source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_parameter.html
lastmod: 

# Class ov::op::v0::Parameter[#](https://docs.openvino.ai#class-ov-op-v0-parameter)

-
class Parameter : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v09ParameterE) A model parameter.

Parameters are nodes that represent the arguments that will be passed to user-defined models.

[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)creation requires a sequence of parameters. Basic graph operations do not need parameters attached to a model.Public Functions

-
Parameter() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v09Parameter9ParameterEv) Constructions a tensor-typed parameter node.


-
Parameter(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&element_type, const[PartialShape](https://docs.openvino.ai/classov_1_1_partial_shape.html#_CPPv4N2ov12PartialShapeE)&pshape)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v09Parameter9ParameterERKN2ov7element4TypeERK12PartialShape) Constructions a tensor-typed parameter node.

- Parameters:
**element_type**– The element type of the parameter.**pshape**– The partial shape of the parameter.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v09Parameter24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
Parameter() = default