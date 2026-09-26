source: https://docs.openvino.ai/2025/api/c_cpp_api/group__ov__runtime__cpp__api.html
lastmod: 

# Group Inference[#](https://docs.openvino.ai#group-inference)

-
*group*Inference OpenVINO Inference C++ API provides

[ov::Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core),[ov::CompiledModel](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model),[ov::InferRequest](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_infer_request)and[ov::Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)classesTypedefs

-
using SupportedOpsMap = std::map<std::string, std::string>
[#](https://docs.openvino.ai#_CPPv415SupportedOpsMap) This type of map is used for result of

[Core::query_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1acdf8e64824fe4cf147c3b52ab32c1aab).`key`

means operation name`value`

means device name supporting this operation


-
class Allocator
[#](https://docs.openvino.ai#_CPPv4N2ov9AllocatorE) *#include <allocator.hpp>*Wraps allocator implementation to provide safe way to store allocater loaded from shared library And constructs default based on

`new`

`delete`

c++ calls allocator if created without parameters Accepts any[std::pmr::memory_resource](https://en.cppreference.com/w/cpp/memory/memory_resource)like allocator.Public Functions

-
~Allocator()
[#](https://docs.openvino.ai#_CPPv4N2ov9AllocatorD0Ev) Destructor preserves unloading order of implementation object and reference to library.


-
Allocator()
[#](https://docs.openvino.ai#_CPPv4N2ov9Allocator9AllocatorEv) Default constructor.


-
Allocator(const
[Allocator](https://docs.openvino.ai/classov_1_1_allocator.html#_CPPv4N2ov9Allocator9AllocatorERK9Allocator)&other) = default[#](https://docs.openvino.ai#_CPPv4N2ov9Allocator9AllocatorERK9Allocator) Default copy constructor.

- Parameters:
**other**– other[Allocator](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_allocator)object


-
[Allocator](https://docs.openvino.ai/classov_1_1_allocator.html#_CPPv4N2ov9AllocatorE)&operator=(const[Allocator](https://docs.openvino.ai/classov_1_1_allocator.html#_CPPv4N2ov9AllocatorE)&other) = default[#](https://docs.openvino.ai#_CPPv4N2ov9AllocatoraSERK9Allocator) Default copy assignment operator.

- Parameters:
**other**– other[Allocator](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_allocator)object- Returns:
reference to the current object



-
Allocator(
[Allocator](https://docs.openvino.ai/classov_1_1_allocator.html#_CPPv4N2ov9Allocator9AllocatorERR9Allocator)&&other) = default[#](https://docs.openvino.ai#_CPPv4N2ov9Allocator9AllocatorERR9Allocator) Default move constructor.

- Parameters:
**other**– other[Allocator](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_allocator)object


-
[Allocator](https://docs.openvino.ai/classov_1_1_allocator.html#_CPPv4N2ov9AllocatorE)&operator=([Allocator](https://docs.openvino.ai/classov_1_1_allocator.html#_CPPv4N2ov9AllocatorE)&&other) = default[#](https://docs.openvino.ai#_CPPv4N2ov9AllocatoraSERR9Allocator) Default move assignment operator.

- Parameters:
**other**– other[Allocator](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_allocator)object- Returns:
reference to the current object



Initialize allocator using any allocator like object.

- Template Parameters:
**A**– Type of allocator- Parameters:
**a**– allocator object


-
void *allocate(const size_t bytes, const size_t alignment = alignof(max_align_t))
[#](https://docs.openvino.ai#_CPPv4N2ov9Allocator8allocateEK6size_tK6size_t) Allocates memory.

- Parameters:
**bytes**– The size in bytes at least to allocate**alignment**– The alignment of storage

- Throws:
[Exception](https://docs.openvino.ai/classov_1_1_exception.html#_CPPv4N2ov9ExceptionE)– if specified size and alignment is not supported- Returns:
Handle to the allocated resource



-
void deallocate(void *ptr, const size_t bytes = 0, const size_t alignment = alignof(max_align_t)) noexcept
[#](https://docs.openvino.ai#_CPPv4N2ov9Allocator10deallocateEPvK6size_tK6size_t) Releases the handle and all associated memory resources which invalidates the handle.

- Parameters:
**ptr**– The handle to free**bytes**– The size in bytes that was passed into[allocate()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_allocator_1aebd41905b0026a61af51360fabaaf947)method**alignment**– The alignment of storage that was passed into[allocate()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_allocator_1aebd41905b0026a61af51360fabaaf947)method



-
bool operator==(const
[Allocator](https://docs.openvino.ai/classov_1_1_allocator.html#_CPPv4N2ov9AllocatorE)&other) const[#](https://docs.openvino.ai#_CPPv4NK2ov9AllocatoreqERK9Allocator) Compares with other

[Allocator](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_allocator).- Parameters:
**other**– Other instance of allocator- Returns:
`true`

if and only if memory allocated from one[Allocator](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_allocator)can be deallocated from the other and vice versa


-
~Allocator()

-
class Tensor
[#](https://docs.openvino.ai#_CPPv4N2ov6TensorE) *#include <tensor.hpp>*[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)API holding host memory It can throw exceptions safely for the application, where it is properly handled.Subclassed by

[ov::RemoteTensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_tensor)Unnamed Group

-
void *data() const
[#](https://docs.openvino.ai#_CPPv4NK2ov6Tensor4dataEv) Provides an access to the underlying host memory.

- Returns:
A host pointer to tensor memory



Unnamed Group

-
void *data(const
[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&type) const[#](https://docs.openvino.ai#_CPPv4NK2ov6Tensor4dataERKN7element4TypeE) Provides an access to the underlying host memory.

Note

The method throws an exception if specified type’s fundamental type does not match with tensor element type’s fundamental type

- Parameters:
**type**– Optional type parameter.- Returns:
A host pointer to tensor memory



Unnamed Group

Public Functions

-
Tensor() = default
[#](https://docs.openvino.ai#_CPPv4N2ov6Tensor6TensorEv) Default constructor.


Copy constructor with adding new shared object.

- Parameters:
**other**– Original tensor**so**– Shared object



-
Tensor(const
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6Tensor6TensorERK6Tensor)&other) = default[#](https://docs.openvino.ai#_CPPv4N2ov6Tensor6TensorERK6Tensor) Default copy constructor.

- Parameters:
**other**– other[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)object


-
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&operator=(const[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&other) = default[#](https://docs.openvino.ai#_CPPv4N2ov6TensoraSERK6Tensor) Default copy assignment operator.

- Parameters:
**other**– other[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)object- Returns:
reference to the current object



-
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&operator=([Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&&other) = default[#](https://docs.openvino.ai#_CPPv4N2ov6TensoraSERR6Tensor) Default move assignment operator.

- Parameters:
**other**– other[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)object- Returns:
reference to the current object



-
~Tensor()
[#](https://docs.openvino.ai#_CPPv4N2ov6TensorD0Ev) Destructor preserves unloading order of implementation object and reference to library.


-
Tensor(const
[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape, const[Allocator](https://docs.openvino.ai/classov_1_1_allocator.html#_CPPv4N2ov9AllocatorE)&allocator = {})[#](https://docs.openvino.ai#_CPPv4N2ov6Tensor6TensorERKN7element4TypeERK5ShapeRK9Allocator) Constructs

[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)using element type and shape. Allocate internal host storage using default allocator.

-
Tensor(const
[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape, void *host_ptr, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&strides = {})[#](https://docs.openvino.ai#_CPPv4N2ov6Tensor6TensorERKN7element4TypeERK5ShapePvRK7Strides) Constructs

[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)using element type and shape. Wraps allocated host memory.Note

Does not perform memory allocation internally


-
Tensor(const
[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape, const void *host_ptr, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&strides = {})[#](https://docs.openvino.ai#_CPPv4N2ov6Tensor6TensorERKN7element4TypeERK5ShapePKvRK7Strides) Constructs

[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)using element type and shape. Wraps allocated host memory as read only.Note

Does not perform memory allocation internally


-
Tensor(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &port, const[Allocator](https://docs.openvino.ai/classov_1_1_allocator.html#_CPPv4N2ov9AllocatorE)&allocator = {})[#](https://docs.openvino.ai#_CPPv4N2ov6Tensor6TensorERKN2ov6OutputIKN2ov4NodeEEERK9Allocator) Constructs

[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)using port from node. Allocate internal host storage using default allocator.- Parameters:
**port**– port from node**allocator**– allocates memory for internal tensor storage



-
Tensor(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &port, void *host_ptr, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&strides = {})[#](https://docs.openvino.ai#_CPPv4N2ov6Tensor6TensorERKN2ov6OutputIKN2ov4NodeEEEPvRK7Strides) Constructs

[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)using port from node. Wraps allocated host memory.Note

Does not perform memory allocation internally

- Parameters:
**port**– port from node**host_ptr**– Pointer to pre-allocated host memory with initialized objects**strides**– Optional strides parameters in bytes.[Strides](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_strides)are supposed to be computed automatically based on shape and element size



-
Tensor(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &port, const void *host_ptr, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&strides = {})[#](https://docs.openvino.ai#_CPPv4N2ov6Tensor6TensorERKN2ov6OutputIKN2ov4NodeEEEPKvRK7Strides) Constructs

[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)using port from node. Wraps allocated host memory as read only.Note

Does not perform memory allocation internally

- Parameters:
**port**– port from node**host_ptr**– Pointer to pre-allocated host memory with initialized objects**strides**– Optional strides parameters in bytes.[Strides](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_strides)are supposed to be computed automatically based on shape and element size



-
Tensor(const
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6Tensor6TensorERK6TensorRK10CoordinateRK10Coordinate)&other, const[Coordinate](https://docs.openvino.ai/classov_1_1_coordinate.html#_CPPv4N2ov10CoordinateE)&begin, const[Coordinate](https://docs.openvino.ai/classov_1_1_coordinate.html#_CPPv4N2ov10CoordinateE)&end)[#](https://docs.openvino.ai#_CPPv4N2ov6Tensor6TensorERK6TensorRK10CoordinateRK10Coordinate) Constructs region of interest (ROI) tensor form another tensor.

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
void set_shape(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape)[#](https://docs.openvino.ai#_CPPv4N2ov6Tensor9set_shapeERKN2ov5ShapeE) Set new shape for tensor, deallocate/allocate if new total size is bigger than previous one.

Note

Memory allocation may happen

- Parameters:
**shape**– A new shape


-
void copy_to(
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)dst) const[#](https://docs.openvino.ai#_CPPv4NK2ov6Tensor7copy_toEN2ov6TensorE) Copy tensor, destination tensor should have the same element type and shape.

- Parameters:
**dst**– destination tensor


-
bool is_continuous() const
[#](https://docs.openvino.ai#_CPPv4NK2ov6Tensor13is_continuousEv) Reports whether the tensor is continuous or not.

- Returns:
true if tensor is continuous



-
size_t get_size() const
[#](https://docs.openvino.ai#_CPPv4NK2ov6Tensor8get_sizeEv) Returns the total number of elements (a product of all the dims or 1 for scalar)

- Returns:
The total number of elements



-
size_t get_byte_size() const
[#](https://docs.openvino.ai#_CPPv4NK2ov6Tensor13get_byte_sizeEv) Returns the size of the current

[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)in bytes.- Returns:
[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)’s size in bytes


-
bool operator!() const noexcept
[#](https://docs.openvino.ai#_CPPv4NK2ov6TensorntEv) Checks if current

[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)object is not initialized.- Returns:
`true`

if current[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)object is not initialized,`false`

- otherwise


-
explicit operator bool() const noexcept
[#](https://docs.openvino.ai#_CPPv4NK2ov6TensorcvbEv) Checks if current

[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)object is initialized.- Returns:
`true`

if current[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)object is initialized,`false`

- otherwise


-
template<typename T>

inline std::enable_if_t<std::is_base_of_v<[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE),[T](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4I0ENK2ov6Tensor2isENSt11enable_if_tINSt12is_base_of_vI6Tensor1TEEbEEv)>, bool> is() const noexcept[#](https://docs.openvino.ai#_CPPv4I0ENK2ov6Tensor2isENSt11enable_if_tINSt12is_base_of_vI6Tensor1TEEbEEv) Checks if the

[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)object can be cast to the type T.- Template Parameters:
**T**– Type to be checked. Must represent a class derived from the[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)- Returns:
true if this object can be dynamically cast to the type const T*. Otherwise, false



-
void *data() const

-
class CompiledModel
[#](https://docs.openvino.ai#_CPPv4N2ov13CompiledModelE) *#include <compiled_model.hpp>*This class represents a compiled model.

A model is compiled by a specific device by applying multiple optimization transformations, then mapping to compute kernels.

Public Functions

-
CompiledModel() = default
[#](https://docs.openvino.ai#_CPPv4N2ov13CompiledModel13CompiledModelEv) Default constructor.


-
~CompiledModel()
[#](https://docs.openvino.ai#_CPPv4N2ov13CompiledModelD0Ev) Destructor that preserves unloading order of an implementation object and reference to library.


-
std::shared_ptr<const
[Model](https://docs.openvino.ai/classov_1_1_model.html#_CPPv4N2ov5ModelE)> get_runtime_model() const[#](https://docs.openvino.ai#_CPPv4NK2ov13CompiledModel17get_runtime_modelEv) Gets runtime model information from a device. This object represents an internal device-specific model that is optimized for a particular accelerator. It contains device-specific nodes, runtime information and can be used only to understand how the source model is optimized and which kernels, element types, and layouts are selected for optimal inference.

- Returns:
A model containing Executable Graph Info.



-
const std::vector<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)>> &inputs() const[#](https://docs.openvino.ai#_CPPv4NK2ov13CompiledModel6inputsEv) Gets all inputs of a compiled model. Inputs are represented as a vector of outputs of the

[ov::op::v0::Parameter](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_parameter)operations. They contain information about input tensors such as tensor shape, names, and element type.- Returns:
std::vector of model inputs.



-
const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input() const[#](https://docs.openvino.ai#_CPPv4NK2ov13CompiledModel5inputEv) Gets a single input of a compiled model. The input is represented as an output of the

[ov::op::v0::Parameter](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_parameter)operation. The input contains information about input tensor such as tensor shape, names, and element type.Note

If a model has more than one input, this method throws

[ov::Exception](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_exception).- Returns:
Compiled model input.



-
const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input(size_t i) const[#](https://docs.openvino.ai#_CPPv4NK2ov13CompiledModel5inputE6size_t) Gets input of a compiled model identified by

`i`

. The input contains information about input tensor such as tensor shape, names, and element type.Note

The method throws

[ov::Exception](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_exception)if input with the specified index`i`

is not found.- Parameters:
**i**– Index of input.- Returns:
Compiled model input.



-
const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input(const std::string &tensor_name) const[#](https://docs.openvino.ai#_CPPv4NK2ov13CompiledModel5inputERKNSt6stringE) Gets input of a compiled model identified by

`tensor_name`

. The input contains information about input tensor such as tensor shape, names, and element type.Note

The method throws

[ov::Exception](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_exception)if input with the specified tensor name`tensor_name`

is not found.- Parameters:
**tensor_name**– The input tensor name.- Returns:
Compiled model input.



-
const std::vector<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)>> &outputs() const[#](https://docs.openvino.ai#_CPPv4NK2ov13CompiledModel7outputsEv) Get all outputs of a compiled model. Outputs are represented as a vector of output from the

[ov::op::v0::Result](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_result)operations. Outputs contain information about output tensors such as tensor shape, names, and element type.- Returns:
std::vector of model outputs.



-
const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &output() const[#](https://docs.openvino.ai#_CPPv4NK2ov13CompiledModel6outputEv) Gets a single output of a compiled model. The output is represented as an output from the

[ov::op::v0::Result](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_result)operation. The output contains information about output tensor such as tensor shape, names, and element type.Note

If a model has more than one output, this method throws

[ov::Exception](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_exception).- Returns:
Compiled model output.



-
const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &output(size_t i) const[#](https://docs.openvino.ai#_CPPv4NK2ov13CompiledModel6outputE6size_t) Gets output of a compiled model identified by

`index`

. The output contains information about output tensor such as tensor shape, names, and element type.Note

The method throws

[ov::Exception](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_exception)if output with the specified index`index`

is not found.- Parameters:
**i**– Index of input.- Returns:
Compiled model output.



-
const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &output(const std::string &tensor_name) const[#](https://docs.openvino.ai#_CPPv4NK2ov13CompiledModel6outputERKNSt6stringE) Gets output of a compiled model identified by

`tensor_name`

. The output contains information about output tensor such as tensor shape, names, and element type.Note

The method throws

[ov::Exception](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_exception)if output with the specified tensor name`tensor_name`

is not found.- Parameters:
**tensor_name**–[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)tensor name.- Returns:
Compiled model output.



-
[InferRequest](https://docs.openvino.ai/classov_1_1_infer_request.html#_CPPv4N2ov12InferRequestE)create_infer_request()[#](https://docs.openvino.ai#_CPPv4N2ov13CompiledModel20create_infer_requestEv) Creates an inference request object used to infer the compiled model. The created request has allocated input and output tensors (which can be changed later).

- Returns:
[InferRequest](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_infer_request)object


-
void export_model(std::ostream &model_stream)
[#](https://docs.openvino.ai#_CPPv4N2ov13CompiledModel12export_modelERNSt7ostreamE) Exports the current compiled model to an output stream

`std::ostream`

. The exported model can also be imported via the[ov::Core::import_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1a0d2853511bd7ba60cb591f4685b91884)method.See also

- Parameters:
**model_stream**–[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)stream to store the model to.


-
void set_property(const AnyMap &properties)
[#](https://docs.openvino.ai#_CPPv4N2ov13CompiledModel12set_propertyERK6AnyMap) Sets properties for the current compiled model.

- Parameters:
**properties**– Map of pairs: (property name, property value).


-
template<typename ...Properties>

inline[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4utilE)::EnableIfAllStringAny<void,[Properties](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4IDpEN2ov13CompiledModel12set_propertyEN4util20EnableIfAllStringAnyIvDp10PropertiesEEDpRR10Properties)...> set_property([Properties](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4IDpEN2ov13CompiledModel12set_propertyEN4util20EnableIfAllStringAnyIvDp10PropertiesEEDpRR10Properties)&&... properties)[#](https://docs.openvino.ai#_CPPv4IDpEN2ov13CompiledModel12set_propertyEN4util20EnableIfAllStringAnyIvDp10PropertiesEEDpRR10Properties) Sets properties for the current compiled model.

- Template Parameters:
**Properties**– Should be the pack of`std::pair<std::string,`

types.[ov::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)>- Parameters:
**properties**– Optional pack of pairs: (property name, property value).


-
[Any](https://docs.openvino.ai/classov_1_1_any.html#_CPPv4N2ov3AnyE)get_property(const std::string &name) const[#](https://docs.openvino.ai#_CPPv4NK2ov13CompiledModel12get_propertyERKNSt6stringE) Gets properties for current compiled model.

The method is responsible for extracting information that affects compiled model inference. The list of supported configuration values can be extracted via

[CompiledModel::get_property](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model_1a109d701ffe8b5de096961c7c98ff0bed)with the[ov::supported_properties](https://docs.openvino.ai/group__ov__runtime__cpp__prop__api.html#group__ov__runtime__cpp__prop__api_1ga097f1274f26f3f4e1aa4fc3928748592)key, but some of these keys cannot be changed dynamically, for example,[ov::device::id](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__runtime__cpp__prop__api_1ga433b8ea52e99c2b1fa8b26453485d75d)cannot be changed if a compiled model has already been compiled for a particular device.

-
template<typename T, PropertyMutability mutability>

inline[T](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4I0_18PropertyMutabilityENK2ov13CompiledModel12get_propertyE1TRKN2ov8PropertyI1T10mutabilityEE)get_property(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Property](https://docs.openvino.ai/classov_1_1_property.html#_CPPv4I0_18PropertyMutabilityEN2ov8PropertyE)<[T](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4I0_18PropertyMutabilityENK2ov13CompiledModel12get_propertyE1TRKN2ov8PropertyI1T10mutabilityEE),[mutability](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4I0_18PropertyMutabilityENK2ov13CompiledModel12get_propertyE1TRKN2ov8PropertyI1T10mutabilityEE)> &property) const[#](https://docs.openvino.ai#_CPPv4I0_18PropertyMutabilityENK2ov13CompiledModel12get_propertyE1TRKN2ov8PropertyI1T10mutabilityEE) Gets properties related to device behaviour.

The method extracts information that can be set via the set_property method.

- Template Parameters:
**T**– Type of a returned value.- Parameters:
**property**–[Property](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_property)object.- Returns:
Value of property.



-
void release_memory()
[#](https://docs.openvino.ai#_CPPv4N2ov13CompiledModel14release_memoryEv) Release intermediate memory.

This method forces the Compiled model to release memory allocated for intermediate structures, e.g. caches, tensors, temporal buffers etc., when possible


-
[RemoteContext](https://docs.openvino.ai/classov_1_1_remote_context.html#_CPPv4N2ov13RemoteContextE)get_context() const[#](https://docs.openvino.ai#_CPPv4NK2ov13CompiledModel11get_contextEv) Returns pointer to device-specific shared context on a remote accelerator device that was used to create this

[CompiledModel](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model).- Returns:
A context.



-
bool operator!() const noexcept
[#](https://docs.openvino.ai#_CPPv4NK2ov13CompiledModelntEv) Checks if the current

[CompiledModel](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model)object is not initialized.- Returns:
`true`

if the current[CompiledModel](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model)object is not initialized;`false`

, otherwise.


-
explicit operator bool() const noexcept
[#](https://docs.openvino.ai#_CPPv4NK2ov13CompiledModelcvbEv) Checks if the current

[CompiledModel](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model)object is initialized.- Returns:
`true`

if the current[CompiledModel](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model)object is initialized;`false`

, otherwise.


-
CompiledModel() = default

-
class Core
[#](https://docs.openvino.ai#_CPPv4N2ov4CoreE) *#include <core.hpp>*This class represents an OpenVINO runtime

[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)entity.User applications can create several

[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)class instances, but in this case the underlying plugins are created multiple times and not shared between several[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)instances. The recommended way is to have a single[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)instance per application.Unnamed Group

-
std::shared_ptr<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Model](https://docs.openvino.ai/classov_1_1_model.html#_CPPv4N2ov5ModelE)> read_model(const std::string &model_path, const std::string &bin_path = {}, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::AnyMap &properties = {}) const[#](https://docs.openvino.ai#_CPPv4NK2ov4Core10read_modelERKNSt6stringERKNSt6stringERKN2ov6AnyMapE) Reads models from IR / ONNX / PDPD / TF / TFLite file formats.

- Parameters:
**model_path**– Path to a model.**bin_path**– Path to a data file. For IR format (*.bin):if

`bin_path`

is empty, will try to read a bin file with the same name as xml andif the bin file with the same name is not found, will load IR without weights. For the following file formats the

`bin_path`

parameter is not used:ONNX format (*.onnx)

PDPD (*.pdmodel)

TF (*.pb, *.meta, SavedModel directory)

TFLite (*.tflite)


**properties**– Optional map of pairs: (property name, property value) relevant only for this read operation.

- Returns:
A model.



Unnamed Group

-
template<typename ...Properties>

inline[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4utilE)::EnableIfAllStringAny<[CompiledModel](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4N2ov13CompiledModelE),[Properties](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4IDpENK2ov4Core10read_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKNSt6stringERKNSt6stringEDpRR10Properties)...> read_model(const std::string &model_path, const std::string &bin_path,[Properties](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4IDpENK2ov4Core10read_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKNSt6stringERKNSt6stringEDpRR10Properties)&&... properties) const[#](https://docs.openvino.ai#_CPPv4IDpENK2ov4Core10read_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKNSt6stringERKNSt6stringEDpRR10Properties) Reads models from IR / ONNX / PDPD / TF / TFLite file formats.

- Parameters:
**model_path**– Path to a model.**bin_path**– Path to a data file. For IR format (*.bin):if

`bin_path`

is empty, will try to read a bin file with the same name as xml andif the bin file with the same name is not found, will load IR without weights. For the following file formats the

`bin_path`

parameter is not used:ONNX format (*.onnx)

PDPD (*.pdmodel)

TF (*.pb, *.meta, SavedModel directory)

TFLite (*.tflite)


**properties**– Optional pack of pairs: (property name, property value) relevant only for this read operation.

- Returns:
A model.



Unnamed Group

-
[CompiledModel](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4N2ov13CompiledModelE)compile_model(const std::string &model_path, const AnyMap &properties = {})[#](https://docs.openvino.ai#_CPPv4N2ov4Core13compile_modelERKNSt6stringERK6AnyMap) Reads and loads a compiled model from the IR/ONNX/PDPD file to the default OpenVINO device selected by the AUTO plugin.

This can be more efficient than using the

[Core::read_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1af3143c652debb91411a186281593bb1a)+ Core::compile_model(model_in_memory_object) flow, especially for cases when caching is enabled and a cached model is available.- Parameters:
**model_path**– Path to a model.**properties**– Optional map of pairs: (property name, property value) relevant only for this load operation.

- Returns:
A compiled model.



Unnamed Group

-
template<typename ...Properties>

inline[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4utilE)::EnableIfAllStringAny<[CompiledModel](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4N2ov13CompiledModelE),[Properties](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4IDpEN2ov4Core13compile_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKNSt6stringEDpRR10Properties)...> compile_model(const std::string &model_path,[Properties](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4IDpEN2ov4Core13compile_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKNSt6stringEDpRR10Properties)&&... properties)[#](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core13compile_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKNSt6stringEDpRR10Properties) Reads and loads a compiled model from IR / ONNX / PDPD file to the default OpenVINO device selected by AUTO plugin.

This can be more efficient than using read_model + compile_model(Model) flow especially for cases when caching is enabled and cached model is available

- Template Parameters:
**Properties**– Should be the pack of`std::pair<std::string,`

types[ov::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)>- Parameters:
**model_path**– path to model with string or wstring**properties**– Optional pack of pairs: (property name, property value) relevant only for this load operation

- Returns:
A compiled model



Unnamed Group

-
[CompiledModel](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4N2ov13CompiledModelE)compile_model(const std::string &model_path, const std::string &device_name, const AnyMap &properties = {})[#](https://docs.openvino.ai#_CPPv4N2ov4Core13compile_modelERKNSt6stringERKNSt6stringERK6AnyMap) Reads a model and creates a compiled model from the IR/ONNX/PDPD file.

This can be more efficient than using the

[Core::read_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1af3143c652debb91411a186281593bb1a)+ Core::compile_model(model_in_memory_object) flow, especially for cases when caching is enabled and a cached model is available.- Parameters:
**model_path**– Path to a model.**device_name**– Name of a device to load a model to.**properties**– Optional map of pairs: (property name, property value) relevant only for this load operation.

- Returns:
A compiled model.



Unnamed Group

-
template<typename ...Properties>

inline[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4utilE)::EnableIfAllStringAny<[CompiledModel](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4N2ov13CompiledModelE),[Properties](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4IDpEN2ov4Core13compile_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKNSt6stringERKNSt6stringEDpRR10Properties)...> compile_model(const std::string &model_path, const std::string &device_name,[Properties](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4IDpEN2ov4Core13compile_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKNSt6stringERKNSt6stringEDpRR10Properties)&&... properties)[#](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core13compile_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKNSt6stringERKNSt6stringEDpRR10Properties) Reads a model and creates a compiled model from the IR/ONNX/PDPD file.

This can be more efficient than using read_model + compile_model(Model) flow especially for cases when caching is enabled and cached model is available.

- Template Parameters:
**Properties**– Should be a pack of`std::pair<std::string,`

types.[ov::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)>- Parameters:
**model_path**– Path to a model.**device_name**– Name of a device to load a model to.**properties**– Optional pack of pairs: (property name, property value) relevant only for this load operation.

- Returns:
A compiled model.



Unnamed Group

-
void add_extension(const std::string &library_path)
[#](https://docs.openvino.ai#_CPPv4N2ov4Core13add_extensionERKNSt6stringE) Registers an extension to a

[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)object.- Parameters:
**library_path**– Path to the library with[ov::Extension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_extension).


Public Functions

-
explicit Core(const std::string &xml_config_file = {})
[#](https://docs.openvino.ai#_CPPv4N2ov4Core4CoreERKNSt6stringE) Constructs an OpenVINO

[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)instance with devices and their plugins description.There are two ways how to configure device plugins:

(default) Use XML configuration file in case of dynamic libraries build;

Use strictly defined configuration in case of static libraries build.


- Parameters:
**xml_config_file**– Path to the .xml file with plugins to load from. If path contains only file name with extension, file will be searched in a folder with OpenVINO runtime shared library. If the XML configuration file is not specified, default OpenVINO Runtime plugins are loaded from:(dynamic build) default

`plugins.xml`

file located in the same folder as OpenVINO runtime shared library;(static build) statically defined configuration. In this case path to the .xml file is ignored.




-
std::map<std::string,
[Version](https://docs.openvino.ai/structov_1_1_version.html#_CPPv4N2ov7VersionE)> get_versions(const std::string &device_name) const[#](https://docs.openvino.ai#_CPPv4NK2ov4Core12get_versionsERKNSt6stringE) Returns device plugins version information. Device name can be complex and identify multiple devices at once like

`HETERO:CPU,GPU`

; in this case, std::map contains multiple entries, each per device.- Parameters:
**device_name**– Device name to identify a plugin.- Returns:
A vector of versions.



-
std::shared_ptr<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Model](https://docs.openvino.ai/classov_1_1_model.html#_CPPv4N2ov5ModelE)> read_model(const std::string &model, const[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&weights) const[#](https://docs.openvino.ai#_CPPv4NK2ov4Core10read_modelERKNSt6stringERK6Tensor) Reads models from IR / ONNX / PDPD / TF / TFLite formats.

Note

Created model object shares the weights with the

`weights`

object. Thus, do not create`weights`

on temporary data that can be freed later, since the model constant data will point to an invalid memory.- Parameters:
**model**– String with a model in IR / ONNX / PDPD / TF / TFLite format.**weights**– Shared pointer to a constant tensor with weights. Reading ONNX / PDPD / TF / TFLite models does not support loading weights from the`weights`

tensors.

- Returns:
A model.



Creates and loads a compiled model from a source model to the default OpenVINO device selected by the AUTO plugin.

Users can create as many compiled models as they need and use them simultaneously (up to the limitation of the hardware resources).

- Parameters:
**model**–[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)object acquired from[Core::read_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1af3143c652debb91411a186281593bb1a).**properties**– Optional map of pairs: (property name, property value) relevant only for this load operation.

- Returns:
A compiled model.



Creates and loads a compiled model from a source model to the default OpenVINO device selected by AUTO plugin.

Users can create as many compiled models as they need and use them simultaneously (up to the limitation of the hardware resources)

- Template Parameters:
**Properties**– Should be the pack of`std::pair<std::string,`

types[ov::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)>- Parameters:
**model**–[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)object acquired from[Core::read_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1af3143c652debb91411a186281593bb1a)**properties**– Optional pack of pairs: (property name, property value) relevant only for this load operation

- Returns:
A compiled model



Creates a compiled model from a source model object.

Users can create as many compiled models as they need and use them simultaneously (up to the limitation of the hardware resources).

- Parameters:
**model**–[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)object acquired from[Core::read_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1af3143c652debb91411a186281593bb1a).**device_name**– Name of a device to load a model to.**properties**– Optional map of pairs: (property name, property value) relevant only for this load operation.

- Returns:
A compiled model.



Creates a compiled model from a source model object.

Users can create as many compiled models as they need and use them simultaneously (up to the limitation of the hardware resources)

- Template Parameters:
**Properties**– Should be the pack of`std::pair<std::string,`

types[ov::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)>- Parameters:
**model**–[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)object acquired from[Core::read_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1af3143c652debb91411a186281593bb1a)**device_name**– Name of device to load model to**properties**– Optional pack of pairs: (property name, property value) relevant only for this load operation

- Returns:
A compiled model



-
[CompiledModel](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4N2ov13CompiledModelE)compile_model(const std::string &model, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&weights, const std::string &device_name, const AnyMap &properties = {})[#](https://docs.openvino.ai#_CPPv4N2ov4Core13compile_modelERKNSt6stringERKN2ov6TensorERKNSt6stringERK6AnyMap) Reads a model and creates a compiled model from the IR/ONNX/PDPD memory.

Note

Created model object shares the weights with the

`weights`

object. Thus, do not create`weights`

on temporary data that can be freed later, since the model constant data will point to an invalid memory.- Parameters:
**model**– String with a model in IR/ONNX/PDPD format.**weights**– Shared pointer to a constant tensor with weights. Reading ONNX/PDPD models does not support loading weights from the`weights`

tensors.**device_name**– Name of a device to load a model to.**properties**– Optional map of pairs: (property name, property value) relevant only for this load operation.

- Returns:
A compiled model.



-
template<typename ...Properties>

inline[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4utilE)::EnableIfAllStringAny<[CompiledModel](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4N2ov13CompiledModelE),[Properties](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4IDpEN2ov4Core13compile_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKNSt6stringERKN2ov6TensorERKNSt6stringEDpRR10Properties)...> compile_model(const std::string &model, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&weights, const std::string &device_name,[Properties](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4IDpEN2ov4Core13compile_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKNSt6stringERKN2ov6TensorERKNSt6stringEDpRR10Properties)&&... properties)[#](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core13compile_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKNSt6stringERKN2ov6TensorERKNSt6stringEDpRR10Properties) Reads a model and creates a compiled model from the IR/ONNX/PDPD memory.

Note

Created model object shares the weights with the

`weights`

object. Thus, do not create`weights`

on temporary data that can be freed later, since the model constant data will point to an invalid memory.- Parameters:
**model**– String with a model in IR/ONNX/PDPD format.**weights**– Shared pointer to a constant tensor with weights. Reading ONNX/PDPD models does not support loading weights from the`weights`

tensors.**device_name**– Name of a device to load a model to.

- Template Parameters:
**Properties**– Should be a pack of`std::pair<std::string,`

types.[ov::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)>- Returns:
A compiled model.



Creates a compiled model from a source model within a specified remote context.

- Parameters:
**model**–[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)object acquired from[Core::read_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1af3143c652debb91411a186281593bb1a).**context**– A reference to a[RemoteContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_context)object.**properties**– Optional map of pairs: (property name, property value) relevant only for this load operation.

- Returns:
A compiled model object.



Creates a compiled model from a source model within a specified remote context.

- Template Parameters:
**Properties**– Should be the pack of`std::pair<std::string,`

types[ov::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)>- Parameters:
**model**–[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)object acquired from[Core::read_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1af3143c652debb91411a186281593bb1a)**context**– Pointer to[RemoteContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_context)object**properties**– Optional pack of pairs: (property name, property value) relevant only for this load operation

- Returns:
A compiled model object



Registers an extension to a

[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)object.- Parameters:
**extension**– Pointer to the extension.


Registers extensions to a

[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)object.- Parameters:
**extensions**– Vector of loaded extensions.


-
template<class T, typename std::enable_if<std::is_base_of<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Extension](https://docs.openvino.ai/classov_1_1_extension.html#_CPPv4N2ov9ExtensionE),[T](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4I0_NSt9enable_ifINSt10is_base_ofIN2ov9ExtensionE1TE5valueEbE4typeEEN2ov4Core13add_extensionEvRK1T)>::value, bool>::type = true>

inline void add_extension(const[T](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4I0_NSt9enable_ifINSt10is_base_ofIN2ov9ExtensionE1TE5valueEbE4typeEEN2ov4Core13add_extensionEvRK1T)&extension)[#](https://docs.openvino.ai#_CPPv4I0_NSt9enable_ifINSt10is_base_ofIN2ov9ExtensionE1TE5valueEbE4typeEEN2ov4Core13add_extensionEvRK1T) Registers an extension to a

[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)object.- Parameters:
**extension**–[Extension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_extension)class that is inherited from the[ov::Extension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_extension)class.


-
template<class T, class ...Targs, typename std::enable_if<std::is_base_of<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Extension](https://docs.openvino.ai/classov_1_1_extension.html#_CPPv4N2ov9ExtensionE),[T](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4I0Dp_NSt9enable_ifINSt10is_base_ofIN2ov9ExtensionE1TE5valueEbE4typeEEN2ov4Core13add_extensionEvRK1TDp5Targs)>::value, bool>::type = true>

inline void add_extension(const[T](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4I0Dp_NSt9enable_ifINSt10is_base_ofIN2ov9ExtensionE1TE5valueEbE4typeEEN2ov4Core13add_extensionEvRK1TDp5Targs)&extension,[Targs](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4I0Dp_NSt9enable_ifINSt10is_base_ofIN2ov9ExtensionE1TE5valueEbE4typeEEN2ov4Core13add_extensionEvRK1TDp5Targs)... args)[#](https://docs.openvino.ai#_CPPv4I0Dp_NSt9enable_ifINSt10is_base_ofIN2ov9ExtensionE1TE5valueEbE4typeEEN2ov4Core13add_extensionEvRK1TDp5Targs) Registers extensions to a

[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)object.- Parameters:
**extension**–[Extension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_extension)class that is inherited from the[ov::Extension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_extension)class.**args**– A list of extensions.



-
template<class T, typename std::enable_if<std::is_base_of<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE),[T](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4I0_NSt9enable_ifINSt10is_base_ofIN2ov2op2OpE1TE5valueEbE4typeEEN2ov4Core13add_extensionEvv)>::value, bool>::type = true>

inline void add_extension()[#](https://docs.openvino.ai#_CPPv4I0_NSt9enable_ifINSt10is_base_ofIN2ov2op2OpE1TE5valueEbE4typeEEN2ov4Core13add_extensionEvv) Registers a custom operation inherited from

[ov::op::Op](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1_op).

-
template<class T, class ...Targs, typename std::enable_if<std::is_base_of<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE),[T](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4I0Dp_NSt9enable_ifIXaaNSt10is_base_ofIN2ov2op2OpE1TE5valueEsZ5TargsEbE4typeEEN2ov4Core13add_extensionEvv)>::value && sizeof...([Targs](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4I0Dp_NSt9enable_ifIXaaNSt10is_base_ofIN2ov2op2OpE1TE5valueEsZ5TargsEbE4typeEEN2ov4Core13add_extensionEvv)), bool>::type = true>

inline void add_extension()[#](https://docs.openvino.ai#_CPPv4I0Dp_NSt9enable_ifIXaaNSt10is_base_ofIN2ov2op2OpE1TE5valueEsZ5TargsEbE4typeEEN2ov4Core13add_extensionEvv) Registers custom operations inherited from

[ov::op::Op](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1_op).

-
[CompiledModel](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4N2ov13CompiledModelE)import_model(std::istream &model_stream, const std::string &device_name, const AnyMap &properties = {})[#](https://docs.openvino.ai#_CPPv4N2ov4Core12import_modelERNSt7istreamERKNSt6stringERK6AnyMap) Imports a compiled model from the previously exported one.

- Parameters:
**model_stream**– std::istream input stream containing a model previously exported using the[ov::CompiledModel::export_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model_1ac9978b1d741c47286cba4eeb109effe4)method.**device_name**– Name of a device to import a compiled model for. Note, if`device_name`

device was not used to compile the original mode, an exception is thrown.**properties**– Optional map of pairs: (property name, property value) relevant only for this load operation.

- Returns:
A compiled model.



-
template<typename ...Properties>

inline[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4utilE)::EnableIfAllStringAny<[CompiledModel](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4N2ov13CompiledModelE),[Properties](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4IDpEN2ov4Core12import_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERNSt7istreamERKNSt6stringEDpRR10Properties)...> import_model(std::istream &model_stream, const std::string &device_name,[Properties](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4IDpEN2ov4Core12import_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERNSt7istreamERKNSt6stringEDpRR10Properties)&&... properties)[#](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core12import_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERNSt7istreamERKNSt6stringEDpRR10Properties) Imports a compiled model from the previously exported one.

- Template Parameters:
**Properties**– Should be the pack of`std::pair<std::string,`

types.[ov::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)>- Parameters:
**model_stream**– std::istream input stream containing a model previously exported using the[ov::CompiledModel::export_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model_1ac9978b1d741c47286cba4eeb109effe4)method.**device_name**– Name of a device to import a compiled model for. Note, if`device_name`

device was not used to compile the original mode, an exception is thrown.**properties**– Optional pack of pairs: (property name, property value) relevant only for this load operation.

- Returns:
A compiled model.



-
[CompiledModel](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4N2ov13CompiledModelE)import_model(std::istream &model_stream, const[RemoteContext](https://docs.openvino.ai/classov_1_1_remote_context.html#_CPPv4N2ov13RemoteContextE)&context, const AnyMap &properties = {})[#](https://docs.openvino.ai#_CPPv4N2ov4Core12import_modelERNSt7istreamERK13RemoteContextRK6AnyMap) Imports a compiled model from the previously exported one with the specified remote context.

- Parameters:
**model_stream**– std::istream input stream containing a model previously exported using the[ov::CompiledModel::export_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model_1ac9978b1d741c47286cba4eeb109effe4)method.**context**– A reference to a[RemoteContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_context)object. Note, if the device from`context`

was not used to compile the original mode, an exception is thrown.**properties**– Optional map of pairs: (property name, property value) relevant only for this load operation.

- Returns:
A compiled model.



-
template<typename ...Properties>

inline[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4utilE)::EnableIfAllStringAny<[CompiledModel](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4N2ov13CompiledModelE),[Properties](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4IDpEN2ov4Core12import_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERNSt7istreamERK13RemoteContextDpRR10Properties)...> import_model(std::istream &model_stream, const[RemoteContext](https://docs.openvino.ai/classov_1_1_remote_context.html#_CPPv4N2ov13RemoteContextE)&context,[Properties](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4IDpEN2ov4Core12import_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERNSt7istreamERK13RemoteContextDpRR10Properties)&&... properties)[#](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core12import_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERNSt7istreamERK13RemoteContextDpRR10Properties) Imports a compiled model from the previously exported one with the specified remote context.

- Template Parameters:
**Properties**– Should be the pack of`std::pair<std::string,`

types.[ov::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)>- Parameters:
**model_stream**– std::istream input stream containing a model previously exported using the[ov::CompiledModel::export_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model_1ac9978b1d741c47286cba4eeb109effe4)method.**context**– Pointer to a[RemoteContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_context)object.**properties**– Optional pack of pairs: (property name, property value) relevant only for this load operation.

- Returns:
A compiled model.



-
[CompiledModel](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4N2ov13CompiledModelE)import_model(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&compiled_blob, const std::string &device_name, const AnyMap &properties = {})[#](https://docs.openvino.ai#_CPPv4N2ov4Core12import_modelERKN2ov6TensorERKNSt6stringERK6AnyMap) Imports a compiled model from the previously exported one.

- Parameters:
**compiled_blob**–[ov::Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)input blob containing a model previously exported using the[ov::CompiledModel::export_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model_1ac9978b1d741c47286cba4eeb109effe4)method.**device_name**– Name of a device to import a compiled model for. Note, if`device_name`

device was not used to compile the original mode, an exception is thrown.**properties**– Optional map of pairs: (property name, property value) relevant only for this load operation.

- Returns:
A compiled model.



-
template<typename ...Properties>

inline[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4utilE)::EnableIfAllStringAny<[CompiledModel](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4N2ov13CompiledModelE),[Properties](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4IDpEN2ov4Core12import_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKN2ov6TensorERKNSt6stringEDpRR10Properties)...> import_model(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&compiled_blob, const std::string &device_name,[Properties](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4IDpEN2ov4Core12import_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKN2ov6TensorERKNSt6stringEDpRR10Properties)&&... properties)[#](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core12import_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKN2ov6TensorERKNSt6stringEDpRR10Properties) Imports a compiled model from the previously exported one.

- Template Parameters:
**Properties**– Should be the pack of`std::pair<std::string,`

types.[ov::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)>- Parameters:
**compiled_blob**–[ov::Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)input blob containing a model previously exported using the[ov::CompiledModel::export_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model_1ac9978b1d741c47286cba4eeb109effe4)method.**device_name**– Name of a device to import a compiled model for. Note, if`device_name`

device was not used to compile the original mode, an exception is thrown.**properties**– Optional pack of pairs: (property name, property value) relevant only for this load operation.

- Returns:
A compiled model.



-
[CompiledModel](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4N2ov13CompiledModelE)import_model(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&compiled_blob, const[RemoteContext](https://docs.openvino.ai/classov_1_1_remote_context.html#_CPPv4N2ov13RemoteContextE)&context, const AnyMap &properties = {})[#](https://docs.openvino.ai#_CPPv4N2ov4Core12import_modelERKN2ov6TensorERK13RemoteContextRK6AnyMap) Imports a compiled model from the previously exported one with the specified remote context.

- Parameters:
**compiled_blob**–[ov::Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)input blob containing a model previously exported using the[ov::CompiledModel::export_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model_1ac9978b1d741c47286cba4eeb109effe4)method.**context**– A reference to a[RemoteContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_context)object. Note, if the device from`context`

was not used to compile the original mode, an exception is thrown.**properties**– Optional map of pairs: (property name, property value) relevant only for this load operation.

- Returns:
A compiled model.



-
template<typename ...Properties>

inline[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4utilE)::EnableIfAllStringAny<[CompiledModel](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4N2ov13CompiledModelE),[Properties](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4IDpEN2ov4Core12import_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKN2ov6TensorERK13RemoteContextDpRR10Properties)...> import_model(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&compiled_blob, const[RemoteContext](https://docs.openvino.ai/classov_1_1_remote_context.html#_CPPv4N2ov13RemoteContextE)&context,[Properties](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4IDpEN2ov4Core12import_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKN2ov6TensorERK13RemoteContextDpRR10Properties)&&... properties)[#](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core12import_modelEN4util20EnableIfAllStringAnyI13CompiledModelDp10PropertiesEERKN2ov6TensorERK13RemoteContextDpRR10Properties) Imports a compiled model from the previously exported one with the specified remote context.

- Template Parameters:
**Properties**– Should be the pack of`std::pair<std::string,`

types.[ov::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)>- Parameters:
**compiled_blob**–[ov::Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)input blob containing a model previously exported using the[ov::CompiledModel::export_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model_1ac9978b1d741c47286cba4eeb109effe4)method.**context**– Pointer to a[RemoteContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_context)object.**properties**– Optional pack of pairs: (property name, property value) relevant only for this load operation.

- Returns:
A compiled model.



Query device if it supports the specified model with specified properties.

- Parameters:
**device_name**– Name of a device to query.**model**–[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)object to query.**properties**– Optional map of pairs: (property name, property value).

- Returns:
An object containing a map of pairs an operation name -> a device name supporting this operation.



Queries a device if it supports the specified model with specified properties.

- Template Parameters:
**Properties**– Should be the pack of`std::pair<std::string,`

types.[ov::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)>- Parameters:
**device_name**– Name of a device to query.**model**–[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)object to query.**properties**– Optional pack of pairs: (property name, property value) relevant only for this query operation.

- Returns:
An object containing a map of pairs an operation name -> a device name supporting this operation.



-
void set_property(const AnyMap &properties)
[#](https://docs.openvino.ai#_CPPv4N2ov4Core12set_propertyERK6AnyMap) Sets properties for all the registered devices, acceptable keys can be found in openvino/runtime/properties.hpp.

- Parameters:
**properties**– Map of pairs: (property name, property value).


-
template<typename ...Properties>

inline[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4utilE)::EnableIfAllStringAny<void,[Properties](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4IDpEN2ov4Core12set_propertyEN4util20EnableIfAllStringAnyIvDp10PropertiesEEDpRR10Properties)...> set_property([Properties](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4IDpEN2ov4Core12set_propertyEN4util20EnableIfAllStringAnyIvDp10PropertiesEEDpRR10Properties)&&... properties)[#](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core12set_propertyEN4util20EnableIfAllStringAnyIvDp10PropertiesEEDpRR10Properties) Sets properties for all the registered devices, acceptable keys can be found in openvino/runtime/properties.hpp.

- Template Parameters:
**Properties**– Should be a pack of`std::pair<std::string,`

types.[ov::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)>- Parameters:
**properties**– Optional pack of pairs: property name, property value.


-
void set_property(const std::string &device_name, const AnyMap &properties)
[#](https://docs.openvino.ai#_CPPv4N2ov4Core12set_propertyERKNSt6stringERK6AnyMap) Sets properties for a device, acceptable keys can be found in openvino/runtime/properties.hpp.

- Parameters:
**device_name**– Name of a device.**properties**– Map of pairs: (property name, property value).



-
template<typename ...Properties>

inline[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4utilE)::EnableIfAllStringAny<void,[Properties](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4IDpEN2ov4Core12set_propertyEN4util20EnableIfAllStringAnyIvDp10PropertiesEERKNSt6stringEDpRR10Properties)...> set_property(const std::string &device_name,[Properties](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4IDpEN2ov4Core12set_propertyEN4util20EnableIfAllStringAnyIvDp10PropertiesEERKNSt6stringEDpRR10Properties)&&... properties)[#](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core12set_propertyEN4util20EnableIfAllStringAnyIvDp10PropertiesEERKNSt6stringEDpRR10Properties) Sets properties for a device, acceptable keys can be found in openvino/runtime/properties.hpp.

- Template Parameters:
**Properties**– Should be the pack of`std::pair<std::string,`

types.[ov::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)>- Parameters:
**device_name**– Name of a device.**properties**– Optional pack of pairs: (property name, property value).



-
[Any](https://docs.openvino.ai/classov_1_1_any.html#_CPPv4N2ov3AnyE)get_property(const std::string &device_name, const std::string &name) const[#](https://docs.openvino.ai#_CPPv4NK2ov4Core12get_propertyERKNSt6stringERKNSt6stringE) Gets properties related to device behaviour.

The method extracts information that can be set via the set_property method.

- Parameters:
**device_name**– Name of a device to get a property value.**name**–[Property](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_property)name.

- Returns:
Value of a property corresponding to the property name.



-
[Any](https://docs.openvino.ai/classov_1_1_any.html#_CPPv4N2ov3AnyE)get_property(const std::string &device_name, const std::string &name, const AnyMap &arguments) const[#](https://docs.openvino.ai#_CPPv4NK2ov4Core12get_propertyERKNSt6stringERKNSt6stringERK6AnyMap) Gets properties related to device behaviour.

The method extracts information that can be set via the set_property method.

- Parameters:
**device_name**– Name of a device to get a property value.**name**–[Property](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_property)name.**arguments**– Additional arguments to get a property.

- Returns:
Value of a property corresponding to the property name.



-
inline
[Any](https://docs.openvino.ai/classov_1_1_any.html#_CPPv4N2ov3AnyE)get_property(const std::string &name) const[#](https://docs.openvino.ai#_CPPv4NK2ov4Core12get_propertyERKNSt6stringE) Gets properties related to core behaviour.

The method extracts information that can be set via the set_property method.

- Parameters:
**name**–[Property](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_property)name.- Returns:
Value of a property corresponding to the property name.



-
template<typename T, PropertyMutability M>

inline[T](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4I0_18PropertyMutabilityENK2ov4Core12get_propertyE1TRKNSt6stringERKN2ov8PropertyI1T1MEE)get_property(const std::string &device_name, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Property](https://docs.openvino.ai/classov_1_1_property.html#_CPPv4I0_18PropertyMutabilityEN2ov8PropertyE)<[T](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4I0_18PropertyMutabilityENK2ov4Core12get_propertyE1TRKNSt6stringERKN2ov8PropertyI1T1MEE),[M](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4I0_18PropertyMutabilityENK2ov4Core12get_propertyE1TRKNSt6stringERKN2ov8PropertyI1T1MEE)> &property) const[#](https://docs.openvino.ai#_CPPv4I0_18PropertyMutabilityENK2ov4Core12get_propertyE1TRKNSt6stringERKN2ov8PropertyI1T1MEE) Gets properties related to device behaviour.

The method is needed to request common device or system properties. It can be device name, temperature, and other devices-specific values.


-
template<typename T, PropertyMutability M>

inline[T](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4I0_18PropertyMutabilityENK2ov4Core12get_propertyE1TRKNSt6stringERKN2ov8PropertyI1T1MEERK6AnyMap)get_property(const std::string &device_name, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Property](https://docs.openvino.ai/classov_1_1_property.html#_CPPv4I0_18PropertyMutabilityEN2ov8PropertyE)<[T](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4I0_18PropertyMutabilityENK2ov4Core12get_propertyE1TRKNSt6stringERKN2ov8PropertyI1T1MEERK6AnyMap),[M](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4I0_18PropertyMutabilityENK2ov4Core12get_propertyE1TRKNSt6stringERKN2ov8PropertyI1T1MEERK6AnyMap)> &property, const AnyMap &arguments) const[#](https://docs.openvino.ai#_CPPv4I0_18PropertyMutabilityENK2ov4Core12get_propertyE1TRKNSt6stringERKN2ov8PropertyI1T1MEERK6AnyMap) Gets properties related to device behaviour.

The method is needed to request common device or system properties. It can be device name, temperature, other devices-specific values.


-
template<typename T, PropertyMutability M, typename ...Args>

inline[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4utilE)::EnableIfAllStringAny<[T](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4I0_18PropertyMutabilityDpENK2ov4Core12get_propertyEN4util20EnableIfAllStringAnyI1TDp4ArgsEERKNSt6stringERKN2ov8PropertyI1T1MEEDpRR4Args),[Args](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4I0_18PropertyMutabilityDpENK2ov4Core12get_propertyEN4util20EnableIfAllStringAnyI1TDp4ArgsEERKNSt6stringERKN2ov8PropertyI1T1MEEDpRR4Args)...> get_property(const std::string &device_name, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Property](https://docs.openvino.ai/classov_1_1_property.html#_CPPv4I0_18PropertyMutabilityEN2ov8PropertyE)<[T](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4I0_18PropertyMutabilityDpENK2ov4Core12get_propertyEN4util20EnableIfAllStringAnyI1TDp4ArgsEERKNSt6stringERKN2ov8PropertyI1T1MEEDpRR4Args),[M](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4I0_18PropertyMutabilityDpENK2ov4Core12get_propertyEN4util20EnableIfAllStringAnyI1TDp4ArgsEERKNSt6stringERKN2ov8PropertyI1T1MEEDpRR4Args)> &property,[Args](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4I0_18PropertyMutabilityDpENK2ov4Core12get_propertyEN4util20EnableIfAllStringAnyI1TDp4ArgsEERKNSt6stringERKN2ov8PropertyI1T1MEEDpRR4Args)&&... args) const[#](https://docs.openvino.ai#_CPPv4I0_18PropertyMutabilityDpENK2ov4Core12get_propertyEN4util20EnableIfAllStringAnyI1TDp4ArgsEERKNSt6stringERKN2ov8PropertyI1T1MEEDpRR4Args) Gets properties related to device behaviour.

The method is needed to request common device or system properties. It can be device name, temperature, other devices-specific values.

- Template Parameters:
**T**– Type of a returned value.**M**–[Property](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_property)mutability.**Args**– Set of additional arguments ended with property object variable.

- Parameters:
**device_name**– Name of a device to get a property value.**property**–[Property](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_property)object.**args**– Optional pack of pairs: (argument name, argument value) ended with property object.

- Returns:
[Property](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_property)value.


-
std::vector<std::string> get_available_devices() const
[#](https://docs.openvino.ai#_CPPv4NK2ov4Core21get_available_devicesEv) Returns devices available for inference.

[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)objects go over all registered plugins and ask about available devices.- Returns:
A vector of devices. The devices are returned as { CPU, GPU.0, GPU.1, NPU }. If there is more than one device of a specific type, they are enumerated with the .# suffix. Such enumerated device can later be used as a device name in all

[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)methods like[Core::compile_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a),[Core::query_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1acdf8e64824fe4cf147c3b52ab32c1aab),[Core::set_property](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1aa953cb0a1601dbc9a34ef6ba82b8476e)and so on.


-
void register_plugin(const std::string &plugin, const std::string &device_name, const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::AnyMap &config = {})[#](https://docs.openvino.ai#_CPPv4N2ov4Core15register_pluginERKNSt6stringERKNSt6stringERKN2ov6AnyMapE) Register a new device and plugin that enables this device inside OpenVINO Runtime.

Note

For security purposes it suggested to specify absolute path to register plugin.

- Parameters:
**plugin**– Path (absolute or relative) or name of a plugin. Depending on platform,`plugin`

is wrapped with shared library suffix and prefix to identify library full name. For example, on Linux platform, plugin name specified as`plugin_name`

will be wrapped as`libplugin_name.so`

. Plugin search algorithm:If

`plugin`

points to an exact library path (absolute or relative), it will be used.If

`plugin`

specifies file name (`libplugin_name.so`

) or plugin name (`plugin_name`

), it will be searched by file name (`libplugin_name.so`

) in CWD or in paths pointed by PATH/LD_LIBRARY_PATH/DYLD_LIBRARY_PATH environment variables depending on the platform.

**device_name**– Device name to register a plugin for.**config**– Plugin configuration options



-
void unload_plugin(const std::string &device_name)
[#](https://docs.openvino.ai#_CPPv4N2ov4Core13unload_pluginERKNSt6stringE) Unloads the previously loaded plugin identified by

`device_name`

from OpenVINO Runtime. The method is needed to remove loaded plugin instance and free its resources. If plugin for a specified device has not been created before, the method throws an exception.Note

This method does not remove plugin from the plugins known to OpenVINO

[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)object.- Parameters:
**device_name**– Device name identifying plugin to remove from OpenVINO Runtime.


-
void register_plugins(const std::string &xml_config_file)
[#](https://docs.openvino.ai#_CPPv4N2ov4Core16register_pluginsERKNSt6stringE) Registers a device plugin to the OpenVINO Runtime

[Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)instance using an XML configuration file with plugins description.The XML file has the following structure:

<ie> <plugins> <plugin name="" location=""> <extensions> <extension location=""/> </extensions> <properties> <property key="" value=""/> </properties> </plugin> </plugins> </ie>

`name`

identifies name of a device enabled by a plugin.`location`

specifies absolute path to dynamic library with a plugin. The path can also be relative to XML file directory. It allows having common config for different systems with different configurations.`properties`

are set to a plugin via the[ov::Core::set_property](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1aa953cb0a1601dbc9a34ef6ba82b8476e)method.`extensions`

are set to a plugin via the[ov::Core::add_extension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1adb5929d85ce33c029794f0dbbb23340f)method.

Note

For security purposes it suggested to specify absolute path to register plugin.

- Parameters:
**xml_config_file**– A path to .xml file with plugins to register.


-
[RemoteContext](https://docs.openvino.ai/classov_1_1_remote_context.html#_CPPv4N2ov13RemoteContextE)create_context(const std::string &device_name, const AnyMap &remote_properties)[#](https://docs.openvino.ai#_CPPv4N2ov4Core14create_contextERKNSt6stringERK6AnyMap) Creates a new remote shared context object on the specified accelerator device using specified plugin-specific low-level device API parameters (device handle, pointer, context, etc.).

- Parameters:
**device_name**– Name of a device to create a new shared context on.**remote_properties**– Map of device-specific shared context remote properties.

- Returns:
Reference to a created remote context.



-
template<typename ...Properties>

inline[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4utilE)::EnableIfAllStringAny<[RemoteContext](https://docs.openvino.ai/classov_1_1_remote_context.html#_CPPv4N2ov13RemoteContextE),[Properties](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4IDpEN2ov4Core14create_contextEN4util20EnableIfAllStringAnyI13RemoteContextDp10PropertiesEERKNSt6stringEDpRR10Properties)...> create_context(const std::string &device_name,[Properties](https://docs.openvino.ai/classov_1_1_core.html#_CPPv4IDpEN2ov4Core14create_contextEN4util20EnableIfAllStringAnyI13RemoteContextDp10PropertiesEERKNSt6stringEDpRR10Properties)&&... remote_properties)[#](https://docs.openvino.ai#_CPPv4IDpEN2ov4Core14create_contextEN4util20EnableIfAllStringAnyI13RemoteContextDp10PropertiesEERKNSt6stringEDpRR10Properties) Creates a new shared context object on specified accelerator device using specified plugin-specific low level device API properties (device handle, pointer, etc.)

- Template Parameters:
**Properties**– Should be the pack of`std::pair<std::string,`

types[ov::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)>- Parameters:
**device_name**– Name of a device to create new shared context on.**remote_properties**– Pack of device-specific shared context remote properties.

- Returns:
A shared pointer to a created remote context.



-
[RemoteContext](https://docs.openvino.ai/classov_1_1_remote_context.html#_CPPv4N2ov13RemoteContextE)get_default_context(const std::string &device_name)[#](https://docs.openvino.ai#_CPPv4N2ov4Core19get_default_contextERKNSt6stringE) Gets a pointer to default (plugin-supplied) shared context object for the specified accelerator device.

- Parameters:
**device_name**– Name of a device to get a default shared context from.- Returns:
Reference to a default remote context.



-
std::shared_ptr<

-
class Cancelled : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Exception](https://docs.openvino.ai/classov_1_1_exception.html#_CPPv4N2ov9ExceptionE)[#](https://docs.openvino.ai#_CPPv4N2ov9CancelledE) *#include <exception.hpp>*Thrown in case of cancelled asynchronous operation.


-
class Busy : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Exception](https://docs.openvino.ai/classov_1_1_exception.html#_CPPv4N2ov9ExceptionE)[#](https://docs.openvino.ai#_CPPv4N2ov4BusyE) *#include <exception.hpp>*Thrown in case of calling the

[InferRequest](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_infer_request)methods while the request is busy with compute operation.

-
class InferRequest
[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequestE) *#include <infer_request.hpp>*This is a class of infer request that can be run in asynchronous or synchronous manners.

Public Functions

-
InferRequest() = default
[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest12InferRequestEv) Default constructor.


-
InferRequest(const
[InferRequest](https://docs.openvino.ai/classov_1_1_infer_request.html#_CPPv4N2ov12InferRequest12InferRequestERK12InferRequest)&other) = default[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest12InferRequestERK12InferRequest) Default copy constructor.

- Parameters:
**other**– Another[InferRequest](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_infer_request)object.


-
[InferRequest](https://docs.openvino.ai/classov_1_1_infer_request.html#_CPPv4N2ov12InferRequestE)&operator=(const[InferRequest](https://docs.openvino.ai/classov_1_1_infer_request.html#_CPPv4N2ov12InferRequestE)&other) = default[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequestaSERK12InferRequest) Default copy assignment operator.

- Parameters:
**other**– Another[InferRequest](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_infer_request)object.- Returns:
Reference to the current object.



-
InferRequest(
[InferRequest](https://docs.openvino.ai/classov_1_1_infer_request.html#_CPPv4N2ov12InferRequest12InferRequestERR12InferRequest)&&other) = default[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest12InferRequestERR12InferRequest) Default move constructor.

- Parameters:
**other**– Another[InferRequest](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_infer_request)object.


-
[InferRequest](https://docs.openvino.ai/classov_1_1_infer_request.html#_CPPv4N2ov12InferRequestE)&operator=([InferRequest](https://docs.openvino.ai/classov_1_1_infer_request.html#_CPPv4N2ov12InferRequestE)&&other) = default[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequestaSERR12InferRequest) Default move assignment operator.

- Parameters:
**other**– Another[InferRequest](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_infer_request)object.- Returns:
Reference to the current object.



-
~InferRequest()
[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequestD0Ev) Destructor that preserves unloading order of implementation object and reference to the library.

Note

To preserve destruction order inside the default generated assignment operator,

`_impl`

is stored before`_so`

. Use the destructor to remove implementation object before referencing to the library explicitly.

-
void set_tensor(const std::string &tensor_name, const
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&tensor)[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest10set_tensorERKNSt6stringERK6Tensor) Sets an input/output tensor to infer on.

- Parameters:
**tensor_name**– Name of the input or output tensor.**tensor**– Reference to the tensor. The element_type and shape of the tensor must match the model’s input/output element_type and size.



-
void set_tensor(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &port, const[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&tensor)[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest10set_tensorERKN2ov6OutputIKN2ov4NodeEEERK6Tensor) Sets an input/output tensor to infer.

- Parameters:
**port**– Port of the input or output tensor. Use the following methods to get the ports:**tensor**– Reference to a tensor. The element_type and shape of a tensor must match the model’s input/output element_type and size.



-
void set_tensor(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &port, const[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&tensor)[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest10set_tensorERKN2ov6OutputIN2ov4NodeEEERK6Tensor) Sets an input/output tensor to infer.

- Parameters:
**port**– Port of the input or output tensor. Use the following methods to get the ports:**tensor**– Reference to a tensor. The element_type and shape of a tensor must match the model’s input/output element_type and size.



-
void set_tensors(const std::string &tensor_name, const std::vector<
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)> &tensors)[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest11set_tensorsERKNSt6stringERKNSt6vectorI6TensorEE) Sets a batch of tensors for input data to infer by tensor name.

[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)input must have batch dimension, and the number of`tensors`

must match the batch size. The current version supports setting tensors to model inputs only. If`tensor_name`

is associated with output (or any other non-input node), an exception is thrown.- Parameters:
**tensor_name**– Name of the input tensor.**tensors**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensors for batched infer request. The type of each tensor must match the model input element type and shape (except batch dimension). Total size of tensors must match the input size.



-
void set_tensors(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &port, const std::vector<[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)> &tensors)[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest11set_tensorsERKN2ov6OutputIKN2ov4NodeEEERKNSt6vectorI6TensorEE) Sets a batch of tensors for input data to infer by input port.

[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)input must have batch dimension, and the number of`tensors`

must match the batch size. The current version supports setting tensors to model inputs only. If`port`

is associated with output (or any other non-input node), an exception is thrown.- Parameters:
**port**– Port of the input tensor.**tensors**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensors for batched infer request. The type of each tensor must match the model input element type and shape (except batch dimension). Total size of tensors must match the input size.



-
void set_input_tensor(size_t idx, const
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&tensor)[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest16set_input_tensorE6size_tRK6Tensor) Sets an input tensor to infer.

- Parameters:
**idx**– Index of the input tensor. If`idx`

is greater than the number of model inputs, an exception is thrown.**tensor**– Reference to the tensor. The element_type and shape of the tensor must match the model’s input/output element_type and size.



-
void set_input_tensor(const
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&tensor)[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest16set_input_tensorERK6Tensor) Sets an input tensor to infer models with single input.

Note

If model has several inputs, an exception is thrown.

- Parameters:
**tensor**– Reference to the input tensor.


-
void set_input_tensors(const std::vector<
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)> &tensors)[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest17set_input_tensorsERKNSt6vectorI6TensorEE) Sets a batch of tensors for single input data.

[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)input must have batch dimension, and the number of`tensors`

must match the batch size.- Parameters:
**tensors**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensors for batched infer request. The type of each tensor must match the model input element type and shape (except batch dimension). Total size of tensors must match the input size.


-
void set_input_tensors(size_t idx, const std::vector<
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)> &tensors)[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest17set_input_tensorsE6size_tRKNSt6vectorI6TensorEE) Sets a batch of tensors for input data to infer by input name.

[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)input must have batch dimension, and number of`tensors`

must match the batch size.- Parameters:
**idx**– Name of the input tensor.**tensors**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensors for batched infer request. The type of each tensor must match the model input element type and shape (except batch dimension). Total size of tensors must match the input size.



-
void set_output_tensor(size_t idx, const
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&tensor)[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest17set_output_tensorE6size_tRK6Tensor) Sets an output tensor to infer.

Note

Index of the input preserved accross

[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model),[ov::CompiledModel](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model), and[ov::InferRequest](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_infer_request).- Parameters:
**idx**– Index of the output tensor.**tensor**– Reference to the output tensor. The type of the tensor must match the model output element type and shape.



-
void set_output_tensor(const
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&tensor)[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest17set_output_tensorERK6Tensor) Sets an output tensor to infer models with single output.

Note

If model has several outputs, an exception is thrown.

- Parameters:
**tensor**– Reference to the output tensor.


-
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)get_tensor(const std::string &tensor_name)[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest10get_tensorERKNSt6stringE) Gets an input/output tensor for inference by tensor name.

- Parameters:
**tensor_name**– Name of a tensor to get.- Returns:
The tensor with name

`tensor_name`

. If the tensor is not found, an exception is thrown.


-
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)get_tensor(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &port)[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest10get_tensorERKN2ov6OutputIKN2ov4NodeEEE) Gets an input/output tensor for inference.

Note

If the tensor with the specified

`port`

is not found, an exception is thrown.- Parameters:
**port**– Port of the tensor to get.- Returns:
[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)for the port`port`

.


-
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)get_tensor(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &port)[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest10get_tensorERKN2ov6OutputIN2ov4NodeEEE) Gets an input/output tensor for inference.

Note

If the tensor with the specified

`port`

is not found, an exception is thrown.- Parameters:
**port**– Port of the tensor to get.- Returns:
[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)for the port`port`

.


-
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)get_input_tensor(size_t idx)[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest16get_input_tensorE6size_t) Gets an input tensor for inference.

- Parameters:
**idx**– Index of the tensor to get.- Returns:
[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)with the input index`idx`

. If the tensor with the specified`idx`

is not found, an exception is thrown.


-
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)get_input_tensor()[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest16get_input_tensorEv) Gets an input tensor for inference.

- Returns:
The input tensor for the model. If model has several inputs, an exception is thrown.



-
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)get_output_tensor(size_t idx)[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest17get_output_tensorE6size_t) Gets an output tensor for inference.

- Parameters:
**idx**– Index of the tensor to get.- Returns:
[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)with the output index`idx`

. If the tensor with the specified`idx`

is not found, an exception is thrown.


-
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)get_output_tensor()[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest17get_output_tensorEv) Gets an output tensor for inference.

- Returns:
[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)tensor for the model. If model has several outputs, an exception is thrown.


-
void infer()
[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest5inferEv) Infers specified input(s) in synchronous mode.

Note

It blocks all methods of

[InferRequest](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_infer_request)while request is ongoing (running or waiting in a queue). Calling any method leads to throwing the[ov::Busy](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_busy)exception.

-
void cancel()
[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest6cancelEv) Cancels inference request.


-
std::vector<
[ProfilingInfo](https://docs.openvino.ai/structov_1_1_profiling_info.html#_CPPv4N2ov13ProfilingInfoE)> get_profiling_info() const[#](https://docs.openvino.ai#_CPPv4NK2ov12InferRequest18get_profiling_infoEv) Queries performance measures per layer to identify the most time consuming operation.

Note

Not all plugins provide meaningful data.

- Returns:
Vector of profiling information for operations in a model.



-
void start_async()
[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest11start_asyncEv) Starts inference of specified input(s) in asynchronous mode.

Note

It returns immediately. Inference starts also immediately. Calling any method while the request in a running state leads to throwing the

[ov::Busy](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_busy)exception.

-
void wait()
[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest4waitEv) Waits for the result to become available. Blocks until the result becomes available.


-
bool wait_for(const std::chrono::milliseconds timeout)
[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest8wait_forEKNSt6chrono12millisecondsE) Waits for the result to become available. Blocks until the specified timeout has elapsed or the result becomes available, whichever comes first.

- Parameters:
**timeout**– Maximum duration, in milliseconds, to block for.- Returns:
True if inference request is ready and false, otherwise.



-
void set_callback(std::function<void(std::exception_ptr)> callback)
[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest12set_callbackENSt8functionIFvNSt13exception_ptrEEEE) Sets a callback std::function that is called on success or failure of an asynchronous request.

Warning

Do not capture strong references to OpenVINO runtime objects into callback. Following objects should not be captured like:

ov::ExecutableNetwork

[ov::Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)As specified objects implement shared reference concept do not capture this objects by value. It can lead to memory leaks or undefined behaviour! Try to use weak references or pointers.

- Parameters:
**callback**– callback object which will be called on when inference finish.


-
std::vector<
[VariableState](https://docs.openvino.ai/classov_1_1_variable_state.html#_CPPv4N2ov13VariableStateE)> query_state()[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest11query_stateEv) Gets state control interface for the given infer request.

State control essential for recurrent models.

- Returns:
Vector of Variable State objects.



-
void reset_state()
[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest11reset_stateEv) Resets all internal variable states for relevant infer request to a value specified as default for the corresponding

`ReadValue`

node.

-
[CompiledModel](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4N2ov13CompiledModelE)get_compiled_model()[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest18get_compiled_modelEv) Returns a compiled model that creates this inference request.

- Returns:
Compiled model object.



-
bool operator!() const noexcept
[#](https://docs.openvino.ai#_CPPv4NK2ov12InferRequestntEv) Checks if the current

[InferRequest](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_infer_request)object is not initialized.- Returns:
True if the current

[InferRequest](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_infer_request)object is not initialized; false, otherwise.


-
explicit operator bool() const noexcept
[#](https://docs.openvino.ai#_CPPv4NK2ov12InferRequestcvbEv) Checks if the current

[InferRequest](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_infer_request)object is initialized.- Returns:
True if the current

[InferRequest](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_infer_request)object is initialized; false, otherwise.


-
bool operator!=(const
[InferRequest](https://docs.openvino.ai/classov_1_1_infer_request.html#_CPPv4N2ov12InferRequestE)&other) const noexcept[#](https://docs.openvino.ai#_CPPv4NK2ov12InferRequestneERK12InferRequest) Compares whether this request wraps the same impl underneath.

- Parameters:
**other**– Another inference request.- Returns:
True if the current

[InferRequest](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_infer_request)object does not wrap the same impl as the operator’s arg.


-
bool operator==(const
[InferRequest](https://docs.openvino.ai/classov_1_1_infer_request.html#_CPPv4N2ov12InferRequestE)&other) const noexcept[#](https://docs.openvino.ai#_CPPv4NK2ov12InferRequesteqERK12InferRequest) Compares whether this request wraps the same impl underneath.

- Parameters:
**other**– Another inference request.- Returns:
True if the current

[InferRequest](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_infer_request)object wraps the same impl as the operator’s arg.


-
InferRequest() = default

-
class RemoteContext
[#](https://docs.openvino.ai#_CPPv4N2ov13RemoteContextE) *#include <remote_context.hpp>*This class represents an abstraction

for remote (non-CPU) accelerator device-specific inference context. Such context represents a scope on the device within which compiled models and remote memory tensors can exist, function, and exchange data.

Subclassed by

[ov::intel_gpu::ocl::ClContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__gpu_1_1ocl_1_1_cl_context),[ov::intel_npu::level_zero::ZeroContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__npu_1_1level__zero_1_1_zero_context)Public Functions

-
RemoteContext() = default
[#](https://docs.openvino.ai#_CPPv4N2ov13RemoteContext13RemoteContextEv) Default constructor.


-
RemoteContext(const
[RemoteContext](https://docs.openvino.ai/classov_1_1_remote_context.html#_CPPv4N2ov13RemoteContext13RemoteContextERK13RemoteContext)&other) = default[#](https://docs.openvino.ai#_CPPv4N2ov13RemoteContext13RemoteContextERK13RemoteContext) Default copy constructor.

- Parameters:
**other**– Another[RemoteContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_context)object.


-
[RemoteContext](https://docs.openvino.ai/classov_1_1_remote_context.html#_CPPv4N2ov13RemoteContextE)&operator=(const[RemoteContext](https://docs.openvino.ai/classov_1_1_remote_context.html#_CPPv4N2ov13RemoteContextE)&other) = default[#](https://docs.openvino.ai#_CPPv4N2ov13RemoteContextaSERK13RemoteContext) Default copy assignment operator.

- Parameters:
**other**– Another[RemoteContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_context)object.- Returns:
Reference to the current object.



-
RemoteContext(
[RemoteContext](https://docs.openvino.ai/classov_1_1_remote_context.html#_CPPv4N2ov13RemoteContext13RemoteContextERR13RemoteContext)&&other) = default[#](https://docs.openvino.ai#_CPPv4N2ov13RemoteContext13RemoteContextERR13RemoteContext) Default move constructor.

- Parameters:
**other**– Another[RemoteContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_context)object.


-
[RemoteContext](https://docs.openvino.ai/classov_1_1_remote_context.html#_CPPv4N2ov13RemoteContextE)&operator=([RemoteContext](https://docs.openvino.ai/classov_1_1_remote_context.html#_CPPv4N2ov13RemoteContextE)&&other) = default[#](https://docs.openvino.ai#_CPPv4N2ov13RemoteContextaSERR13RemoteContext) Default move assignment operator.

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

inline const[T](https://docs.openvino.ai/classov_1_1_remote_context.html#_CPPv4I0ENK2ov13RemoteContext2asEK1Tv)as() const[#](https://docs.openvino.ai#_CPPv4I0ENK2ov13RemoteContext2asEK1Tv) Casts this

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
[RemoteContext](https://docs.openvino.ai/classov_1_1_remote_context.html#_CPPv4N2ov13RemoteContextE)&remote_context, const std::map<std::string, std::vector<std::string>> &type_info = {})[#](https://docs.openvino.ai#_CPPv4N2ov13RemoteContext10type_checkERK13RemoteContextRKNSt3mapINSt6stringENSt6vectorINSt6stringEEEEE) Internal method: checks remote type.

- Parameters:
**remote_context**– Remote context which type is checked.**type_info**– Map with remote object runtime info.

- Throws:
[Exception](https://docs.openvino.ai/classov_1_1_exception.html#_CPPv4N2ov9ExceptionE)– if type check with the specified parameters failed.


-
RemoteContext() = default

-
class RemoteTensor : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)[#](https://docs.openvino.ai#_CPPv4N2ov12RemoteTensorE) *#include <remote_tensor.hpp>*Remote memory access and interoperability API.

Subclassed by

[ov::intel_gpu::ocl::ClBufferTensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__gpu_1_1ocl_1_1_cl_buffer_tensor),[ov::intel_gpu::ocl::ClImage2DTensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__gpu_1_1ocl_1_1_cl_image2_d_tensor),[ov::intel_gpu::ocl::USMTensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__gpu_1_1ocl_1_1_u_s_m_tensor),[ov::intel_npu::level_zero::ZeroBufferTensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1intel__npu_1_1level__zero_1_1_zero_buffer_tensor)Public Functions

-
RemoteTensor() = default
[#](https://docs.openvino.ai#_CPPv4N2ov12RemoteTensor12RemoteTensorEv) Default constructor.


-
RemoteTensor(const
[RemoteTensor](https://docs.openvino.ai/classov_1_1_remote_tensor.html#_CPPv4N2ov12RemoteTensor12RemoteTensorERK12RemoteTensorRK10CoordinateRK10Coordinate)&other, const[Coordinate](https://docs.openvino.ai/classov_1_1_coordinate.html#_CPPv4N2ov10CoordinateE)&begin, const[Coordinate](https://docs.openvino.ai/classov_1_1_coordinate.html#_CPPv4N2ov10CoordinateE)&end)[#](https://docs.openvino.ai#_CPPv4N2ov12RemoteTensor12RemoteTensorERK12RemoteTensorRK10CoordinateRK10Coordinate) Constructs region of interest (ROI) tensor from another remote tensor.

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

-
class VariableState
[#](https://docs.openvino.ai#_CPPv4N2ov13VariableStateE) *#include <variable_state.hpp>*[VariableState](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_variable_state)class.Public Functions

-
VariableState() = default
[#](https://docs.openvino.ai#_CPPv4N2ov13VariableState13VariableStateEv) Default constructor.


-
~VariableState()
[#](https://docs.openvino.ai#_CPPv4N2ov13VariableStateD0Ev) Destructor that preserves unloading order of implementation object and reference to the library.


-
void reset()
[#](https://docs.openvino.ai#_CPPv4N2ov13VariableState5resetEv) Resets internal variable state for relevant infer request to a value specified as default for the corresponding ReadValue node.


-
std::string get_name() const
[#](https://docs.openvino.ai#_CPPv4NK2ov13VariableState8get_nameEv) Gets the name of the current variable state. If length of an array is not enough, the name is truncated by len, null terminator is inserted as well.

`variable_id`

from the corresponding`ReadValue`

is used as variable state name.- Returns:
A string representing state name.



-
VariableState() = default

-
struct ProfilingInfo
[#](https://docs.openvino.ai#_CPPv4N2ov13ProfilingInfoE) *#include <profiling_info.hpp>*Represents basic inference profiling information per operation.

If the operation is executed using tiling, the sum time per each tile is indicated as the total execution time. Due to parallel execution, the total execution time for all nodes might be greater than the total inference time.

Public Types


-
using SupportedOpsMap = std::map<std::string, std::string>