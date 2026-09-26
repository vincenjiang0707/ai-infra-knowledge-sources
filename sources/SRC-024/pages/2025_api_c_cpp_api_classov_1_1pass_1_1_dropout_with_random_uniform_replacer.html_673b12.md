source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_dropout_with_random_uniform_replacer.html
lastmod: 

# Class ov::pass::DropoutWithRandomUniformReplacer[#](https://docs.openvino.ai#class-ov-pass-dropoutwithrandomuniformreplacer)

-
class DropoutWithRandomUniformReplacer : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass32DropoutWithRandomUniformReplacerE) This transformation replaces possible Dropout block (in inference mode) with RandomUniform to Broadcast of half-ones in a sub-graph.

Dropout block: RandomUniform ——-—> Add —> Floor /\ /\ /\ | | | Const(0) Const(1) Const(1) min_val max_val

Resulted block: Broadcast —-—> Add —> Floor /\ /\ | | Const(0.5) Const(1)