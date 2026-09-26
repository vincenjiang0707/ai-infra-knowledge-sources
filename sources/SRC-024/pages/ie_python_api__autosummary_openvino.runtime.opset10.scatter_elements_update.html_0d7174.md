source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset10.scatter_elements_update.html
lastmod: 

# openvino.runtime.opset10.scatter_elements_update[#](https://docs.openvino.ai#openvino-runtime-opset10-scatter-elements-update)

-
openvino.runtime.opset10.scatter_elements_update(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*indices:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*updates:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*axis:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset10.scatter_elements_update) Return a node which produces a ScatterElementsUpdate operation.

- Parameters:
**data**– The input tensor to be updated.**indices**– The tensor with indexes which will be updated.**updates**– The tensor with update values.**axis**– The axis for scatter.

- Returns:
ScatterElementsUpdate node


ScatterElementsUpdate creates a copy of the first input tensor with updated elements specified with second and third input tensors.

For each entry in updates, the target index in data is obtained by combining the corresponding entry in indices with the index of the entry itself: the index-value for dimension equal to axis is obtained from the value of the corresponding entry in indices and the index-value for dimension not equal to axis is obtained from the index of the entry itself.