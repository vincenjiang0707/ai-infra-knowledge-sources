source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.VASurfaceTensor.html
lastmod: 

# openvino.VASurfaceTensor[#](https://docs.openvino.ai#openvino-vasurfacetensor)

-
*class*openvino.VASurfaceTensor[#](https://docs.openvino.ai#openvino.VASurfaceTensor) Bases:

`RemoteTensor`

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.VASurfaceTensor.__init__)

Methods

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

(self)`get_device_name`

Returns name of a device on which the tensor is allocated.

(self)`get_params`

Returns a dict of device-specific parameters required for low-level operations with the underlying tensor.

(self)`get_shape`

Gets Tensor's shape.

Attributes

This property is not implemented.

This property is not implemented.

Returns plane ID of underlying video decoder surface.

This property is not implemented.

Returns ID of underlying video decoder surface.

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.VASurfaceTensor.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.VASurfaceTensor.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.VASurfaceTensor.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.VASurfaceTensor.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.VASurfaceTensor.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.VASurfaceTensor.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.VASurfaceTensor.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.VASurfaceTensor.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino.VASurfaceTensor.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.VASurfaceTensor.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino.VASurfaceTensor.__hash__) Return hash(self).


-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.VASurfaceTensor.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.VASurfaceTensor.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.VASurfaceTensor.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.VASurfaceTensor.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.VASurfaceTensor.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.VASurfaceTensor.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.VASurfaceTensor.__reduce_ex__) Helper for pickle.


-
__repr__(
*self:*) str[openvino._pyopenvino.VASurfaceTensor](https://docs.openvino.ai#openvino.VASurfaceTensor)[#](https://docs.openvino.ai#openvino.VASurfaceTensor.__repr__)

-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.VASurfaceTensor.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino.VASurfaceTensor.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino.VASurfaceTensor.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.VASurfaceTensor.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.VASurfaceTensor._pybind11_conduit_v1_)

-
*property*bytes_data[#](https://docs.openvino.ai#openvino.VASurfaceTensor.bytes_data) This property is not implemented.


-
copy_from(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.VASurfaceTensor.copy_from) Overloaded function.

copy_from(self: openvino._pyopenvino.RemoteTensor, source_tensor: openvino._pyopenvino.RemoteTensor) -> None

Copy source remote tensor’s data to this tensor. Tensors should have the same element type. In case of RoiTensor, tensors should also have the same shape.

- param source_tensor:
The source remote tensor from which the data will be copied.

- type source_tensor:
openvino.RemoteTensor


copy_from(self: openvino._pyopenvino.RemoteTensor, source_tensor: openvino._pyopenvino.Tensor) -> None

Copy source tensor’s data to this tensor. Tensors should have the same element type and shape. In case of RoiTensor, tensors should also have the same shape.

- param source_tensor:
The source tensor from which the data will be copied.

- type source_tensor:
openvino.Tensor




-
copy_to(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.VASurfaceTensor.copy_to) Overloaded function.

copy_to(self: openvino._pyopenvino.RemoteTensor, target_tensor: openvino._pyopenvino.RemoteTensor) -> None

Copy tensor’s data to a destination remote tensor. The destination tensor should have the same element type. In case of RoiTensor, the destination tensor should also have the same shape.

- param target_tensor:
The destination remote tensor to which the data will be copied.

- type target_tensor:
openvino.RemoteTensor


copy_to(self: openvino._pyopenvino.RemoteTensor, target_tensor: openvino._pyopenvino.Tensor) -> None

Copy tensor’s data to a destination tensor. The destination tensor should have the same element type. In case of RoiTensor, the destination tensor should also have the same shape.

- param target_tensor:
The destination tensor to which the data will be copied.

- type target_tensor:
openvino.Tensor




-
*property*data[#](https://docs.openvino.ai#openvino.VASurfaceTensor.data) This property is not implemented.


-
get_byte_size(
*self:*) int[openvino._pyopenvino.RemoteTensor](https://docs.openvino.ai/openvino.RemoteTensor.html#openvino.RemoteTensor)[#](https://docs.openvino.ai#openvino.VASurfaceTensor.get_byte_size) Gets Tensor’s size in bytes.

- Return type:
int



-
get_device_name(
*self:*) str[openvino._pyopenvino.RemoteTensor](https://docs.openvino.ai/openvino.RemoteTensor.html#openvino.RemoteTensor)[#](https://docs.openvino.ai#openvino.VASurfaceTensor.get_device_name) Returns name of a device on which the tensor is allocated.

- Returns:
A device name string in fully specified format <device_name>[.<device_id>[.<tile_id>]].

- Return type:
str



-
get_params(
*self:*) dict[str,[openvino._pyopenvino.RemoteTensor](https://docs.openvino.ai/openvino.RemoteTensor.html#openvino.RemoteTensor)[openvino._pyopenvino.OVAny](https://docs.openvino.ai/openvino.OVAny.html#openvino.OVAny)][#](https://docs.openvino.ai#openvino.VASurfaceTensor.get_params) Returns a dict of device-specific parameters required for low-level operations with the underlying tensor. Parameters include device/context/surface/buffer handles, access flags, etc. Content of the returned dict depends on remote execution context that is currently set on the device (working scenario).

- Returns:
A dictionary of device-specific parameters.

- Return type:
dict



-
get_shape(
*self:*)[openvino._pyopenvino.RemoteTensor](https://docs.openvino.ai/openvino.RemoteTensor.html#openvino.RemoteTensor)[openvino._pyopenvino.Shape](https://docs.openvino.ai/openvino.Shape.html#openvino.Shape)[#](https://docs.openvino.ai#openvino.VASurfaceTensor.get_shape) Gets Tensor’s shape.

- Return type:


-
*property*plane_id[#](https://docs.openvino.ai#openvino.VASurfaceTensor.plane_id) Returns plane ID of underlying video decoder surface.

- Returns:
Plane ID of underlying video decoder surface.

- Return type:
int



-
*property*str_data[#](https://docs.openvino.ai#openvino.VASurfaceTensor.str_data) This property is not implemented.


-
*property*surface_id[#](https://docs.openvino.ai#openvino.VASurfaceTensor.surface_id) Returns ID of underlying video decoder surface.

- Returns:
VASurfaceID of the tensor.

- Return type:
int



-
__init__(