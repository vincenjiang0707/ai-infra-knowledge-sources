source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset10.prior_box_clustered.html
lastmod: 

# openvino.runtime.opset10.prior_box_clustered[#](https://docs.openvino.ai#openvino-runtime-opset10-prior-box-clustered)

-
openvino.runtime.opset10.prior_box_clustered(
*output_size:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*image_size:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*attrs: dict*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset10.prior_box_clustered) Generate prior boxes of specified sizes normalized to the input image size.

- Parameters:
**output_size**– 1D tensor with two integer elements [height, width]. Specifies the spatial size of generated grid with boxes.**image_size**– 1D tensor with two integer elements [image_height, image_width] that specifies shape of the image for which boxes are generated.**attrs**– The dictionary containing key, value pairs for attributes.**name**– Optional name for the output node.

- Returns:
Node representing PriorBoxClustered operation.

Available attributes are:


- widths Specifies desired boxes widths in pixels.
Range of values: floating point positive numbers. Default value: 1.0 Required: no


- heights Specifies desired boxes heights in pixels.
Range of values: floating point positive numbers. Default value: 1.0 Required: no


- clip The flag that denotes if each value in the output tensor should be clipped
within [0,1]. Range of values: {True, False} Default value: True Required: no


- step_widths The distance between box centers.
Range of values: floating point positive number Default value: 0.0 Required: no


- step_heights The distance between box centers.
Range of values: floating point positive number Default value: 0.0 Required: no


- offset The shift of box respectively to the top left corner.
Range of values: floating point positive number Default value: None Required: yes


- variance Denotes a variance of adjusting bounding boxes.
Range of values: floating point positive numbers Default value: [] Required: no



Example of attribute dictionary:

# just required ones attrs = { 'offset': 85, } attrs = { 'offset': 85, 'clip': False, 'step_widths': [1.5, 2.0, 2.5] }

Optional attributes which are absent from dictionary will be set with corresponding default.