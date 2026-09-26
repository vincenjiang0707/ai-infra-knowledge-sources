source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1util_1_1_multi_sub_graph_op_1_1_concat_output_description.html
lastmod: 

# Class ov::op::util::MultiSubGraphOp::ConcatOutputDescription[#](https://docs.openvino.ai#class-ov-op-util-multisubgraphop-concatoutputdescription)

-
class ConcatOutputDescription : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[MultiSubGraphOp](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_multi_sub_graph_op.html#_CPPv4N2ov2op4util15MultiSubGraphOpE)::[OutputDescription](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_multi_sub_graph_op.html#_CPPv4N2ov2op4util15MultiSubGraphOp17OutputDescriptionE) Produces an output by concatenating an output from each iteration.

Public Functions

-
ConcatOutputDescription(uint64_t body_value_index, uint64_t output_index, int64_t start, int64_t stride, int64_t part_size, int64_t end, int64_t axis)
Constructs a new instance.

- Parameters:
**body_value_index**– A body value that produces the output**output_index**– The[MultiSubGraphOp](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_multi_sub_graph_op)output index**start**– First index for slices**stride**– Step amount for slices**part_size**– Width of slices**end**– Last index for slices**axis**– Axis being sliced



-
ConcatOutputDescription(uint64_t body_value_index, uint64_t output_index, int64_t start, int64_t stride, int64_t part_size, int64_t end, int64_t axis)