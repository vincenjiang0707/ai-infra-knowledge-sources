source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1intel__gpu_1_1ocl_1_1_v_a_surface_tensor.html
lastmod: 

# Class ov::intel_gpu::ocl::VASurfaceTensor[#](https://docs.openvino.ai#class-ov-intel-gpu-ocl-vasurfacetensor)

-
class VASurfaceTensor : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[intel_gpu](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9intel_gpuE)::[ocl](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9intel_gpu3oclE)::[ClImage2DTensor](https://docs.openvino.ai/classov_1_1intel__gpu_1_1ocl_1_1_cl_image2_d_tensor.html#_CPPv4N2ov9intel_gpu3ocl15ClImage2DTensorE)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl15VASurfaceTensorE) This class represents an abstraction for GPU plugin remote tensor which is shared with VA output surface. The plugin object derived from this class can be obtained with

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