source: https://docs.vllm.ai/en/latest/api/vllm/distributed/ec_transfer/ec_connector/mooncake/metadata/
lastmod: 2026-09-23

#

`vllm.distributed.ec_transfer.ec_connector.mooncake.metadata`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.mooncake.metadata)

Metadata exchanged by the Mooncake encoder-cache connector.

Classes:

-
–[ECMooncakeConnectorMetadata](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.mooncake.metadata.ECMooncakeConnectorMetadata)Worker operations emitted for one Scheduler step.

-
–[ECMooncakeLoadSpec](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.mooncake.metadata.ECMooncakeLoadSpec)Describe a remote reservation or resident allocation to load.

-
–[ECMooncakePushSpec](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.mooncake.metadata.ECMooncakePushSpec)Describe a destination reservation prepared before a tensor is ready.

-
–[ECMooncakeWorkerMetadata](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.mooncake.metadata.ECMooncakeWorkerMetadata)Completion state reported from Workers to the Scheduler.


##

`ECMooncakeConnectorMetadata`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.mooncake.metadata.ECMooncakeConnectorMetadata)

Bases: [ECConnectorMetadata](https://docs.vllm.ai/base/#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorMetadata)

Worker operations emitted for one Scheduler step.

## Source code in `vllm/distributed/ec_transfer/ec_connector/mooncake/metadata.py`


##

`ECMooncakeLoadSpec`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.mooncake.metadata.ECMooncakeLoadSpec)

Describe a remote reservation or resident allocation to load.

## Source code in `vllm/distributed/ec_transfer/ec_connector/mooncake/metadata.py`


##

`ECMooncakePushSpec`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.mooncake.metadata.ECMooncakePushSpec)

Describe a destination reservation prepared before a tensor is ready.

## Source code in `vllm/distributed/ec_transfer/ec_connector/mooncake/metadata.py`


##

`ECMooncakeWorkerMetadata`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.mooncake.metadata.ECMooncakeWorkerMetadata)

Bases: [ECConnectorWorkerMetadata](https://docs.vllm.ai/base/#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorWorkerMetadata)

Completion state reported from Workers to the Scheduler.