source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1util_1_1_logical_reduction_keep_dims.html
lastmod: 

# Class ov::op::util::LogicalReductionKeepDims[#](https://docs.openvino.ai#class-ov-op-util-logicalreductionkeepdims)

-
class LogicalReductionKeepDims : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[LogicalReduction](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_logical_reduction.html#_CPPv4N2ov2op4util16LogicalReductionE)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util24LogicalReductionKeepDimsE) Subclassed by

[ov::op::v1::ReduceLogicalAnd](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_reduce_logical_and),[ov::op::v1::ReduceLogicalOr](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_reduce_logical_or)Public Functions

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util24LogicalReductionKeepDims24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline virtual bool get_keep_dims() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op4util24LogicalReductionKeepDims13get_keep_dimsEv) - Returns:
If set to 1 it holds axes that are used for reduction. For each such axis, output dimension is equal to 1.



-
virtual void validate_and_infer_types() override