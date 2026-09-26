source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset10.convert_like.html
lastmod: 

# openvino.runtime.opset10.convert_like[#](https://docs.openvino.ai#openvino-runtime-opset10-convert-like)

-
openvino.runtime.opset10.convert_like(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*like:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset10.convert_like) Return node which casts data node values to the type of another node.

- Parameters:
**data**– Node which produces the input tensor**like**– Node which provides the target type information for the conversion**name**– Optional name for the output node.

- Returns:
New node performing the conversion operation.