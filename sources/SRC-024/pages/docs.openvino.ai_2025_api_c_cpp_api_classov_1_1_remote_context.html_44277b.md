source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_remote_context.html
lastmod: 

# Class ov::RemoteContext[#](https://docs.openvino.ai#class-ov-remotecontext)

-
class RemoteContext
[#](https://docs.openvino.ai#_CPPv4N2ov13RemoteContextE) This class represents an abstraction

for remote (non-CPU) accelerator device-specific inference context. Such context represents a scope on the device within which compiled models and remote memory tensors can exist, function, and exchange data.

Subclassed by

[ov::intel_gpu::ocl::ClContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__gpu_1_1ocl_1_1_cl_context),[ov::intel_npu::level_zero::ZeroContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__npu_1_1level__zero_1_1_zero_context)Public Functions

-
RemoteContext() = default
[#](https://docs.openvino.ai#_CPPv4N2ov13RemoteContext13RemoteContextEv) Default constructor.


-
RemoteContext(const
[RemoteContext](https://docs.openvino.ai#_CPPv4N2ov13RemoteContext13RemoteContextERK13RemoteContext)&other) = default[#](https://docs.openvino.ai#_CPPv4N2ov13RemoteContext13RemoteContextERK13RemoteContext) Default copy constructor.

- Parameters:
**other**– Another[RemoteContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_context)object.


-
[RemoteContext](https://docs.openvino.ai#_CPPv4N2ov13RemoteContextE)&operator=(const[RemoteContext](https://docs.openvino.ai#_CPPv4N2ov13RemoteContextE)&other) = default[#](https://docs.openvino.ai#_CPPv4N2ov13RemoteContextaSERK13RemoteContext) Default copy assignment operator.

- Parameters:
**other**– Another[RemoteContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_context)object.- Returns:
Reference to the current object.



-
RemoteContext(
[RemoteContext](https://docs.openvino.ai#_CPPv4N2ov13RemoteContext13RemoteContextERR13RemoteContext)&&other) = default[#](https://docs.openvino.ai#_CPPv4N2ov13RemoteContext13RemoteContextERR13RemoteContext) Default move constructor.

- Parameters:
**other**– Another[RemoteContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_context)object.


-
[RemoteContext](https://docs.openvino.ai#_CPPv4N2ov13RemoteContextE)&operator=([RemoteContext](https://docs.openvino.ai#_CPPv4N2ov13RemoteContextE)&&other) = default[#](https://docs.openvino.ai#_CPPv4N2ov13RemoteContextaSERR13RemoteContext) Default move assignment operator.

- Parameters:
**other**– Another[RemoteContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_context)object.- Returns:
Reference to the current object.



-
operator bool() const noexcept
[#](https://docs.openvino.ai#_CPPv4NK2ov13RemoteContextcvbEv) Checks if current

[RemoteContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_context)object is initialized.- Returns:
`true`

if current[RemoteContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_context)object is initialized,`false`

- otherwise


-
~RemoteContext()
[#](https://docs.openvino.ai#_CPPv4N2ov13RemoteContextD0Ev) Destructor that preserves unloading order of implementation object and reference to the library.


-
template<typename T>

inline bool is() const noexcept[#](https://docs.openvino.ai#_CPPv4I0ENK2ov13RemoteContext2isEbv) Checks if the

[RemoteContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_context)object can be cast to the type T.- Template Parameters:
**T**– Type to be checked. Must represent a class derived from[RemoteContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_context).- Returns:
True if this object can be dynamically cast to the type T*; false, otherwise.



-
template<typename T>

inline const[T](https://docs.openvino.ai#_CPPv4I0ENK2ov13RemoteContext2asEK1Tv)as() const[#](https://docs.openvino.ai#_CPPv4I0ENK2ov13RemoteContext2asEK1Tv) Casts this

[RemoteContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_context)object to the type T.- Template Parameters:
**T**– Type to cast to. Must represent a class derived from[RemoteContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_context).- Returns:
T Object.



-
[RemoteTensor](https://docs.openvino.ai/classov_1_1_remote_tensor.html#_CPPv4N2ov12RemoteTensorE)create_tensor(const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape, const AnyMap ¶ms = {})[#](https://docs.openvino.ai#_CPPv4N2ov13RemoteContext13create_tensorERKN7element4TypeERK5ShapeRK6AnyMap) Allocates memory tensor in device memory or wraps user-supplied memory handle using the specified tensor description and low-level device-specific parameters. Returns a pointer to the object that implements the

[RemoteTensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_tensor)interface.- Parameters:
**type**– Defines the element type of the tensor.**shape**– Defines the shape of the tensor.**params**– Map of the low-level tensor object parameters.

- Returns:
Pointer to a plugin object that implements the

[RemoteTensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_tensor)interface.


-
AnyMap get_params() const
[#](https://docs.openvino.ai#_CPPv4NK2ov13RemoteContext10get_paramsEv) Returns a map of device-specific parameters required for low-level operations with the underlying object. Parameters include device/context handles, access flags, etc. Content of the returned map depends on a remote execution context that is currently set on the device (working scenario). Abstract method.

- Returns:
A map of name/parameter elements.



-
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)create_host_tensor(const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape)[#](https://docs.openvino.ai#_CPPv4N2ov13RemoteContext18create_host_tensorEKN7element4TypeERK5Shape) This method is used to create a host tensor object friendly for the device in current context. For example, GPU context may allocate USM host memory (if corresponding extension is available), which could be more efficient than regular host memory.


Public Static Functions

-
static void type_check(const
[RemoteContext](https://docs.openvino.ai#_CPPv4N2ov13RemoteContextE)&remote_context, const std::map<std::string, std::vector<std::string>> &type_info = {})[#](https://docs.openvino.ai#_CPPv4N2ov13RemoteContext10type_checkERK13RemoteContextRKNSt3mapINSt6stringENSt6vectorINSt6stringEEEEE) Internal method: checks remote type.

- Parameters:
**remote_context**– Remote context which type is checked.**type_info**– Map with remote object runtime info.

- Throws:
[Exception](https://docs.openvino.ai/classov_1_1_exception.html#_CPPv4N2ov9ExceptionE)– if type check with the specified parameters failed.


-
RemoteContext() = default