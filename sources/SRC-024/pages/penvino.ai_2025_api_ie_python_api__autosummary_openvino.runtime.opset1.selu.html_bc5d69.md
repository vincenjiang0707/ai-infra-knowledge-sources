source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset1.selu.html
lastmod: 

# openvino.runtime.opset1.selu[#](https://docs.openvino.ai#openvino-runtime-opset1-selu)

-
openvino.runtime.opset1.selu(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*alpha:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*lambda_value:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset1.selu) Perform a Scaled Exponential Linear Unit (SELU) operation on input node element-wise.

- Parameters:
**data**– input node, array or scalar.**alpha**– Alpha coefficient of SELU operation**lambda_value**– Lambda coefficient of SELU operation**name**– The optional output node name.

- Returns:
The new node performing relu operation on its input element-wise.