source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1transpose__sinking_1_1_t_s_data_movement_backward.html
lastmod: 

# Class ov::pass::transpose_sinking::TSDataMovementBackward[#](https://docs.openvino.ai#class-ov-pass-transpose-sinking-tsdatamovementbackward)

-
class TSDataMovementBackward : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass17transpose_sinking22TSDataMovementBackwardE) [TSDataMovementBackward](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1transpose__sinking_1_1_t_s_data_movement_backward)transformation sinks Transpose through BatchToSpace, SpaceToBatch, ReverseSequence and Pad operations in the backward direction. These operations are categorized as “DataMovement” and are handled in a similar way in this transformation.