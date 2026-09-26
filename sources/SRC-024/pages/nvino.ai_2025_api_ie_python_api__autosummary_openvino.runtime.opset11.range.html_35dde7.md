source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.range.html
lastmod: 

# openvino.runtime.opset11.range[#](https://docs.openvino.ai#openvino-runtime-opset11-range)

-
openvino.runtime.opset11.range(
*start:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*stop:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*step:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.range) Return a node which produces the Range operation.

- Parameters:
**start**– The start value of the generated range.**stop**– The stop value of the generated range.**step**– The step value for the generated range.**name**– Optional name for output node.

- Returns:
Range node