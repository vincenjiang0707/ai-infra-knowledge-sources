source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset12.is_nan.html
lastmod: 

# openvino.runtime.opset12.is_nan[#](https://docs.openvino.ai#openvino-runtime-opset12-is-nan)

-
openvino.runtime.opset12.is_nan(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset12.is_nan) Performs element-wise mapping from NaN to True. Other values are mapped to False.

- Parameters:
**data**– A tensor of floating point numeric type and arbitrary shape.**name**– Optional name for the output node. Default is None.

- Returns:
Node representing is_nan operation.