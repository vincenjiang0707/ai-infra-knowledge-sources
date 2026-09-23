source: https://docs.vllm.ai/en/latest/api/vllm/distributed/ec_transfer/ec_connector/cpu/
lastmod: 2026-09-23

#

`vllm.distributed.ec_transfer.ec_connector.cpu`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu)

Modules:

-
–[common](https://docs.vllm.ai/common/#vllm.distributed.ec_transfer.ec_connector.cpu.common)Shared types for the ECCPUConnector scheduler and worker delegates.

-
–[connector](https://docs.vllm.ai/connector/#vllm.distributed.ec_transfer.ec_connector.cpu.connector)ECCPUConnector — CPU encoder-cache offloading.

-
–[control](https://docs.vllm.ai/control/#vllm.distributed.ec_transfer.ec_connector.cpu.control) -
–[data](https://docs.vllm.ai/data/#vllm.distributed.ec_transfer.ec_connector.cpu.data) -
–[ec_shared_region](https://docs.vllm.ai/ec_shared_region/#vllm.distributed.ec_transfer.ec_connector.cpu.ec_shared_region)Lightweight mmap-backed shared memory region for encoder cache (EC) data.

-
–[protocol](https://docs.vllm.ai/protocol/#vllm.distributed.ec_transfer.ec_connector.cpu.protocol)Scheduler-side wire types for the ECCPUConnector.

-
–[scheduler](https://docs.vllm.ai/scheduler/#vllm.distributed.ec_transfer.ec_connector.cpu.scheduler)ECCPUScheduler — CPU offload scheduler delegate.

-
–[session](https://docs.vllm.ai/session/#vllm.distributed.ec_transfer.ec_connector.cpu.session)Session objects for the ECCPUConnector.

-
–[utils](https://docs.vllm.ai/utils/#vllm.distributed.ec_transfer.ec_connector.cpu.utils)Supporting utilities for the ECCPUConnector scheduler.

-
–[worker](https://docs.vllm.ai/worker/#vllm.distributed.ec_transfer.ec_connector.cpu.worker)Worker-side of the ECCPUConnector.