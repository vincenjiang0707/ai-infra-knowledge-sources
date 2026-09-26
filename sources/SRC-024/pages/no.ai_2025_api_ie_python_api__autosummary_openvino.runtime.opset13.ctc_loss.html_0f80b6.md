source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset13.ctc_loss.html
lastmod: 

# openvino.runtime.opset13.ctc_loss[#](https://docs.openvino.ai#openvino-runtime-opset13-ctc-loss)

-
openvino.runtime.opset13.ctc_loss(
*logits:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*logit_length:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*labels:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*label_length:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*blank_index:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray | None = None*preprocess_collapse_repeated: bool = False*,*ctc_merge_repeated: bool = True*,*unique: bool = False*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset13.ctc_loss) Return a node which performs CTCLoss.

- Parameters:
**logits**– 3-D tensor of logits.**logit_length**– 1-D tensor of lengths for each object from a batch.**labels**– 2-D tensor of labels for which likelihood is estimated using logits.**label_length**– 1-D tensor of length for each label sequence.**blank_index**– Scalar used to mark a blank index.**preprocess_collapse_repeated**– Flag for preprocessing labels before loss calculation.**ctc_merge_repeated**– Flag for merging repeated characters in a potential alignment.**unique**– Flag to find unique elements in a target.

- Returns:
The new node which performs CTCLoss