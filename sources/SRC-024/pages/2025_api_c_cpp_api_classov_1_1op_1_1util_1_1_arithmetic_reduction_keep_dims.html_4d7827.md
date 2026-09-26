source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1util_1_1_arithmetic_reduction_keep_dims.html
lastmod: 

# Class ov::op::util::ArithmeticReductionKeepDims[#](https://docs.openvino.ai#class-ov-op-util-arithmeticreductionkeepdims)

-
class ArithmeticReductionKeepDims : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ArithmeticReduction](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_arithmetic_reduction.html#_CPPv4N2ov2op4util19ArithmeticReductionE)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util27ArithmeticReductionKeepDimsE) Subclassed by

[ov::op::v1::ReduceMax](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_reduce_max),[ov::op::v1::ReduceMean](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_reduce_mean),[ov::op::v1::ReduceMin](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_reduce_min),[ov::op::v1::ReduceProd](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_reduce_prod),[ov::op::v1::ReduceSum](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_reduce_sum),[ov::op::v4::ReduceL1](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_reduce_l1),[ov::op::v4::ReduceL2](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_reduce_l2)Public Functions

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util27ArithmeticReductionKeepDims24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline virtual bool get_keep_dims() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op4util27ArithmeticReductionKeepDims13get_keep_dimsEv) - Returns:
If set to 1 it holds axes that are used for reduction. For each such axis, output dimension is equal to 1.



-
virtual void validate_and_infer_types() override