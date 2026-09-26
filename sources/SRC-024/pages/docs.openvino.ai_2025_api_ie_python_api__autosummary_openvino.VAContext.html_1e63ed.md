source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.VAContext.html
lastmod: 

# openvino.VAContext[#](https://docs.openvino.ai#openvino-vacontext)

-
*class*openvino.VAContext[#](https://docs.openvino.ai#openvino.VAContext) Bases:

`RemoteContext`

-
__init__(
*self:*,[openvino._pyopenvino.VAContext](https://docs.openvino.ai#openvino.VAContext)*core: openvino._pyopenvino.Core*,*display: typing_extensions.CapsuleType*,*target_tile_id: SupportsInt = -1*) None[#](https://docs.openvino.ai#openvino.VAContext.__init__) Constructs remote context object from valid VA display handle.

- Parameters:
**core**() – OpenVINO Runtime Core object.*openvino.Core***device**(*Any*) – A valid VADisplay to create remote context from.**target_tile_id**(*int*) – Desired tile id within given context for multi-tile system. Default value (-1) means that root device should be used.

- Returns:
A context instance.

- Return type:


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

(self, core, display[, target_tile_id])`__init__`

Constructs remote context object from valid VA display handle.

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

(self, type, shape, surface[, ...])`create_tensor`

Create remote tensor from VA surface handle.

(self, height, width, ...)`create_tensor_nv12`

This function is used to obtain a NV12 tensor from NV12 VA decoder output.

(self)`get_device_name`

Returns name of a device on which the context is allocated.

(self)`get_params`

Returns a dict of device-specific parameters required for low-level operations with the underlying context.

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.VAContext.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.VAContext.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.VAContext.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.VAContext.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.VAContext.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.VAContext.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.VAContext.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.VAContext.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino.VAContext.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.VAContext.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino.VAContext.__hash__) Return hash(self).


-
__init__(
*self:*,[openvino._pyopenvino.VAContext](https://docs.openvino.ai#openvino.VAContext)*core: openvino._pyopenvino.Core*,*display: typing_extensions.CapsuleType*,*target_tile_id: SupportsInt = -1*) None[#](https://docs.openvino.ai#id0) Constructs remote context object from valid VA display handle.

- Parameters:
**core**() – OpenVINO Runtime Core object.*openvino.Core***device**(*Any*) – A valid VADisplay to create remote context from.**target_tile_id**(*int*) – Desired tile id within given context for multi-tile system. Default value (-1) means that root device should be used.

- Returns:
A context instance.

- Return type:


-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.VAContext.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.VAContext.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.VAContext.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.VAContext.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.VAContext.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.VAContext.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.VAContext.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino.VAContext.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.VAContext.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino.VAContext.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino.VAContext.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.VAContext.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.VAContext._pybind11_conduit_v1_)

-
create_host_tensor(
*self:*,[openvino._pyopenvino.RemoteContext](https://docs.openvino.ai/openvino.RemoteContext.html#openvino.RemoteContext)*type:*,[openvino._pyopenvino.Type](https://docs.openvino.ai/openvino.Type.html#openvino.Type)*shape:*)[openvino._pyopenvino.Shape](https://docs.openvino.ai/openvino.Shape.html#openvino.Shape)[openvino._pyopenvino.Tensor](https://docs.openvino.ai/openvino.Tensor.html#openvino.Tensor)[#](https://docs.openvino.ai#openvino.VAContext.create_host_tensor) This method is used to create a host tensor object friendly for the device in current context. For example, GPU context may allocate USM host memory (if corresponding extension is available), which could be more efficient than regular host memory.

GIL is released while running this function.

- Parameters:
**type**() – Defines the element type of the tensor.*openvino.Type***shape**() – Defines the shape of the tensor.*openvino.Shape*

- Returns:
A tensor instance with device friendly memory.

- Return type:


-
create_tensor(
*self:*,[openvino._pyopenvino.VAContext](https://docs.openvino.ai#openvino.VAContext)*type:*,[openvino._pyopenvino.Type](https://docs.openvino.ai/openvino.Type.html#openvino.Type)*shape:*,[openvino._pyopenvino.Shape](https://docs.openvino.ai/openvino.Shape.html#openvino.Shape)*surface: SupportsInt*,*plane: SupportsInt = 0*) VASurfaceTensorWrapper[#](https://docs.openvino.ai#openvino.VAContext.create_tensor) Create remote tensor from VA surface handle.

GIL is released while running this function.

- Parameters:
**type**() – Defines the element type of the tensor.*openvino.Type***shape**() – Defines the shape of the tensor.*openvino.Shape***surface**(*int*) – VASurfaceID to create tensor from.**plane**(*int*) – An index of a plane inside VASurfaceID to create tensor from. Default: 0

- Returns:
A remote tensor instance wrapping VASurfaceID.

- Return type:


-
create_tensor_nv12(
*self:*,[openvino._pyopenvino.VAContext](https://docs.openvino.ai#openvino.VAContext)*height: SupportsInt*,*width: SupportsInt*,*nv12_surface: SupportsInt*) tuple[#](https://docs.openvino.ai#openvino.VAContext.create_tensor_nv12) This function is used to obtain a NV12 tensor from NV12 VA decoder output. The result contains two remote tensors for Y and UV planes of the surface.

GIL is released while running this function.

- Parameters:
**height**(*int*) – A height of Y plane.**width**(*int*) – A width of Y plane**nv12_surface**(*int*) – NV12 VASurfaceID to create NV12 from.

- Returns:
A pair of remote tensors for each plane.

- Return type:


-
get_device_name(
*self:*) str[openvino._pyopenvino.RemoteContext](https://docs.openvino.ai/openvino.RemoteContext.html#openvino.RemoteContext)[#](https://docs.openvino.ai#openvino.VAContext.get_device_name) Returns name of a device on which the context is allocated.

- Returns:
A device name string in fully specified format <device_name>[.<device_id>[.<tile_id>]].

- Return type:
str



-
get_params(
*self:*) dict[str,[openvino._pyopenvino.RemoteContext](https://docs.openvino.ai/openvino.RemoteContext.html#openvino.RemoteContext)[openvino._pyopenvino.OVAny](https://docs.openvino.ai/openvino.OVAny.html#openvino.OVAny)][#](https://docs.openvino.ai#openvino.VAContext.get_params) Returns a dict of device-specific parameters required for low-level operations with the underlying context. Parameters include device/context handles, access flags, etc. Content of the returned dict depends on remote execution context that is currently set on the device (working scenario).

- Returns:
A dictionary of device-specific parameters.

- Return type:
dict



-
__init__(