source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset14.shape_of.html
lastmod: 

# openvino.runtime.opset14.shape_of[#](https://docs.openvino.ai#openvino-runtime-opset14-shape-of)

-
openvino.runtime.opset14.shape_of(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*output_type: str = 'i64'*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset14.shape_of) Return a node which produces a tensor containing the shape of its input data.

- Parameters:
**data**– The tensor containing the input data.**output_type**– Output element type.

- Returns:
ShapeOf node