source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset15.squeeze.html
lastmod: 

# openvino.runtime.opset15.squeeze[#](https://docs.openvino.ai#openvino-runtime-opset15-squeeze)

-
openvino.runtime.opset15.squeeze(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*axes:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray | None = None*allow_axis_skip: bool = False*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset15.squeeze) Perform squeeze operation on input tensor.

- Parameters:
**data**– The node with data tensor.**axes**– Optional list of integers, indicating the dimensions to squeeze. Negative indices are supported. One of: input node or array.**allow_axis_skip**– If true, shape inference results in a dynamic rank, when selected axis has value 1 in its dynamic range. Used only if axes input is given. Defaults to false.**name**– Optional new name for output node.

- Returns:
The new node performing a squeeze operation on input tensor.


Remove single-dimensional entries from the shape of a tensor. Takes an optional parameter axes with a list of axes to squeeze. If axes is not provided, all the single dimensions will be removed from the shape.

For example:

Inputs: tensor with shape [1, 2, 1, 3, 1, 1], axes=[2, 4]

Result: tensor with shape [1, 2, 3, 1]