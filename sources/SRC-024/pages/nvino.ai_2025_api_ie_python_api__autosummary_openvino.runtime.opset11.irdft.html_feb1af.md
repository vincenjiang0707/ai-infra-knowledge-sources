source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.irdft.html
lastmod: 

# openvino.runtime.opset11.irdft[#](https://docs.openvino.ai#openvino-runtime-opset11-irdft)

-
openvino.runtime.opset11.irdft(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*axes:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*signal_size:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray | None = None*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.irdft) Return a node which performs IRDFT operation.

- Parameters:
**data**– Tensor with data.**axes**– Tensor with axes to transform.**signal_size**– Optional tensor specifying signal size with respect to axes from the input ‘axes’.**name**– Optional output node name.

- Returns:
The new node which performs IRDFT operation on the input data tensor.