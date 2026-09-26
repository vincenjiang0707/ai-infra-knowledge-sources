source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.relu.html
lastmod: 

# openvino.runtime.opset11.relu[#](https://docs.openvino.ai#openvino-runtime-opset11-relu)

-
openvino.runtime.opset11.relu(
*node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.relu) Perform rectified linear unit operation on input node element-wise.

- Parameters:
**node**– One of: input node, array or scalar.**name**– The optional output node name.

- Returns:
The new node performing relu operation on its input element-wise.