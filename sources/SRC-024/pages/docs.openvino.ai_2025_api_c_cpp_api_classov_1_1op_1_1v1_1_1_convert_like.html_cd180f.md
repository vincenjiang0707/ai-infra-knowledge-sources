source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v1_1_1_convert_like.html
lastmod: 

# Class ov::op::v1::ConvertLike[#](https://docs.openvino.ai#class-ov-op-v1-convertlike)

-
class ConvertLike : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v111ConvertLikeE) Elementwise type conversion operation.

Public Functions

-
ConvertLike() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v111ConvertLike11ConvertLikeEv) Constructs a conversion operation.


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v111ConvertLike24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
ConvertLike() = default