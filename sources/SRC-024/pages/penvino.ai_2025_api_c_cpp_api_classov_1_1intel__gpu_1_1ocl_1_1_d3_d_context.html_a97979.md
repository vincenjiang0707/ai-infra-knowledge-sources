source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1intel__gpu_1_1ocl_1_1_d3_d_context.html
lastmod: 

# Class ov::intel_gpu::ocl::D3DContext[#](https://docs.openvino.ai#class-ov-intel-gpu-ocl-d3dcontext)

-
class D3DContext : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[intel_gpu](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9intel_gpuE)::[ocl](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9intel_gpu3oclE)::[ClContext](https://docs.openvino.ai/classov_1_1intel__gpu_1_1ocl_1_1_cl_context.html#_CPPv4N2ov9intel_gpu3ocl9ClContextE)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl10D3DContextE) This class represents an abstraction for GPU plugin remote context which is shared with Direct3D 11 device. The plugin object derived from this class can be obtained either with

[CompiledModel::get_context()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model_1a22c5537d4c7182072d327077c386b01a)or[Core::create_context()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1ab9a3eef07c3471037070242f8da2fb01)calls.Note

User can also obtain OpenCL context handle from this class.

Public Functions

-
inline operator ID3D11Device*()
[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl10D3DContextcvP12ID3D11DeviceEv) ID3D11Device conversion operator for the

[D3DContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__gpu_1_1ocl_1_1_d3_d_context)object.- Returns:
Pointer to underlying ID3D11Device interface



-
inline D3DContext(
[Core](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4N2ov4CoreE)&core, ID3D11Device *device, int target_tile_id = -1)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl10D3DContext10D3DContextER4CoreP12ID3D11Devicei) Constructs

[D3DContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__gpu_1_1ocl_1_1_d3_d_context)remote context object from ID3D11Device.- Parameters:
**core**– OpenVINO Runtime[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)object instance**device**– A pointer to ID3D11Device to be used to create a remote context**target_tile_id**– Desired tile id within given context for multi-tile system. Default value (-1) means that root device should be used



-
inline std::pair<
[D3DSurface2DTensor](https://docs.openvino.ai/classov_1_1intel__gpu_1_1ocl_1_1_d3_d_surface2_d_tensor.html#_CPPv4N2ov9intel_gpu3ocl18D3DSurface2DTensorE),[D3DSurface2DTensor](https://docs.openvino.ai/classov_1_1intel__gpu_1_1ocl_1_1_d3_d_surface2_d_tensor.html#_CPPv4N2ov9intel_gpu3ocl18D3DSurface2DTensorE)> create_tensor_nv12(const size_t height, const size_t width, ID3D11Texture2D *nv12_surf)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl10D3DContext18create_tensor_nv12EK6size_tK6size_tP15ID3D11Texture2D) This function is used to obtain a NV12 tensor from NV12 DXGI video decoder output. The resulting tensor contains two remote tensors for Y and UV planes of the surface.

- Parameters:
**height**– Height of Y plane**width**– Width of Y plane**nv12_surf**– A ID3D11Texture2D instance to create NV12 tensor from

- Returns:
A pair of remote tensors for each plane



-
inline
[D3DBufferTensor](https://docs.openvino.ai/classov_1_1intel__gpu_1_1ocl_1_1_d3_d_buffer_tensor.html#_CPPv4N2ov9intel_gpu3ocl15D3DBufferTensorE)create_tensor(const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape, ID3D11Buffer *buffer)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl10D3DContext13create_tensorEKN7element4TypeERK5ShapeP12ID3D11Buffer) This function is used to obtain remote tensor object from ID3D11Buffer.


-
inline
[D3DSurface2DTensor](https://docs.openvino.ai/classov_1_1intel__gpu_1_1ocl_1_1_d3_d_surface2_d_tensor.html#_CPPv4N2ov9intel_gpu3ocl18D3DSurface2DTensorE)create_tensor(const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape, ID3D11Texture2D *surface, uint32_t plane = 0)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl10D3DContext13create_tensorEKN7element4TypeERK5ShapeP15ID3D11Texture2D8uint32_t) This function is used to obtain remote tensor object from ID3D11Texture2D.

Note

The underlying ID3D11Texture2D can also be a plane of output surface of DXGI video decoder

- Parameters:
- Returns:
[D3DSurface2DTensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__gpu_1_1ocl_1_1_d3_d_surface2_d_tensor)tensor


-
inline
[ClBufferTensor](https://docs.openvino.ai/classov_1_1intel__gpu_1_1ocl_1_1_cl_buffer_tensor.html#_CPPv4N2ov9intel_gpu3ocl14ClBufferTensorE)create_tensor(const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape, const cl_mem buffer)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl10D3DContext13create_tensorEKN7element4TypeERK5ShapeK6cl_mem) This function is used to obtain remote tensor object from user-supplied cl_mem object.


-
inline
[ClBufferTensor](https://docs.openvino.ai/classov_1_1intel__gpu_1_1ocl_1_1_cl_buffer_tensor.html#_CPPv4N2ov9intel_gpu3ocl14ClBufferTensorE)create_tensor(const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape, const cl::Buffer &buffer)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl10D3DContext13create_tensorEKN7element4TypeERK5ShapeRKN2cl6BufferE) This function is used to obtain remote tensor object from user-supplied cl::Buffer object.


-
inline
[ClImage2DTensor](https://docs.openvino.ai/classov_1_1intel__gpu_1_1ocl_1_1_cl_image2_d_tensor.html#_CPPv4N2ov9intel_gpu3ocl15ClImage2DTensorE)create_tensor(const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape, const cl::Image2D &image)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl10D3DContext13create_tensorEKN7element4TypeERK5ShapeRKN2cl7Image2DE) This function is used to obtain remote tensor object from user-supplied cl::Image2D object.


Public Static Functions

-
static inline void type_check(const
[RemoteContext](https://docs.openvino.ai/classov_1_1_remote_context.html#_CPPv4N2ov13RemoteContextE)&remote_context)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl10D3DContext10type_checkERK13RemoteContext) Checks that type defined runtime parameters are presented in remote object.

- Parameters:
**remote_context**– A remote context to check


-
inline operator ID3D11Device*()