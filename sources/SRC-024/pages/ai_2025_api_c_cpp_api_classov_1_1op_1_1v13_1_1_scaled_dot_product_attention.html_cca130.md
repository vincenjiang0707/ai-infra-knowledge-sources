source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v13_1_1_scaled_dot_product_attention.html
lastmod: 

# Class ov::op::v13::ScaledDotProductAttention[#](https://docs.openvino.ai#class-ov-op-v13-scaleddotproductattention)

-
class ScaledDotProductAttention : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1325ScaledDotProductAttentionE) Scaled dot product attention operation from PyTorch.

Public Functions

-
ScaledDotProductAttention() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1325ScaledDotProductAttention25ScaledDotProductAttentionEv) Constructs a

[ScaledDotProductAttention](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v13_1_1_scaled_dot_product_attention)operation.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1325ScaledDotProductAttention24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
ScaledDotProductAttention() = default