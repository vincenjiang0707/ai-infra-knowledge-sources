source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset10.softsign.html
lastmod: 

# openvino.runtime.opset10.softsign[#](https://docs.openvino.ai#openvino-runtime-opset10-softsign)

-
openvino.runtime.opset10.softsign(
*node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset10.softsign) Apply SoftSign operation on the input node element-wise.

- Parameters:
**node**– One of: input node, array or scalar.**name**– The optional name for the output node.

- Returns:
New node with SoftSign operation applied on each element of it.