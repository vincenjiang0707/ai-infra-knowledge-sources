source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset1.ctc_greedy_decoder.html
lastmod: 

# openvino.runtime.opset1.ctc_greedy_decoder[#](https://docs.openvino.ai#openvino-runtime-opset1-ctc-greedy-decoder)

-
openvino.runtime.opset1.ctc_greedy_decoder(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*sequence_mask:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*merge_repeated: bool = True*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset1.ctc_greedy_decoder) Perform greedy decoding on the logits given in input (best path).

- Parameters:
**data**– Logits on which greedy decoding is performed.**sequence_mask**– The tensor with sequence masks for each sequence in the batch.**merge_repeated**– The flag for merging repeated labels during the CTC calculation.**name**– Optional name for output node.

- Returns:
The new node performing an CTCGreedyDecoder operation on input tensor.