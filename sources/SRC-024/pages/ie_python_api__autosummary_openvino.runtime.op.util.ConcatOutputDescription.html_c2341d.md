source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.op.util.ConcatOutputDescription.html
lastmod: 

# openvino.runtime.op.util.ConcatOutputDescription[#](https://docs.openvino.ai#openvino-runtime-op-util-concatoutputdescription)

-
*class*openvino.runtime.op.util.ConcatOutputDescription[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription) Bases:

`OutputDescription`

openvino.impl.op.util.ConcatOutputDescription wraps ov::op::util::ConcatOutputDescription

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription.__init__) Overloaded function.

__init__(self: openvino._pyopenvino.op.util.ConcatOutputDescription) -> None

__init__(self: openvino._pyopenvino.op.util.ConcatOutputDescription, body_value_index: typing.SupportsInt, output_index: typing.SupportsInt, start: typing.SupportsInt, stride: typing.SupportsInt, part_size: typing.SupportsInt, end: typing.SupportsInt, axis: typing.SupportsInt) -> None



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

(self)`copy`

(self)`get_type_info`

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription.__hash__) Return hash(self).


-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0) Overloaded function.

__init__(self: openvino._pyopenvino.op.util.ConcatOutputDescription) -> None

__init__(self: openvino._pyopenvino.op.util.ConcatOutputDescription, body_value_index: typing.SupportsInt, output_index: typing.SupportsInt, start: typing.SupportsInt, stride: typing.SupportsInt, part_size: typing.SupportsInt, end: typing.SupportsInt, axis: typing.SupportsInt) -> None



-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription.__reduce_ex__) Helper for pickle.


-
__repr__(
*self:*) str[openvino._pyopenvino.op.util.ConcatOutputDescription](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription)[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription.__repr__)

-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription._pybind11_conduit_v1_)

-
*property*axis[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription.axis)

-
*property*body_value_index[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription.body_value_index)

-
copy(
*self:*) openvino._pyopenvino.op.util.OutputDescription[openvino._pyopenvino.op.util.ConcatOutputDescription](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription)[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription.copy)

-
*property*end[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription.end)

-
get_type_info(
*self:*)[openvino._pyopenvino.op.util.ConcatOutputDescription](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription)[openvino._pyopenvino.DiscreteTypeInfo](https://docs.openvino.ai/openvino.DiscreteTypeInfo.html#openvino.DiscreteTypeInfo)[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription.get_type_info)

-
*property*output_index[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription.output_index)

-
*property*part_size[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription.part_size)

-
*property*start[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription.start)

-
*property*stride[#](https://docs.openvino.ai#openvino.runtime.op.util.ConcatOutputDescription.stride)

-
__init__(