source: https://docs.nvidia.com/compute-sanitizer/api/struct_sanitizer___launch_data.html

# Sanitizer_LaunchData[#](https://docs.nvidia.com#sanitizer-launchdata)

-
struct Sanitizer_LaunchData
[#](https://docs.nvidia.com#_CPPv420Sanitizer_LaunchData) Data passed into a launch callback function.

Data passed into a launch callback function as the

`cbdata`

argument to[Sanitizer_CallbackFunc](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i.html#group___s_a_n_i_t_i_z_e_r___c_a_l_l_b_a_c_k___a_p_i_1gac1ae37612d036530e060f1bca8c3ccd8). The`cbdata`

will be this type for`domain`

equal to SANITIZER_CB_DOMAIN_LAUNCH. The callback data is only valid within the invocation of the callback function that is passed the data. If you need to retain some data for use outside of the callback, you must make a copy of it.Unnamed Group

-
uint32_t gridDim_x
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_LaunchData9gridDim_xE) Launch properties of the grid. These values are only valid for SANITIZER_CBID_LAUNCH_BEGIN and graph node launch callbacks


-
uint32_t gridDim_y
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_LaunchData9gridDim_yE)

-
uint32_t gridDim_z
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_LaunchData9gridDim_zE)

-
uint32_t blockDim_x
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_LaunchData10blockDim_xE)

-
uint32_t blockDim_y
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_LaunchData10blockDim_yE)

-
uint32_t blockDim_z
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_LaunchData10blockDim_zE)

-
uint32_t clusterDim_x
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_LaunchData12clusterDim_xE)

-
uint32_t clusterDim_y
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_LaunchData12clusterDim_yE)

-
uint32_t clusterDim_z
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_LaunchData12clusterDim_zE)

Public Members

-
CUcontext apiContext
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_LaunchData10apiContextE) Only valid for graph node launches.

This is the context of the stream used in the graph launch API call.


-
CUstream apiStream
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_LaunchData9apiStreamE) Only valid for graph node launches.

This is the stream used in the graph launch API call.


-
CUcontext context
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_LaunchData7contextE) The context where the grid is launched.

For graph node launches, this is the context in which the kernel will run.


-
CUdevice device
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_LaunchData6deviceE) The device where the grid is launched.


-
CUfunction function
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_LaunchData8functionE) The function of the grid launch.


-
const char *functionName
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_LaunchData12functionNameE) The name of the launched function.


-
uint64_t gridId
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_LaunchData6gridIdE) Unique identifier of the grid launch.

For graph node launches, this is only unique within the graphexec launch.


-
[Sanitizer_StreamHandle](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___s_t_r_e_a_m___a_p_i.html#_CPPv422Sanitizer_StreamHandle)hApiStream[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_LaunchData10hApiStreamE) Unique handle for the API stream.


-
[Sanitizer_LaunchHandle](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___p_a_t_c_h_i_n_g___a_p_i.html#_CPPv422Sanitizer_LaunchHandle)hLaunch[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_LaunchData7hLaunchE) Handle of the grid launch.

This is only valid between the launch begin and end callbacks.


-
[Sanitizer_StreamHandle](https://docs.nvidia.com/group___s_a_n_i_t_i_z_e_r___s_t_r_e_a_m___a_p_i.html#_CPPv422Sanitizer_StreamHandle)hStream[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_LaunchData7hStreamE) Unique handle for the stream.


-
CUmodule module
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_LaunchData6moduleE) The module containing the grid code.


-
uint32_t splitLaunchPart
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_LaunchData15splitLaunchPartE) Split launch part.

0 if the launch is not split.


-
CUstream stream
[#](https://docs.nvidia.com#_CPPv4N20Sanitizer_LaunchData6streamE) The stream where the grid is launched.


-
uint32_t gridDim_x