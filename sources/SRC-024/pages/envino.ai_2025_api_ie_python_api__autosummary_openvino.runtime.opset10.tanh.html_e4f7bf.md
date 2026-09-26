source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset10.tanh.html
lastmod: 

# openvino.runtime.opset10.tanh[#](https://docs.openvino.ai#openvino-runtime-opset10-tanh)

-
openvino.runtime.opset10.tanh(
*node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset10.tanh) Return node which applies hyperbolic tangent to the input node element-wise.

- Parameters:
**node**– One of: input node, array or scalar.**name**– Optional new name for output node.

- Returns:
New node with tanh operation applied on it.