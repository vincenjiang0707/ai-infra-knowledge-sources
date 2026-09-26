source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.Input.html
lastmod: 

# openvino.Input[#](https://docs.openvino.ai#openvino-input)

-
*class*openvino.Input[#](https://docs.openvino.ai#openvino.Input) Bases:

`pybind11_object`

openvino.Input wraps ov::Input<Node>

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.Input.__init__)

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

(self)`get_element_type`

The element type of the input referred to by this input handle.

(self)`get_index`

The index of the input referred to by this input handle.

(self)`get_node`

Get node referenced by this input handle.

(self)`get_partial_shape`

The partial shape of the input referred to by this input handle.

(self)`get_rt_info`

Returns RTMap which is a dictionary of user defined runtime info.

(self)`get_shape`

The shape of the input referred to by this input handle.

(self)`get_source_output`

A handle to the output that is connected to this input.

(self)`get_tensor`

A reference to the tensor descriptor for this input.

(self, new_source_output)`replace_source_output`

Replaces the source output of this input.

(self, value, key)`set_rt_info`

Add a value to the runtime info.

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.Input.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.Input.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.Input.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.Input.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Input.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.Input.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Input.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.Input.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino.Input.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Input.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino.Input.__hash__) Return hash(self).


-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.Input.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Input.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Input.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Input.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.Input.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.Input.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.Input.__reduce_ex__) Helper for pickle.


-
__repr__(
*self:*) str[openvino._pyopenvino.Input](https://docs.openvino.ai#openvino.Input)[#](https://docs.openvino.ai#openvino.Input.__repr__)

-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.Input.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino.Input.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino.Input.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.Input.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.Input._pybind11_conduit_v1_)

-
get_element_type(
*self:*)[openvino._pyopenvino.Input](https://docs.openvino.ai#openvino.Input)[openvino._pyopenvino.Type](https://docs.openvino.ai/openvino.Type.html#openvino.Type)[#](https://docs.openvino.ai#openvino.Input.get_element_type) The element type of the input referred to by this input handle.

- Returns:
Type of the input.

- Return type:


-
get_index(
*self:*) int[openvino._pyopenvino.Input](https://docs.openvino.ai#openvino.Input)[#](https://docs.openvino.ai#openvino.Input.get_index) The index of the input referred to by this input handle.

- Returns:
Index value as integer.

- Return type:
int



-
get_node(
*self:*) ov::Node[openvino._pyopenvino.Input](https://docs.openvino.ai#openvino.Input)[#](https://docs.openvino.ai#openvino.Input.get_node) Get node referenced by this input handle.

- Returns:
Node object referenced by this input handle.

- Return type:


-
get_partial_shape(
*self:*)[openvino._pyopenvino.Input](https://docs.openvino.ai#openvino.Input)[openvino._pyopenvino.PartialShape](https://docs.openvino.ai/openvino.PartialShape.html#openvino.PartialShape)[#](https://docs.openvino.ai#openvino.Input.get_partial_shape) The partial shape of the input referred to by this input handle.

- Returns:
PartialShape of the input.

- Return type:


-
get_rt_info(
*self:*)[openvino._pyopenvino.Input](https://docs.openvino.ai#openvino.Input)[openvino._pyopenvino.RTMap](https://docs.openvino.ai/openvino.RTMap.html#openvino.RTMap)[#](https://docs.openvino.ai#openvino.Input.get_rt_info) Returns RTMap which is a dictionary of user defined runtime info.

- Returns:
A dictionary of user defined data.

- Return type:


-
get_shape(
*self:*)[openvino._pyopenvino.Input](https://docs.openvino.ai#openvino.Input)[openvino._pyopenvino.Shape](https://docs.openvino.ai/openvino.Shape.html#openvino.Shape)[#](https://docs.openvino.ai#openvino.Input.get_shape) The shape of the input referred to by this input handle.

- Returns:
Shape of the input.

- Return type:


-
get_source_output(
*self:*)[openvino._pyopenvino.Input](https://docs.openvino.ai#openvino.Input)[openvino._pyopenvino.Output](https://docs.openvino.ai/openvino.Output.html#openvino.Output)[#](https://docs.openvino.ai#openvino.Input.get_source_output) A handle to the output that is connected to this input.

- Returns:
Output that is connected to the input.

- Return type:


-
get_tensor(
*self:*) openvino._pyopenvino.DescriptorTensor[openvino._pyopenvino.Input](https://docs.openvino.ai#openvino.Input)[#](https://docs.openvino.ai#openvino.Input.get_tensor) A reference to the tensor descriptor for this input.

- Returns:
Tensor of the input.

- Return type:
openvino._pyopenvino.DescriptorTensor



-
replace_source_output(
*self:*,[openvino._pyopenvino.Input](https://docs.openvino.ai#openvino.Input)*new_source_output:*) None[openvino._pyopenvino.Output](https://docs.openvino.ai/openvino.Output.html#openvino.Output)[#](https://docs.openvino.ai#openvino.Input.replace_source_output) Replaces the source output of this input.

- Parameters:
**new_source_output**() – A handle for the output that will replace this input’s source.*openvino.Input*


-
*property*rt_info[#](https://docs.openvino.ai#openvino.Input.rt_info)

-
set_rt_info(
*self:*,[openvino._pyopenvino.Input](https://docs.openvino.ai#openvino.Input)*value: object*,*key: str*) None[#](https://docs.openvino.ai#openvino.Input.set_rt_info) Add a value to the runtime info.

- Parameters:
**value**(*Any*) – Value for the runtime info.**key**(*str*) – String that defines a key in the runtime info dictionary.



-
__init__(