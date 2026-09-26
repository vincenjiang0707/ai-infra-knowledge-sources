source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.is_finite.html
lastmod: 

# openvino.runtime.opset11.is_finite[#](https://docs.openvino.ai#openvino-runtime-opset11-is-finite)

-
openvino.runtime.opset11.is_finite(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.is_finite) Performs element-wise mapping from NaN and Infinity to False. Other values are mapped to True.

- Parameters:
**data**– A tensor of floating-point numeric type and arbitrary shape.**name**– Optional name for the output node. The default is None.

- Returns:
Node representing is_finite operation.