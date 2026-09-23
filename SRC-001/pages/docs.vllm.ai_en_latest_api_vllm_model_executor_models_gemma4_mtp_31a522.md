source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/gemma4_mtp/
lastmod: 2026-09-23

#

`vllm.model_executor.models.gemma4_mtp`

[¶](https://docs.vllm.ai#vllm.model_executor.models.gemma4_mtp)

Inference-only Gemma4 MTP (Multi-Token Prediction) model.

The Gemma4 assistant model is a lightweight decoder that shares KV cache with the target (backbone) model. All assistant decoder layers are KV-shared: they only have Q projections (no K/V projections or norms), and read K/V from the target model's cache at runtime.

Checkpoint layout (`gemma4_assistant`

)::

```
model.embed_tokens.* -- token embeddings
model.layers.{i}.* -- decoder layers (Q-only attention + MLP)
model.norm.* -- final RMSNorm
pre_projection.* -- Linear(2 * backbone_hidden_size, hidden_size)
post_projection.* -- Linear(hidden_size, backbone_hidden_size)
lm_head.* -- language model head (tied to embed_tokens)
masked_embedding.centroids.* -- centroid projection (when use_ordered_embeddings)
masked_embedding.token_ordering -- token-to-centroid mapping buffer
```


Classes:

-
–[Gemma4MTP](https://docs.vllm.ai#vllm.model_executor.models.gemma4_mtp.Gemma4MTP)Gemma4 Multi-Token Prediction model for speculative decoding.

-
–[Gemma4MTPAttention](https://docs.vllm.ai#vllm.model_executor.models.gemma4_mtp.Gemma4MTPAttention)Q-only attention for Gemma4 MTP layers.

-
–[Gemma4MTPMaskedEmbedder](https://docs.vllm.ai#vllm.model_executor.models.gemma4_mtp.Gemma4MTPMaskedEmbedder)Sparse logit computation via centroid-based vocabulary masking.

-
–[Gemma4MultiTokenPredictor](https://docs.vllm.ai#vllm.model_executor.models.gemma4_mtp.Gemma4MultiTokenPredictor)

##

`Gemma4MTP`

[¶](https://docs.vllm.ai#vllm.model_executor.models.gemma4_mtp.Gemma4MTP)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Gemma4 Multi-Token Prediction model for speculative decoding.

forward() returns (draft_hidden_states, backbone_hidden_states). The proposer uses draft_hidden_states for compute_logits (via the draft-dim lm_head) and backbone_hidden_states for the hidden-state feedback buffer.

Methods:

-
–[get_top_tokens](https://docs.vllm.ai#vllm.model_executor.models.gemma4_mtp.Gemma4MTP.get_top_tokens)Sparse argmax via centroids masking. Returns token IDs directly.


## Source code in `vllm/model_executor/models/gemma4_mtp.py`


|
|

###

`get_top_tokens(hidden_states)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.gemma4_mtp.Gemma4MTP.get_top_tokens)

Sparse argmax via centroids masking. Returns token IDs directly.

## Source code in `vllm/model_executor/models/gemma4_mtp.py`


##

`Gemma4MTPAttention`

[¶](https://docs.vllm.ai#vllm.model_executor.models.gemma4_mtp.Gemma4MTPAttention)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Q-only attention for Gemma4 MTP layers.

K/V come from the target model's KV cache via `kv_sharing_target_layer_name`

(set by the proposer after model construction).

## Source code in `vllm/model_executor/models/gemma4_mtp.py`


|
|

##

`Gemma4MTPMaskedEmbedder`

[¶](https://docs.vllm.ai#vllm.model_executor.models.gemma4_mtp.Gemma4MTPMaskedEmbedder)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Sparse logit computation via centroid-based vocabulary masking.

Instead of computing logits against the full vocabulary, projects hidden states to centroid scores, selects top-K centroids, and computes logits only for the ~top_k * (vocab_size / num_centroids) tokens belonging to those centroids.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.gemma4_mtp.Gemma4MTPMaskedEmbedder.forward)Full-vocab logits with non-selected positions masked to -inf.

-
–[get_top_tokens](https://docs.vllm.ai#vllm.model_executor.models.gemma4_mtp.Gemma4MTPMaskedEmbedder.get_top_tokens)Sparse argmax — returns vocab token IDs without full-vocab tensor.


## Source code in `vllm/model_executor/models/gemma4_mtp.py`


|
|

###

`_select_and_score(hidden_states, lm_head_weight)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.gemma4_mtp.Gemma4MTPMaskedEmbedder._select_and_score)

Centroid selection + sparse dot product.

Returns:

-
(`logits`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(num_tokens, num_selected) sparse logits.

-
(`indices`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(num_tokens, num_selected) corresponding vocab indices.


## Source code in `vllm/model_executor/models/gemma4_mtp.py`


###

`forward(hidden_states, lm_head_weight)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.gemma4_mtp.Gemma4MTPMaskedEmbedder.forward)

Full-vocab logits with non-selected positions masked to -inf.

## Source code in `vllm/model_executor/models/gemma4_mtp.py`


###

`get_top_tokens(hidden_states, lm_head_weight)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.gemma4_mtp.Gemma4MTPMaskedEmbedder.get_top_tokens)

Sparse argmax — returns vocab token IDs without full-vocab tensor.

## Source code in `vllm/model_executor/models/gemma4_mtp.py`


##

`Gemma4MultiTokenPredictor`

[¶](https://docs.vllm.ai#vllm.model_executor.models.gemma4_mtp.Gemma4MultiTokenPredictor)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.gemma4_mtp.Gemma4MultiTokenPredictor.forward)Returns (draft_hidden_states, backbone_hidden_states).


## Source code in `vllm/model_executor/models/gemma4_mtp.py`


|
|

###

`forward(input_ids, positions, hidden_states, intermediate_tensors=None, inputs_embeds=None, spec_step_idx=0)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.gemma4_mtp.Gemma4MultiTokenPredictor.forward)

Returns (draft_hidden_states, backbone_hidden_states).

draft_hidden_states: draft-dim, used by compute_logits via lm_head. backbone_hidden_states: backbone-dim, stored in the proposer's hidden-state buffer and fed back as input to the next step.