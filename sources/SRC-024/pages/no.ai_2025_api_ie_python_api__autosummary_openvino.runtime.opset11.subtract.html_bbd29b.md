source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.subtract.html
lastmod: 

# openvino.runtime.opset11.subtract[#](https://docs.openvino.ai#openvino-runtime-opset11-subtract)

-
openvino.runtime.opset11.subtract(
*left_node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*right_node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*auto_broadcast: str = 'NUMPY'*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.subtract) Return node which applies f(x) = A-B to the input nodes element-wise.

- Parameters:
**left_node**– The node providing data for left hand side of operator.**right_node**– The node providing data for right hand side of operator.**auto_broadcast**– The type of broadcasting that specifies mapping of input tensor axes to output shape axes. Range of values: numpy, explicit.**name**– The optional name for output node.

- Returns:
The new output node performing subtraction operation on both tensors element-wise.