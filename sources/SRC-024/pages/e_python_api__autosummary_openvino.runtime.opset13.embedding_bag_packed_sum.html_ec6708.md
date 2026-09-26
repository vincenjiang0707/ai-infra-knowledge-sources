source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset13.embedding_bag_packed_sum.html
lastmod: 

# openvino.runtime.opset13.embedding_bag_packed_sum[#](https://docs.openvino.ai#openvino-runtime-opset13-embedding-bag-packed-sum)

-
openvino.runtime.opset13.embedding_bag_packed_sum(
*emb_table:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*indices:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*per_sample_weights:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray | None = None*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset13.embedding_bag_packed_sum) Return an EmbeddingBagPackedSum node.

EmbeddingSegmentsSum constructs an output tensor by replacing every index in a given input tensor with a row (from the weights matrix) at that index

- Parameters:
**emb_table**– Tensor containing the embedding lookup table.**indices**– Tensor with indices.**per_sample_weights**– Weights to be multiplied with embedding table.**name**– Optional name for output node.

- Returns:
EmbeddingBagPackedSum node