source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1util_1_1_variable_extension.html
lastmod: 

# Class ov::op::util::VariableExtension[#](https://docs.openvino.ai#class-ov-op-util-variableextension)

-
class VariableExtension
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util17VariableExtensionE) Subclassed by

[ov::op::util::AssignBase](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_assign_base),[ov::op::util::ReadValueBase](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_read_value_base)Public Functions

-
inline virtual std::shared_ptr<
[Variable](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_variable.html#_CPPv4N2ov2op4util8VariableE)> get_variable() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op4util17VariableExtension12get_variableEv) Returns variable connected to this node.


Sets a new variable to be connected to this node.

- Parameters:
**variable**– New variable to be connected to this node.


-
inline virtual void set_variable_id(const std::string &variable_id)
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util17VariableExtension15set_variable_idERKNSt6stringE) Sets the identifier to a variable.

- Parameters:
**variable_id**– New identifier of the variable.


-
virtual std::string get_variable_id() const = 0
[#](https://docs.openvino.ai#_CPPv4NK2ov2op4util17VariableExtension15get_variable_idEv) Returns the identifier of corresponding variable.


-
inline virtual std::shared_ptr<