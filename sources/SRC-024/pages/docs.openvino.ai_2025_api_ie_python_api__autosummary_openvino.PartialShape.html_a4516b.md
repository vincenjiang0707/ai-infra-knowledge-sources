source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.PartialShape.html
lastmod: 

# openvino.PartialShape[#](https://docs.openvino.ai#openvino-partialshape)

-
*class*openvino.PartialShape[#](https://docs.openvino.ai#openvino.PartialShape) Bases:

`pybind11_object`

openvino.PartialShape wraps ov::PartialShape

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.PartialShape.__init__) Overloaded function.

__init__(self: openvino._pyopenvino.PartialShape, arg0: openvino._pyopenvino.Shape) -> None

__init__(self: openvino._pyopenvino.PartialShape, arg0: openvino._pyopenvino.PartialShape) -> None

__init__(self: openvino._pyopenvino.PartialShape, arg0: list) -> None

__init__(self: openvino._pyopenvino.PartialShape, arg0: tuple) -> None

__init__(self: openvino._pyopenvino.PartialShape, shape: str) -> None



Methods

(self)`__copy__`

(self, arg0)`__deepcopy__`

memo

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

(*args, **kwargs)`__getitem__`

Overloaded function.

Helper for pickle.

(value, /)`__gt__`

Return self>value.

(*args, **kwargs)`__init__`

Overloaded function.

This method is called when a class is subclassed.

(self)`__iter__`

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

(*args, **kwargs)`__setitem__`

Overloaded function.

Size of object in memory, in bytes.

(self)`__str__`

Abstract classes can override this to customize issubclass().

(self, shape)`compatible`

Check whether this shape is compatible with the argument, i.e., whether it is possible to merge them.

(*args, **kwargs)`dynamic`

Overloaded function.

(self, index)`get_dimension`

Get the dimension at specified index of a partial shape.

(self)`get_max_shape`

(self)`get_min_shape`

(self)`get_shape`

(self, shape)`refines`

Check whether this shape is a refinement of the argument.

(self, shape)`relaxes`

Check whether this shape is a relaxation of the argument.

(self, shape)`same_scheme`

Check whether this shape represents the same scheme as the argument.

(self)`to_shape`

(self)`to_string`

Attributes

True if all static dimensions of the tensor are non-negative, else False.

False if this shape is static, else True.

True if this shape is static, else False.

The rank of the shape.

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.PartialShape.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.PartialShape.__class__) alias of

`pybind11_type`


-
__copy__(
*self:*)[openvino._pyopenvino.PartialShape](https://docs.openvino.ai#openvino.PartialShape)[openvino._pyopenvino.PartialShape](https://docs.openvino.ai#openvino.PartialShape)[#](https://docs.openvino.ai#openvino.PartialShape.__copy__)

-
__deepcopy__(
*self:*,[openvino._pyopenvino.PartialShape](https://docs.openvino.ai#openvino.PartialShape)*arg0: dict*)[openvino._pyopenvino.PartialShape](https://docs.openvino.ai#openvino.PartialShape)[#](https://docs.openvino.ai#openvino.PartialShape.__deepcopy__) memo


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.PartialShape.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.PartialShape.__dir__) Default dir() implementation.


-
__eq__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.PartialShape.__eq__) Overloaded function.

__eq__(self: openvino._pyopenvino.PartialShape, arg0: openvino._pyopenvino.PartialShape) -> bool

__eq__(self: openvino._pyopenvino.PartialShape, arg0: openvino._pyopenvino.Shape) -> bool

__eq__(self: openvino._pyopenvino.PartialShape, arg0: tuple) -> bool

__eq__(self: openvino._pyopenvino.PartialShape, arg0: list) -> bool



-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.PartialShape.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.PartialShape.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.PartialShape.__getattribute__) Return getattr(self, name).


-
__getitem__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.PartialShape.__getitem__) Overloaded function.

__getitem__(self: openvino._pyopenvino.PartialShape, arg0: typing.SupportsInt) -> openvino._pyopenvino.Dimension

__getitem__(self: openvino._pyopenvino.PartialShape, arg0: slice) -> openvino._pyopenvino.PartialShape



-
__getstate__()
[#](https://docs.openvino.ai#openvino.PartialShape.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.PartialShape.__gt__) Return self>value.


-
__hash__
*= None*[#](https://docs.openvino.ai#openvino.PartialShape.__hash__)

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0) Overloaded function.

__init__(self: openvino._pyopenvino.PartialShape, arg0: openvino._pyopenvino.Shape) -> None

__init__(self: openvino._pyopenvino.PartialShape, arg0: openvino._pyopenvino.PartialShape) -> None

__init__(self: openvino._pyopenvino.PartialShape, arg0: list) -> None

__init__(self: openvino._pyopenvino.PartialShape, arg0: tuple) -> None

__init__(self: openvino._pyopenvino.PartialShape, shape: str) -> None



-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.PartialShape.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__iter__(
*self:*) collections.abc.Iterator[[openvino._pyopenvino.PartialShape](https://docs.openvino.ai#openvino.PartialShape)[openvino._pyopenvino.Dimension](https://docs.openvino.ai/openvino.Dimension.html#openvino.Dimension)][#](https://docs.openvino.ai#openvino.PartialShape.__iter__)

-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.PartialShape.__le__) Return self<=value.


-
__len__(
*self:*) int[openvino._pyopenvino.PartialShape](https://docs.openvino.ai#openvino.PartialShape)[#](https://docs.openvino.ai#openvino.PartialShape.__len__)

-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.PartialShape.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.PartialShape.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.PartialShape.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.PartialShape.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.PartialShape.__reduce_ex__) Helper for pickle.


-
__repr__(
*self:*) str[openvino._pyopenvino.PartialShape](https://docs.openvino.ai#openvino.PartialShape)[#](https://docs.openvino.ai#openvino.PartialShape.__repr__)

-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.PartialShape.__setattr__) Implement setattr(self, name, value).


-
__setitem__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.PartialShape.__setitem__) Overloaded function.

__setitem__(self: openvino._pyopenvino.PartialShape, arg0: typing.SupportsInt, arg1: typing.SupportsInt) -> None

__setitem__(self: openvino._pyopenvino.PartialShape, arg0: typing.SupportsInt, arg1: openvino._pyopenvino.Dimension) -> None



-
__sizeof__()
[#](https://docs.openvino.ai#openvino.PartialShape.__sizeof__) Size of object in memory, in bytes.


-
__str__(
*self:*) str[openvino._pyopenvino.PartialShape](https://docs.openvino.ai#openvino.PartialShape)[#](https://docs.openvino.ai#openvino.PartialShape.__str__)

-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.PartialShape.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.PartialShape._pybind11_conduit_v1_)

-
*property*all_non_negative[#](https://docs.openvino.ai#openvino.PartialShape.all_non_negative) True if all static dimensions of the tensor are non-negative, else False.


-
compatible(
*self:*,[openvino._pyopenvino.PartialShape](https://docs.openvino.ai#openvino.PartialShape)*shape:*) bool[openvino._pyopenvino.PartialShape](https://docs.openvino.ai#openvino.PartialShape)[#](https://docs.openvino.ai#openvino.PartialShape.compatible) Check whether this shape is compatible with the argument, i.e., whether it is possible to merge them.

- Parameters:
**shape**() – The shape to be checked for compatibility with this shape.*openvino.PartialShape*- Returns:
True if this shape is compatible with s, else False.

- Return type:
bool



-
*static*dynamic(**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.PartialShape.dynamic) Overloaded function.

dynamic(rank: openvino._pyopenvino.Dimension = <Dimension: ?>) -> openvino._pyopenvino.PartialShape

Construct a PartialShape with the given rank and all dimensions are dynamic.

- param rank:
The rank of the PartialShape. This is the number of dimensions in the shape.

- type rank:
openvino.Dimension

- return:
A PartialShape with the given rank (or undefined rank if not provided), and all dimensions are dynamic.


dynamic(rank: typing.SupportsInt) -> openvino._pyopenvino.PartialShape

Construct a PartialShape with the given rank and all dimensions are dynamic.

- param rank:
The rank of the PartialShape. This is the number of dimensions in the shape.

- type rank:
int

- return:
A PartialShape with the given rank, and all dimensions are dynamic.




-
get_dimension(
*self:*,[openvino._pyopenvino.PartialShape](https://docs.openvino.ai#openvino.PartialShape)*index: SupportsInt*)[openvino._pyopenvino.Dimension](https://docs.openvino.ai/openvino.Dimension.html#openvino.Dimension)[#](https://docs.openvino.ai#openvino.PartialShape.get_dimension) Get the dimension at specified index of a partial shape.

- Parameters:
**index**(*int*) – The index of dimension.- Returns:
Get the particular dimension of a partial shape.

- Return type:


-
get_max_shape(
*self:*)[openvino._pyopenvino.PartialShape](https://docs.openvino.ai#openvino.PartialShape)[openvino._pyopenvino.Shape](https://docs.openvino.ai/openvino.Shape.html#openvino.Shape)[#](https://docs.openvino.ai#openvino.PartialShape.get_max_shape) - Returns:
Get the max bounding shape.

- Return type:


-
get_min_shape(
*self:*)[openvino._pyopenvino.PartialShape](https://docs.openvino.ai#openvino.PartialShape)[openvino._pyopenvino.Shape](https://docs.openvino.ai/openvino.Shape.html#openvino.Shape)[#](https://docs.openvino.ai#openvino.PartialShape.get_min_shape) - Returns:
Get the min bounding shape.

- Return type:


-
get_shape(
*self:*)[openvino._pyopenvino.PartialShape](https://docs.openvino.ai#openvino.PartialShape)[openvino._pyopenvino.Shape](https://docs.openvino.ai/openvino.Shape.html#openvino.Shape)[#](https://docs.openvino.ai#openvino.PartialShape.get_shape) - Returns:
Get the unique shape.

- Return type:


-
*property*is_dynamic[#](https://docs.openvino.ai#openvino.PartialShape.is_dynamic) False if this shape is static, else True. A shape is considered static if it has static rank, and all dimensions of the shape are static.


-
*property*is_static[#](https://docs.openvino.ai#openvino.PartialShape.is_static) True if this shape is static, else False. A shape is considered static if it has static rank, and all dimensions of the shape are static.


-
*property*rank[#](https://docs.openvino.ai#openvino.PartialShape.rank) The rank of the shape.


-
refines(
*self:*,[openvino._pyopenvino.PartialShape](https://docs.openvino.ai#openvino.PartialShape)*shape:*) bool[openvino._pyopenvino.PartialShape](https://docs.openvino.ai#openvino.PartialShape)[#](https://docs.openvino.ai#openvino.PartialShape.refines) Check whether this shape is a refinement of the argument.

- Parameters:
**shape**() – The shape which is being compared against this shape.*openvino.PartialShape*- Returns:
True if this shape refines s, else False.

- Return type:
bool



-
relaxes(
*self:*,[openvino._pyopenvino.PartialShape](https://docs.openvino.ai#openvino.PartialShape)*shape:*) bool[openvino._pyopenvino.PartialShape](https://docs.openvino.ai#openvino.PartialShape)[#](https://docs.openvino.ai#openvino.PartialShape.relaxes) Check whether this shape is a relaxation of the argument.

- Parameters:
**shape**() – The shape which is being compared against this shape.*openvino.PartialShape*- Returns:
True if this shape relaxes s, else False.

- Return type:
bool



-
same_scheme(
*self:*,[openvino._pyopenvino.PartialShape](https://docs.openvino.ai#openvino.PartialShape)*shape:*) bool[openvino._pyopenvino.PartialShape](https://docs.openvino.ai#openvino.PartialShape)[#](https://docs.openvino.ai#openvino.PartialShape.same_scheme) Check whether this shape represents the same scheme as the argument.

- Parameters:
**shape**() – The shape which is being compared against this shape.*openvino.PartialShape*- Returns:
True if shape represents the same scheme as s, else False.

- Return type:
bool



-
to_shape(
*self:*)[openvino._pyopenvino.PartialShape](https://docs.openvino.ai#openvino.PartialShape)[openvino._pyopenvino.Shape](https://docs.openvino.ai/openvino.Shape.html#openvino.Shape)[#](https://docs.openvino.ai#openvino.PartialShape.to_shape) - Returns:
Get the unique shape.

- Return type:


-
to_string(
*self:*) str[openvino._pyopenvino.PartialShape](https://docs.openvino.ai#openvino.PartialShape)[#](https://docs.openvino.ai#openvino.PartialShape.to_string)

-
__init__(