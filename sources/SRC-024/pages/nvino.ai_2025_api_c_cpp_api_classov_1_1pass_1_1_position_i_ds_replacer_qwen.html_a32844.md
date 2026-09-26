source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_position_i_ds_replacer_qwen.html
lastmod: 

# Class ov::pass::PositionIDsReplacerQwen[#](https://docs.openvino.ai#class-ov-pass-positionidsreplacerqwen)

-
class PositionIDsReplacerQwen : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass23PositionIDsReplacerQwenE) Qwen model expects data processing in order, the “position ids” input is detached and is not explicitly used in the model. The model uses implicitly defined “position ids” based on the past KV cache size.

To use this model in Continuous batching mode, we need to apply position_ids and use the corresponding rotary_emb_cos/rotary_emb_sin. For this, we replace rotary_emb_cos/rotary_emb_sin -> Slice -> Slice With rotary_emb_cos/rotary_emb_sin -> Gather(by position_ids) Which enables applying RoPE for each token independently of their order in the input tensor.