source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset13.bitwise_xor.html
lastmod: 

# openvino.runtime.opset13.bitwise_xor[#](https://docs.openvino.ai#openvino-runtime-opset13-bitwise-xor)

-
openvino.runtime.opset13.bitwise_xor(
*left_node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*right_node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*auto_broadcast: str = 'NUMPY'*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset13.bitwise_xor) Return node which performs bitwise XOR operation on input nodes element-wise.

For boolean input tensors, operator is equivalent to logical_xor.

- Parameters:
**left_node**– Tensor of integer or boolean datatype providing data.**right_node**– Tensor of integer or boolean datatype providing data.**auto_broadcast**– The type of broadcasting specifies rules used for auto-broadcasting of input tensors. Defaults to “NUMPY”.**name**– The optional new name for output node.

- Returns:
The node performing bitwise XOR operation on input nodes corresponding elements.