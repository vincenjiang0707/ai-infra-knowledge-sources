source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset1.gather.html
lastmod: 

# openvino.runtime.opset1.gather[#](https://docs.openvino.ai#openvino-runtime-opset1-gather)

-
openvino.runtime.opset1.gather(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*indices:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*axis:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset1.gather) Return Gather node which takes slices from axis of data according to indices.

- Parameters:
**data**– The tensor from which slices are gathered.**indices**– Tensor with indexes to gather.**axis**– The dimension index to gather data from.**name**– Optional name for output node.

- Returns:
The new node performing a Gather operation on the data input tensor.