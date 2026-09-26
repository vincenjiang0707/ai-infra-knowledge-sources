source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.ProfilingInfo.html
lastmod: 

# openvino.ProfilingInfo[#](https://docs.openvino.ai#openvino-profilinginfo)

-
*class*openvino.ProfilingInfo[#](https://docs.openvino.ai#openvino.ProfilingInfo) Bases:

`pybind11_object`

openvino.ProfilingInfo contains performance metrics for single node.

-
__init__(
*self:*) None[openvino._pyopenvino.ProfilingInfo](https://docs.openvino.ai#openvino.ProfilingInfo)[#](https://docs.openvino.ai#openvino.ProfilingInfo.__init__)

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

(self)`__init__`

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

Attributes

-
EXECUTED
*= <Status.EXECUTED: 2>*[#](https://docs.openvino.ai#openvino.ProfilingInfo.EXECUTED)

-
NOT_RUN
*= <Status.NOT_RUN: 0>*[#](https://docs.openvino.ai#openvino.ProfilingInfo.NOT_RUN)

-
OPTIMIZED_OUT
*= <Status.OPTIMIZED_OUT: 1>*[#](https://docs.openvino.ai#openvino.ProfilingInfo.OPTIMIZED_OUT)

-
*class*Status[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status) Bases:

`pybind11_object`

Members:

NOT_RUN

OPTIMIZED_OUT

EXECUTED

-
EXECUTED
*= <Status.EXECUTED: 2>*[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status.EXECUTED)

-
NOT_RUN
*= <Status.NOT_RUN: 0>*[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status.NOT_RUN)

-
OPTIMIZED_OUT
*= <Status.OPTIMIZED_OUT: 1>*[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status.OPTIMIZED_OUT)

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status.__dir__) Default dir() implementation.


-
__eq__(
*self: object*,*other: object*,*/*) bool[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status.__eq__)

-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status.__getattribute__) Return getattr(self, name).


-
__getstate__(
*self: object*,*/*) int[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status.__getstate__)

-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status.__gt__) Return self>value.


-
__hash__(
*self: object*,*/*) int[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status.__hash__)

-
__index__(
*self:*,[openvino._pyopenvino.ProfilingInfo.Status](https://docs.openvino.ai#openvino.ProfilingInfo.Status)*/*) int[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status.__index__)

-
__init__(
*self:*,[openvino._pyopenvino.ProfilingInfo.Status](https://docs.openvino.ai#openvino.ProfilingInfo.Status)*value: SupportsInt*) None[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status.__init__)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__int__(
*self:*,[openvino._pyopenvino.ProfilingInfo.Status](https://docs.openvino.ai#openvino.ProfilingInfo.Status)*/*) int[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status.__int__)

-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status.__lt__) Return self<value.


-
__members__
*= {'EXECUTED': <Status.EXECUTED: 2>, 'NOT_RUN': <Status.NOT_RUN: 0>, 'OPTIMIZED_OUT': <Status.OPTIMIZED_OUT: 1>}*[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status.__members__)

-
__ne__(
*self: object*,*other: object*,*/*) bool[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status.__ne__)

-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status.__reduce_ex__) Helper for pickle.


-
__repr__(
*self: object*,*/*) str[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status.__repr__)

-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status.__setattr__) Implement setattr(self, name, value).


-
__setstate__(
*self:*,[openvino._pyopenvino.ProfilingInfo.Status](https://docs.openvino.ai#openvino.ProfilingInfo.Status)*state: SupportsInt*,*/*) None[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status.__setstate__)

-
__sizeof__()
[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status.__sizeof__) Size of object in memory, in bytes.


-
__str__(
*self: object*,*/*) str[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status.__str__)

-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status._pybind11_conduit_v1_)

-
*property*name[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status.name)

-
*property*value[#](https://docs.openvino.ai#openvino.ProfilingInfo.Status.value)

-
EXECUTED

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.ProfilingInfo.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.ProfilingInfo.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.ProfilingInfo.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.ProfilingInfo.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.ProfilingInfo.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.ProfilingInfo.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.ProfilingInfo.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.ProfilingInfo.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino.ProfilingInfo.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.ProfilingInfo.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino.ProfilingInfo.__hash__) Return hash(self).


-
__init__(
*self:*) None[openvino._pyopenvino.ProfilingInfo](https://docs.openvino.ai#openvino.ProfilingInfo)[#](https://docs.openvino.ai#id0)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.ProfilingInfo.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.ProfilingInfo.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.ProfilingInfo.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.ProfilingInfo.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.ProfilingInfo.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.ProfilingInfo.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.ProfilingInfo.__reduce_ex__) Helper for pickle.


-
__repr__(
*self:*) str[openvino._pyopenvino.ProfilingInfo](https://docs.openvino.ai#openvino.ProfilingInfo)[#](https://docs.openvino.ai#openvino.ProfilingInfo.__repr__)

-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.ProfilingInfo.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino.ProfilingInfo.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino.ProfilingInfo.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.ProfilingInfo.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.ProfilingInfo._pybind11_conduit_v1_)

-
*property*cpu_time[#](https://docs.openvino.ai#openvino.ProfilingInfo.cpu_time)

-
*property*exec_type[#](https://docs.openvino.ai#openvino.ProfilingInfo.exec_type)

-
*property*node_name[#](https://docs.openvino.ai#openvino.ProfilingInfo.node_name)

-
*property*node_type[#](https://docs.openvino.ai#openvino.ProfilingInfo.node_type)

-
*property*real_time[#](https://docs.openvino.ai#openvino.ProfilingInfo.real_time)

-
*property*status[#](https://docs.openvino.ai#openvino.ProfilingInfo.status)

-
__init__(