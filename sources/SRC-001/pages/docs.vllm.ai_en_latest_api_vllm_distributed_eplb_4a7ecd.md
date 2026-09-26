source: https://docs.vllm.ai/en/latest/api/vllm/distributed/eplb/
lastmod: 2026-09-24

#

`vllm.distributed.eplb`

[¶](https://docs.vllm.ai#vllm.distributed.eplb)

Expert parallelism load balancer (EPLB).

Modules:

-
–[async_worker](https://docs.vllm.ai/async_worker/#vllm.distributed.eplb.async_worker)The async worker that transfers experts in the background.

-
–[eplb_communicator](https://docs.vllm.ai/eplb_communicator/#vllm.distributed.eplb.eplb_communicator)EPLB communicator implementations and factory.

-
–[eplb_state](https://docs.vllm.ai/eplb_state/#vllm.distributed.eplb.eplb_state)Expert parallelism load balancer (EPLB) metrics and states.

-
–[eplb_utils](https://docs.vllm.ai/eplb_utils/#vllm.distributed.eplb.eplb_utils)Utility functions for EPLB (Expert Parallel Load Balancing).

-
–[policy](https://docs.vllm.ai/policy/#vllm.distributed.eplb.policy) -
–[rebalance_execute](https://docs.vllm.ai/rebalance_execute/#vllm.distributed.eplb.rebalance_execute)The actual execution of the rearrangement.