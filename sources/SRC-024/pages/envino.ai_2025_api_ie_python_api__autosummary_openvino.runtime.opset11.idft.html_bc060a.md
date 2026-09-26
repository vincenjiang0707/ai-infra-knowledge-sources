source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.idft.html
lastmod: 

# openvino.runtime.opset11.idft[#](https://docs.openvino.ai#openvino-runtime-opset11-idft)

-
openvino.runtime.opset11.idft(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*axes:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*signal_size:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray | None = None*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.idft) Return a node which performs IDFT operation.

- Parameters:
**data**– Tensor with transformed data.**axes**– Tensor with axes to transform.**signal_size**– Tensor specifying signal size with respect to axes from the input ‘axes’.**name**– Optional output node name.

- Returns:
The new node which performs IDFT operation on the input data tensor.