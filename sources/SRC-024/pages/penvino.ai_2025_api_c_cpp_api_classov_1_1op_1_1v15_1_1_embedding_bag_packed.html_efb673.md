source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v15_1_1_embedding_bag_packed.html
lastmod: 

# Class ov::op::v15::EmbeddingBagPacked[#](https://docs.openvino.ai#class-ov-op-v15-embeddingbagpacked)

-
class EmbeddingBagPacked : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[EmbeddingBagPackedBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_embedding_bag_packed_base.html#_CPPv4N2ov2op4util22EmbeddingBagPackedBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1518EmbeddingBagPackedE) Returns embeddings for given indices.

Public Functions

-
EmbeddingBagPacked() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1518EmbeddingBagPacked18EmbeddingBagPackedEv) Constructs a

[EmbeddingBagPacked](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_embedding_bag_packed)operation.

-
EmbeddingBagPacked(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &emb_table, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &indices, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &per_sample_weights, const Reduction &reduction = Reduction::SUM)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1518EmbeddingBagPacked18EmbeddingBagPackedERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK9Reduction) Constructs a

[EmbeddingBagPacked](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_embedding_bag_packed)operation.[EmbeddingBagPacked](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_embedding_bag_packed)constructs an output tensor by replacing every index in a given input tensor with a row (from the weights matrix) at that index- Parameters:
**emb_table**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)containing the embedding lookup table of the module of shape [num_emb, emb_dim1, emb_dim2, …] and of type T**indices**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)of shape`[batch, indices_per_bag]`

and of type*T_IND*. Required.**per_sample_weights**– tensor of the same shape as indices and of type T. Each value in this tensor are multiplied with each value pooled from embedding table for each index. Optional.**reduction**– enum to select algorithm used to perform reduction of elements in bag. Optional.



-
EmbeddingBagPacked() = default