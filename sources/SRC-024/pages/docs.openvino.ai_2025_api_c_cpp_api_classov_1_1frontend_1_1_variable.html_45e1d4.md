source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1frontend_1_1_variable.html
lastmod: 

# Class ov::frontend::Variable[#](https://docs.openvino.ai#class-ov-frontend-variable)

-
class Variable : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[FrameworkNode](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_framework_node.html#_CPPv4N2ov2op4util13FrameworkNodeE)[#](https://docs.openvino.ai#_CPPv4N2ov8frontend8VariableE) [Variable](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_variable)is a special node used in a conversion step It can have several values (or states) during the conversion.[Variable](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_variable)value at some time step is represented with a graph.Subclassed by

[ov::frontend::HashTable](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_hash_table)Public Functions

-
inline virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov8frontend8Variable24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline bool is_initialized() const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend8Variable14is_initializedEv) Checks if variable is initialized with some value.


-
inline uint64_t get_init_counter() const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend8Variable16get_init_counterEv) Returns a counter value (a number of values that have assigned to this variable)


-
inline virtual void validate_and_infer_types() override