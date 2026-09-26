source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset10.power.html
lastmod: 

# openvino.runtime.opset10.power[#](https://docs.openvino.ai#openvino-runtime-opset10-power)

-
openvino.runtime.opset10.power(
*left_node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*right_node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*auto_broadcast: str = 'NUMPY'*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset10.power) Return node which perform element-wise exponentiation operation.

- Parameters:
**left_node**– The node providing the base of operation.**right_node**– The node providing the exponent of operation.**name**– The optional name for the new output node.**auto_broadcast**– The type of broadcasting specifies rules used for auto-broadcasting of input tensors.

- Returns:
The new node performing element-wise exponentiation operation on input nodes.