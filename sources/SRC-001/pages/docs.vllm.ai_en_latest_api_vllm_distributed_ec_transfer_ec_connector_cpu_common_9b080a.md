source: https://docs.vllm.ai/en/latest/api/vllm/distributed/ec_transfer/ec_connector/cpu/common/
lastmod: 2026-09-24

#

`vllm.distributed.ec_transfer.ec_connector.cpu.common`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.common)

Shared types for the ECCPUConnector scheduler and worker delegates.

Classes:

-
–[ECCPUConnectorMetadata](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.common.ECCPUConnectorMetadata)Per-step scheduler → worker payload for the ECCPUConnector.

-
–[ECCPUWorkerMetadata](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.common.ECCPUWorkerMetadata)Per-step worker → scheduler payload for the ECCPUConnector.


Functions:

-
–[create_ec_shared_region](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.common.create_ec_shared_region)Build the EC mmap region from

`vllm_config`

.

##

`ECCPUConnectorMetadata`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.common.ECCPUConnectorMetadata)

Bases: [ECConnectorMetadata](https://docs.vllm.ai/base/#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorMetadata)

Per-step scheduler → worker payload for the ECCPUConnector.

Populated by `ECCPUScheduler.build_connector_meta`

; consumed by `ECCPUWorker`

via the mixin's `bind_connector_metadata`

.

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/common.py`


##

`ECCPUWorkerMetadata`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.common.ECCPUWorkerMetadata)

Bases: [ECConnectorWorkerMetadata](https://docs.vllm.ai/base/#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorWorkerMetadata)

Per-step worker → scheduler payload for the ECCPUConnector.

Reports the GPU copies that completed this step: saved mm_hashes become safe to mark ready, and loaded transfers become safe to unpin once every participating rank has reported them. Built by `ECCPUWorker.build_connector_worker_meta`

; consumed by `ECCPUScheduler.update_connector_output`

.

Loads are reported by transfer id rather than mm_hash because every rank copies the same blocks: `aggregate`

concatenates, so an id appears once per reporting rank and the scheduler can count participants off the list.

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/common.py`


##

`_get_encoder_cache_hidden_dim(vllm_config)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.common._get_encoder_cache_hidden_dim)

Return the per-token hidden dimension for encoder cache entries.

For most models this equals the LLM's hidden size. Qwen3-VL (and any future model with deepstack visual encoding) is an exception: the ViT concatenates its own output with features from N decoder layers before storing in encoder_cache, producing a tensor of width `out_hidden_size * (1 + N)`

per visual token. Using the plain LLM hidden size would under-allocate EC blocks and silently truncate the transferred data, leading to a shape mismatch on the consumer.

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/common.py`


##

`create_ec_shared_region(vllm_config)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.common.create_ec_shared_region)

Build the EC mmap region from `vllm_config`

.

Both `ECCPUScheduler`

and `ECCPUWorker`

call this to get the same shared region (same engine_id, same block_size_bytes).