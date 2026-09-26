source: https://docs.openvino.ai/2025/api/genai_api/_autosummary/openvino_genai.StopCriteria.html
lastmod: 

# openvino_genai.StopCriteria[#](https://docs.openvino.ai#openvino-genai-stopcriteria)

-
*class*openvino_genai.StopCriteria[#](https://docs.openvino.ai#openvino_genai.StopCriteria) Bases:

`pybind11_object`

StopCriteria controls the stopping condition for grouped beam search.

- The following values are possible:
“openvino_genai.StopCriteria.EARLY” stops as soon as there are num_beams complete candidates. “openvino_genai.StopCriteria.HEURISTIC” stops when is it unlikely to find better candidates. “openvino_genai.StopCriteria.NEVER” stops when there cannot be better candidates.


Members:

EARLY

HEURISTIC

NEVER

-
__init__(
*self:*,[openvino_genai.py_openvino_genai.StopCriteria](https://docs.openvino.ai#openvino_genai.StopCriteria)*value: SupportsInt*) None[#](https://docs.openvino.ai#openvino_genai.StopCriteria.__init__)

Methods

(name, /)`__delattr__`

Implement delattr(self, name).

()`__dir__`

Default dir() implementation.

(self, other, /)`__eq__`

(format_spec, /)`__format__`

Default object formatter.

(value, /)`__ge__`

Return self>=value.

(name, /)`__getattribute__`

Return getattr(self, name).

(self, /)`__getstate__`

(value, /)`__gt__`

Return self>value.

(self, /)`__hash__`

(self, /)`__index__`

(self, value)`__init__`

This method is called when a class is subclassed.

(self, /)`__int__`

(value, /)`__le__`

Return self<=value.

(value, /)`__lt__`

Return self<value.

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
EARLY
*= <StopCriteria.EARLY: 0>*[#](https://docs.openvino.ai#openvino_genai.StopCriteria.EARLY)

-
HEURISTIC
*= <StopCriteria.HEURISTIC: 1>*[#](https://docs.openvino.ai#openvino_genai.StopCriteria.HEURISTIC)

-
NEVER
*= <StopCriteria.NEVER: 2>*[#](https://docs.openvino.ai#openvino_genai.StopCriteria.NEVER)

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino_genai.StopCriteria.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino_genai.StopCriteria.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.StopCriteria.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino_genai.StopCriteria.__dir__) Default dir() implementation.


-
__eq__(
*self: object*,*other: object*,*/*) bool[#](https://docs.openvino.ai#openvino_genai.StopCriteria.__eq__)

-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino_genai.StopCriteria.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.StopCriteria.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.StopCriteria.__getattribute__) Return getattr(self, name).


-
__getstate__(
*self: object*,*/*) int[#](https://docs.openvino.ai#openvino_genai.StopCriteria.__getstate__)

-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.StopCriteria.__gt__) Return self>value.


-
__hash__(
*self: object*,*/*) int[#](https://docs.openvino.ai#openvino_genai.StopCriteria.__hash__)

-
__index__(
*self:*,[openvino_genai.py_openvino_genai.StopCriteria](https://docs.openvino.ai#openvino_genai.StopCriteria)*/*) int[#](https://docs.openvino.ai#openvino_genai.StopCriteria.__index__)

-
__init__(
*self:*,[openvino_genai.py_openvino_genai.StopCriteria](https://docs.openvino.ai#openvino_genai.StopCriteria)*value: SupportsInt*) None[#](https://docs.openvino.ai#id0)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino_genai.StopCriteria.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__int__(
*self:*,[openvino_genai.py_openvino_genai.StopCriteria](https://docs.openvino.ai#openvino_genai.StopCriteria)*/*) int[#](https://docs.openvino.ai#openvino_genai.StopCriteria.__int__)

-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.StopCriteria.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.StopCriteria.__lt__) Return self<value.


-
__members__
*= {'EARLY': <StopCriteria.EARLY: 0>, 'HEURISTIC': <StopCriteria.HEURISTIC: 1>, 'NEVER': <StopCriteria.NEVER: 2>}*[#](https://docs.openvino.ai#openvino_genai.StopCriteria.__members__)

-
__ne__(
*self: object*,*other: object*,*/*) bool[#](https://docs.openvino.ai#openvino_genai.StopCriteria.__ne__)

-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino_genai.StopCriteria.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino_genai.StopCriteria.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino_genai.StopCriteria.__reduce_ex__) Helper for pickle.


-
__repr__(
*self: object*,*/*) str[#](https://docs.openvino.ai#openvino_genai.StopCriteria.__repr__)

-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.StopCriteria.__setattr__) Implement setattr(self, name, value).


-
__setstate__(
*self:*,[openvino_genai.py_openvino_genai.StopCriteria](https://docs.openvino.ai#openvino_genai.StopCriteria)*state: SupportsInt*,*/*) None[#](https://docs.openvino.ai#openvino_genai.StopCriteria.__setstate__)

-
__sizeof__()
[#](https://docs.openvino.ai#openvino_genai.StopCriteria.__sizeof__) Size of object in memory, in bytes.


-
__str__(
*self: object*,*/*) str[#](https://docs.openvino.ai#openvino_genai.StopCriteria.__str__)

-
__subclasshook__()
[#](https://docs.openvino.ai#openvino_genai.StopCriteria.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino_genai.StopCriteria._pybind11_conduit_v1_)

-
*property*name[#](https://docs.openvino.ai#openvino_genai.StopCriteria.name)

-
*property*value[#](https://docs.openvino.ai#openvino_genai.StopCriteria.value)