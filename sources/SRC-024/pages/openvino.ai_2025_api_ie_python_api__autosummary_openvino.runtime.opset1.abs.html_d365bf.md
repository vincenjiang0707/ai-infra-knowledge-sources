source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset1.abs.html
lastmod: 

# openvino.runtime.opset1.abs[#](https://docs.openvino.ai#openvino-runtime-opset1-abs)

-
openvino.runtime.opset1.abs(
*node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset1.abs) Return node which applies f(x) = abs(x) to the input node element-wise.

- Parameters:
**node**– One of: input node, array or scalar.**name**– Optional new name for output node.

- Returns:
New node with Abs operation applied on it.