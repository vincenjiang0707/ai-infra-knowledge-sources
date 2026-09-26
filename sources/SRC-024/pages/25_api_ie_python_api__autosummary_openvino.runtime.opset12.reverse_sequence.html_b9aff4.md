source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset12.reverse_sequence.html
lastmod: 

# openvino.runtime.opset12.reverse_sequence[#](https://docs.openvino.ai#openvino-runtime-opset12-reverse-sequence)

-
openvino.runtime.opset12.reverse_sequence(
*input:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*seq_lengths:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*batch_axis: int | float | ndarray*,*seq_axis: int | float | ndarray*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset12.reverse_sequence) Return a node which produces a ReverseSequence operation.

- Parameters:
**input**– tensor with input data to reverse**seq_lengths**– 1D tensor of integers with sequence lengths in the input tensor.**batch_axis**– index of the batch dimension.**seq_axis**– index of the sequence dimension.

- Returns:
ReverseSequence node