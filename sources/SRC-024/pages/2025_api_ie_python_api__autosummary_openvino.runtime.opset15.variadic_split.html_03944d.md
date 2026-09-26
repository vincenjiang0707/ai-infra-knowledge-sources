source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset15.variadic_split.html
lastmod: 

# openvino.runtime.opset15.variadic_split[#](https://docs.openvino.ai#openvino-runtime-opset15-variadic-split)

-
openvino.runtime.opset15.variadic_split(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*axis:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*split_lengths:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset15.variadic_split) Return a node which splits the input tensor into variadic length slices.

- Parameters:
**data**– The input tensor to be split**axis**– Axis along which the input data will be split**split_lengths**– Sizes of the output tensors along the split axis

- Returns:
VariadicSplit node