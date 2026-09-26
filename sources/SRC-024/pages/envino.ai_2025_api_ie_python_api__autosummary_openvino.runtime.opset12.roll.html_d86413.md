source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset12.roll.html
lastmod: 

# openvino.runtime.opset12.roll[#](https://docs.openvino.ai#openvino-runtime-opset12-roll)

-
openvino.runtime.opset12.roll(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*shift:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*axes:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset12.roll) Return a node which performs Roll operation.

- Parameters:
**data**– The node with data tensor.**shift**– The node with the tensor with numbers of places by which elements are shifted.**axes**– The node with the tensor with axes along which elements are shifted.**name**– Optional output node name.

- Returns:
The new node performing a Roll operation on the input tensor.