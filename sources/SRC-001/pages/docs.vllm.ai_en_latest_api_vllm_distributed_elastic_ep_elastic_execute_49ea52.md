source: https://docs.vllm.ai/en/latest/api/vllm/distributed/elastic_ep/elastic_execute/
lastmod: 2026-09-24

#

`vllm.distributed.elastic_ep.elastic_execute`

[¶](https://docs.vllm.ai#vllm.distributed.elastic_ep.elastic_execute)

Functions:

-
–[can_reuse_fused_moe_kernel](https://docs.vllm.ai#vllm.distributed.elastic_ep.elastic_execute.can_reuse_fused_moe_kernel)Whether fused MoE kernels can be reused across EP rank changes.


##

`can_reuse_fused_moe_kernel(parallel_config)`

[¶](https://docs.vllm.ai#vllm.distributed.elastic_ep.elastic_execute.can_reuse_fused_moe_kernel)

Whether fused MoE kernels can be reused across EP rank changes.

The EP backend must preserve its CUDA graph entries when ranks are connected, disconnected, masked, or unmasked.