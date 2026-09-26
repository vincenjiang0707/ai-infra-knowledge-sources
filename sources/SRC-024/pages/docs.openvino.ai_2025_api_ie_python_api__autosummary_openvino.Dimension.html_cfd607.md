source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.Dimension.html
lastmod: 

# openvino.Dimension[#](https://docs.openvino.ai#openvino-dimension)

-
*class*openvino.Dimension[#](https://docs.openvino.ai#openvino.Dimension) Bases:

`pybind11_object`

openvino.Dimension wraps ov::Dimension

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.Dimension.__init__) Overloaded function.

__init__(self: openvino._pyopenvino.Dimension) -> None

__init__(self: openvino._pyopenvino.Dimension, dimension: typing.SupportsInt) -> None

Construct a static dimension.

- param dimension:
Value of the dimension.

- type dimension:
int


__init__(self: openvino._pyopenvino.Dimension, min_dimension: typing.SupportsInt, max_dimension: typing.SupportsInt) -> None

Construct a dynamic dimension with bounded range.

- param min_dimension:
The lower inclusive limit for the dimension.

- type min_dimension:
int

- param max_dimension:
The upper inclusive limit for the dimension.

- type max_dimension:
int


__init__(self: openvino._pyopenvino.Dimension, str: str) -> None



Methods

(name, /)`__delattr__`

Implement delattr(self, name).

()`__dir__`

Default dir() implementation.

(*args, **kwargs)`__eq__`

Overloaded function.

(format_spec, /)`__format__`

Default object formatter.

(value, /)`__ge__`

Return self>=value.

(name, /)`__getattribute__`

Return getattr(self, name).

Helper for pickle.

(value, /)`__gt__`

Return self>value.

(*args, **kwargs)`__init__`

Overloaded function.

This method is called when a class is subclassed.

(value, /)`__le__`

Return self<=value.

(self)`__len__`

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

(self)`__str__`

Abstract classes can override this to customize issubclass().

(self, dim)`compatible`

Check whether this dimension is capable of being merged with the argument dimension.

()`dynamic`

(self)`get_length`

Return this dimension as integer.

(self)`get_max_length`

Return this dimension's max_dimension as integer.

(self)`get_min_length`

Return this dimension's min_dimension as integer.

(self)`get_symbol`

Return this dimension's symbol as Symbol object.

(self)`has_symbol`

Check if Dimension has meaningful symbol.

(self, dim)`refines`

Check whether this dimension is a refinement of the argument.

(self, dim)`relaxes`

Check whether this dimension is a relaxation of the argument.

(self, dim)`same_scheme`

Return this dimension's max_dimension as integer.

(self, symbol)`set_symbol`

Sets provided Symbol as this dimension's symbol.

(self)`to_string`

Attributes

Check if Dimension is dynamic.

Check if Dimension is static.

Return this dimension's max_dimension as integer.

Return this dimension's min_dimension as integer.

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.Dimension.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.Dimension.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.Dimension.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.Dimension.__dir__) Default dir() implementation.


-
__eq__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.Dimension.__eq__) Overloaded function.

__eq__(self: openvino._pyopenvino.Dimension, arg0: openvino._pyopenvino.Dimension) -> bool

__eq__(self: openvino._pyopenvino.Dimension, arg0: typing.SupportsInt) -> bool



-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.Dimension.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Dimension.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.Dimension.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino.Dimension.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Dimension.__gt__) Return self>value.


-
__hash__
*= None*[#](https://docs.openvino.ai#openvino.Dimension.__hash__)

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0) Overloaded function.

__init__(self: openvino._pyopenvino.Dimension) -> None

__init__(self: openvino._pyopenvino.Dimension, dimension: typing.SupportsInt) -> None

Construct a static dimension.

- param dimension:
Value of the dimension.

- type dimension:
int


__init__(self: openvino._pyopenvino.Dimension, min_dimension: typing.SupportsInt, max_dimension: typing.SupportsInt) -> None

Construct a dynamic dimension with bounded range.

- param min_dimension:
The lower inclusive limit for the dimension.

- type min_dimension:
int

- param max_dimension:
The upper inclusive limit for the dimension.

- type max_dimension:
int


__init__(self: openvino._pyopenvino.Dimension, str: str) -> None



-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.Dimension.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Dimension.__le__) Return self<=value.


-
__len__(
*self:*) int[openvino._pyopenvino.Dimension](https://docs.openvino.ai#openvino.Dimension)[#](https://docs.openvino.ai#openvino.Dimension.__len__)

-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Dimension.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Dimension.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.Dimension.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.Dimension.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.Dimension.__reduce_ex__) Helper for pickle.


-
__repr__(
*self:*) str[openvino._pyopenvino.Dimension](https://docs.openvino.ai#openvino.Dimension)[#](https://docs.openvino.ai#openvino.Dimension.__repr__)

-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.Dimension.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino.Dimension.__sizeof__) Size of object in memory, in bytes.


-
__str__(
*self:*) str[openvino._pyopenvino.Dimension](https://docs.openvino.ai#openvino.Dimension)[#](https://docs.openvino.ai#openvino.Dimension.__str__)

-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.Dimension.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.Dimension._pybind11_conduit_v1_)

-
compatible(
*self:*,[openvino._pyopenvino.Dimension](https://docs.openvino.ai#openvino.Dimension)*dim:*) bool[openvino._pyopenvino.Dimension](https://docs.openvino.ai#openvino.Dimension)[#](https://docs.openvino.ai#openvino.Dimension.compatible) Check whether this dimension is capable of being merged with the argument dimension.

- Parameters:
**dim**() – The dimension to compare this dimension with.*Dimension*- Returns:
True if this dimension is compatible with d, else False.

- Return type:
bool



-
*static*dynamic()[openvino._pyopenvino.Dimension](https://docs.openvino.ai#openvino.Dimension)[#](https://docs.openvino.ai#openvino.Dimension.dynamic)

-
get_length(
*self:*) int[openvino._pyopenvino.Dimension](https://docs.openvino.ai#openvino.Dimension)[#](https://docs.openvino.ai#openvino.Dimension.get_length) Return this dimension as integer. This dimension must be static and non-negative.

- Returns:
Value of the dimension.

- Return type:
int



-
get_max_length(
*self:*) int[openvino._pyopenvino.Dimension](https://docs.openvino.ai#openvino.Dimension)[#](https://docs.openvino.ai#openvino.Dimension.get_max_length) Return this dimension’s max_dimension as integer. This dimension must be dynamic and non-negative.

- Returns:
Value of the dimension.

- Return type:
int



-
get_min_length(
*self:*) int[openvino._pyopenvino.Dimension](https://docs.openvino.ai#openvino.Dimension)[#](https://docs.openvino.ai#openvino.Dimension.get_min_length) Return this dimension’s min_dimension as integer. This dimension must be dynamic and non-negative.

- Returns:
Value of the dimension.

- Return type:
int



-
get_symbol(
*self:*)[openvino._pyopenvino.Dimension](https://docs.openvino.ai#openvino.Dimension)[openvino._pyopenvino.Symbol](https://docs.openvino.ai/openvino.Symbol.html#openvino.Symbol)[#](https://docs.openvino.ai#openvino.Dimension.get_symbol) Return this dimension’s symbol as Symbol object.

- Returns:
Value of the dimension.

- Return type:


-
has_symbol(
*self:*) bool[openvino._pyopenvino.Dimension](https://docs.openvino.ai#openvino.Dimension)[#](https://docs.openvino.ai#openvino.Dimension.has_symbol) Check if Dimension has meaningful symbol.

- Returns:
True if symbol was set, else False.

- Return type:
bool



-
*property*is_dynamic[#](https://docs.openvino.ai#openvino.Dimension.is_dynamic) Check if Dimension is dynamic. :return: True if dynamic, else False. :rtype: bool


-
*property*is_static[#](https://docs.openvino.ai#openvino.Dimension.is_static) Check if Dimension is static.

- Returns:
True if static, else False.

- Return type:
bool



-
*property*max_length[#](https://docs.openvino.ai#openvino.Dimension.max_length) Return this dimension’s max_dimension as integer. This dimension must be dynamic and non-negative.

- Returns:
Value of the dimension.

- Return type:
int



-
*property*min_length[#](https://docs.openvino.ai#openvino.Dimension.min_length) Return this dimension’s min_dimension as integer. This dimension must be dynamic and non-negative.

- Returns:
Value of the dimension.

- Return type:
int



-
refines(
*self:*,[openvino._pyopenvino.Dimension](https://docs.openvino.ai#openvino.Dimension)*dim:*) bool[openvino._pyopenvino.Dimension](https://docs.openvino.ai#openvino.Dimension)[#](https://docs.openvino.ai#openvino.Dimension.refines) Check whether this dimension is a refinement of the argument. This dimension refines (or is a refinement of) d if:

this and d are static and equal

d dimension contains this dimension


this.refines(d) is equivalent to d.relaxes(this).

- Parameters:
**dim**() – The dimension to compare this dimension with.*Dimension*- Returns:
True if this dimension refines d, else False.

- Return type:
bool



-
relaxes(
*self:*,[openvino._pyopenvino.Dimension](https://docs.openvino.ai#openvino.Dimension)*dim:*) bool[openvino._pyopenvino.Dimension](https://docs.openvino.ai#openvino.Dimension)[#](https://docs.openvino.ai#openvino.Dimension.relaxes) Check whether this dimension is a relaxation of the argument. This dimension relaxes (or is a relaxation of) d if:

this and d are static and equal

this dimension contains d dimension


this.relaxes(d) is equivalent to d.refines(this).

- Parameters:
**dim**() – The dimension to compare this dimension with.*Dimension*- Returns:
True if this dimension relaxes d, else False.

- Return type:
bool



-
same_scheme(
*self:*,[openvino._pyopenvino.Dimension](https://docs.openvino.ai#openvino.Dimension)*dim:*) bool[openvino._pyopenvino.Dimension](https://docs.openvino.ai#openvino.Dimension)[#](https://docs.openvino.ai#openvino.Dimension.same_scheme) Return this dimension’s max_dimension as integer. This dimension must be dynamic and non-negative.

- Parameters:
**dim**() – The other dimension to compare this dimension to.*Dimension*- Returns:
True if this dimension and dim are both dynamic, or if they are both static and equal, otherwise False.

- Return type:
bool



-
set_symbol(
*self:*,[openvino._pyopenvino.Dimension](https://docs.openvino.ai#openvino.Dimension)*symbol:*) None[openvino._pyopenvino.Symbol](https://docs.openvino.ai/openvino.Symbol.html#openvino.Symbol)[#](https://docs.openvino.ai#openvino.Dimension.set_symbol) Sets provided Symbol as this dimension’s symbol.

- Parameters:
**symbol**() – The symbol to set to this dimension.*openvino.Symbol*


-
to_string(
*self:*) str[openvino._pyopenvino.Dimension](https://docs.openvino.ai#openvino.Dimension)[#](https://docs.openvino.ai#openvino.Dimension.to_string)

-
__init__(