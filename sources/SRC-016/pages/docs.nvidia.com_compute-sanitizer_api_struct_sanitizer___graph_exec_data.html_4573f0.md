source: https://docs.nvidia.com/compute-sanitizer/api/struct_sanitizer___graph_exec_data.html

# Sanitizer_GraphExecData[#](https://docs.nvidia.com#sanitizer-graphexecdata)

-
struct Sanitizer_GraphExecData
[#](https://docs.nvidia.com#_CPPv423Sanitizer_GraphExecData) Data passed into a graphexec creation callback function.

Data passed into a graphs callback function as the

`cbdata`

argument to[Sanitizer_CallbackFunc](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i.html#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1gac1ae37612d036530e060f1bca8c3ccd8). The`cbdata`

will be this type for`domain`

equal to SANITIZER_CB_DOMAIN_GRAPHS and`cbid`

equal to SANITIZER_CBID_GRAPHS_GRAPHEXEC_CREATING. The callback data is only valid within the invocation of the callback function that is passed the data. If you need to retain some data for use outside of the callback, you must make a copy of it.Public Members

-
uint32_t containsDeviceGraphLaunches
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_GraphExecData27containsDeviceGraphLaunchesE) Boolean value indicating if the graphexec may launch device graphs.

Only valid in the SANITIZER_CBID_GRAPHS_GRAPHEXEC_CREATED callback with driver version of 535 or newer.


-
CUcontext deviceGraphLaunchesContext
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_GraphExecData26deviceGraphLaunchesContextE) Context where the graphexec can launch device graphs.

NULL if the graphExec doesn’t launch device graphs. Only valid in the SANITIZER_CBID_GRAPHS_GRAPHEXEC_CREATED callback with driver version of 535 or newer.


-
CUgraph graph
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_GraphExecData5graphE) CUDA graph being instantiated.


-
CUgraphExec graphExec
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_GraphExecData9graphExecE) Instance of the CUDA graph.

Can be NULL for device graph launches in the SANITIZER_CBID_GRAPHS_GRAPHEXEC_CREATING callback.


-
uint32_t isDeviceLaunch
[#](https://docs.nvidia.com#_CPPv4N23Sanitizer_GraphExecData14isDeviceLaunchE) Boolean value indicating if the graphexec is for a device graph launch.


-
uint32_t containsDeviceGraphLaunches