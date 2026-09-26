source: https://docs.vllm.ai/en/latest/api/vllm/models/inkling/nvidia/mtp/
lastmod: 2026-09-24

#

`vllm.models.inkling.nvidia.mtp`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.mtp)

Inkling MTP (Multi-Token Prediction) draft model (NVIDIA).

Mirrors the reference `mtp_model.py`

shipped with the checkpoint: each MTP depth `i`

owns `hidden_norm`

/ `embed_norm`

RMSNorms, an `input_proj`

(`2H -> H`

) and a full Inkling transformer block (dense bf16 MLP, with the same short convolutions as the backbone; its attention is full or sliding-window per depth, selected by `mtp_config.local_layer_ids`

). When enabled, a shared `chain_norm`

is applied after every depth; its output is both the logits input and the previous hidden state fed to the next depth.

The draft shares the target's token embedding table and LM head (`load_eagle_model`

wires those references) and applies the backbone `embed_norm`

on top: the depth layers were trained on the same normed embeddings the backbone consumes (their own `embed_norm`

weights are near-identity trims, unlike the backbone's whitening `embed_norm`

).

Classes:

-
–[InklingMTP](https://docs.vllm.ai#vllm.models.inkling.nvidia.mtp.InklingMTP) -
–[InklingMTPDepthLayer](https://docs.vllm.ai#vllm.models.inkling.nvidia.mtp.InklingMTPDepthLayer)One MTP depth: norm both inputs, fuse (2H->H), run a Inkling block.

-
–[InklingMultiTokenPredictor](https://docs.vllm.ai#vllm.models.inkling.nvidia.mtp.InklingMultiTokenPredictor)

##

`InklingMTP`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.mtp.InklingMTP)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)[SupportsMultiModalEmbeddings](https://docs.vllm.ai/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsMultiModalEmbeddings)

Methods:

-
–[get_top_tokens](https://docs.vllm.ai#vllm.models.inkling.nvidia.mtp.InklingMTP.get_top_tokens)Greedy draft tokens via rank-local argmax + tiny (value, index)


## Source code in `vllm/models/inkling/nvidia/mtp.py`


|
|

###

`get_top_tokens(hidden_states)`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.mtp.InklingMTP.get_top_tokens)

Greedy draft tokens via rank-local argmax + tiny (value, index) reduction — no full-vocab logits all-gather. The muP divisor is a positive scalar, so the argmax is invariant and the scaling is skipped entirely.

## Source code in `vllm/models/inkling/nvidia/mtp.py`


##

`InklingMTPDepthLayer`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.mtp.InklingMTPDepthLayer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

One MTP depth: norm both inputs, fuse (2H->H), run a Inkling block.

## Source code in `vllm/models/inkling/nvidia/mtp.py`


##

`InklingMultiTokenPredictor`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.mtp.InklingMultiTokenPredictor)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[embed_input_ids](https://docs.vllm.ai#vllm.models.inkling.nvidia.mtp.InklingMultiTokenPredictor.embed_input_ids)Draft-prefill embedding: fused gather + backbone embed_norm, then

-
–[fused_input_cat](https://docs.vllm.ai#vllm.models.inkling.nvidia.mtp.InklingMultiTokenPredictor.fused_input_cat)The depth layer's [rmsnorm(hidden) | embed_norm(embed)] input in one


## Source code in `vllm/models/inkling/nvidia/mtp.py`


|
|

###

`embed_input_ids(input_ids, multimodal_embeddings=None, *, is_multimodal=None)`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.mtp.InklingMultiTokenPredictor.embed_input_ids)

Draft-prefill embedding: fused gather + backbone embed_norm, then the target's tower embeddings scattered in unnormed (the backbone convention — MM embeds are merged after embed_norm).

## Source code in `vllm/models/inkling/nvidia/mtp.py`


###

`fused_input_cat(layer, previous_hidden, input_ids, inputs_embeds)`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.mtp.InklingMultiTokenPredictor.fused_input_cat)

The depth layer's [rmsnorm(hidden) | embed_norm(embed)] input in one launch: embedding row gather + the backbone embed_norm + the depth embed_norm chain on one side, hidden_norm on the other, written straight into the cat buffer.

## Source code in `vllm/models/inkling/nvidia/mtp.py`


##

`_load_inkling_mtp_weights(module, weights)`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.mtp._load_inkling_mtp_weights)

Load `model.mtp.*`

weights into the MTP module.

Checkpoint keys look like `model.mtp.chain_norm.weight`

and `model.mtp.layers.{i}.{...}`

. The transformer block reuses the backbone layer's fused-projection layout, so we apply the same qkvr / gate_up / down remapping as `_load_inkling_weights`

. Token embedding and LM head are shared (provided by `load_eagle_model`

) and are not present in mtp.safetensors.

## Source code in `vllm/models/inkling/nvidia/mtp.py`


|
|