source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset10.less.html
lastmod: 

# openvino.runtime.opset10.less[#](https://docs.openvino.ai#openvino-runtime-opset10-less)

-
openvino.runtime.opset10.less(
*left_node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*right_node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*auto_broadcast: str = 'NUMPY'*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset10.less) Return node which checks if left input node is less than the right node element-wise.

- Parameters:
**left_node**– The first input node providing data.**right_node**– The second input node providing data.**auto_broadcast**– The type of broadcasting specifies rules used for auto-broadcasting of input tensors.**name**– The optional new name for output node.

- Returns:
The node performing element-wise check whether left_node is less than the right_node.