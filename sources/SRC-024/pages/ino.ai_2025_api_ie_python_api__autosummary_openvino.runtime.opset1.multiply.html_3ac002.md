source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset1.multiply.html
lastmod: 

# openvino.runtime.opset1.multiply[#](https://docs.openvino.ai#openvino-runtime-opset1-multiply)

-
openvino.runtime.opset1.multiply(
*left_node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*right_node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*auto_broadcast: str = 'NUMPY'*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset1.multiply) Return node which applies f(A,B) = A*B to the input nodes elementwise.

- Parameters:
**left_node**– The first input node for multiply operation.**right_node**– The second input node for multiply operation.**auto_broadcast**– The type of broadcasting specifies rules used for auto-broadcasting of input tensors. Defaults to “NUMPY”.**name**– The optional name for output new node.

- Returns:
The node performing element-wise multiplication.