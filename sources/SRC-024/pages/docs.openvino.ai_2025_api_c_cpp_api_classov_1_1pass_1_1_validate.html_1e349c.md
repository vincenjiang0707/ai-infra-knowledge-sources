source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_validate.html
lastmod: 

# Class ov::pass::Validate[#](https://docs.openvino.ai#class-ov-pass-validate)

-
class Validate : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[ModelPass](https://docs.openvino.ai/classov_1_1pass_1_1_model_pass.html#_CPPv4N2ov4pass9ModelPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass8ValidateE) The

[Validate](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_validate)pass performs sanity checks on attributes and inputs, and computes output shapes and element types for all computation nodes in a given computation graph.The verification and inference is done via invoking each node’s specific implementation of

[ov::Node::validate_and_infer_types()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node_1ac5224b5be848ec670d2078d9816d12e7)function.By default, the

[ov::pass::Manager](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_manager)runs this pass after executing every optimization pass. This is to ensure that any update to the graph by an optimization pass does not break the shape and data type requirement on a computation node. This default validation run can be changed via calling the[ov::pass::Manager::set_per_pass_validation(bool)](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_manager_1a4efe949a17dd14d02888540b2586d411)function.