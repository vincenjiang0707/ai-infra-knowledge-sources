source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v4/common/ops/fused_mtp_input_rmsnorm/
lastmod: 2026-09-23

#

`vllm.models.deepseek_v4.common.ops.fused_mtp_input_rmsnorm`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.fused_mtp_input_rmsnorm)

Fused MTP-input RMSNorm: enorm (with mask-zero at position 0) + hnorm.

## Replaces the eager sequence at the top of the MTP draft forward

inputs_embeds = torch.where(positions.unsqueeze(-1) == 0, 0, inputs_embeds) inputs_embeds = self.enorm(inputs_embeds) previous_hidden_states = previous_hidden_states.view(-1, hc_mult, H) previous_hidden_states = self.hnorm(previous_hidden_states)

which lowers to ~6 small kernels (CompareEq, where, Fill, enorm rms_norm, hnorm rms_norm, plus aten elementwise helpers) on the breakable-cudagraph path. Math is preserved: positions==0 → masked row → zero RMS output regardless of weight.

A single grid (T, hc_mult+1) drives both norms: task 0 is enorm on inputs_embeds[token, :], task k+1 is hnorm on previous_hidden_states[token, k, :].