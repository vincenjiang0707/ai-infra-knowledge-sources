source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v1_1_1_reduce_mean.html
lastmod: 

# Class ov::op::v1::ReduceMean[#](https://docs.openvino.ai#class-ov-op-v1-reducemean)

-
class ReduceMean : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ArithmeticReductionKeepDims](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_arithmetic_reduction_keep_dims.html#_CPPv4N2ov2op4util27ArithmeticReductionKeepDimsE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v110ReduceMeanE) [ReduceMean](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_reduce_mean)operation.Public Functions

-
ReduceMean(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &reduction_axes, bool keep_dims = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v110ReduceMean10ReduceMeanERK6OutputI4NodeERK6OutputI4NodeEb) - Parameters:
**arg**– The tensor to be summed.**reduction_axes**– The axis positions (0-based) to be eliminated.**keep_dims**– If set to 1 it holds axes that are used for reduction.



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v110ReduceMean12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
ReduceMean(const