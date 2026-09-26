source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset13.hard_sigmoid.html
lastmod: 

# openvino.runtime.opset13.hard_sigmoid[#](https://docs.openvino.ai#openvino-runtime-opset13-hard-sigmoid)

-
openvino.runtime.opset13.hard_sigmoid(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*alpha:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*beta:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset13.hard_sigmoid) Perform Hard Sigmoid operation element-wise on data from input node.

- Parameters:
**data**– The node with data tensor.**alpha**– A node producing the alpha parameter.**beta**– A node producing the beta parameter**name**– Optional output node name.

- Returns:
The new node performing a Hard Sigmoid element-wise on input tensor.


Hard Sigmoid uses the following logic:

y = max(0, min(1, alpha * data + beta))