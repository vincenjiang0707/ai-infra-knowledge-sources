source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1util_1_1_framework_node.html
lastmod: 

# Class ov::op::util::FrameworkNode[#](https://docs.openvino.ai#class-ov-op-util-frameworknode)

-
class FrameworkNode : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[MultiSubGraphOp](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_multi_sub_graph_op.html#_CPPv4N2ov2op4util15MultiSubGraphOpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util13FrameworkNodeE) Subclassed by

[ov::frontend::ComplexTypeMark](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_complex_type_mark),[ov::frontend::SequenceMark](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_sequence_mark),[ov::frontend::Variable](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_variable)Public Functions

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util13FrameworkNode24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual void validate_and_infer_types() override