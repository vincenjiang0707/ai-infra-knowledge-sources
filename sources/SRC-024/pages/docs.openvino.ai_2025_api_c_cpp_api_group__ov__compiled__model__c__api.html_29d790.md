source: https://docs.openvino.ai/2025/api/c_cpp_api/group__ov__compiled__model__c__api.html
lastmod: 

# Group Compiled Model[#](https://docs.openvino.ai#group-compiled-model)

-
*group*Compiled Model The operations about compiled model.

Functions

-
ov_compiled_model_inputs_size(const
[ov_compiled_model_t](https://docs.openvino.ai/structov__compiled__model__t.html#_CPPv419ov_compiled_model_t)*compiled_model, size_t *size)[#](https://docs.openvino.ai#_CPPv429ov_compiled_model_inputs_sizePK19ov_compiled_model_tP6size_t) Get the input size of

[ov_compiled_model_t](https://docs.openvino.ai#structov__compiled__model__t).- Parameters:
**compiled_model**– A pointer to the[ov_compiled_model_t](https://docs.openvino.ai#structov__compiled__model__t).**input_size**– the compiled_model’s input size.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_compiled_model_input(const
[ov_compiled_model_t](https://docs.openvino.ai/structov__compiled__model__t.html#_CPPv419ov_compiled_model_t)*compiled_model,[ov_output_const_port_t](https://docs.openvino.ai/structov__output__const__port__t.html#_CPPv422ov_output_const_port_t)**input_port)[#](https://docs.openvino.ai#_CPPv423ov_compiled_model_inputPK19ov_compiled_model_tPP22ov_output_const_port_t) Get the single const input port of

[ov_compiled_model_t](https://docs.openvino.ai#structov__compiled__model__t), which only support single input model.- Parameters:
**compiled_model**– A pointer to the[ov_compiled_model_t](https://docs.openvino.ai#structov__compiled__model__t).**input_port**– A pointer to the[ov_output_const_port_t](https://docs.openvino.ai/group__ov__node__c__api.html#structov__output__const__port__t).

- Returns:
Status code of the operation: OK(0) for success.



-
ov_compiled_model_input_by_index(const
[ov_compiled_model_t](https://docs.openvino.ai/structov__compiled__model__t.html#_CPPv419ov_compiled_model_t)*compiled_model, const size_t index,[ov_output_const_port_t](https://docs.openvino.ai/structov__output__const__port__t.html#_CPPv422ov_output_const_port_t)**input_port)[#](https://docs.openvino.ai#_CPPv432ov_compiled_model_input_by_indexPK19ov_compiled_model_tK6size_tPP22ov_output_const_port_t) Get a const input port of

[ov_compiled_model_t](https://docs.openvino.ai#structov__compiled__model__t)by port index.- Parameters:
**compiled_model**– A pointer to the[ov_compiled_model_t](https://docs.openvino.ai#structov__compiled__model__t).**index**– input index.**input_port**– A pointer to the[ov_output_const_port_t](https://docs.openvino.ai/group__ov__node__c__api.html#structov__output__const__port__t).

- Returns:
Status code of the operation: OK(0) for success.



-
ov_compiled_model_input_by_name(const
[ov_compiled_model_t](https://docs.openvino.ai/structov__compiled__model__t.html#_CPPv419ov_compiled_model_t)*compiled_model, const char *name,[ov_output_const_port_t](https://docs.openvino.ai/structov__output__const__port__t.html#_CPPv422ov_output_const_port_t)**input_port)[#](https://docs.openvino.ai#_CPPv431ov_compiled_model_input_by_namePK19ov_compiled_model_tPKcPP22ov_output_const_port_t) Get a const input port of

[ov_compiled_model_t](https://docs.openvino.ai#structov__compiled__model__t)by name.- Parameters:
**compiled_model**– A pointer to the[ov_compiled_model_t](https://docs.openvino.ai#structov__compiled__model__t).**name**– input tensor name (char *).**input_port**– A pointer to the[ov_output_const_port_t](https://docs.openvino.ai/group__ov__node__c__api.html#structov__output__const__port__t).

- Returns:
Status code of the operation: OK(0) for success.



-
ov_compiled_model_outputs_size(const
[ov_compiled_model_t](https://docs.openvino.ai/structov__compiled__model__t.html#_CPPv419ov_compiled_model_t)*compiled_model, size_t *size)[#](https://docs.openvino.ai#_CPPv430ov_compiled_model_outputs_sizePK19ov_compiled_model_tP6size_t) Get the output size of

[ov_compiled_model_t](https://docs.openvino.ai#structov__compiled__model__t).- Parameters:
**compiled_model**– A pointer to the[ov_compiled_model_t](https://docs.openvino.ai#structov__compiled__model__t).**size**– the compiled_model’s output size.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_compiled_model_output(const
[ov_compiled_model_t](https://docs.openvino.ai/structov__compiled__model__t.html#_CPPv419ov_compiled_model_t)*compiled_model,[ov_output_const_port_t](https://docs.openvino.ai/structov__output__const__port__t.html#_CPPv422ov_output_const_port_t)**output_port)[#](https://docs.openvino.ai#_CPPv424ov_compiled_model_outputPK19ov_compiled_model_tPP22ov_output_const_port_t) Get the single const output port of

[ov_compiled_model_t](https://docs.openvino.ai#structov__compiled__model__t), which only support single output model.- Parameters:
**compiled_model**– A pointer to the[ov_compiled_model_t](https://docs.openvino.ai#structov__compiled__model__t).**output_port**– A pointer to the[ov_output_const_port_t](https://docs.openvino.ai/group__ov__node__c__api.html#structov__output__const__port__t).

- Returns:
Status code of the operation: OK(0) for success.



-
ov_compiled_model_output_by_index(const
[ov_compiled_model_t](https://docs.openvino.ai/structov__compiled__model__t.html#_CPPv419ov_compiled_model_t)*compiled_model, const size_t index,[ov_output_const_port_t](https://docs.openvino.ai/structov__output__const__port__t.html#_CPPv422ov_output_const_port_t)**output_port)[#](https://docs.openvino.ai#_CPPv433ov_compiled_model_output_by_indexPK19ov_compiled_model_tK6size_tPP22ov_output_const_port_t) Get a const output port of

[ov_compiled_model_t](https://docs.openvino.ai#structov__compiled__model__t)by port index.- Parameters:
**compiled_model**– A pointer to the[ov_compiled_model_t](https://docs.openvino.ai#structov__compiled__model__t).**index**– input index.**output_port**– A pointer to the[ov_output_const_port_t](https://docs.openvino.ai/group__ov__node__c__api.html#structov__output__const__port__t).

- Returns:
Status code of the operation: OK(0) for success.



-
ov_compiled_model_output_by_name(const
[ov_compiled_model_t](https://docs.openvino.ai/structov__compiled__model__t.html#_CPPv419ov_compiled_model_t)*compiled_model, const char *name,[ov_output_const_port_t](https://docs.openvino.ai/structov__output__const__port__t.html#_CPPv422ov_output_const_port_t)**output_port)[#](https://docs.openvino.ai#_CPPv432ov_compiled_model_output_by_namePK19ov_compiled_model_tPKcPP22ov_output_const_port_t) Get a const output port of

[ov_compiled_model_t](https://docs.openvino.ai#structov__compiled__model__t)by name.- Parameters:
**compiled_model**– A pointer to the[ov_compiled_model_t](https://docs.openvino.ai#structov__compiled__model__t).**name**– input tensor name (char *).**output_port**– A pointer to the[ov_output_const_port_t](https://docs.openvino.ai/group__ov__node__c__api.html#structov__output__const__port__t).

- Returns:
Status code of the operation: OK(0) for success.



-
ov_compiled_model_get_runtime_model(const
[ov_compiled_model_t](https://docs.openvino.ai/structov__compiled__model__t.html#_CPPv419ov_compiled_model_t)*compiled_model,[ov_model_t](https://docs.openvino.ai/structov__model__t.html#_CPPv410ov_model_t)**model)[#](https://docs.openvino.ai#_CPPv435ov_compiled_model_get_runtime_modelPK19ov_compiled_model_tPP10ov_model_t) Gets runtime model information from a device.

- Parameters:
**compiled_model**– A pointer to the[ov_compiled_model_t](https://docs.openvino.ai#structov__compiled__model__t).**model**– A pointer to the[ov_model_t](https://docs.openvino.ai/group__ov__model__c__api.html#structov__model__t).

- Returns:
Status code of the operation: OK(0) for success.



-
ov_compiled_model_create_infer_request(const
[ov_compiled_model_t](https://docs.openvino.ai/structov__compiled__model__t.html#_CPPv419ov_compiled_model_t)*compiled_model,[ov_infer_request_t](https://docs.openvino.ai/structov__infer__request__t.html#_CPPv418ov_infer_request_t)**infer_request)[#](https://docs.openvino.ai#_CPPv438ov_compiled_model_create_infer_requestPK19ov_compiled_model_tPP18ov_infer_request_t) Creates an inference request object used to infer the compiled model.

- Parameters:
**compiled_model**– A pointer to the[ov_compiled_model_t](https://docs.openvino.ai#structov__compiled__model__t).**infer_request**– A pointer to the[ov_infer_request_t](https://docs.openvino.ai/group__ov__infer__request__c__api.html#structov__infer__request__t).

- Returns:
Status code of the operation: OK(0) for success.



-
ov_compiled_model_set_property(const
[ov_compiled_model_t](https://docs.openvino.ai/structov__compiled__model__t.html#_CPPv419ov_compiled_model_t)*compiled_model, ...)[#](https://docs.openvino.ai#_CPPv430ov_compiled_model_set_propertyPK19ov_compiled_model_tz) Sets properties for a device, acceptable keys can be found in ov_property_key_xxx.

- Parameters:
**compiled_model**– A pointer to the[ov_compiled_model_t](https://docs.openvino.ai#structov__compiled__model__t).**...**– variadic paramaters The format is <char *property_key, char* property_value>. Supported property key please see ov_property.h.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_compiled_model_get_property(const
[ov_compiled_model_t](https://docs.openvino.ai/structov__compiled__model__t.html#_CPPv419ov_compiled_model_t)*compiled_model, const char *property_key, char **property_value)[#](https://docs.openvino.ai#_CPPv430ov_compiled_model_get_propertyPK19ov_compiled_model_tPKcPPc) Gets properties for current compiled model.

- Parameters:
**compiled_model**– A pointer to the[ov_compiled_model_t](https://docs.openvino.ai#structov__compiled__model__t).**property_key**– Property key.**property_value**– A pointer to property value.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_compiled_model_export_model(const
[ov_compiled_model_t](https://docs.openvino.ai/structov__compiled__model__t.html#_CPPv419ov_compiled_model_t)*compiled_model, const char *export_model_path)[#](https://docs.openvino.ai#_CPPv430ov_compiled_model_export_modelPK19ov_compiled_model_tPKc) Exports the current compiled model to an output stream

`std::ostream`

. The exported model can also be imported via the[ov::Core::import_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1a0d2853511bd7ba60cb591f4685b91884)method.- Parameters:
**compiled_model**– A pointer to the[ov_compiled_model_t](https://docs.openvino.ai#structov__compiled__model__t).**export_model_path**– Path to the file.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_compiled_model_free(
[ov_compiled_model_t](https://docs.openvino.ai/structov__compiled__model__t.html#_CPPv419ov_compiled_model_t)*compiled_model)[#](https://docs.openvino.ai#_CPPv422ov_compiled_model_freeP19ov_compiled_model_t) Release the memory allocated by

[ov_compiled_model_t](https://docs.openvino.ai#structov__compiled__model__t).- Parameters:
**compiled_model**– A pointer to the[ov_compiled_model_t](https://docs.openvino.ai#structov__compiled__model__t)to free memory.


-
ov_compiled_model_get_context(const
[ov_compiled_model_t](https://docs.openvino.ai/structov__compiled__model__t.html#_CPPv419ov_compiled_model_t)*compiled_model, ov_remote_context_t **context)[#](https://docs.openvino.ai#_CPPv429ov_compiled_model_get_contextPK19ov_compiled_model_tPP19ov_remote_context_t) Returns pointer to device-specific shared context on a remote accelerator device that was used to create this CompiledModel.

- Parameters:
**compiled_model**– A pointer to the[ov_compiled_model_t](https://docs.openvino.ai#structov__compiled__model__t).**context**– Return context.

- Returns:
Status code of the operation: OK(0) for success.



-
struct ov_compiled_model_t
[#](https://docs.openvino.ai#_CPPv419ov_compiled_model_t) *#include <ov_compiled_model.h>*type define

[ov_compiled_model_t](https://docs.openvino.ai#structov__compiled__model__t)from ov_compiled_model

-
ov_compiled_model_inputs_size(const