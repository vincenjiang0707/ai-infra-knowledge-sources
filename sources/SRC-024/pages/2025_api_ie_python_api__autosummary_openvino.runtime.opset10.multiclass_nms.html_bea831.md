source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset10.multiclass_nms.html
lastmod: 

# openvino.runtime.opset10.multiclass_nms[#](https://docs.openvino.ai#openvino-runtime-opset10-multiclass-nms)

-
openvino.runtime.opset10.multiclass_nms(
*boxes:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*scores:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*roisnum:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray | None = None*sort_result_type: str | None = 'none'*,*sort_result_across_batch: bool | None = False*,*output_type: str | None = 'i64'*,*iou_threshold: float | None = 0.0*,*score_threshold: float | None = 0.0*,*nms_top_k: int | None = -1*,*keep_top_k: int | None = -1*,*background_class: int | None = -1*,*nms_eta: float | None = 1.0*,*normalized: bool | None = True*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset10.multiclass_nms) Return a node which performs MulticlassNms.

- Parameters:
**boxes**– Tensor with box coordinates.**scores**– Tensor with box scores.**roisnum**– Tensor with roisnum. Specifies the number of rois in each image. Required when ‘scores’ is a 2-dimensional tensor.**sort_result_type**– Specifies order of output elements, possible values: ‘class’: sort selected boxes by class id (ascending) ‘score’: sort selected boxes by score (descending) ‘none’: do not guarantee the order.**sort_result_across_batch**– Specifies whenever it is necessary to sort selected boxes across batches or not**output_type**– Specifies the output tensor type, possible values: ‘i64’, ‘i32’**iou_threshold**– Specifies intersection over union threshold**score_threshold**– Specifies minimum score to consider box for the processing**nms_top_k**– Specifies maximum number of boxes to be selected per class, -1 meaning to keep all boxes**keep_top_k**– Specifies maximum number of boxes to be selected per batch element, -1 meaning to keep all boxes**background_class**– Specifies the background class id, -1 meaning to keep all classes**nms_eta**– Specifies eta parameter for adpative NMS, in close range [0, 1.0]**normalized**– Specifies whether boxes are normalized or not**name**– The optional name for the output node

- Returns:
The new node which performs MuticlassNms