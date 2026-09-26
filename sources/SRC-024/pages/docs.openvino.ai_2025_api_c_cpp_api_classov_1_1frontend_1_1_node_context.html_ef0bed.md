source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1frontend_1_1_node_context.html
lastmod: 

# Class ov::frontend::NodeContext[#](https://docs.openvino.ai#class-ov-frontend-nodecontext)

-
class NodeContext
[#](https://docs.openvino.ai#_CPPv4N2ov8frontend11NodeContextE) Public Functions

-
inline virtual size_t get_input_size() const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend11NodeContext14get_input_sizeEv) Returns a number of inputs.


-
inline virtual size_t get_input_size(const std::string &port_name) const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend11NodeContext14get_input_sizeERKNSt6stringE) Returns a number of inputs.


-
inline virtual
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> get_input(int idx) const[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend11NodeContext9get_inputEi) Returns exactly one input with a given idx; throws if there is no inputs or there are more than one input.


-
inline virtual
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> get_input(const std::string &name, int idx) const[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend11NodeContext9get_inputERKNSt6stringEi) Returns exactly one input with a given name and idx; throws if there is no inputs or there are more than one input.


-
inline virtual
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> get_input(const std::string &name) const[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend11NodeContext9get_inputERKNSt6stringE) Returns exactly one input with a given name; throws if there is no inputs or there are more than one input.


-
inline virtual
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> get_input_by_reference(int idx) const[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend11NodeContext22get_input_by_referenceEi) Returns output of

[Variable](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_variable)node (or[Variable](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_variable)value).[Variable](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_variable)is a special node that stores a value represented with a sub-graph.[Variable](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_variable)has a concrete value at each conversion step. The current (consuming) operation node can change its value so consumers of this[Variable](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_variable)will have a new value at next conversion steps. See[ov::frontend::Variable](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_variable)class for more details.

-
inline virtual
[Any](https://docs.openvino.ai/classov_1_1_any.html#_CPPv4N2ov3AnyE)get_values_from_const_input(int idx) const[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend11NodeContext27get_values_from_const_inputEi) Returns values from Constant input with the given index as

[ov::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any). Throws an exception if the input cannot be represented as Constant.

-
template<class T>

inline[T](https://docs.openvino.ai#_CPPv4I0ENK2ov8frontend11NodeContext13get_attributeE1TRKNSt6stringE)get_attribute(const std::string &name) const[#](https://docs.openvino.ai#_CPPv4I0ENK2ov8frontend11NodeContext13get_attributeE1TRKNSt6stringE) Returns node attribute by name.


-
template<class T>

inline[T](https://docs.openvino.ai#_CPPv4I0ENK2ov8frontend11NodeContext13get_attributeE1TRKNSt6stringERK1T)get_attribute(const std::string &name, const[T](https://docs.openvino.ai#_CPPv4I0ENK2ov8frontend11NodeContext13get_attributeE1TRKNSt6stringERK1T)&def) const[#](https://docs.openvino.ai#_CPPv4I0ENK2ov8frontend11NodeContext13get_attributeE1TRKNSt6stringERK1T) Returns node attribute by name. Returns ‘def’ value if attribute does not exist.


-
inline bool has_attribute(const std::string &name) const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend11NodeContext13has_attributeERKNSt6stringE) Check if an attribute of a given name exist.


-
virtual
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Any](https://docs.openvino.ai/classov_1_1_any.html#_CPPv4N2ov3AnyE)get_attribute_as_any(const std::string &name) const = 0[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend11NodeContext20get_attribute_as_anyERKNSt6stringE) Returns node attribute by name as

[ov::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any).

-
inline virtual size_t get_subgraph_size() const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend11NodeContext17get_subgraph_sizeEv) Returns the number of sub-graphs that can be enumerated with get_subgraph.


-
inline virtual std::shared_ptr<
[Model](https://docs.openvino.ai/classov_1_1_model.html#_CPPv4N2ov5ModelE)> get_subgraph(int idx) const[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend11NodeContext12get_subgraphEi) Returns subgraph converted on demand by the first access If there is no query for specific sub-graph it shouldn’t be converted idx should be in range 0..

[get_subgraph_size()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_node_context_1abb9e3c6bc924a129f38ae1cf3cedf4e7)-1.

Returns

[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)object that can be with updated attributes such node name, runtime info, etc. By default, it returns the same node without update.

-
inline virtual bool input_is_none(size_t index) const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend11NodeContext13input_is_noneE6size_t) PyTorch may have None inputs coming to operations Other frontends do not have it per our observation.


-
inline virtual size_t get_input_size() const