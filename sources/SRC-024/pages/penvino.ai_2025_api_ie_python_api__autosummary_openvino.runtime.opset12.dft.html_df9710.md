source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset12.dft.html
lastmod: 

# openvino.runtime.opset12.dft[#](https://docs.openvino.ai#openvino-runtime-opset12-dft)

-
openvino.runtime.opset12.dft(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*axes:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*signal_size:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray | None = None*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset12.dft) Return a node which performs DFT operation.

- Parameters:
**data**– Tensor with transformed data.**axes**– Tensor with axes to transform.**signal_size**– Tensor specifying signal size with respect to axes from the input ‘axes’.**name**– Optional output node name.

- Returns:
The new node which performs DFT operation on the input data tensor.