source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/vocab_parallel_embedding/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.vocab_parallel_embedding`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding)

Classes:

-
–[ParallelLMHead](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.ParallelLMHead)Parallelized LM head.

-
–[UnquantizedEmbeddingMethod](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.UnquantizedEmbeddingMethod)Unquantized method for embeddings.

-
–[VocabParallelEmbedding](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.VocabParallelEmbedding)Embedding parallelized in the vocabulary dimension.

-
–[VocabParallelEmbeddingShardIndices](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.VocabParallelEmbeddingShardIndices)Indices for a shard of a vocab parallel embedding.


Functions:

-
–[pad_vocab_size](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.pad_vocab_size)Pad the vocab size to the given value.


##

`ParallelLMHead`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.ParallelLMHead)

Bases: [VocabParallelEmbedding](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.VocabParallelEmbedding)

Parallelized LM head.

Output logits weight matrices used in the Sampler. The weight and bias tensors are padded to make sure they are divisible by the number of model parallel GPUs.

Parameters:

-

(`num_embeddings`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.ParallelLMHead(num_embeddings))

) –[int](https://docs.python.org/3/builtins/functions.html#int)vocabulary size.

-

(`embedding_dim`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.ParallelLMHead(embedding_dim))

) –[int](https://docs.python.org/3/builtins/functions.html#int)size of hidden state.

-

(`bias`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.ParallelLMHead(bias))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –whether to use bias.

-

(`params_dtype`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.ParallelLMHead(params_dtype))

, default:[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)| None`None`

) –type of the parameters.

-

(`org_num_embeddings`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.ParallelLMHead(org_num_embeddings))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –original vocabulary size (without LoRA).

-

(`padding_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.ParallelLMHead(padding_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`DEFAULT_VOCAB_PADDING_SIZE`

) –padding size for the vocabulary.

-

(`disable_tp`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.ParallelLMHead(disable_tp))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –If true, tensor parallelism will be disabled for this layer.


Methods:

-
–[tie_weights](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.ParallelLMHead.tie_weights)Tie the weights with word embeddings.


## Source code in `vllm/model_executor/layers/vocab_parallel_embedding.py`


###

`tie_weights(embed_tokens)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.ParallelLMHead.tie_weights)

##

`UnquantizedEmbeddingMethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.UnquantizedEmbeddingMethod)

Bases: [QuantizeMethodBase](https://docs.vllm.ai/quantization/base_config/#vllm.model_executor.layers.quantization.base_config.QuantizeMethodBase)

Unquantized method for embeddings.

Methods:

-
–[create_weights](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.UnquantizedEmbeddingMethod.create_weights)Create weights for embedding layer.


## Source code in `vllm/model_executor/layers/vocab_parallel_embedding.py`


###

`create_weights(layer, input_size_per_partition, output_partition_sizes, input_size, output_size, params_dtype, **extra_weight_attrs)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.UnquantizedEmbeddingMethod.create_weights)

Create weights for embedding layer.

## Source code in `vllm/model_executor/layers/vocab_parallel_embedding.py`


##

`VocabParallelEmbedding`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.VocabParallelEmbedding)

Bases: [PluggableLayer](https://docs.vllm.ai/custom_op/#vllm.model_executor.custom_op.PluggableLayer)

Embedding parallelized in the vocabulary dimension.

Adapted from torch.nn.Embedding, note that we pad the vocabulary size to make sure it is divisible by the number of model parallel GPUs.

In order to support various loading methods, we ensure that LoRA-added embeddings are always at the end of TP-sharded tensors. In other words, we shard base embeddings and LoRA embeddings separately (both padded), and place them in the same tensor. In this example, we will have the original vocab size = 1010, added vocab size = 16 and padding to 64. Therefore, the total vocab size with padding will be 1088 (because we first pad 1010 to 1024, add 16, and then pad to 1088). Therefore, the tensor format looks like the following: TP1, rank 0 (no sharding): |< --------BASE-------- >|< -BASE PADDING-- >|< -----LORA------ >|< -LORA PADDING-- >| corresponding token_id: | 0 | 1 | ... | 1009 | -1 | ... | -1 | 1010 | ... | 1025 | -1 | ... | -1 | index: | 0 | 1 | ... | 1009 | 1010 | ... | 1023 | 1024 | ... | 1039 | 1040 | ... | 1087 |

TP2, rank 0: |< --------------------BASE--------------------- >|< -----LORA------ >|< -LORA PADDING- >| corresponding token_id: | 0 | 1 | 2 | ... | 497 | 498 | ... | 511 | 1010 | ... | 1025 | -1 | ... | -1 | index: | 0 | 1 | 2 | ... | 497 | 498 | ... | 511 | 512 | ... | 527 | 528 | ... | 543 | TP2, rank 1: |< -----------BASE----------- >|< -BASE PADDING- >|< -----------LORA PADDING----------- >| corresponding token_id: | 512 | 513 | 514 | ... | 1009 | -1 | ... | -1 | -1 | ... | -1 | -1 | ... | -1 | index: | 0 | 1 | 2 | ... | 497 | 498 | ... | 511 | 512 | ... | 527 | 528 | ... | 543 |

Parameters:

-

(`num_embeddings`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.VocabParallelEmbedding(num_embeddings))

) –[int](https://docs.python.org/3/builtins/functions.html#int)vocabulary size.

-

(`embedding_dim`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.VocabParallelEmbedding(embedding_dim))

) –[int](https://docs.python.org/3/builtins/functions.html#int)size of hidden state.

-

(`params_dtype`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.VocabParallelEmbedding(params_dtype))

, default:[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)| None`None`

) –type of the parameters.

-

(`org_num_embeddings`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.VocabParallelEmbedding(org_num_embeddings))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –original vocabulary size (without LoRA).

-

(`padding_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.VocabParallelEmbedding(padding_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`DEFAULT_VOCAB_PADDING_SIZE`

) –padding size for the vocabulary.

-

(`quant_config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.VocabParallelEmbedding(quant_config))

, default:[QuantizationConfig](https://docs.vllm.ai/quantization/base_config/#vllm.model_executor.layers.quantization.base_config.QuantizationConfig)| None`None`

) –quant config for the layer

-

(`prefix`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.VocabParallelEmbedding(prefix))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`''`

) –full name of the layer in the state dict

-

(`disable_tp`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.VocabParallelEmbedding(disable_tp))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –If true, tensor parallelism will be disabled for this layer.

-

(`quant_method`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.VocabParallelEmbedding(quant_method))

, default:[QuantizeMethodBase](https://docs.vllm.ai/quantization/base_config/#vllm.model_executor.layers.quantization.base_config.QuantizeMethodBase)| None`None`

) –Preselected quantization method for model-specific layers.

-

(`parallel_group`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.VocabParallelEmbedding(parallel_group))

, default:[GroupCoordinator](https://docs.vllm.ai/distributed/#vllm.distributed.GroupCoordinator)| None`None`

) –Process group used to shard and reduce the embedding.


Methods:

-
–[get_sharded_to_full_mapping](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.VocabParallelEmbedding.get_sharded_to_full_mapping)Get a mapping that can be used to reindex the gathered


## Source code in `vllm/model_executor/layers/vocab_parallel_embedding.py`


|
|

###

`_get_indices(vocab_size_padded, org_vocab_size_padded, vocab_size, org_vocab_size, tp_rank, tp_size)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.VocabParallelEmbedding._get_indices)

Get start and end indices for vocab parallel embedding, following the layout outlined in the class docstring, based on the given tp_rank and tp_size.

## Source code in `vllm/model_executor/layers/vocab_parallel_embedding.py`


###

`get_sharded_to_full_mapping()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.VocabParallelEmbedding.get_sharded_to_full_mapping)

Get a mapping that can be used to reindex the gathered logits for sampling.

During sampling, we gather logits from all ranks. The relationship of index->token_id will follow the same format as outlined in the class docstring. However, after the gather, we want to reindex the final logits tensor to map index->token_id one-to-one (the index is always equal the token_id it corresponds to). The indices returned by this method allow us to do that.

## Source code in `vllm/model_executor/layers/vocab_parallel_embedding.py`


##

`VocabParallelEmbeddingShardIndices`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.VocabParallelEmbeddingShardIndices)

Indices for a shard of a vocab parallel embedding.

## Source code in `vllm/model_executor/layers/vocab_parallel_embedding.py`


##

`pad_vocab_size(vocab_size, pad_to=DEFAULT_VOCAB_PADDING_SIZE)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.vocab_parallel_embedding.pad_vocab_size)

Pad the vocab size to the given value.