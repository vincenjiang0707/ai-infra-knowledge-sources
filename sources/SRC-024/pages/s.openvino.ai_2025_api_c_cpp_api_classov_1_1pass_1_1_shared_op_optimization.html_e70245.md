source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_shared_op_optimization.html
lastmod: 

# Class ov::pass::SharedOpOptimization[#](https://docs.openvino.ai#class-ov-pass-sharedopoptimization)

-
class SharedOpOptimization : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[ModelPass](https://docs.openvino.ai/classov_1_1pass_1_1_model_pass.html#_CPPv4N2ov4pass9ModelPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass20SharedOpOptimizationE) [SharedOpOptimization](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_shared_op_optimization)optimizes operations which are sourcing from same[Output<Node>](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output_3_01_node_01_4)and perform the same action on the same data.

Site Navigation

Section Navigation

[SharedOpOptimization](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_shared_op_optimization) optimizes operations which are sourcing from same [Output<Node>](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output_3_01_node_01_4) and perform the same action on the same data.