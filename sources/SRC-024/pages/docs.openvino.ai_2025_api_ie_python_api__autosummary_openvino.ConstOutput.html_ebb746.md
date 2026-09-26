source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.ConstOutput.html
lastmod: 

# openvino.ConstOutput[#](https://docs.openvino.ai#openvino-constoutput)

-
*class*openvino.ConstOutput[#](https://docs.openvino.ai#openvino.ConstOutput) Bases:

`pybind11_object`

openvino.ConstOutput represents port/node output.

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.ConstOutput.__init__)

Methods

(self)`__copy__`

(self, arg0)`__deepcopy__`

(name, /)`__delattr__`

Implement delattr(self, name).

()`__dir__`

Default dir() implementation.

(self, arg0)`__eq__`

(format_spec, /)`__format__`

Default object formatter.

(self, arg0)`__ge__`

(name, /)`__getattribute__`

Return getattr(self, name).

Helper for pickle.

(self, arg0)`__gt__`

(self)`__hash__`

(*args, **kwargs)`__init__`

This method is called when a class is subclassed.

(self, arg0)`__le__`

(self, arg0)`__lt__`

(self, arg0)`__ne__`

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

(self)`_from_node`

(self)`get_any_name`

One of the tensor names associated with this output.

(self)`get_element_type`

The element type of the output referred to by this output handle.

(self)`get_index`

The index of the output referred to by this output handle.

(self)`get_names`

The tensor names associated with this output.

(self)`get_node`

Get node referenced by this output handle.

(self)`get_partial_shape`

The partial shape of the output referred to by this output handle.

(self)`get_rt_info`

Returns RTMap which is a dictionary of user defined runtime info.

(self)`get_shape`

The shape of the output referred to by this output handle.

(self)`get_target_inputs`

A set containing handles for all inputs, targeted by the output, referenced by this output handle.

(self)`get_tensor`

A reference to the tensor descriptor for this output.

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.ConstOutput.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.ConstOutput.__class__) alias of

`pybind11_type`


-
__copy__(
*self:*)[openvino._pyopenvino.ConstOutput](https://docs.openvino.ai#openvino.ConstOutput)[openvino._pyopenvino.ConstOutput](https://docs.openvino.ai#openvino.ConstOutput)[#](https://docs.openvino.ai#openvino.ConstOutput.__copy__)

-
__deepcopy__(
*self:*,[openvino._pyopenvino.ConstOutput](https://docs.openvino.ai#openvino.ConstOutput)*arg0: dict*) None[#](https://docs.openvino.ai#openvino.ConstOutput.__deepcopy__)

-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.ConstOutput.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.ConstOutput.__dir__) Default dir() implementation.


-
__eq__(
*self:*,[openvino._pyopenvino.ConstOutput](https://docs.openvino.ai#openvino.ConstOutput)*arg0:*) bool[openvino._pyopenvino.ConstOutput](https://docs.openvino.ai#openvino.ConstOutput)[#](https://docs.openvino.ai#openvino.ConstOutput.__eq__)

-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.ConstOutput.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*self:*,[openvino._pyopenvino.ConstOutput](https://docs.openvino.ai#openvino.ConstOutput)*arg0:*) bool[openvino._pyopenvino.ConstOutput](https://docs.openvino.ai#openvino.ConstOutput)[#](https://docs.openvino.ai#openvino.ConstOutput.__ge__)

-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.ConstOutput.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino.ConstOutput.__getstate__) Helper for pickle.


-
__gt__(
*self:*,[openvino._pyopenvino.ConstOutput](https://docs.openvino.ai#openvino.ConstOutput)*arg0:*) bool[openvino._pyopenvino.ConstOutput](https://docs.openvino.ai#openvino.ConstOutput)[#](https://docs.openvino.ai#openvino.ConstOutput.__gt__)

-
__hash__(
*self:*) int[openvino._pyopenvino.ConstOutput](https://docs.openvino.ai#openvino.ConstOutput)[#](https://docs.openvino.ai#openvino.ConstOutput.__hash__)

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.ConstOutput.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*self:*,[openvino._pyopenvino.ConstOutput](https://docs.openvino.ai#openvino.ConstOutput)*arg0:*) bool[openvino._pyopenvino.ConstOutput](https://docs.openvino.ai#openvino.ConstOutput)[#](https://docs.openvino.ai#openvino.ConstOutput.__le__)

-
__lt__(
*self:*,[openvino._pyopenvino.ConstOutput](https://docs.openvino.ai#openvino.ConstOutput)*arg0:*) bool[openvino._pyopenvino.ConstOutput](https://docs.openvino.ai#openvino.ConstOutput)[#](https://docs.openvino.ai#openvino.ConstOutput.__lt__)

-
__ne__(
*self:*,[openvino._pyopenvino.ConstOutput](https://docs.openvino.ai#openvino.ConstOutput)*arg0:*) bool[openvino._pyopenvino.ConstOutput](https://docs.openvino.ai#openvino.ConstOutput)[#](https://docs.openvino.ai#openvino.ConstOutput.__ne__)

-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.ConstOutput.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.ConstOutput.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.ConstOutput.__reduce_ex__) Helper for pickle.


-
__repr__(
*self:*) str[openvino._pyopenvino.ConstOutput](https://docs.openvino.ai#openvino.ConstOutput)[#](https://docs.openvino.ai#openvino.ConstOutput.__repr__)

-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.ConstOutput.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino.ConstOutput.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino.ConstOutput.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.ConstOutput.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_from_node(
*self:*)[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[openvino._pyopenvino.Output](https://docs.openvino.ai/openvino.Output.html#openvino.Output)[#](https://docs.openvino.ai#openvino.ConstOutput._from_node)

-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.ConstOutput._pybind11_conduit_v1_)

-
*property*any_name[#](https://docs.openvino.ai#openvino.ConstOutput.any_name)

-
*property*element_type[#](https://docs.openvino.ai#openvino.ConstOutput.element_type)

-
get_any_name(
*self:*) str[openvino._pyopenvino.ConstOutput](https://docs.openvino.ai#openvino.ConstOutput)[#](https://docs.openvino.ai#openvino.ConstOutput.get_any_name) One of the tensor names associated with this output. Note: first name in lexicographical order.

- Returns:
Tensor name as string.

- Return type:
str



-
get_element_type(
*self:*)[openvino._pyopenvino.ConstOutput](https://docs.openvino.ai#openvino.ConstOutput)[openvino._pyopenvino.Type](https://docs.openvino.ai/openvino.Type.html#openvino.Type)[#](https://docs.openvino.ai#openvino.ConstOutput.get_element_type) The element type of the output referred to by this output handle.

- Returns:
Type of the output.

- Return type:


-
get_index(
*self:*) int[openvino._pyopenvino.ConstOutput](https://docs.openvino.ai#openvino.ConstOutput)[#](https://docs.openvino.ai#openvino.ConstOutput.get_index) The index of the output referred to by this output handle.

- Returns:
Index value as integer.

- Return type:
int



-
get_names(
*self:*) set[str][openvino._pyopenvino.ConstOutput](https://docs.openvino.ai#openvino.ConstOutput)[#](https://docs.openvino.ai#openvino.ConstOutput.get_names) The tensor names associated with this output.

- Returns:
set of tensor names.

- Return type:
set[str]



-
get_node(
*self:*)[openvino._pyopenvino.ConstOutput](https://docs.openvino.ai#openvino.ConstOutput)[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.ConstOutput.get_node) Get node referenced by this output handle.

- Returns:
Node object referenced by this output handle.

- Return type:


-
get_partial_shape(
*self:*)[openvino._pyopenvino.ConstOutput](https://docs.openvino.ai#openvino.ConstOutput)[openvino._pyopenvino.PartialShape](https://docs.openvino.ai/openvino.PartialShape.html#openvino.PartialShape)[#](https://docs.openvino.ai#openvino.ConstOutput.get_partial_shape) The partial shape of the output referred to by this output handle.

- Returns:
Copy of PartialShape of the output.

- Return type:


-
get_rt_info(
*self:*)[openvino._pyopenvino.ConstOutput](https://docs.openvino.ai#openvino.ConstOutput)[openvino._pyopenvino.RTMap](https://docs.openvino.ai/openvino.RTMap.html#openvino.RTMap)[#](https://docs.openvino.ai#openvino.ConstOutput.get_rt_info) Returns RTMap which is a dictionary of user defined runtime info.

- Returns:
A dictionary of user defined data.

- Return type:


-
get_shape(
*self:*)[openvino._pyopenvino.ConstOutput](https://docs.openvino.ai#openvino.ConstOutput)[openvino._pyopenvino.Shape](https://docs.openvino.ai/openvino.Shape.html#openvino.Shape)[#](https://docs.openvino.ai#openvino.ConstOutput.get_shape) The shape of the output referred to by this output handle.

- Returns:
Copy of Shape of the output.

- Return type:


-
get_target_inputs(
*self:*) set[[openvino._pyopenvino.ConstOutput](https://docs.openvino.ai#openvino.ConstOutput)[openvino._pyopenvino.Input](https://docs.openvino.ai/openvino.Input.html#openvino.Input)][#](https://docs.openvino.ai#openvino.ConstOutput.get_target_inputs) A set containing handles for all inputs, targeted by the output, referenced by this output handle.

- Returns:
set of Inputs.

- Return type:
set[

[openvino.Input](https://docs.openvino.ai/openvino.Input.html#openvino.Input)]


-
get_tensor(
*self:*) openvino._pyopenvino.DescriptorTensor[openvino._pyopenvino.ConstOutput](https://docs.openvino.ai#openvino.ConstOutput)[#](https://docs.openvino.ai#openvino.ConstOutput.get_tensor) A reference to the tensor descriptor for this output.

- Returns:
Tensor of the output.

- Return type:
openvino._pyopenvino.DescriptorTensor



-
*property*index[#](https://docs.openvino.ai#openvino.ConstOutput.index)

-
*property*names[#](https://docs.openvino.ai#openvino.ConstOutput.names)

-
*property*node[#](https://docs.openvino.ai#openvino.ConstOutput.node)

-
*property*partial_shape[#](https://docs.openvino.ai#openvino.ConstOutput.partial_shape)

-
*property*rt_info[#](https://docs.openvino.ai#openvino.ConstOutput.rt_info)

-
*property*shape[#](https://docs.openvino.ai#openvino.ConstOutput.shape)

-
*property*target_inputs[#](https://docs.openvino.ai#openvino.ConstOutput.target_inputs)

-
*property*tensor[#](https://docs.openvino.ai#openvino.ConstOutput.tensor)

-
__init__(