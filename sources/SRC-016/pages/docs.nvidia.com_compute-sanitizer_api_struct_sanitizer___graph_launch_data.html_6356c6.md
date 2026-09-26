source: https://docs.nvidia.com/compute-sanitizer/api/struct_sanitizer___graph_launch_data.html

# Sanitizer_GraphLaunchData[#](https://docs.nvidia.com#sanitizer-graphlaunchdata)

-
struct Sanitizer_GraphLaunchData
[#](https://docs.nvidia.com#_CPPv425Sanitizer_GraphLaunchData) Data passed into a graph launch callback function.

Data passed into a graphs callback function as the

`cbdata`

argument to[Sanitizer_CallbackFunc](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i.html#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1gac1ae37612d036530e060f1bca8c3ccd8). The`cbdata`

will be this type for`domain`

equal to SANITIZER_CB_DOMAIN_GRAPHS and`cbid`

equal to SANITIZER_CBID_GRAPHS_LAUNCH_BEGIN or SANITIZER_CBID_GRAPHS_LAUNCH_END. The callback data is only valid within the invocation of the callback function that is passed the data. If you need to retain some data for use outside of the callback, you must make a copy of it.Public Members

-
CUcontext context
[#](https://docs.nvidia.com#_CPPv4N25Sanitizer_GraphLaunchData7contextE) The context where the graph is launched.


-
CUgraphExec graphExec
[#](https://docs.nvidia.com#_CPPv4N25Sanitizer_GraphLaunchData9graphExecE) Instance of the CUDA graph being launched.


-
[Sanitizer_StreamHandle](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___s_t_r_e_a_m___a_p_i.html#_CPPv422Sanitizer_StreamHandle)hStream[#](https://docs.nvidia.com#_CPPv4N25Sanitizer_GraphLaunchData7hStreamE) Unique handle for the stream.


-
uint32_t isGraphUpload
[#](https://docs.nvidia.com#_CPPv4N25Sanitizer_GraphLaunchData13isGraphUploadE) Boolean value indicating if the launch callback is part of a graph upload.

This field is only valid if the driver version is 510 or newer.


-
CUstream stream
[#](https://docs.nvidia.com#_CPPv4N25Sanitizer_GraphLaunchData6streamE) The stream where the graph is launched.


-
CUcontext context