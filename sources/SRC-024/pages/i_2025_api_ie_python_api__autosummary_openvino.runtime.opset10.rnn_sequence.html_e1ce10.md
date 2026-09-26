source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset10.rnn_sequence.html
lastmod: 

# openvino.runtime.opset10.rnn_sequence[#](https://docs.openvino.ai#openvino-runtime-opset10-rnn-sequence)

-
openvino.runtime.opset10.rnn_sequence(
*X:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*initial_hidden_state:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*sequence_lengths:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*W:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*R:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*B:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*hidden_size: int*,*direction: str*,*activations: list[str] | None = None*,*activations_alpha: list[float] | None = None*,*activations_beta: list[float] | None = None*,*clip: float = 0.0*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset10.rnn_sequence) Return a node which performs RNNSequence operation.

- Parameters:
**X**– The input tensor. Shape: [batch_size, seq_length, input_size].**initial_hidden_state**– The hidden state tensor. Shape: [batch_size, num_directions, hidden_size].**sequence_lengths**– Specifies real sequence lengths for each batch element. Shape: [batch_size]. Integer type.**W**– Tensor with weights for matrix multiplication operation with input portion of data. Shape: [num_directions, hidden_size, input_size].**R**– The tensor with weights for matrix multiplication operation with hidden state. Shape: [num_directions, hidden_size, hidden_size].**B**– The sum of biases (weight and recurrence). Shape: [num_directions, hidden_size].**hidden_size**– Specifies hidden state size.**direction**– Specifies if the RNN is forward, reverse, or bidirectional.**activations**– The list of three activation functions for gates.**activations_alpha**– The list of alpha parameters for activation functions.**activations_beta**– The list of beta parameters for activation functions.**clip**– Specifies bound values [-C, C] for tensor clipping performed before activations.**name**– An optional name of the output node.

- Returns:
The new node represents RNNSequence. Node outputs count: 2.