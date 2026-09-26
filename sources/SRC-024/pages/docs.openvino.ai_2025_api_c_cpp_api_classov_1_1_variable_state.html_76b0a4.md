source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_variable_state.html
lastmod: 

# Class ov::VariableState[#](https://docs.openvino.ai#class-ov-variablestate)

-
class VariableState
[#](https://docs.openvino.ai#_CPPv4N2ov13VariableStateE) [VariableState](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_variable_state)class.Public Functions

-
VariableState() = default
[#](https://docs.openvino.ai#_CPPv4N2ov13VariableState13VariableStateEv) Default constructor.


-
~VariableState()
[#](https://docs.openvino.ai#_CPPv4N2ov13VariableStateD0Ev) Destructor that preserves unloading order of implementation object and reference to the library.


-
void reset()
[#](https://docs.openvino.ai#_CPPv4N2ov13VariableState5resetEv) Resets internal variable state for relevant infer request to a value specified as default for the corresponding ReadValue node.


-
std::string get_name() const
[#](https://docs.openvino.ai#_CPPv4NK2ov13VariableState8get_nameEv) Gets the name of the current variable state. If length of an array is not enough, the name is truncated by len, null terminator is inserted as well.

`variable_id`

from the corresponding`ReadValue`

is used as variable state name.- Returns:
A string representing state name.



-
VariableState() = default