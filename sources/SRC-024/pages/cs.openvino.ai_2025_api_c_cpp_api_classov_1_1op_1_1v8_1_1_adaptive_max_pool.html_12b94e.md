source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v8_1_1_adaptive_max_pool.html
lastmod: 

# Class ov::op::v8::AdaptiveMaxPool[#](https://docs.openvino.ai#class-ov-op-v8-adaptivemaxpool)

-
class AdaptiveMaxPool : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v815AdaptiveMaxPoolE) Adaptive max pooling operation.

Public Functions

-
AdaptiveMaxPool(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &output_shape, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&index_element_type =[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i64](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i64EN6Type_t3i64E))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v815AdaptiveMaxPool15AdaptiveMaxPoolERK6OutputI4NodeERK6OutputI4NodeERKN2ov7element4TypeE) Constructs adaptive max pooling operation.

- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)data**output_shape**– 1D tensor describing output shape for spatial dimensions.**index_element_type**– Specifies the output tensor type for indices output



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v815AdaptiveMaxPool24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
AdaptiveMaxPool(const