source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset14.unsqueeze.html
lastmod: 

# openvino.runtime.opset14.unsqueeze[#](https://docs.openvino.ai#openvino-runtime-opset14-unsqueeze)

-
openvino.runtime.opset14.unsqueeze(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*axes:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset14.unsqueeze) Perform unsqueeze operation on input tensor.

Insert single-dimensional entries to the shape of a tensor. Takes one required argument axes, a list of dimensions that will be inserted. Dimension indices in axes are as seen in the output tensor.

- For example: Inputs: tensor with shape [3, 4, 5], axes=[0, 4]
Result: tensor with shape [1, 3, 4, 5, 1]


- Parameters:
**data**– The node with data tensor.**axes**– list of non-negative integers, indicate the dimensions to be inserted. One of: input node or array.

- Returns:
The new node performing an unsqueeze operation on input tensor.