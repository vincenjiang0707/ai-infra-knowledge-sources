source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.Model.html
lastmod: 

# openvino.Model[#](https://docs.openvino.ai#openvino-model)

-
*class*openvino.Model(**args: Any*,***kwargs: Any*)[#](https://docs.openvino.ai#openvino.Model) Bases:

`object`

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.Model.__init__) Overloaded function.

__init__(self: openvino._pyopenvino.Model, other: openvino._pyopenvino.Model) -> None

__init__(self: openvino._pyopenvino.Model, results: collections.abc.Sequence[openvino._pyopenvino.op.Result], sinks: collections.abc.Sequence[openvino._pyopenvino.Node], parameters: collections.abc.Sequence[openvino._pyopenvino.op.Parameter], name: str = ‘’) -> None

Create user-defined Model which is a representation of a model.

- param results:
list of results.

- type results:
list[op.Result]

- param sinks:
list of Nodes to be used as Sinks (e.g. Assign ops).

- type sinks:
list[openvino.Node]

- param parameters:
list of parameters.

- type parameters:
list[op.Parameter]

- param name:
String to set as model’s friendly name.

- type name:
str


__init__(self: openvino._pyopenvino.Model, results: collections.abc.Sequence[openvino._pyopenvino.op.Result], parameters: collections.abc.Sequence[openvino._pyopenvino.op.Parameter], name: str = ‘’) -> None

Create user-defined Model which is a representation of a model.

- param results:
list of results.

- type results:
list[op.Result]

- param parameters:
list of parameters.

- type parameters:
list[op.Parameter]

- param name:
String to set as model’s friendly name.

- type name:
str


__init__(self: openvino._pyopenvino.Model, results: collections.abc.Sequence[openvino._pyopenvino.Node], parameters: collections.abc.Sequence[openvino._pyopenvino.op.Parameter], name: str = ‘’) -> None

Create user-defined Model which is a representation of a model.

- param results:
list of Nodes to be used as results.

- type results:
list[openvino.Node]

- param parameters:
list of parameters.

- type parameters:
list[op.Parameter]

- param name:
String to set as model’s friendly name.

- type name:
str


__init__(self: openvino._pyopenvino.Model, result: openvino._pyopenvino.Node, parameters: collections.abc.Sequence[openvino._pyopenvino.op.Parameter], name: str = ‘’) -> None

Create user-defined Model which is a representation of a model.

- param result:
Node to be used as result.

- type result:
openvino.Node

- param parameters:
list of parameters.

- type parameters:
list[op.Parameter]

- param name:
String to set as model’s friendly name.

- type name:
str


__init__(self: openvino._pyopenvino.Model, results: collections.abc.Sequence[openvino._pyopenvino.Output], parameters: collections.abc.Sequence[openvino._pyopenvino.op.Parameter], name: str = ‘’) -> None

Create user-defined Model which is a representation of a model

- param results:
list of outputs.

- type results:
list[openvino.Output]

- param parameters:
list of parameters.

- type parameters:
list[op.Parameter]

- param name:
String to set as model’s friendly name.

- type name:
str


__init__(self: openvino._pyopenvino.Model, results: collections.abc.Sequence[openvino._pyopenvino.Output], sinks: collections.abc.Sequence[openvino._pyopenvino.Node], parameters: collections.abc.Sequence[openvino._pyopenvino.op.Parameter], name: str = ‘’) -> None

Create user-defined Model which is a representation of a model

- param results:
list of outputs.

- type results:
list[openvino.Output]

- param sinks:
list of Nodes to be used as Sinks (e.g. Assign ops).

- type sinks:
list[openvino.Node]

- param parameters:
list of parameters.

- type parameters:
list[op.Parameter]

- param name:
String to set as model’s friendly name.

- type name:
str


__init__(self: openvino._pyopenvino.Model, results: collections.abc.Sequence[openvino._pyopenvino.Output], sinks: collections.abc.Sequence[openvino._pyopenvino.Output], parameters: collections.abc.Sequence[openvino._pyopenvino.op.Parameter], name: str = ‘’) -> None

Create user-defined Model which is a representation of a model

- param results:
list of outputs.

- type results:
list[openvino.Output]

- param sinks:
list of Output sink node handles.

- type sinks:
list[openvino.Output]

- param parameters:
list of parameters.

- type parameters:
list[op.Parameter]

- param name:
String to set as model’s friendly name.

- type name:
str


__init__(self: openvino._pyopenvino.Model, results: collections.abc.Sequence[openvino._pyopenvino.Output], sinks: collections.abc.Sequence[openvino._pyopenvino.Output], parameters: collections.abc.Sequence[openvino._pyopenvino.op.Parameter], variables: collections.abc.Sequence[openvino._pyopenvino.op.util.Variable], name: str = ‘’) -> None

Create user-defined Model which is a representation of a model

- param results:
list of outputs.

- type results:
list[openvino.Output]

- param sinks:
list of Output sink node handles.

- type sinks:
list[openvino.Output]

- param parameters:
list of parameters.

- type parameters:
list[op.Parameter]

- param variables:
list of variables.

- type variables:
list[op.util.Variable]

- param name:
String to set as model’s friendly name.

- type name:
str


__init__(self: openvino._pyopenvino.Model, results: collections.abc.Sequence[openvino._pyopenvino.op.Result], sinks: collections.abc.Sequence[openvino._pyopenvino.Output], parameters: collections.abc.Sequence[openvino._pyopenvino.op.Parameter], name: str = ‘’) -> None

Create user-defined Model which is a representation of a model

- param results:
list of results.

- type results:
list[op.Result]

- param sinks:
list of Output sink node handles.

- type sinks:
list[openvino.Output]

- param parameters:
list of parameters.

- type parameters:
list[op.Parameter]

- param name:
String to set as model’s friendly name.

- type name:
str


__init__(self: openvino._pyopenvino.Model, results: collections.abc.Sequence[openvino._pyopenvino.op.Result], sinks: collections.abc.Sequence[openvino._pyopenvino.Output], parameters: collections.abc.Sequence[openvino._pyopenvino.op.Parameter], variables: collections.abc.Sequence[openvino._pyopenvino.op.util.Variable], name: str = ‘’) -> None

Create user-defined Model which is a representation of a model

- param results:
list of results.

- type results:
list[op.Result]

- param sinks:
list of Output sink node handles.

- type sinks:
list[openvino.Output]

- param parameters:
list of parameters.

- type parameters:
list[op.Parameter]

- param variables:
list of variables.

- type variables:
list[op.util.Variable]

- param name:
String to set as model’s friendly name.

- type name:
str


__init__(self: openvino._pyopenvino.Model, results: collections.abc.Sequence[openvino._pyopenvino.op.Result], sinks: collections.abc.Sequence[openvino._pyopenvino.Node], parameters: collections.abc.Sequence[openvino._pyopenvino.op.Parameter], variables: collections.abc.Sequence[openvino._pyopenvino.op.util.Variable], name: str = ‘’) -> None

Create user-defined Model which is a representation of a model

- param results:
list of results.

- type results:
list[op.Result]

- param sinks:
list of Nodes to be used as Sinks (e.g. Assign ops).

- type sinks:
list[openvino.Node]

- param parameters:
list of parameters.

- type parameters:
list[op.Parameter]

- param variables:
list of variables.

- type variables:
list[op.util.Variable]

- param name:
String to set as model’s friendly name.

- type name:
str


__init__(self: openvino._pyopenvino.Model, results: collections.abc.Sequence[openvino._pyopenvino.Output], sinks: collections.abc.Sequence[openvino._pyopenvino.Node], parameters: collections.abc.Sequence[openvino._pyopenvino.op.Parameter], variables: collections.abc.Sequence[openvino._pyopenvino.op.util.Variable], name: str = ‘’) -> None

Create user-defined Model which is a representation of a model

- param results:
list of results.

- type results:
list[openvino.Output]

- param sinks:
list of Nodes to be used as Sinks (e.g. Assign ops).

- type sinks:
list[openvino.Node]

- param variables:
list of variables.

- type variables:
list[op.util.Variable]

- param name:
String to set as model’s friendly name.

- type name:
str


__init__(self: openvino._pyopenvino.Model, results: collections.abc.Sequence[openvino._pyopenvino.op.Result], parameters: collections.abc.Sequence[openvino._pyopenvino.op.Parameter], variables: collections.abc.Sequence[openvino._pyopenvino.op.util.Variable], name: str = ‘’) -> None

Create user-defined Model which is a representation of a model

- param results:
list of results.

- type results:
list[op.Result]

- param parameters:
list of parameters.

- type parameters:
list[op.Parameter]

- param variables:
list of variables.

- type variables:
list[op.util.Variable]

- param name:
String to set as model’s friendly name.

- type name:
str


__init__(self: openvino._pyopenvino.Model, results: collections.abc.Sequence[openvino._pyopenvino.Output], parameters: collections.abc.Sequence[openvino._pyopenvino.op.Parameter], variables: collections.abc.Sequence[openvino._pyopenvino.op.util.Variable], name: str = ‘’) -> None

Create user-defined Model which is a representation of a model

- param results:
list of results.

- type results:
list[openvino.Output]

- param parameters:
list of parameters.

- type parameters:
list[op.Parameter]

- param name:
String to set as model’s friendly name.

- type name:
str




Methods

()`__copy__`

(memo)`__deepcopy__`

Returns a deepcopy of Model.

(name, /)`__delattr__`

Implement delattr(self, name).

()`__dir__`

Default dir() implementation.

(value, /)`__eq__`

Return self==value.

(exc_type, exc_value, traceback)`__exit__`

(format_spec, /)`__format__`

Default object formatter.

(value, /)`__ge__`

Return self>=value.

(name)`__getattr__`

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

()`__repr__`

Return repr(self).

(name, value, /)`__setattr__`

Implement setattr(self, name, value).

Size of object in memory, in bytes.

()`__str__`

Return str(self).

Abstract classes can override this to customize issubclass().

(self)`_get_raw_address`

Returns a raw address of the Model object from C++.

(self, outputs)`add_outputs`

(self, parameters)`add_parameters`

Add new Parameter nodes to the list.

(self, results)`add_results`

Add new Result nodes to the list.

(self, sinks)`add_sinks`

Add new sink nodes to the list.

(self, variables)`add_variables`

Add new variables to the list.

()`clone`

(output_tensors, input_tensors[, ...])`evaluate`

(self)`get_friendly_name`

Gets the friendly name for a model.

(self)`get_name`

Get the unique name of the model.

(self)`get_ops`

Return ops used in the model.

(self)`get_ordered_ops`

Return ops used in the model in topological order.

(self, index)`get_output_element_type`

Return the element type of output i

(self, index)`get_output_op`

Return the op that generates output i

(self, index)`get_output_partial_shape`

Return the partial shape of element i

(self, index)`get_output_shape`

Return the shape of element i

(self)`get_output_size`

Return the number of outputs for the model.

(self, parameter)`get_parameter_index`

Return the index position of parameter

(self)`get_parameters`

Return the model parameters.

(self)`get_result`

Return single result.

(*args, **kwargs)`get_result_index`

Overloaded function.

(self)`get_results`

Return a list of model outputs.

(*args, **kwargs)`get_rt_info`

Overloaded function.

(*args, **kwargs)`get_sink_index`

Overloaded function.

(self)`get_sinks`

Return a list of model's sinks.

(self, arg0)`get_variable_by_id`

Return a variable by specified variable_id.

(self)`get_variables`

Return a list of model's variables.

(*args, **kwargs)`has_rt_info`

Overloaded function.

(*args, **kwargs)`input`

Overloaded function.

(self)`is_dynamic`

Returns true if any of the op's defined in the model contains partial shape.

(*args, **kwargs)`output`

Overloaded function.

(self, parameter)`remove_parameter`

Delete Parameter node from the list of parameters.

(self, result)`remove_result`

Delete Result node from the list of results.

(self, sink)`remove_sink`

Delete sink node from the list of sinks.

(self, variable)`remove_variable`

Delete variable from the list of variables.

(self, parameter_index, ...)`replace_parameter`

Replace the parameter_index parameter of the model with parameter

(*args, **kwargs)`reshape`

Overloaded function.

(self, name)`set_friendly_name`

Sets a friendly name for a model.

(*args, **kwargs)`set_rt_info`

Overloaded function.

Attributes

`__pybind11_module_local_v11_system_libstdcpp_gxx_abi_1xxx_use_cxx11_abi_0__`

Returns true if any of the op's defined in the model contains partial shape.

Return the model parameters.

Return single result.

Return a list of model outputs.

Return a list of model's sinks.

Return a list of model's variables.

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.Model.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.Model.__class__) alias of

`ModelMeta`


-
__deepcopy__(
*memo: dict*)[Model](https://docs.openvino.ai#openvino.Model)[#](https://docs.openvino.ai#openvino.Model.__deepcopy__) Returns a deepcopy of Model.

- Returns:
A copy of Model.

- Return type:


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.Model.__delattr__) Implement delattr(self, name).


-
__dir__() list
[#](https://docs.openvino.ai#openvino.Model.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Model.__eq__) Return self==value.


-
__exit__(
*exc_type: type[BaseException]*,*exc_value: BaseException*,*traceback: TracebackType*) None[#](https://docs.openvino.ai#openvino.Model.__exit__)

-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.Model.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Model.__ge__) Return self>=value.


-
__getattr__(
*name: str*) Any[#](https://docs.openvino.ai#openvino.Model.__getattr__)

-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.Model.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino.Model.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Model.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino.Model.__hash__) Return hash(self).


-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0) Overloaded function.

__init__(self: openvino._pyopenvino.Model, other: openvino._pyopenvino.Model) -> None

__init__(self: openvino._pyopenvino.Model, results: collections.abc.Sequence[openvino._pyopenvino.op.Result], sinks: collections.abc.Sequence[openvino._pyopenvino.Node], parameters: collections.abc.Sequence[openvino._pyopenvino.op.Parameter], name: str = ‘’) -> None

Create user-defined Model which is a representation of a model.

- param results:
list of results.

- type results:
list[op.Result]

- param sinks:
list of Nodes to be used as Sinks (e.g. Assign ops).

- type sinks:
list[openvino.Node]

- param parameters:
list of parameters.

- type parameters:
list[op.Parameter]

- param name:
String to set as model’s friendly name.

- type name:
str


__init__(self: openvino._pyopenvino.Model, results: collections.abc.Sequence[openvino._pyopenvino.op.Result], parameters: collections.abc.Sequence[openvino._pyopenvino.op.Parameter], name: str = ‘’) -> None

Create user-defined Model which is a representation of a model.

- param results:
list of results.

- type results:
list[op.Result]

- param parameters:
list of parameters.

- type parameters:
list[op.Parameter]

- param name:
String to set as model’s friendly name.

- type name:
str


__init__(self: openvino._pyopenvino.Model, results: collections.abc.Sequence[openvino._pyopenvino.Node], parameters: collections.abc.Sequence[openvino._pyopenvino.op.Parameter], name: str = ‘’) -> None

Create user-defined Model which is a representation of a model.

- param results:
list of Nodes to be used as results.

- type results:
list[openvino.Node]

- param parameters:
list of parameters.

- type parameters:
list[op.Parameter]

- param name:
String to set as model’s friendly name.

- type name:
str


__init__(self: openvino._pyopenvino.Model, result: openvino._pyopenvino.Node, parameters: collections.abc.Sequence[openvino._pyopenvino.op.Parameter], name: str = ‘’) -> None

Create user-defined Model which is a representation of a model.

- param result:
Node to be used as result.

- type result:
openvino.Node

- param parameters:
list of parameters.

- type parameters:
list[op.Parameter]

- param name:
String to set as model’s friendly name.

- type name:
str


__init__(self: openvino._pyopenvino.Model, results: collections.abc.Sequence[openvino._pyopenvino.Output], parameters: collections.abc.Sequence[openvino._pyopenvino.op.Parameter], name: str = ‘’) -> None

Create user-defined Model which is a representation of a model

- param results:
list of outputs.

- type results:
list[openvino.Output]

- param parameters:
list of parameters.

- type parameters:
list[op.Parameter]

- param name:
String to set as model’s friendly name.

- type name:
str


__init__(self: openvino._pyopenvino.Model, results: collections.abc.Sequence[openvino._pyopenvino.Output], sinks: collections.abc.Sequence[openvino._pyopenvino.Node], parameters: collections.abc.Sequence[openvino._pyopenvino.op.Parameter], name: str = ‘’) -> None

Create user-defined Model which is a representation of a model

- param results:
list of outputs.

- type results:
list[openvino.Output]

- param sinks:
list of Nodes to be used as Sinks (e.g. Assign ops).

- type sinks:
list[openvino.Node]

- param parameters:
list of parameters.

- type parameters:
list[op.Parameter]

- param name:
String to set as model’s friendly name.

- type name:
str


__init__(self: openvino._pyopenvino.Model, results: collections.abc.Sequence[openvino._pyopenvino.Output], sinks: collections.abc.Sequence[openvino._pyopenvino.Output], parameters: collections.abc.Sequence[openvino._pyopenvino.op.Parameter], name: str = ‘’) -> None

Create user-defined Model which is a representation of a model

- param results:
list of outputs.

- type results:
list[openvino.Output]

- param sinks:
list of Output sink node handles.

- type sinks:
list[openvino.Output]

- param parameters:
list of parameters.

- type parameters:
list[op.Parameter]

- param name:
String to set as model’s friendly name.

- type name:
str


__init__(self: openvino._pyopenvino.Model, results: collections.abc.Sequence[openvino._pyopenvino.Output], sinks: collections.abc.Sequence[openvino._pyopenvino.Output], parameters: collections.abc.Sequence[openvino._pyopenvino.op.Parameter], variables: collections.abc.Sequence[openvino._pyopenvino.op.util.Variable], name: str = ‘’) -> None

Create user-defined Model which is a representation of a model

- param results:
list of outputs.

- type results:
list[openvino.Output]

- param sinks:
list of Output sink node handles.

- type sinks:
list[openvino.Output]

- param parameters:
list of parameters.

- type parameters:
list[op.Parameter]

- param variables:
list of variables.

- type variables:
list[op.util.Variable]

- param name:
String to set as model’s friendly name.

- type name:
str


__init__(self: openvino._pyopenvino.Model, results: collections.abc.Sequence[openvino._pyopenvino.op.Result], sinks: collections.abc.Sequence[openvino._pyopenvino.Output], parameters: collections.abc.Sequence[openvino._pyopenvino.op.Parameter], name: str = ‘’) -> None

Create user-defined Model which is a representation of a model

- param results:
list of results.

- type results:
list[op.Result]

- param sinks:
list of Output sink node handles.

- type sinks:
list[openvino.Output]

- param parameters:
list of parameters.

- type parameters:
list[op.Parameter]

- param name:
String to set as model’s friendly name.

- type name:
str


__init__(self: openvino._pyopenvino.Model, results: collections.abc.Sequence[openvino._pyopenvino.op.Result], sinks: collections.abc.Sequence[openvino._pyopenvino.Output], parameters: collections.abc.Sequence[openvino._pyopenvino.op.Parameter], variables: collections.abc.Sequence[openvino._pyopenvino.op.util.Variable], name: str = ‘’) -> None

Create user-defined Model which is a representation of a model

- param results:
list of results.

- type results:
list[op.Result]

- param sinks:
list of Output sink node handles.

- type sinks:
list[openvino.Output]

- param parameters:
list of parameters.

- type parameters:
list[op.Parameter]

- param variables:
list of variables.

- type variables:
list[op.util.Variable]

- param name:
String to set as model’s friendly name.

- type name:
str


__init__(self: openvino._pyopenvino.Model, results: collections.abc.Sequence[openvino._pyopenvino.op.Result], sinks: collections.abc.Sequence[openvino._pyopenvino.Node], parameters: collections.abc.Sequence[openvino._pyopenvino.op.Parameter], variables: collections.abc.Sequence[openvino._pyopenvino.op.util.Variable], name: str = ‘’) -> None

Create user-defined Model which is a representation of a model

- param results:
list of results.

- type results:
list[op.Result]

- param sinks:
list of Nodes to be used as Sinks (e.g. Assign ops).

- type sinks:
list[openvino.Node]

- param parameters:
list of parameters.

- type parameters:
list[op.Parameter]

- param variables:
list of variables.

- type variables:
list[op.util.Variable]

- param name:
String to set as model’s friendly name.

- type name:
str


__init__(self: openvino._pyopenvino.Model, results: collections.abc.Sequence[openvino._pyopenvino.Output], sinks: collections.abc.Sequence[openvino._pyopenvino.Node], parameters: collections.abc.Sequence[openvino._pyopenvino.op.Parameter], variables: collections.abc.Sequence[openvino._pyopenvino.op.util.Variable], name: str = ‘’) -> None

Create user-defined Model which is a representation of a model

- param results:
list of results.

- type results:
list[openvino.Output]

- param sinks:
list of Nodes to be used as Sinks (e.g. Assign ops).

- type sinks:
list[openvino.Node]

- param variables:
list of variables.

- type variables:
list[op.util.Variable]

- param name:
String to set as model’s friendly name.

- type name:
str


__init__(self: openvino._pyopenvino.Model, results: collections.abc.Sequence[openvino._pyopenvino.op.Result], parameters: collections.abc.Sequence[openvino._pyopenvino.op.Parameter], variables: collections.abc.Sequence[openvino._pyopenvino.op.util.Variable], name: str = ‘’) -> None

Create user-defined Model which is a representation of a model

- param results:
list of results.

- type results:
list[op.Result]

- param parameters:
list of parameters.

- type parameters:
list[op.Parameter]

- param variables:
list of variables.

- type variables:
list[op.util.Variable]

- param name:
String to set as model’s friendly name.

- type name:
str


__init__(self: openvino._pyopenvino.Model, results: collections.abc.Sequence[openvino._pyopenvino.Output], parameters: collections.abc.Sequence[openvino._pyopenvino.op.Parameter], variables: collections.abc.Sequence[openvino._pyopenvino.op.util.Variable], name: str = ‘’) -> None

Create user-defined Model which is a representation of a model

- param results:
list of results.

- type results:
list[openvino.Output]

- param parameters:
list of parameters.

- type parameters:
list[op.Parameter]

- param name:
String to set as model’s friendly name.

- type name:
str




-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.Model.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Model.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Model.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Model.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.Model.__new__)

-
__pybind11_module_local_v11_system_libstdcpp_gxx_abi_1xxx_use_cxx11_abi_0__
*= <capsule object NULL>*[#](https://docs.openvino.ai#openvino.Model.__pybind11_module_local_v11_system_libstdcpp_gxx_abi_1xxx_use_cxx11_abi_0__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.Model.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.Model.__reduce_ex__) Helper for pickle.


-
__repr__() str
[#](https://docs.openvino.ai#openvino.Model.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.Model.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino.Model.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino.Model.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.Model.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_get_raw_address(
*self: openvino._pyopenvino.Model*) int[#](https://docs.openvino.ai#openvino.Model._get_raw_address) Returns a raw address of the Model object from C++.

Use this function in order to compare underlying C++ addresses instead of using __eq__ in Python.

- Returns:
a raw address of the Model object.

- Return type:
int



-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.Model._pybind11_conduit_v1_)

-
add_outputs(
*self: openvino._pyopenvino.Model*,*outputs: object*) list[[openvino._pyopenvino.Output](https://docs.openvino.ai/openvino.Output.html#openvino.Output)][#](https://docs.openvino.ai#openvino.Model.add_outputs)

-
add_parameters(
*self: openvino._pyopenvino.Model*,*parameters: collections.abc.Sequence[*) None[openvino._pyopenvino.op.Parameter](https://docs.openvino.ai/openvino.runtime.op.Parameter.html#openvino.runtime.op.Parameter)][#](https://docs.openvino.ai#openvino.Model.add_parameters) Add new Parameter nodes to the list.

Method doesn’t change or validate graph, it should be done manually. For example, if you want to replace ReadValue node by Parameter, you should do the following steps: * replace node ReadValue by Parameter in graph * call add_parameter() to add new input to the list * call graph validation to check correctness of changes

- Parameters:
**parameter**(*list**[**op.Parameter**]*) – new Parameter nodes.


-
add_results(
*self: openvino._pyopenvino.Model*,*results: collections.abc.Sequence[*) None[openvino._pyopenvino.op.Result](https://docs.openvino.ai/openvino.runtime.op.Result.html#openvino.runtime.op.Result)][#](https://docs.openvino.ai#openvino.Model.add_results) Add new Result nodes to the list.

Method doesn’t validate graph, it should be done manually after all changes.

- Parameters:
**results**(*list**[**op.Result**]*) – new Result nodes.


-
add_sinks(
*self: openvino._pyopenvino.Model*,*sinks: list*) None[#](https://docs.openvino.ai#openvino.Model.add_sinks) Add new sink nodes to the list.

Method doesn’t validate graph, it should be done manually after all changes.

- Parameters:
**sinks**(*list**[**openvino.Node**]*) – new sink nodes.


-
add_variables(
*self: openvino._pyopenvino.Model*,*variables: collections.abc.Sequence[*) None[openvino._pyopenvino.op.util.Variable](https://docs.openvino.ai/openvino.runtime.op.util.Variable.html#openvino.runtime.op.util.Variable)][#](https://docs.openvino.ai#openvino.Model.add_variables) Add new variables to the list.

Method doesn’t validate graph, it should be done manually after all changes.

- Parameters:
**variables**(*list**[**op.util.Variable**]*) – new variables to add.


-
*property*dynamic[#](https://docs.openvino.ai#openvino.Model.dynamic) Returns true if any of the op’s defined in the model contains partial shape.

- Return type:
bool



-
evaluate(
*output_tensors: list[*,[Tensor](https://docs.openvino.ai/openvino.Tensor.html#openvino.Tensor)] |[TensorVector](https://docs.openvino.ai/openvino.TensorVector.html#openvino.TensorVector)*input_tensors: list[*,[Tensor](https://docs.openvino.ai/openvino.Tensor.html#openvino.Tensor)] |[TensorVector](https://docs.openvino.ai/openvino.TensorVector.html#openvino.TensorVector)*evaluation_context:*) bool[RTMap](https://docs.openvino.ai/openvino.RTMap.html#openvino.RTMap)| None = None[#](https://docs.openvino.ai#openvino.Model.evaluate)

-
*property*friendly_name[#](https://docs.openvino.ai#openvino.Model.friendly_name)

-
get_friendly_name(
*self: openvino._pyopenvino.Model*) str[#](https://docs.openvino.ai#openvino.Model.get_friendly_name) Gets the friendly name for a model. If no friendly name has been set via set_friendly_name then the model’s unique name is returned.

- Returns:
String with a friendly name of the model.

- Return type:
str



-
get_name(
*self: openvino._pyopenvino.Model*) str[#](https://docs.openvino.ai#openvino.Model.get_name) Get the unique name of the model.

- Returns:
String with a name of the model.

- Return type:
str



-
get_ops(
*self: openvino._pyopenvino.Model*) list[[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)][#](https://docs.openvino.ai#openvino.Model.get_ops) Return ops used in the model.

- Returns:
list of Nodes representing ops used in model.

- Return type:
list[

[openvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)]


-
get_ordered_ops(
*self: openvino._pyopenvino.Model*) list[[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)][#](https://docs.openvino.ai#openvino.Model.get_ordered_ops) Return ops used in the model in topological order.

- Returns:
list of sorted Nodes representing ops used in model.

- Return type:
list[

[openvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)]


-
get_output_element_type(
*self: openvino._pyopenvino.Model*,*index: SupportsInt*)[openvino._pyopenvino.Type](https://docs.openvino.ai/openvino.Type.html#openvino.Type)[#](https://docs.openvino.ai#openvino.Model.get_output_element_type) Return the element type of output i

- Parameters:
**index**(*int*) – output index- Returns:
Type object of output i

- Return type:


-
get_output_op(
*self: openvino._pyopenvino.Model*,*index: SupportsInt*)[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.Model.get_output_op) Return the op that generates output i

- Parameters:
**index**(*output index*) – output index- Returns:
Node object that generates output i

- Return type:


-
get_output_partial_shape(
*self: openvino._pyopenvino.Model*,*index: SupportsInt*)[openvino._pyopenvino.PartialShape](https://docs.openvino.ai/openvino.PartialShape.html#openvino.PartialShape)[#](https://docs.openvino.ai#openvino.Model.get_output_partial_shape) Return the partial shape of element i

- Parameters:
**index**(*int*) – element index- Returns:
PartialShape object of element i

- Return type:


-
get_output_shape(
*self: openvino._pyopenvino.Model*,*index: SupportsInt*)[openvino._pyopenvino.Shape](https://docs.openvino.ai/openvino.Shape.html#openvino.Shape)[#](https://docs.openvino.ai#openvino.Model.get_output_shape) Return the shape of element i

- Parameters:
**index**(*int*) – element index- Returns:
Shape object of element i

- Return type:


-
get_output_size(
*self: openvino._pyopenvino.Model*) int[#](https://docs.openvino.ai#openvino.Model.get_output_size) Return the number of outputs for the model.

- Returns:
Number of outputs.

- Return type:
int



-
get_parameter_index(
*self: openvino._pyopenvino.Model*,*parameter:*) int[openvino._pyopenvino.op.Parameter](https://docs.openvino.ai/openvino.runtime.op.Parameter.html#openvino.runtime.op.Parameter)[#](https://docs.openvino.ai#openvino.Model.get_parameter_index) Return the index position of parameter

Return -1 if parameter not matched.

- Parameters:
**parameter**() – Parameter, which index is to be found.*op.Parameter*- Returns:
Index for parameter

- Return type:
int



-
get_parameters(
*self: openvino._pyopenvino.Model*) list[[openvino._pyopenvino.op.Parameter](https://docs.openvino.ai/openvino.runtime.op.Parameter.html#openvino.runtime.op.Parameter)][#](https://docs.openvino.ai#openvino.Model.get_parameters) Return the model parameters.

- Returns:
a list of model’s parameters.

- Return type:
list[

[op.Parameter](https://docs.openvino.ai/openvino.runtime.op.Parameter.html#openvino.runtime.op.Parameter)]


-
get_result(
*self: openvino._pyopenvino.Model*)[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.Model.get_result) Return single result.

- Returns:
Node object representing result.

- Return type:


-
get_result_index(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.Model.get_result_index) Overloaded function.

get_result_index(self: openvino._pyopenvino.Model, value: openvino._pyopenvino.Output) -> int

Return index of result.

Return -1 if value not matched.

- param value:
Output containing Node

- type value:
openvino.Output

- return:
Index for value referencing it.

- rtype:
int


get_result_index(self: openvino._pyopenvino.Model, value: openvino._pyopenvino.ConstOutput) -> int

Return index of result.

Return -1 if value not matched.

- param value:
Output containing Node

- type value:
openvino.Output

- return:
Index for value referencing it.

- rtype:
int


get_result_index(self: openvino._pyopenvino.Model, result: openvino._pyopenvino.op.Result) -> int

Return index of result.

Return -1 if result not matched.

- param result:
Result operation

- type result:
op.Result

- return:
Index for result referencing it.

- rtype:
int




-
get_results(
*self: openvino._pyopenvino.Model*) list[[openvino._pyopenvino.op.Result](https://docs.openvino.ai/openvino.runtime.op.Result.html#openvino.runtime.op.Result)][#](https://docs.openvino.ai#openvino.Model.get_results) Return a list of model outputs.

- Returns:
a list of model’s result nodes.

- Return type:
list[

[op.Result](https://docs.openvino.ai/openvino.runtime.op.Result.html#openvino.runtime.op.Result)]


-
get_rt_info(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.Model.get_rt_info) Overloaded function.

get_rt_info(self: openvino._pyopenvino.Model) -> openvino._pyopenvino.RTMap

Returns PyRTMap which is a dictionary of user defined runtime info.

- return:
A dictionary of user defined data.

- rtype:
openvino.RTMap


get_rt_info(self: openvino._pyopenvino.Model, path: list) -> object

Returns runtime attribute as a OVAny object.

- param path:
list of strings which defines a path to runtime info.

- type path:
list[str]

- return:
A runtime attribute.

- rtype:
openvino.OVAny


get_rt_info(self: openvino._pyopenvino.Model, path: str) -> object

Returns runtime attribute as a OVAny object.

- param path:
list of strings which defines a path to runtime info.

- type path:
str

- return:
A runtime attribute.

- rtype:
openvino.OVAny




-
get_sink_index(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.Model.get_sink_index) Overloaded function.

get_sink_index(self: openvino._pyopenvino.Model, value: openvino._pyopenvino.Output) -> int

Return index of sink.

Return -1 if value not matched.

- param value:
Output sink node handle

- type value:
openvino.Output

- return:
Index of sink node referenced by output handle.

- rtype:
int


get_sink_index(self: openvino._pyopenvino.Model, value: openvino._pyopenvino.ConstOutput) -> int

Return index of sink.

Return -1 if value not matched.

- param value:
Output sink node handle

- type value:
openvino.Output

- return:
Index of sink node referenced by output handle.

- rtype:
int


get_sink_index(self: openvino._pyopenvino.Model, sink: object) -> int

Return index of sink node.

Return -1 if sink not matched.

- param sink:
Sink node.

- type sink:
openvino.Node

- return:
Index of sink node.

- rtype:
int




-
get_sinks(
*self: openvino._pyopenvino.Model*) list[[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)][#](https://docs.openvino.ai#openvino.Model.get_sinks) Return a list of model’s sinks.

- Returns:
a list of model’s sinks.

- Return type:
list[

[openvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)]


-
get_variable_by_id(
*self: openvino._pyopenvino.Model*,*arg0: str*)[openvino._pyopenvino.op.util.Variable](https://docs.openvino.ai/openvino.runtime.op.util.Variable.html#openvino.runtime.op.util.Variable)[#](https://docs.openvino.ai#openvino.Model.get_variable_by_id) Return a variable by specified variable_id.

- Parameters:
**variable_id**(*str*) – a variable id to get variable node.- Returns:
a variable node.

- Return type:


-
get_variables(
*self: openvino._pyopenvino.Model*) list[[openvino._pyopenvino.op.util.Variable](https://docs.openvino.ai/openvino.runtime.op.util.Variable.html#openvino.runtime.op.util.Variable)][#](https://docs.openvino.ai#openvino.Model.get_variables) Return a list of model’s variables.

- Returns:
a list of model’s variables.

- Return type:
list[

[op.util.Variable](https://docs.openvino.ai/openvino.runtime.op.util.Variable.html#openvino.runtime.op.util.Variable)]


-
has_rt_info(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.Model.has_rt_info) Overloaded function.

has_rt_info(self: openvino._pyopenvino.Model, path: list) -> bool

Checks if given path exists in runtime info of the model.

- param path:
list of strings which defines a path to runtime info.

- type path:
list[str]

- return:
True if path exists, otherwise False.

- rtype:
bool


has_rt_info(self: openvino._pyopenvino.Model, path: str) -> bool

Checks if given path exists in runtime info of the model.

- param path:
list of strings which defines a path to runtime info.

- type path:
str

- return:
True if path exists, otherwise False.

- rtype:
bool




-
input(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.Model.input) Overloaded function.

input(self: openvino._pyopenvino.Model) -> openvino._pyopenvino.Output

input(self: openvino._pyopenvino.Model, index: typing.SupportsInt) -> openvino._pyopenvino.Output

input(self: openvino._pyopenvino.Model, tensor_name: str) -> openvino._pyopenvino.Output

input(self: openvino._pyopenvino.Model) -> openvino._pyopenvino.ConstOutput

input(self: openvino._pyopenvino.Model, index: typing.SupportsInt) -> openvino._pyopenvino.ConstOutput

input(self: openvino._pyopenvino.Model, tensor_name: str) -> openvino._pyopenvino.ConstOutput



-
*property*inputs[#](https://docs.openvino.ai#openvino.Model.inputs)

-
is_dynamic(
*self: openvino._pyopenvino.Model*) bool[#](https://docs.openvino.ai#openvino.Model.is_dynamic) Returns true if any of the op’s defined in the model contains partial shape.

- Return type:
bool



-
*property*name[#](https://docs.openvino.ai#openvino.Model.name)

-
output(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.Model.output) Overloaded function.

output(self: openvino._pyopenvino.Model) -> openvino._pyopenvino.Output

output(self: openvino._pyopenvino.Model, index: typing.SupportsInt) -> openvino._pyopenvino.Output

output(self: openvino._pyopenvino.Model, tensor_name: str) -> openvino._pyopenvino.Output

output(self: openvino._pyopenvino.Model) -> openvino._pyopenvino.ConstOutput

output(self: openvino._pyopenvino.Model, index: typing.SupportsInt) -> openvino._pyopenvino.ConstOutput

output(self: openvino._pyopenvino.Model, tensor_name: str) -> openvino._pyopenvino.ConstOutput



-
*property*outputs[#](https://docs.openvino.ai#openvino.Model.outputs)

-
*property*parameters[#](https://docs.openvino.ai#openvino.Model.parameters) Return the model parameters.

- Returns:
a list of model’s parameters.

- Return type:
list[

[op.Parameter](https://docs.openvino.ai/openvino.runtime.op.Parameter.html#openvino.runtime.op.Parameter)]


-
remove_parameter(
*self: openvino._pyopenvino.Model*,*parameter:*) None[openvino._pyopenvino.op.Parameter](https://docs.openvino.ai/openvino.runtime.op.Parameter.html#openvino.runtime.op.Parameter)[#](https://docs.openvino.ai#openvino.Model.remove_parameter) Delete Parameter node from the list of parameters. Method will not delete node from graph. You need to replace Parameter with other operation manually.

Attention: Indexing of parameters can be changed.

Possible use of method is to replace input by variable. For it the following steps should be done: * Parameter node should be replaced by ReadValue * call remove_parameter(param) to remove input from the list * check if any parameter indexes are saved/used somewhere, update it for all inputs because indexes can be changed * call graph validation to check all changes

- Parameters:
**parameter**() – Parameter node to delete.*op.Parameter*


-
remove_result(
*self: openvino._pyopenvino.Model*,*result:*) None[openvino._pyopenvino.op.Result](https://docs.openvino.ai/openvino.runtime.op.Result.html#openvino.runtime.op.Result)[#](https://docs.openvino.ai#openvino.Model.remove_result) Delete Result node from the list of results. Method will not delete node from graph.

- Parameters:
**result**() – Result node to delete.*op.Result*


-
remove_sink(
*self: openvino._pyopenvino.Model*,*sink: object*) None[#](https://docs.openvino.ai#openvino.Model.remove_sink) Delete sink node from the list of sinks. Method doesn’t delete node from graph.

- Parameters:
**sink**() – Sink to delete.*openvino.Node*


-
remove_variable(
*self: openvino._pyopenvino.Model*,*variable:*) None[openvino._pyopenvino.op.util.Variable](https://docs.openvino.ai/openvino.runtime.op.util.Variable.html#openvino.runtime.op.util.Variable)[#](https://docs.openvino.ai#openvino.Model.remove_variable) Delete variable from the list of variables. Method doesn’t delete nodes that used this variable from the graph.

- Parameters:
**variable**() – Variable to delete.*op.util.Variable*


-
replace_parameter(
*self: openvino._pyopenvino.Model*,*parameter_index: SupportsInt*,*parameter:*) None[openvino._pyopenvino.op.Parameter](https://docs.openvino.ai/openvino.runtime.op.Parameter.html#openvino.runtime.op.Parameter)[#](https://docs.openvino.ai#openvino.Model.replace_parameter) Replace the parameter_index parameter of the model with parameter

All users of the parameter_index parameter are redirected to parameter , and the parameter_index entry in the model parameter list is replaced with parameter

- Parameters:
**parameter_index**(*int*) – The index of the parameter to replace.**parameter**() – The parameter to substitute for the parameter_index parameter.*op.Parameter*



-
reshape(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.Model.reshape) Overloaded function.

reshape(self: openvino._pyopenvino.Model, partial_shape: openvino._pyopenvino.PartialShape, variables_shapes: dict = {}) -> None

Reshape model input.

The allowed types of keys in the variables_shapes dictionary is str. The allowed types of values in the variables_shapes are:

openvino.PartialShape

list consisting of dimensions

tuple consisting of dimensions

str, string representation of openvino.PartialShape


When list or tuple are used to describe dimensions, each dimension can be written in form:

non-negative int which means static value for the dimension


(2) [min, max], dynamic dimension where min specifies lower bound and max specifies upper bound; the range includes both min and max; using -1 for min or max means no known bound (3) (min, max), the same as above (4) -1 is a dynamic dimension without known bounds (4) openvino.Dimension (5) str using next syntax:

‘?’ - to define fully dynamic dimension ‘1’ - to define dimension which length is 1 ‘1..10’ - to define bounded dimension ‘..10’ or ‘1..’ to define dimension with only lower or only upper limit

GIL is released while running this function.

- param partial_shape:
New shape.

- type partial_shape:
openvino.PartialShape

- param variables_shapes:
New shapes for variables

- type variables_shapes:
dict[keys, values]


:return : void

reshape(self: openvino._pyopenvino.Model, partial_shape: list, variables_shapes: dict = {}) -> None

Reshape model input.

The allowed types of keys in the variables_shapes dictionary is str. The allowed types of values in the variables_shapes are:

openvino.PartialShape

list consisting of dimensions

tuple consisting of dimensions

str, string representation of openvino.PartialShape


When list or tuple are used to describe dimensions, each dimension can be written in form:

non-negative int which means static value for the dimension


(2) [min, max], dynamic dimension where min specifies lower bound and max specifies upper bound; the range includes both min and max; using -1 for min or max means no known bound (3) (min, max), the same as above (4) -1 is a dynamic dimension without known bounds (4) openvino.Dimension (5) str using next syntax:

‘?’ - to define fully dynamic dimension ‘1’ - to define dimension which length is 1 ‘1..10’ - to define bounded dimension ‘..10’ or ‘1..’ to define dimension with only lower or only upper limit

GIL is released while running this function.

- param partial_shape:
New shape.

- type partial_shape:
list

- param variables_shapes:
New shapes for variables

- type variables_shapes:
dict[keys, values]


:return : void

reshape(self: openvino._pyopenvino.Model, partial_shape: tuple, variables_shapes: dict = {}) -> None

Reshape model input.

The allowed types of keys in the variables_shapes dictionary is str. The allowed types of values in the variables_shapes are:

openvino.PartialShape

list consisting of dimensions

tuple consisting of dimensions

str, string representation of openvino.PartialShape


When list or tuple are used to describe dimensions, each dimension can be written in form:

non-negative int which means static value for the dimension


(2) [min, max], dynamic dimension where min specifies lower bound and max specifies upper bound; the range includes both min and max; using -1 for min or max means no known bound (3) (min, max), the same as above (4) -1 is a dynamic dimension without known bounds (4) openvino.Dimension (5) str using next syntax:

‘?’ - to define fully dynamic dimension ‘1’ - to define dimension which length is 1 ‘1..10’ - to define bounded dimension ‘..10’ or ‘1..’ to define dimension with only lower or only upper limit

GIL is released while running this function.

- param partial_shape:
New shape.

- type partial_shape:
tuple

- param variables_shapes:
New shapes for variables

- type variables_shapes:
dict[keys, values]


:return : void

reshape(self: openvino._pyopenvino.Model, partial_shape: str, variables_shapes: dict = {}) -> None

Reshape model input.

The allowed types of keys in the variables_shapes dictionary is str. The allowed types of values in the variables_shapes are:

openvino.PartialShape

list consisting of dimensions

tuple consisting of dimensions

str, string representation of openvino.PartialShape


When list or tuple are used to describe dimensions, each dimension can be written in form:

non-negative int which means static value for the dimension


(2) [min, max], dynamic dimension where min specifies lower bound and max specifies upper bound; the range includes both min and max; using -1 for min or max means no known bound (3) (min, max), the same as above (4) -1 is a dynamic dimension without known bounds (4) openvino.Dimension (5) str using next syntax:

‘?’ - to define fully dynamic dimension ‘1’ - to define dimension which length is 1 ‘1..10’ - to define bounded dimension ‘..10’ or ‘1..’ to define dimension with only lower or only upper limit

GIL is released while running this function.

- param partial_shape:
New shape.

- type partial_shape:
str

- param variables_shapes:
New shapes for variables

- type variables_shapes:
dict[keys, values]


:return : void

reshape(self: openvino._pyopenvino.Model, partial_shapes: dict, variables_shapes: dict = {}) -> None


Reshape model inputs.

The allowed types of keys in the partial_shapes dictionary are:

int, input index

str, input tensor name

openvino.Output


The allowed types of values in the partial_shapes are:

openvino.PartialShape

list consisting of dimensions

tuple consisting of dimensions

str, string representation of openvino.PartialShape


When list or tuple are used to describe dimensions, each dimension can be written in form:

non-negative int which means static value for the dimension

[min, max], dynamic dimension where min specifies lower bound and max specifies upper bound; the range includes both min and max; using -1 for min or max means no known bound

(min, max), the same as above


(4) -1 is a dynamic dimension without known bounds (4) openvino.Dimension (5) str using next syntax:

‘?’ - to define fully dynamic dimension ‘1’ - to define dimension which length is 1 ‘1..10’ - to define bounded dimension ‘..10’ or ‘1..’ to define dimension with only lower or only upper limit

The allowed types of keys in the variables_shapes dictionary is str. The allowed types of values in the variables_shapes are:

openvino.PartialShape

list consisting of dimensions

tuple consisting of dimensions

str, string representation of openvino.PartialShape


When list or tuple are used to describe dimensions, each dimension can be written in form:

non-negative int which means static value for the dimension


(2) [min, max], dynamic dimension where min specifies lower bound and max specifies upper bound; the range includes both min and max; using -1 for min or max means no known bound (3) (min, max), the same as above (4) -1 is a dynamic dimension without known bounds (4) openvino.Dimension (5) str using next syntax:

‘?’ - to define fully dynamic dimension ‘1’ - to define dimension which length is 1 ‘1..10’ - to define bounded dimension ‘..10’ or ‘1..’ to define dimension with only lower or only upper limit

Reshape model inputs.

GIL is released while running this function.

- param partial_shapes:
New shapes.

- type partial_shapes:
dict[keys, values]

- param variables_shapes:
New shapes for variables

- type variables_shapes:
dict[keys, values]



-
*property*result[#](https://docs.openvino.ai#openvino.Model.result) Return single result.

- Returns:
Node object representing result.

- Return type:


-
*property*results[#](https://docs.openvino.ai#openvino.Model.results) Return a list of model outputs.

- Returns:
a list of model’s result nodes.

- Return type:
list[

[op.Result](https://docs.openvino.ai/openvino.runtime.op.Result.html#openvino.runtime.op.Result)]


-
*property*rt_info[#](https://docs.openvino.ai#openvino.Model.rt_info)

-
set_friendly_name(
*self: openvino._pyopenvino.Model*,*name: str*) None[#](https://docs.openvino.ai#openvino.Model.set_friendly_name) Sets a friendly name for a model. This does not overwrite the unique name of the model and is retrieved via get_friendly_name(). Used mainly for debugging.

- Parameters:
**name**(*str*) – String to set as the friendly name.


-
set_rt_info(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.Model.set_rt_info) Overloaded function.

set_rt_info(self: openvino._pyopenvino.Model, obj: object, path: list) -> None

Add value inside runtime info

- param obj:
value for the runtime info

- type obj:
py:object

- param path:
list of strings which defines a path to runtime info.

- type path:
list[str]


set_rt_info(self: openvino._pyopenvino.Model, obj: object, path: str) -> None

Add value inside runtime info

- param obj:
value for the runtime info

- type obj:
Any

- param path:
String which defines a path to runtime info.

- type path:
str




-
*property*sinks[#](https://docs.openvino.ai#openvino.Model.sinks) Return a list of model’s sinks.

- Returns:
a list of model’s sinks.

- Return type:
list[

[openvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)]


-
validate_nodes_and_infer_types(
*self: openvino._pyopenvino.Model*) None[#](https://docs.openvino.ai#openvino.Model.validate_nodes_and_infer_types)

-
*property*variables[#](https://docs.openvino.ai#openvino.Model.variables) Return a list of model’s variables.

- Returns:
a list of model’s variables.

- Return type:
list[

[op.util.Variable](https://docs.openvino.ai/openvino.runtime.op.util.Variable.html#openvino.runtime.op.util.Variable)]


-
__init__(