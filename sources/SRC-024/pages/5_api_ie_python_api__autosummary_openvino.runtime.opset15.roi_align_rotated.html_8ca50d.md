source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset15.roi_align_rotated.html
lastmod: 

# openvino.runtime.opset15.roi_align_rotated[#](https://docs.openvino.ai#openvino-runtime-opset15-roi-align-rotated)

-
openvino.runtime.opset15.roi_align_rotated(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*rois:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*batch_indices:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*pooled_h: int*,*pooled_w: int*,*sampling_ratio: int*,*spatial_scale: float*,*clockwise_mode: bool*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset15.roi_align_rotated) Return a node which performs ROIAlignRotated operation.

- Parameters:
**data**– Input data.**rois**– RoIs (Regions of Interest) to pool over.**batch_indices**– Tensor with each element denoting the index of the corresponding image in the batch.**pooled_h**– Height of the ROI output feature map.**pooled_w**– Width of the ROI output feature map.**sampling_ratio**– Number of bins over height and width to use to calculate each output feature map element.**spatial_scale**– Multiplicative spatial scale factor to translate ROI coordinates.**clockwise_mode**– If true, rotation angle is interpreted as clockwise, otherwise as counterclockwise**name**– The optional name for the output node

- Returns:
The new node which performs ROIAlignRotated