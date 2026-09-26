source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset15.reduce_logical_or.html
lastmod: 

# openvino.runtime.opset15.reduce_logical_or[#](https://docs.openvino.ai#openvino-runtime-opset15-reduce-logical-or)

-
openvino.runtime.opset15.reduce_logical_or(
*node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*reduction_axes:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*keep_dims: bool = False*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset15.reduce_logical_or) Logical OR reduction operation on input tensor, eliminating the specified reduction axes.

- Parameters:
**node**– The tensor we want to reduce.**reduction_axes**– The axes to eliminate through OR operation.**keep_dims**– If set to True it holds axes that are used for reduction.**name**– Optional name for output node.

- Returns:
The new node performing reduction operation.