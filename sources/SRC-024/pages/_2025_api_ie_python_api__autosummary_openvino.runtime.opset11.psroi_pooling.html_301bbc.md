source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.psroi_pooling.html
lastmod: 

# openvino.runtime.opset11.psroi_pooling[#](https://docs.openvino.ai#openvino-runtime-opset11-psroi-pooling)

-
openvino.runtime.opset11.psroi_pooling(
*input:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*coords:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*output_dim: int*,*group_size: int*,*spatial_scale: float*,*spatial_bins_x: int*,*spatial_bins_y: int*,*mode: str*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.psroi_pooling) Return a node which produces a PSROIPooling operation.

- Parameters:
**input**– Input feature map {N, C, …}.**coords**– Coordinates of bounding boxes.**output_dim**– Output channel number.**group_size**– Number of groups to encode position-sensitive scores.**spatial_scale**– Ratio of input feature map over input image size.**spatial_bins_x**– Numbers of bins to divide the input feature maps over.**spatial_bins_y**– Numbers of bins to divide the input feature maps over.**mode**– Mode of pooling - “avg” or “bilinear”.

- Returns:
PSROIPooling node