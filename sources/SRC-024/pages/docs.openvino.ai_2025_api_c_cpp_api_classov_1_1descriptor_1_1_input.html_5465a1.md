source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1descriptor_1_1_input.html
lastmod: 

# Class ov::descriptor::Input[#](https://docs.openvino.ai#class-ov-descriptor-input)

-
class Input
[#](https://docs.openvino.ai#_CPPv4N2ov10descriptor5InputE) Public Functions

-
Input(
[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)*node, size_t index,[Output](https://docs.openvino.ai/classov_1_1descriptor_1_1_output.html#_CPPv4N2ov10descriptor6OutputE)&output)[#](https://docs.openvino.ai#_CPPv4N2ov10descriptor5Input5InputEP4Node6size_tR6Output) - Parameters:
**node**– The node that owns this input**index**– The position of this tensor in all input tensors**output**– The output that supplies a value for this input



-
Input(
[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)*node, size_t index)[#](https://docs.openvino.ai#_CPPv4N2ov10descriptor5Input5InputEP4Node6size_t) Create an

[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1descriptor_1_1_input)that is not connected to an output.- Parameters:
**node**– The node that owns this input**index**– The position of this tensor in all input tensors



-
inline
[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)*get_raw_pointer_node() const[#](https://docs.openvino.ai#_CPPv4NK2ov10descriptor5Input20get_raw_pointer_nodeEv) - Returns:
the raw pointer to the node that this is an input of



-
inline size_t get_index() const
[#](https://docs.openvino.ai#_CPPv4NK2ov10descriptor5Input9get_indexEv) - Returns:
the position within all supplied tensors of this input



-
inline bool has_output() const
[#](https://docs.openvino.ai#_CPPv4NK2ov10descriptor5Input10has_outputEv) - Returns:
true if an output is connected to the input.



Replace the current output that supplies a value for this input with output i of node.


-
void replace_output(
[Output](https://docs.openvino.ai/classov_1_1descriptor_1_1_output.html#_CPPv4N2ov10descriptor6OutputE)&output)[#](https://docs.openvino.ai#_CPPv4N2ov10descriptor5Input14replace_outputER6Output) Replace the current output that supplies a value for this input with output.


-
void remove_output()
[#](https://docs.openvino.ai#_CPPv4N2ov10descriptor5Input13remove_outputEv) Remove the output from this input. The node will not be valid until another output is supplied.


-
inline bool get_is_relevant_to_shape() const
[#](https://docs.openvino.ai#_CPPv4NK2ov10descriptor5Input24get_is_relevant_to_shapeEv) See Node::set_input_is_relevant_to_shape for more details.

- Returns:
true if the value of this input is relevant to the output shapes of the corresponding node. (Usually this is false.)



-
inline bool get_is_relevant_to_value() const
[#](https://docs.openvino.ai#_CPPv4NK2ov10descriptor5Input24get_is_relevant_to_valueEv) See Node::set_input_is_relevant_to_value for more details.

- Returns:
true if the value of this input is relevant to the output value of the corresponding node. (Usually this is true.)



-
const
[PartialShape](https://docs.openvino.ai/classov_1_1_partial_shape.html#_CPPv4N2ov12PartialShapeE)&get_partial_shape() const[#](https://docs.openvino.ai#_CPPv4NK2ov10descriptor5Input17get_partial_shapeEv) - Returns:
the partial shape of the connected output



-
Input(