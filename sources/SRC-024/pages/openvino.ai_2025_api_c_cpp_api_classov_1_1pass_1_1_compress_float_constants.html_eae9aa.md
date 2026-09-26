source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_compress_float_constants.html
lastmod: 

# Class ov::pass::CompressFloatConstants[#](https://docs.openvino.ai#class-ov-pass-compressfloatconstants)

-
class CompressFloatConstants : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[GraphRewrite](https://docs.openvino.ai/classov_1_1pass_1_1_graph_rewrite.html#_CPPv4N2ov4pass12GraphRewriteE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass22CompressFloatConstantsE) [CompressFloatConstants](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_compress_float_constants)transformation replaces FP32/FP64 Constants with FP16 ones.Public Functions

-
inline CompressFloatConstants(bool postponed = false)
[#](https://docs.openvino.ai#_CPPv4N2ov4pass22CompressFloatConstants22CompressFloatConstantsEb) Transformation constructor.

- Parameters:
**postponed**– Postponed compression, see[ov::pass::CompressFloatConstantsImpl](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_compress_float_constants_impl)for details.


-
inline CompressFloatConstants(bool postponed = false)