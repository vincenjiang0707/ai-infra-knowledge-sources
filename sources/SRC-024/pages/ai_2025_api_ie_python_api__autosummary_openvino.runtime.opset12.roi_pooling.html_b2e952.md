source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset12.roi_pooling.html
lastmod: 

# openvino.runtime.opset12.roi_pooling[#](https://docs.openvino.ai#openvino-runtime-opset12-roi-pooling)

-
openvino.runtime.opset12.roi_pooling(
*input:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*coords:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*output_roi: list[int] | None = None*,*spatial_scale: int | float | ndarray | None = None*,*method: str = 'max'*,*name: str | None = None*,***,*output_size: list[int] | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset12.roi_pooling) Return a node which produces an ROIPooling operation.

- Parameters:
**input**– Input feature map {N, C, …}.**coords**– Coordinates of bounding boxes.**output_roi**– Height/Width of ROI output features (shape).**spatial_scale**– Ratio of input feature map over input image size (float).**method**– Method of pooling - string: “max” or “bilinear”. Default: “max”**output_size**– (DEPRECATED!) Height/Width of ROI output features (shape). Will override output_roi if used and change behavior of the operator.

- Returns:
ROIPooling node.