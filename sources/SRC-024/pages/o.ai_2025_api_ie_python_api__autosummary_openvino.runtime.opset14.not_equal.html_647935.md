source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset14.not_equal.html
lastmod: 

# openvino.runtime.opset14.not_equal[#](https://docs.openvino.ai#openvino-runtime-opset14-not-equal)

-
openvino.runtime.opset14.not_equal(
*left_node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*right_node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*auto_broadcast: str = 'NUMPY'*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset14.not_equal) Return node which checks if input nodes are unequal element-wise.

- Parameters:
**left_node**– The first input node for not-equal operation.**right_node**– The second input node for not-equal operation.**auto_broadcast**– The type of broadcasting specifies rules used for auto-broadcasting of input tensors.**name**– The optional name for output new node.

- Returns:
The node performing element-wise inequality check.