source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset1.depth_to_space.html
lastmod: 

# openvino.runtime.opset1.depth_to_space[#](https://docs.openvino.ai#openvino-runtime-opset1-depth-to-space)

-
openvino.runtime.opset1.depth_to_space(
*node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*mode: str*,*block_size: int = 1*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset1.depth_to_space) Rearranges input tensor from depth into blocks of spatial data.

Values from the height and width dimensions are moved to the depth dimension.

Input tensor has shape [N,C,H,W], where N is the batch axis, C is the channel or depth, H is the height and W is the width.

Output node produces a tensor with shape:

[N, C * block_size * block_size, H / block_size, W / block_size]

- Parameters:
**node**– The node with input tensor data.**mode**–Specifies how the input depth dimension is split to block coordinates

blocks_first: The input is divided to [block_size, …, block_size, new_depth] depth_first: The input is divided to [new_depth, block_size, …, block_size]

**block_size**– The size of the spatial block of values describing how the tensor’s data is to be rearranged.**name**– Optional output node name.

- Returns:
The new node performing an DepthToSpace operation on its input tensor.