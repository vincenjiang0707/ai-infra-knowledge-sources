source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.split.html
lastmod: 

# openvino.runtime.opset11.split[#](https://docs.openvino.ai#openvino-runtime-opset11-split)

-
openvino.runtime.opset11.split(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*axis:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*num_splits: int*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.split) Return a node which splits the input tensor into same-length slices.

- Parameters:
**data**– The input tensor to be split**axis**– Axis along which the input data will be split**num_splits**– Number of the output tensors that should be produced

- Returns:
Split node