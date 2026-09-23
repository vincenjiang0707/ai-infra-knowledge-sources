source: https://docs.vllm.ai/en/latest/api/vllm/models/kimi_k3/common/mtp/
lastmod: 2026-09-23

#

`vllm.models.kimi_k3.common.mtp`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.common.mtp)

Fused Kimi-K3 MTP input preparation.

Functions:

-
–[fused_mtp_input](https://docs.vllm.ai#vllm.models.kimi_k3.common.mtp.fused_mtp_input)Mask and normalize both MTP inputs into the projection layout.


##

`fused_mtp_input(positions, inputs_embeds, previous_hidden_states, enorm_weight, hnorm_weight, eps)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.common.mtp.fused_mtp_input)

Mask and normalize both MTP inputs into the projection layout.