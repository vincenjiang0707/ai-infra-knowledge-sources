source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset13.reduce_logical_and.html
lastmod: 

# openvino.runtime.opset13.reduce_logical_and[#](https://docs.openvino.ai#openvino-runtime-opset13-reduce-logical-and)

-
openvino.runtime.opset13.reduce_logical_and(
*node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*reduction_axes:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*keep_dims: bool = False*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset13.reduce_logical_and) Logical AND reduction operation on input tensor, eliminating the specified reduction axes.

- Parameters:
**node**– The tensor we want to reduce.**reduction_axes**– The axes to eliminate through AND operation.**keep_dims**– If set to True it holds axes that are used for reduction.**name**– Optional name for output node.

- Returns:
The new node performing reduction operation.