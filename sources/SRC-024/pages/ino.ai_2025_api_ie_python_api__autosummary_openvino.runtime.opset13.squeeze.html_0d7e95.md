source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset13.squeeze.html
lastmod: 

# openvino.runtime.opset13.squeeze[#](https://docs.openvino.ai#openvino-runtime-opset13-squeeze)

-
openvino.runtime.opset13.squeeze(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*axes:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset13.squeeze) Perform squeeze operation on input tensor.

- Parameters:
**data**– The node with data tensor.**axes**– list of non-negative integers, indicate the dimensions to squeeze. One of: input node or array.**name**– Optional new name for output node.

- Returns:
The new node performing a squeeze operation on input tensor.


Remove single-dimensional entries from the shape of a tensor. Takes a parameter axes with a list of axes to squeeze. If axes is not provided, all the single dimensions will be removed from the shape. If an axis is selected with shape entry not equal to one, an error is raised.

For example:

Inputs: tensor with shape [1, 2, 1, 3, 1, 1], axes=[2, 4]

Result: tensor with shape [1, 2, 3, 1]