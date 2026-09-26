source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/pooling/scoring/io_processor/
lastmod: 2026-09-24

class ScoringIOProcessor(PoolingIOProcessor):
name: str
pooling_task: PoolingTask
def __init__(self, *args, **kwargs):
super().__init__(*args, **kwargs)
self.tokenizer = self.renderer.get_tokenizer()
self.architecture = self.model_config.architecture
self.is_multimodal_model = self.model_config.is_multimodal_model
self.pad_token_id = self.tokenizer.pad_token_id
def create_pooling_params(self, request):
return request.to_pooling_params(self.pooling_task)
def _validate_token_limit(self, value: int, name: str) -> None:
if value < 0:
raise ValueError(f"{name} must be a non-negative integer")
if value >= self.model_config.max_model_len:
raise ValueError(
f"{name} ({value}) must be less "
f"than max_model_len ({self.model_config.max_model_len})."
)
def _get_token_limits(
self,
request: ScoringRequest | None = None,
pooling_params: PoolingParams | None = None,
) -> tuple[int, int]:
"""Extract and validate token limits from request or pooling_params."""
if request is not None:
max_tokens_per_query = getattr(request, "max_tokens_per_query", 0)
max_tokens_per_doc = getattr(request, "max_tokens_per_doc", 0)
else:
extra = (
(pooling_params.extra_kwargs or {})
if pooling_params is not None
else {}
)
max_tokens_per_query = extra.get("max_tokens_per_query", 0)
max_tokens_per_doc = extra.get("max_tokens_per_doc", 0)
if max_tokens_per_query != 0:
self._validate_token_limit(max_tokens_per_query, "max_tokens_per_query")
if max_tokens_per_doc != 0:
self._validate_token_limit(max_tokens_per_doc, "max_tokens_per_doc")
return max_tokens_per_query, max_tokens_per_doc
def _truncate_scoring_data(
self,
scoring_data: ScoringData,
max_tokens_per_query: int = 0,
max_tokens_per_doc: int = 0,
) -> ScoringData:
"""Truncate query/document texts to token limits."""
data_1 = scoring_data.data_1
data_2 = scoring_data.data_2
if max_tokens_per_query > 0:
data_1 = [
truncate_text_to_tokens(d, self.tokenizer, max_tokens_per_query)
if isinstance(d, str)
else d
for d in data_1
]
if max_tokens_per_doc > 0:
data_2 = [
truncate_text_to_tokens(d, self.tokenizer, max_tokens_per_doc)
if isinstance(d, str)
else d
for d in data_2
]
return ScoringData(data_1=data_1, data_2=data_2)
def valid_inputs(
self,
data_1: ScoreInput | list[ScoreInput],
data_2: ScoreInput | list[ScoreInput],
) -> ScoringData:
scoring_data = validate_score_input(
data_1,
data_2,
is_multimodal_model=self.is_multimodal_model,
architecture=self.architecture,
)
return scoring_data
def valid_inputs_online(self, request: AnyPoolingRequest):
if isinstance(request, ScoreRequest):
data_1 = request.data_1
data_2 = request.data_2
elif isinstance(request, RerankRequest):
data_1 = request.query
data_2 = request.documents
else:
raise ValueError(f"Invalid {request.__class__.__name__} request type")
scoring_data = self.valid_inputs(data_1, data_2)
return scoring_data