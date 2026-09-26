source: https://docs.openvino.ai/2025/api/c_cpp_api/group__ov__dev__api__sync__infer__request__api.html
lastmod: 

# Group Inference Request base classes[#](https://docs.openvino.ai#group-inference-request-base-classes)

-
*group*Inference Request base classes A set of base and helper classes to implement a syncrhonous inference request class.

-
class ISyncInferRequest : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[IInferRequest](https://docs.openvino.ai/classov_1_1_i_infer_request.html#_CPPv4N2ov13IInferRequestE)[#](https://docs.openvino.ai#_CPPv4N2ov17ISyncInferRequestE) *#include <isync_infer_request.hpp>*Interface for syncronous infer request.

Public Functions

Constructs syncronous inference request.

- Parameters:
**compiled_model**– pointer to compiled model


-
virtual
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[SoPtr](https://docs.openvino.ai/structov_1_1_so_ptr.html#_CPPv4I0EN2ov5SoPtrE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::ITensor> get_tensor(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &port) const override[#](https://docs.openvino.ai#_CPPv4NK2ov17ISyncInferRequest10get_tensorERKN2ov6OutputIKN2ov4NodeEEE) Gets an input/output tensor for inference.

Note

If the tensor with the specified

`port`

is not found, an exception is thrown.- Parameters:
**port**– Port of the tensor to get.- Returns:
[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)for the port`port`

.


-
virtual void set_tensor(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &port, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[SoPtr](https://docs.openvino.ai/structov_1_1_so_ptr.html#_CPPv4I0EN2ov5SoPtrE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::ITensor> &tensor) override[#](https://docs.openvino.ai#_CPPv4N2ov17ISyncInferRequest10set_tensorERKN2ov6OutputIKN2ov4NodeEEERKN2ov5SoPtrIN2ov7ITensorEEE) Sets an input/output tensor to infer.

- Parameters:
**port**– Port of the input or output tensor.**tensor**– Reference to a tensor. The element_type and shape of a tensor must match the model’s input/output element_type and size.



-
virtual std::vector<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[SoPtr](https://docs.openvino.ai/structov_1_1_so_ptr.html#_CPPv4I0EN2ov5SoPtrE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::ITensor>> get_tensors(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &port) const override[#](https://docs.openvino.ai#_CPPv4NK2ov17ISyncInferRequest11get_tensorsERKN2ov6OutputIKN2ov4NodeEEE) Gets a batch of tensors for input data to infer by input port.

[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)input must have batch dimension, and the number of`tensors`

must match the batch size. The current version supports setting tensors to model inputs only. If`port`

is associated with output (or any other non-input node), an exception is thrown.- Parameters:
**port**– Port of the input tensor.**tensors**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensors for batched infer request. The type of each tensor must match the model input element type and shape (except batch dimension). Total size of tensors must match the input size.

- Returns:
vector of tensors



-
virtual void set_tensors(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &port, const std::vector<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[SoPtr](https://docs.openvino.ai/structov_1_1_so_ptr.html#_CPPv4I0EN2ov5SoPtrE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::ITensor>> &tensors) override[#](https://docs.openvino.ai#_CPPv4N2ov17ISyncInferRequest11set_tensorsERKN2ov6OutputIKN2ov4NodeEEERKNSt6vectorIN2ov5SoPtrIN2ov7ITensorEEEEE) Sets a batch of tensors for input data to infer by input port.

[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)input must have batch dimension, and the number of`tensors`

must match the batch size. The current version supports setting tensors to model inputs only. If`port`

is associated with output (or any other non-input node), an exception is thrown.- Parameters:
**port**– Port of the input tensor.**tensors**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensors for batched infer request. The type of each tensor must match the model input element type and shape (except batch dimension). Total size of tensors must match the input size.



-
virtual const std::vector<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)>> &get_inputs() const override[#](https://docs.openvino.ai#_CPPv4NK2ov17ISyncInferRequest10get_inputsEv) Gets inputs for infer request.

- Returns:
vector of input ports



-
virtual const std::vector<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)>> &get_outputs() const override[#](https://docs.openvino.ai#_CPPv4NK2ov17ISyncInferRequest11get_outputsEv) Gets outputs for infer request.

- Returns:
vector of output ports



-
virtual const std::shared_ptr<const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[ICompiledModel](https://docs.openvino.ai/classov_1_1_i_compiled_model.html#_CPPv4N2ov14ICompiledModelE)> &get_compiled_model() const override[#](https://docs.openvino.ai#_CPPv4NK2ov17ISyncInferRequest18get_compiled_modelEv) Gets pointer to compiled model (usually synchronous request holds the compiled model)

- Returns:
Pointer to the compiled model




-
class ISyncInferRequest : public