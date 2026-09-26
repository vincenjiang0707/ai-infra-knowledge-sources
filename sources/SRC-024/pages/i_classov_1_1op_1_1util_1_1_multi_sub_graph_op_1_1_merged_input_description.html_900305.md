source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1util_1_1_multi_sub_graph_op_1_1_merged_input_description.html
lastmod: 

# Class ov::op::util::MultiSubGraphOp::MergedInputDescription[#](https://docs.openvino.ai#class-ov-op-util-multisubgraphop-mergedinputdescription)

-
class MergedInputDescription : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[MultiSubGraphOp](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_multi_sub_graph_op.html#_CPPv4N2ov2op4util15MultiSubGraphOpE)::[InputDescription](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_multi_sub_graph_op.html#_CPPv4N2ov2op4util15MultiSubGraphOp16InputDescriptionE) Describes a body input initialized from a

[MultiSubGraphOp](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_multi_sub_graph_op)input on the first iteration, and then a body output thereafter.Public Functions

-
MergedInputDescription(uint64_t input_index, uint64_t body_parameter_index, uint64_t body_value_index)
Constructs a new instance.

- Parameters:
**input_index**– Position of the[MultiSubGraphOp](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_multi_sub_graph_op)input supplying a value to body_parameter for the initial iteration.**body_parameter_index**– Body parameter position to receive input.**body_value_index**– Body value to supply body_parameter for successive iterations.



-
MergedInputDescription(uint64_t input_index, uint64_t body_parameter_index, uint64_t body_value_index)