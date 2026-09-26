source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1util_1_1_multi_sub_graph_op_1_1_body_output_description.html
lastmod: 

# Class ov::op::util::MultiSubGraphOp::BodyOutputDescription[#](https://docs.openvino.ai#class-ov-op-util-multisubgraphop-bodyoutputdescription)

-
class BodyOutputDescription : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[MultiSubGraphOp](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_multi_sub_graph_op.html#_CPPv4N2ov2op4util15MultiSubGraphOpE)::[OutputDescription](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_multi_sub_graph_op.html#_CPPv4N2ov2op4util15MultiSubGraphOp17OutputDescriptionE) Produces an output from a specific iteration.

Public Functions

-
BodyOutputDescription(uint64_t body_value_index, uint64_t output_index, int64_t iteration = -1)
Constructs a new instance.

- Parameters:
**body_value_index**– A body value that produces the output**output_index**– The[SubGraphOp](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_sub_graph_op)output index**iteration**– which iteration (typically -1, final) will supply the value



-
BodyOutputDescription(uint64_t body_value_index, uint64_t output_index, int64_t iteration = -1)