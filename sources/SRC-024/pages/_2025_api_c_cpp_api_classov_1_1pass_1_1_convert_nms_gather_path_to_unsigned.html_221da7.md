source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_convert_nms_gather_path_to_unsigned.html
lastmod: 

# Class ov::pass::ConvertNmsGatherPathToUnsigned[#](https://docs.openvino.ai#class-ov-pass-convertnmsgatherpathtounsigned)

-
class ConvertNmsGatherPathToUnsigned : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[GraphRewrite](https://docs.openvino.ai/classov_1_1pass_1_1_graph_rewrite.html#_CPPv4N2ov4pass12GraphRewriteE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass30ConvertNmsGatherPathToUnsignedE) Converts Gather indices to unsigned if indices are from NMS selected indices output. NMS returns -1 for not selected boxes, old version of Gather fill corresponding output for such indices with zero. But new Gather-8 has support of negative indices indicating counting from the end. In order to keep such behaviour (until dynamism is not supported) instead of -1 new Gather-8 will accept UINT32_MAX which is always outside of the bounds and corresponding output for such indices in gather always will be filled with zeros.