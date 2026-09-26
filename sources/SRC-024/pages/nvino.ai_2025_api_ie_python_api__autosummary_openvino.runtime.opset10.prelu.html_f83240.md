source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset10.prelu.html
lastmod: 

# openvino.runtime.opset10.prelu[#](https://docs.openvino.ai#openvino-runtime-opset10-prelu)

-
openvino.runtime.opset10.prelu(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*slope:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset10.prelu) Perform Parametrized Relu operation element-wise on data from input node.

- Parameters:
**data**– The node with data tensor.**slope**– The node with the multipliers for negative values.**name**– Optional output node name.

- Returns:
The new node performing a PRelu operation on tensor’s channels.


PRelu uses the following logic:

if data < 0: data = data * slope elif data >= 0: data = data