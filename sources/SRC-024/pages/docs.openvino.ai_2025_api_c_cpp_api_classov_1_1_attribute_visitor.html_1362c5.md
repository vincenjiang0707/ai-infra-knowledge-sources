source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_attribute_visitor.html
lastmod: 

# Class ov::AttributeVisitor[#](https://docs.openvino.ai#class-ov-attributevisitor)

-
class AttributeVisitor
[#](https://docs.openvino.ai#_CPPv4N2ov16AttributeVisitorE) Visits the attributes of a node, primarily for serialization-like tasks.

Attributes are the node parameters that are always compile-time constants. Values computed from the graph topology and attributes during compilation are not attributes.

Attributes have a wide variety of types, but serialization formats are more restricted. We assume serialization easily supports scalar types of bool 64-bit signed, string, and double, and has specialized ways to support numeric arrays and raw data+size. The visitor and adapter convert between the limited serialization types and the unlimited attribute types.

A visitor is passed to an op’s visit_attributes method. The visit_attributes method calls the template method visitor.on_attribute<AT>(const std::string& name, AT& value) on each attribute. The visitor can read or write the attribute’s value. The on_attribute method creates an AttributeAdapter<AT> for the value and passes it to one of the visitors on_adapter methods. The on_adapter methods expect a reference to a ValueAccessor<VAT> or a

[VisitorAdapter](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_visitor_adapter). A ValueAccessor<VAT> has get/set methods that can be used to read/write the attribute value as type VAT. These methods are triggered by deriving AttributeAdapter<AT> from ValueAccessor<VAT>. For more complex cases, such as structs, the on_adapter method for[VisitorAdapter](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_visitor_adapter)passes the name and visitor to the adapter, so that the adapter can perform additional work such as visiting struct members or sequence values.When a node visits an attribute with structure, the node’s on_attribute passes a name for the entire attribute, but the struct will have its own methods to be visited. Similarly, a vector will have a sequence of members to be visited. The adapter may use the visitor methods start_struct/finish_struct and start_vector/next_vector/finish_vector to inidicate nexted members.

The visitor method get_name_with_context creates a generic nested version of the name. Visitors can override according to their serialization requirements.

Attributes that are shared_ptr<Node> are special. They must have been already been registered with the visitor using register_node, which needs a shared pointer to a node and a string ID. The ID string will be used to serialize the node or find the node during deserialization.

Subclassed by

[ov::IstreamAttributeVisitor< IStreamType >](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_istream_attribute_visitor),[ov::OstreamAttributeVisitor< OStreamType >](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_ostream_attribute_visitor),[ov::frontend::FWVisitor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_f_w_visitor),[ov::frontend::FWVisitorInputAttributes](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_f_w_visitor_input_attributes),[ov::gen_pattern::detail::AttrSetter](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1gen__pattern_1_1detail_1_1_attr_setter),[ov::pass::detail::OstreamAttributeVisitor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1detail_1_1_ostream_attribute_visitor)Public Functions

-
virtual void on_adapter(const std::string &name,
[ValueAccessor](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov13ValueAccessorIvEE)<void> &adapter) = 0[#](https://docs.openvino.ai#_CPPv4N2ov16AttributeVisitor10on_adapterERKNSt6stringER13ValueAccessorIvE) handles all specialized on_adapter methods implemented by the visitor.

The adapter implements get_type_info(), which can be used to determine the adapter directly or via is_type and as_type on any platform


-
virtual void on_adapter(const std::string &name,
[VisitorAdapter](https://docs.openvino.ai/classov_1_1_visitor_adapter.html#_CPPv4N2ov14VisitorAdapterE)&adapter)[#](https://docs.openvino.ai#_CPPv4N2ov16AttributeVisitor10on_adapterERKNSt6stringER14VisitorAdapter) Hook for adapters that need visitor access.


Provides API to handle openvino Function attribute type, accessed as

[ValueAccessor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_value_accessor).- Parameters:
**name**– attribute name**adapter**– reference to a Function ValueAccessor<VAT>



-
template<typename AT>

inline void on_attribute(const std::string &name,[AT](https://docs.openvino.ai#_CPPv4I0EN2ov16AttributeVisitor12on_attributeEvRKNSt6stringER2AT)&value)[#](https://docs.openvino.ai#_CPPv4I0EN2ov16AttributeVisitor12on_attributeEvRKNSt6stringER2AT) The generic visitor. There must be a definition of AttributeAdapter<T> that can convert to a

[ValueAccessor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_value_accessor)

-
inline const std::vector<std::string> &get_context() const
[#](https://docs.openvino.ai#_CPPv4NK2ov16AttributeVisitor11get_contextEv) - Returns:
The nested context of visits



-
virtual std::string get_name_with_context()
[#](https://docs.openvino.ai#_CPPv4N2ov16AttributeVisitor21get_name_with_contextEv) - Returns:
context prepended to names



-
virtual void start_structure(const std::string &name)
[#](https://docs.openvino.ai#_CPPv4N2ov16AttributeVisitor15start_structureERKNSt6stringE) Start visiting a nested structure.


-
virtual std::string finish_structure()
[#](https://docs.openvino.ai#_CPPv4N2ov16AttributeVisitor16finish_structureEv) Finish visiting a nested structure.


Associate a node with an id.

No node may be used as an attribute unless it has already been registered with an ID. References to nodes are visited with a

[ValueAccessor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_value_accessor)of their ID.

-
virtual std::shared_ptr<
[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> get_registered_node(node_id_t id)[#](https://docs.openvino.ai#_CPPv4N2ov16AttributeVisitor19get_registered_nodeE9node_id_t) Returns the node with the given id, or nullptr if there is no registered node.


Returns the id for the node, or -1 if the node is not registered.


-
virtual void on_adapter(const std::string &name,