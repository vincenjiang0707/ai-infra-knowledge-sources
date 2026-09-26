source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_move_eltwise_up_through_data_mov_scalar.html
lastmod: 

# Class ov::pass::MoveEltwiseUpThroughDataMovScalar[#](https://docs.openvino.ai#class-ov-pass-moveeltwiseupthroughdatamovscalar)

-
class MoveEltwiseUpThroughDataMovScalar : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass33MoveEltwiseUpThroughDataMovScalarE) This transformation tries to put element-wise operations (Unary or Binary with scalar second input) before a set of data movement ops in order to allow further element-wise op fusion to previous op and zero-copy optimizations for data movement op itself. ┌───────────┐ ┌───────────┐ │ AnyOp │ │ AnyOp │ └─────┬─────┘ └─────┬─────┘ │ │ │ │ ┌───────┴────────┐ ┌───────┴────────┐ | DataMovementOp | => | Element-Wise | └───────┬────────┘ └───────┬────────┘ │ │ │ │ ┌───────┴────────┐ ┌───────┴────────┐ │ Element-Wise | │ DataMovementOp | └────────────────┘ └────────────────┘