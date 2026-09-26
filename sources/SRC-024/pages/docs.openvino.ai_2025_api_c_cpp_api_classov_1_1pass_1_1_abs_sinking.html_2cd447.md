source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_abs_sinking.html
lastmod: 

# Class ov::pass::AbsSinking[#](https://docs.openvino.ai#class-ov-pass-abssinking)

-
class AbsSinking : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass10AbsSinkingE) [AbsSinking](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_abs_sinking)optimizes out the Abs which input is non negative. Has a special case for Concat -> Abs graph, it moves Abs up through Concat to its inputs, tries to constant fold new Abs ops. In case folding fails applies optimization to the leftover Abs ops.