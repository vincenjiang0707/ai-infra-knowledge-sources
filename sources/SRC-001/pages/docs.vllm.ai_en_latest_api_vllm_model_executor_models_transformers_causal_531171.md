source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/transformers/causal/
lastmod: 2026-09-23

class CausalMixin(VllmModelForTextGeneration, Base):
def __init__(self, *, vllm_config: "VllmConfig", prefix: str = ""):
# Skip VllmModelForTextGeneration.__init__ and call the next class in MRO
super(VllmModelForTextGeneration, self).__init__(
vllm_config=vllm_config, prefix=prefix
)
tie_word_embeddings = self._get_tie_word_embeddings()
if self.pp_group.is_last_rank:
self.lm_head = ParallelLMHead(
self.text_config.vocab_size,
self.text_config.hidden_size,
quant_config=self.quant_config,
prefix=maybe_prefix(prefix, "lm_head"),
)
if tie_word_embeddings:
for module in self.model.get_input_embeddings().modules():
if isinstance(module, VocabParallelEmbedding):
self.lm_head = self.lm_head.tie_weights(module)
break
self.logits_processor = LogitsProcessor(
self.text_config.vocab_size,
scale=getattr(self.text_config, "logit_scale", 1.0),
soft_cap=getattr(self.text_config, "final_logit_softcapping", None),
)
else:
self.lm_head = PPMissingLayer()
def load_weights(self, weights: Iterable[tuple[str, "torch.Tensor"]]) -> set[str]:
"""A thin wrapper around `Base.load_weights` to handle the lm_head bias."""
lm_head_bias = set()
def auto_load_lm_head_bias(weights):
for name, weight in weights:
if name.endswith("lm_head.bias") and self.pp_group.is_last_rank:
self.lm_head._register_bias()
self.lm_head.bias.weight_loader(self.lm_head.bias, weight)
lm_head_bias.add(name)
else:
yield name, weight
return super().load_weights(auto_load_lm_head_bias(weights)) | lm_head_bias
def compute_logits(self, hidden_states: "torch.Tensor") -> "torch.Tensor | None":
logits = self.logits_processor(self.lm_head, hidden_states, self.lm_head.bias)
return logits