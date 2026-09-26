source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.frontend.Place.html
lastmod: 

# openvino.frontend.Place[#](https://docs.openvino.ai#openvino-frontend-place)

-
*class*openvino.frontend.Place[#](https://docs.openvino.ai#openvino.frontend.Place) Bases:

`pybind11_object`

openvino.frontend.Place wraps ov::frontend::Place

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.frontend.Place.__init__)

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

()`__repr__`

Return repr(self).

(name, value, /)`__setattr__`

Implement setattr(self, name, value).

Size of object in memory, in bytes.

()`__str__`

Return str(self).

Abstract classes can override this to customize issubclass().

(self[, ...])`get_consuming_operations`

Returns references to all operation nodes that consume data from this place for specified output port.

(self)`get_consuming_ports`

Returns all input ports that consume data flows through this place.

(self[, input_name, ...])`get_input_port`

For operation node returns reference to an input port with specified name and index.

(self)`get_names`

All associated names (synonyms) that identify this place in the graph in a framework specific way.

(self[, output_name, ...])`get_output_port`

For operation node returns reference to an output port with specified name and index.

(self[, input_name, ...])`get_producing_operation`

Get an operation node place that immediately produces data for this place.

(self)`get_producing_port`

Returns a port that produces data for this place.

(self[, input_name, ...])`get_source_tensor`

Returns a tensor place that supplies data for this place; applicable for operations, input ports and input edges.

(self[, output_name, ...])`get_target_tensor`

Returns a tensor place that gets data from this place; applicable for operations, output ports and output edges.

(self, other)`is_equal`

Returns true if another place is the same as this place.

(self, other)`is_equal_data`

Returns true if another place points to the same data. Note: The same data means all places on path: output port -> output edge -> tensor -> input edge -> input port.

(self)`is_input`

Returns true if this place is input for a model.

(self)`is_output`

Returns true if this place is output for a model.

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.frontend.Place.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.frontend.Place.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.frontend.Place.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.frontend.Place.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.Place.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.frontend.Place.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.Place.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.frontend.Place.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino.frontend.Place.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.Place.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino.frontend.Place.__hash__) Return hash(self).


-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.frontend.Place.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.Place.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.Place.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.Place.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.frontend.Place.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.frontend.Place.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.frontend.Place.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino.frontend.Place.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.Place.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino.frontend.Place.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino.frontend.Place.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.frontend.Place.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.frontend.Place._pybind11_conduit_v1_)

-
get_consuming_operations(
*self:*,[openvino._pyopenvino.Place](https://docs.openvino.ai#openvino.frontend.Place)*output_name: object = None*,*output_port_index: object = None*) list[[openvino._pyopenvino.Place](https://docs.openvino.ai#openvino.frontend.Place)][#](https://docs.openvino.ai#openvino.frontend.Place.get_consuming_operations) Returns references to all operation nodes that consume data from this place for specified output port. Note: It can be called for any kind of graph place searching for the first consuming operations.

- Parameters:
**output_name**(*str*) – Name of output port group. May not be set if node has one output port group.**output_port_index**(*int*) – If place is an operational node it specifies which output port should be considered May not be set if node has only one output port.

- Returns:
A list with all operation node references that consumes data from this place

- Return type:
list[

[openvino.frontend.Place](https://docs.openvino.ai#openvino.frontend.Place)]


-
get_consuming_ports(
*self:*) list[[openvino._pyopenvino.Place](https://docs.openvino.ai#openvino.frontend.Place)[openvino._pyopenvino.Place](https://docs.openvino.ai#openvino.frontend.Place)][#](https://docs.openvino.ai#openvino.frontend.Place.get_consuming_ports) Returns all input ports that consume data flows through this place.

- Returns:
Input ports that consume data flows through this place.

- Return type:
list[

[openvino.frontend.Place](https://docs.openvino.ai#openvino.frontend.Place)]


-
get_input_port(
*self:*,[openvino._pyopenvino.Place](https://docs.openvino.ai#openvino.frontend.Place)*input_name: object = None*,*input_port_index: object = None*)[openvino._pyopenvino.Place](https://docs.openvino.ai#openvino.frontend.Place)[#](https://docs.openvino.ai#openvino.frontend.Place.get_input_port) For operation node returns reference to an input port with specified name and index.

- Parameters:
**input_name**(*str*) – Name of port group. May not be set if node has one input port group.**input_port_index**(*int*) – Input port index in a group. May not be set if node has one input port in a group.

- Returns:
Appropriate input port place.

- Return type:


-
get_names(
*self:*) list[str][openvino._pyopenvino.Place](https://docs.openvino.ai#openvino.frontend.Place)[#](https://docs.openvino.ai#openvino.frontend.Place.get_names) All associated names (synonyms) that identify this place in the graph in a framework specific way.

- Returns:
A vector of strings each representing a name that identifies this place in the graph. Can be empty if there are no names associated with this place or name cannot be attached.

- Return type:
list[str]



-
get_output_port(
*self:*,[openvino._pyopenvino.Place](https://docs.openvino.ai#openvino.frontend.Place)*output_name: object = None*,*output_port_index: object = None*)[openvino._pyopenvino.Place](https://docs.openvino.ai#openvino.frontend.Place)[#](https://docs.openvino.ai#openvino.frontend.Place.get_output_port) For operation node returns reference to an output port with specified name and index.

- Parameters:
**output_name**(*str*) – Name of output port group. May not be set if node has one output port group.**output_port_index**(*int*) – Output port index. May not be set if node has one output port in a group.

- Returns:
Appropriate output port place.

- Return type:


-
get_producing_operation(
*self:*,[openvino._pyopenvino.Place](https://docs.openvino.ai#openvino.frontend.Place)*input_name: object = None*,*input_port_index: object = None*)[openvino._pyopenvino.Place](https://docs.openvino.ai#openvino.frontend.Place)[#](https://docs.openvino.ai#openvino.frontend.Place.get_producing_operation) Get an operation node place that immediately produces data for this place.

- Parameters:
**input_name**(*str*) – Name of port group. May not be set if node has one input port group.**input_port_index**(*int*) – If a given place is itself an operation node, this specifies a port index. May not be set if place has only one input port.

- Returns:
An operation place that produces data for this place.

- Return type:


-
get_producing_port(
*self:*)[openvino._pyopenvino.Place](https://docs.openvino.ai#openvino.frontend.Place)[openvino._pyopenvino.Place](https://docs.openvino.ai#openvino.frontend.Place)[#](https://docs.openvino.ai#openvino.frontend.Place.get_producing_port) Returns a port that produces data for this place.

- Returns:
A port place that produces data for this place.

- Return type:


-
get_source_tensor(
*self:*,[openvino._pyopenvino.Place](https://docs.openvino.ai#openvino.frontend.Place)*input_name: object = None*,*input_port_index: object = None*)[openvino._pyopenvino.Place](https://docs.openvino.ai#openvino.frontend.Place)[#](https://docs.openvino.ai#openvino.frontend.Place.get_source_tensor) Returns a tensor place that supplies data for this place; applicable for operations, input ports and input edges.

:param input_name : Name of port group. May not be set if node has one input port group. :type input_name: str :param input_port_index: Input port index for operational node. May not be specified if place has only one input port. :type input_port_index: int :return: A tensor place which supplies data for this place. :rtype: openvino.frontend.Place


-
get_target_tensor(
*self:*,[openvino._pyopenvino.Place](https://docs.openvino.ai#openvino.frontend.Place)*output_name: object = None*,*output_port_index: object = None*)[openvino._pyopenvino.Place](https://docs.openvino.ai#openvino.frontend.Place)[#](https://docs.openvino.ai#openvino.frontend.Place.get_target_tensor) Returns a tensor place that gets data from this place; applicable for operations, output ports and output edges.

- Parameters:
**output_name**(*str*) – Name of output port group. May not be set if node has one output port group.**output_port_index**(*int*) – Output port index if the current place is an operation node and has multiple output ports. May not be set if place has only one output port.

- Returns:
A tensor place which hold the resulting value for this place.

- Return type:


-
is_equal(
*self:*,[openvino._pyopenvino.Place](https://docs.openvino.ai#openvino.frontend.Place)*other:*) bool[openvino._pyopenvino.Place](https://docs.openvino.ai#openvino.frontend.Place)[#](https://docs.openvino.ai#openvino.frontend.Place.is_equal) Returns true if another place is the same as this place.

- Parameters:
**other**() – Another place object.*openvino.frontend.Place*- Returns:
True if another place is the same as this place.

- Return type:
bool



-
is_equal_data(
*self:*,[openvino._pyopenvino.Place](https://docs.openvino.ai#openvino.frontend.Place)*other:*) bool[openvino._pyopenvino.Place](https://docs.openvino.ai#openvino.frontend.Place)[#](https://docs.openvino.ai#openvino.frontend.Place.is_equal_data) Returns true if another place points to the same data. Note: The same data means all places on path:

output port -> output edge -> tensor -> input edge -> input port.

- Parameters:
**other**() – Another place object.*openvino.frontend.Place*- Returns:
True if another place points to the same data.

- Return type:
bool



-
is_input(
*self:*) bool[openvino._pyopenvino.Place](https://docs.openvino.ai#openvino.frontend.Place)[#](https://docs.openvino.ai#openvino.frontend.Place.is_input) Returns true if this place is input for a model.

- Returns:
True if this place is input for a model

- Return type:
bool



-
is_output(
*self:*) bool[openvino._pyopenvino.Place](https://docs.openvino.ai#openvino.frontend.Place)[#](https://docs.openvino.ai#openvino.frontend.Place.is_output) Returns true if this place is output for a model.

- Returns:
True if this place is output for a model.

- Return type:
bool



-
__init__(