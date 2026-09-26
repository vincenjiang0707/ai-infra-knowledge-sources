source: https://docs.vllm.ai/en/latest/api/vllm/distributed/eplb/eplb_state/
lastmod: 2026-09-24

#

`vllm.distributed.eplb.eplb_state`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state)

Expert parallelism load balancer (EPLB) metrics and states.

## Glossary[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state--glossary)

**Logical Expert**: An expert that is part of the model's logical structure. It holds a set of weights and is replicated across multiple physical experts.**Redundant Expert**: To achieve load balancing, for some popular logical experts, we create additional copies of the expert weights. During inference, each of these copies can be routed to by the same set of tokens.**Physical Expert**: An expert that is instantiated on a specific device. It is a replica of a logical expert and can be rearranged across devices. I.e., one logical expert may have multiple sets of weights initialized on different devices, and each of these sets is a physical expert.**Local Physical Expert**: A physical expert that is instantiated on the current device.

For example: DeepSeek-R1 has 256 logical experts, so each MoE layer has 256 sets of linear layer weights in the model parameters. If we add 32 redundant experts, DeepSeek-R1 will have 256 + 32 = 288 physical experts in total. And when deploying, we'll have 288 sets of linear layer weights for each MoE layer. If we have 32 EP ranks, then each GPU will hold 288 / 32 = 9 local physical experts.

Classes:

-
–[EplbLayerState](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbLayerState)Runtime EPLB data stored in the MoE layer.

-
–[EplbModelState](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbModelState)EPLB metrics.

-
–[EplbState](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState)EplbState of each expert parallel model. Key is the model config hash.

-
–[EplbStats](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbStats)Model stats used in EPLB rebalancing algorithm.


Functions:

-
–[compute_logical_maps](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.compute_logical_maps)Derive logical_to_physical_map and logical_replica_count from


##

`EplbLayerState`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbLayerState)

Runtime EPLB data stored in the MoE layer.

Attributes:

-
([num_unpadded_tokens_tensors](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbLayerState.num_unpadded_tokens_tensors)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)] | NoneReference to the parent :class:

`EplbModelState`

's tensor list so the -
([should_record_tensor](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbLayerState.should_record_tensor)

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| NoneShared scalar bool tensor controlling whether to accumulate expert load


## Source code in `vllm/distributed/eplb/eplb_state.py`


###

`num_unpadded_tokens_tensors = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbLayerState.num_unpadded_tokens_tensors)

Reference to the parent :class:`EplbModelState`

's tensor list so the router can read the correct per-[u]batch unpadded token count.

###

`should_record_tensor = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbLayerState.should_record_tensor)

Shared scalar bool tensor controlling whether to accumulate expert load metrics during this forward pass. All layers reference the **same** tensor object, which is owned and updated by :class:`EplbState`

.

Set to `False`

for the first `step_interval - window_size`

steps of each rearrangement period: those steps would be overwritten in the sliding window before the next rearrangement, so recording them wastes GPU work.

##

`EplbModelState`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbModelState)

EPLB metrics.

Attributes:

-
([communicator](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbModelState.communicator)

) –[EplbCommunicator](https://docs.vllm.ai/eplb_communicator/#vllm.distributed.eplb.eplb_communicator.EplbCommunicator)The communicator for expert weight transfers.

-
([device_index](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbModelState.device_index)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneDevice index for the async EPLB worker thread.

-
([eplb_stats](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbModelState.eplb_stats)

) –[EplbStats](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbStats)| NoneEPLB stats for the model.

-
([expert_buffer](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbModelState.expert_buffer)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]The buffer to store the expert weights during transfer.

-
([expert_load_pass](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbModelState.expert_load_pass)

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Expert load during this forward pass.

-
([expert_load_pass_buffer](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbModelState.expert_load_pass_buffer)

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Maximum-capacity buffer backing

`expert_load_pass`

. -
([expert_load_window](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbModelState.expert_load_window)

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)A sliding window of expert load.

-
([logical_replica_count](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbModelState.logical_replica_count)

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Number of replicas for each logical expert.

-
([logical_to_physical_map](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbModelState.logical_to_physical_map)

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Mapping from logical experts to physical experts.

-
([num_unpadded_tokens_tensors](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbModelState.num_unpadded_tokens_tensors)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)] | NonePer-ubatch scalar int32 tensors holding the number of real (non-padding)

-
([pending_result](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbModelState.pending_result)

) –[AsyncEplbLayerResult](https://docs.vllm.ai/rebalance_execute/#vllm.distributed.eplb.rebalance_execute.AsyncEplbLayerResult)| NoneSet by the async worker after all writes to expert_buffer are done. Consumed

-
([physical_to_logical_map](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbModelState.physical_to_logical_map)

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Mapping from physical experts to logical experts.

-
([physical_to_logical_map_buffer](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbModelState.physical_to_logical_map_buffer)

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Maximum-capacity buffer backing

`physical_to_logical_map`

. -
([rebalanced](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbModelState.rebalanced)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)This flag is only used when running Async EPLB. It is set to True by the main thread


## Source code in `vllm/distributed/eplb/eplb_state.py`


|
|

###

`communicator`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbModelState.communicator)

The communicator for expert weight transfers.

###

`device_index`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbModelState.device_index)

Device index for the async EPLB worker thread.

###

`eplb_stats`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbModelState.eplb_stats)

EPLB stats for the model.

###

`expert_buffer`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbModelState.expert_buffer)

The buffer to store the expert weights during transfer.

###

`expert_load_pass`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbModelState.expert_load_pass)

Expert load during this forward pass. We use the token count each expert processes as the load.

Shape: (num_moe_layers, num_physical_experts)

###

`expert_load_pass_buffer`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbModelState.expert_load_pass_buffer)

Maximum-capacity buffer backing `expert_load_pass`

.

###

`expert_load_window`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbModelState.expert_load_window)

A sliding window of expert load.

Shape: (window_size, num_moe_layers, num_physical_experts)

NOTE: The expert_load_view now records load for all physical experts rather than just local experts. This ensures consistent load statistics across different dispatch methods (naive all-to-all, DeepEP). The recorded load will be multiplied by dp_size when using naive all-to-all due to each DP rank contributing the same token set to the calculation. See: https://github.com/vllm-project/vllm/pull/22167#pullrequestreview-3086143856

###

`logical_replica_count`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbModelState.logical_replica_count)

Number of replicas for each logical expert. This is exactly the non-`-1`

count in the `logical_to_physical_map`

.

Shape: (num_moe_layers, num_logical_experts)

#### Example[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbModelState.logical_replica_count--example)

For a 2-layer MoE model with 6 physical experts and 4 logical experts on 3 EP ranks, the count could look like this:

``` [[2, 2, 1, 1], [3, 1, 1, 1]]

###

`logical_to_physical_map`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbModelState.logical_to_physical_map)

Mapping from logical experts to physical experts.

This is a sparse matrix, where -1 indicates no mapping.

Shape: (num_moe_layers, num_logical_experts, num_redundant_experts + 1)

#### Example[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbModelState.logical_to_physical_map--example)

For a 2-layer MoE model with 6 physical experts and 4 logical experts on 3 EP ranks, the mapping could look like this:

###

`num_unpadded_tokens_tensors = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbModelState.num_unpadded_tokens_tensors)

Per-ubatch scalar int32 tensors holding the number of real (non-padding) tokens. Allocated once in :meth:`EplbState.add_model`

so that device pointers remain stable across CUDA-graph replays. The router kernel indexes this list with `dbo_current_ubatch_id()`

.

###

`pending_result = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbModelState.pending_result)

Set by the async worker after all writes to expert_buffer are done. Consumed and reset to None by the main thread in move_to_workspace() after the contents of expert_buffer have been transferred out. At most one result is pending at a time.

pending_result relies on the GIL to synchronize access between the main thread and the async worker.

###

`physical_to_logical_map`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbModelState.physical_to_logical_map)

Mapping from physical experts to logical experts.

Shape: (num_moe_layers, num_physical_experts)

#### Example[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbModelState.physical_to_logical_map--example)

For a 2-layer MoE model with 6 physical experts and 4 logical experts on 3 EP ranks, the mapping could look like this:

###

`physical_to_logical_map_buffer`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbModelState.physical_to_logical_map_buffer)

Maximum-capacity buffer backing `physical_to_logical_map`

.

###

`rebalanced`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbModelState.rebalanced)

This flag is only used when running Async EPLB. It is set to True by the main thread after the new expert maps have been computed. This indicates that the async worker should start transferring weights. move_to_workspace sets this flag to False when all weights have been transferred and the new map has been successfully committed.

rebalanced relies on the GIL to synchronize access between the main thread and the async worker.

##

`EplbState`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState)

EplbState of each expert parallel model. Key is the model config hash.

Methods:

-
–[add_model](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.add_model)Build the initial EPLB state.

-
–[build_initial_global_physical_to_logical_map](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.build_initial_global_physical_to_logical_map)Build an initial expert arrangement using the following structure:

-
–[drain_async](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.drain_async)Drain in-flight async EPLB by consuming all remaining layer results.

-
–[prepare_forward](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.prepare_forward)Fill the per-[u]batch

`num_unpadded_tokens`

tensors before a -
–[rearrange](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.rearrange)Rearrange the experts according to the current load.

-
–[reconfigure_physical_expert_slots](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.reconfigure_physical_expert_slots)Replace physical_to_logical_map and expert_load_pass with views

-
–[step](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.step)Step the EPLB state.

-
–[validate_ep_configuration](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.validate_ep_configuration)Validate that the expert parallel configuration of


Attributes:

-
([async_worker](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.async_worker)

) –[Thread](https://docs.python.org/3/library/threading.html#threading.Thread)| NoneBackground thread handling async transfers.

-
([device_index](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.device_index)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneDevice index for the async EPLB worker thread.

-
([expert_load_window_size](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.expert_load_window_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Size of the expert load sliding window.

-
([expert_load_window_step](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.expert_load_window_step)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Current step in the sliding window.

-
([expert_rearrangement_step](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.expert_rearrangement_step)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Steps after last rearrangement.

-
([expert_rearrangement_step_interval](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.expert_rearrangement_step_interval)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Interval for expert rearrangement steps.

-
([is_async](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.is_async)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)The flag indicates whether the EPLB is running in async mode.

-
([policy](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.policy)

) –[type](https://docs.python.org/3/builtins/functions.html#type)[[AbstractEplbPolicy](https://docs.vllm.ai/policy/#vllm.distributed.eplb.policy.AbstractEplbPolicy)]Selected EPLB algorithm class

-
([rearrange_event](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.rearrange_event)

) –[CpuGpuEvent](https://docs.vllm.ai/eplb_utils/#vllm.distributed.eplb.eplb_utils.CpuGpuEvent)Event to signal when a new rearrangement is needed for the async thread.

-
([should_record_tensor](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.should_record_tensor)

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| NoneShared scalar bool tensor for all layers. Every


## Source code in `vllm/distributed/eplb/eplb_state.py`


|
|

###

`async_worker = None`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.async_worker)

Background thread handling async transfers.

###

`device_index = None`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.device_index)

Device index for the async EPLB worker thread.

###

`expert_load_window_size = 0`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.expert_load_window_size)

Size of the expert load sliding window. This is a constant and is taken from the config.

###

`expert_load_window_step = 0`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.expert_load_window_step)

Current step in the sliding window.

Different from `expert_rearrangement_step`

, each EP rank may have its own `expert_load_window_step`

.

###

`expert_rearrangement_step = 0`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.expert_rearrangement_step)

Steps after last rearrangement. Will trigger a rearrangement if it exceeds the threshold.

NOTE: Keep in mind that all EP ranks need to have the same `expert_rearrangement_step`

value to ensure synchronization. Otherwise, the rearrangement will hang at collective communication calls.

###

`expert_rearrangement_step_interval = 0`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.expert_rearrangement_step_interval)

Interval for expert rearrangement steps. This is a constant and is taken from the config.

###

`is_async = False`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.is_async)

The flag indicates whether the EPLB is running in async mode.

###

`policy = DefaultEplbPolicy`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.policy)

Selected EPLB algorithm class

###

`rearrange_event = CpuGpuEvent()`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.rearrange_event)

Event to signal when a new rearrangement is needed for the async thread.

###

`should_record_tensor = None`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.should_record_tensor)

Shared scalar bool tensor for all layers. Every :class:`EplbLayerState`

holds a reference to the **same** object so a single `.fill_()`

updates all layers at once. Allocated on the first call to :meth:`_propagate_shared_tensors`

.

###

`_allreduce_list(tensor_list)`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState._allreduce_list)

All-reduce a list of tensors.

## Source code in `vllm/distributed/eplb/eplb_state.py`


###

`_propagate_shared_tensors(model, num_unpadded_tokens_tensors)`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState._propagate_shared_tensors)

Propagate shared tensors to every :class:`EplbLayerState`

.

Allocates `should_record_tensor`

on the first call and then assigns both it and `num_unpadded_tokens_tensors`

to every MoE layer's :class:`EplbLayerState`

. All layers reference the **same** objects so a single update is visible everywhere.

Must be called after :meth:`model.set_eplb_state`

so that each layer's `eplb_state`

is already populated.

## Source code in `vllm/distributed/eplb/eplb_state.py`


###

`_should_record_current_step(log_stats=False)`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState._should_record_current_step)

Return whether expert-load recording should be enabled this step.

Recording is enabled when we are close to either: 1) The next rearrangement step, so the sliding window is ready. 2) The next balancedness logging step, when log_stats is enabled.

## Source code in `vllm/distributed/eplb/eplb_state.py`


###

`_sync_load_pass()`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState._sync_load_pass)

Sync the expert load pass across all ranks for log stats. Doesn't update the expert load pass in eplb_model_state.

## Source code in `vllm/distributed/eplb/eplb_state.py`


###

`_update_layer_should_record(log_stats=False)`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState._update_layer_should_record)

Update the shared `should_record_tensor`

for all layers.

## Source code in `vllm/distributed/eplb/eplb_state.py`


###

`add_model(model, model_config)`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.add_model)

Build the initial EPLB state.

## Source code in `vllm/distributed/eplb/eplb_state.py`


|
|

###

`build_initial_global_physical_to_logical_map(num_routed_experts, num_redundant_experts)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.build_initial_global_physical_to_logical_map)

Build an initial expert arrangement using the following structure: [original routed experts, redundant experts]

Returns:

-
(`physical_to_logical_map`


) –[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[int](https://docs.python.org/3/builtins/functions.html#int)]A list of integers, where each integer is the index of the logical expert that the corresponding physical expert maps to.


## Source code in `vllm/distributed/eplb/eplb_state.py`


###

`drain_async()`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.drain_async)

Drain in-flight async EPLB by consuming all remaining layer results.

Each pending result is acknowledged (consumed_event recorded) so the async worker can proceed, but the transferred weights are intentionally NOT applied — a full rearrange is expected to follow.

Ranks are kept in lockstep via _all_ranks_result_ready (all_reduce on the EP CPU group). The async worker's coordinated-stop collectives use the separate EPLB group, so the two sets of collectives do not interfere.

No-op when no async cycle is in progress (rebalanced=False).

## Source code in `vllm/distributed/eplb/eplb_state.py`


###

`prepare_forward(model_config, num_unpadded_tokens, ubatch_slices=None)`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.prepare_forward)

Fill the per-[u]batch `num_unpadded_tokens`

tensors before a forward pass.

Parameters:

-

(`model_config`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.prepare_forward(model_config))

) –[ModelConfig](https://docs.vllm.ai/config/#vllm.config.ModelConfig)Identifies which

`EplbModelState`

to update. -

(`num_unpadded_tokens`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.prepare_forward(num_unpadded_tokens))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Total number of real (non-padding) tokens in the batch.

-

(`ubatch_slices`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.prepare_forward(ubatch_slices))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)| None`None`

) –When DBO is active, a list of

`UBatchSlice`

objects describing each micro-batch's token range. When`None`

, only`tensors[0]`

is filled.

## Source code in `vllm/distributed/eplb/eplb_state.py`


###

`rearrange(is_profile=False, rank_mapping=None)`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.rearrange)

Rearrange the experts according to the current load.

Parameters:

-

(`is_profile`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.rearrange(is_profile))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –If

`True`

, perform a dummy rearrangement. This is used in`profile_run`

to reserve enough memory, no memory movement will be performed. Default is False. -

(`rank_mapping`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.rearrange(rank_mapping))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int)] | None`None`

) –The rank mapping when scaling is done in EEP.


## Source code in `vllm/distributed/eplb/eplb_state.py`


|
|

###

`reconfigure_physical_expert_slots(model_config, num_physical_experts)`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.reconfigure_physical_expert_slots)

Replace physical_to_logical_map and expert_load_pass with views covering the new active size.

## Source code in `vllm/distributed/eplb/eplb_state.py`


###

`step(is_dummy=False, is_profile=False, log_stats=False)`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.step)

Step the EPLB state.

Parameters:

-

(`is_dummy`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.step(is_dummy))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –If

`True`

, this is a dummy step and the load metrics recorded in this forward pass will not count. Defaults to`False`

. -

(`is_profile`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.step(is_profile))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –If

`True`

, perform a dummy rearrangement with maximum communication cost. This is used in`profile_run`

to reserve enough memory for the communication buffer. -

(`log_stats`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.step(log_stats))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –If

`True`

, log the expert load metrics.

#### Stats[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.step--stats)

```
The metrics are all summed up across layers.
- `avg_tokens`: The average load across ranks.
- `max_tokens`: The maximum load across ranks.
- `balancedness`: The ratio of average load to maximum load.
```


## Source code in `vllm/distributed/eplb/eplb_state.py`


|
|

###

`validate_ep_configuration(new_model)`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbState.validate_ep_configuration)

Validate that the expert parallel configuration of the new model is the same as the existing models.

## Source code in `vllm/distributed/eplb/eplb_state.py`


##

`EplbStats`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbStats)

Model stats used in EPLB rebalancing algorithm.

Attributes:

-
([global_expert_load_window](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbStats.global_expert_load_window)

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Experts load window.

-
([num_gpus](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbStats.num_gpus)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of GPUs.

-
([num_groups](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbStats.num_groups)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of expert groups.

-
([num_nodes](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbStats.num_nodes)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of nodes.

-
([num_replicas](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbStats.num_replicas)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of physical experts.


## Source code in `vllm/distributed/eplb/eplb_state.py`


###

`global_expert_load_window`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbStats.global_expert_load_window)

Experts load window. Shape: (window_size, num_moe_layers, num_physical_experts)

###

`num_gpus`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbStats.num_gpus)

Number of GPUs.

###

`num_groups`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbStats.num_groups)

Number of expert groups.

###

`num_nodes`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbStats.num_nodes)

Number of nodes.

###

`num_replicas`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.EplbStats.num_replicas)

Number of physical experts.

##

`_commit_eplb_maps(model_state, new_physical_to_logical_map)`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state._commit_eplb_maps)

Copies all of the new_* maps into model_state. After this function completes, the new mappings will become the current mappings and will be visible to the model.

## Source code in `vllm/distributed/eplb/eplb_state.py`


##

`_commit_eplb_maps_for_layer(model_state, new_physical_to_logical_map, layer)`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state._commit_eplb_maps_for_layer)

Per-layer version of *commit_eplb_maps that's used by the sync portion of EPLB when running async EPLB. Copies all of the new** maps into model_state. After this function completes, the new mappings will become the current mappings and will be visible to the model.

## Source code in `vllm/distributed/eplb/eplb_state.py`


##

`compute_logical_maps(physical_to_logical_map, num_logical_experts)`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.compute_logical_maps)

Derive logical_to_physical_map and logical_replica_count from physical_to_logical_map.

Parameters:

-

(`physical_to_logical_map`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.compute_logical_maps(physical_to_logical_map))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[num_layers, num_physical_experts], logical expert index for each physical expert slot

-

(`num_logical_experts`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_state.compute_logical_maps(num_logical_experts))

) –[int](https://docs.python.org/3/builtins/functions.html#int)total number of logical experts


Returns:

-
(`logical_to_physical_map`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[num_layers, num_logical_experts, max_replicas], physical slots per logical expert; -1 where unused

-
(`logical_replica_count`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[num_layers, num_logical_experts], number of physical replicas per logical expert


## Source code in `vllm/distributed/eplb/eplb_state.py`


|
|