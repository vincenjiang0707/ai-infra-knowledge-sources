source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_compress_float_constants_impl.html
lastmod: 

# Class ov::pass::CompressFloatConstantsImpl[#](https://docs.openvino.ai#class-ov-pass-compressfloatconstantsimpl)

-
class CompressFloatConstantsImpl : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass26CompressFloatConstantsImplE) [CompressFloatConstantsImpl](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_compress_float_constants_impl)transformation replaces FP32/FP64 Constants with FP16 ones.Public Functions

-
CompressFloatConstantsImpl(bool postponed = false)
[#](https://docs.openvino.ai#_CPPv4N2ov4pass26CompressFloatConstantsImpl26CompressFloatConstantsImplEb) Transformation constructor.

- Parameters:
**postponed**– If true then the transformation won’t compress the constants keeping them in the original type but still will insert Converts. This is a special mode of operation that requires another transformation to apply a real compression on constants. Constants eligible for postponed compression are marked with a special rt_info tag.


-
CompressFloatConstantsImpl(bool postponed = false)