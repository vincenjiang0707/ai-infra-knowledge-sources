source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/interfaces_base/
lastmod: 2026-09-24

#

`vllm.model_executor.models.interfaces_base`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces_base)

Classes:

-
–[VllmModel](https://docs.vllm.ai#vllm.model_executor.models.interfaces_base.VllmModel)The interface required for all models in vLLM.

-
–[VllmModelForPooling](https://docs.vllm.ai#vllm.model_executor.models.interfaces_base.VllmModelForPooling)The interface required for all pooling models in vLLM.

-
–[VllmModelForTextGeneration](https://docs.vllm.ai#vllm.model_executor.models.interfaces_base.VllmModelForTextGeneration)The interface required for all generative models in vLLM.


Functions:

-
–[attn_type](https://docs.vllm.ai#vllm.model_executor.models.interfaces_base.attn_type)Decorator to set

`VllmModelForPooling.attn_type`

. -
–[default_pooling_type](https://docs.vllm.ai#vllm.model_executor.models.interfaces_base.default_pooling_type)Decorator to set

`VllmModelForPooling.default_*_pooling_type`

.

##

`VllmModel`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces_base.VllmModel)

Bases: [Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)[T_co]

The interface required for all models in vLLM.

Methods:

-
–[embed_input_ids](https://docs.vllm.ai#vllm.model_executor.models.interfaces_base.VllmModel.embed_input_ids)Apply token embeddings to

`input_ids`

.

## Source code in `vllm/model_executor/models/interfaces_base.py`


##

`VllmModelForPooling`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces_base.VllmModelForPooling)

Bases:

, [VllmModel](https://docs.vllm.ai#vllm.model_executor.models.interfaces_base.VllmModel)[T_co][Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)[T_co]

The interface required for all pooling models in vLLM.

Attributes:

-
([attn_type](https://docs.vllm.ai#vllm.model_executor.models.interfaces_base.VllmModelForPooling.attn_type)`AttnTypeStr`

) –Indicates the

-
([default_seq_pooling_type](https://docs.vllm.ai#vllm.model_executor.models.interfaces_base.VllmModelForPooling.default_seq_pooling_type)`SequencePoolingType`

) –Indicates the

[vllm.config.pooler.PoolerConfig.seq_pooling_type](https://docs.vllm.ai/config/pooler/#vllm.config.pooler.PoolerConfig.seq_pooling_type) -
([default_tok_pooling_type](https://docs.vllm.ai#vllm.model_executor.models.interfaces_base.VllmModelForPooling.default_tok_pooling_type)`TokenPoolingType`

) –Indicates the

[vllm.config.pooler.PoolerConfig.tok_pooling_type](https://docs.vllm.ai/config/pooler/#vllm.config.pooler.PoolerConfig.tok_pooling_type) -
([is_pooling_model](https://docs.vllm.ai#vllm.model_executor.models.interfaces_base.VllmModelForPooling.is_pooling_model)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)[True]A flag that indicates this model supports pooling.

-
([pooler](https://docs.vllm.ai#vllm.model_executor.models.interfaces_base.VllmModelForPooling.pooler)

) –[Pooler](https://docs.vllm.ai/layers/pooler/#vllm.model_executor.layers.pooler.Pooler)The pooler is only called on TP rank 0.

-
([score_type](https://docs.vllm.ai#vllm.model_executor.models.interfaces_base.VllmModelForPooling.score_type)`ScoreType`

) –Indicates the


## Source code in `vllm/model_executor/models/interfaces_base.py`


###

`attn_type = 'decoder'`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces_base.VllmModelForPooling.attn_type)

Indicates the [vllm.config.model.ModelConfig.attn_type](https://docs.vllm.ai/config/model/#vllm.config.model.ModelConfig.attn_type) to use by default.

You can use the [vllm.model_executor.models.interfaces_base.attn_type](https://docs.vllm.ai#vllm.model_executor.models.interfaces_base.attn_type) decorator to conveniently set this field.

###

`default_seq_pooling_type = 'LAST'`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces_base.VllmModelForPooling.default_seq_pooling_type)

Indicates the [vllm.config.pooler.PoolerConfig.seq_pooling_type](https://docs.vllm.ai/config/pooler/#vllm.config.pooler.PoolerConfig.seq_pooling_type) to use by default.

You can use the [vllm.model_executor.models.interfaces_base.default_pooling_type](https://docs.vllm.ai#vllm.model_executor.models.interfaces_base.default_pooling_type) decorator to conveniently set this field.

###

`default_tok_pooling_type = 'ALL'`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces_base.VllmModelForPooling.default_tok_pooling_type)

Indicates the [vllm.config.pooler.PoolerConfig.tok_pooling_type](https://docs.vllm.ai/config/pooler/#vllm.config.pooler.PoolerConfig.tok_pooling_type) to use by default.

You can use the [vllm.model_executor.models.interfaces_base.default_pooling_type](https://docs.vllm.ai#vllm.model_executor.models.interfaces_base.default_pooling_type) decorator to conveniently set this field.

###

`is_pooling_model = True`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces_base.VllmModelForPooling.is_pooling_model)

A flag that indicates this model supports pooling.

## Note

There is no need to redefine this flag if this class is in the MRO of your model class.

###

`pooler`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces_base.VllmModelForPooling.pooler)

The pooler is only called on TP rank 0.

###

`score_type = 'bi-encoder'`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces_base.VllmModelForPooling.score_type)

Indicates the [vllm.config.model.ModelConfig.score_type](https://docs.vllm.ai/config/model/#vllm.config.model.ModelConfig.score_type) to use by default.

Scoring API handles score/rerank for:

-
"classify" task (score_type: cross-encoder models)

-
"embed" task (score_type: bi-encoder models)

-
"token_embed" task (score_type: late interaction models)


score_type defaults to bi-encoder, then the Score API uses the "embed" task.

If you set score_type to cross-encoder via [vllm.model_executor.models.interfaces.SupportsCrossEncoding](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsCrossEncoding), then the Score API uses the "score" task.

If you set score_type to late-interaction via [vllm.model_executor.models.interfaces.SupportsLateInteraction](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsLateInteraction), then the Score API uses the "token_embed" task.

##

`VllmModelForTextGeneration`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces_base.VllmModelForTextGeneration)

Bases:

, [VllmModel](https://docs.vllm.ai#vllm.model_executor.models.interfaces_base.VllmModel)[T][Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)[T]

The interface required for all generative models in vLLM.

Methods:

-
–[compute_logits](https://docs.vllm.ai#vllm.model_executor.models.interfaces_base.VllmModelForTextGeneration.compute_logits)Return

`None`

if TP rank > 0.

## Source code in `vllm/model_executor/models/interfaces_base.py`


##

`attn_type(attn_type)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces_base.attn_type)

Decorator to set `VllmModelForPooling.attn_type`

.

##

`default_pooling_type(*, seq_pooling_type='LAST', tok_pooling_type='ALL')`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces_base.default_pooling_type)

Decorator to set `VllmModelForPooling.default_*_pooling_type`

.