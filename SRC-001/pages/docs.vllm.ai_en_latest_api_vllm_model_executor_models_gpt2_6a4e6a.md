source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/gpt2/
lastmod: 2026-09-23

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

, [SupportsCrossEncoding](../interfaces/#vllm.model_executor.models.interfaces.SupportsCrossEncoding)


GPT2 Model for sequence classification.

This class expands GPT2Model with pooling and score functions - last token is being used for classification.

Attributes:

-
`transformer`

– An instance of GPT2Model used for forward operations.

-
`score`

– A layer for calculating logits.

-
`_pooler`

– An instance of Pooler used for pooling operations.


## Source code in `vllm/model_executor/models/gpt2.py`


| class GPT2ForSequenceClassification(nn.Module, SupportsCrossEncoding):
"""GPT2 Model for sequence classification.
This class expands GPT2Model with pooling and score functions - last token
is being used for classification.
Attributes:
transformer: An instance of GPT2Model used for forward operations.
score: A layer for calculating logits.
_pooler: An instance of Pooler used for pooling operations.
"""
is_pooling_model = True
def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
super().__init__()
config = vllm_config.model_config.hf_config
self.transformer = GPT2Model(
vllm_config=vllm_config, prefix=maybe_prefix(prefix, "transformer")
)
self.score = nn.Linear(
config.n_embd,
config.num_labels,
bias=False,
dtype=vllm_config.model_config.head_dtype,
)
pooler_config = vllm_config.model_config.pooler_config
assert pooler_config is not None
self.pooler = DispatchPooler.for_seq_cls(pooler_config, classifier=self.score)
def embed_input_ids(self, input_ids: torch.Tensor) -> torch.Tensor:
return self.transformer.embed_input_ids(input_ids)
def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]):
loader = AutoWeightsLoader(self)
weights = _add_transformer_prefix(weights)
return loader.load_weights(weights)
def forward(
self,
input_ids: torch.Tensor | None,
positions: torch.Tensor,
intermediate_tensors: IntermediateTensors | None = None,
inputs_embeds: torch.Tensor | None = None,
) -> torch.Tensor:
hidden_states = self.transformer(
input_ids=input_ids,
position_ids=positions,
inputs_embeds=inputs_embeds,
intermediate_tensors=intermediate_tensors,
)
return hidden_states
|