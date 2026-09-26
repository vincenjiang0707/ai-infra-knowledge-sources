source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1intel__npu_1_1level__zero_1_1_zero_context.html
lastmod: 

# Class ov::intel_npu::level_zero::ZeroContext[#](https://docs.openvino.ai#class-ov-intel-npu-level-zero-zerocontext)

-
class ZeroContext : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[RemoteContext](https://docs.openvino.ai/classov_1_1_remote_context.html#_CPPv4N2ov13RemoteContextE)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_npu10level_zero11ZeroContextE) This class represents an abstraction for NPU plugin remote context which is shared with LevelZero context object. The plugin object derived from this class can be obtained either with

[CompiledModel::get_context()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model_1a22c5537d4c7182072d327077c386b01a)or[Core::create_context()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1ab9a3eef07c3471037070242f8da2fb01)calls.Public Functions

-
inline ZeroContext(
[Core](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4N2ov4CoreE)&core)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_npu10level_zero11ZeroContext11ZeroContextER4Core) Constructs context object from user-supplied LevelZero context handle.

- Parameters:
**core**– A reference to OpenVINO Runtime[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)object


-
inline void *get()
[#](https://docs.openvino.ai#_CPPv4N2ov9intel_npu10level_zero11ZeroContext3getEv) Returns the underlying LevelZero context handle.

- Returns:
`void*`



-
inline
[ZeroBufferTensor](https://docs.openvino.ai/classov_1_1intel__npu_1_1level__zero_1_1_zero_buffer_tensor.html#_CPPv4N2ov9intel_npu10level_zero16ZeroBufferTensorE)create_tensor(const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape, void *buffer)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_npu10level_zero11ZeroContext13create_tensorEKN7element4TypeERK5ShapePv) This function is used to obtain remote tensor object from user-supplied NT handle object.


-
inline
[ZeroBufferTensor](https://docs.openvino.ai/classov_1_1intel__npu_1_1level__zero_1_1_zero_buffer_tensor.html#_CPPv4N2ov9intel_npu10level_zero16ZeroBufferTensorE)create_tensor(const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape, int fd)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_npu10level_zero11ZeroContext13create_tensorEKN7element4TypeERK5Shapei) This function is used to obtain remote tensor object from user-supplied DMA-BUF System Heap object.


-
inline
[ZeroBufferTensor](https://docs.openvino.ai/classov_1_1intel__npu_1_1level__zero_1_1_zero_buffer_tensor.html#_CPPv4N2ov9intel_npu10level_zero16ZeroBufferTensorE)create_tensor(const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape, const[FileDescriptor](https://docs.openvino.ai/structov_1_1intel__npu_1_1_file_descriptor.html#_CPPv4N2ov9intel_npu14FileDescriptorE)&file_descriptor, const[TensorType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9intel_npu10TensorTypeE)tensor_type =[TensorType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9intel_npu10TensorTypeE)::[INPUT](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9intel_npu10TensorType5INPUTE))[#](https://docs.openvino.ai#_CPPv4N2ov9intel_npu10level_zero11ZeroContext13create_tensorEKN7element4TypeERK5ShapeRK14FileDescriptorK10TensorType) This function is used to obtain remote tensor object from a file.


-
inline
[ZeroBufferTensor](https://docs.openvino.ai/classov_1_1intel__npu_1_1level__zero_1_1_zero_buffer_tensor.html#_CPPv4N2ov9intel_npu10level_zero16ZeroBufferTensorE)create_l0_host_tensor(const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape, const[TensorType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9intel_npu10TensorTypeE)tensor_type =[TensorType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9intel_npu10TensorTypeE)::[BINDED](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9intel_npu10TensorType6BINDEDE))[#](https://docs.openvino.ai#_CPPv4N2ov9intel_npu10level_zero11ZeroContext21create_l0_host_tensorEKN7element4TypeERK5ShapeK10TensorType) This function is used to obtain remote tensor object.


-
[RemoteTensor](https://docs.openvino.ai/classov_1_1_remote_tensor.html#_CPPv4N2ov12RemoteTensorE)create_tensor(const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape, const AnyMap ¶ms = {})[#](https://docs.openvino.ai#_CPPv4N2ov9intel_npu10level_zero11ZeroContext13create_tensorERKN7element4TypeERK5ShapeRK6AnyMap) Allocates memory tensor in device memory or wraps user-supplied memory handle using the specified tensor description and low-level device-specific parameters. Returns a pointer to the object that implements the

[RemoteTensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_tensor)interface.- Parameters:
**type**– Defines the element type of the tensor.**shape**– Defines the shape of the tensor.**params**– Map of the low-level tensor object parameters.

- Returns:
Pointer to a plugin object that implements the

[RemoteTensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_tensor)interface.


-
inline ZeroContext(