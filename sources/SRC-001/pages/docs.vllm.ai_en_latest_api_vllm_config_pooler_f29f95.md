source: https://docs.vllm.ai/en/latest/api/vllm/config/pooler/
lastmod: 2026-09-24

#

`vllm.config.pooler`

[¶](https://docs.vllm.ai#vllm.config.pooler)

Classes:

-
–[PoolerConfig](https://docs.vllm.ai#vllm.config.pooler.PoolerConfig)Controls the behavior of output pooling in pooling models.


##

`PoolerConfig`

[¶](https://docs.vllm.ai#vllm.config.pooler.PoolerConfig)

Controls the behavior of output pooling in pooling models.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.pooler.PoolerConfig.compute_hash)WARNING: Whenever a new field is added to this config,


Attributes:

-
([dimensions](https://docs.vllm.ai#vllm.config.pooler.PoolerConfig.dimensions)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneReduce the dimensions of embeddings if model

-
([enable_chunked_processing](https://docs.vllm.ai#vllm.config.pooler.PoolerConfig.enable_chunked_processing)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to enable chunked processing for long inputs that exceed the model's

-
([logit_mean](https://docs.vllm.ai#vllm.config.pooler.PoolerConfig.logit_mean)

) –[float](https://docs.python.org/3/builtins/functions.html#float)| NoneIf provided, subtract this value from classification logits before

-
([logit_sigma](https://docs.vllm.ai#vllm.config.pooler.PoolerConfig.logit_sigma)

) –[float](https://docs.python.org/3/builtins/functions.html#float)| NoneIf provided, divide the classification logits by this value after

-
([max_embed_len](https://docs.vllm.ai#vllm.config.pooler.PoolerConfig.max_embed_len)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneMaximum input length allowed for embedding generation. When set, allows

-
([pooling_type](https://docs.vllm.ai#vllm.config.pooler.PoolerConfig.pooling_type)`SequencePoolingType | TokenPoolingType | None`

) –The pooling method used for pooling.

-
([returned_token_ids](https://docs.vllm.ai#vllm.config.pooler.PoolerConfig.returned_token_ids)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | NoneA list of indices for the vocabulary dimensions to be extracted,

-
([seq_pooling_type](https://docs.vllm.ai#vllm.config.pooler.PoolerConfig.seq_pooling_type)`SequencePoolingType | None`

) –The pooling method used for sequence pooling.

-
([step_tag_id](https://docs.vllm.ai#vllm.config.pooler.PoolerConfig.step_tag_id)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneIf set, only the score corresponding to the

`step_tag_id`

in the -
([task](https://docs.vllm.ai#vllm.config.pooler.PoolerConfig.task)`PoolingTask | None`

) –The task used for pooling.

-
([tok_pooling_type](https://docs.vllm.ai#vllm.config.pooler.PoolerConfig.tok_pooling_type)`TokenPoolingType | None`

) –The pooling method used for tokenwise pooling.

-
([use_activation](https://docs.vllm.ai#vllm.config.pooler.PoolerConfig.use_activation)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)| NoneWhether to apply activation function to the pooler outputs.


## Source code in `vllm/config/pooler.py`


|
|

###

`dimensions = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.pooler.PoolerConfig.dimensions)

Reduce the dimensions of embeddings if model support matryoshka representation. Defaults to None.

###

`enable_chunked_processing = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.pooler.PoolerConfig.enable_chunked_processing)

Whether to enable chunked processing for long inputs that exceed the model's maximum position embeddings. When enabled, long inputs will be split into chunks, processed separately, and then aggregated using weighted averaging. This allows embedding models to handle arbitrarily long text without CUDA errors. Defaults to False.

###

`logit_mean = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.pooler.PoolerConfig.logit_mean)

If provided, subtract this value from classification logits before activation. Used for affine score calibration (Platt scaling): activation((logit - logit_mean) / logit_sigma). Defaults to None.

###

`logit_sigma = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.pooler.PoolerConfig.logit_sigma)

If provided, divide the classification logits by this value after mean subtraction. Used for affine score calibration (Platt scaling): activation((logit - logit_mean) / logit_sigma). Defaults to None.

###

`max_embed_len = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.pooler.PoolerConfig.max_embed_len)

Maximum input length allowed for embedding generation. When set, allows inputs longer than max_embed_len to be accepted for embedding models. When an input exceeds max_embed_len, it will be handled according to the original max_model_len validation logic. Defaults to None (i.e. set to max_model_len).

###

`pooling_type = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.pooler.PoolerConfig.pooling_type)

The pooling method used for pooling.

If set, `seq_pooling_type`

or `tok_pooling_type`

are automatically populated with this field. Alternatively, users can set `seq_pooling_type`

and `tok_pooling_type`

explicitly.

This field is mainly for user convenience. Internal code should always use `seq_pooling_type`

or `tok_pooling_type`

instead of `pooling_type`

.

###

`returned_token_ids = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.pooler.PoolerConfig.returned_token_ids)

A list of indices for the vocabulary dimensions to be extracted, such as the token IDs of `good_token`

and `bad_token`

in the `math-shepherd-mistral-7b-prm`

model.

###

`seq_pooling_type = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.pooler.PoolerConfig.seq_pooling_type)

The pooling method used for sequence pooling.

###

`step_tag_id = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.pooler.PoolerConfig.step_tag_id)

If set, only the score corresponding to the `step_tag_id`

in the generated sentence should be returned. Otherwise, the scores for all tokens are returned.

###

`task = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.pooler.PoolerConfig.task)

The task used for pooling.

###

`tok_pooling_type = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.pooler.PoolerConfig.tok_pooling_type)

The pooling method used for tokenwise pooling.

###

`use_activation = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.pooler.PoolerConfig.use_activation)

Whether to apply activation function to the pooler outputs. `None`

uses the pooler's default, which is `True`

in most cases.

###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.pooler.PoolerConfig.compute_hash)

WARNING: Whenever a new field is added to this config, ensure that it is included in the factors list if it affects the computation graph.

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.