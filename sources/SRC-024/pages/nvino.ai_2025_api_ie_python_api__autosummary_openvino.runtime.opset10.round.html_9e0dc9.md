source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset10.round.html
lastmod: 

# openvino.runtime.opset10.round[#](https://docs.openvino.ai#openvino-runtime-opset10-round)

-
openvino.runtime.opset10.round(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*mode: str = 'half_to_even'*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset10.round) Apply Round operation on each element of input tensor.

- Parameters:
**data**– The tensor providing input data.**mode**– Rule to round halfway cases. If set to ‘half_to_even’ then halfs round to the nearest even integer or rounding in such a way that the result heads away from zero if mode attribute is ‘half_away_from_zero`.**name**– An optional name of the output node.

- Returns:
The new node with Round operation applied on each element.