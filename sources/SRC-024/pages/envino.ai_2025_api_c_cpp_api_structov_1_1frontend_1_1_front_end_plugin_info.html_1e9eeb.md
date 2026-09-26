source: https://docs.openvino.ai/2025/api/c_cpp_api/structov_1_1frontend_1_1_front_end_plugin_info.html
lastmod: 

# Struct ov::frontend::FrontEndPluginInfo[#](https://docs.openvino.ai#struct-ov-frontend-frontendplugininfo)

-
struct FrontEndPluginInfo
[#](https://docs.openvino.ai#_CPPv4N2ov8frontend18FrontEndPluginInfoE) Each frontend plugin is responsible to export get_front_end_data function returning heap-allocated pointer to this structure. Will be used by

[FrontEndManager](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_front_end_manager)during loading of plugins.