source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset1.lstm_cell.html
lastmod: 

# openvino.runtime.opset1.lstm_cell[#](https://docs.openvino.ai#openvino-runtime-opset1-lstm-cell)

-
openvino.runtime.opset1.lstm_cell(
*X:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*initial_hidden_state:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*initial_cell_state:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*W:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*R:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*B:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*hidden_size: int*,*activations: list[str] | None = None*,*activations_alpha: list[float] | None = None*,*activations_beta: list[float] | None = None*,*clip: float = 0.0*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset1.lstm_cell) Return a node which performs LSTMCell operation.

- Parameters:
**X**– The input tensor with shape: [batch_size, input_size].**initial_hidden_state**– The hidden state tensor with shape: [batch_size, hidden_size].**initial_cell_state**– The cell state tensor with shape: [batch_size, hidden_size].**W**– The weight tensor with shape: [4*hidden_size, input_size].**R**– The recurrence weight tensor with shape: [4*hidden_size, hidden_size].**B**– The bias tensor for gates with shape: [4*hidden_size].**hidden_size**– Specifies hidden state size.**activations**– The list of three activation functions for gates.**activations_alpha**– The list of alpha parameters for activation functions.**activations_beta**– The list of beta parameters for activation functions.**clip**– Specifies bound values [-C, C] for tensor clipping performed before activations.**name**– An optional name of the output node.

- Returns:
The new node represents LSTMCell. Node outputs count: 2.