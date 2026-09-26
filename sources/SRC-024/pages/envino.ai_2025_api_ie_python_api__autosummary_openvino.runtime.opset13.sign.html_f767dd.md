source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset13.sign.html
lastmod: 

# openvino.runtime.opset13.sign[#](https://docs.openvino.ai#openvino-runtime-opset13-sign)

-
openvino.runtime.opset13.sign(
*node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset13.sign) Perform element-wise sign operation.

- Parameters:
**node**– One of: input node, array or scalar.**name**– The optional new name for output node.

- Returns:
The node with mapped elements of the input tensor to -1 (if it is negative), 0 (if it is zero), or 1 (if it is positive).