source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1internal_1_1_fully_connected.html
lastmod: 

# Class ov::op::internal::FullyConnected[#](https://docs.openvino.ai#class-ov-op-internal-fullyconnected)

-
class FullyConnected : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op8internal14FullyConnectedE) Subclassed by

[ov::op::internal::FullyConnectedCompressed](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1internal_1_1_fully_connected_compressed),[ov::op::internal::FullyConnectedQuantized](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1internal_1_1_fully_connected_quantized),[ov::op::internal::FullyConnectedQuantizedLegacy](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1internal_1_1_fully_connected_quantized_legacy)Public Functions

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op8internal14FullyConnected24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual void validate_and_infer_types() override