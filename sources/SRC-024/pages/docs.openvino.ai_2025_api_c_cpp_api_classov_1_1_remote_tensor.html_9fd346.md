source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_remote_tensor.html
lastmod: 

# Class ov::RemoteTensor[#](https://docs.openvino.ai#class-ov-remotetensor)

-
class RemoteTensor : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)[#](https://docs.openvino.ai#_CPPv4N2ov12RemoteTensorE) Remote memory access and interoperability API.

Subclassed by

[ov::intel_gpu::ocl::ClBufferTensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__gpu_1_1ocl_1_1_cl_buffer_tensor),[ov::intel_gpu::ocl::ClImage2DTensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__gpu_1_1ocl_1_1_cl_image2_d_tensor),[ov::intel_gpu::ocl::USMTensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__gpu_1_1ocl_1_1_u_s_m_tensor),[ov::intel_npu::level_zero::ZeroBufferTensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__npu_1_1level__zero_1_1_zero_buffer_tensor)Public Functions

-
RemoteTensor() = default
[#](https://docs.openvino.ai#_CPPv4N2ov12RemoteTensor12RemoteTensorEv) Default constructor.


-
RemoteTensor(const
[RemoteTensor](https://docs.openvino.ai#_CPPv4N2ov12RemoteTensor12RemoteTensorERK12RemoteTensorRK10CoordinateRK10Coordinate)&other, const[Coordinate](https://docs.openvino.ai/classov_1_1_coordinate.html#_CPPv4N2ov10CoordinateE)&begin, const[Coordinate](https://docs.openvino.ai/classov_1_1_coordinate.html#_CPPv4N2ov10CoordinateE)&end)[#](https://docs.openvino.ai#_CPPv4N2ov12RemoteTensor12RemoteTensorERK12RemoteTensorRK10CoordinateRK10Coordinate) Constructs region of interest (ROI) tensor from another remote tensor.

Note

Does not perform memory allocation internally

Note

A Number of dimensions in

`begin`

and`end`

must match number of dimensions in`other.get_shape()`

- Parameters:
**other**– original tensor**begin**– start coordinate of ROI object inside of the original object.**end**– end coordinate of ROI object inside of the original object.



-
void *data(const
[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)) = delete[#](https://docs.openvino.ai#_CPPv4N2ov12RemoteTensor4dataEKN7element4TypeE) Access to host memory is not available for

[RemoteTensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_tensor). To access a device-specific memory, cast to a specific[RemoteTensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_tensor)derived object and work with its properties or parse device memory properties via[RemoteTensor::get_params](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_tensor_1aecdf1dc2e396c38b58a45b6d0202a0b3).- Returns:
Nothing, throws an exception.



-
void copy_to(
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&dst) const[#](https://docs.openvino.ai#_CPPv4NK2ov12RemoteTensor7copy_toERN2ov6TensorE) Copies data from this

[RemoteTensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_tensor)to the specified destination tensor.- Parameters:
**dst**– The destination tensor to which data will be copied.


-
void copy_from(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&src)[#](https://docs.openvino.ai#_CPPv4N2ov12RemoteTensor9copy_fromERKN2ov6TensorE) Copies data from the specified source tensor to this

[RemoteTensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_tensor).- Parameters:
**src**– The source tensor from which data will be copied.


-
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::AnyMap get_params() const[#](https://docs.openvino.ai#_CPPv4NK2ov12RemoteTensor10get_paramsEv) Returns a map of device-specific parameters required for low-level operations with underlying object. Parameters include device/context/surface/buffer handles, access flags, etc. Content of the returned map depends on remote execution context that is currently set on the device (working scenario). Abstract method.

- Returns:
A map of name/parameter elements.



-
RemoteTensor() = default