source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1frontend_1_1_f_w_visitor.html
lastmod: 

# Class ov::frontend::FWVisitor[#](https://docs.openvino.ai#class-ov-frontend-fwvisitor)

-
class FWVisitor : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[AttributeVisitor](https://docs.openvino.ai/classov_1_1_attribute_visitor.html#_CPPv4N2ov16AttributeVisitorE)[#](https://docs.openvino.ai#_CPPv4N2ov8frontend9FWVisitorE) Public Functions

-
inline virtual void on_adapter(const std::string &name,
[ValueAccessor](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov13ValueAccessorIvEE)<void> &adapter) override[#](https://docs.openvino.ai#_CPPv4N2ov8frontend9FWVisitor10on_adapterERKNSt6stringER13ValueAccessorIvE) handles all specialized on_adapter methods implemented by the visitor.

The adapter implements get_type_info(), which can be used to determine the adapter directly or via is_type and as_type on any platform


-
inline virtual void on_adapter(const std::string &name,