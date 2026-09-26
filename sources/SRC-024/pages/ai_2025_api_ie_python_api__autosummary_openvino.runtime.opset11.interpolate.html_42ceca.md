source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.interpolate.html
lastmod: 

# openvino.runtime.opset11.interpolate[#](https://docs.openvino.ai#openvino-runtime-opset11-interpolate)

-
openvino.runtime.opset11.interpolate(
*image:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*scales_or_sizes:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*mode: str*,*shape_calculation_mode: str*,*pads_begin: list[int] | None = None*,*pads_end: list[int] | None = None*,*coordinate_transformation_mode: str = 'half_pixel'*,*nearest_mode: str = 'round_prefer_floor'*,*antialias: bool = False*,*cube_coeff: float = -0.75*,*axes:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray | None = None*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.interpolate) Perfors the interpolation of the input tensor.

- Parameters:
**image**– The node providing input tensor with data for interpolation.**scales_or_sizes**– 1D tensor providing information used to calculate the output shape of the operation. It might contain floats (scales) or integers(sizes).**mode**– Specifies type of interpolation. Possible values are: nearest, linear, linear_onnx, cubic, bilinear_pillow, bicubic_pillow.**shape_calculation_mode**– Specifies how the scales_or_sizes input should be interpreted.**pads_begin**– Specifies the number of pixels to add to the beginning of the image being interpolated. Default is None.**pads_end**– Specifies the number of pixels to add to the end of the image being interpolated. Default is None.**coordinate_transformation_mode**– Specifies how to transform the coordinate in the resized tensor to the coordinate in the original tensor. Default is “half_pixel”.**nearest_mode**– Specifies round mode when mode == nearest and is used only when mode == nearest. Default is “round_prefer_floor”.**antialias**– Specifies whether to perform anti-aliasing. Default is False.**cube_coeff**– Specifies the parameter a for cubic interpolation. Default is -0.75.**axes**– 1D tensor specifying dimension indices where interpolation is applied. The default is None.**name**– Optional name for the output node. The default is None.

- Returns:
Node representing the interpolation operation.