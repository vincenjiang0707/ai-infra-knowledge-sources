source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/jina/
lastmod: 2026-09-23

#

`vllm.model_executor.models.jina`

[¶](https://docs.vllm.ai#vllm.model_executor.models.jina)

Classes:

-
–[JinaEmbeddingsV5DecoderModel](https://docs.vllm.ai#vllm.model_executor.models.jina.JinaEmbeddingsV5DecoderModel)jina-embeddings-v5 with a Qwen3 decoder backbone (e.g. -small).

-
–[JinaEmbeddingsV5EncoderModel](https://docs.vllm.ai#vllm.model_executor.models.jina.JinaEmbeddingsV5EncoderModel)jina-embeddings-v5 with a bidirectional EuroBERT (Llama) encoder backbone.

-
–[JinaEmbeddingsV5Model](https://docs.vllm.ai#vllm.model_executor.models.jina.JinaEmbeddingsV5Model)Dispatcher for the jina-embeddings-v5 family.


##

`JinaEmbeddingsV5DecoderModel`

[¶](https://docs.vllm.ai#vllm.model_executor.models.jina.JinaEmbeddingsV5DecoderModel)

Bases: `Qwen3ForCausalLM`

, [VllmModelForPooling](https://docs.vllm.ai/interfaces_base/#vllm.model_executor.models.interfaces_base.VllmModelForPooling)

jina-embeddings-v5 with a Qwen3 decoder backbone (e.g. -small).

Task-specific LoRA adapters are merged into the base weights at load time. Declares itself a pooling model so that as_embedding_model() does not wrap it.

## Source code in `vllm/model_executor/models/jina.py`


##

`JinaEmbeddingsV5EncoderModel`

[¶](https://docs.vllm.ai#vllm.model_executor.models.jina.JinaEmbeddingsV5EncoderModel)

Bases: `LlamaForCausalLM`

, [VllmModelForPooling](https://docs.vllm.ai/interfaces_base/#vllm.model_executor.models.interfaces_base.VllmModelForPooling)

jina-embeddings-v5 with a bidirectional EuroBERT (Llama) encoder backbone.

Used by encoder checkpoints such as jina-embeddings-v5-text-nano (`is_decoder=False`

). EuroBERT is architecturally a bidirectional Llama, so the LlamaModel backbone switches to EncoderOnlyAttention when the config carries `is_causal=False`

(set by `JinaEmbeddingsV5ModelConfig`

).

## Source code in `vllm/model_executor/models/jina.py`


##

`JinaEmbeddingsV5Model`

[¶](https://docs.vllm.ai#vllm.model_executor.models.jina.JinaEmbeddingsV5Model)

Bases: [JinaEmbeddingsV5DecoderModel](https://docs.vllm.ai#vllm.model_executor.models.jina.JinaEmbeddingsV5DecoderModel)

Dispatcher for the jina-embeddings-v5 family.

The family ships two backbones under one `architectures`

entry: Qwen3 decoders (-small) and bidirectional EuroBERT encoders (-nano), told apart by `is_decoder`

. Inherits the decoder implementation so registry introspection still sees a valid pooling model, and `__new__`

swaps in the encoder variant for encoder checkpoints.

## Source code in `vllm/model_executor/models/jina.py`


##

`_build_lora_pairs(adapter_weights)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.jina._build_lora_pairs)

Group raw adapter tensors into {base_key: {"A": tensor, "B": tensor}} pairs.

## Transforms adapter keys like

base_model.model.layers.0.self_attn.q_proj.lora_A.weight

Into base keys like: layers.0.self_attn.q_proj.weight

## Source code in `vllm/model_executor/models/jina.py`


##

`_load_adapter(model, task, revision)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.jina._load_adapter)

Load adapter config and weights from a local path or HF repo.

Returns (adapter_config, adapter_weights) or None if not found.

## Source code in `vllm/model_executor/models/jina.py`


##

`_load_jina_v5_weights(model, weights)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.jina._load_jina_v5_weights)

Shared loader: merge the selected task LoRA adapter into the base weights.

## Source code in `vllm/model_executor/models/jina.py`


##

`_setup_jina_v5_task_and_pooler(model, vllm_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.jina._setup_jina_v5_task_and_pooler)

Shared init for jina-embeddings-v5 wrappers: select task + build pooler.