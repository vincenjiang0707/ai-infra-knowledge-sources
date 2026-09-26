source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.transpose.html
lastmod: 

# openvino.runtime.opset11.transpose[#](https://docs.openvino.ai#openvino-runtime-opset11-transpose)

-
openvino.runtime.opset11.transpose(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*input_order:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.transpose) Return a node which transposes the data in the input tensor.

- Parameters:
**data**– The input tensor to be transposed**input_order**– Permutation of axes to be applied to the input tensor

- Returns:
Transpose node