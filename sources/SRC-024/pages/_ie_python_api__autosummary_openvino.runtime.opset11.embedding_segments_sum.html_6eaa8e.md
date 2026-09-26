source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.embedding_segments_sum.html
lastmod: 

# openvino.runtime.opset11.embedding_segments_sum[#](https://docs.openvino.ai#openvino-runtime-opset11-embedding-segments-sum)

-
openvino.runtime.opset11.embedding_segments_sum(
*emb_table:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*indices:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*segment_ids:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*num_segments:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray | None = None*default_index:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray | None = None*per_sample_weights:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray | None = None*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.embedding_segments_sum) Return an EmbeddingSegmentsSum node.

EmbeddingSegmentsSum constructs an output tensor by replacing every index in a given input tensor with a row (from the weights matrix) at that index

- Parameters:
**emb_table**– Tensor containing the embedding lookup table.**indices**– Tensor with indices.**segment_ids**– Tensor with indices into the output Tensor**num_segments**– Tensor with number of segments.**default_index**– Scalar containing default index in embedding table to fill empty bags.**per_sample_weights**– Weights to be multiplied with embedding table.**name**– Optional name for output node.

- Returns:
EmbeddingSegmentsSum node