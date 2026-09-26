source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset1.prior_box.html
lastmod: 

# openvino.runtime.opset1.prior_box[#](https://docs.openvino.ai#openvino-runtime-opset1-prior-box)

-
openvino.runtime.opset1.prior_box(
*layer_shape:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*image_shape:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*attrs: dict*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset1.prior_box) Generate prior boxes of specified sizes and aspect ratios across all dimensions.

- Parameters:
**layer_shape**– Shape of layer for which prior boxes are computed.**image_shape**– Shape of image to which prior boxes are scaled.**attrs**– The dictionary containing key, value pairs for attributes.**name**– Optional name for the output node.

- Returns:
Node representing prior box operation.


Available attributes are:

- min_size The minimum box size (in pixels).
Range of values: positive floating point numbers Default value: [] Required: no


- max_size The maximum box size (in pixels).
Range of values: positive floating point numbers Default value: [] Required: no


- aspect_ratio Aspect ratios of prior boxes.
Range of values: set of positive floating point numbers Default value: [] Required: no


- flip The flag that denotes that each aspect_ratio is duplicated and flipped.
Range of values: {True, False} Default value: False Required: no


- clip The flag that denotes if each value in the output tensor should be clipped
to [0,1] interval. Range of values: {True, False} Default value: False Required: no


- step The distance between box centers.
Range of values: floating point non-negative number Default value: 0 Required: no


- offset This is a shift of box respectively to top left corner.
Range of values: floating point non-negative number Default value: None Required: yes


- variance The variance denotes a variance of adjusting bounding boxes. The attribute
could contain 0, 1 or 4 elements. Range of values: floating point positive numbers Default value: [] Required: no


- scale_all_sizes The flag that denotes type of inference.
- Range of values: False - max_size is ignored
True - max_size is used


Default value: True Required: no


- fixed_ratio This is an aspect ratio of a box.
Range of values: a list of positive floating-point numbers Default value: None Required: no


- fixed_size This is an initial box size (in pixels).
Range of values: a list of positive floating-point numbers Default value: None Required: no


- density This is the square root of the number of boxes of each type.
Range of values: a list of positive floating-point numbers Default value: None Required: no



Example of attribute dictionary:

# just required ones attrs = { 'offset': 85, } attrs = { 'offset': 85, 'flip': True, 'clip': True, 'fixed_size': [32, 64, 128] }

Optional attributes which are absent from dictionary will be set with corresponding default.