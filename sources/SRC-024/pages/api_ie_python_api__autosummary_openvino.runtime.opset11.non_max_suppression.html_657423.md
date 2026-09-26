source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.non_max_suppression.html
lastmod: 

# openvino.runtime.opset11.non_max_suppression[#](https://docs.openvino.ai#openvino-runtime-opset11-non-max-suppression)

-
openvino.runtime.opset11.non_max_suppression(
*boxes:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*scores:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*max_output_boxes_per_class:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray | None = None*iou_threshold:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray | None = None*score_threshold:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray | None = None*soft_nms_sigma:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray | None = None*box_encoding: str = 'corner'*,*sort_result_descending: bool = True*,*output_type: str = 'i64'*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.non_max_suppression) Return a node which performs NonMaxSuppression.

- Parameters:
**boxes**– Tensor with box coordinates.**scores**– Tensor with box scores.**max_output_boxes_per_class**– Tensor Specifying maximum number of boxes to be selected per class.**iou_threshold**– Tensor specifying intersection over union threshold**score_threshold**– Tensor specifying minimum score to consider box for the processing.**soft_nms_sigma**– Tensor specifying the sigma parameter for Soft-NMS.**box_encoding**– Format of boxes data encoding.**sort_result_descending**– Flag that specifies whenever it is necessary to sort selected boxes across batches or not.**output_type**– Output element type.

- Returns:
The new node which performs NonMaxSuppression