source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_disable_f_p16_compression.html
lastmod: 

# Class ov::DisableFP16Compression[#](https://docs.openvino.ai#class-ov-disablefp16compression)

-
class DisableFP16Compression : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[RuntimeAttribute](https://docs.openvino.ai/classov_1_1_runtime_attribute.html#_CPPv4N2ov16RuntimeAttributeE)[#](https://docs.openvino.ai#_CPPv4N2ov22DisableFP16CompressionE) [DisableFP16Compression](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_disable_f_p16_compression)class represents runtime info attribute that marks operation as prohibited to convert to lower precision (e.g. to FP16) and they should be inferred precisely in the original precision.