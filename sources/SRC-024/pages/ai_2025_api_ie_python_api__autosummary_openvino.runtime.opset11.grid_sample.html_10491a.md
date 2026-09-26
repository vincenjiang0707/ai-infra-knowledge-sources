source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.grid_sample.html
lastmod: 

# openvino.runtime.opset11.grid_sample[#](https://docs.openvino.ai#openvino-runtime-opset11-grid-sample)

-
openvino.runtime.opset11.grid_sample(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*grid:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*attributes: dict*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.grid_sample) Return a node which performs GridSample operation.

- Parameters:
**data**– The input image.**grid**– Grid values (normalized input coordinates).**attributes**– A dictionary containing GridSample’s attributes.**name**– Optional name of the node.


Available attributes:

- align_corners A flag which specifies whether to align the grid extrema values
with the borders or center points of the input tensor’s border pixels. Range of values: true, false Default value: false Required: no


- mode Specifies the type of interpolation.
Range of values: bilinear, bicubic, nearest Default value: bilinear Required: no


- padding_mode Specifies how the out-of-bounds coordinates should be handled.
Range of values: zeros, border, reflection Default value: zeros Required: no



- Returns:
A new GridSample node.