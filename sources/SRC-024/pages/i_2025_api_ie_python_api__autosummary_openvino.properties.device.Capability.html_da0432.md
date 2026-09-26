source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.properties.device.Capability.html
lastmod: 

# openvino.properties.device.Capability[#](https://docs.openvino.ai#openvino-properties-device-capability)

-
*class*openvino.properties.device.Capability[#](https://docs.openvino.ai#openvino.properties.device.Capability) Bases:

`pybind11_object`

openvino.properties.device.Capability that simulates ov::device::capability

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.properties.device.Capability.__init__)

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

Attributes

-
BF16
*= 'BF16'*[#](https://docs.openvino.ai#openvino.properties.device.Capability.BF16)

-
BIN
*= 'BIN'*[#](https://docs.openvino.ai#openvino.properties.device.Capability.BIN)

-
EXPORT_IMPORT
*= 'EXPORT_IMPORT'*[#](https://docs.openvino.ai#openvino.properties.device.Capability.EXPORT_IMPORT)

-
FP16
*= 'FP16'*[#](https://docs.openvino.ai#openvino.properties.device.Capability.FP16)

-
FP32
*= 'FP32'*[#](https://docs.openvino.ai#openvino.properties.device.Capability.FP32)

-
INT16
*= 'INT16'*[#](https://docs.openvino.ai#openvino.properties.device.Capability.INT16)

-
INT8
*= 'INT8'*[#](https://docs.openvino.ai#openvino.properties.device.Capability.INT8)

-
WINOGRAD
*= 'WINOGRAD'*[#](https://docs.openvino.ai#openvino.properties.device.Capability.WINOGRAD)

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.properties.device.Capability.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.properties.device.Capability.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.properties.device.Capability.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.properties.device.Capability.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.properties.device.Capability.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.properties.device.Capability.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.properties.device.Capability.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.properties.device.Capability.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino.properties.device.Capability.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.properties.device.Capability.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino.properties.device.Capability.__hash__) Return hash(self).


-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.properties.device.Capability.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.properties.device.Capability.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.properties.device.Capability.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.properties.device.Capability.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.properties.device.Capability.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.properties.device.Capability.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.properties.device.Capability.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino.properties.device.Capability.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.properties.device.Capability.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino.properties.device.Capability.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino.properties.device.Capability.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.properties.device.Capability.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.properties.device.Capability._pybind11_conduit_v1_)

-
__init__(