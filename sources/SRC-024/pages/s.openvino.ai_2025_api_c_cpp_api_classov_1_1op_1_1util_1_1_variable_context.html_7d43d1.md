source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1util_1_1_variable_context.html
lastmod: 

# Class ov::op::util::VariableContext[#](https://docs.openvino.ai#class-ov-op-util-variablecontext)

-
class VariableContext
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15VariableContextE) [VariableContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_variable_context)stores and manages a evaluation context for Variables.Public Functions

-
VariableContext() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15VariableContext15VariableContextEv) Constructs an uninitialized

[VariableContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_variable_context).

-
inline explicit VariableContext(const
[VariableMap](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4util11VariableMapE)&variable_values)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15VariableContext15VariableContextERK11VariableMap) Constructor for

[VariableContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_variable_context).- Parameters:
**variable_values**– The values associated with a particular Variables.


-
inline void reset_variable_context() const
[#](https://docs.openvino.ai#_CPPv4NK2ov2op4util15VariableContext22reset_variable_contextEv) Sets the reset flags for all stored Variables to true.


-
inline void set_variable_values(const
[VariableMap](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4util11VariableMapE)&variable_values)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15VariableContext19set_variable_valuesERK11VariableMap) Sets the new values for Variables.

- Parameters:
**variable_values**– The new values associated with a particular[Variable](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_variable).


-
inline void set_variable_value(const
[Variable](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_variable.html#_CPPv4N2ov2op4util8VariableE)::Ptr &variable, const[VariableValue](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_variable_value.html#_CPPv4N2ov2op4util13VariableValueE)::Ptr &variable_value)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15VariableContext18set_variable_valueERKN8Variable3PtrERKN13VariableValue3PtrE) Changes/sets the values for

[Variable](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_variable).- Parameters:
**variable**– New or stored[Variable](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_variable).**variable_value**– The values associated with the variable.



-
inline void remove_variable_value(const
[Variable](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_variable.html#_CPPv4N2ov2op4util8VariableE)::Ptr &variable)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15VariableContext21remove_variable_valueERKN8Variable3PtrE) Removes context for a particular

[Variable](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_variable).- Parameters:
**variable**– The variable for which the context will be cleared.


-
inline const
[VariableMap](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4util11VariableMapE)&get_variable_values() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op4util15VariableContext19get_variable_valuesEv) Returns the current values for Variables.


-
inline
[VariableValue](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_variable_value.html#_CPPv4N2ov2op4util13VariableValueE)::Ptr get_variable_value(const[Variable](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_variable.html#_CPPv4N2ov2op4util8VariableE)::Ptr &variable) const[#](https://docs.openvino.ai#_CPPv4NK2ov2op4util15VariableContext18get_variable_valueERKN8Variable3PtrE) Returns the value for specified

[Variable](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_variable).

-
VariableContext() = default