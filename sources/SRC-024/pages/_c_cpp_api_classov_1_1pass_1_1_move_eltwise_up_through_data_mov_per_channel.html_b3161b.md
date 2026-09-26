source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_move_eltwise_up_through_data_mov_per_channel.html
lastmod: 

# Class ov::pass::MoveEltwiseUpThroughDataMovPerChannel[#](https://docs.openvino.ai#class-ov-pass-moveeltwiseupthroughdatamovperchannel)

-
class MoveEltwiseUpThroughDataMovPerChannel : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass37MoveEltwiseUpThroughDataMovPerChannelE) This transformation tries to put element-wise operations before Reshape/Squeeze/Unsqueeze ops when second input to eltwise is per-channel Constant op ┌───────────┐ ┌────────────────┐ ┌───────────┐ ┌────────────────────┐ │ AnyOp │ │ TargetShape │ │ AnyOp │ │ Per-Channel Const │ └─────┬─────┘ └────────┬───────┘ └─────┬─────┘ └─────────┬──────────┘ │ │ │ │ │ | │ | │ ┌─────────┐ │ │ ┌──────────────┐ │ └───┤ Reshape ├────────┘ => └───┤ Element-Wise ├─────────┘ └────┬────┘ └───────┬──────┘ │ │ │ │ ┌───────┴────────┐ ┌────────────────────┐ ┌─────┴─────┐ ┌─────────────┐ │ Element-Wise ├────┤ Per-Channel Const │ │ Reshape ├────┤ TargetShape │ └────────────────┘ └────────────────────┘ └───────────┘ └─────────────┘