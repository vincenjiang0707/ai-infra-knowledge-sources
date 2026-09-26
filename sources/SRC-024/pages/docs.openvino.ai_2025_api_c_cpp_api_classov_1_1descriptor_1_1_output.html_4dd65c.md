source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1descriptor_1_1_output.html
lastmod: 

# Class ov::descriptor::Output[#](https://docs.openvino.ai#class-ov-descriptor-output)

-
class Output
[#](https://docs.openvino.ai#_CPPv4N2ov10descriptor6OutputE) Public Functions

- Parameters:
**node**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that owns this output.**index**– Position of the output tensor in all output tensors**tensor**– The tensor where the value will be written



-
inline
[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)*get_raw_pointer_node() const[#](https://docs.openvino.ai#_CPPv4NK2ov10descriptor6Output20get_raw_pointer_nodeEv) - Returns:
the raw pointer to the node that this is an output of



-
const
[PartialShape](https://docs.openvino.ai/classov_1_1_partial_shape.html#_CPPv4N2ov12PartialShapeE)&get_partial_shape() const[#](https://docs.openvino.ai#_CPPv4NK2ov10descriptor6Output17get_partial_shapeEv) - Returns:
the partial shape of the output