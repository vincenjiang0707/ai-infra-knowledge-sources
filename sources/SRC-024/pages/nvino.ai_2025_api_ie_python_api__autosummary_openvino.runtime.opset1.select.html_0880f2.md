source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset1.select.html
lastmod: 

# openvino.runtime.opset1.select[#](https://docs.openvino.ai#openvino-runtime-opset1-select)

-
openvino.runtime.opset1.select(
*cond:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*then_node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*else_node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*auto_broadcast: str = 'numpy'*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset1.select) Perform an element-wise selection operation on input tensors.

- Parameters:
**cond**– Tensor with selection mask of type boolean.**then_node**– Tensor providing data to be selected if respective cond item value is True.**else_node**– Tensor providing data to be selected if respective cond item value is False.**auto_broadcast**– Mode specifies rules used for auto-broadcasting of input tensors.**name**– The optional new name for output node.

- Returns:
The new node with values selected according to provided arguments.