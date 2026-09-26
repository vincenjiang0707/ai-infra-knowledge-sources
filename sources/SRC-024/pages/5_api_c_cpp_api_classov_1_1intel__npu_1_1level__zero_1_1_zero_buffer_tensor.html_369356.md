source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1intel__npu_1_1level__zero_1_1_zero_buffer_tensor.html
lastmod: 

# Class ov::intel_npu::level_zero::ZeroBufferTensor[#](https://docs.openvino.ai#class-ov-intel-npu-level-zero-zerobuffertensor)

-
class ZeroBufferTensor : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[RemoteTensor](https://docs.openvino.ai/classov_1_1_remote_tensor.html#_CPPv4N2ov12RemoteTensorE)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_npu10level_zero16ZeroBufferTensorE) This class represents an abstraction for NPU plugin remote tensor which can be shared with user-supplied LevelZero buffer. The plugin object derived from this class can be obtained with

[ZeroContext::create_tensor()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__npu_1_1level__zero_1_1_zero_context_1a87ab3f0376e3f7699fba50ef8a4f9f68)call.Note

User can obtain Level Zero buffer handle from this class.

Public Functions

-
inline void *get()
[#](https://docs.openvino.ai#_CPPv4N2ov9intel_npu10level_zero16ZeroBufferTensor3getEv) Returns the underlying LevelZero memory object handle.

- Returns:
underlying void* memory object handle



-
inline void *get()