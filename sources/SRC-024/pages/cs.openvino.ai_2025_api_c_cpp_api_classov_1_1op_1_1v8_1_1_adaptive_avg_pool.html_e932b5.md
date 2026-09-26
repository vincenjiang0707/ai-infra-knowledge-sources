source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v8_1_1_adaptive_avg_pool.html
lastmod: 

# Class ov::op::v8::AdaptiveAvgPool[#](https://docs.openvino.ai#class-ov-op-v8-adaptiveavgpool)

-
class AdaptiveAvgPool : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v815AdaptiveAvgPoolE) Adaptive average pooling operation.

Public Functions

-
AdaptiveAvgPool(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &output_shape)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v815AdaptiveAvgPool15AdaptiveAvgPoolERK6OutputI4NodeERK6OutputI4NodeE) Constructs adaptive average pooling operation.

- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)data**output_shape**– 1D tensor describing output shape for spatial dimensions.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v815AdaptiveAvgPool24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
AdaptiveAvgPool(const