source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v15_1_1_embedding_bag_offsets.html
lastmod: 

# Class ov::op::v15::EmbeddingBagOffsets[#](https://docs.openvino.ai#class-ov-op-v15-embeddingbagoffsets)

-
class EmbeddingBagOffsets : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[EmbeddingBagOffsetsBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_embedding_bag_offsets_base.html#_CPPv4N2ov2op4util23EmbeddingBagOffsetsBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1519EmbeddingBagOffsetsE) Returns embeddings for given indices.

Public Functions

-
EmbeddingBagOffsets() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1519EmbeddingBagOffsets19EmbeddingBagOffsetsEv) Constructs a

[EmbeddingBagOffsets](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_embedding_bag_offsets)operation.

-
EmbeddingBagOffsets(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &emb_table, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &indices, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &offsets, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &default_index, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &per_sample_weights, const Reduction &reduction = Reduction::SUM)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1519EmbeddingBagOffsets19EmbeddingBagOffsetsERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK9Reduction) Constructs a

[EmbeddingBagOffsets](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_embedding_bag_offsets)operation.[EmbeddingBagOffsets](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_embedding_bag_offsets)constructs an output tensor by replacing every index in a given input tensor with a row (from the weights matrix) at that index- Parameters:
**emb_table**– tensor containing the embedding lookup table of the module of shape [num_emb, emb_dim1, emb_dim2, …] and of type T**indices**– tensor of shape [num_indices] and of type T_IND. Required**offsets**– tensor of shape [batch] and of type T_IND containing the starting index positions of each “bag” in indices. Required.**default_index**– scalar of type T_IND containing default index in embedding table to fill empty “bags”. If set to value -1 or not provided, empty “bags” are filled with zeros. Reverse indexing using negative values is not supported. Optional.**per_sample_weights**– tensor of the same shape as indices and of type T. Each value in this tensor are multiplied with each value pooled from embedding table for each index. Optional.**reduction**– enum to select algorithm used to perform reduction of elements in bag. Optional.



-
EmbeddingBagOffsets() = default