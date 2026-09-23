source: https://docs.vllm.ai/en/latest/api/vllm/distributed/ec_transfer/ec_connector/mooncake/
lastmod: 2026-09-23

#

`vllm.distributed.ec_transfer.ec_connector.mooncake`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.mooncake)

Internal building blocks for the Mooncake encoder-cache connector.

The public connector remains in :mod:`mooncake_ec_connector`

. This package separates configuration, control-plane messaging, transfer state, registered memory, and worker/scheduler orchestration so that each component has one owner and can be tested independently.

Modules:

-
–[config](https://docs.vllm.ai/config/#vllm.distributed.ec_transfer.ec_connector.mooncake.config) -
–[control](https://docs.vllm.ai/control/#vllm.distributed.ec_transfer.ec_connector.mooncake.control)ZMQ control plane for Mooncake encoder-cache reservations and events.

-
–[memory](https://docs.vllm.ai/memory/#vllm.distributed.ec_transfer.ec_connector.mooncake.memory)Registered-memory allocation and residency for Mooncake transfers.

-
–[metadata](https://docs.vllm.ai/metadata/#vllm.distributed.ec_transfer.ec_connector.mooncake.metadata)Metadata exchanged by the Mooncake encoder-cache connector.

-
–[producer](https://docs.vllm.ai/producer/#vllm.distributed.ec_transfer.ec_connector.mooncake.producer)Producer-side push lifecycle, futures, and source-tensor ownership.

-
–[reservation](https://docs.vllm.ai/reservation/#vllm.distributed.ec_transfer.ec_connector.mooncake.reservation)Consumer-side reservation lifecycle and destination-memory ownership.

-
–[scheduler](https://docs.vllm.ai/scheduler/#vllm.distributed.ec_transfer.ec_connector.mooncake.scheduler)Scheduler-side planning and observation for Mooncake cache transfers.

-
–[state](https://docs.vllm.ai/state/#vllm.distributed.ec_transfer.ec_connector.mooncake.state)Scheduler-owned lifecycle and indexes for Consumer-bound transfers.

-
–[transfer](https://docs.vllm.ai/transfer/#vllm.distributed.ec_transfer.ec_connector.mooncake.transfer)Mooncake data-plane engine and memory-registration ownership.

-
–[worker](https://docs.vllm.ai/worker/#vllm.distributed.ec_transfer.ec_connector.mooncake.worker)Worker-side orchestration of Mooncake control, memory, and data planes.