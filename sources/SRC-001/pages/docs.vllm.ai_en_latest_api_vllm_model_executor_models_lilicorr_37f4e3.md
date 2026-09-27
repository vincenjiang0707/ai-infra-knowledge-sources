source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/lilicorr/
lastmod: 2026-09-27

@support_torch_compile
class LiLiCorrHead(nn.Module):
num_candidate_features = 5
def __init__(
self,
*,
model_hidden_size: int,
block_size: int,
rms_norm_eps: float,
config: dict[str, Any],
quant_config: QuantizationConfig | None = None,
prefix: str = "",
) -> None:
super().__init__()
hidden_size = config["lilicorr_hidden_size"] or model_hidden_size
self.block_size = block_size
self.num_candidate_slots = block_size - 1
self.candidate_topk = config["lilicorr_candidate_topk"]
if (
self.candidate_topk <= 0
or self.candidate_topk > 16
or self.candidate_topk & (self.candidate_topk - 1)
):
raise ValueError("LiLiCorr candidate_topk must be a power of two <= 16.")
self.hidden_size = hidden_size
self.num_heads = config["lilicorr_num_heads"]
self.mlp_ratio = config["lilicorr_mlp_ratio"]
self.factor_dim = config["lilicorr_factor_dim"]
self.vector_eps = config["lilicorr_vector_eps"]
self.logit_scale = config["lilicorr_logit_scale"]
# Candidate IDs and embeddings are replicated across TP ranks, so each
# rank scores the same lattice; the MLPs use standard tensor parallelism.
self.token_proj = (
nn.Identity()
if model_hidden_size == hidden_size
else ReplicatedLinear(
model_hidden_size,
hidden_size,
return_bias=False,
quant_config=quant_config,
prefix=maybe_prefix(prefix, "token_proj"),
)
)
self.pass_hidden_proj = ReplicatedLinear(
model_hidden_size,
hidden_size,
return_bias=False,
quant_config=quant_config,
prefix=maybe_prefix(prefix, "pass_hidden_proj"),
)
self.feature_norm = nn.LayerNorm(self.num_candidate_features)
self.feature_mlp = NemotronHMLP(
config=None,
hidden_size=self.num_candidate_features,
intermediate_size=hidden_size,
hidden_act="silu",
output_size=hidden_size,
bias=True,
quant_config=quant_config,
prefix=maybe_prefix(prefix, "feature_mlp"),
)
self.slot_embedding = nn.Parameter(
torch.zeros(1, 1, self.num_candidate_slots, 1, hidden_size)
)
self.rank_embedding = nn.Parameter(
torch.zeros(1, 1, 1, self.candidate_topk, hidden_size)
)
self.relative_slot_bias = nn.Parameter(
torch.zeros(self.num_heads, 2 * self.block_size - 1)
)
self.same_slot_bias = nn.Parameter(torch.zeros(self.num_heads))
self.context_proj = ReplicatedLinear(
model_hidden_size,
hidden_size,
return_bias=False,
quant_config=quant_config,
prefix=maybe_prefix(prefix, "context_proj"),
)
self.layers = nn.ModuleList(
[
LiLiCorrLayer(
hidden_size=hidden_size,
num_heads=self.num_heads,
mlp_ratio=self.mlp_ratio,
rms_norm_eps=rms_norm_eps,
quant_config=quant_config,
prefix=maybe_prefix(prefix, f"layers.{i}"),
)
for i in range(config["lilicorr_num_layers"])
]
)
self.output_norm = nn.RMSNorm(hidden_size, eps=rms_norm_eps)
self.anchor_norm = nn.RMSNorm(hidden_size, eps=rms_norm_eps)
self.factor_input_proj = ReplicatedLinear(
hidden_size * 3,
hidden_size,
return_bias=False,
quant_config=None,
prefix=maybe_prefix(prefix, "factor_input_proj"),
)
# Each candidate gets outgoing and incoming vectors. After normalization,
# their dot product scores a transition from slot s to slot s+1:
# pair_score[s, i, j] = dot(out[s, i], incoming[s+1, j])
# The anchor supplies the outgoing vector for the first slot.
self.out_head = ReplicatedLinear(
hidden_size,
self.factor_dim,
return_bias=False,
quant_config=None,
prefix=maybe_prefix(prefix, "out_head"),
)
self.in_head = ReplicatedLinear(
hidden_size,
self.factor_dim,
return_bias=False,
quant_config=None,
prefix=maybe_prefix(prefix, "in_head"),
)
self.anchor_out_head = ReplicatedLinear(
hidden_size,
self.factor_dim,
return_bias=False,
quant_config=quant_config,
prefix=maybe_prefix(prefix, "anchor_out_head"),
)
self._fused_edge_weight: torch.Tensor | None = None
self._fused_edge_bias: torch.Tensor | None = None
self._factor_input_splits: tuple[torch.Tensor, ...]
self._attn_bias: torch.Tensor | None = None
self._rank_frac_col: torch.Tensor
self._is_top1_col: torch.Tensor
@torch.no_grad()
def materialize_inference_buffers(
self, device: torch.device, dtype: torch.dtype
) -> None:
"""Build inference-only views/copies after checkpoint weights are loaded."""
topk = self.candidate_topk
self._attn_bias = self._build_attention_bias(device=device, dtype=dtype)
# Both projections consume the same candidate features f:
# out = W_out @ f + b_out
# incoming = W_in @ f + b_in
# Stack weights and biases to compute both in one linear call. score()
# splits the result and normalizes the two vectors separately.
self._fused_edge_weight = (
torch.cat([self.out_head.weight, self.in_head.weight], dim=0)
.to(device=device, dtype=dtype)
.contiguous()
)
self._fused_edge_bias = (
torch.cat([self.out_head.bias, self.in_head.bias], dim=0)
.to(device=device, dtype=dtype)
.contiguous()
)
# For candidate state x and request anchor a, the trained projection is:
# W @ concat(x, a, x*a) + b
# Split W into input blocks to evaluate the same expression as:
# W_x @ x + W_a @ a + W_cross @ (x*a) + b
# Here x*a is elementwise. This avoids concatenating inputs and reuses
# W_a @ a across candidates, adding the original bias only once.
weight = self.factor_input_proj.weight
hdim = self.hidden_size
self._factor_input_splits = (
weight[:, :hdim].contiguous(),
weight[:, hdim : 2 * hdim].contiguous(),
weight[:, 2 * hdim :].contiguous(),
)
if topk > 1:
rank_frac = torch.arange(topk, device=device, dtype=torch.float32).view(
1, 1, topk
) / float(topk - 1)
else:
rank_frac = torch.zeros(1, 1, topk, device=device, dtype=torch.float32)
is_top1 = torch.zeros(1, 1, topk, device=device, dtype=torch.float32)
is_top1[..., 0] = 1.0
self._rank_frac_col = rank_frac.contiguous()
self._is_top1_col = is_top1.contiguous()
def _build_attention_bias(
self, *, device: torch.device, dtype: torch.dtype
) -> torch.Tensor:
topk = self.candidate_topk
slot_ids = torch.arange(
self.num_candidate_slots, device=device, dtype=torch.long
).repeat_interleave(topk)
# Attention flattens [slot, candidate] into one sequence. With topk=2,
# the candidate slot IDs are [0, 0, 1, 1, ...]. Each head learns:
# bias(q, k) = relative_bias[slot(q) - slot(k) + offset]
# + same_slot_bias * (slot(q) == slot(k))
# The same-slot term includes distinct candidates at the same position.
# This is an additive preference, not a causal mask. Keep the trained
# offset = block_size-1 when score() selects a shorter draft's prefix,
# so each distance continues to use the same learned weight.
rel = slot_ids.view(-1, 1) - slot_ids.view(1, -1)
bias = self.relative_slot_bias[:, rel + self.block_size - 1]
same_slot = slot_ids.view(-1, 1) == slot_ids.view(1, -1)
bias = bias + same_slot.unsqueeze(0).to(
dtype=bias.dtype
) * self.same_slot_bias.view(-1, 1, 1)
return bias.to(device=device, dtype=dtype).contiguous()
def score(
self,
*,
token_embeddings: torch.Tensor,
candidate_log_probs: torch.Tensor,
pass_hidden: torch.Tensor,
anchor_hidden: torch.Tensor,
anchor_valid: torch.Tensor,
) -> tuple[torch.Tensor, torch.Tensor]:
if self._attn_bias is None:
raise RuntimeError(
"Call materialize_inference_buffers() after loading the LiLiCorr head."
)
bsz, n_slots, topk = candidate_log_probs.shape
if not 1 <= n_slots <= self.num_candidate_slots:
raise ValueError(
f"LiLiCorr supports 1..{self.num_candidate_slots} candidate slots, "
f"got {n_slots}."
)
if topk != self.candidate_topk:
raise ValueError(
f"LiLiCorr expects candidate_topk={self.candidate_topk}, got {topk}."
)
proj_dtype = self.slot_embedding.dtype
if token_embeddings.dtype != proj_dtype:
token_embeddings = token_embeddings.to(proj_dtype)
if pass_hidden.dtype != proj_dtype:
pass_hidden = pass_hidden.to(proj_dtype)
token_states = self.token_proj(token_embeddings)
pass_states = self.pass_hidden_proj(pass_hidden).unsqueeze(-2)
log_probs = candidate_log_probs.float()
features = torch.stack(
[
log_probs,
log_probs.exp(),
log_probs - log_probs.max(dim=-1, keepdim=True).values,
self._rank_frac_col.expand_as(log_probs),
self._is_top1_col.expand_as(log_probs),
],
dim=-1,
)
hidden_states = token_states + pass_states
hidden_states = hidden_states + self.feature_mlp(
self.feature_norm(features.to(dtype=token_states.dtype))
)
hidden_states = hidden_states + self.slot_embedding[:, 0, :n_slots]
hidden_states = hidden_states + self.rank_embedding[:, 0]
hidden_states = hidden_states.reshape(bsz, n_slots * topk, self.hidden_size)
anchor_state = self.context_proj(anchor_hidden)
anchor_state = anchor_state * anchor_valid[:, None].to(anchor_state.dtype)
# Shorter drafts use the learned prefix; keep checkpoint parameter shapes.
lattice = n_slots * topk
attention_bias = self._attn_bias[None, :, :lattice, :lattice]
for layer in self.layers:
hidden_states = layer(hidden_states, attention_bias)
hidden_states = self.output_norm(hidden_states).reshape(
bsz, n_slots, topk, self.hidden_size
)
anchor_state = self.anchor_norm(anchor_state)
w_self, w_anchor, w_cross = self._factor_input_splits
anchor_row = anchor_state[:, None, None, :]
pre = F.linear(hidden_states, w_self, self.factor_input_proj.bias)
pre = pre + F.linear(anchor_row, w_anchor)
pre = pre + F.linear(hidden_states * anchor_row, w_cross)
factor_hidden = F.silu(pre)
edges = F.linear(factor_hidden, self._fused_edge_weight, self._fused_edge_bias)
out_vec, in_vec = F.normalize(
edges.unflatten(-1, (2, self.factor_dim)), dim=-1, eps=self.vector_eps
).unbind(-2)
anchor_out = F.normalize(
self.anchor_out_head(anchor_state), dim=-1, eps=self.vector_eps
)
# start_scores[b, j] scores anchor -> candidate j in slot zero.
# pair_scores[b, s, i, j] scores candidate i in slot s -> candidate j
# in slot s+1. Normalized factor dot products encode learned compatibility;
# forward() scales them into logits for the candidate-path selector.
start_scores = (anchor_out[:, None, :] * in_vec[:, 0, :, :]).sum(dim=-1)
pair_scores = torch.matmul(out_vec[:, :-1], in_vec[:, 1:].transpose(-1, -2))
return (start_scores, pair_scores)
def forward(
self,
token_embeddings: torch.Tensor,
candidate_log_probs: torch.Tensor,
pass_hidden: torch.Tensor,
anchor_hidden: torch.Tensor,
anchor_valid: torch.Tensor,
) -> torch.Tensor:
start, pairs = self.score(
token_embeddings=token_embeddings,
candidate_log_probs=candidate_log_probs,
pass_hidden=pass_hidden,
anchor_hidden=anchor_hidden,
anchor_valid=anchor_valid,
)
start = self.logit_scale * start.float()
pairs = self.logit_scale * pairs.float()
# The shared walk starts at predecessor index zero; all first rows agree.
first = start[:, None, None, :].expand(-1, 1, self.candidate_topk, -1)
return torch.cat((first, pairs), dim=1)