source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_m_v_n_fusion_without_constants.html
lastmod: 

# Class ov::pass::MVNFusionWithoutConstants[#](https://docs.openvino.ai#class-ov-pass-mvnfusionwithoutconstants)

-
class MVNFusionWithoutConstants : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass25MVNFusionWithoutConstantsE) [MVNFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_m_v_n_fusion)transformation replaces group of operations: (x - ReduceMean(x, axes)) / (Sqrt(ReduceMean((x - ReduceMean(x, axes)) ^ 2)) + eps) to MVN op.