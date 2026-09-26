source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.frontend.TelemetryExtension.html
lastmod: 

# openvino.frontend.TelemetryExtension[#](https://docs.openvino.ai#openvino-frontend-telemetryextension)

-
*class*openvino.frontend.TelemetryExtension[#](https://docs.openvino.ai#openvino.frontend.TelemetryExtension) Bases:

`Extension`

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.frontend.TelemetryExtension.__init__) Overloaded function.

__init__(self: openvino._pyopenvino.TelemetryExtension, arg0: str, arg1: collections.abc.Callable, arg2: collections.abc.Callable, arg3: collections.abc.Callable) -> None

__init__(self: openvino._pyopenvino.TelemetryExtension, arg0: str, arg1: collections.abc.Callable[[str, str, str, typing.SupportsInt], None], arg2: collections.abc.Callable[[str, str], None], arg3: collections.abc.Callable[[str, str], None]) -> None



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

(self, arg0)`send_error`

(self, arg0, arg1, arg2)`send_event`

(self, arg0)`send_stack_trace`

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.frontend.TelemetryExtension.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.frontend.TelemetryExtension.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.frontend.TelemetryExtension.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.frontend.TelemetryExtension.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.TelemetryExtension.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.frontend.TelemetryExtension.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.TelemetryExtension.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.frontend.TelemetryExtension.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino.frontend.TelemetryExtension.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.TelemetryExtension.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino.frontend.TelemetryExtension.__hash__) Return hash(self).


-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0) Overloaded function.

__init__(self: openvino._pyopenvino.TelemetryExtension, arg0: str, arg1: collections.abc.Callable, arg2: collections.abc.Callable, arg3: collections.abc.Callable) -> None

__init__(self: openvino._pyopenvino.TelemetryExtension, arg0: str, arg1: collections.abc.Callable[[str, str, str, typing.SupportsInt], None], arg2: collections.abc.Callable[[str, str], None], arg3: collections.abc.Callable[[str, str], None]) -> None



-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.frontend.TelemetryExtension.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.TelemetryExtension.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.TelemetryExtension.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.TelemetryExtension.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.frontend.TelemetryExtension.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.frontend.TelemetryExtension.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.frontend.TelemetryExtension.__reduce_ex__) Helper for pickle.


-
__repr__(
*self:*) str[openvino._pyopenvino.Extension](https://docs.openvino.ai/openvino.Extension.html#openvino.Extension)[#](https://docs.openvino.ai#openvino.frontend.TelemetryExtension.__repr__)

-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.TelemetryExtension.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino.frontend.TelemetryExtension.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino.frontend.TelemetryExtension.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.frontend.TelemetryExtension.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.frontend.TelemetryExtension._pybind11_conduit_v1_)

-
send_error(
*self:*,[openvino._pyopenvino.TelemetryExtension](https://docs.openvino.ai#openvino.frontend.TelemetryExtension)*arg0: str*) None[#](https://docs.openvino.ai#openvino.frontend.TelemetryExtension.send_error)

-
send_event(
*self:*,[openvino._pyopenvino.TelemetryExtension](https://docs.openvino.ai#openvino.frontend.TelemetryExtension)*arg0: str*,*arg1: str*,*arg2: SupportsInt*) None[#](https://docs.openvino.ai#openvino.frontend.TelemetryExtension.send_event)

-
send_stack_trace(
*self:*,[openvino._pyopenvino.TelemetryExtension](https://docs.openvino.ai#openvino.frontend.TelemetryExtension)*arg0: str*) None[#](https://docs.openvino.ai#openvino.frontend.TelemetryExtension.send_stack_trace)

-
__init__(