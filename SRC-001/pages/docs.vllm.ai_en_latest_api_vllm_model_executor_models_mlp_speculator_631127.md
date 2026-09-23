source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/mlp_speculator/
lastmod: 2026-09-23

class MLPSpeculator(nn.Module):
"""An implementation of the speculative models introduced in
"Accelerating Production LLMs with Combined Token/Embedding
Speculators"
https://arxiv.org/pdf/2404.19124
Trained speculators of this type are available on HF hub at:
https://huggingface.co/ibm-ai-platform and https://huggingface.co/ibm-granite
"""
def __init__(self, *, vllm_config: VllmConfig, prefix: str = "") -> None:
super().__init__()
config = vllm_config.model_config.hf_config
self.n_predict = config.n_predict
self.vocab_size = config.vocab_size
self.emb_dim = config.emb_dim
self.inner_dim = config.inner_dim if config.inner_dim != 0 else config.emb_dim
self.max_speculative_tokens = config.num_lookahead_tokens
self.tie_weights = config.tie_weights
self.scale_input = config.scale_input
if self.tie_weights:
assert self.n_predict > 1, (
"You cannot tie weights between stages when only 1 exists"
)
embedding = VocabParallelEmbedding(
config.vocab_size, self.inner_dim, org_num_embeddings=config.vocab_size
)
self.emb = nn.ModuleList([embedding] * self.max_speculative_tokens)
# the initial projection from the base model may
# have a different size, so that stays separate.
proj_first = nn.Linear(self.emb_dim, self.inner_dim, bias=False)
proj_tied = nn.Linear(self.inner_dim, self.inner_dim, bias=False)
self.proj = nn.ModuleList(
[proj_first] + [proj_tied] * (self.max_speculative_tokens - 1)
)
self.head = nn.ModuleList(
[
ParallelLMHead(
self.vocab_size,
self.inner_dim,
bias=False,
prefix=maybe_prefix(prefix, f"head.{i}"),
)
for i in range(self.max_speculative_tokens)
]
)
ln = MLPSpeculatorLayerNorm(
self.inner_dim, elementwise_scale_and_shift=True
)
self.ln = nn.ModuleList([ln] * self.max_speculative_tokens)
else:
self.emb = nn.ModuleList(
[
VocabParallelEmbedding(
config.vocab_size,
self.inner_dim,
)
for _ in range(self.max_speculative_tokens)
]
)
self.proj = nn.ModuleList(
[
nn.Linear(
(self.emb_dim if i == 0 else self.inner_dim),
self.inner_dim,
bias=False,
)
for i in range(self.max_speculative_tokens)
]
)
self.head = nn.ModuleList(
[
ParallelLMHead(
self.vocab_size,
self.inner_dim,
bias=False,
prefix=maybe_prefix(prefix, f"head.{i}"),
)
for i in range(self.max_speculative_tokens)
]
)
self.ln = nn.ModuleList(
[
MLPSpeculatorLayerNorm(
self.inner_dim, elementwise_scale_and_shift=True
)
for _ in range(self.max_speculative_tokens)
]
)
if self.scale_input:
self.ln0 = MLPSpeculatorLayerNorm(
self.emb_dim, elementwise_scale_and_shift=False
)
self.state_weight = 0.5 ** (0.5 / config.n_predict)
self.emb_weight = math.sqrt((1 - self.state_weight**2) * (self.inner_dim / 2))
self.activation = nn.GELU()
self.config = config
self.logits_processor = LogitsProcessor(
config.vocab_size, config.vocab_size, 1.0
)
def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
params_dict = dict(self.named_parameters())
loaded_params: set[str] = set()
for name, loaded_weight in weights:
name = name.replace("speculator.", "")
param = params_dict.get(name)
if param is not None:
weight_loader = getattr(param, "weight_loader", default_weight_loader)
weight_loader(param, loaded_weight)
loaded_params.add(name)
return loaded_params