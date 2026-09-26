source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1intel__gpu_1_1ocl_1_1_u_s_m_tensor.html
lastmod: 

# Class ov::intel_gpu::ocl::USMTensor[#](https://docs.openvino.ai#class-ov-intel-gpu-ocl-usmtensor)

-
class USMTensor : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[RemoteTensor](https://docs.openvino.ai/classov_1_1_remote_tensor.html#_CPPv4N2ov12RemoteTensorE)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl9USMTensorE) This class represents an abstraction for GPU plugin remote tensor which can be shared with user-supplied USM device pointer. The plugin object derived from this class can be obtained with

[ClContext::create_tensor()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__gpu_1_1ocl_1_1_cl_context_1ad9eb11f702e791114f2dc591a3abcb16)call.Note

User can obtain USM pointer from this class.

Public Functions

-
inline void *get()
[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl9USMTensor3getEv) Returns the underlying USM pointer.

- Returns:
underlying USM pointer



-
inline void *get()