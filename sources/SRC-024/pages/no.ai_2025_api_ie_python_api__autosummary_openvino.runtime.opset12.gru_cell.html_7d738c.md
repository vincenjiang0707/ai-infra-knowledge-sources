source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset12.gru_cell.html
lastmod: 

# openvino.runtime.opset12.gru_cell[#](https://docs.openvino.ai#openvino-runtime-opset12-gru-cell)

-
openvino.runtime.opset12.gru_cell(
*X:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*initial_hidden_state:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*W:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*R:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*B:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*hidden_size: int*,*activations: list[str] | None = None*,*activations_alpha: list[float] | None = None*,*activations_beta: list[float] | None = None*,*clip: float = 0.0*,*linear_before_reset: bool = False*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset12.gru_cell) Perform GRUCell operation on the tensor from input node.

GRUCell represents a single GRU Cell that computes the output using the formula described in the paper:

[https://arxiv.org/abs/1406.1078](https://arxiv.org/abs/1406.1078)Note this class represents only single

*cell*and not whole*layer*.- Parameters:
**X**– The input tensor with shape: [batch_size, input_size].**initial_hidden_state**– The hidden state tensor at current time step with shape: [batch_size, hidden_size].**W**– The weights for matrix multiplication, gate order: zrh. Shape: [3*hidden_size, input_size].**R**– The recurrence weights for matrix multiplication. Shape: [3*hidden_size, hidden_size].**B**– The sum of biases (weight and recurrence). For linear_before_reset set True the shape is [4*hidden_size]. Otherwise the shape is [3*hidden_size].**hidden_size**– The number of hidden units for recurrent cell. Specifies hidden state size.**activations**– The vector of activation functions used inside recurrent cell.**activation_alpha**– The vector of alpha parameters for activation functions in order respective to activation list.**activation_beta**– The vector of beta parameters for activation functions in order respective to activation list.**clip**– The value defining clipping range [-clip, clip] on input of activation functions.**linear_before_reset**– Flag denotes if the layer behaves according to the modification of GRUCell described in the formula in the ONNX documentation.**name**– Optional output node name.

- Returns:
The new node performing a GRUCell operation on tensor from input node.