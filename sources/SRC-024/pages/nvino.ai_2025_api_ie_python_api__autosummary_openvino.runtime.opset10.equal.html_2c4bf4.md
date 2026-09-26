source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset10.equal.html
lastmod: 

# openvino.runtime.opset10.equal[#](https://docs.openvino.ai#openvino-runtime-opset10-equal)

-
openvino.runtime.opset10.equal(
*left_node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*right_node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*auto_broadcast: str = 'NUMPY'*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset10.equal) Return node which checks if input nodes are equal element-wise.

- Parameters:
**left_node**– The first input node for equal operation.**right_node**– The second input node for equal operation.**auto_broadcast**– The type of broadcasting specifies rules used for auto-broadcasting of input tensors.**name**– The optional name for output new node.

- Returns:
The node performing element-wise equality check.