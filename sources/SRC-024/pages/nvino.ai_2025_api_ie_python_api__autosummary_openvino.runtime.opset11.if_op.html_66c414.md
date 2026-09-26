source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.if_op.html
lastmod: 

# openvino.runtime.opset11.if_op[#](https://docs.openvino.ai#openvino-runtime-opset11-if-op)

-
*class*openvino.runtime.opset11.if_op[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op) Bases:

`Node`

openvino.impl.op.If wraps ov::op::v0::If

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.__init__) Overloaded function.

__init__(self: openvino._pyopenvino.op.if_op) -> None

__init__(self: openvino._pyopenvino.op.if_op, execution_condition: openvino._pyopenvino.Output) -> None

Constructs If with condition.

- param execution_condition:
condition node.

- type execution_condition:
openvino.Output

- rtype:
openvino.impl.op.If


__init__(self: openvino._pyopenvino.op.if_op, execution_condition: openvino._pyopenvino.Node) -> None

Constructs If with condition.

- param execution_condition:
condition node.

- type execution_condition:
openvino.Node

- rtype:
openvino.impl.op.If




Methods

(self, right)`__add__`

Return node which applies f(A,B) = A+B to the input nodes element-wise.

(self, arg0, arg1, *args, ...)`__array_ufunc__`

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

(self, arg0)`__getattr__`

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

(self, right)`__mul__`

Return node which applies f(A,B) = A*B to the input nodes element-wise.

(value, /)`__ne__`

Return self!=value.

(**kwargs)`__new__`

(self, arg0)`__radd__`

Helper for pickle.

(protocol, /)`__reduce_ex__`

Helper for pickle.

(self)`__repr__`

(self, arg0)`__rmul__`

(self, arg0)`__rsub__`

(self, arg0)`__rtruediv__`

(name, value, /)`__setattr__`

Implement setattr(self, name, value).

Size of object in memory, in bytes.

()`__str__`

Return str(self).

(self, right)`__sub__`

Return node which applies f(A,B) = A-B to the input nodes element-wise.

Abstract classes can override this to customize issubclass().

(self, right)`__truediv__`

Return node which applies f(A,B) = A/B to the input nodes element-wise.

(*args, **kwargs)`evaluate`

Overloaded function.

(self)`get_attributes`

(self)`get_element_type`

Checks that there is exactly one output and returns it's element type.

(self)`get_else_body`

Gets else_body as Model object.

(self)`get_friendly_name`

Gets the friendly name for a node.

(self, index)`get_function`

Gets internal sub-graph by index in MultiSubGraphOp.

(self, index)`get_input_descriptions`

Gets list with connections between operation inputs and internal sub-graph parameters.

(self, index)`get_input_element_type`

Returns the element type for input index

(self, index)`get_input_partial_shape`

Returns the partial shape for input index

(self, index)`get_input_shape`

Returns the shape for input index

(self)`get_input_size`

Returns the number of inputs to the node.

(self, index)`get_input_tensor`

Returns the tensor for the node's input with index i

(self)`get_instance_id`

Returns id of the node.

(self)`get_name`

Get the unique name of the node

(self, index)`get_output_descriptions`

Gets list with connections between operation outputs and internal sub-graph parameters.

(self, index)`get_output_element_type`

Returns the element type for output index

(self, index)`get_output_partial_shape`

Returns the partial shape for output index

(self, index)`get_output_shape`

Returns the shape for output index

(self)`get_output_size`

Returns the number of outputs from the node.

(self, index)`get_output_tensor`

Returns the tensor for output index

(self)`get_rt_info`

Returns RTMap which is a dictionary of user defined runtime info.

(self)`get_then_body`

Gets then_body as Model object.

(self)`get_type_info`

(self)`get_type_name`

Returns Type's name from the node.

(self, input_index)`input`

A handle to the input_index input of this node.

(self, index)`input_value`

Returns input of the node with index i

(self)`input_values`

Returns list of node's inputs, in order.

(self)`inputs`

A list containing a handle for each of this node's inputs, in order.

(self, output_index)`output`

A handle to the output_index output of this node.

(self)`outputs`

A list containing a handle for each of this node's outputs, in order.

(self, arg0, arg1)`set_argument`

(*args, **kwargs)`set_arguments`

Overloaded function.

(self, arg0, arg1)`set_attribute`

(self, body)`set_else_body`

Sets new Model object as new else_body.

(self, name)`set_friendly_name`

Sets a friendly name for a node.

(self, index, func)`set_function`

Adds sub-graph to MultiSubGraphOp.

(self, value, then_parameter, ...)`set_input`

Sets new input to the operation associated with parameters of each sub-graphs.

(self, index, inputs)`set_input_descriptions`

Sets list with connections between operation inputs and internal sub-graph parameters.

(self, then_result, else_result)`set_output`

Sets new output from the operation associated with results of each sub-graphs.

(self, index, outputs)`set_output_descriptions`

Sets list with connections between operation outputs and internal sub-graph parameters.

(self, size)`set_output_size`

Sets the number of outputs

(self, index, element_type, shape)`set_output_type`

Sets output's element type and shape.

(self, value, key)`set_rt_info`

Add a value to the runtime info.

(self, body)`set_then_body`

Sets new Model object as new then_body.

(self)`validate_and_infer_types`

Verifies that attributes and inputs are consistent and computes output shapes and element types.

(self, arg0)`visit_attributes`

Attributes

-
__add__(
*self:*,[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*right:*)[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| SupportsInt | SupportsFloat | numpy.ndarray[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.__add__) Return node which applies f(A,B) = A+B to the input nodes element-wise.

- Parameters:
**right**(*Union**[**openvino.Node**,**int**,**float**,**numpy.ndarray**]*) – The right operand.- Returns:
The node performing element-wise addition.

- Return type:


-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.__annotations__)

-
__array_ufunc__(
*self: object*,*arg0: object*,*arg1: str*,**args*,***kwargs*) object[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.__array_ufunc__)

-
__class__
[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.__ge__) Return self>=value.


-
__getattr__(
*self:*,[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*arg0: str*) collections.abc.Callable[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.__getattr__)

-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.__hash__) Return hash(self).


-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0) Overloaded function.

__init__(self: openvino._pyopenvino.op.if_op) -> None

__init__(self: openvino._pyopenvino.op.if_op, execution_condition: openvino._pyopenvino.Output) -> None

Constructs If with condition.

- param execution_condition:
condition node.

- type execution_condition:
openvino.Output

- rtype:
openvino.impl.op.If


__init__(self: openvino._pyopenvino.op.if_op, execution_condition: openvino._pyopenvino.Node) -> None

Constructs If with condition.

- param execution_condition:
condition node.

- type execution_condition:
openvino.Node

- rtype:
openvino.impl.op.If




-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.__lt__) Return self<value.


-
__mul__(
*self:*,[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*right:*)[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| SupportsInt | SupportsFloat | numpy.ndarray[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.__mul__) Return node which applies f(A,B) = A*B to the input nodes element-wise.

- Parameters:
**right**(*Union**[**openvino.Node**,**int**,**float**,**numpy.ndarray**]*) – The right operand.- Returns:
The node performing element-wise multiplication.

- Return type:


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.__new__)

-
__radd__(
*self:*,[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*arg0:*)[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| SupportsInt | SupportsFloat | numpy.ndarray[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.__radd__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.__reduce_ex__) Helper for pickle.


-
__repr__(
*self:*) str[openvino._pyopenvino.op.if_op](https://docs.openvino.ai#openvino.runtime.opset11.if_op)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.__repr__)

-
__rmul__(
*self:*,[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*arg0:*)[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| SupportsInt | SupportsFloat | numpy.ndarray[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.__rmul__)

-
__rsub__(
*self:*,[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*arg0:*)[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| SupportsInt | SupportsFloat | numpy.ndarray[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.__rsub__)

-
__rtruediv__(
*self:*,[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*arg0:*)[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| SupportsInt | SupportsFloat | numpy.ndarray[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.__rtruediv__)

-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.__str__) Return str(self).


-
__sub__(
*self:*,[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*right:*)[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| SupportsInt | SupportsFloat | numpy.ndarray[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.__sub__) Return node which applies f(A,B) = A-B to the input nodes element-wise.

- Parameters:
**right**(*Union**[**openvino.Node**,**int**,**float**,**numpy.ndarray**]*) – The right operand.- Returns:
The node performing element-wise subtraction.

- Return type:


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
__truediv__(
*self:*,[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*right:*)[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| SupportsInt | SupportsFloat | numpy.ndarray[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.__truediv__) Return node which applies f(A,B) = A/B to the input nodes element-wise.

- Parameters:
**right**(*Union**[**openvino.Node**,**int**,**float**,**numpy.ndarray**]*) – The right operand.- Returns:
The node performing element-wise division.

- Return type:


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op._pybind11_conduit_v1_)

-
constructor_validate_and_infer_types(
*self:*) None[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.constructor_validate_and_infer_types)

-
evaluate(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.evaluate) Overloaded function.

evaluate(self: openvino._pyopenvino.Node, output_values: openvino._pyopenvino.TensorVector, input_values: openvino._pyopenvino.TensorVector, evaluationContext: openvino._pyopenvino.RTMap = <RTMap>) -> bool

Evaluate the node on inputs, putting results in outputs

- param output_tensors:
Tensors for the outputs to compute. One for each result.

- type output_tensors:
openvino.TensorVector

- param input_tensors:
Tensors for the inputs. One for each inputs.

- type input_tensors:
openvino.TensorVector

- param evaluation_context:
Storage of additional settings and attributes that can be used


when evaluating the function. This additional information can be shared across nodes. :type evaluation_context: openvino.RTMap :rtype: bool

evaluate(self: openvino._pyopenvino.Node, output_values: list, input_values: list, evaluationContext: openvino._pyopenvino.RTMap = <RTMap>) -> bool

Evaluate the node on inputs, putting results in outputs

- param output_tensors:
Tensors for the outputs to compute. One for each result.

- type output_tensors:
openvino.TensorVector

- param input_tensors:
Tensors for the inputs. One for each inputs.

- type input_tensors:
openvino.TensorVector

- param evaluation_context:
Storage of additional settings and attributes that can be used


when evaluating the function. This additional information can be shared across nodes. :type evaluation_context: openvino.RTMap :rtype: bool



-
*property*friendly_name[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.friendly_name)

-
get_attributes(
*self:*) dict[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.get_attributes)

-
get_element_type(
*self:*)[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[openvino._pyopenvino.Type](https://docs.openvino.ai/openvino.Type.html#openvino.Type)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.get_element_type) Checks that there is exactly one output and returns it’s element type.

- Returns:
Type of the output.

- Return type:


-
get_else_body(
*self:*) object[openvino._pyopenvino.op.if_op](https://docs.openvino.ai#openvino.runtime.opset11.if_op)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.get_else_body) Gets else_body as Model object.

- Returns:
else_body as Model object.

- Return type:


-
get_friendly_name(
*self:*) str[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.get_friendly_name) Gets the friendly name for a node. If no friendly name has been set via set_friendly_name then the node’s unique name is returned.

- Returns:
Friendly name of the node.

- Return type:
str



-
get_function(
*self:*,[openvino._pyopenvino.op.if_op](https://docs.openvino.ai#openvino.runtime.opset11.if_op)*index: SupportsInt*) object[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.get_function) Gets internal sub-graph by index in MultiSubGraphOp.

- Parameters:
**index**(*int*) – sub-graph’s index in op.- Returns:
Model with sub-graph.

- Return type:


-
get_input_descriptions(
*self:*,[openvino._pyopenvino.op.if_op](https://docs.openvino.ai#openvino.runtime.opset11.if_op)*index: SupportsInt*) list[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.get_input_descriptions) Gets list with connections between operation inputs and internal sub-graph parameters.

- Parameters:
**index**(*int*) – index of internal sub-graph.- Returns:
list of input descriptions.

- Return type:
list[

[Union](https://docs.openvino.ai/genai_api/_autosummary/openvino_genai.StructuredOutputConfig.html#openvino_genai.StructuredOutputConfig.Union)[openvino.op.util.MergedInputDescription, openvino.op.util.InvariantInputDescription, openvino.op.util.SliceInputDescription]]


-
get_input_element_type(
*self:*,[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*index: SupportsInt*)[openvino._pyopenvino.Type](https://docs.openvino.ai/openvino.Type.html#openvino.Type)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.get_input_element_type) Returns the element type for input index

- Parameters:
**index**(*int*) – Index of the input.- Returns:
Type of the input index

- Return type:


-
get_input_partial_shape(
*self:*,[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*index: SupportsInt*)[openvino._pyopenvino.PartialShape](https://docs.openvino.ai/openvino.PartialShape.html#openvino.PartialShape)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.get_input_partial_shape) Returns the partial shape for input index

- Parameters:
**index**(*int*) – Index of the input.- Returns:
PartialShape of the input index

- Return type:


-
get_input_shape(
*self:*,[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*index: SupportsInt*)[openvino._pyopenvino.Shape](https://docs.openvino.ai/openvino.Shape.html#openvino.Shape)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.get_input_shape) Returns the shape for input index

- Parameters:
**index**(*int*) – Index of the input.- Returns:
Shape of the input index

- Return type:


-
get_input_size(
*self:*) int[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.get_input_size) Returns the number of inputs to the node.

- Returns:
Number of inputs.

- Return type:
int



-
get_input_tensor(
*self:*,[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*index: SupportsInt*) openvino._pyopenvino.DescriptorTensor[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.get_input_tensor) Returns the tensor for the node’s input with index i

- Parameters:
**index**(*int*) – Index of Input.- Returns:
Tensor of the input index

- Return type:
openvino._pyopenvino.DescriptorTensor



-
get_instance_id(
*self:*) int[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.get_instance_id) Returns id of the node. May be used to compare nodes if they are same instances.

- Returns:
id of the node.

- Return type:
int



-
get_name(
*self:*) str[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.get_name) Get the unique name of the node

- Returns:
Unique name of the node.

- Return type:
str



-
get_output_descriptions(
*self:*,[openvino._pyopenvino.op.if_op](https://docs.openvino.ai#openvino.runtime.opset11.if_op)*index: SupportsInt*) list[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.get_output_descriptions) Gets list with connections between operation outputs and internal sub-graph parameters.

- Parameters:
**index**(*int*) – index of internal sub-graph.- Returns:
list of output descriptions.

- Return type:
list[

[Union](https://docs.openvino.ai/genai_api/_autosummary/openvino_genai.StructuredOutputConfig.html#openvino_genai.StructuredOutputConfig.Union)[openvino.op.util.BodyOutputDescription, openvino.op.util.ConcatOutputDescription]]


-
get_output_element_type(
*self:*,[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*index: SupportsInt*)[openvino._pyopenvino.Type](https://docs.openvino.ai/openvino.Type.html#openvino.Type)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.get_output_element_type) Returns the element type for output index

- Parameters:
**index**(*int*) – Index of the output.- Returns:
Type of the output index

- Return type:


-
get_output_partial_shape(
*self:*,[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*index: SupportsInt*)[openvino._pyopenvino.PartialShape](https://docs.openvino.ai/openvino.PartialShape.html#openvino.PartialShape)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.get_output_partial_shape) Returns the partial shape for output index

- Parameters:
**index**(*int*) – Index of the output.- Returns:
PartialShape of the output index

- Return type:


-
get_output_shape(
*self:*,[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*index: SupportsInt*)[openvino._pyopenvino.Shape](https://docs.openvino.ai/openvino.Shape.html#openvino.Shape)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.get_output_shape) Returns the shape for output index

- Parameters:
**index**(*int*) – Index of the output.- Returns:
Shape of the output index

- Return type:


-
get_output_size(
*self:*) int[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.get_output_size) Returns the number of outputs from the node.

- Returns:
Number of outputs.

- Return type:
int



-
get_output_tensor(
*self:*,[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*index: SupportsInt*) openvino._pyopenvino.DescriptorTensor[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.get_output_tensor) Returns the tensor for output index

- Parameters:
**index**(*int*) – Index of the output.- Returns:
Tensor of the output index

- Return type:
openvino._pyopenvino.DescriptorTensor



-
get_rt_info(
*self:*)[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[openvino._pyopenvino.RTMap](https://docs.openvino.ai/openvino.RTMap.html#openvino.RTMap)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.get_rt_info) Returns RTMap which is a dictionary of user defined runtime info.

- Returns:
A dictionary of user defined data.

- Return type:


-
get_then_body(
*self:*) object[openvino._pyopenvino.op.if_op](https://docs.openvino.ai#openvino.runtime.opset11.if_op)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.get_then_body) Gets then_body as Model object.

- Returns:
then_body as Model object.

- Return type:


-
get_type_info(
*self:*)[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[openvino._pyopenvino.DiscreteTypeInfo](https://docs.openvino.ai/openvino.DiscreteTypeInfo.html#openvino.DiscreteTypeInfo)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.get_type_info)

-
get_type_name(
*self:*) str[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.get_type_name) Returns Type’s name from the node.

- Returns:
String representing Type’s name.

- Return type:
str



-
input(
*self:*,[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*input_index: SupportsInt*)[openvino._pyopenvino.Input](https://docs.openvino.ai/openvino.Input.html#openvino.Input)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.input) A handle to the input_index input of this node.

- Parameters:
**input_index**(*int*) – Index of Input.- Returns:
Input of this node.

- Return type:


-
input_value(
*self:*,[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*index: SupportsInt*)[openvino._pyopenvino.Output](https://docs.openvino.ai/openvino.Output.html#openvino.Output)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.input_value) Returns input of the node with index i

- Parameters:
**index**(*int*) – Index of Input.- Returns:
Input of this node.

- Return type:


-
input_values(
*self:*) list[[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[openvino._pyopenvino.Output](https://docs.openvino.ai/openvino.Output.html#openvino.Output)][#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.input_values) Returns list of node’s inputs, in order.

- Returns:
list of node’s inputs

- Return type:
list[

[openvino.Input](https://docs.openvino.ai/openvino.Input.html#openvino.Input)]


-
inputs(
*self:*) list[[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[openvino._pyopenvino.Input](https://docs.openvino.ai/openvino.Input.html#openvino.Input)][#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.inputs) A list containing a handle for each of this node’s inputs, in order.

- Returns:
list of node’s inputs.

- Return type:
list[

[openvino.Input](https://docs.openvino.ai/openvino.Input.html#openvino.Input)]


-
*property*name[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.name)

-
output(
*self:*,[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*output_index: SupportsInt*)[openvino._pyopenvino.Output](https://docs.openvino.ai/openvino.Output.html#openvino.Output)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.output) A handle to the output_index output of this node.

- Parameters:
**output_index**(*int*) – Index of Output.- Returns:
Output of this node.

- Return type:


-
outputs(
*self:*) list[[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[openvino._pyopenvino.Output](https://docs.openvino.ai/openvino.Output.html#openvino.Output)][#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.outputs) A list containing a handle for each of this node’s outputs, in order.

- Returns:
list of node’s outputs.

- Return type:
list[

[openvino.Output](https://docs.openvino.ai/openvino.Output.html#openvino.Output)]


-
*property*rt_info[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.rt_info)

-
set_argument(
*self:*,[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*arg0: SupportsInt*,*arg1:*) None[openvino._pyopenvino.Output](https://docs.openvino.ai/openvino.Output.html#openvino.Output)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.set_argument)

-
set_arguments(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.set_arguments) Overloaded function.

set_arguments(self: openvino._pyopenvino.Node, arg0: collections.abc.Sequence[openvino._pyopenvino.Node]) -> None

set_arguments(self: openvino._pyopenvino.Node, arg0: collections.abc.Sequence[openvino._pyopenvino.Output]) -> None



-
set_attribute(
*self:*,[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*arg0: str*,*arg1: object*) None[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.set_attribute)

-
set_else_body(
*self:*,[openvino._pyopenvino.op.if_op](https://docs.openvino.ai#openvino.runtime.opset11.if_op)*body: object*) None[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.set_else_body) Sets new Model object as new else_body.

- Parameters:
**body**() – new body for ‘else’ branch.*openvino.Model*- Return type:
None



-
set_friendly_name(
*self:*,[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*name: str*) None[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.set_friendly_name) Sets a friendly name for a node. This does not overwrite the unique name of the node and is retrieved via get_friendly_name(). Used mainly for debugging. The friendly name may be set exactly once.

- Parameters:
**name**(*str*) – Friendly name to set.


-
set_function(
*self:*,[openvino._pyopenvino.op.if_op](https://docs.openvino.ai#openvino.runtime.opset11.if_op)*index: SupportsInt*,*func: object*) None[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.set_function) Adds sub-graph to MultiSubGraphOp.

- Parameters:
**index**(*int*) – index of new sub-graph.**func**() – func new sub_graph as a Model.*openvino.Model*

- Return type:
None



-
set_input(
*self:*,[openvino._pyopenvino.op.if_op](https://docs.openvino.ai#openvino.runtime.opset11.if_op)*value:*,[openvino._pyopenvino.Output](https://docs.openvino.ai/openvino.Output.html#openvino.Output)*then_parameter:*,[openvino._pyopenvino.op.Parameter](https://docs.openvino.ai/openvino.runtime.op.Parameter.html#openvino.runtime.op.Parameter)*else_parameter:*) None[openvino._pyopenvino.op.Parameter](https://docs.openvino.ai/openvino.runtime.op.Parameter.html#openvino.runtime.op.Parameter)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.set_input) Sets new input to the operation associated with parameters of each sub-graphs.

- Parameters:
**value**() – input to operation.*openvino.Output***then_result**() – parameter for then_body or nullptr.*openvino.Node***else_result**() – parameter for else_body or nullptr.*openvino.Node*

- Return type:
None



-
set_input_descriptions(
*self:*,[openvino._pyopenvino.op.if_op](https://docs.openvino.ai#openvino.runtime.opset11.if_op)*index: SupportsInt*,*inputs: list*) None[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.set_input_descriptions) Sets list with connections between operation inputs and internal sub-graph parameters.

- Parameters:
**index**(*int*) – index of internal sub-graph.**inputs**(*list**[**Union**[**openvino.op.util.MergedInputDescription**,**openvino.op.util.InvariantInputDescription**,**openvino.op.util.SliceInputDescription**]**]*) – list of input descriptions.

- Return type:
None



-
set_output(
*self:*,[openvino._pyopenvino.op.if_op](https://docs.openvino.ai#openvino.runtime.opset11.if_op)*then_result:*,[openvino._pyopenvino.op.Result](https://docs.openvino.ai/openvino.runtime.op.Result.html#openvino.runtime.op.Result)*else_result:*)[openvino._pyopenvino.op.Result](https://docs.openvino.ai/openvino.runtime.op.Result.html#openvino.runtime.op.Result)[openvino._pyopenvino.Output](https://docs.openvino.ai/openvino.Output.html#openvino.Output)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.set_output) Sets new output from the operation associated with results of each sub-graphs.

- Parameters:
- Returns:
output from operation.

- Return type:


-
set_output_descriptions(
*self:*,[openvino._pyopenvino.op.if_op](https://docs.openvino.ai#openvino.runtime.opset11.if_op)*index: SupportsInt*,*outputs: list*) None[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.set_output_descriptions) Sets list with connections between operation outputs and internal sub-graph parameters.

- Parameters:
**index**(*int*) – index of internal sub-graph.**outputs**(*list**[**Union**[**openvino.op.util.BodyOutputDescription**,**openvino.op.util.ConcatOutputDescription**]**]*) – list of output descriptions.

- Return type:
None



-
set_output_size(
*self:*,[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*size: SupportsInt*) None[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.set_output_size) Sets the number of outputs

- Parameters:
**size**(*int*) – number of outputs.


-
set_output_type(
*self:*,[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*index: SupportsInt*,*element_type:*,[openvino._pyopenvino.Type](https://docs.openvino.ai/openvino.Type.html#openvino.Type)*shape:*) None[openvino._pyopenvino.PartialShape](https://docs.openvino.ai/openvino.PartialShape.html#openvino.PartialShape)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.set_output_type) Sets output’s element type and shape.

- Parameters:
**index**(*int*) – Index of the output.**element_type**() – Element type of the output.*openvino.Type***shape**() – Shape of the output.*openvino.PartialShape*



-
set_rt_info(
*self:*,[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*value: object*,*key: str*) None[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.set_rt_info) Add a value to the runtime info.

- Parameters:
**value**(*Any*) – Value for the runtime info.**key**(*str*) – String that defines a key in the runtime info dictionary.



-
set_then_body(
*self:*,[openvino._pyopenvino.op.if_op](https://docs.openvino.ai#openvino.runtime.opset11.if_op)*body: object*) None[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.set_then_body) Sets new Model object as new then_body.

- Parameters:
**body**() – new body for ‘then’ branch.*openvino.Model*- Return type:
None



-
*property*shape[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.shape)

-
*property*type_info[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.type_info)

-
validate_and_infer_types(
*self:*) None[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.validate_and_infer_types) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
visit_attributes(
*self:*,[openvino._pyopenvino.Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*arg0: openvino._pyopenvino.AttributeVisitor*) bool[#](https://docs.openvino.ai#openvino.runtime.opset11.if_op.visit_attributes)

-
__init__(