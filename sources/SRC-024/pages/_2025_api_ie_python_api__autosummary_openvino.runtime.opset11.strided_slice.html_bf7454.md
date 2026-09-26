source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.strided_slice.html
lastmod: 

# openvino.runtime.opset11.strided_slice[#](https://docs.openvino.ai#openvino-runtime-opset11-strided-slice)

-
openvino.runtime.opset11.strided_slice(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*begin:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*end:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*strides:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*begin_mask: list[int]*,*end_mask: list[int]*,*new_axis_mask: list[int] | None = None*,*shrink_axis_mask: list[int] | None = None*,*ellipsis_mask: list[int] | None = None*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.strided_slice) Return a node which dynamically repeats(replicates) the input data tensor.

- Parameters:
**data**– The tensor to be sliced**begin**– 1D tensor with begin indexes for input blob slicing**end**– 1D tensor with end indexes for input blob slicing**strides**– The slicing strides**begin_mask**– A mask applied to the ‘begin’ input indicating which elements shoud be ignored**end_mask**– A mask applied to the ‘end’ input indicating which elements shoud be ignored**new_axis_mask**– A mask indicating dimensions where ‘1’ should be inserted**shrink_axis_mask**– A mask indicating which dimensions should be deleted**ellipsis_mask**– Indicates positions where missing dimensions should be inserted

- Returns:
StridedSlice node