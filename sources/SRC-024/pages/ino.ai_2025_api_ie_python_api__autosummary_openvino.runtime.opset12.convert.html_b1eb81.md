source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset12.convert.html
lastmod: 

# openvino.runtime.opset12.convert[#](https://docs.openvino.ai#openvino-runtime-opset12-convert)

-
openvino.runtime.opset12.convert(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*destination_type: str | type | dtype |*,[Type](https://docs.openvino.ai/openvino.Type.html#openvino.Type)*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset12.convert) Return node which casts input node values to specified type.

- Parameters:
**data**– Node which produces the input tensor.**destination_type**– Provides the target type for the conversion.**name**– Optional name for the output node.

- Returns:
New node performing the conversion operation.