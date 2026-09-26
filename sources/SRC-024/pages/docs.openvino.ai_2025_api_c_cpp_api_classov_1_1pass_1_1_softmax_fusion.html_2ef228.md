source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_softmax_fusion.html
lastmod: 

# Class ov::pass::SoftmaxFusion[#](https://docs.openvino.ai#class-ov-pass-softmaxfusion)

-
class SoftmaxFusion : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass13SoftmaxFusionE) [SoftmaxFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_softmax_fusion)transformation replaces following graphs:and +—————+ │ │ │ input │ │ │ +—————++---------------+ │ │ │ input │ │ │ +---------------+ │ │ │ v │ +-----------+ │ │ │ │ │ ReduceMax │ │ │ │ │ +-----------+ │ │ │ │ v v +---------------+ │ │ │ Sub │ │ │ +---------------+ | | v +---------------+ │ │ │ Exp │ │ │ +---------------+ │ │ │ v │ +-----------+ │ │ │ │ │ ReduceSum │ │ │ │ │ +-----------+ │ │ │ │ v v +-------------+ | │ | Div │ │ │ +-------------+


v +—————+ │ │ │ Exp │ │ │ +—————+ │ │ │ v │ +——–—+ │ │ │ │ │ ReduceSum │ │ │ │ │ +——–—+ │ │ │ │ v v +———-—+ | │ | Div │ │ │ +———-—+to a single Softmax node

Restrictions:

ReduceMax and ReduceSum axes must be scalar constants and they have to point to the same axis