source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/mimo_v2_mtp/
lastmod: 2026-09-24

#

`vllm.model_executor.models.mimo_v2_mtp`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mimo_v2_mtp)

Inference-only MiMo-V2 MTP (Multi-Token Prediction) draft model.

Supports both MiMo-V2-Pro and MiMo-V2-Flash checkpoints.

Checkpoint weight layout (model.mtp.layers.{idx}.*): enorm - RMSNorm for token embeddings hnorm - RMSNorm for previous hidden states eh_proj - ReplicatedLinear(hidden*2 -> hidden) input_layernorm - pre-attention RMSNorm self_attn.* - attention weights; format differs by variant: Pro: fused qkv_proj [Q;K;V] concatenated Flash: separate q_proj, k_proj, v_proj pre_mlp_layernorm - post-attention / pre-MLP RMSNorm mlp.* - dense MLP (gate_proj / up_proj / down_proj) final_layernorm - norm applied before logit computation

Classes:

-
–[MiMoV2MTPLayer](https://docs.vllm.ai#vllm.model_executor.models.mimo_v2_mtp.MiMoV2MTPLayer)Single MTP predictor layer for MiMo-V2 (Pro and Flash).


##

`MiMoV2MTPLayer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mimo_v2_mtp.MiMoV2MTPLayer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Single MTP predictor layer for MiMo-V2 (Pro and Flash).

Mirrors the single-layer MiMo-V2 nextn reference implementation.

## Source code in `vllm/model_executor/models/mimo_v2_mtp.py`


##

`_MiMoV2MTPLayers`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mimo_v2_mtp._MiMoV2MTPLayers)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Thin wrapper so parameter paths match checkpoint: model.mtp.layers.*.