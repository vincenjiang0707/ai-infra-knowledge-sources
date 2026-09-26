source: https://docs.openvino.ai/2025/api/c_cpp_api/group__ov__dev__api__variable__state__api.html
lastmod: 

# Group Variable state base classes[#](https://docs.openvino.ai#group-variable-state-base-classes)

-
*group*Variable state base classes A set of base and helper classes to implement variable state.

-
interface IVariableState : public std::enable_shared_from_this<
[IVariableState](https://docs.openvino.ai#_CPPv4N2ov14IVariableStateE)>[#](https://docs.openvino.ai#_CPPv4N2ov14IVariableStateE) *#include <ivariable_state.hpp>*Minimal interface for variable state implementation.

Public Functions

-
virtual const std::string &get_name() const
[#](https://docs.openvino.ai#_CPPv4NK2ov14IVariableState8get_nameEv) Gets a variable state name.

- Returns:
A string representing variable state name



-
virtual void reset()
[#](https://docs.openvino.ai#_CPPv4N2ov14IVariableState5resetEv) Reset internal variable state for relevant infer request, to a value specified as default for according

`ReadValue`

node.

-
virtual const std::string &get_name() const

-
interface IVariableState : public std::enable_shared_from_this<