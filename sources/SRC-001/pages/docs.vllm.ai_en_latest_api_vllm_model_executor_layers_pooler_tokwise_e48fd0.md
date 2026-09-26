source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/pooler/tokwise/
lastmod: 2026-09-24

Bases: [Pooler](../abstract/#vllm.model_executor.layers.pooler.abstract.Pooler)


A layer that pools specific information from hidden states.

This layer does the following: 1. Extracts specific tokens or aggregates data based on pooling method. 2. Postprocesses the output based on pooling head. 3. Returns structured results as `PoolerOutput`

.

## Source code in `vllm/model_executor/layers/pooler/tokwise/poolers.py`


| class TokenPooler(Pooler):
"""A layer that pools specific information from hidden states.
This layer does the following:
1. Extracts specific tokens or aggregates data based on pooling method.
2. Postprocesses the output based on pooling head.
3. Returns structured results as `PoolerOutput`.
"""
def __init__(
self,
pooling: TokenPoolingMethod | TokenPoolingFn,
head: TokenPoolerHead | TokenPoolingHeadFn | None = None,
) -> None:
super().__init__()
self.pooling = pooling
self.head = head
def extra_repr(self) -> str:
head_name = self.head.__class__.__name__ if self.head is not None else None
return f"pooling={self.pooling.__class__.__name__}, head={head_name}"
def get_supported_tasks(self) -> Set[PoolingTask]:
tasks = set(POOLING_TASKS)
if isinstance(self.pooling, TokenPoolingMethod):
tasks &= self.pooling.get_supported_tasks()
if isinstance(self.head, TokenPoolerHead):
tasks &= self.head.get_supported_tasks()
return tasks
def get_pooling_updates(self, task: PoolingTask) -> PoolingParamsUpdate:
updates = PoolingParamsUpdate()
if isinstance(self.pooling, TokenPoolingMethod):
updates |= self.pooling.get_pooling_updates(task)
return updates
def forward(
self,
hidden_states: torch.Tensor,
pooling_metadata: PoolingMetadata,
) -> TokenPoolerOutput:
pooled_data = self.pooling(hidden_states, pooling_metadata)
if self.head is not None:
pooled_data = self.head(pooled_data, pooling_metadata)
return pooled_data
|