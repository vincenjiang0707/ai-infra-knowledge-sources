source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.negative.html
lastmod: 

# openvino.runtime.opset11.negative[#](https://docs.openvino.ai#openvino-runtime-opset11-negative)

-
openvino.runtime.opset11.negative(
*node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.negative) Return node which applies f(x) = -x to the input node elementwise.

- Parameters:
**node**– Input node for negative operation.**name**– The optional name for output new node.

- Returns:
The node performing element-wise multiplicaion by -1.