source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1internal_1_1_ro_p_e.html
lastmod: 

# Class ov::op::internal::RoPE[#](https://docs.openvino.ai#class-ov-op-internal-rope)

-
class RoPE : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op8internal4RoPEE) Rotary Positional Embeddings operation Internal operation which may change in the future.

Public Functions

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op8internal4RoPE24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
struct Config
[#](https://docs.openvino.ai#_CPPv4N2ov2op8internal4RoPE6ConfigE)

-
virtual void validate_and_infer_types() override