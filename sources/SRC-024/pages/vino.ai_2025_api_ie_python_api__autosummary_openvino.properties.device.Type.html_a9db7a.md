source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.properties.device.Type.html
lastmod: 

# openvino.properties.device.Type[#](https://docs.openvino.ai#openvino-properties-device-type)

-
*class*openvino.properties.device.Type[#](https://docs.openvino.ai#openvino.properties.device.Type) Bases:

`pybind11_object`

Members:

INTEGRATED

DISCRETE

-
__init__(
*self:*,[openvino._pyopenvino.properties.device.Type](https://docs.openvino.ai#openvino.properties.device.Type)*value: SupportsInt*) None[#](https://docs.openvino.ai#openvino.properties.device.Type.__init__)

Methods

(name, /)`__delattr__`

Implement delattr(self, name).

()`__dir__`

Default dir() implementation.

(self, other, /)`__eq__`

(format_spec, /)`__format__`

Default object formatter.

(self, other, /)`__ge__`

(name, /)`__getattribute__`

Return getattr(self, name).

(self, /)`__getstate__`

(self, other, /)`__gt__`

(self, /)`__hash__`

(self, /)`__index__`

(self, value)`__init__`

This method is called when a class is subclassed.

(self, /)`__int__`

(self, other, /)`__le__`

(self, other, /)`__lt__`

(self, other, /)`__ne__`

(**kwargs)`__new__`

Helper for pickle.

(protocol, /)`__reduce_ex__`

Helper for pickle.

(self, /)`__repr__`

(name, value, /)`__setattr__`

Implement setattr(self, name, value).

(self, state, /)`__setstate__`

Size of object in memory, in bytes.

(self, /)`__str__`

Abstract classes can override this to customize issubclass().

Attributes

`__entries`

-
DISCRETE
*= <Type.DISCRETE: 1>*[#](https://docs.openvino.ai#openvino.properties.device.Type.DISCRETE)

-
INTEGRATED
*= <Type.INTEGRATED: 0>*[#](https://docs.openvino.ai#openvino.properties.device.Type.INTEGRATED)

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.properties.device.Type.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.properties.device.Type.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.properties.device.Type.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.properties.device.Type.__dir__) Default dir() implementation.


-
__eq__(
*self: object*,*other: object*,*/*) bool[#](https://docs.openvino.ai#openvino.properties.device.Type.__eq__)

-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.properties.device.Type.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*self: object*,*other: object*,*/*) bool[#](https://docs.openvino.ai#openvino.properties.device.Type.__ge__)

-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.properties.device.Type.__getattribute__) Return getattr(self, name).


-
__getstate__(
*self: object*,*/*) int[#](https://docs.openvino.ai#openvino.properties.device.Type.__getstate__)

-
__gt__(
*self: object*,*other: object*,*/*) bool[#](https://docs.openvino.ai#openvino.properties.device.Type.__gt__)

-
__hash__(
*self: object*,*/*) int[#](https://docs.openvino.ai#openvino.properties.device.Type.__hash__)

-
__index__(
*self:*,[openvino._pyopenvino.properties.device.Type](https://docs.openvino.ai#openvino.properties.device.Type)*/*) int[#](https://docs.openvino.ai#openvino.properties.device.Type.__index__)

-
__init__(
*self:*,[openvino._pyopenvino.properties.device.Type](https://docs.openvino.ai#openvino.properties.device.Type)*value: SupportsInt*) None[#](https://docs.openvino.ai#id0)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.properties.device.Type.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__int__(
*self:*,[openvino._pyopenvino.properties.device.Type](https://docs.openvino.ai#openvino.properties.device.Type)*/*) int[#](https://docs.openvino.ai#openvino.properties.device.Type.__int__)

-
__le__(
*self: object*,*other: object*,*/*) bool[#](https://docs.openvino.ai#openvino.properties.device.Type.__le__)

-
__lt__(
*self: object*,*other: object*,*/*) bool[#](https://docs.openvino.ai#openvino.properties.device.Type.__lt__)

-
__members__
*= {'DISCRETE': <Type.DISCRETE: 1>, 'INTEGRATED': <Type.INTEGRATED: 0>}*[#](https://docs.openvino.ai#openvino.properties.device.Type.__members__)

-
__ne__(
*self: object*,*other: object*,*/*) bool[#](https://docs.openvino.ai#openvino.properties.device.Type.__ne__)

-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.properties.device.Type.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.properties.device.Type.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.properties.device.Type.__reduce_ex__) Helper for pickle.


-
__repr__(
*self: object*,*/*) str[#](https://docs.openvino.ai#openvino.properties.device.Type.__repr__)

-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.properties.device.Type.__setattr__) Implement setattr(self, name, value).


-
__setstate__(
*self:*,[openvino._pyopenvino.properties.device.Type](https://docs.openvino.ai#openvino.properties.device.Type)*state: SupportsInt*,*/*) None[#](https://docs.openvino.ai#openvino.properties.device.Type.__setstate__)

-
__sizeof__()
[#](https://docs.openvino.ai#openvino.properties.device.Type.__sizeof__) Size of object in memory, in bytes.


-
__str__(
*self: object*,*/*) str[#](https://docs.openvino.ai#openvino.properties.device.Type.__str__)

-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.properties.device.Type.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.properties.device.Type._pybind11_conduit_v1_)

-
*property*name[#](https://docs.openvino.ai#openvino.properties.device.Type.name)

-
*property*value[#](https://docs.openvino.ai#openvino.properties.device.Type.value)

-
__init__(