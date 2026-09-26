source: https://docs.openvino.ai/2025/api/c_cpp_api/group__ov__model__c__api.html
lastmod: 

# Group Model[#](https://docs.openvino.ai#group-model)

-
*group*Model The definitions & operations about model.

Functions

-
ov_model_free(
[ov_model_t](https://docs.openvino.ai/structov__model__t.html#_CPPv410ov_model_t)*model)[#](https://docs.openvino.ai#_CPPv413ov_model_freeP10ov_model_t) Release the memory allocated by

[ov_model_t](https://docs.openvino.ai#structov__model__t).- Parameters:
**model**– A pointer to the[ov_model_t](https://docs.openvino.ai#structov__model__t)to free memory.


-
ov_model_const_input(const
[ov_model_t](https://docs.openvino.ai/structov__model__t.html#_CPPv410ov_model_t)*model,[ov_output_const_port_t](https://docs.openvino.ai/structov__output__const__port__t.html#_CPPv422ov_output_const_port_t)**input_port)[#](https://docs.openvino.ai#_CPPv420ov_model_const_inputPK10ov_model_tPP22ov_output_const_port_t) Get a const input port of

[ov_model_t](https://docs.openvino.ai#structov__model__t),which only support single input model.- Parameters:
**model**– A pointer to the[ov_model_t](https://docs.openvino.ai#structov__model__t).**input_port**– A pointer to the[ov_output_const_port_t](https://docs.openvino.ai/group__ov__node__c__api.html#structov__output__const__port__t).

- Returns:
Status code of the operation: OK(0) for success.



-
ov_model_const_input_by_name(const
[ov_model_t](https://docs.openvino.ai/structov__model__t.html#_CPPv410ov_model_t)*model, const char *tensor_name,[ov_output_const_port_t](https://docs.openvino.ai/structov__output__const__port__t.html#_CPPv422ov_output_const_port_t)**input_port)[#](https://docs.openvino.ai#_CPPv428ov_model_const_input_by_namePK10ov_model_tPKcPP22ov_output_const_port_t) Get a const input port of

[ov_model_t](https://docs.openvino.ai#structov__model__t)by name.- Parameters:
**model**– A pointer to the[ov_model_t](https://docs.openvino.ai#structov__model__t).**tensor_name**– The name of input tensor.**input_port**– A pointer to the[ov_output_const_port_t](https://docs.openvino.ai/group__ov__node__c__api.html#structov__output__const__port__t).

- Returns:
Status code of the operation: OK(0) for success.



-
ov_model_const_input_by_index(const
[ov_model_t](https://docs.openvino.ai/structov__model__t.html#_CPPv410ov_model_t)*model, const size_t index,[ov_output_const_port_t](https://docs.openvino.ai/structov__output__const__port__t.html#_CPPv422ov_output_const_port_t)**input_port)[#](https://docs.openvino.ai#_CPPv429ov_model_const_input_by_indexPK10ov_model_tK6size_tPP22ov_output_const_port_t) Get a const input port of

[ov_model_t](https://docs.openvino.ai#structov__model__t)by port index.- Parameters:
**model**– A pointer to the[ov_model_t](https://docs.openvino.ai#structov__model__t).**index**– input tensor index.**input_port**– A pointer to the[ov_output_const_port_t](https://docs.openvino.ai/group__ov__node__c__api.html#structov__output__const__port__t).

- Returns:
Status code of the operation: OK(0) for success.



-
ov_model_input(const
[ov_model_t](https://docs.openvino.ai/structov__model__t.html#_CPPv410ov_model_t)*model,[ov_output_port_t](https://docs.openvino.ai/structov__output__port__t.html#_CPPv416ov_output_port_t)**input_port)[#](https://docs.openvino.ai#_CPPv414ov_model_inputPK10ov_model_tPP16ov_output_port_t) Get single input port of

[ov_model_t](https://docs.openvino.ai#structov__model__t), which only support single input model.- Parameters:
**model**– A pointer to the[ov_model_t](https://docs.openvino.ai#structov__model__t).**input_port**– A pointer to the[ov_output_port_t](https://docs.openvino.ai/group__ov__node__c__api.html#structov__output__port__t).

- Returns:
Status code of the operation: OK(0) for success.



-
ov_model_input_by_name(const
[ov_model_t](https://docs.openvino.ai/structov__model__t.html#_CPPv410ov_model_t)*model, const char *tensor_name,[ov_output_port_t](https://docs.openvino.ai/structov__output__port__t.html#_CPPv416ov_output_port_t)**input_port)[#](https://docs.openvino.ai#_CPPv422ov_model_input_by_namePK10ov_model_tPKcPP16ov_output_port_t) Get an input port of

[ov_model_t](https://docs.openvino.ai#structov__model__t)by name.- Parameters:
**model**– A pointer to the[ov_model_t](https://docs.openvino.ai#structov__model__t).**tensor_name**– input tensor name (char *).**input_port**– A pointer to the[ov_output_port_t](https://docs.openvino.ai/group__ov__node__c__api.html#structov__output__port__t).

- Returns:
Status code of the operation: OK(0) for success.



-
ov_model_input_by_index(const
[ov_model_t](https://docs.openvino.ai/structov__model__t.html#_CPPv410ov_model_t)*model, const size_t index,[ov_output_port_t](https://docs.openvino.ai/structov__output__port__t.html#_CPPv416ov_output_port_t)**input_port)[#](https://docs.openvino.ai#_CPPv423ov_model_input_by_indexPK10ov_model_tK6size_tPP16ov_output_port_t) Get an input port of

[ov_model_t](https://docs.openvino.ai#structov__model__t)by port index.- Parameters:
**model**– A pointer to the[ov_model_t](https://docs.openvino.ai#structov__model__t).**index**– input tensor index.**input_port**– A pointer to the[ov_output_port_t](https://docs.openvino.ai/group__ov__node__c__api.html#structov__output__port__t).

- Returns:
Status code of the operation: OK(0) for success.



-
ov_model_const_output(const
[ov_model_t](https://docs.openvino.ai/structov__model__t.html#_CPPv410ov_model_t)*model,[ov_output_const_port_t](https://docs.openvino.ai/structov__output__const__port__t.html#_CPPv422ov_output_const_port_t)**output_port)[#](https://docs.openvino.ai#_CPPv421ov_model_const_outputPK10ov_model_tPP22ov_output_const_port_t) Get a single const output port of

[ov_model_t](https://docs.openvino.ai#structov__model__t), which only support single output model.- Parameters:
**model**– A pointer to the[ov_model_t](https://docs.openvino.ai#structov__model__t).**output_port**– A pointer to the[ov_output_const_port_t](https://docs.openvino.ai/group__ov__node__c__api.html#structov__output__const__port__t).

- Returns:
Status code of the operation: OK(0) for success.



-
ov_model_const_output_by_index(const
[ov_model_t](https://docs.openvino.ai/structov__model__t.html#_CPPv410ov_model_t)*model, const size_t index,[ov_output_const_port_t](https://docs.openvino.ai/structov__output__const__port__t.html#_CPPv422ov_output_const_port_t)**output_port)[#](https://docs.openvino.ai#_CPPv430ov_model_const_output_by_indexPK10ov_model_tK6size_tPP22ov_output_const_port_t) Get a const output port of

[ov_model_t](https://docs.openvino.ai#structov__model__t)by port index.- Parameters:
**model**– A pointer to the[ov_model_t](https://docs.openvino.ai#structov__model__t).**index**– input tensor index.**output_port**– A pointer to the[ov_output_const_port_t](https://docs.openvino.ai/group__ov__node__c__api.html#structov__output__const__port__t).

- Returns:
Status code of the operation: OK(0) for success.



-
ov_model_const_output_by_name(const
[ov_model_t](https://docs.openvino.ai/structov__model__t.html#_CPPv410ov_model_t)*model, const char *tensor_name,[ov_output_const_port_t](https://docs.openvino.ai/structov__output__const__port__t.html#_CPPv422ov_output_const_port_t)**output_port)[#](https://docs.openvino.ai#_CPPv429ov_model_const_output_by_namePK10ov_model_tPKcPP22ov_output_const_port_t) Get a const output port of

[ov_model_t](https://docs.openvino.ai#structov__model__t)by name.- Parameters:
**model**– A pointer to the[ov_model_t](https://docs.openvino.ai#structov__model__t).**tensor_name**– input tensor name (char *).**output_port**– A pointer to the[ov_output_const_port_t](https://docs.openvino.ai/group__ov__node__c__api.html#structov__output__const__port__t).

- Returns:
Status code of the operation: OK(0) for success.



-
ov_model_output(const
[ov_model_t](https://docs.openvino.ai/structov__model__t.html#_CPPv410ov_model_t)*model,[ov_output_port_t](https://docs.openvino.ai/structov__output__port__t.html#_CPPv416ov_output_port_t)**output_port)[#](https://docs.openvino.ai#_CPPv415ov_model_outputPK10ov_model_tPP16ov_output_port_t) Get a single output port of

[ov_model_t](https://docs.openvino.ai#structov__model__t), which only support single output model.- Parameters:
**model**– A pointer to the[ov_model_t](https://docs.openvino.ai#structov__model__t).**output_port**– A pointer to the[ov_output_const_port_t](https://docs.openvino.ai/group__ov__node__c__api.html#structov__output__const__port__t).

- Returns:
Status code of the operation: OK(0) for success.



-
ov_model_output_by_index(const
[ov_model_t](https://docs.openvino.ai/structov__model__t.html#_CPPv410ov_model_t)*model, const size_t index,[ov_output_port_t](https://docs.openvino.ai/structov__output__port__t.html#_CPPv416ov_output_port_t)**output_port)[#](https://docs.openvino.ai#_CPPv424ov_model_output_by_indexPK10ov_model_tK6size_tPP16ov_output_port_t) Get an output port of

[ov_model_t](https://docs.openvino.ai#structov__model__t)by port index.- Parameters:
**model**– A pointer to the[ov_model_t](https://docs.openvino.ai#structov__model__t).**index**– input tensor index.**output_port**– A pointer to the[ov_output_port_t](https://docs.openvino.ai/group__ov__node__c__api.html#structov__output__port__t).

- Returns:
Status code of the operation: OK(0) for success.



-
ov_model_output_by_name(const
[ov_model_t](https://docs.openvino.ai/structov__model__t.html#_CPPv410ov_model_t)*model, const char *tensor_name,[ov_output_port_t](https://docs.openvino.ai/structov__output__port__t.html#_CPPv416ov_output_port_t)**output_port)[#](https://docs.openvino.ai#_CPPv423ov_model_output_by_namePK10ov_model_tPKcPP16ov_output_port_t) Get an output port of

[ov_model_t](https://docs.openvino.ai#structov__model__t)by name.- Parameters:
**model**– A pointer to the[ov_model_t](https://docs.openvino.ai#structov__model__t).**tensor_name**– output tensor name (char *).**output_port**– A pointer to the[ov_output_port_t](https://docs.openvino.ai/group__ov__node__c__api.html#structov__output__port__t).

- Returns:
Status code of the operation: OK(0) for success.



-
ov_model_inputs_size(const
[ov_model_t](https://docs.openvino.ai/structov__model__t.html#_CPPv410ov_model_t)*model, size_t *input_size)[#](https://docs.openvino.ai#_CPPv420ov_model_inputs_sizePK10ov_model_tP6size_t) Get the input size of

[ov_model_t](https://docs.openvino.ai#structov__model__t).- Parameters:
**model**– A pointer to the[ov_model_t](https://docs.openvino.ai#structov__model__t).**input_size**– the model’s input size.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_model_outputs_size(const
[ov_model_t](https://docs.openvino.ai/structov__model__t.html#_CPPv410ov_model_t)*model, size_t *output_size)[#](https://docs.openvino.ai#_CPPv421ov_model_outputs_sizePK10ov_model_tP6size_t) Get the output size of

[ov_model_t](https://docs.openvino.ai#structov__model__t).- Parameters:
**model**– A pointer to the[ov_model_t](https://docs.openvino.ai#structov__model__t).**output_size**– the model’s output size.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_model_reshape(const
[ov_model_t](https://docs.openvino.ai/structov__model__t.html#_CPPv410ov_model_t)*model, const char **tensor_names, const ov_partial_shape_t *partial_shapes, size_t size)[#](https://docs.openvino.ai#_CPPv416ov_model_reshapePK10ov_model_tPPKcPK18ov_partial_shape_t6size_t) Do reshape in model with a list of <name, partial shape>.

- Parameters:
**model**– A pointer to the[ov_model_t](https://docs.openvino.ai#structov__model__t).**tensor_names**– The list of input tensor names.**partialShape**– A PartialShape list.**size**– The item count in the list.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_model_reshape_input_by_name(const
[ov_model_t](https://docs.openvino.ai/structov__model__t.html#_CPPv410ov_model_t)*model, const char *tensor_name, const ov_partial_shape_t partial_shape)[#](https://docs.openvino.ai#_CPPv430ov_model_reshape_input_by_namePK10ov_model_tPKcK18ov_partial_shape_t) Do reshape in model with partial shape for a specified name.

- Parameters:
**model**– A pointer to the[ov_model_t](https://docs.openvino.ai#structov__model__t).**tensor_name**– The tensor name of input tensor.**partialShape**– A PartialShape.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_model_reshape_single_input(const
[ov_model_t](https://docs.openvino.ai/structov__model__t.html#_CPPv410ov_model_t)*model, const ov_partial_shape_t partial_shape)[#](https://docs.openvino.ai#_CPPv429ov_model_reshape_single_inputPK10ov_model_tK18ov_partial_shape_t) Do reshape in model for one node(port 0).

- Parameters:
**model**– A pointer to the[ov_model_t](https://docs.openvino.ai#structov__model__t).**partialShape**– A PartialShape.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_model_reshape_by_port_indexes(const
[ov_model_t](https://docs.openvino.ai/structov__model__t.html#_CPPv410ov_model_t)*model, const size_t *port_indexes, const ov_partial_shape_t *partial_shape, size_t size)[#](https://docs.openvino.ai#_CPPv432ov_model_reshape_by_port_indexesPK10ov_model_tPK6size_tPK18ov_partial_shape_t6size_t) Do reshape in model with a list of <port id, partial shape>.

- Parameters:
**model**– A pointer to the[ov_model_t](https://docs.openvino.ai#structov__model__t).**port_indexes**– The array of port indexes.**partialShape**– A PartialShape list.**size**– The item count in the list.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_model_reshape_by_ports(const
[ov_model_t](https://docs.openvino.ai/structov__model__t.html#_CPPv410ov_model_t)*model, const[ov_output_port_t](https://docs.openvino.ai/structov__output__port__t.html#_CPPv416ov_output_port_t)**output_ports, const ov_partial_shape_t *partial_shapes, size_t size)[#](https://docs.openvino.ai#_CPPv425ov_model_reshape_by_portsPK10ov_model_tPPK16ov_output_port_tPK18ov_partial_shape_t6size_t) Do reshape in model with a list of <

[ov_output_port_t](https://docs.openvino.ai/group__ov__node__c__api.html#structov__output__port__t), partial shape>.- Parameters:
**model**– A pointer to the[ov_model_t](https://docs.openvino.ai#structov__model__t).**output_ports**– The[ov_output_port_t](https://docs.openvino.ai/group__ov__node__c__api.html#structov__output__port__t)list.**partialShape**– A PartialShape list.**size**– The item count in the list.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_model_get_friendly_name(const
[ov_model_t](https://docs.openvino.ai/structov__model__t.html#_CPPv410ov_model_t)*model, char **friendly_name)[#](https://docs.openvino.ai#_CPPv426ov_model_get_friendly_namePK10ov_model_tPPc) Gets the friendly name for a model.

- Parameters:
**model**– A pointer to the[ov_model_t](https://docs.openvino.ai#structov__model__t).**friendly_name**– the model’s friendly name.

- Returns:
Status code of the operation: OK(0) for success.



-
struct ov_model_t
[#](https://docs.openvino.ai#_CPPv410ov_model_t) *#include <ov_model.h>*type define

[ov_model_t](https://docs.openvino.ai#structov__model__t)from ov_model

-
ov_model_free(