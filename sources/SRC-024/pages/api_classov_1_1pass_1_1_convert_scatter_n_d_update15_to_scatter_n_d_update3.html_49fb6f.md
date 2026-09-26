source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_convert_scatter_n_d_update15_to_scatter_n_d_update3.html
lastmod: 

# Class ov::pass::ConvertScatterNDUpdate15ToScatterNDUpdate3[#](https://docs.openvino.ai#class-ov-pass-convertscatterndupdate15toscatterndupdate3)

-
class ConvertScatterNDUpdate15ToScatterNDUpdate3 : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass42ConvertScatterNDUpdate15ToScatterNDUpdate3E) Converts ScatterNDUpdate version 15 to ScatterNDUpdate version 3 if ScatterNDUpdate reduction attribute is set to None.