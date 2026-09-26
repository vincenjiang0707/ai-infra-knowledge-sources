source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset14.einsum.html
lastmod: 

# openvino.runtime.opset14.einsum[#](https://docs.openvino.ai#openvino-runtime-opset14-einsum)

-
openvino.runtime.opset14.einsum(
*inputs: list[*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)]*equation: str*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset14.einsum) Return a node which performs Einsum operation.

- Parameters:
**inputs**– The list of input nodes**equation**– Einsum equation**name**– Optional output node name.

- Returns:
The new node performing Einsum operation on the inputs