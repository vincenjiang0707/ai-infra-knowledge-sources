source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset12.divide.html
lastmod: 

# openvino.runtime.opset12.divide[#](https://docs.openvino.ai#openvino-runtime-opset12-divide)

-
openvino.runtime.opset12.divide(
*left_node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*right_node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*auto_broadcast: str = 'NUMPY'*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset12.divide) Return node which applies f(x) = A/B to the input nodes element-wise.

- Parameters:
**left_node**– The node providing dividend data.**right_node**– The node providing divisor data.**auto_broadcast**– Specifies rules used for auto-broadcasting of input tensors.**name**– Optional name for output node.

- Returns:
The node performing element-wise division.