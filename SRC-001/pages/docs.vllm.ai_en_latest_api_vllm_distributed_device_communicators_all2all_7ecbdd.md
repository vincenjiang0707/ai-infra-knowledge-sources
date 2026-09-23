source: https://docs.vllm.ai/en/latest/api/vllm/distributed/device_communicators/all2all/
lastmod: 2026-09-23

#

`vllm.distributed.device_communicators.all2all`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all)

Classes:

-
–[AgRsAll2AllManager](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.AgRsAll2AllManager)An implementation of all2all communication based on

-
–[DeepEPAll2AllManagerBase](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.DeepEPAll2AllManagerBase)All2All communication based on DeepEP High-Throughput kernels.

-
–[DeepEPHTAll2AllManager](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.DeepEPHTAll2AllManager)All2All communication based on DeepEP High-Throughput kernels.

-
–[DeepEPLLAll2AllManager](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.DeepEPLLAll2AllManager)All2All communication based on DeepEP Low-Latency kernels.

-
–[DeepEPV2All2AllManager](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.DeepEPV2All2AllManager)All2All communication based on DeepEP v2 ElasticBuffer (unified API).

-
–[FlashInferNVLinkOneSidedManager](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.FlashInferNVLinkOneSidedManager)All2All communication based on FlashInfer's MoeAlltoAll/One-sided NVLink kernel.

-
–[FlashInferNVLinkTwoSidedManager](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.FlashInferNVLinkTwoSidedManager)All2All communication based on flashinfer all2allv/two-sided NVLink kernels.

-
–[MoonEPAll2AllManager](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.MoonEPAll2AllManager)All2All communication based on MoonEP

-
–[NixlEPAll2AllManager](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.NixlEPAll2AllManager)All2All communication based on NIXL EP kernels.


##

`AgRsAll2AllManager`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.AgRsAll2AllManager)

Bases: [All2AllManagerBase](https://docs.vllm.ai/base_device_communicator/#vllm.distributed.device_communicators.base_device_communicator.All2AllManagerBase)

An implementation of all2all communication based on all-gather (dispatch) and reduce-scatter (combine).

Methods:

-
–[combine](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.AgRsAll2AllManager.combine)Reduce-scatter hidden_states across all dp ranks.

-
–[dispatch](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.AgRsAll2AllManager.dispatch)Gather hidden_states and router_logits from all dp ranks.

-
–[dispatch_router_logits](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.AgRsAll2AllManager.dispatch_router_logits)Gather hidden_states and router_logits from all dp ranks.


## Source code in `vllm/distributed/device_communicators/all2all.py`


|
|

###

`combine(hidden_states, is_sequence_parallel=False)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.AgRsAll2AllManager.combine)

Reduce-scatter hidden_states across all dp ranks.

## Source code in `vllm/distributed/device_communicators/all2all.py`


###

`dispatch(hidden_states, topk_weights, topk_ids, is_sequence_parallel=False, extra_tensors=None)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.AgRsAll2AllManager.dispatch)

Gather hidden_states and router_logits from all dp ranks.

## Source code in `vllm/distributed/device_communicators/all2all.py`


###

`dispatch_router_logits(hidden_states, router_logits, is_sequence_parallel=False, extra_tensors=None)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.AgRsAll2AllManager.dispatch_router_logits)

Gather hidden_states and router_logits from all dp ranks.

## Source code in `vllm/distributed/device_communicators/all2all.py`


##

`DeepEPAll2AllManagerBase`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.DeepEPAll2AllManagerBase)

Bases: [All2AllManagerBase](https://docs.vllm.ai/base_device_communicator/#vllm.distributed.device_communicators.base_device_communicator.All2AllManagerBase)

All2All communication based on DeepEP High-Throughput kernels.

## Source code in `vllm/distributed/device_communicators/all2all.py`


##

`DeepEPHTAll2AllManager`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.DeepEPHTAll2AllManager)

Bases: [DeepEPAll2AllManagerBase](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.DeepEPAll2AllManagerBase)

All2All communication based on DeepEP High-Throughput kernels.

## Source code in `vllm/distributed/device_communicators/all2all.py`


##

`DeepEPLLAll2AllManager`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.DeepEPLLAll2AllManager)

Bases: [DeepEPAll2AllManagerBase](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.DeepEPAll2AllManagerBase)

All2All communication based on DeepEP Low-Latency kernels.

Methods:

-
–[get_handle](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.DeepEPLLAll2AllManager.get_handle)The kwargs for DeepEPLLAll2AllManager is dictated by


## Source code in `vllm/distributed/device_communicators/all2all.py`


|
|

###

`_make_all2all_kwargs(max_num_tokens_per_dp_rank, token_hidden_size, num_ep_ranks, num_global_experts, num_local_experts)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.DeepEPLLAll2AllManager._make_all2all_kwargs)

## the maximum number of tokens a DP rank

can dispatch all the ranks must hold the same value.

token_hidden_size: the hidden dimension of each token. num_ep_ranks: the number of EP group ranks. num_global_experts: Number of experts in the model. num_local_experts: Number of experts in an EP rank.

## Source code in `vllm/distributed/device_communicators/all2all.py`


###

`get_handle(kwargs)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.DeepEPLLAll2AllManager.get_handle)

The kwargs for DeepEPLLAll2AllManager is dictated by _make_all2all_kwargs.

## Source code in `vllm/distributed/device_communicators/all2all.py`


##

`DeepEPV2All2AllManager`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.DeepEPV2All2AllManager)

Bases: [All2AllManagerBase](https://docs.vllm.ai/base_device_communicator/#vllm.distributed.device_communicators.base_device_communicator.All2AllManagerBase)

All2All communication based on DeepEP v2 ElasticBuffer (unified API). Uses NCCL Gin backend with analytical SM calculation.

## Source code in `vllm/distributed/device_communicators/all2all.py`


|
|

##

`FlashInferNVLinkOneSidedManager`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.FlashInferNVLinkOneSidedManager)

Bases: [All2AllManagerBase](https://docs.vllm.ai/base_device_communicator/#vllm.distributed.device_communicators.base_device_communicator.All2AllManagerBase)

All2All communication based on FlashInfer's MoeAlltoAll/One-sided NVLink kernel. This is a newer kernel from trtllm that should perform better than the kernel used by flashinfer_nvlink_two_sided.

Methods:

-
–[cleanup](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.FlashInferNVLinkOneSidedManager.cleanup)Clean up resources.

-
–[combine_into](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.FlashInferNVLinkOneSidedManager.combine_into)Combine into

`output`

, with a fallback for older FlashInfer. -
–[initialize](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.FlashInferNVLinkOneSidedManager.initialize)Initialize (or grow) the MoeAlltoAll workspace.


## Source code in `vllm/distributed/device_communicators/all2all.py`


|
|

###

`cleanup()`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.FlashInferNVLinkOneSidedManager.cleanup)

Clean up resources.

## Source code in `vllm/distributed/device_communicators/all2all.py`


###

`combine_into(payload, runtime_max_tokens_per_rank, output)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.FlashInferNVLinkOneSidedManager.combine_into)

Combine into `output`

, with a fallback for older FlashInfer.

## Source code in `vllm/distributed/device_communicators/all2all.py`


###

`initialize(max_num_tokens, top_k, num_experts, hidden_size, x_bytes_per_token, x_sf_bytes_per_token)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.FlashInferNVLinkOneSidedManager.initialize)

Initialize (or grow) the MoeAlltoAll workspace.

## Source code in `vllm/distributed/device_communicators/all2all.py`


|
|

##

`FlashInferNVLinkTwoSidedManager`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.FlashInferNVLinkTwoSidedManager)

Bases: [All2AllManagerBase](https://docs.vllm.ai/base_device_communicator/#vllm.distributed.device_communicators.base_device_communicator.All2AllManagerBase)

All2All communication based on flashinfer all2allv/two-sided NVLink kernels.

Methods:

-
–[cleanup](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.FlashInferNVLinkTwoSidedManager.cleanup)Clean up workspace.

-
–[ensure_alltoall_workspace_initialized](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.FlashInferNVLinkTwoSidedManager.ensure_alltoall_workspace_initialized)Ensure workspace is initialized.

-
–[initialize](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.FlashInferNVLinkTwoSidedManager.initialize)Initialize workspace.


## Source code in `vllm/distributed/device_communicators/all2all.py`


|
|

###

`cleanup()`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.FlashInferNVLinkTwoSidedManager.cleanup)

Clean up workspace.

## Source code in `vllm/distributed/device_communicators/all2all.py`


###

`ensure_alltoall_workspace_initialized()`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.FlashInferNVLinkTwoSidedManager.ensure_alltoall_workspace_initialized)

Ensure workspace is initialized.

## Source code in `vllm/distributed/device_communicators/all2all.py`


###

`initialize(world_size, rank, gpus_per_node)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.FlashInferNVLinkTwoSidedManager.initialize)

Initialize workspace.

## Source code in `vllm/distributed/device_communicators/all2all.py`


##

`MoonEPAll2AllManager`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.MoonEPAll2AllManager)

Bases: [All2AllManagerBase](https://docs.vllm.ai/base_device_communicator/#vllm.distributed.device_communicators.base_device_communicator.All2AllManagerBase)

All2All communication based on MoonEP (https://github.com/MoonshotAI/MoonEP).

MoonEP keeps token loads perfectly balanced across EP ranks by planning a small number of dynamically redundant experts online and prefetching their weights before expert compute. Every rank receives exactly S x K token slots regardless of router skew, so all communication and compute shapes are static.

Requires NVLink symmetric-memory / multicast capable topologies (single node NVSwitch, e.g. H100/H200/B200/GB300 class).

## Source code in `vllm/distributed/device_communicators/all2all.py`


|
|

##

`NixlEPAll2AllManager`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.NixlEPAll2AllManager)

Bases: [All2AllManagerBase](https://docs.vllm.ai/base_device_communicator/#vllm.distributed.device_communicators.base_device_communicator.All2AllManagerBase)

All2All communication based on NIXL EP kernels. This backend supports elastic EP with dynamic rank connection/disconnection.

Methods:

-
–[commit_ep_size](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.NixlEPAll2AllManager.commit_ep_size)Commit the staged EP size to the active communication set.


## Source code in `vllm/distributed/device_communicators/all2all.py`


|
|

###

`commit_ep_size()`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.all2all.NixlEPAll2AllManager.commit_ep_size)

Commit the staged EP size to the active communication set.