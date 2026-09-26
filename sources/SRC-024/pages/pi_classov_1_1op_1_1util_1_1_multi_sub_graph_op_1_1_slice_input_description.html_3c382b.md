source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1util_1_1_multi_sub_graph_op_1_1_slice_input_description.html
lastmod: 

# Class ov::op::util::MultiSubGraphOp::SliceInputDescription[#](https://docs.openvino.ai#class-ov-op-util-multisubgraphop-sliceinputdescription)

-
class SliceInputDescription : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[MultiSubGraphOp](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_multi_sub_graph_op.html#_CPPv4N2ov2op4util15MultiSubGraphOpE)::[InputDescription](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_multi_sub_graph_op.html#_CPPv4N2ov2op4util15MultiSubGraphOp16InputDescriptionE) Describes a body input formed from slices of an input to

[MultiSubGraphOp](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_multi_sub_graph_op).Public Functions

-
SliceInputDescription(uint64_t input_index, uint64_t body_parameter_index, int64_t start, int64_t stride, int64_t part_size, int64_t end, int64_t axis)
Constructs a new instance.

- Parameters:
**input_index**– Position of the[MultiSubGraphOp](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_multi_sub_graph_op)input**body_parameter_index**– Body parameter position to receive input**start**– First index for slices**stride**– Step amount for slices**part_size**– Width of slices**end**– Last index for slices**axis**– Axis being sliced



-
SliceInputDescription(uint64_t input_index, uint64_t body_parameter_index, int64_t start, int64_t stride, int64_t part_size, int64_t end, int64_t axis)