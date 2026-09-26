source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.op.util.IndexReduction.html
lastmod: 

# openvino.runtime.op.util.IndexReduction[#](https://docs.openvino.ai#openvino-runtime-op-util-indexreduction)

-
*class*openvino.runtime.op.util.IndexReduction[#](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction) Bases:

`pybind11_object`

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction.__init__)

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

(self)`get_index_element_type`

(self)`get_reduction_axis`

(self, arg0)`set_index_element_type`

(self, arg0)`set_reduction_axis`

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction.__hash__) Return hash(self).


-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction.__reduce_ex__) Helper for pickle.


-
__repr__(
*self:*) str[openvino._pyopenvino.op.util.IndexReduction](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction)[#](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction.__repr__)

-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction._pybind11_conduit_v1_)

-
get_index_element_type(
*self:*)[openvino._pyopenvino.op.util.IndexReduction](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction)[openvino._pyopenvino.Type](https://docs.openvino.ai/openvino.Type.html#openvino.Type)[#](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction.get_index_element_type)

-
get_reduction_axis(
*self:*) int[openvino._pyopenvino.op.util.IndexReduction](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction)[#](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction.get_reduction_axis)

-
*property*index_element_type[#](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction.index_element_type)

-
*property*reduction_axis[#](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction.reduction_axis)

-
set_index_element_type(
*self:*,[openvino._pyopenvino.op.util.IndexReduction](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction)*arg0:*) None[openvino._pyopenvino.Type](https://docs.openvino.ai/openvino.Type.html#openvino.Type)[#](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction.set_index_element_type)

-
set_reduction_axis(
*self:*,[openvino._pyopenvino.op.util.IndexReduction](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction)*arg0: SupportsInt*) None[#](https://docs.openvino.ai#openvino.runtime.op.util.IndexReduction.set_reduction_axis)

-
__init__(