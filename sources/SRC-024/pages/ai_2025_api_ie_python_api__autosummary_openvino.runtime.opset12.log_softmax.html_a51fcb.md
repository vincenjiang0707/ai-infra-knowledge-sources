source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset12.log_softmax.html
lastmod: 

# openvino.runtime.opset12.log_softmax[#](https://docs.openvino.ai#openvino-runtime-opset12-log-softmax)

-
openvino.runtime.opset12.log_softmax(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*axis: int*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset12.log_softmax) Apply LogSoftmax operation on each element of input tensor.

- Parameters:
**data**– The tensor providing input data.**axis**– An axis along which LogSoftmax should be calculated

- Returns:
The new node with LogSoftmax operation applied on each element.