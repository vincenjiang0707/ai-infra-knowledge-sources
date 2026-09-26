source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset13.logical_and.html
lastmod: 

# openvino.runtime.opset13.logical_and[#](https://docs.openvino.ai#openvino-runtime-opset13-logical-and)

-
openvino.runtime.opset13.logical_and(
*left_node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*right_node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*auto_broadcast: str = 'NUMPY'*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset13.logical_and) Return node which perform logical and operation on input nodes element-wise.

- Parameters:
**left_node**– The first input node providing data.**right_node**– The second input node providing data.**auto_broadcast**– The type of broadcasting that specifies mapping of input tensor axes to output shape axes. Range of values: numpy, explicit.**name**– The optional new name for output node.

- Returns:
The node performing logical and operation on input nodes corresponding elements.