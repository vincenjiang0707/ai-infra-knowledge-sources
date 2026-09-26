source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1util_1_1_multi_sub_graph_op_1_1_invariant_input_description.html
lastmod: 

# Class ov::op::util::MultiSubGraphOp::InvariantInputDescription[#](https://docs.openvino.ai#class-ov-op-util-multisubgraphop-invariantinputdescription)

-
class InvariantInputDescription : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[MultiSubGraphOp](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_multi_sub_graph_op.html#_CPPv4N2ov2op4util15MultiSubGraphOpE)::[InputDescription](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_multi_sub_graph_op.html#_CPPv4N2ov2op4util15MultiSubGraphOp16InputDescriptionE) Produces an input.

Public Functions

-
InvariantInputDescription(uint64_t input_index, uint64_t body_parameter_index)
Constructs a new instance.

- Parameters:
**input_index**– Position of the[MultiSubGraphOp](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_multi_sub_graph_op)input**body_parameter_index**– Body parameter to receive input



-
InvariantInputDescription(uint64_t input_index, uint64_t body_parameter_index)