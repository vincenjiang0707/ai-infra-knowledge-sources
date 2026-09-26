source: https://docs.openvino.ai/2025/api/c_cpp_api/group__ov__runtime__ocl__gpu__cpp__api.html
lastmod: 

# Group Intel GPU OpenCL interoperability[#](https://docs.openvino.ai#group-intel-gpu-opencl-interoperability)

-
*group*Intel GPU OpenCL interoperability Set of C++ classes and properties to work with Remote API for Intel GPU OpenCL plugin.

Typedefs

-
using gpu_handle_param = void*
[#](https://docs.openvino.ai#_CPPv416gpu_handle_param) Shortcut for defining a handle parameter.


Enums

-
enum class ContextType
[#](https://docs.openvino.ai#_CPPv411ContextType) Enum to define the type of the shared context.

*Values:*-
enumerator OCL
[#](https://docs.openvino.ai#_CPPv4N11ContextType3OCLE) Pure OpenCL context.


-
enumerator VA_SHARED
[#](https://docs.openvino.ai#_CPPv4N11ContextType9VA_SHAREDE) Context shared with a video decoding device.


-
enumerator OCL

Enum to define the type of the shared memory buffer.

*Values:*Shared OpenCL buffer blob.


Shared OpenCL 2D image blob.


Shared USM pointer allocated by user.


Shared USM pointer type with host allocation type allocated by plugin.


Shared USM pointer type with device allocation type allocated by plugin.


Shared video decoder surface or D3D 2D texture blob.


Shared D3D buffer blob.



Variables

-
static constexpr Property<
[ContextType](https://docs.openvino.ai#_CPPv411ContextType)> context_type = {"CONTEXT_TYPE"}[#](https://docs.openvino.ai#_CPPv412context_type) Shared device context type: can be either pure OpenCL (OCL) or shared video decoder (VA_SHARED) context.


-
static constexpr Property<
[gpu_handle_param](https://docs.openvino.ai#_CPPv416gpu_handle_param)> ocl_context = {"OCL_CONTEXT"}[#](https://docs.openvino.ai#_CPPv411ocl_context) This key identifies OpenCL context handle in a shared context or shared memory blob parameter map.


-
static constexpr Property<int> ocl_context_device_id = {"OCL_CONTEXT_DEVICE_ID"}
[#](https://docs.openvino.ai#_CPPv421ocl_context_device_id) This key identifies ID of device in OpenCL context if multiple devices are present in the context.


-
static constexpr Property<int> tile_id = {"TILE_ID"}
[#](https://docs.openvino.ai#_CPPv47tile_id) In case of multi-tile system, this key identifies tile within given context.


-
static constexpr Property<
[gpu_handle_param](https://docs.openvino.ai#_CPPv416gpu_handle_param)> ocl_queue = {"OCL_QUEUE"}[#](https://docs.openvino.ai#_CPPv49ocl_queue) This key identifies OpenCL queue handle in a shared context.


-
static constexpr Property<
[gpu_handle_param](https://docs.openvino.ai#_CPPv416gpu_handle_param)> va_device = {"VA_DEVICE"}[#](https://docs.openvino.ai#_CPPv49va_device) This key identifies video acceleration device/display handle in a shared context or shared memory blob parameter map.


This key identifies type of internal shared memory in a shared memory blob parameter map.


-
static constexpr Property<
[gpu_handle_param](https://docs.openvino.ai#_CPPv416gpu_handle_param)> mem_handle = {"MEM_HANDLE"} This key identifies OpenCL memory handle in a shared memory blob parameter map.


-
static constexpr Property<
[gpu_handle_param](https://docs.openvino.ai#_CPPv416gpu_handle_param)> dev_object_handle = {"DEV_OBJECT_HANDLE"}[#](https://docs.openvino.ai#_CPPv417dev_object_handle) This key identifies video decoder surface handle in a shared memory blob parameter map.


-
static constexpr Property<uint32_t> va_plane = {"VA_PLANE"}
[#](https://docs.openvino.ai#_CPPv48va_plane) This key identifies video decoder surface plane in a shared memory blob parameter map.


-
class D3DBufferTensor : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[intel_gpu](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9intel_gpuE)::[ocl](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9intel_gpu3oclE)::[ClBufferTensor](https://docs.openvino.ai/classov_1_1intel__gpu_1_1ocl_1_1_cl_buffer_tensor.html#_CPPv4N2ov9intel_gpu3ocl14ClBufferTensorE)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl15D3DBufferTensorE) *#include <dx.hpp>*This class represents an abstraction for GPU plugin remote tensor which is shared with Direct3D 11 buffer. The plugin object derived from this class can be obtained with

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

-
class D3DSurface2DTensor : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[intel_gpu](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9intel_gpuE)::[ocl](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9intel_gpu3oclE)::[ClImage2DTensor](https://docs.openvino.ai/classov_1_1intel__gpu_1_1ocl_1_1_cl_image2_d_tensor.html#_CPPv4N2ov9intel_gpu3ocl15ClImage2DTensorE)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl18D3DSurface2DTensorE) *#include <dx.hpp>*This class represents an abstraction for GPU plugin remote tensor which is shared with Direct3D 11 2D texture. The plugin object derived from this class can be obtained with

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

-
class D3DContext : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[intel_gpu](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9intel_gpuE)::[ocl](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9intel_gpu3oclE)::[ClContext](https://docs.openvino.ai/classov_1_1intel__gpu_1_1ocl_1_1_cl_context.html#_CPPv4N2ov9intel_gpu3ocl9ClContextE)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl10D3DContextE) *#include <dx.hpp>*This class represents an abstraction for GPU plugin remote context which is shared with Direct3D 11 device. The plugin object derived from this class can be obtained either with

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

-
class ClBufferTensor : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[RemoteTensor](https://docs.openvino.ai/classov_1_1_remote_tensor.html#_CPPv4N2ov12RemoteTensorE)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl14ClBufferTensorE) *#include <ocl.hpp>*This class represents an abstraction for GPU plugin remote tensor which can be shared with user-supplied OpenCL buffer. The plugin object derived from this class can be obtained with

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

-
class ClImage2DTensor : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[RemoteTensor](https://docs.openvino.ai/classov_1_1_remote_tensor.html#_CPPv4N2ov12RemoteTensorE)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl15ClImage2DTensorE) *#include <ocl.hpp>*This class represents an abstraction for GPU plugin remote tensor which can be shared with user-supplied OpenCL 2D Image. The plugin object derived from this class can be obtained with

[ClContext::create_tensor()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__gpu_1_1ocl_1_1_cl_context_1ad9eb11f702e791114f2dc591a3abcb16)call.Note

User can obtain OpenCL image handle from this class.

Subclassed by

[ov::intel_gpu::ocl::D3DSurface2DTensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__gpu_1_1ocl_1_1_d3_d_surface2_d_tensor),[ov::intel_gpu::ocl::VASurfaceTensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__gpu_1_1ocl_1_1_v_a_surface_tensor)

-
class USMTensor : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[RemoteTensor](https://docs.openvino.ai/classov_1_1_remote_tensor.html#_CPPv4N2ov12RemoteTensorE)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl9USMTensorE) *#include <ocl.hpp>*This class represents an abstraction for GPU plugin remote tensor which can be shared with user-supplied USM device pointer. The plugin object derived from this class can be obtained with

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

-
class ClContext : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[RemoteContext](https://docs.openvino.ai/classov_1_1_remote_context.html#_CPPv4N2ov13RemoteContextE)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl9ClContextE) *#include <ocl.hpp>*This class represents an abstraction for GPU plugin remote context which is shared with OpenCL context object. The plugin object derived from this class can be obtained either with

[CompiledModel::get_context()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model_1a22c5537d4c7182072d327077c386b01a)or[Core::create_context()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1ab9a3eef07c3471037070242f8da2fb01)calls.Subclassed by

[ov::intel_gpu::ocl::D3DContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__gpu_1_1ocl_1_1_d3_d_context),[ov::intel_gpu::ocl::VAContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__gpu_1_1ocl_1_1_v_a_context)Public Functions

-
inline ClContext(
[Core](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4N2ov4CoreE)&core, cl_context ctx, int ctx_device_id = 0)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl9ClContext9ClContextER4Core10cl_contexti) Constructs context object from user-supplied OpenCL context handle.

- Parameters:
**core**– A reference to OpenVINO Runtime[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)object**ctx**– A OpenCL context to be used to create shared remote context**ctx_device_id**– An ID of device to be used from ctx



-
inline ClContext(
[Core](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4N2ov4CoreE)&core, cl_command_queue queue)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl9ClContext9ClContextER4Core16cl_command_queue) Constructs context object from user-supplied OpenCL context handle.

Note

Only latency mode is supported for such context sharing case.

- Parameters:
**core**– A reference to OpenVINO Runtime[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)object**queue**– An OpenCL queue to be used to create shared remote context. Queue will be reused inside the plugin.



-
inline cl_context get()
[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl9ClContext3getEv) Returns the underlying OpenCL context handle.

- Returns:
`cl_context`



-
inline operator cl_context()
[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl9ClContextcv10cl_contextEv) OpenCL context handle conversion operator for the

[ClContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__gpu_1_1ocl_1_1_cl_context)object.- Returns:
`cl_context`



-
inline operator cl::Context()
[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl9ClContextcvN2cl7ContextEEv) Standard Khronos cl::Context wrapper conversion operator for the

[ClContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__gpu_1_1ocl_1_1_cl_context)object.- Returns:
`cl::Context`

object


-
inline std::pair<
[ClImage2DTensor](https://docs.openvino.ai/classov_1_1intel__gpu_1_1ocl_1_1_cl_image2_d_tensor.html#_CPPv4N2ov9intel_gpu3ocl15ClImage2DTensorE),[ClImage2DTensor](https://docs.openvino.ai/classov_1_1intel__gpu_1_1ocl_1_1_cl_image2_d_tensor.html#_CPPv4N2ov9intel_gpu3ocl15ClImage2DTensorE)> create_tensor_nv12(const cl::Image2D &nv12_image_plane_y, const cl::Image2D &nv12_image_plane_uv)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl9ClContext18create_tensor_nv12ERKN2cl7Image2DERKN2cl7Image2DE) This function is used to construct a NV12 compound tensor object from two cl::Image2D wrapper objects. The resulting compound contains two remote tensors for Y and UV planes of the surface.

- Parameters:
**nv12_image_plane_y**– cl::Image2D object containing Y plane data.**nv12_image_plane_uv**– cl::Image2D object containing UV plane data.

- Returns:
A pair of remote tensors for each plane



-
inline
[ClBufferTensor](https://docs.openvino.ai/classov_1_1intel__gpu_1_1ocl_1_1_cl_buffer_tensor.html#_CPPv4N2ov9intel_gpu3ocl14ClBufferTensorE)create_tensor(const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape, const cl_mem buffer)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl9ClContext13create_tensorEKN7element4TypeERK5ShapeK6cl_mem) This function is used to obtain remote tensor object from user-supplied cl_mem object.


-
inline
[ClBufferTensor](https://docs.openvino.ai/classov_1_1intel__gpu_1_1ocl_1_1_cl_buffer_tensor.html#_CPPv4N2ov9intel_gpu3ocl14ClBufferTensorE)create_tensor(const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape, const cl::Buffer &buffer)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl9ClContext13create_tensorEKN7element4TypeERK5ShapeRKN2cl6BufferE) This function is used to obtain remote tensor object from user-supplied cl::Buffer object.


-
inline
[ClImage2DTensor](https://docs.openvino.ai/classov_1_1intel__gpu_1_1ocl_1_1_cl_image2_d_tensor.html#_CPPv4N2ov9intel_gpu3ocl15ClImage2DTensorE)create_tensor(const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape, const cl::Image2D &image)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl9ClContext13create_tensorEKN7element4TypeERK5ShapeRKN2cl7Image2DE) This function is used to obtain remote tensor object from user-supplied cl::Image2D object.


-
inline
[USMTensor](https://docs.openvino.ai/classov_1_1intel__gpu_1_1ocl_1_1_u_s_m_tensor.html#_CPPv4N2ov9intel_gpu3ocl9USMTensorE)create_tensor(const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape, void *usm_ptr)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl9ClContext13create_tensorEKN7element4TypeERK5ShapePv) This function is used to obtain remote tensor object from user-supplied USM pointer.


-
inline
[USMTensor](https://docs.openvino.ai/classov_1_1intel__gpu_1_1ocl_1_1_u_s_m_tensor.html#_CPPv4N2ov9intel_gpu3ocl9USMTensorE)create_usm_host_tensor(const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl9ClContext22create_usm_host_tensorEKN7element4TypeERK5Shape) This function is used to allocate USM tensor with host allocation type.


-
inline
[USMTensor](https://docs.openvino.ai/classov_1_1intel__gpu_1_1ocl_1_1_u_s_m_tensor.html#_CPPv4N2ov9intel_gpu3ocl9USMTensorE)create_usm_device_tensor(const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl9ClContext24create_usm_device_tensorEKN7element4TypeERK5Shape) This function is used to allocate USM tensor with device allocation type.


-
[RemoteTensor](https://docs.openvino.ai/classov_1_1_remote_tensor.html#_CPPv4N2ov12RemoteTensorE)create_tensor(const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape, const AnyMap ¶ms = {})[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl9ClContext13create_tensorERKN7element4TypeERK5ShapeRK6AnyMap) Allocates memory tensor in device memory or wraps user-supplied memory handle using the specified tensor description and low-level device-specific parameters. Returns a pointer to the object that implements the

[RemoteTensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_tensor)interface.- Parameters:
**type**– Defines the element type of the tensor.**shape**– Defines the shape of the tensor.**params**– Map of the low-level tensor object parameters.

- Returns:
Pointer to a plugin object that implements the

[RemoteTensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_tensor)interface.


Public Static Functions

-
static inline void type_check(const
[RemoteContext](https://docs.openvino.ai/classov_1_1_remote_context.html#_CPPv4N2ov13RemoteContextE)&remote_context)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl9ClContext10type_checkERK13RemoteContext) Checks that type defined runtime parameters are presented in remote object.

- Parameters:
**remote_context**– A remote context to check


-
inline ClContext(

-
class VASurfaceTensor : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[intel_gpu](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9intel_gpuE)::[ocl](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9intel_gpu3oclE)::[ClImage2DTensor](https://docs.openvino.ai/classov_1_1intel__gpu_1_1ocl_1_1_cl_image2_d_tensor.html#_CPPv4N2ov9intel_gpu3ocl15ClImage2DTensorE)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl15VASurfaceTensorE) *#include <va.hpp>*This class represents an abstraction for GPU plugin remote tensor which is shared with VA output surface. The plugin object derived from this class can be obtained with

[VAContext::create_tensor()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__gpu_1_1ocl_1_1_v_a_context_1ab0216bc65aae095a60f06da22cd8ba59)call.Note

User can also obtain OpenCL 2D image handle from this class.

Public Functions

-
inline operator VASurfaceID()
[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl15VASurfaceTensorcv11VASurfaceIDEv) VASurfaceID conversion operator for the

[VASurfaceTensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__gpu_1_1ocl_1_1_v_a_surface_tensor)object.- Returns:
`VASurfaceID`

handle


-
inline uint32_t plane()
[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl15VASurfaceTensor5planeEv) Returns plane ID of underlying video decoder surface.

- Returns:
Plane ID



-
inline operator VASurfaceID()

-
class VAContext : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[intel_gpu](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9intel_gpuE)::[ocl](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9intel_gpu3oclE)::[ClContext](https://docs.openvino.ai/classov_1_1intel__gpu_1_1ocl_1_1_cl_context.html#_CPPv4N2ov9intel_gpu3ocl9ClContextE)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl9VAContextE) *#include <va.hpp>*This class represents an abstraction for GPU plugin remote context which is shared with VA display object. The plugin object derived from this class can be obtained either with

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

-
using gpu_handle_param = void*