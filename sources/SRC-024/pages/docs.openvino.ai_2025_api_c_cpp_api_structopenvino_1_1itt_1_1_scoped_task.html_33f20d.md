source: https://docs.openvino.ai/2025/api/c_cpp_api/structopenvino_1_1itt_1_1_scoped_task.html
lastmod: 

# Class openvino::itt::ScopedTask[#](https://docs.openvino.ai#class-openvino-itt-scopedtask)

-
template<
[domain_t](https://docs.openvino.ai/group__ov__dev__profiling.html#_CPPv4N8openvino3itt8domain_tE)(*domain)()>

class ScopedTask[#](https://docs.openvino.ai#_CPPv4I_PF8domain_tvEEN8openvino3itt10ScopedTaskE) Used to annotate section of code which would be named at runtime.

Note

Uses ITT task begin/end. If a region is active on the current thread, tasks started within it are recorded as its children.

- Template Parameters:
**The**–`domain`

parameter is domain type which shoud be defined with[OV_ITT_DOMAIN()](https://docs.openvino.ai/group__ov__dev__profiling.html#group__ov__dev__profiling_1ga83ad6f539c8e1aef944160e37fcfcb4d)macro.

Public Functions

-
inline ScopedTask(
[handle_t](https://docs.openvino.ai/group__ov__dev__profiling.html#_CPPv4N8openvino3itt8handle_tE)taskHandle) noexcept[#](https://docs.openvino.ai#_CPPv4N8openvino3itt10ScopedTask10ScopedTaskE8handle_t) Construct

[ScopedTask](https://docs.openvino.ai#structopenvino_1_1itt_1_1_scoped_task)with defined annotation handle.

-
inline ~ScopedTask() noexcept
[#](https://docs.openvino.ai#_CPPv4N8openvino3itt10ScopedTaskD0Ev) The

[ScopedTask](https://docs.openvino.ai#structopenvino_1_1itt_1_1_scoped_task)destructor closes or ends the task scope.