source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset15.generate_proposals.html
lastmod: 

# openvino.runtime.opset15.generate_proposals[#](https://docs.openvino.ai#openvino-runtime-opset15-generate-proposals)

-
openvino.runtime.opset15.generate_proposals(
*im_info:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*anchors:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*deltas:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*scores:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*min_size: float*,*nms_threshold: float*,*pre_nms_count: int*,*post_nms_count: int*,*normalized: bool = True*,*nms_eta: float = 1.0*,*roi_num_type: str = 'i64'*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset15.generate_proposals) Return a node which performs GenerateProposals operation.

- Parameters:
**im_info**– Input with image info.**anchors**– Input anchors.**deltas**– Input deltas.**scores**– Input scores.**min_size**– Specifies minimum box width and height.**nms_threshold**– Specifies threshold to be used in the NMS stage.**pre_nms_count**– Specifies number of top-n proposals before NMS.**post_nms_count**– Specifies number of top-n proposals after NMS.**normalized**– Specifies whether proposal bboxes are normalized or not. Optional attribute, default value is True.**nms_eta**– Specifies eta parameter for adaptive NMS., must be in range [0.0, 1.0]. Optional attribute, default value is 1.0.**roi_num_type**– Specifies the element type of the third output rpnroisnum. Optional attribute, range of values: i64 (default) or i32.**name**– The optional name for the output node.

- Returns:
New node performing GenerateProposals operation.