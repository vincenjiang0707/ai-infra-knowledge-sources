source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.RemoteContext.html
lastmod: 

# openvino.RemoteContext[#](https://docs.openvino.ai#openvino-remotecontext)

-
*class*openvino.RemoteContext[#](https://docs.openvino.ai#openvino.RemoteContext) Bases:

`pybind11_object`

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.RemoteContext.__init__)

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

()`__repr__`

Return repr(self).

(name, value, /)`__setattr__`

Implement setattr(self, name, value).

Size of object in memory, in bytes.

()`__str__`

Return str(self).

Abstract classes can override this to customize issubclass().

(self, type, shape)`create_host_tensor`

This method is used to create a host tensor object friendly for the device in current context.

(self, type, shape, properties)`create_tensor`

Allocates memory tensor in device memory or wraps user-supplied memory handle using the specified tensor description and low-level device-specific parameters.

(self)`get_device_name`

Returns name of a device on which the context is allocated.

(self)`get_params`

Returns a dict of device-specific parameters required for low-level operations with the underlying context.

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.RemoteContext.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.RemoteContext.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.RemoteContext.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.RemoteContext.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.RemoteContext.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.RemoteContext.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.RemoteContext.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.RemoteContext.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino.RemoteContext.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.RemoteContext.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino.RemoteContext.__hash__) Return hash(self).


-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.RemoteContext.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.RemoteContext.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.RemoteContext.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.RemoteContext.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.RemoteContext.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.RemoteContext.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.RemoteContext.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino.RemoteContext.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.RemoteContext.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino.RemoteContext.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino.RemoteContext.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.RemoteContext.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.RemoteContext._pybind11_conduit_v1_)

-
create_host_tensor(
*self:*,[openvino._pyopenvino.RemoteContext](https://docs.openvino.ai#openvino.RemoteContext)*type:*,[openvino._pyopenvino.Type](https://docs.openvino.ai/openvino.Type.html#openvino.Type)*shape:*)[openvino._pyopenvino.Shape](https://docs.openvino.ai/openvino.Shape.html#openvino.Shape)[openvino._pyopenvino.Tensor](https://docs.openvino.ai/openvino.Tensor.html#openvino.Tensor)[#](https://docs.openvino.ai#openvino.RemoteContext.create_host_tensor) This method is used to create a host tensor object friendly for the device in current context. For example, GPU context may allocate USM host memory (if corresponding extension is available), which could be more efficient than regular host memory.

GIL is released while running this function.

- Parameters:
**type**() – Defines the element type of the tensor.*openvino.Type***shape**() – Defines the shape of the tensor.*openvino.Shape*

- Returns:
A tensor instance with device friendly memory.

- Return type:


-
create_tensor(
*self:*,[openvino._pyopenvino.RemoteContext](https://docs.openvino.ai#openvino.RemoteContext)*type:*,[openvino._pyopenvino.Type](https://docs.openvino.ai/openvino.Type.html#openvino.Type)*shape:*,[openvino._pyopenvino.Shape](https://docs.openvino.ai/openvino.Shape.html#openvino.Shape)*properties: collections.abc.Mapping[str, object]*)[openvino._pyopenvino.RemoteTensor](https://docs.openvino.ai/openvino.RemoteTensor.html#openvino.RemoteTensor)[#](https://docs.openvino.ai#openvino.RemoteContext.create_tensor) Allocates memory tensor in device memory or wraps user-supplied memory handle using the specified tensor description and low-level device-specific parameters. Returns the object that implements the RemoteTensor interface.

GIL is released while running this function.

- Parameters:
**type**() – Defines the element type of the tensor.*openvino.Type***shape**() – Defines the shape of the tensor.*openvino.Shape***properties**(*dict*) – dict of the low-level tensor object parameters.

- Returns:
A remote tensor instance.

- Return type:


-
get_device_name(
*self:*) str[openvino._pyopenvino.RemoteContext](https://docs.openvino.ai#openvino.RemoteContext)[#](https://docs.openvino.ai#openvino.RemoteContext.get_device_name) Returns name of a device on which the context is allocated.

- Returns:
A device name string in fully specified format <device_name>[.<device_id>[.<tile_id>]].

- Return type:
str



-
get_params(
*self:*) dict[str,[openvino._pyopenvino.RemoteContext](https://docs.openvino.ai#openvino.RemoteContext)[openvino._pyopenvino.OVAny](https://docs.openvino.ai/openvino.OVAny.html#openvino.OVAny)][#](https://docs.openvino.ai#openvino.RemoteContext.get_params) Returns a dict of device-specific parameters required for low-level operations with the underlying context. Parameters include device/context handles, access flags, etc. Content of the returned dict depends on remote execution context that is currently set on the device (working scenario).

- Returns:
A dictionary of device-specific parameters.

- Return type:
dict



-
__init__(