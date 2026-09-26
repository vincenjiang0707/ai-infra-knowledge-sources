source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1intel__gpu_1_1ocl_1_1_cl_image2_d_tensor.html
lastmod: 

# Class ov::intel_gpu::ocl::ClImage2DTensor[#](https://docs.openvino.ai#class-ov-intel-gpu-ocl-climage2dtensor)

-
class ClImage2DTensor : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[RemoteTensor](https://docs.openvino.ai/classov_1_1_remote_tensor.html#_CPPv4N2ov12RemoteTensorE)[#](https://docs.openvino.ai#_CPPv4N2ov9intel_gpu3ocl15ClImage2DTensorE) This class represents an abstraction for GPU plugin remote tensor which can be shared with user-supplied OpenCL 2D Image. The plugin object derived from this class can be obtained with

[ClContext::create_tensor()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__gpu_1_1ocl_1_1_cl_context_1ad9eb11f702e791114f2dc591a3abcb16)call.Note

User can obtain OpenCL image handle from this class.

Subclassed by

[ov::intel_gpu::ocl::D3DSurface2DTensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__gpu_1_1ocl_1_1_d3_d_surface2_d_tensor),[ov::intel_gpu::ocl::VASurfaceTensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__gpu_1_1ocl_1_1_v_a_surface_tensor)