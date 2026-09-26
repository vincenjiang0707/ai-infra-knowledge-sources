source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_convert_interpolate11_to_interpolate4.html
lastmod: 

# Class ov::pass::ConvertInterpolate11ToInterpolate4[#](https://docs.openvino.ai#class-ov-pass-convertinterpolate11tointerpolate4)

-
class ConvertInterpolate11ToInterpolate4 : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass34ConvertInterpolate11ToInterpolate4E) Converts Interpolate version 11 to Interpolate version 4 if the new op uses any of the v4 allowed interpolation modes.