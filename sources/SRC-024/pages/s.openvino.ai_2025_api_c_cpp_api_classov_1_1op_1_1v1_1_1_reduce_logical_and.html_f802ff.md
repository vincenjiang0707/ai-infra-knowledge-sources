source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v1_1_1_reduce_logical_and.html
lastmod: 

# Class ov::op::v1::ReduceLogicalAnd[#](https://docs.openvino.ai#class-ov-op-v1-reducelogicaland)

-
class ReduceLogicalAnd : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[LogicalReductionKeepDims](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_logical_reduction_keep_dims.html#_CPPv4N2ov2op4util24LogicalReductionKeepDimsE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v116ReduceLogicalAndE) Performs a reduction using “logical and”.

The reduction is performed over slices of the first input. The slices shape depends on the values passed to the second input - the axes.

Public Functions

-
ReduceLogicalAnd(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &reduction_axes, const bool keep_dims = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v116ReduceLogicalAnd16ReduceLogicalAndERK6OutputI4NodeERK6OutputI4NodeEKb) Constructs a

[ReduceLogicalAnd](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_reduce_logical_and)node.- Parameters:
**data**– - The input tensor with data to be reduced**reduction_axes**– - The input tensor with information about axes over which the first tensor should be sliced prior to the reduction operation**keep_dims**– - Indicates if the axes used for reduction should be held/kept



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v116ReduceLogicalAnd12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
ReduceLogicalAnd(const