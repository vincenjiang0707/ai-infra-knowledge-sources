source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset13.embedding_bag_offsets_sum.html
lastmod: 

# openvino.runtime.opset13.embedding_bag_offsets_sum[#](https://docs.openvino.ai#openvino-runtime-opset13-embedding-bag-offsets-sum)

-
openvino.runtime.opset13.embedding_bag_offsets_sum(
*emb_table:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*indices:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*offsets:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*default_index:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray | None = None*per_sample_weights:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray | None = None*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset13.embedding_bag_offsets_sum) Return a node which performs sums of bags of embeddings without the intermediate embeddings.

- Parameters:
**emb_table**– Tensor containing the embedding lookup table.**indices**– Tensor with indices.**offsets**– Tensor containing the starting index positions of each bag in indices.**per_sample_weights**– Tensor with weights for each sample.**default_index**– Scalar containing default index in embedding table to fill empty bags.**name**– Optional name for output node.

- Returns:
The new node which performs EmbeddingBagOffsetsSum