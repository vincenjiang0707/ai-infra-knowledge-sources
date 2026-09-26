source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset10.gelu.html
lastmod: 

# openvino.runtime.opset10.gelu[#](https://docs.openvino.ai#openvino-runtime-opset10-gelu)

-
openvino.runtime.opset10.gelu(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*approximation_mode: str*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset10.gelu) Return a node which performs Gelu activation function.

- Parameters:
**data**– The node with data tensor.**approximation_mode**– defines which approximation to use (‘tanh’ or ‘erf’)**name**– Optional output node name.

- Returns:
The new node performing a Gelu activation with the input tensor.