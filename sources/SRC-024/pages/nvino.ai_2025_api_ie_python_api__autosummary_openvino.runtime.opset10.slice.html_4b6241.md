source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset10.slice.html
lastmod: 

# openvino.runtime.opset10.slice[#](https://docs.openvino.ai#openvino-runtime-opset10-slice)

-
openvino.runtime.opset10.slice(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*start:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*stop:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*step:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*axes:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray | None = None*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset10.slice) Return a node which generates Slice operation.

- Parameters:
**data**– The node providing input data.**start**– The node providing start indices (inclusively).**stop**– The node providing stop indices (exclusively).**step**– The node providing step values.**axes**– The optional node providing axes to slice, default [0, 1, …, len(start)-1].**name**– The optional name for the created output node.

- Returns:
The new node performing Slice operation.