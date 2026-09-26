source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v3_1_1_embedding_bag_offsets_sum.html
lastmod: 

# Class ov::op::v3::EmbeddingBagOffsetsSum[#](https://docs.openvino.ai#class-ov-op-v3-embeddingbagoffsetssum)

-
class EmbeddingBagOffsetsSum : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[EmbeddingBagOffsetsBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_embedding_bag_offsets_base.html#_CPPv4N2ov2op4util23EmbeddingBagOffsetsBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v322EmbeddingBagOffsetsSumE) Returns embeddings for given indices.

Public Functions

-
EmbeddingBagOffsetsSum() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v322EmbeddingBagOffsetsSum22EmbeddingBagOffsetsSumEv) Constructs a

[EmbeddingBagOffsetsSum](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_embedding_bag_offsets_sum)operation.

-
EmbeddingBagOffsetsSum(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &emb_table, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &indices, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &offsets, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &default_index, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &per_sample_weights)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v322EmbeddingBagOffsetsSum22EmbeddingBagOffsetsSumERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) Constructs a

[EmbeddingBagOffsetsSum](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_embedding_bag_offsets_sum)operation.[EmbeddingBagOffsetsSum](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_embedding_bag_offsets_sum)constructs an output tensor by replacing every index in a given input tensor with a row (from the weights matrix) at that index- Parameters:
**emb_table**– tensor containing the embedding lookup table of the module of shape [num_emb, emb_dim1, emb_dim2, …] and of type T**indices**– tensor of shape [num_indices] and of type T_IND. Required**offsets**– tensor of shape [batch] and of type T_IND containing the starting index positions of each “bag” in indices. Required.**default_index**– scalar of type T_IND containing default index in embedding table to fill empty “bags”. If set to value -1 or not provided, empty “bags” are filled with zeros. Reverse indexing using negative values is not supported. Optional.**per_sample_weights**– tensor of the same shape as indices and of type T. Each value in this tensor are multiplied with each value pooled from embedding table for each index. Optional.



-
EmbeddingBagOffsetsSum() = default