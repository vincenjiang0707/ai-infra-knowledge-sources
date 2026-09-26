source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1util_1_1_multi_sub_graph_op.html
lastmod: 

# Class ov::op::util::MultiSubGraphOp[#](https://docs.openvino.ai#class-ov-op-util-multisubgraphop)

-
class MultiSubGraphOp : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Sink](https://docs.openvino.ai/classov_1_1op_1_1_sink.html#_CPPv4N2ov2op4SinkE)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15MultiSubGraphOpE) Abstract base class for sub-graph based ops, i.e ops that have some sub-graphs.

Subclassed by

[ov::op::util::FrameworkNode](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_framework_node),[ov::op::util::SubGraphOp](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_sub_graph_op),[ov::op::v8::If](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_if)Public Functions

-
inline virtual const std::shared_ptr<
[Model](https://docs.openvino.ai/classov_1_1_model.html#_CPPv4N2ov5ModelE)> &get_function(size_t index) const[#](https://docs.openvino.ai#_CPPv4NK2ov2op4util15MultiSubGraphOp12get_functionE6size_t) Gets internal sub-graph by index in

[MultiSubGraphOp](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_multi_sub_graph_op).- Parameters:
**index**– sub-graph’s index in op- Returns:
pointer to

[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)with sub-graph


-
inline virtual const std::vector<std::shared_ptr<
[Model](https://docs.openvino.ai/classov_1_1_model.html#_CPPv4N2ov5ModelE)>> &get_functions() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op4util15MultiSubGraphOp13get_functionsEv) Gets internal sub-graphs.

- Returns:
a vector of pointers to sub-graph Models



Adds sub-graph to

[MultiSubGraphOp](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_multi_sub_graph_op).- Parameters:
**index**– index of new sub-graph**func**– func new sub_graph as[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)



-
inline const MultiSubgraphInputDescriptionVector &get_input_descriptions(int index) const
[#](https://docs.openvino.ai#_CPPv4NK2ov2op4util15MultiSubGraphOp22get_input_descriptionsEi) Gets vector with connections between operation inputs and internal sub-graph parameters.

- Parameters:
**index**– index of internal sub-graph- Returns:
vector of input descriptions



-
inline MultiSubgraphInputDescriptionVector &get_input_descriptions(int index)
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15MultiSubGraphOp22get_input_descriptionsEi) Gets vector with connections between operation inputs and internal sub-graph parameters.

- Parameters:
**index**– index of internal sub-graph- Returns:
vector of input descriptions



-
inline const MultiSubgraphOutputDescriptionVector &get_output_descriptions(int index) const
[#](https://docs.openvino.ai#_CPPv4NK2ov2op4util15MultiSubGraphOp23get_output_descriptionsEi) Gets vector with connections between operation outputs and internal sub-graph results.

- Parameters:
**index**– index of internal sub-graph- Returns:
vector of output descriptions



-
inline MultiSubgraphOutputDescriptionVector &get_output_descriptions(int index)
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15MultiSubGraphOp23get_output_descriptionsEi) Gets vector with connections between operation outputs and internal sub-graph results.

- Parameters:
**index**– index of internal sub-graph- Returns:
vector of output descriptions



-
inline void set_input_descriptions(int index, const MultiSubgraphInputDescriptionVector &inputs)
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15MultiSubGraphOp22set_input_descriptionsEiRK35MultiSubgraphInputDescriptionVector) Sets vector with connections between operation inputs and internal sub-graph parameters.

- Parameters:
**index**– index of internal sub-graph**inputs**– vector of input descriptions



-
inline void set_output_descriptions(int index, const MultiSubgraphOutputDescriptionVector &outputs)
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15MultiSubGraphOp23set_output_descriptionsEiRK36MultiSubgraphOutputDescriptionVector) Sets vector with connections between operation outputs and internal sub-graph results.

- Parameters:
**index**– index of internal sub-graph**outputs**– vector of input descriptions



-
virtual void set_invariant_inputs(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &value, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::ParameterVector &bodies_parameters)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15MultiSubGraphOp20set_invariant_inputsERK6OutputI4NodeERKN2ov15ParameterVectorE) Set input decriptions for

[MultiSubGraphOp](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_multi_sub_graph_op)input.- Parameters:
**value**– The value supplied as an input to the block.**bodies_parameters**– vector of bodies parameters.



-
virtual
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> set_body_outputs(const ResultVector &bodies_results)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15MultiSubGraphOp16set_body_outputsERK12ResultVector) Set output decriptions for

[MultiSubGraphOp](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_multi_sub_graph_op)output.- Parameters:
**bodies_results**– vector of bodies results for one output.- Returns:
value

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)node for bodies_results.


-
inline virtual size_t get_internal_subgraphs_size() const
[#](https://docs.openvino.ai#_CPPv4NK2ov2op4util15MultiSubGraphOp27get_internal_subgraphs_sizeEv) Get number of internal sub-graphs.

- Returns:
Number of sub-graphs.



-
inline virtual size_t get_input_descriptions_size() const
[#](https://docs.openvino.ai#_CPPv4NK2ov2op4util15MultiSubGraphOp27get_input_descriptions_sizeEv) Get number of input descriptions.

- Returns:
Number of input descriptions



-
inline virtual size_t get_output_descriptions_size() const
[#](https://docs.openvino.ai#_CPPv4NK2ov2op4util15MultiSubGraphOp28get_output_descriptions_sizeEv) Get number of output descriptions.

- Returns:
Number of output descriptions



-
class BodyOutputDescription : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[MultiSubGraphOp](https://docs.openvino.ai#_CPPv4N2ov2op4util15MultiSubGraphOpE)::[OutputDescription](https://docs.openvino.ai#_CPPv4N2ov2op4util15MultiSubGraphOp17OutputDescriptionE)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15MultiSubGraphOp21BodyOutputDescriptionE) Produces an output from a specific iteration.

Public Functions

-
BodyOutputDescription(uint64_t body_value_index, uint64_t output_index, int64_t iteration = -1)
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15MultiSubGraphOp21BodyOutputDescription21BodyOutputDescriptionE8uint64_t8uint64_t7int64_t) Constructs a new instance.

- Parameters:
**body_value_index**– A body value that produces the output**output_index**– The[SubGraphOp](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_sub_graph_op)output index**iteration**– which iteration (typically -1, final) will supply the value



-
BodyOutputDescription(uint64_t body_value_index, uint64_t output_index, int64_t iteration = -1)

-
class ConcatOutputDescription : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[MultiSubGraphOp](https://docs.openvino.ai#_CPPv4N2ov2op4util15MultiSubGraphOpE)::[OutputDescription](https://docs.openvino.ai#_CPPv4N2ov2op4util15MultiSubGraphOp17OutputDescriptionE)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15MultiSubGraphOp23ConcatOutputDescriptionE) Produces an output by concatenating an output from each iteration.

Public Functions

-
ConcatOutputDescription(uint64_t body_value_index, uint64_t output_index, int64_t start, int64_t stride, int64_t part_size, int64_t end, int64_t axis)
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15MultiSubGraphOp23ConcatOutputDescription23ConcatOutputDescriptionE8uint64_t8uint64_t7int64_t7int64_t7int64_t7int64_t7int64_t) Constructs a new instance.

- Parameters:
**body_value_index**– A body value that produces the output**output_index**– The[MultiSubGraphOp](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_multi_sub_graph_op)output index**start**– First index for slices**stride**– Step amount for slices**part_size**– Width of slices**end**– Last index for slices**axis**– Axis being sliced



-
ConcatOutputDescription(uint64_t body_value_index, uint64_t output_index, int64_t start, int64_t stride, int64_t part_size, int64_t end, int64_t axis)

-
class InputDescription
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15MultiSubGraphOp16InputDescriptionE) Abstract class describes a connection between a

[MultiSubGraphOp](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_multi_sub_graph_op)input and the body.Subclassed by

[ov::op::util::MultiSubGraphOp::InvariantInputDescription](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_multi_sub_graph_op_1_1_invariant_input_description),[ov::op::util::MultiSubGraphOp::MergedInputDescription](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_multi_sub_graph_op_1_1_merged_input_description),[ov::op::util::MultiSubGraphOp::SliceInputDescription](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_multi_sub_graph_op_1_1_slice_input_description)

-
class InvariantInputDescription : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[MultiSubGraphOp](https://docs.openvino.ai#_CPPv4N2ov2op4util15MultiSubGraphOpE)::[InputDescription](https://docs.openvino.ai#_CPPv4N2ov2op4util15MultiSubGraphOp16InputDescriptionE)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15MultiSubGraphOp25InvariantInputDescriptionE) Produces an input.

Public Functions

-
InvariantInputDescription(uint64_t input_index, uint64_t body_parameter_index)
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15MultiSubGraphOp25InvariantInputDescription25InvariantInputDescriptionE8uint64_t8uint64_t) Constructs a new instance.

- Parameters:
**input_index**– Position of the[MultiSubGraphOp](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_multi_sub_graph_op)input**body_parameter_index**– Body parameter to receive input



-
InvariantInputDescription(uint64_t input_index, uint64_t body_parameter_index)

-
class MergedInputDescription : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[MultiSubGraphOp](https://docs.openvino.ai#_CPPv4N2ov2op4util15MultiSubGraphOpE)::[InputDescription](https://docs.openvino.ai#_CPPv4N2ov2op4util15MultiSubGraphOp16InputDescriptionE)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15MultiSubGraphOp22MergedInputDescriptionE) Describes a body input initialized from a

[MultiSubGraphOp](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_multi_sub_graph_op)input on the first iteration, and then a body output thereafter.Public Functions

-
MergedInputDescription(uint64_t input_index, uint64_t body_parameter_index, uint64_t body_value_index)
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15MultiSubGraphOp22MergedInputDescription22MergedInputDescriptionE8uint64_t8uint64_t8uint64_t) Constructs a new instance.

- Parameters:
**input_index**– Position of the[MultiSubGraphOp](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_multi_sub_graph_op)input supplying a value to body_parameter for the initial iteration.**body_parameter_index**– Body parameter position to receive input.**body_value_index**– Body value to supply body_parameter for successive iterations.



-
MergedInputDescription(uint64_t input_index, uint64_t body_parameter_index, uint64_t body_value_index)

-
class OutputDescription
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15MultiSubGraphOp17OutputDescriptionE) Abstract class describes how a

[MultiSubGraphOp](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_multi_sub_graph_op)output is produced from the body.Subclassed by

[ov::op::util::MultiSubGraphOp::BodyOutputDescription](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_multi_sub_graph_op_1_1_body_output_description),[ov::op::util::MultiSubGraphOp::ConcatOutputDescription](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_multi_sub_graph_op_1_1_concat_output_description)

-
class SliceInputDescription : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[MultiSubGraphOp](https://docs.openvino.ai#_CPPv4N2ov2op4util15MultiSubGraphOpE)::[InputDescription](https://docs.openvino.ai#_CPPv4N2ov2op4util15MultiSubGraphOp16InputDescriptionE)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15MultiSubGraphOp21SliceInputDescriptionE) Describes a body input formed from slices of an input to

[MultiSubGraphOp](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_multi_sub_graph_op).Public Functions

-
SliceInputDescription(uint64_t input_index, uint64_t body_parameter_index, int64_t start, int64_t stride, int64_t part_size, int64_t end, int64_t axis)
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15MultiSubGraphOp21SliceInputDescription21SliceInputDescriptionE8uint64_t8uint64_t7int64_t7int64_t7int64_t7int64_t7int64_t) Constructs a new instance.

- Parameters:
**input_index**– Position of the[MultiSubGraphOp](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_multi_sub_graph_op)input**body_parameter_index**– Body parameter position to receive input**start**– First index for slices**stride**– Step amount for slices**part_size**– Width of slices**end**– Last index for slices**axis**– Axis being sliced



-
SliceInputDescription(uint64_t input_index, uint64_t body_parameter_index, int64_t start, int64_t stride, int64_t part_size, int64_t end, int64_t axis)

-
inline virtual const std::shared_ptr<