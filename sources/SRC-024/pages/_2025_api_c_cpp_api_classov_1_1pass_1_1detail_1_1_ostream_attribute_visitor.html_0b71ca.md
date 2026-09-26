source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1detail_1_1_ostream_attribute_visitor.html
lastmod: 

# Class ov::pass::detail::OstreamAttributeVisitor[#](https://docs.openvino.ai#class-ov-pass-detail-ostreamattributevisitor)

-
class OstreamAttributeVisitor : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[AttributeVisitor](https://docs.openvino.ai/classov_1_1_attribute_visitor.html#_CPPv4N2ov16AttributeVisitorE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass6detail23OstreamAttributeVisitorE) Public Functions

-
inline virtual void on_adapter(const std::string &name,
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[ValueAccessor](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov13ValueAccessorIvEE)<void> &adapter) override[#](https://docs.openvino.ai#_CPPv4N2ov4pass6detail23OstreamAttributeVisitor10on_adapterERKNSt6stringERN2ov13ValueAccessorIvEE) handles all specialized on_adapter methods implemented by the visitor.

The adapter implements get_type_info(), which can be used to determine the adapter directly or via is_type and as_type on any platform


Provides API to handle openvino Function attribute type, accessed as

[ValueAccessor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_value_accessor).- Parameters:
**name**– attribute name**adapter**– reference to a Function ValueAccessor<VAT>



-
inline virtual void on_adapter(const std::string &name,