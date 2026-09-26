source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset10.ctc_greedy_decoder_seq_len.html
lastmod: 

# openvino.runtime.opset10.ctc_greedy_decoder_seq_len[#](https://docs.openvino.ai#openvino-runtime-opset10-ctc-greedy-decoder-seq-len)

-
openvino.runtime.opset10.ctc_greedy_decoder_seq_len(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*sequence_length:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*blank_index:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray | None = None*merge_repeated: bool = True*,*classes_index_type: str = 'i32'*,*sequence_length_type: str = 'i32'*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset10.ctc_greedy_decoder_seq_len) Return a node which performs CTCGreedyDecoderSeqLen.

- Parameters:
**data**– The input 3D tensor. Shape: [batch_size, seq_length, num_classes]**sequence_length**– Input 1D tensor with sequence length. Shape: [batch_size]**blank_index**– Scalar or 1D tensor with specifies the class index to use for the blank class. Optional parameter. Default value is num_classes-1.

- Returns:
The new node which performs CTCGreedyDecoderSeqLen.