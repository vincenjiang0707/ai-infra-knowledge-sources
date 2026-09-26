source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.proposal.html
lastmod: 

# openvino.runtime.opset11.proposal[#](https://docs.openvino.ai#openvino-runtime-opset11-proposal)

-
openvino.runtime.opset11.proposal(
*class_probs:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*bbox_deltas:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*image_shape:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*attrs: dict*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.proposal) Filter bounding boxes and outputs only those with the highest prediction confidence.

- Parameters:
**class_probs**– 4D input floating point tensor with class prediction scores.**bbox_deltas**– 4D input floating point tensor with corrected predictions of bounding boxes**image_shape**– The 1D input tensor with 3 or 4 elements describing image shape.**attrs**– The dictionary containing key, value pairs for attributes.**name**– Optional name for the output node.


- base_size The size of the anchor to which scale and ratio attributes are applied.
Range of values: a positive unsigned integer number Default value: None Required: yes


- pre_nms_topn The number of bounding boxes before the NMS operation.
Range of values: a positive unsigned integer number Default value: None Required: yes


- post_nms_topn The number of bounding boxes after the NMS operation.
Range of values: a positive unsigned integer number Default value: None Required: yes


- nms_thresh The minimum value of the proposal to be taken into consideration.
Range of values: a positive floating-point number Default value: None Required: yes


- feat_stride The step size to slide over boxes (in pixels).
Range of values: a positive unsigned integer Default value: None Required: yes


- min_size The minimum size of box to be taken into consideration.
Range of values: a positive unsigned integer number Default value: None Required: yes


- ratio The ratios for anchor generation.
Range of values: a list of floating-point numbers Default value: None Required: yes


- scale The scales for anchor generation.
Range of values: a list of floating-point numbers Default value: None Required: yes


- clip_before_nms The flag that specifies whether to perform clip bounding boxes before
non-maximum suppression or not. Range of values: True or False Default value: True Required: no


- clip_after_nms The flag that specifies whether to perform clip bounding boxes after
non-maximum suppression or not. Range of values: True or False Default value: False Required: no


- normalize The flag that specifies whether to perform normalization of output boxes to
[0,1] interval or not. Range of values: True or False Default value: False Required: no


- box_size_scale Specifies the scale factor applied to logits of box sizes before decoding.
Range of values: a positive floating-point number Default value: 1.0 Required: no


- box_coordinate_scale Specifies the scale factor applied to logits of box coordinates
before decoding. Range of values: a positive floating-point number Default value: 1.0 Required: no


- framework Specifies how the box coordinates are calculated.
- Range of values: “” (empty string) - calculate box coordinates like in Caffe*
- tensorflow - calculate box coordinates like in the TensorFlow*
Object Detection API models



Default value: “” (empty string) Required: no



Example of attribute dictionary:

# just required ones attrs = { 'base_size': 85, 'pre_nms_topn': 10, 'post_nms_topn': 20, 'nms_thresh': 0.34, 'feat_stride': 16, 'min_size': 32, 'ratio': [0.1, 1.5, 2.0, 2.5], 'scale': [2, 3, 3, 4], }

Optional attributes which are absent from dictionary will be set with corresponding default. :return: Node representing Proposal operation.