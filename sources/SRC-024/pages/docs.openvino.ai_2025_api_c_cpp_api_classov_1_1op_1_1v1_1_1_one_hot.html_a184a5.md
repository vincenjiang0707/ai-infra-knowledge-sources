source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v1_1_1_one_hot.html
lastmod: 

# Class ov::op::v1::OneHot[#](https://docs.openvino.ai#class-ov-op-v1-onehot)

-
class OneHot : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[OneHotBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_one_hot_base.html#_CPPv4N2ov2op4util10OneHotBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v16OneHotE) [OneHot](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_one_hot)operation.Public Functions

-
OneHot() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v16OneHot6OneHotEv) Constructs a one-hot operation.


-
OneHot(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &indices, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &depth, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &on_value, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &off_value, int64_t axis)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v16OneHot6OneHotERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE7int64_t) Constructs a one-hot operation.

- Parameters:
**indices**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor containing indices.**depth**– Specifies number of classes and the size of one-hot dimension.**on_value**– Specifies value that the locations in output tensor represented by indices in input take.**off_value**– Specifies value that the locations in output tensor not represented by indices in input take.**axis**– Axis along which one-hot representation in added.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v16OneHot24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v16OneHot12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
OneHot() = default