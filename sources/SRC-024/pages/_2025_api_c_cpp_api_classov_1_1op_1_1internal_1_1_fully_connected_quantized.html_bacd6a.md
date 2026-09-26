source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1internal_1_1_fully_connected_quantized.html
lastmod: 

# Class ov::op::internal::FullyConnectedQuantized[#](https://docs.openvino.ai#class-ov-op-internal-fullyconnectedquantized)

-
class FullyConnectedQuantized : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[internal](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op8internalE)::[FullyConnected](https://docs.openvino.ai/classov_1_1op_1_1internal_1_1_fully_connected.html#_CPPv4N2ov2op8internal14FullyConnectedE)[#](https://docs.openvino.ai#_CPPv4N2ov2op8internal23FullyConnectedQuantizedE) Public Functions

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op8internal23FullyConnectedQuantized24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual void validate_and_infer_types() override