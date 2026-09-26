source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_i_remote_context.html
lastmod: 

# Class ov::IRemoteContext[#](https://docs.openvino.ai#class-ov-iremotecontext)

-
class IRemoteContext : public std::enable_shared_from_this<
[IRemoteContext](https://docs.openvino.ai#_CPPv4N2ov14IRemoteContextE)>[#](https://docs.openvino.ai#_CPPv4N2ov14IRemoteContextE) Public Functions

-
virtual const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::AnyMap &get_property() const = 0[#](https://docs.openvino.ai#_CPPv4NK2ov14IRemoteContext12get_propertyEv) Returns a map of device-specific parameters required for low-level operations with underlying object. Parameters include device/context handles, access flags, etc. Contents of the map returned depend on remote execution context that is currently set on the device (working scenario). Abstract method.

- Returns:
A map of name/Any elements.



-
virtual
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[SoPtr](https://docs.openvino.ai/structov_1_1_so_ptr.html#_CPPv4I0EN2ov5SoPtrE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[IRemoteTensor](https://docs.openvino.ai/classov_1_1_i_remote_tensor.html#_CPPv4N2ov13IRemoteTensorE)> create_tensor(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&type, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::AnyMap ¶ms = {}) = 0[#](https://docs.openvino.ai#_CPPv4N2ov14IRemoteContext13create_tensorERKN2ov7element4TypeERKN2ov5ShapeERKN2ov6AnyMapE) Allocates memory tensor in device memory or wraps user-supplied memory handle using the specified tensor description and low-level device-specific parameters. Returns a pointer to the object that implements the

[RemoteTensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_tensor)interface.- Parameters:
**type**– Defines the element type of the tensor.**shape**– Defines the shape of the tensor.**params**– Map of the low-level tensor object parameters.

- Returns:
Pointer to a plugin object that implements the

[RemoteTensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_tensor)interface.


-
virtual
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[SoPtr](https://docs.openvino.ai/structov_1_1_so_ptr.html#_CPPv4I0EN2ov5SoPtrE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::ITensor> create_host_tensor(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)type, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape)[#](https://docs.openvino.ai#_CPPv4N2ov14IRemoteContext18create_host_tensorEKN2ov7element4TypeERKN2ov5ShapeE) This method is used to create a host tensor object friendly for the device in current context. For example, GPU context may allocate USM host memory (if corresponding extension is available), which could be more efficient than regular host memory.


-
virtual const