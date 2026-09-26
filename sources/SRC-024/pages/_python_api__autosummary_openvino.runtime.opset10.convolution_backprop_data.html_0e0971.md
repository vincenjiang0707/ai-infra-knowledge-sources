source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset10.convolution_backprop_data.html
lastmod: 

# openvino.runtime.opset10.convolution_backprop_data[#](https://docs.openvino.ai#openvino-runtime-opset10-convolution-backprop-data)

-
openvino.runtime.opset10.convolution_backprop_data(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*filters:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*strides: list[int]*,*output_shape:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray | None = None*pads_begin: list[int] | None = None*,*pads_end: list[int] | None = None*,*dilations: list[int] | None = None*,*auto_pad: str | None = None*,*output_padding: list[int] | None = None*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset10.convolution_backprop_data) Create node performing a batched-convolution backprop data operation.

- Parameters:
**data**– The node producing data from forward-prop**filters**– The node producing the filters from forward-prop.**output_shape**– The node producing output delta.**strides**– The distance (in pixels) to slide the filter on the feature map over the axes.**pads_begin**– The number of pixels to add to the beginning along each axis.**pads_end**– The number of pixels to add to the end along each axis.**dilations**– The distance in width and height between elements (weights) in the filter.**name**– The node name.

- Returns:
The node object representing ConvolutionBackpropData operation.