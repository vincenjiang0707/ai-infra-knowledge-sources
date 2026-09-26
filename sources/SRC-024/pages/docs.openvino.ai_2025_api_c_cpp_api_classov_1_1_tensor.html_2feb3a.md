source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_tensor.html
lastmod: 

# Class ov::Tensor[#](https://docs.openvino.ai#class-ov-tensor)

-
class Tensor
[#](https://docs.openvino.ai#_CPPv4N2ov6TensorE) [Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)API holding host memory It can throw exceptions safely for the application, where it is properly handled.Subclassed by

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
[Tensor](https://docs.openvino.ai#_CPPv4N2ov6Tensor6TensorERK6Tensor)&other) = default[#](https://docs.openvino.ai#_CPPv4N2ov6Tensor6TensorERK6Tensor) Default copy constructor.

- Parameters:
**other**– other[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)object


-
[Tensor](https://docs.openvino.ai#_CPPv4N2ov6TensorE)&operator=(const[Tensor](https://docs.openvino.ai#_CPPv4N2ov6TensorE)&other) = default[#](https://docs.openvino.ai#_CPPv4N2ov6TensoraSERK6Tensor) Default copy assignment operator.

- Parameters:
**other**– other[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)object- Returns:
reference to the current object



-
[Tensor](https://docs.openvino.ai#_CPPv4N2ov6TensorE)&operator=([Tensor](https://docs.openvino.ai#_CPPv4N2ov6TensorE)&&other) = default[#](https://docs.openvino.ai#_CPPv4N2ov6TensoraSERR6Tensor) Default move assignment operator.

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
[Tensor](https://docs.openvino.ai#_CPPv4N2ov6Tensor6TensorERK6TensorRK10CoordinateRK10Coordinate)&other, const[Coordinate](https://docs.openvino.ai/classov_1_1_coordinate.html#_CPPv4N2ov10CoordinateE)&begin, const[Coordinate](https://docs.openvino.ai/classov_1_1_coordinate.html#_CPPv4N2ov10CoordinateE)&end)[#](https://docs.openvino.ai#_CPPv4N2ov6Tensor6TensorERK6TensorRK10CoordinateRK10Coordinate) Constructs region of interest (ROI) tensor form another tensor.

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
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Tensor](https://docs.openvino.ai#_CPPv4N2ov6TensorE)dst) const[#](https://docs.openvino.ai#_CPPv4NK2ov6Tensor7copy_toEN2ov6TensorE) Copy tensor, destination tensor should have the same element type and shape.

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

inline std::enable_if_t<std::is_base_of_v<[Tensor](https://docs.openvino.ai#_CPPv4N2ov6TensorE),[T](https://docs.openvino.ai#_CPPv4I0ENK2ov6Tensor2isENSt11enable_if_tINSt12is_base_of_vI6Tensor1TEEbEEv)>, bool> is() const noexcept[#](https://docs.openvino.ai#_CPPv4I0ENK2ov6Tensor2isENSt11enable_if_tINSt12is_base_of_vI6Tensor1TEEbEEv) Checks if the

[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)object can be cast to the type T.- Template Parameters:
**T**– Type to be checked. Must represent a class derived from the[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)- Returns:
true if this object can be dynamically cast to the type const T*. Otherwise, false



-
void *data() const