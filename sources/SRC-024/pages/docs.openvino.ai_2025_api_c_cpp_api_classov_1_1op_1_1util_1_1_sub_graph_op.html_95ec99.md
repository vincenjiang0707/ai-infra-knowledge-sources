source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1util_1_1_sub_graph_op.html
lastmod: 

# Class ov::op::util::SubGraphOp[#](https://docs.openvino.ai#class-ov-op-util-subgraphop)

-
class SubGraphOp : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[MultiSubGraphOp](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_multi_sub_graph_op.html#_CPPv4N2ov2op4util15MultiSubGraphOpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util10SubGraphOpE) Abstract base class for sub-graph based ops, i.e ops that have only one sub-graph.

Subclassed by

[ov::op::internal::LoraSubgraph](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1internal_1_1_lora_subgraph),[ov::op::v0::TensorIterator](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_tensor_iterator),[ov::op::v5::Loop](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v5_1_1_loop)Public Functions

-
inline const std::vector<std::shared_ptr<InputDescription>> &get_input_descriptions() const
[#](https://docs.openvino.ai#_CPPv4NK2ov2op4util10SubGraphOp22get_input_descriptionsEv) - Returns:
a reference to the input descriptions.



-
inline std::vector<std::shared_ptr<InputDescription>> &get_input_descriptions()
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util10SubGraphOp22get_input_descriptionsEv) - Returns:
a reference to the input descriptions. Can add input descriptions before validation.



-
inline const std::vector<std::shared_ptr<OutputDescription>> &get_output_descriptions() const
[#](https://docs.openvino.ai#_CPPv4NK2ov2op4util10SubGraphOp23get_output_descriptionsEv) - Returns:
a reference to the output descriptions.



-
inline std::vector<std::shared_ptr<OutputDescription>> &get_output_descriptions()
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util10SubGraphOp23get_output_descriptionsEv) - Returns:
a reference to the output descriptions. Can add output descriptions before validation.



Indicate that a body parameter comes from slices of a value.

- Parameters:
**parameter**– The parameter to receive the slices**value**– The value to be sliced. This will be added as an input to[SubGraphOp](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_sub_graph_op).**start**– First index on axis of the slicing**stride**– Stepping of the slice**part_size**– Size of the slice on axis**end**– The last index on axis of the slicing**axis**– The axis to slice along



Indicates that a body parameter has an initial value in the first iteration and computed value thereafter.

- Parameters:
**body_parameter**–**[in]**The body parameter**initial_value**– Value for the parameter in first iteration. This will be added as an input to Loop.**successive_value**– Value for the parameter in successive iterations. The value is what is active in the most recent completed iteration.



Indicates that a body parameter has an invariant value during iteration that may depend on values computed outside of the iteration.

- Parameters:
**body_parameter**– The body parameter**value**– The value supplied as an input to the block



-
virtual
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> get_iter_value(const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &body_value, int64_t iteration = -1)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util10SubGraphOp14get_iter_valueERK6OutputI4NodeE7int64_t) Gets a value for a particular iteration point.

- Parameters:
**body_value**– The value**iteration**– The iteration that supplies the value. Negative values are from the last iteration. Default value -1 (the last iteration).

- Returns:
The iterator value.



-
virtual
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> get_concatenated_slices(const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &value, int64_t start, int64_t stride, int64_t part_size, int64_t end, int64_t axis)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util10SubGraphOp23get_concatenated_slicesERK6OutputI4NodeE7int64_t7int64_t7int64_t7int64_t7int64_t) Concatenates slices from all iterations.

- Parameters:
**value**– The value supplying slice values from each iteration.**start**– First index on axis of the slicing**stride**– Stepping of the slice**part_size**– Size of the slice on axis**end**– The last index on axis of the slicing**axis**– The axis to slice along

- Returns:
The concatenated slices.



-
inline const std::vector<std::shared_ptr<InputDescription>> &get_input_descriptions() const