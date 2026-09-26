source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_eliminate_loop_inputs_outputs.html
lastmod: 

# Class ov::pass::EliminateLoopInputsOutputs[#](https://docs.openvino.ai#class-ov-pass-eliminateloopinputsoutputs)

-
class EliminateLoopInputsOutputs : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass26EliminateLoopInputsOutputsE) [EliminateLoopInputsOutputs](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_eliminate_loop_inputs_outputs)transformation manages Loop inputs/outputs. Check if Loop input is not changed in body input node -> Loop input -> body parameter -> body result -> Loop output -> output node than: 1) reconnect input node -> output node directly 2) update Loop input description from merged to invariant.