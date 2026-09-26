source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v3_1_1_embedding_bag_packed_sum.html
lastmod: 

# Class ov::op::v3::EmbeddingBagPackedSum[#](https://docs.openvino.ai#class-ov-op-v3-embeddingbagpackedsum)

-
class EmbeddingBagPackedSum : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[EmbeddingBagPackedBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_embedding_bag_packed_base.html#_CPPv4N2ov2op4util22EmbeddingBagPackedBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v321EmbeddingBagPackedSumE) Returns embeddings for given indices.

Public Functions

-
EmbeddingBagPackedSum() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v321EmbeddingBagPackedSum21EmbeddingBagPackedSumEv) Constructs a

[EmbeddingBagPackedSum](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_embedding_bag_packed_sum)operation.

-
EmbeddingBagPackedSum(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &emb_table, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &indices, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &per_sample_weights)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v321EmbeddingBagPackedSum21EmbeddingBagPackedSumERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) Constructs a

[EmbeddingBagPackedSum](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_embedding_bag_packed_sum)operation.[EmbeddingBagPackedSum](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_embedding_bag_packed_sum)constructs an output tensor by replacing every index in a given input tensor with a row (from the weights matrix) at that index- Parameters:
**emb_table**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)containing the embedding lookup table of the module of shape [num_emb, emb_dim1, emb_dim2, …] and of type T**indices**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)of shape`[batch, indices_per_bag]`

and of type*T_IND*. Required.**per_sample_weigths**– tensor of the same shape as indices and of type T. Each value in this tensor are multiplied with each value pooled from embedding table for each index. Optional.



-
EmbeddingBagPackedSum() = default