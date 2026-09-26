source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1frontend_1_1_hash_table.html
lastmod: 

# Class ov::frontend::HashTable[#](https://docs.openvino.ai#class-ov-frontend-hashtable)

-
class HashTable : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[frontend](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov8frontendE)::[Variable](https://docs.openvino.ai/classov_1_1frontend_1_1_variable.html#_CPPv4N2ov8frontend8VariableE)[#](https://docs.openvino.ai#_CPPv4N2ov8frontend9HashTableE) [HashTable](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_hash_table)is a special type of[Variable](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_variable)that has a complex value including keys and values. Keys and values are represented with two separate graph at each time step.Public Functions

-
inline virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov8frontend9HashTable24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline virtual void validate_and_infer_types() override