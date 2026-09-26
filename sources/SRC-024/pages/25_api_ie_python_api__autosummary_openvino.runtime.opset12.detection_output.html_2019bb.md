source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset12.detection_output.html
lastmod: 

# openvino.runtime.opset12.detection_output[#](https://docs.openvino.ai#openvino-runtime-opset12-detection-output)

-
openvino.runtime.opset12.detection_output(
*box_logits:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*class_preds:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*proposals:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*attrs: dict*,*aux_class_preds:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray | None = None*aux_box_preds:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray | None = None*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset12.detection_output) Generate the detection output using information on location and confidence predictions.

- Parameters:
**box_logits**– The 2D input tensor with box logits.**class_preds**– The 2D input tensor with class predictions.**proposals**– The 3D input tensor with proposals.**attrs**– The dictionary containing key, value pairs for attributes.**aux_class_preds**– The 2D input tensor with additional class predictions information.**aux_box_preds**– The 2D input tensor with additional box predictions information.**name**– Optional name for the output node.

- Returns:
Node representing DetectionOutput operation. Available attributes are:


- background_label_id The background label id.
Range of values: integer value Default value: 0 Required: no


- top_k Maximum number of results to be kept per batch after NMS step.
Range of values: integer value Default value: -1 Required: no


- variance_encoded_in_target The flag that denotes if variance is encoded in target.
Range of values: {False, True} Default value: False Required: no


- keep_top_k Maximum number of bounding boxes per batch to be kept after NMS step.
Range of values: integer values Default value: None Required: yes


- code_type The type of coding method for bounding boxes.
- Range of values: {‘caffe.PriorBoxParameter.CENTER_SIZE’,
‘caffe.PriorBoxParameter.CORNER’}


Default value: ‘caffe.PriorBoxParameter.CORNER’ Required: no


- share_location The flag that denotes if bounding boxes are shared among different
classes. Range of values: {True, False} Default value: True Required: no


- nms_threshold The threshold to be used in the NMS stage.
Range of values: floating point value Default value: None Required: yes


- confidence_threshold Specifies the minimum confidence threshold for detection boxes to be
considered. Range of values: floating point value Default value: 0 Required: no


- clip_after_nms The flag that denotes whether to perform clip bounding boxes after
non-maximum suppression or not. Range of values: {True, False} Default value: False Required: no


- clip_before_nms The flag that denotes whether to perform clip bounding boxes before
non-maximum suppression or not. Range of values: {True, False} Default value: False Required: no


- decrease_label_id The flag that denotes how to perform NMS.
- Range of values: False - perform NMS like in Caffe*.
True - perform NMS like in MxNet*.


Default value: False Required: no


- normalized The flag that denotes whether input tensors with boxes are normalized.
Range of values: {True, False} Default value: False Required: no


- input_height The input image height.
Range of values: positive integer number Default value: 1 Required: no


- input_width The input image width.
Range of values: positive integer number Default value: 1 Required: no


- objectness_score The threshold to sort out confidence predictions.
Range of values: non-negative float number Default value: 0 Required: no



Example of attribute dictionary:

# just required ones attrs = { 'keep_top_k': [1, 2, 3], 'nms_threshold': 0.645, } attrs = { 'keep_top_k': [1, 2, 3], 'nms_threshold': 0.645, 'normalized': True, 'clip_before_nms': True, 'input_height': [32], 'input_width': [32], }

Optional attributes which are absent from dictionary will be set with corresponding default.