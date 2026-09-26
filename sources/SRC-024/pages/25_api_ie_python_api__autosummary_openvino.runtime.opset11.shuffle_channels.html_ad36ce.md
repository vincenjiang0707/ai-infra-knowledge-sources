source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.shuffle_channels.html
lastmod: 

# openvino.runtime.opset11.shuffle_channels[#](https://docs.openvino.ai#openvino-runtime-opset11-shuffle-channels)

-
openvino.runtime.opset11.shuffle_channels(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*axis: int*,*group: int*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.shuffle_channels) Perform permutation on data in the channel dimension of the input tensor.

- Parameters:
**data**– The node with input tensor.**axis**– Channel dimension index in the data tensor. A negative value means that the index should be calculated from the back of the input data shape.**group**– The channel dimension specified by the axis parameter should be split into this number of groups.**name**– Optional output node name.

- Returns:
The new node performing a permutation on data in the channel dimension of the input tensor.


The operation is the equivalent with the following transformation of the input tensor data of shape [N, C, H, W]:

data_reshaped = reshape(data, [N, group, C / group, H * W])

data_transposed = transpose(data_reshaped, [0, 2, 1, 3])

output = reshape(data_transposed, [N, C, H, W])

For example:

Inputs: tensor of shape [1, 6, 2, 2] data = [[[[ 0., 1.], [ 2., 3.]], [[ 4., 5.], [ 6., 7.]], [[ 8., 9.], [10., 11.]], [[12., 13.], [14., 15.]], [[16., 17.], [18., 19.]], [[20., 21.], [22., 23.]]]] axis = 1 groups = 3 Output: tensor of shape [1, 6, 2, 2] output = [[[[ 0., 1.], [ 2., 3.]], [[ 8., 9.], [10., 11.]], [[16., 17.], [18., 19.]], [[ 4., 5.], [ 6., 7.]], [[12., 13.], [14., 15.]], [[20., 21.], [22., 23.]]]]