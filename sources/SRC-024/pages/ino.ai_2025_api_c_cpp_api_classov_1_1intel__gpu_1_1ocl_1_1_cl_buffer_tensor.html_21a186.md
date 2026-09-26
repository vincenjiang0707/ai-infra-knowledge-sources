source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1intel__gpu_1_1ocl_1_1_cl_buffer_tensor.html
lastmod: 

# Class ov::intel_gpu::ocl::ClBufferTensor[#](https://docs.openvino.ai#class-ov-intel-gpu-ocl-clbuffertensor)

-
class ClBufferTensor : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[RemoteTensor](https://docs.openvino.ai/classov_1_1_remote_tensor.html#_CPPv4N2ov12RemoteTensorE)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl14ClBufferTensorE) This class represents an abstraction for GPU plugin remote tensor which can be shared with user-supplied OpenCL buffer. The plugin object derived from this class can be obtained with

[ClContext::create_tensor()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__gpu_1_1ocl_1_1_cl_context_1ad9eb11f702e791114f2dc591a3abcb16)call.Note

User can obtain OpenCL buffer handle from this class.

Subclassed by

[ov::intel_gpu::ocl::D3DBufferTensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__gpu_1_1ocl_1_1_d3_d_buffer_tensor)Public Functions

-
inline cl_mem get()
[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl14ClBufferTensor3getEv) Returns the underlying OpenCL memory object handle.

- Returns:
underlying OpenCL memory object handle



-
inline operator cl_mem()
[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl14ClBufferTensorcv6cl_memEv) OpenCL memory handle conversion operator.

- Returns:
`cl_mem`



-
inline operator cl::Buffer()
[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl14ClBufferTensorcvN2cl6BufferEEv) Standard Khronos cl::Buffer wrapper conversion operator.

- Returns:
`cl::Buffer`

object


-
inline cl_mem get()