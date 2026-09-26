source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.scatter_update.html
lastmod: 

# openvino.runtime.opset11.scatter_update[#](https://docs.openvino.ai#openvino-runtime-opset11-scatter-update)

-
openvino.runtime.opset11.scatter_update(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*indices:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*updates:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*axis:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.scatter_update) Return a node which produces a ScatterUpdate operation.

ScatterUpdate sets new values to slices from data addressed by indices.

- Parameters:
**data**– The input tensor to be updated.**indices**– The tensor with indexes which will be updated.**updates**– The tensor with update values.**axis**– The axis at which elements will be updated.

- Returns:
ScatterUpdate node