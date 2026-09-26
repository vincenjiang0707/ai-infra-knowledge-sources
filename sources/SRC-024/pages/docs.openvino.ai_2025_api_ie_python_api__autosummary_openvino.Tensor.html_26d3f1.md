source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.Tensor.html
lastmod: 

# openvino.Tensor[#](https://docs.openvino.ai#openvino-tensor)

-
*class*openvino.Tensor[#](https://docs.openvino.ai#openvino.Tensor) Bases:

`pybind11_object`

openvino.Tensor holding either copy of memory or shared host memory.

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.Tensor.__init__) Overloaded function.

__init__(self: openvino._pyopenvino.Tensor, array: numpy.ndarray, shared_memory: bool = False) -> None

Tensor’s special constructor.

- param array:
Array to create the tensor from.

- type array:
numpy.array

- param shared_memory:
If True, this Tensor memory is being shared with a host. Any action performed on the host memory is reflected on this Tensor’s memory! If False, data is being copied to this Tensor. Requires data to be C_CONTIGUOUS if True. If the passed array contains strings, the flag must be set to

[`](https://docs.openvino.ai#id1)False’.- type shared_memory:
bool


__init__(self: openvino._pyopenvino.Tensor, array: numpy.ndarray, shape: openvino._pyopenvino.Shape, type: openvino._pyopenvino.Type = <Type: ‘dynamic’>) -> None

Another Tensor’s special constructor.

Represents array in the memory with given shape and element type. It’s recommended to use this constructor only for wrapping array’s memory with the specific openvino element type parameter.

- param array:
C_CONTIGUOUS numpy array which will be wrapped in openvino.Tensor with given parameters (shape and element_type). Array’s memory is being shared with a host. Any action performed on the host memory will be reflected on this Tensor’s memory!

- type array:
numpy.array

- param shape:
Shape of the new tensor.

- type shape:
openvino.Shape

- param type:
Element type

- type type:
openvino.Type

- Example:

import openvino as ov import numpy as np arr = np.array(shape=(100), dtype=np.uint8) t = ov.Tensor(arr, ov.Shape([100, 8]), ov.Type.u1)

__init__(self: openvino._pyopenvino.Tensor, array: numpy.ndarray, shape: collections.abc.Sequence[typing.SupportsInt], type: openvino._pyopenvino.Type = <Type: ‘dynamic’>) -> None

Another Tensor’s special constructor.

Represents array in the memory with given shape and element type. It’s recommended to use this constructor only for wrapping array’s memory with the specific openvino element type parameter.

- param array:
C_CONTIGUOUS numpy array which will be wrapped in openvino.Tensor with given parameters (shape and element_type). Array’s memory is being shared with a host. Any action performed on the host memory will be reflected on this Tensor’s memory!

- type array:
numpy.array

- param shape:
Shape of the new tensor.

- type shape:
list or tuple

- param type:
Element type.

- type type:
openvino.Type

- Example:

import openvino as ov import numpy as np arr = np.array(shape=(100), dtype=np.uint8) t = ov.Tensor(arr, [100, 8], ov.Type.u1)

__init__(self: openvino._pyopenvino.Tensor, list: list) -> None

Tensor’s special constructor.

Creates a Tensor from a given Python list. Warning: It is always a copy of list’s data!

- param array:
list to create the tensor from.

- type array:
list[int, float, str]


__init__(self: openvino._pyopenvino.Tensor, type: openvino._pyopenvino.Type, shape: openvino._pyopenvino.Shape) -> None

__init__(self: openvino._pyopenvino.Tensor, type: openvino._pyopenvino.Type, shape: collections.abc.Sequence[typing.SupportsInt]) -> None

__init__(self: openvino._pyopenvino.Tensor, type: numpy.dtype, shape: collections.abc.Sequence[typing.SupportsInt]) -> None

__init__(self: openvino._pyopenvino.Tensor, type: object, shape: collections.abc.Sequence[typing.SupportsInt]) -> None

__init__(self: openvino._pyopenvino.Tensor, type: numpy.dtype, shape: openvino._pyopenvino.Shape) -> None

__init__(self: openvino._pyopenvino.Tensor, type: object, shape: openvino._pyopenvino.Shape) -> None

__init__(self: openvino._pyopenvino.Tensor, port: openvino._pyopenvino.Output) -> None

Constructs Tensor using port from node. Type and shape will be taken from the port.

- param port:
Output port from a node.

- type param:
openvino.Output


__init__(self: openvino._pyopenvino.Tensor, port: openvino._pyopenvino.Output, array: numpy.ndarray) -> None

Constructs Tensor using port from node. Type and shape will be taken from the port.

- param port:
Output port from a node.

- type param:
openvino.Output

- param array:
C_CONTIGUOUS numpy array which will be wrapped in openvino.Tensor. Array’s memory is being shared wi a host. Any action performed on the host memory will be reflected on this Tensor’s memory!

- type array:
numpy.array


__init__(self: openvino._pyopenvino.Tensor, port: ov::Output<ov::Node const>) -> None

Constructs Tensor using port from node. Type and shape will be taken from the port.

- param port:
Output port from a node.

- type param:
openvino.ConstOutput


__init__(self: openvino._pyopenvino.Tensor, port: ov::Output<ov::Node const>, array: numpy.ndarray) -> None

Constructs Tensor using port from node. Type and shape will be taken from the port.

- param port:
Output port from a node.

- type param:
openvino.ConstOutput

- param array:
C_CONTIGUOUS numpy array which will be wrapped in openvino.Tensor. Array’s memory is being shared with a host. Any action performed on the host memory will be reflected on this Tensor’s memory!

- type array:
numpy.array


__init__(self: openvino._pyopenvino.Tensor, other: openvino._pyopenvino.Tensor, begin: openvino._pyopenvino.Coordinate, end: openvino._pyopenvino.Coordinate) -> None

__init__(self: openvino._pyopenvino.Tensor, other: openvino._pyopenvino.Tensor, begin: collections.abc.Sequence[typing.SupportsInt], end: collections.abc.Sequence[typing.SupportsInt]) -> None

__init__(self: openvino._pyopenvino.Tensor, image: object) -> None

Constructs Tensor from a Pillow Image.

- param image:
Pillow Image to create the tensor from.

- type image:
PIL.Image.Image

- Example:

from PIL import Image import openvino as ov img = Image.open("example.jpg") tensor = ov.Tensor(img)



Methods

(self)`__copy__`

(self, arg0)`__deepcopy__`

(name, /)`__delattr__`

Implement delattr(self, name).

()`__dir__`

Default dir() implementation.

(value, /)`__eq__`

Return self==value.

(format_spec, /)`__format__`

Default object formatter.

(value, /)`__ge__`

Return self>=value.

(name, /)`__getattribute__`

Return getattr(self, name).

Helper for pickle.

(value, /)`__gt__`

Return self>value.

()`__hash__`

Return hash(self).

(*args, **kwargs)`__init__`

Overloaded function.

This method is called when a class is subclassed.

(value, /)`__le__`

Return self<=value.

(value, /)`__lt__`

Return self<value.

(value, /)`__ne__`

Return self!=value.

(**kwargs)`__new__`

Helper for pickle.

(protocol, /)`__reduce_ex__`

Helper for pickle.

(self)`__repr__`

(name, value, /)`__setattr__`

Implement setattr(self, name, value).

Size of object in memory, in bytes.

()`__str__`

Return str(self).

Abstract classes can override this to customize issubclass().

(*args, **kwargs)`copy_from`

Overloaded function.

(*args, **kwargs)`copy_to`

Overloaded function.

(self)`get_byte_size`

Gets Tensor's size in bytes.

(self)`get_element_type`

Gets Tensor's element type.

(self)`get_shape`

Gets Tensor's shape.

(self)`get_size`

Gets Tensor's size as total number of elements.

(self)`get_strides`

Gets Tensor's strides in bytes.

(self)`is_continuous`

Reports whether the tensor is continuous or not.

(*args, **kwargs)`set_shape`

Overloaded function.

Attributes

Tensor's size in bytes.

Access to Tensor's data with string Type in np.bytes_ dtype.

Access to Tensor's data.

Tensor's element type.

Tensor's shape get/set.

Tensor's size as total number of elements.

Access to Tensor's data with string Type in np.str_ dtype.

Tensor's strides in bytes.

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.Tensor.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.Tensor.__class__) alias of

`pybind11_type`


-
__copy__(
*self:*)[openvino._pyopenvino.Tensor](https://docs.openvino.ai#openvino.Tensor)[openvino._pyopenvino.Tensor](https://docs.openvino.ai#openvino.Tensor)[#](https://docs.openvino.ai#openvino.Tensor.__copy__)

-
__deepcopy__(
*self:*,[openvino._pyopenvino.Tensor](https://docs.openvino.ai#openvino.Tensor)*arg0: dict*)[openvino._pyopenvino.Tensor](https://docs.openvino.ai#openvino.Tensor)[#](https://docs.openvino.ai#openvino.Tensor.__deepcopy__)

-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.Tensor.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.Tensor.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Tensor.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.Tensor.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Tensor.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.Tensor.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino.Tensor.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Tensor.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino.Tensor.__hash__) Return hash(self).


-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0) Overloaded function.

__init__(self: openvino._pyopenvino.Tensor, array: numpy.ndarray, shared_memory: bool = False) -> None

Tensor’s special constructor.

- param array:
Array to create the tensor from.

- type array:
numpy.array

- param shared_memory:
If True, this Tensor memory is being shared with a host. Any action performed on the host memory is reflected on this Tensor’s memory! If False, data is being copied to this Tensor. Requires data to be C_CONTIGUOUS if True. If the passed array contains strings, the flag must be set to

[`](https://docs.openvino.ai#id3)False’.- type shared_memory:
bool


__init__(self: openvino._pyopenvino.Tensor, array: numpy.ndarray, shape: openvino._pyopenvino.Shape, type: openvino._pyopenvino.Type = <Type: ‘dynamic’>) -> None

Another Tensor’s special constructor.

Represents array in the memory with given shape and element type. It’s recommended to use this constructor only for wrapping array’s memory with the specific openvino element type parameter.

- param array:
C_CONTIGUOUS numpy array which will be wrapped in openvino.Tensor with given parameters (shape and element_type). Array’s memory is being shared with a host. Any action performed on the host memory will be reflected on this Tensor’s memory!

- type array:
numpy.array

- param shape:
Shape of the new tensor.

- type shape:
openvino.Shape

- param type:
Element type

- type type:
openvino.Type

- Example:

import openvino as ov import numpy as np arr = np.array(shape=(100), dtype=np.uint8) t = ov.Tensor(arr, ov.Shape([100, 8]), ov.Type.u1)

__init__(self: openvino._pyopenvino.Tensor, array: numpy.ndarray, shape: collections.abc.Sequence[typing.SupportsInt], type: openvino._pyopenvino.Type = <Type: ‘dynamic’>) -> None

Another Tensor’s special constructor.

Represents array in the memory with given shape and element type. It’s recommended to use this constructor only for wrapping array’s memory with the specific openvino element type parameter.

- param array:
C_CONTIGUOUS numpy array which will be wrapped in openvino.Tensor with given parameters (shape and element_type). Array’s memory is being shared with a host. Any action performed on the host memory will be reflected on this Tensor’s memory!

- type array:
numpy.array

- param shape:
Shape of the new tensor.

- type shape:
list or tuple

- param type:
Element type.

- type type:
openvino.Type

- Example:

import openvino as ov import numpy as np arr = np.array(shape=(100), dtype=np.uint8) t = ov.Tensor(arr, [100, 8], ov.Type.u1)

__init__(self: openvino._pyopenvino.Tensor, list: list) -> None

Tensor’s special constructor.

Creates a Tensor from a given Python list. Warning: It is always a copy of list’s data!

- param array:
list to create the tensor from.

- type array:
list[int, float, str]


__init__(self: openvino._pyopenvino.Tensor, type: openvino._pyopenvino.Type, shape: openvino._pyopenvino.Shape) -> None

__init__(self: openvino._pyopenvino.Tensor, type: openvino._pyopenvino.Type, shape: collections.abc.Sequence[typing.SupportsInt]) -> None

__init__(self: openvino._pyopenvino.Tensor, type: numpy.dtype, shape: collections.abc.Sequence[typing.SupportsInt]) -> None

__init__(self: openvino._pyopenvino.Tensor, type: object, shape: collections.abc.Sequence[typing.SupportsInt]) -> None

__init__(self: openvino._pyopenvino.Tensor, type: numpy.dtype, shape: openvino._pyopenvino.Shape) -> None

__init__(self: openvino._pyopenvino.Tensor, type: object, shape: openvino._pyopenvino.Shape) -> None

__init__(self: openvino._pyopenvino.Tensor, port: openvino._pyopenvino.Output) -> None

Constructs Tensor using port from node. Type and shape will be taken from the port.

- param port:
Output port from a node.

- type param:
openvino.Output


__init__(self: openvino._pyopenvino.Tensor, port: openvino._pyopenvino.Output, array: numpy.ndarray) -> None

Constructs Tensor using port from node. Type and shape will be taken from the port.

- param port:
Output port from a node.

- type param:
openvino.Output

- param array:
C_CONTIGUOUS numpy array which will be wrapped in openvino.Tensor. Array’s memory is being shared wi a host. Any action performed on the host memory will be reflected on this Tensor’s memory!

- type array:
numpy.array


__init__(self: openvino._pyopenvino.Tensor, port: ov::Output<ov::Node const>) -> None

Constructs Tensor using port from node. Type and shape will be taken from the port.

- param port:
Output port from a node.

- type param:
openvino.ConstOutput


__init__(self: openvino._pyopenvino.Tensor, port: ov::Output<ov::Node const>, array: numpy.ndarray) -> None

Constructs Tensor using port from node. Type and shape will be taken from the port.

- param port:
Output port from a node.

- type param:
openvino.ConstOutput

- param array:
C_CONTIGUOUS numpy array which will be wrapped in openvino.Tensor. Array’s memory is being shared with a host. Any action performed on the host memory will be reflected on this Tensor’s memory!

- type array:
numpy.array


__init__(self: openvino._pyopenvino.Tensor, other: openvino._pyopenvino.Tensor, begin: openvino._pyopenvino.Coordinate, end: openvino._pyopenvino.Coordinate) -> None

__init__(self: openvino._pyopenvino.Tensor, other: openvino._pyopenvino.Tensor, begin: collections.abc.Sequence[typing.SupportsInt], end: collections.abc.Sequence[typing.SupportsInt]) -> None

__init__(self: openvino._pyopenvino.Tensor, image: object) -> None

Constructs Tensor from a Pillow Image.

- param image:
Pillow Image to create the tensor from.

- type image:
PIL.Image.Image

- Example:

from PIL import Image import openvino as ov img = Image.open("example.jpg") tensor = ov.Tensor(img)



-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.Tensor.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Tensor.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Tensor.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Tensor.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.Tensor.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.Tensor.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.Tensor.__reduce_ex__) Helper for pickle.


-
__repr__(
*self:*) str[openvino._pyopenvino.Tensor](https://docs.openvino.ai#openvino.Tensor)[#](https://docs.openvino.ai#openvino.Tensor.__repr__)

-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.Tensor.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino.Tensor.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino.Tensor.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.Tensor.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.Tensor._pybind11_conduit_v1_)

-
*property*byte_size[#](https://docs.openvino.ai#openvino.Tensor.byte_size) Tensor’s size in bytes.

- Return type:
int



-
*property*bytes_data[#](https://docs.openvino.ai#openvino.Tensor.bytes_data) Access to Tensor’s data with string Type in np.bytes_ dtype.

Getter returns a numpy array with corresponding shape and dtype. Warning: Data of string type is always a copy of underlaying memory!

Setter fills underlaying Tensor’s memory by copying strings from other. other must have the same size (number of elements) as the Tensor. Tensor’s shape is not changed by performing this operation!


-
copy_from(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.Tensor.copy_from) Overloaded function.

copy_from(self: openvino._pyopenvino.Tensor, source_tensor: openvino._pyopenvino.Tensor) -> None

Copy source tensor’s data to this tensor. Tensors should have the same element type and shape.

- param source_tensor:
The source tensor from which the data will be copied.

- type source_tensor:
openvino.Tensor


copy_from(self: openvino._pyopenvino.Tensor, source_tensor: RemoteTensorWrapper) -> None

Copy source remote tensor’s data to this tensor. Tensors should have the same element type. In case of RoiTensor, tensors should also have the same shape.

- param source_tensor:
The source remote tensor from which the data will be copied.

- type source_tensor:
openvino.RemoteTensor


copy_from(self: openvino._pyopenvino.Tensor, source: numpy.ndarray) -> None

Copy the source to this tensor. This tensor and the source should have the same element type. Shape will be adjusted if there is a mismatch.

copy_from(self: openvino._pyopenvino.Tensor, source: list) -> None

Copy the source to this tensor. This tensor and the source should have the same element type. Shape will be adjusted if there is a mismatch.



-
copy_to(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.Tensor.copy_to) Overloaded function.

copy_to(self: openvino._pyopenvino.Tensor, target_tensor: openvino._pyopenvino.Tensor) -> None

Copy tensor’s data to a destination tensor. The destination tensor should have the same element type and shape.

- param target_tensor:
The destination tensor to which the data will be copied.

- type target_tensor:
openvino.Tensor


copy_to(self: openvino._pyopenvino.Tensor, target_tensor: RemoteTensorWrapper) -> None

Copy tensor’s data to a destination remote tensor. The destination remote tensor should have the same element type. In case of RoiRemoteTensor, the destination tensor should also have the same shape.

- param target_tensor:
The destination remote tensor to which the data will be copied.

- type target_tensor:
openvino.RemoteTensor




-
*property*data[#](https://docs.openvino.ai#openvino.Tensor.data) Access to Tensor’s data.

Returns numpy array with corresponding shape and dtype.

For tensors with OpenVINO specific element type, such as u1, u4 or i4 it returns linear array, with uint8 / int8 numpy dtype.

For tensors with string element type, returns a numpy array of bytes without any decoding. To change the underlaying data use str_data/bytes_data properties or the copy_from function. Warning: Data of string type is always a copy of underlaying memory!

- Return type:
numpy.array



-
*property*element_type[#](https://docs.openvino.ai#openvino.Tensor.element_type) Tensor’s element type.

- Return type:


-
get_byte_size(
*self:*) int[openvino._pyopenvino.Tensor](https://docs.openvino.ai#openvino.Tensor)[#](https://docs.openvino.ai#openvino.Tensor.get_byte_size) Gets Tensor’s size in bytes.

- Return type:
int



-
get_element_type(
*self:*)[openvino._pyopenvino.Tensor](https://docs.openvino.ai#openvino.Tensor)[openvino._pyopenvino.Type](https://docs.openvino.ai/openvino.Type.html#openvino.Type)[#](https://docs.openvino.ai#openvino.Tensor.get_element_type) Gets Tensor’s element type.

- Return type:


-
get_shape(
*self:*)[openvino._pyopenvino.Tensor](https://docs.openvino.ai#openvino.Tensor)[openvino._pyopenvino.Shape](https://docs.openvino.ai/openvino.Shape.html#openvino.Shape)[#](https://docs.openvino.ai#openvino.Tensor.get_shape) Gets Tensor’s shape.

- Return type:


-
get_size(
*self:*) int[openvino._pyopenvino.Tensor](https://docs.openvino.ai#openvino.Tensor)[#](https://docs.openvino.ai#openvino.Tensor.get_size) Gets Tensor’s size as total number of elements.

- Return type:
int



-
get_strides(
*self:*)[openvino._pyopenvino.Tensor](https://docs.openvino.ai#openvino.Tensor)[openvino._pyopenvino.Strides](https://docs.openvino.ai/openvino.Strides.html#openvino.Strides)[#](https://docs.openvino.ai#openvino.Tensor.get_strides) Gets Tensor’s strides in bytes.

- Return type:


-
is_continuous(
*self:*) bool[openvino._pyopenvino.Tensor](https://docs.openvino.ai#openvino.Tensor)[#](https://docs.openvino.ai#openvino.Tensor.is_continuous) Reports whether the tensor is continuous or not. :return: True if the tensor is continuous, otherwise False. :rtype: bool


-
set_shape(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.Tensor.set_shape) Overloaded function.

set_shape(self: openvino._pyopenvino.Tensor, arg0: openvino._pyopenvino.Shape) -> None

Sets Tensor’s shape.

set_shape(self: openvino._pyopenvino.Tensor, arg0: collections.abc.Sequence[typing.SupportsInt]) -> None

Sets Tensor’s shape.



-
*property*shape[#](https://docs.openvino.ai#openvino.Tensor.shape) Tensor’s shape get/set.


-
*property*size[#](https://docs.openvino.ai#openvino.Tensor.size) Tensor’s size as total number of elements.

- Return type:
int



-
*property*str_data[#](https://docs.openvino.ai#openvino.Tensor.str_data) Access to Tensor’s data with string Type in np.str_ dtype.

Getter returns a numpy array with corresponding shape and dtype. Warning: Data of string type is always a copy of underlaying memory!

Setter fills underlaying Tensor’s memory by copying strings from other. other must have the same size (number of elements) as the Tensor. Tensor’s shape is not changed by performing this operation!


-
*property*strides[#](https://docs.openvino.ai#openvino.Tensor.strides) Tensor’s strides in bytes.

- Return type:


-
__init__(