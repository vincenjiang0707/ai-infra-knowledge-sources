source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_mark_rope_inputs_to_keep_in_mixed_precision.html
lastmod: 

# Class ov::pass::MarkRopeInputsToKeepInMixedPrecision[#](https://docs.openvino.ai#class-ov-pass-markropeinputstokeepinmixedprecision)

-
class MarkRopeInputsToKeepInMixedPrecision : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass36MarkRopeInputsToKeepInMixedPrecisionE) This transformation markups the 2nd/3rd inputs of Rope with FP32 to mantian accuracy. +—-—+ +—-—+ +—-—+ |intput1| |input2 | |input3 | |(orig) | |(fp32) | |(fp32) | +—|—+ +—|—+ +—|—+.


| | | ROPE | +—————————-—++—+————

————+—+