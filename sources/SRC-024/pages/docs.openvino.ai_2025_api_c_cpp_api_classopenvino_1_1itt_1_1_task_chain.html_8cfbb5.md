source: https://docs.openvino.ai/2025/api/c_cpp_api/classopenvino_1_1itt_1_1_task_chain.html
lastmod: 

# Class openvino::itt::TaskChain[#](https://docs.openvino.ai#class-openvino-itt-taskchain)

-
template<
[domain_t](https://docs.openvino.ai/group__ov__dev__profiling.html#_CPPv4N8openvino3itt8domain_tE)(*domain)()>

class TaskChain[#](https://docs.openvino.ai#_CPPv4I_PF8domain_tvEEN8openvino3itt9TaskChainE) Used to annotate a sequence of sections of code which would be named at runtime.

- Template Parameters:
**The**–`domain`

parameter is domain type which shoud be defined with[OV_ITT_DOMAIN()](https://docs.openvino.ai/group__ov__dev__profiling.html#group__ov__dev__profiling_1ga83ad6f539c8e1aef944160e37fcfcb4d)macro.