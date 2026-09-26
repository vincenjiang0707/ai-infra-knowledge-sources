source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset10.space_to_batch.html
lastmod: 

# openvino.runtime.opset10.space_to_batch[#](https://docs.openvino.ai#openvino-runtime-opset10-space-to-batch)

-
openvino.runtime.opset10.space_to_batch(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*block_shape:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*pads_begin:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*pads_end:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset10.space_to_batch) Perform SpaceToBatch operation on the input tensor.

SpaceToBatch permutes data tensor blocks of spatial data into batch dimension. The operator returns a copy of the input tensor where values from spatial blocks dimensions are moved in the batch dimension

- Parameters:
**data**– Node producing the data tensor.**block_shape**– The sizes of the block of values to be moved.**pads_begin**– Specifies the padding for the beginning along each axis of data.**pads_end**– Specifies the padding for the ending along each axis of data.**name**– Optional output node name.

- Returns:
The new node performing a SpaceToBatch operation.