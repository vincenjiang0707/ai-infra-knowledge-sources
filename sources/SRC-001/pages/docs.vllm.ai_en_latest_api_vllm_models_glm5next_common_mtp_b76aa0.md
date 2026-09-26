source: https://docs.vllm.ai/en/latest/api/vllm/models/glm5next/common/mtp/
lastmod: 2026-09-24

class Glm5NextMultiTokenPredictor(nn.Module):
def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
super().__init__()
config = vllm_config.model_config.hf_config
self.mtp_start_layer_idx = config.num_hidden_layers
self.num_mtp_layers = config.num_nextn_predict_layers
self.layers = torch.nn.ModuleDict(
{
str(idx): Glm5NextMultiTokenPredictorLayer(
vllm_config, f"{prefix}.layers.{idx}"
)
for idx in range(
self.mtp_start_layer_idx,
self.mtp_start_layer_idx + self.num_mtp_layers,
)
}
)
self.embed_tokens = VocabParallelEmbedding(
config.vocab_size,
config.hidden_size,
prefix=maybe_prefix(prefix, "embed_tokens"),
)
# Plain list for the per-propose lookup: ModuleDict[str(...)] builds a
# string and hashes it on every draft step.
self._mtp_layers = list(self.layers.values())
self._mtp_mla_attns = []
for layer in self._mtp_layers:
self_attn = layer.mtp_block.self_attn
assert isinstance(self_attn, Glm5NextMLAAttention)
self._mtp_mla_attns.append(self_attn.mla_attn)
self.logits_processor = LogitsProcessor(config.vocab_size)
def set_skip_topk(self, skip: bool):
# index_share_for_mtp_iteration: step 0 computes top-k, steps 1+ reuse.
for mla_attn in self._mtp_mla_attns:
mla_attn.skip_topk = skip
def compact_topk_indices(self, slot_ids: torch.Tensor):
"""Gather the top-k index rows at ``slot_ids`` to the front of the buffer."""
num_slots = slot_ids.numel()
for mla_attn in self._mtp_mla_attns:
topk_indices_buffer = mla_attn.topk_indices_buffer
assert topk_indices_buffer is not None
topk_indices_buffer[:num_slots] = topk_indices_buffer[slot_ids]
def embed_input_ids(self, input_ids: torch.Tensor) -> torch.Tensor:
return self.embed_tokens(input_ids)
def forward(
self,
input_ids: torch.Tensor,
positions: torch.Tensor,
previous_hidden_states: torch.Tensor,
inputs_embeds: torch.Tensor | None = None,
spec_step_idx: int = 0,
) -> torch.Tensor:
if inputs_embeds is None:
inputs_embeds = self.embed_tokens(input_ids)
current_step_idx = spec_step_idx % self.num_mtp_layers
return self._mtp_layers[current_step_idx](
input_ids,
positions,
previous_hidden_states,
inputs_embeds,
current_step_idx,
)
def compute_logits(
self,
hidden_states: torch.Tensor,
spec_step_idx: int = 0,
) -> torch.Tensor:
current_step_idx = spec_step_idx % self.num_mtp_layers
mtp_layer = self._mtp_layers[current_step_idx]
# hidden_states is already post-final-norm (produced in the layer
# forward and recycled as-is); apply the LM head only, without a
# second RMSNorm.
return self.logits_processor(mtp_layer.shared_head.head, hidden_states)
def get_top_tokens(
self,
hidden_states: torch.Tensor,
spec_step_idx: int = 0,
) -> torch.Tensor:
current_step_idx = spec_step_idx % self.num_mtp_layers
mtp_layer = self._mtp_layers[current_step_idx]
# Vocab-parallel argmax for the greedy draft: per-rank head projection
# + local argmax + a [batch, 2*tp] (value, index) reduce, instead of
# materializing and all-gathering full [N, vocab] logits per draft
# step. Tie-breaking matches the full argmax (shards are contiguous
# and rank-ordered, so the lowest-rank winner is the lowest global
# index), so greedy draft tokens are unchanged.
return self.logits_processor.get_top_tokens(
mtp_layer.shared_head.head, hidden_states
)