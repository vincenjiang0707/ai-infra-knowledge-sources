source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset12.rnn_cell.html
lastmod: 

# openvino.runtime.opset12.rnn_cell[#](https://docs.openvino.ai#openvino-runtime-opset12-rnn-cell)

-
openvino.runtime.opset12.rnn_cell(
*X:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*initial_hidden_state:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*W:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*R:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*B:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*hidden_size: int*,*activations: list[str]*,*activations_alpha: list[float]*,*activations_beta: list[float]*,*clip: float = 0.0*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset12.rnn_cell) Perform RNNCell operation on tensor from input node.

It follows notation and equations defined as in ONNX standard:

[onnx/onnx](https://github.com/onnx/onnx/blob/master/docs/Operators.md#RNN)Note this class represents only single

*cell*and not whole RNN*layer*.- Parameters:
**X**– The input tensor with shape: [batch_size, input_size].**initial_hidden_state**– The hidden state tensor at current time step with shape: [batch_size, hidden_size].**W**– The weight tensor with shape: [hidden_size, input_size].**R**– The recurrence weight tensor with shape: [hidden_size, hidden_size].**B**– The sum of biases (weight and recurrence) with shape: [hidden_size].**hidden_size**– The number of hidden units for recurrent cell. Specifies hidden state size.**activations**– The vector of activation functions used inside recurrent cell.**activation_alpha**– The vector of alpha parameters for activation functions in order respective to activation list.**activation_beta**– The vector of beta parameters for activation functions in order respective to activation list.**clip**– The value defining clipping range [-clip, clip] on input of activation functions.**name**– Optional output node name.

- Returns:
The new node performing a RNNCell operation on tensor from input node.