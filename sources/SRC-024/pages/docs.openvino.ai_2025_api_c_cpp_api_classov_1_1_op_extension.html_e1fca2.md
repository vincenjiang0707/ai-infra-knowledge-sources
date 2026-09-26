source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_op_extension.html
lastmod: 

# Class ov::OpExtension[#](https://docs.openvino.ai#class-ov-opextension)

-
template<class T>

class OpExtension : public[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[BaseOpExtension](https://docs.openvino.ai/classov_1_1_base_op_extension.html#_CPPv4N2ov15BaseOpExtensionE)[#](https://docs.openvino.ai#_CPPv4I0EN2ov11OpExtensionE) The default implementation of OpenVINO operation extensions.

Public Functions

-
inline OpExtension()
[#](https://docs.openvino.ai#_CPPv4N2ov11OpExtension11OpExtensionEv) Default constructor.


-
inline virtual
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::OutputVector create(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::OutputVector &inputs,[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[AttributeVisitor](https://docs.openvino.ai/classov_1_1_attribute_visitor.html#_CPPv4N2ov16AttributeVisitorE)&visitor) const override[#](https://docs.openvino.ai#_CPPv4NK2ov11OpExtension6createERKN2ov12OutputVectorERN2ov16AttributeVisitorE) Method creates an OpenVINO operation.

- Parameters:
**inputs**– vector of input ports**visitor**– attribute visitor which allows to read necessaty arguments

- Returns:
vector of output ports



-
inline virtual std::vector<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Extension](https://docs.openvino.ai/classov_1_1_extension.html#_CPPv4N2ov9ExtensionE)::Ptr> get_attached_extensions() const override[#](https://docs.openvino.ai#_CPPv4NK2ov11OpExtension23get_attached_extensionsEv) Returns extensions that should be registered together with this extension class object.

Attached extensions may include frontend extensions that OpenVINO op to framework ops or necessary transformations that should be applied to the network which consist of target op.

- Returns:


-
inline OpExtension()