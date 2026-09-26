source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.frontend.ProgressReporterExtension.html
lastmod: 

# openvino.frontend.ProgressReporterExtension[#](https://docs.openvino.ai#openvino-frontend-progressreporterextension)

-
*class*openvino.frontend.ProgressReporterExtension[#](https://docs.openvino.ai#openvino.frontend.ProgressReporterExtension) Bases:

`Extension`

An extension class intented to use as progress reporting utility

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.frontend.ProgressReporterExtension.__init__) Overloaded function.

__init__(self: openvino._pyopenvino.ProgressReporterExtension) -> None

__init__(self: openvino._pyopenvino.ProgressReporterExtension, arg0: collections.abc.Callable) -> None

__init__(self: openvino._pyopenvino.ProgressReporterExtension, arg0: collections.abc.Callable[[typing.SupportsFloat, typing.SupportsInt, typing.SupportsInt], None]) -> None

__init__(self: openvino._pyopenvino.ProgressReporterExtension, arg0: collections.abc.Callable[[typing.SupportsFloat, typing.SupportsInt, typing.SupportsInt], None]) -> None



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

(self, arg0, arg1, arg2)`report_progress`

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.frontend.ProgressReporterExtension.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.frontend.ProgressReporterExtension.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.frontend.ProgressReporterExtension.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.frontend.ProgressReporterExtension.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.ProgressReporterExtension.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.frontend.ProgressReporterExtension.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.ProgressReporterExtension.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.frontend.ProgressReporterExtension.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino.frontend.ProgressReporterExtension.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.ProgressReporterExtension.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino.frontend.ProgressReporterExtension.__hash__) Return hash(self).


-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0) Overloaded function.

__init__(self: openvino._pyopenvino.ProgressReporterExtension) -> None

__init__(self: openvino._pyopenvino.ProgressReporterExtension, arg0: collections.abc.Callable) -> None

__init__(self: openvino._pyopenvino.ProgressReporterExtension, arg0: collections.abc.Callable[[typing.SupportsFloat, typing.SupportsInt, typing.SupportsInt], None]) -> None

__init__(self: openvino._pyopenvino.ProgressReporterExtension, arg0: collections.abc.Callable[[typing.SupportsFloat, typing.SupportsInt, typing.SupportsInt], None]) -> None



-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.frontend.ProgressReporterExtension.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.ProgressReporterExtension.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.ProgressReporterExtension.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.ProgressReporterExtension.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.frontend.ProgressReporterExtension.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.frontend.ProgressReporterExtension.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.frontend.ProgressReporterExtension.__reduce_ex__) Helper for pickle.


-
__repr__(
*self:*) str[openvino._pyopenvino.Extension](https://docs.openvino.ai/openvino.Extension.html#openvino.Extension)[#](https://docs.openvino.ai#openvino.frontend.ProgressReporterExtension.__repr__)

-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.ProgressReporterExtension.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino.frontend.ProgressReporterExtension.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino.frontend.ProgressReporterExtension.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.frontend.ProgressReporterExtension.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.frontend.ProgressReporterExtension._pybind11_conduit_v1_)

-
report_progress(
*self:*,[openvino._pyopenvino.ProgressReporterExtension](https://docs.openvino.ai#openvino.frontend.ProgressReporterExtension)*arg0: SupportsFloat*,*arg1: SupportsInt*,*arg2: SupportsInt*) None[#](https://docs.openvino.ai#openvino.frontend.ProgressReporterExtension.report_progress)

-
__init__(