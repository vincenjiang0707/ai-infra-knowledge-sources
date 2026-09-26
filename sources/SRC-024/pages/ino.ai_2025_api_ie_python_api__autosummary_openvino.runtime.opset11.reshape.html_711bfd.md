source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.reshape.html
lastmod: 

# openvino.runtime.opset11.reshape[#](https://docs.openvino.ai#openvino-runtime-opset11-reshape)

-
openvino.runtime.opset11.reshape(
*node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*output_shape:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*special_zero: bool*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.reshape) Return reshaped node according to provided parameters.

- Parameters:
**node**– The tensor we want to reshape.**output_shape**– The node with a new shape for input tensor.**special_zero**– The boolean variable that controls how zero values in shape are interpreted. If special_zero is false, then 0 is interpreted as-is which means that output shape will contain a zero dimension at the specified location. Input and output tensors are empty in this case. If special_zero is true, then all zeros in shape implies the copying of corresponding dimensions from data.shape into the output shape. Range of values: False or True

- Returns:
The node reshaping an input tensor.