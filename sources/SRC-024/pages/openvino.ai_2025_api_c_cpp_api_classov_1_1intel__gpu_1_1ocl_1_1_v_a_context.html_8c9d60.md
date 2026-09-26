source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1intel__gpu_1_1ocl_1_1_v_a_context.html
lastmod: 

# Class ov::intel_gpu::ocl::VAContext[#](https://docs.openvino.ai#class-ov-intel-gpu-ocl-vacontext)

-
class VAContext : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[intel_gpu](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9intel_gpuE)::[ocl](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9intel_gpu3oclE)::[ClContext](https://docs.openvino.ai/classov_1_1intel__gpu_1_1ocl_1_1_cl_context.html#_CPPv4N2ov9intel_gpu3ocl9ClContextE)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl9VAContextE) This class represents an abstraction for GPU plugin remote context which is shared with VA display object. The plugin object derived from this class can be obtained either with

[CompiledModel::get_context()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model_1a22c5537d4c7182072d327077c386b01a)or[Core::create_context()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1ab9a3eef07c3471037070242f8da2fb01)calls.Note

User can also obtain OpenCL context handle from this class.

Public Functions

-
inline operator VADisplay()
[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl9VAContextcv9VADisplayEv) `VADisplay`

conversion operator for the[VAContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__gpu_1_1ocl_1_1_v_a_context)object.- Returns:
Underlying

`VADisplay`

object handle


-
inline VAContext(
[Core](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4N2ov4CoreE)&core, VADisplay device, int target_tile_id = -1)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl9VAContext9VAContextER4Core9VADisplayi) Constructs remote context object from VA display handle.

- Parameters:
**core**– OpenVINO Runtime[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)object**device**– A`VADisplay`

to create remote context from**target_tile_id**– Desired tile id within given context for multi-tile system. Default value (-1) means that root device should be used



-
inline std::pair<
[VASurfaceTensor](https://docs.openvino.ai/classov_1_1intel__gpu_1_1ocl_1_1_v_a_surface_tensor.html#_CPPv4N2ov9intel_gpu3ocl15VASurfaceTensorE),[VASurfaceTensor](https://docs.openvino.ai/classov_1_1intel__gpu_1_1ocl_1_1_v_a_surface_tensor.html#_CPPv4N2ov9intel_gpu3ocl15VASurfaceTensorE)> create_tensor_nv12(const size_t height, const size_t width, const VASurfaceID nv12_surf)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl9VAContext18create_tensor_nv12EK6size_tK6size_tK11VASurfaceID) This function is used to obtain a NV12 tensor from NV12 VA decoder output. The resulting tensor contains two remote tensors for Y and UV planes of the surface.

- Parameters:
**height**– A height of Y plane**width**– A width of Y plane**nv12_surf**– NV12`VASurfaceID`

to create NV12 from

- Returns:
A pair of remote tensors for each plane



-
inline
[VASurfaceTensor](https://docs.openvino.ai/classov_1_1intel__gpu_1_1ocl_1_1_v_a_surface_tensor.html#_CPPv4N2ov9intel_gpu3ocl15VASurfaceTensorE)create_tensor(const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape, const VASurfaceID surface, const uint32_t plane = 0)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl9VAContext13create_tensorEKN7element4TypeERK5ShapeK11VASurfaceIDK8uint32_t) This function is used to create remote tensor from VA surface handle.


-
inline
[ClBufferTensor](https://docs.openvino.ai/classov_1_1intel__gpu_1_1ocl_1_1_cl_buffer_tensor.html#_CPPv4N2ov9intel_gpu3ocl14ClBufferTensorE)create_tensor(const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape, const cl_mem buffer)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl9VAContext13create_tensorEKN7element4TypeERK5ShapeK6cl_mem) This function is used to obtain remote tensor object from user-supplied cl_mem object.


-
inline
[ClBufferTensor](https://docs.openvino.ai/classov_1_1intel__gpu_1_1ocl_1_1_cl_buffer_tensor.html#_CPPv4N2ov9intel_gpu3ocl14ClBufferTensorE)create_tensor(const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape, const cl::Buffer &buffer)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl9VAContext13create_tensorEKN7element4TypeERK5ShapeRKN2cl6BufferE) This function is used to obtain remote tensor object from user-supplied cl::Buffer object.


-
inline
[ClImage2DTensor](https://docs.openvino.ai/classov_1_1intel__gpu_1_1ocl_1_1_cl_image2_d_tensor.html#_CPPv4N2ov9intel_gpu3ocl15ClImage2DTensorE)create_tensor(const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape, const cl::Image2D &image)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl9VAContext13create_tensorEKN7element4TypeERK5ShapeRKN2cl7Image2DE) This function is used to obtain remote tensor object from user-supplied cl::Image2D object.


-
inline
[USMTensor](https://docs.openvino.ai/classov_1_1intel__gpu_1_1ocl_1_1_u_s_m_tensor.html#_CPPv4N2ov9intel_gpu3ocl9USMTensorE)create_tensor(const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape, void *usm_ptr)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl9VAContext13create_tensorEKN7element4TypeERK5ShapePv) This function is used to obtain remote tensor object from user-supplied USM pointer.


-
[RemoteTensor](https://docs.openvino.ai/classov_1_1_remote_tensor.html#_CPPv4N2ov12RemoteTensorE)create_tensor(const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape, const AnyMap ¶ms = {})[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl9VAContext13create_tensorERKN7element4TypeERK5ShapeRK6AnyMap) Allocates memory tensor in device memory or wraps user-supplied memory handle using the specified tensor description and low-level device-specific parameters. Returns a pointer to the object that implements the

[RemoteTensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_tensor)interface.- Parameters:
**type**– Defines the element type of the tensor.**shape**– Defines the shape of the tensor.**params**– Map of the low-level tensor object parameters.

- Returns:
Pointer to a plugin object that implements the

[RemoteTensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_tensor)interface.


Public Static Functions

-
static inline void type_check(const
[RemoteContext](https://docs.openvino.ai/classov_1_1_remote_context.html#_CPPv4N2ov13RemoteContextE)&remote_context)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl9VAContext10type_checkERK13RemoteContext) Checks that type defined runtime parameters are presented in remote object.

- Parameters:
**remote_context**– A remote context to check


-
inline operator VADisplay()