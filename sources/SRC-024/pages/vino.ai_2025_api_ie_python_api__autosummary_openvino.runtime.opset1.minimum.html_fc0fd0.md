source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset1.minimum.html
lastmod: 

# openvino.runtime.opset1.minimum[#](https://docs.openvino.ai#openvino-runtime-opset1-minimum)

-
openvino.runtime.opset1.minimum(
*left_node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*right_node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*auto_broadcast: str = 'NUMPY'*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset1.minimum) Return node which applies the minimum operation to input nodes elementwise.

- Parameters:
**left_node**– The first input node for minimum operation.**right_node**– The second input node for minimum operation.**auto_broadcast**– The type of broadcasting specifies rules used for auto-broadcasting of input tensors. Defaults to “NUMPY”.**name**– The optional name for output new node.

- Returns:
The node performing element-wise minimum operation.