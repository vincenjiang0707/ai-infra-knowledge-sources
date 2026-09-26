source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1gen__pattern_1_1detail_1_1_attr_setter.html
lastmod: 

# Class ov::gen_pattern::detail::AttrSetter[#](https://docs.openvino.ai#class-ov-gen-pattern-detail-attrsetter)

-
class AttrSetter : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[AttributeVisitor](https://docs.openvino.ai/classov_1_1_attribute_visitor.html#_CPPv4N2ov16AttributeVisitorE)[#](https://docs.openvino.ai#_CPPv4N2ov11gen_pattern6detail10AttrSetterE) Public Functions

-
inline virtual void on_adapter(const std::string &name,
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[ValueAccessor](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov13ValueAccessorIvEE)<void> &adapter) override[#](https://docs.openvino.ai#_CPPv4N2ov11gen_pattern6detail10AttrSetter10on_adapterERKNSt6stringERN2ov13ValueAccessorIvEE) handles all specialized on_adapter methods implemented by the visitor.

The adapter implements get_type_info(), which can be used to determine the adapter directly or via is_type and as_type on any platform


-
inline virtual void on_adapter(const std::string &name,