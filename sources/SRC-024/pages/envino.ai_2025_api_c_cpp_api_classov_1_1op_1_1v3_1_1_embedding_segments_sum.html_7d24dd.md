source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v3_1_1_embedding_segments_sum.html
lastmod: 

# Class ov::op::v3::EmbeddingSegmentsSum[#](https://docs.openvino.ai#class-ov-op-v3-embeddingsegmentssum)

-
class EmbeddingSegmentsSum : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v320EmbeddingSegmentsSumE) Returns embeddings for given indices.

Public Functions

-
EmbeddingSegmentsSum() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v320EmbeddingSegmentsSum20EmbeddingSegmentsSumEv) Constructs a

[EmbeddingSegmentsSum](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_embedding_segments_sum)operation.

-
EmbeddingSegmentsSum(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &emb_table, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &indices, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &segment_ids, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &num_segments, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &default_index, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &per_sample_weights)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v320EmbeddingSegmentsSum20EmbeddingSegmentsSumERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) Constructs a

[EmbeddingSegmentsSum](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_embedding_segments_sum)operation.[EmbeddingSegmentsSum](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_embedding_segments_sum)constructs an output tensor by replacing every index in a given input tensor with a row (from the weights matrix) at that index- Parameters:
**'emb_table'**– tensor containing the embedding lookup table of the module of shape [num_emb, emb_dim1, emb_dim2, …] and of type T**'indices'**– tensor of shape [num_indices] and of type T_IND. Required**<tt>segment_ids</tt>**– tensor of shape`[num_indices]`

and of type*T_IND*with indices into the output[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor). Values should be sorted and can be repeated. Required.**<tt>num_segments</tt>**– scalar of type*T_IND*indicating the number of segments. Required.**'default_index'**– scalar of type T_IND containing default index in embedding table to fill empty “bags”. If not provided empty “bags” are filled with zeros. Optional.**'per_sample_weights'**– tensor of the same shape as indices and of type T. Each value in this tensor are multiplied with each value pooled from embedding table for each index. Optional.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v320EmbeddingSegmentsSum24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
EmbeddingSegmentsSum() = default