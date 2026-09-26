source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.space_to_depth.html
lastmod: 

# openvino.runtime.opset11.space_to_depth[#](https://docs.openvino.ai#openvino-runtime-opset11-space-to-depth)

-
openvino.runtime.opset11.space_to_depth(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*mode: str*,*block_size: int = 1*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.space_to_depth) Perform SpaceToDepth operation on the input tensor.

SpaceToDepth rearranges blocks of spatial data into depth. The operator :return: a copy of the input tensor where values from the height and width dimensions are moved to the depth dimension.

- Parameters:
**data**– The node with data tensor.**mode**–Specifies how the output depth dimension is gathered from block coordinates.

blocks_first: The output depth is gathered from [block_size, …, block_size, C] depth_first: The output depth is gathered from [C, block_size, …, block_size]

**block_size**– The size of the block of values to be moved. Scalar value.**name**– Optional output node name.

- Returns:
The new node performing a SpaceToDepth operation on input tensor.