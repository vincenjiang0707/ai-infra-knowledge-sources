source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset14.bitwise_not.html
lastmod: 

# openvino.runtime.opset14.bitwise_not[#](https://docs.openvino.ai#openvino-runtime-opset14-bitwise-not)

-
openvino.runtime.opset14.bitwise_not(
*node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset14.bitwise_not) Return node which performs bitwise NOT operation on input node element-wise.

For boolean input tensors, operator is equivalent to logical_not.

- Parameters:
**node**– Tensor of integer or boolean datatype providing data.**name**– The optional new name for output node.

- Returns:
The node performing bitwise NOT operation on the given tensor.