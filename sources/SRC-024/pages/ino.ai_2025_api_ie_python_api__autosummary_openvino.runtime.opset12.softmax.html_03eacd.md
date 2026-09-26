source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset12.softmax.html
lastmod: 

# openvino.runtime.opset12.softmax[#](https://docs.openvino.ai#openvino-runtime-opset12-softmax)

-
openvino.runtime.opset12.softmax(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*axis: int*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset12.softmax) Apply softmax operation on each element of input tensor.

- Parameters:
**data**– The tensor providing input data.**axis**– An axis along which Softmax should be calculated. Can be positive or negative.**name**– Optional name for the node.

- Returns:
The new node with softmax operation applied on each element.