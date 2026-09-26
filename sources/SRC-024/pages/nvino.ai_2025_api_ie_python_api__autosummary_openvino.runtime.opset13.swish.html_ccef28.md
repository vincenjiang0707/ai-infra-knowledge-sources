source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset13.swish.html
lastmod: 

# openvino.runtime.opset13.swish[#](https://docs.openvino.ai#openvino-runtime-opset13-swish)

-
openvino.runtime.opset13.swish(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*beta:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray | None = None*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset13.swish) Return a node which performing Swish activation function Swish(x, beta=1.0) = x * sigmoid(x * beta)).

- Parameters:
**data**– Tensor with input data floating point type.- Returns:
The new node which performs Swish