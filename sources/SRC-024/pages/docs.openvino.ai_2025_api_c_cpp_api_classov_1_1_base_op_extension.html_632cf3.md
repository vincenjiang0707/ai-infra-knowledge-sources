source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_base_op_extension.html
lastmod: 

# Class ov::BaseOpExtension[#](https://docs.openvino.ai#class-ov-baseopextension)

-
class BaseOpExtension : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Extension](https://docs.openvino.ai/classov_1_1_extension.html#_CPPv4N2ov9ExtensionE)[#](https://docs.openvino.ai#_CPPv4N2ov15BaseOpExtensionE) The base interface for OpenVINO operation extensions.

Subclassed by

[ov::OpExtension< T >](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_op_extension)Public Functions

-
virtual
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::OutputVector create(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::OutputVector &inputs,[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[AttributeVisitor](https://docs.openvino.ai/classov_1_1_attribute_visitor.html#_CPPv4N2ov16AttributeVisitorE)&visitor) const = 0[#](https://docs.openvino.ai#_CPPv4NK2ov15BaseOpExtension6createERKN2ov12OutputVectorERN2ov16AttributeVisitorE) Method creates an OpenVINO operation.

- Parameters:
**inputs**– vector of input ports**visitor**– attribute visitor which allows to read necessaty arguments

- Returns:
vector of output ports



-
virtual std::vector<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Extension](https://docs.openvino.ai/classov_1_1_extension.html#_CPPv4N2ov9ExtensionE)::Ptr> get_attached_extensions() const = 0[#](https://docs.openvino.ai#_CPPv4NK2ov15BaseOpExtension23get_attached_extensionsEv) Returns extensions that should be registered together with this extension class object.

Attached extensions may include frontend extensions that OpenVINO op to framework ops or necessary transformations that should be applied to the network which consist of target op.

- Returns:


-
virtual ~BaseOpExtension() override
[#](https://docs.openvino.ai#_CPPv4N2ov15BaseOpExtensionD0Ev) Destructor.


-
virtual