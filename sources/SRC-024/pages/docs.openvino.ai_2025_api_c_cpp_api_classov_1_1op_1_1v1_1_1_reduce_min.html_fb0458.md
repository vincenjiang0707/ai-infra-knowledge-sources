source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v1_1_1_reduce_min.html
lastmod: 

# Class ov::op::v1::ReduceMin[#](https://docs.openvino.ai#class-ov-op-v1-reducemin)

-
class ReduceMin : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ArithmeticReductionKeepDims](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_arithmetic_reduction_keep_dims.html#_CPPv4N2ov2op4util27ArithmeticReductionKeepDimsE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19ReduceMinE) [ReduceMin](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_reduce_min)operation.Public Functions

-
ReduceMin() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19ReduceMin9ReduceMinEv) Constructs a summation operation.


-
ReduceMin(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &reduction_axes, bool keep_dims = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19ReduceMin9ReduceMinERK6OutputI4NodeERK6OutputI4NodeEb) Constructs a summation operation.

- Parameters:
**arg**– The tensor to be summed.**reduction_axes**– The axis positions (0-based) to be eliminated.**keep_dims**– If set to 1 it holds axes that are used for reduction.



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v19ReduceMin12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
ReduceMin() = default