source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_chained_maximum_optimization.html
lastmod: 

# Class ov::pass::ChainedMaximumOptimization[#](https://docs.openvino.ai#class-ov-pass-chainedmaximumoptimization)

-
class ChainedMaximumOptimization : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass26ChainedMaximumOptimizationE) Optimizes graphs based on value symbols Maximum(Maximum(A, B), B) -> Maximum(A, B) Maximum(Maximum(A, B), A) -> Maximum(A, B)


Site Navigation

Section Navigation

Optimizes graphs based on value symbols Maximum(Maximum(A, B), B) -> Maximum(A, B) Maximum(Maximum(A, B), A) -> Maximum(A, B)