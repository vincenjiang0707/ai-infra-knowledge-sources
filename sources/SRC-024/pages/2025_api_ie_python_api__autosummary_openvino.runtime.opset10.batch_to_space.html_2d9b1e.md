source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset10.batch_to_space.html
lastmod: 

# openvino.runtime.opset10.batch_to_space[#](https://docs.openvino.ai#openvino-runtime-opset10-batch-to-space)

-
openvino.runtime.opset10.batch_to_space(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*block_shape:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*crops_begin:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*crops_end:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset10.batch_to_space) Perform BatchToSpace operation on the input tensor.

BatchToSpace permutes data from the batch dimension of the data tensor into spatial dimensions.

- Parameters:
**data**– Node producing the data tensor.**block_shape**– The sizes of the block of values to be moved.**crops_begin**– Specifies the amount to crop from the beginning along each axis of data.**crops_end**– Specifies the amount to crop from the end along each axis of data.**name**– Optional output node name.

- Returns:
The new node performing a BatchToSpace operation.