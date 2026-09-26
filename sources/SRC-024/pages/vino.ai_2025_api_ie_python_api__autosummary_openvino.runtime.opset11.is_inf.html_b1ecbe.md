source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.is_inf.html
lastmod: 

# openvino.runtime.opset11.is_inf[#](https://docs.openvino.ai#openvino-runtime-opset11-is-inf)

-
openvino.runtime.opset11.is_inf(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*attributes: dict | None = None*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.is_inf) Return a node which performs IsInf operation.

- Parameters:
**data**– The input tensor.**attributes**– Optional dictionary containing IsInf attributes.**name**– Optional name of the node.


Available attributes:

- detect_negative Specifies whether to map negative infinities to true in output map.
Range of values: true, false Default value: true Required: no


- detect_positive Specifies whether to map positive infinities to true in output map.
Range of values: true, false Default value: true Required: no



- Returns:
A new IsInf node.