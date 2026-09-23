source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/pooler/seqwise/
lastmod: 2026-09-23

Bases: [Pooler](../abstract/#vllm.model_executor.layers.pooler.abstract.Pooler)


A layer that pools specific information from hidden states.

This layer does the following: 1. Extracts specific tokens or aggregates data based on pooling method. 2. Postprocesses the output based on pooling head. 3. Returns structured results as `PoolerOutput`

.

## Source code in `vllm/model_executor/layers/pooler/seqwise/poolers.py`


| class SequencePooler(Pooler):
"""A layer that pools specific information from hidden states.
This layer does the following:
1. Extracts specific tokens or aggregates data based on pooling method.
2. Postprocesses the output based on pooling head.
3. Returns structured results as `PoolerOutput`.
"""
def __init__(
self,
pooling: SequencePoolingMethod | SequencePoolingFn,
head: SequencePoolerHead | SequencePoolingHeadFn,
) -> None:
super().__init__()
self.pooling = pooling
self.head = head
def extra_repr(self) -> str:
return (
f"pooling={self.pooling.__class__.__name__}, "
f"head={self.head.__class__.__name__}"
)
def get_supported_tasks(self) -> Set[PoolingTask]:
tasks = set(POOLING_TASKS)
if isinstance(self.pooling, SequencePoolingMethod):
tasks &= self.pooling.get_supported_tasks()
if isinstance(self.head, SequencePoolerHead):
tasks &= self.head.get_supported_tasks()
return tasks
def get_pooling_updates(self, task: PoolingTask) -> PoolingParamsUpdate:
updates = PoolingParamsUpdate()
if isinstance(self.pooling, SequencePoolingMethod):
updates |= self.pooling.get_pooling_updates(task)
return updates
def forward(
self,
hidden_states: torch.Tensor,
pooling_metadata: PoolingMetadata,
) -> SequencePoolerOutput:
pooled_data = self.pooling(hidden_states, pooling_metadata)
pooled_data = self.head(pooled_data, pooling_metadata)
return pooled_data
|