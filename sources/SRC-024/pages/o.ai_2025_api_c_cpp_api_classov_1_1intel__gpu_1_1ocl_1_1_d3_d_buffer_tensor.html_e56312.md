source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1intel__gpu_1_1ocl_1_1_d3_d_buffer_tensor.html
lastmod: 

# Class ov::intel_gpu::ocl::D3DBufferTensor[#](https://docs.openvino.ai#class-ov-intel-gpu-ocl-d3dbuffertensor)

-
class D3DBufferTensor : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[intel_gpu](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9intel_gpuE)::[ocl](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9intel_gpu3oclE)::[ClBufferTensor](https://docs.openvino.ai/classov_1_1intel__gpu_1_1ocl_1_1_cl_buffer_tensor.html#_CPPv4N2ov9intel_gpu3ocl14ClBufferTensorE)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl15D3DBufferTensorE) This class represents an abstraction for GPU plugin remote tensor which is shared with Direct3D 11 buffer. The plugin object derived from this class can be obtained with

[D3DContext::create_tensor()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__gpu_1_1ocl_1_1_d3_d_context_1a20f1fdfe8e231908be276cec21253acc)call.Note

User can also obtain OpenCL buffer handle from this class.

Public Functions

-
inline operator ID3D11Buffer*()
[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl15D3DBufferTensorcvP12ID3D11BufferEv) ID3D11Buffer conversion operator for the

[D3DContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__gpu_1_1ocl_1_1_d3_d_context)object.- Returns:
Pointer to underlying ID3D11Buffer interface



-
inline operator ID3D11Buffer*()