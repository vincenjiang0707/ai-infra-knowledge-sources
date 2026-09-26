source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1intel__gpu_1_1ocl_1_1_d3_d_surface2_d_tensor.html
lastmod: 

# Class ov::intel_gpu::ocl::D3DSurface2DTensor[#](https://docs.openvino.ai#class-ov-intel-gpu-ocl-d3dsurface2dtensor)

-
class D3DSurface2DTensor : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[intel_gpu](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9intel_gpuE)::[ocl](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9intel_gpu3oclE)::[ClImage2DTensor](https://docs.openvino.ai/classov_1_1intel__gpu_1_1ocl_1_1_cl_image2_d_tensor.html#_CPPv4N2ov9intel_gpu3ocl15ClImage2DTensorE)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl18D3DSurface2DTensorE) This class represents an abstraction for GPU plugin remote tensor which is shared with Direct3D 11 2D texture. The plugin object derived from this class can be obtained with

[D3DContext::create_tensor()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__gpu_1_1ocl_1_1_d3_d_context_1a20f1fdfe8e231908be276cec21253acc)call.Note

User can also obtain OpenCL 2D image handle from this class.

Public Functions

-
inline operator ID3D11Texture2D*()
[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl18D3DSurface2DTensorcvP15ID3D11Texture2DEv) ID3D11Texture2D conversion operator for the

[D3DContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__gpu_1_1ocl_1_1_d3_d_context)object.- Returns:
Pointer to underlying ID3D11Texture2D interface



-
inline uint32_t plane()
[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl18D3DSurface2DTensor5planeEv) Returns plane ID of underlying video decoder surface, or 0 if no video surface was shared.

- Returns:
Plane ID



-
inline operator ID3D11Texture2D*()