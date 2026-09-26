source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset13.logical_not.html
lastmod: 

# openvino.runtime.opset13.logical_not[#](https://docs.openvino.ai#openvino-runtime-opset13-logical-not)

-
openvino.runtime.opset13.logical_not(
*node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset13.logical_not) Return node which applies element-wise logical negation to the input node.

- Parameters:
**node**– The input node providing data.**name**– The optional new name for output node.

- Returns:
The node performing element-wise logical NOT operation with given tensor.