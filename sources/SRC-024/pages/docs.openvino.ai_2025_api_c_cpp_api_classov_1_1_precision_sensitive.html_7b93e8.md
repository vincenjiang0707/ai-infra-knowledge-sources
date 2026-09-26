source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_precision_sensitive.html
lastmod: 

# Class ov::PrecisionSensitive[#](https://docs.openvino.ai#class-ov-precisionsensitive)

-
class PrecisionSensitive : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[RuntimeAttribute](https://docs.openvino.ai/classov_1_1_runtime_attribute.html#_CPPv4N2ov16RuntimeAttributeE)[#](https://docs.openvino.ai#_CPPv4N2ov18PrecisionSensitiveE) [PrecisionSensitive](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_precision_sensitive)class represents runtime info attribute that marks input to an operation as a precision sensitive and disables compression to FP16 of the subgraph before this input.