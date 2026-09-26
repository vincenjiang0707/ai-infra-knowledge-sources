source: https://docs.openvino.ai/2025/api/c_cpp_api/group__ov__infer__request__c__api.html
lastmod: 

# Group Infer Request[#](https://docs.openvino.ai#group-infer-request)

-
*group*Infer Request The definitions & operations about infer request.

Functions

-
ov_infer_request_set_tensor(
[ov_infer_request_t](https://docs.openvino.ai/structov__infer__request__t.html#_CPPv418ov_infer_request_t)*infer_request, const char *tensor_name, const[ov_tensor_t](https://docs.openvino.ai/structov__tensor__t.html#_CPPv411ov_tensor_t)*tensor)[#](https://docs.openvino.ai#_CPPv427ov_infer_request_set_tensorP18ov_infer_request_tPKcPK11ov_tensor_t) Set an input/output tensor to infer on by the name of tensor.

- Parameters:
**infer_request**– A pointer to the[ov_infer_request_t](https://docs.openvino.ai#structov__infer__request__t).**tensor_name**– Name of the input or output tensor.**tensor**– Reference to the tensor.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_infer_request_set_tensor_by_port(
[ov_infer_request_t](https://docs.openvino.ai/structov__infer__request__t.html#_CPPv418ov_infer_request_t)*infer_request, const[ov_output_port_t](https://docs.openvino.ai/structov__output__port__t.html#_CPPv416ov_output_port_t)*port, const[ov_tensor_t](https://docs.openvino.ai/structov__tensor__t.html#_CPPv411ov_tensor_t)*tensor)[#](https://docs.openvino.ai#_CPPv435ov_infer_request_set_tensor_by_portP18ov_infer_request_tPK16ov_output_port_tPK11ov_tensor_t) Set an input/output tensor to infer request for the port.

- Parameters:
**infer_request**– A pointer to the[ov_infer_request_t](https://docs.openvino.ai#structov__infer__request__t).**port**– Port of the input or output tensor, which can be got by calling ov_model_t/ov_compiled_model_t interface.**tensor**– Reference to the tensor.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_infer_request_set_tensor_by_const_port(
[ov_infer_request_t](https://docs.openvino.ai/structov__infer__request__t.html#_CPPv418ov_infer_request_t)*infer_request, const[ov_output_const_port_t](https://docs.openvino.ai/structov__output__const__port__t.html#_CPPv422ov_output_const_port_t)*port, const[ov_tensor_t](https://docs.openvino.ai/structov__tensor__t.html#_CPPv411ov_tensor_t)*tensor)[#](https://docs.openvino.ai#_CPPv441ov_infer_request_set_tensor_by_const_portP18ov_infer_request_tPK22ov_output_const_port_tPK11ov_tensor_t) Set an input/output tensor to infer request for the port.

- Parameters:
**infer_request**– A pointer to the[ov_infer_request_t](https://docs.openvino.ai#structov__infer__request__t).**port**– Const port of the input or output tensor, which can be got by call interface from ov_model_t/ov_compiled_model_t.**tensor**– Reference to the tensor.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_infer_request_set_input_tensor_by_index(
[ov_infer_request_t](https://docs.openvino.ai/structov__infer__request__t.html#_CPPv418ov_infer_request_t)*infer_request, const size_t idx, const[ov_tensor_t](https://docs.openvino.ai/structov__tensor__t.html#_CPPv411ov_tensor_t)*tensor)[#](https://docs.openvino.ai#_CPPv442ov_infer_request_set_input_tensor_by_indexP18ov_infer_request_tK6size_tPK11ov_tensor_t) Set an input tensor to infer on by the index of tensor.

- Parameters:
**infer_request**– A pointer to the[ov_infer_request_t](https://docs.openvino.ai#structov__infer__request__t).**idx**– Index of the input port. If`idx`

is greater than the number of model inputs, an error will return.**tensor**– Reference to the tensor.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_infer_request_set_input_tensor(
[ov_infer_request_t](https://docs.openvino.ai/structov__infer__request__t.html#_CPPv418ov_infer_request_t)*infer_request, const[ov_tensor_t](https://docs.openvino.ai/structov__tensor__t.html#_CPPv411ov_tensor_t)*tensor)[#](https://docs.openvino.ai#_CPPv433ov_infer_request_set_input_tensorP18ov_infer_request_tPK11ov_tensor_t) Set an input tensor for the model with single input to infer on.

Note

If model has several inputs, an error will return.

- Parameters:
**infer_request**– A pointer to the[ov_infer_request_t](https://docs.openvino.ai#structov__infer__request__t).**tensor**– Reference to the tensor.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_infer_request_set_output_tensor_by_index(
[ov_infer_request_t](https://docs.openvino.ai/structov__infer__request__t.html#_CPPv418ov_infer_request_t)*infer_request, const size_t idx, const[ov_tensor_t](https://docs.openvino.ai/structov__tensor__t.html#_CPPv411ov_tensor_t)*tensor)[#](https://docs.openvino.ai#_CPPv443ov_infer_request_set_output_tensor_by_indexP18ov_infer_request_tK6size_tPK11ov_tensor_t) Set an output tensor to infer by the index of output tensor.

Note

Index of the output preserved accross

[ov_model_t](https://docs.openvino.ai/group__ov__model__c__api.html#structov__model__t),[ov_compiled_model_t](https://docs.openvino.ai/group__ov__compiled__model__c__api.html#structov__compiled__model__t).- Parameters:
**infer_request**– A pointer to the[ov_infer_request_t](https://docs.openvino.ai#structov__infer__request__t).**idx**– Index of the output tensor.**tensor**– Reference to the tensor.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_infer_request_set_output_tensor(
[ov_infer_request_t](https://docs.openvino.ai/structov__infer__request__t.html#_CPPv418ov_infer_request_t)*infer_request, const[ov_tensor_t](https://docs.openvino.ai/structov__tensor__t.html#_CPPv411ov_tensor_t)*tensor)[#](https://docs.openvino.ai#_CPPv434ov_infer_request_set_output_tensorP18ov_infer_request_tPK11ov_tensor_t) Set an output tensor to infer models with single output.

- Parameters:
**infer_request**– A pointer to the[ov_infer_request_t](https://docs.openvino.ai#structov__infer__request__t).**tensor**– Reference to the tensor.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_infer_request_get_tensor(const
[ov_infer_request_t](https://docs.openvino.ai/structov__infer__request__t.html#_CPPv418ov_infer_request_t)*infer_request, const char *tensor_name,[ov_tensor_t](https://docs.openvino.ai/structov__tensor__t.html#_CPPv411ov_tensor_t)**tensor)[#](https://docs.openvino.ai#_CPPv427ov_infer_request_get_tensorPK18ov_infer_request_tPKcPP11ov_tensor_t) Get an input/output tensor by the name of tensor.

Note

If model has several outputs, an error will return.

- Parameters:
**infer_request**– A pointer to the[ov_infer_request_t](https://docs.openvino.ai#structov__infer__request__t).**tensor_name**– Name of the input or output tensor to get.**tensor**– Reference to the tensor.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_infer_request_get_tensor_by_const_port(const
[ov_infer_request_t](https://docs.openvino.ai/structov__infer__request__t.html#_CPPv418ov_infer_request_t)*infer_request, const[ov_output_const_port_t](https://docs.openvino.ai/structov__output__const__port__t.html#_CPPv422ov_output_const_port_t)*port,[ov_tensor_t](https://docs.openvino.ai/structov__tensor__t.html#_CPPv411ov_tensor_t)**tensor)[#](https://docs.openvino.ai#_CPPv441ov_infer_request_get_tensor_by_const_portPK18ov_infer_request_tPK22ov_output_const_port_tPP11ov_tensor_t) Get an input/output tensor by const port.

- Parameters:
**infer_request**– A pointer to the[ov_infer_request_t](https://docs.openvino.ai#structov__infer__request__t).**port**– Port of the tensor to get.`port`

is not found, an error will return.**tensor**– Reference to the tensor.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_infer_request_get_tensor_by_port(const
[ov_infer_request_t](https://docs.openvino.ai/structov__infer__request__t.html#_CPPv418ov_infer_request_t)*infer_request, const[ov_output_port_t](https://docs.openvino.ai/structov__output__port__t.html#_CPPv416ov_output_port_t)*port,[ov_tensor_t](https://docs.openvino.ai/structov__tensor__t.html#_CPPv411ov_tensor_t)**tensor)[#](https://docs.openvino.ai#_CPPv435ov_infer_request_get_tensor_by_portPK18ov_infer_request_tPK16ov_output_port_tPP11ov_tensor_t) Get an input/output tensor by port.

- Parameters:
**infer_request**– A pointer to the[ov_infer_request_t](https://docs.openvino.ai#structov__infer__request__t).**port**– Port of the tensor to get.`port`

is not found, an error will return.**tensor**– Reference to the tensor.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_infer_request_get_input_tensor_by_index(const
[ov_infer_request_t](https://docs.openvino.ai/structov__infer__request__t.html#_CPPv418ov_infer_request_t)*infer_request, const size_t idx,[ov_tensor_t](https://docs.openvino.ai/structov__tensor__t.html#_CPPv411ov_tensor_t)**tensor)[#](https://docs.openvino.ai#_CPPv442ov_infer_request_get_input_tensor_by_indexPK18ov_infer_request_tK6size_tPP11ov_tensor_t) Get an input tensor by the index of input tensor.

- Parameters:
**infer_request**– A pointer to the[ov_infer_request_t](https://docs.openvino.ai#structov__infer__request__t).**idx**– Index of the tensor to get.`idx`

. If the tensor with the specified`idx`

is not found, an error will return.**tensor**– Reference to the tensor.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_infer_request_get_input_tensor(const
[ov_infer_request_t](https://docs.openvino.ai/structov__infer__request__t.html#_CPPv418ov_infer_request_t)*infer_request,[ov_tensor_t](https://docs.openvino.ai/structov__tensor__t.html#_CPPv411ov_tensor_t)**tensor)[#](https://docs.openvino.ai#_CPPv433ov_infer_request_get_input_tensorPK18ov_infer_request_tPP11ov_tensor_t) Get an input tensor from the model with only one input tensor.

- Parameters:
**infer_request**– A pointer to the[ov_infer_request_t](https://docs.openvino.ai#structov__infer__request__t).**tensor**– Reference to the tensor.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_infer_request_get_output_tensor_by_index(const
[ov_infer_request_t](https://docs.openvino.ai/structov__infer__request__t.html#_CPPv418ov_infer_request_t)*infer_request, const size_t idx,[ov_tensor_t](https://docs.openvino.ai/structov__tensor__t.html#_CPPv411ov_tensor_t)**tensor)[#](https://docs.openvino.ai#_CPPv443ov_infer_request_get_output_tensor_by_indexPK18ov_infer_request_tK6size_tPP11ov_tensor_t) Get an output tensor by the index of output tensor.

- Parameters:
**infer_request**– A pointer to the[ov_infer_request_t](https://docs.openvino.ai#structov__infer__request__t).**idx**– Index of the tensor to get.`idx`

. If the tensor with the specified`idx`

is not found, an error will return.**tensor**– Reference to the tensor.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_infer_request_get_output_tensor(const
[ov_infer_request_t](https://docs.openvino.ai/structov__infer__request__t.html#_CPPv418ov_infer_request_t)*infer_request,[ov_tensor_t](https://docs.openvino.ai/structov__tensor__t.html#_CPPv411ov_tensor_t)**tensor)[#](https://docs.openvino.ai#_CPPv434ov_infer_request_get_output_tensorPK18ov_infer_request_tPP11ov_tensor_t) Get an output tensor from the model with only one output tensor.

Note

If model has several outputs, an error will return.

- Parameters:
**infer_request**– A pointer to the[ov_infer_request_t](https://docs.openvino.ai#structov__infer__request__t).**tensor**– Reference to the tensor.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_infer_request_infer(
[ov_infer_request_t](https://docs.openvino.ai/structov__infer__request__t.html#_CPPv418ov_infer_request_t)*infer_request)[#](https://docs.openvino.ai#_CPPv422ov_infer_request_inferP18ov_infer_request_t) Infer specified input(s) in synchronous mode.

- Parameters:
**infer_request**– A pointer to the[ov_infer_request_t](https://docs.openvino.ai#structov__infer__request__t).- Returns:
Status code of the operation: OK(0) for success.



-
ov_infer_request_cancel(
[ov_infer_request_t](https://docs.openvino.ai/structov__infer__request__t.html#_CPPv418ov_infer_request_t)*infer_request)[#](https://docs.openvino.ai#_CPPv423ov_infer_request_cancelP18ov_infer_request_t) Cancel inference request.

- Parameters:
**infer_request**– A pointer to the[ov_infer_request_t](https://docs.openvino.ai#structov__infer__request__t).- Returns:
Status code of the operation: OK(0) for success.



-
ov_infer_request_start_async(
[ov_infer_request_t](https://docs.openvino.ai/structov__infer__request__t.html#_CPPv418ov_infer_request_t)*infer_request)[#](https://docs.openvino.ai#_CPPv428ov_infer_request_start_asyncP18ov_infer_request_t) Start inference of specified input(s) in asynchronous mode.

- Parameters:
**infer_request**– A pointer to the[ov_infer_request_t](https://docs.openvino.ai#structov__infer__request__t).- Returns:
Status code of the operation: OK(0) for success.



-
ov_infer_request_wait(
[ov_infer_request_t](https://docs.openvino.ai/structov__infer__request__t.html#_CPPv418ov_infer_request_t)*infer_request)[#](https://docs.openvino.ai#_CPPv421ov_infer_request_waitP18ov_infer_request_t) Wait for the result to become available.

- Parameters:
**infer_request**– A pointer to the[ov_infer_request_t](https://docs.openvino.ai#structov__infer__request__t).- Returns:
Status code of the operation: OK(0) for success.



-
ov_infer_request_wait_for(
[ov_infer_request_t](https://docs.openvino.ai/structov__infer__request__t.html#_CPPv418ov_infer_request_t)*infer_request, const int64_t timeout)[#](https://docs.openvino.ai#_CPPv425ov_infer_request_wait_forP18ov_infer_request_tK7int64_t) Waits for the result to become available. Blocks until the specified timeout has elapsed or the result becomes available, whichever comes first.

- Parameters:
**infer_request**– A pointer to the[ov_infer_request_t](https://docs.openvino.ai#structov__infer__request__t).**timeout**– Maximum duration, in milliseconds, to block for.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_infer_request_set_callback(
[ov_infer_request_t](https://docs.openvino.ai/structov__infer__request__t.html#_CPPv418ov_infer_request_t)*infer_request, const[ov_callback_t](https://docs.openvino.ai/structov__callback__t.html#_CPPv413ov_callback_t)*callback)[#](https://docs.openvino.ai#_CPPv429ov_infer_request_set_callbackP18ov_infer_request_tPK13ov_callback_t) Set callback function, which will be called when inference is done.

- Parameters:
**infer_request**– A pointer to the[ov_infer_request_t](https://docs.openvino.ai#structov__infer__request__t).**callback**– A function to be called.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_infer_request_free(
[ov_infer_request_t](https://docs.openvino.ai/structov__infer__request__t.html#_CPPv418ov_infer_request_t)*infer_request)[#](https://docs.openvino.ai#_CPPv421ov_infer_request_freeP18ov_infer_request_t) Release the memory allocated by

[ov_infer_request_t](https://docs.openvino.ai#structov__infer__request__t).- Parameters:
**infer_request**– A pointer to the[ov_infer_request_t](https://docs.openvino.ai#structov__infer__request__t)to free memory.


-
ov_infer_request_get_profiling_info(const
[ov_infer_request_t](https://docs.openvino.ai/structov__infer__request__t.html#_CPPv418ov_infer_request_t)*infer_request,[ov_profiling_info_list_t](https://docs.openvino.ai/structov__profiling__info__list__t.html#_CPPv424ov_profiling_info_list_t)*profiling_infos)[#](https://docs.openvino.ai#_CPPv435ov_infer_request_get_profiling_infoPK18ov_infer_request_tP24ov_profiling_info_list_t) Query performance measures per layer to identify the most time consuming operation.

- Parameters:
**infer_request**– A pointer to the[ov_infer_request_t](https://docs.openvino.ai#structov__infer__request__t).**profiling_infos**– Vector of profiling information for operations in a model.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_profiling_info_list_free(
[ov_profiling_info_list_t](https://docs.openvino.ai/structov__profiling__info__list__t.html#_CPPv424ov_profiling_info_list_t)*profiling_infos)[#](https://docs.openvino.ai#_CPPv427ov_profiling_info_list_freeP24ov_profiling_info_list_t) Release the memory allocated by

[ov_profiling_info_list_t](https://docs.openvino.ai#structov__profiling__info__list__t).- Parameters:
**profiling_infos**– A pointer to the[ov_profiling_info_list_t](https://docs.openvino.ai#structov__profiling__info__list__t)to free memory.


-
struct ov_infer_request_t
[#](https://docs.openvino.ai#_CPPv418ov_infer_request_t) *#include <ov_infer_request.h>*type define

[ov_infer_request_t](https://docs.openvino.ai#structov__infer__request__t)from ov_infer_request

-
struct ov_callback_t
[#](https://docs.openvino.ai#_CPPv413ov_callback_t) *#include <ov_infer_request.h>*Completion callback definition about the function and args.

Public Functions

- void (OPENVINO_C_API_CALLBACK *callback_func)(void *args)
The callback func.


Public Members

-
void *args
[#](https://docs.openvino.ai#_CPPv4N13ov_callback_t4argsE) The args of callback func.



-
struct ov_ProfilingInfo_t
[#](https://docs.openvino.ai#_CPPv418ov_ProfilingInfo_t) *#include <ov_infer_request.h>*Store profiling info data.


-
struct ov_profiling_info_list_t
[#](https://docs.openvino.ai#_CPPv424ov_profiling_info_list_t) *#include <ov_infer_request.h>*A list of profiling info data.

Public Members

-
[ov_profiling_info_t](https://docs.openvino.ai/structov__profiling__info__t.html#_CPPv419ov_profiling_info_t)*profiling_infos[#](https://docs.openvino.ai#_CPPv4N24ov_profiling_info_list_t15profiling_infosE) The list of ov_profilling_info_t.


-
size_t size
[#](https://docs.openvino.ai#_CPPv4N24ov_profiling_info_list_t4sizeE) The list size.


-

-
ov_infer_request_set_tensor(