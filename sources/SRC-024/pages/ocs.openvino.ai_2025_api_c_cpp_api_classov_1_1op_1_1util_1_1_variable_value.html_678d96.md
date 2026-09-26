source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1util_1_1_variable_value.html
lastmod: 

# Class ov::op::util::VariableValue[#](https://docs.openvino.ai#class-ov-op-util-variablevalue)

-
class VariableValue
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util13VariableValueE) [VariableValue](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_variable_value)stores data and state (reset flag) for a[Variable](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_variable), and provides an interface for changing them.Public Functions

-
VariableValue()
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util13VariableValue13VariableValueEv) Constructs an uninitialized

[VariableValue](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_variable_value).

-
void set_reset(bool reset)
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util13VariableValue9set_resetEb) Sets the reset flag to a new state.

- Parameters:
**reset**– The new state of the reset flag.


-
bool get_reset() const
[#](https://docs.openvino.ai#_CPPv4NK2ov2op4util13VariableValue9get_resetEv) Returns the current reset flag state.


-
VariableValue(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&value, bool reset)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util13VariableValue13VariableValueERKN2ov6TensorEb) Constructor for

[VariableValue](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_variable_value).- Parameters:
**value**– Data for[Variable](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_variable).**reset**– The current state of the reset flag.



-
VariableValue()