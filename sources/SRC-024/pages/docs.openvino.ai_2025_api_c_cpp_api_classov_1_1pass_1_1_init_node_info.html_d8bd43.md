source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_init_node_info.html
lastmod: 

# Class ov::pass::InitNodeInfo[#](https://docs.openvino.ai#class-ov-pass-initnodeinfo)

-
class InitNodeInfo : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[ModelPass](https://docs.openvino.ai/classov_1_1pass_1_1_model_pass.html#_CPPv4N2ov4pass9ModelPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass12InitNodeInfoE) [InitNodeInfo](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_init_node_info)transformation helps to set runtime info attributes in a single place.Every runtime info attribute that needs to be initialized should be registered in run_on_function method. Also do not forget to override init methods for registered attribute. This transformations should be called first in transformation pipeline. If attribute was already set initialization will be skipped for this node.