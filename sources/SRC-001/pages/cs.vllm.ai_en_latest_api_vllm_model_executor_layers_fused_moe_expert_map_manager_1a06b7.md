source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/expert_map_manager/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.fused_moe.expert_map_manager`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager)

Expert Map Manager for MoE layers.

This module contains the ExpertMapManager class which manages expert ID mappings and placement strategies for Expert Parallelism in MoE models.

Classes:

-
–[ExpertMapManager](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager)Manages expert ID mappings and placement for Expert Parallelism.


Functions:

-
–[determine_expert_map](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.determine_expert_map)Calculates how many experts should be assigned to each rank for EP and


##

`ExpertMapManager`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager)

Manages expert ID mappings and placement for Expert Parallelism.

Responsibilities: - Calculate local vs global expert counts - Map between global, local, and physical expert IDs - Manage placement strategies (linear, round_robin) - Maintain routing tables for round-robin placement - Support dynamic reconfiguration of EP topology

When expert_map is required: - Expert Parallelism (EP) is enabled, i.e., when ep_size > 1 - EP disabled (ep_size == 1): expert_map is None * All experts are local to the current rank * No mapping is needed - EP enabled (ep_size > 1): expert_map is created * Maps global expert IDs to local expert IDs * Shape: (global_num_experts,) * Contains the local expert index for experts on this rank, -1 for experts on other ranks * Used by kernels to handle distributed expert execution - Kernel support varies: * Supports expert_map: fused_moe, fused_marlin_moe, fused_humming_moe, rocm_aiter_fused_moe, deep_gemm_moe, xpu_moe, gpt_oss_triton_kernels_moe * Does not support: flashinfer_cutlass_moe, fused_batched_moe, most cutlass_moe variants, trtllm_* kernels * When kernel doesn't support expert_map: The modular kernel method sets expert_map=None even if EP is enabled

Methods:

-
–[__init__](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager.__init__)Initialize expert map manager.

-
–[get_compressed_map_string](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager.get_compressed_map_string)Get compressed string representation of expert map for logging.

-
–[get_local_expert_ids](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager.get_local_expert_ids)Get list of global IDs for experts on this rank.

-
–[is_local_expert](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager.is_local_expert)Check if expert is assigned to this rank.

-
–[map_global_to_local](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager.map_global_to_local)Map global expert ID to local expert ID.

-
–[update](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager.update)Update expert mappings for new EP configuration.


Attributes:

-
([expert_map](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager.expert_map)

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| NoneMapping from global expert ID to local expert ID.

-
([expert_mask](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager.expert_mask)

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| NoneExpert mask for AITER fusion (ROCm-specific).

-
([placement_strategy](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager.placement_strategy)`ExpertPlacementStrategy`

) –Expert placement strategy ('linear' or 'round_robin').

-
([routing_tables](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager.routing_tables)

) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)] | NoneRouting tables for round-robin placement.


## Source code in `vllm/model_executor/layers/fused_moe/expert_map_manager.py`


|
|

###

`expert_map`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager.expert_map)

Mapping from global expert ID to local expert ID.

Returns tensor of shape (global_num_experts,) where: - expert_map[global_id] = local_id if expert is on this rank - expert_map[global_id] = -1 if expert is not on this rank

Returns None if EP is not enabled (ep_size == 1).

###

`expert_mask`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager.expert_mask)

Expert mask for AITER fusion (ROCm-specific).

Returns tensor of shape (global_num_experts + num_fused_shared + 1,) where 1 indicates expert is on this rank, 0 otherwise.

###

`placement_strategy`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager.placement_strategy)

Expert placement strategy ('linear' or 'round_robin').

###

`routing_tables`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager.routing_tables)

Routing tables for round-robin placement.

Returns (global_to_physical, physical_to_global, local_to_global) or None if not using round-robin or tables not needed.

###

`__init__(max_num_batched_tokens, top_k, global_num_experts, num_redundant_experts, num_expert_group, moe_parallel_config, placement_strategy, enable_eplb, num_fused_shared_experts=0, rocm_aiter_enabled=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager.__init__)

Initialize expert map manager.

Parameters:

-

(`max_num_batched_tokens`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager.__init__(max_num_batched_tokens))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Maximum number of batched tokens per step

-

(`top_k`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager.__init__(top_k))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of experts each token is routed to

-

(`global_num_experts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager.__init__(global_num_experts))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Total number of experts across all ranks

-

(`num_redundant_experts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager.__init__(num_redundant_experts))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of redundant expert replicas (EPLB)

-

(`num_expert_group`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager.__init__(num_expert_group))

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneNumber of expert groups, when grouped routing is used

-

(`moe_parallel_config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager.__init__(moe_parallel_config))

) –[FusedMoEParallelConfig](https://docs.vllm.ai/config/#vllm.model_executor.layers.fused_moe.config.FusedMoEParallelConfig)MoE parallel configuration (contains ep_size, ep_rank, backend flags)

-

(`placement_strategy`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager.__init__(placement_strategy))`ExpertPlacementStrategy`

) –Strategy for placing experts ('linear' or 'round_robin')

-

(`num_fused_shared_experts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager.__init__(num_fused_shared_experts))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –Number of fused shared experts (for AITER)

-

(`rocm_aiter_enabled`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager.__init__(rocm_aiter_enabled))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether ROCm AITER fusion is enabled

-

(`enable_eplb`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager.__init__(enable_eplb))

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether expert-parallel load balancing is enabled


## Source code in `vllm/model_executor/layers/fused_moe/expert_map_manager.py`


|
|

###

`_calculate_expert_maps()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager._calculate_expert_maps)

Calculate expert mappings based on placement strategy.

## Source code in `vllm/model_executor/layers/fused_moe/expert_map_manager.py`


###

`_determine_placement_strategy(requested_strategy)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager._determine_placement_strategy)

Determine effective placement strategy based on config.

## Source code in `vllm/model_executor/layers/fused_moe/expert_map_manager.py`


###

`_init_round_robin_expert_routing_tables()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager._init_round_robin_expert_routing_tables)

Build routing tables for round-robin placement.

## Source code in `vllm/model_executor/layers/fused_moe/expert_map_manager.py`


###

`_init_routing_tables()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager._init_routing_tables)

Ensure routing tables are initialized if needed for round-robin.

This is a public method that can be called to explicitly initialize routing tables. It's safe to call multiple times (idempotent).

## Source code in `vllm/model_executor/layers/fused_moe/expert_map_manager.py`


###

`get_compressed_map_string()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager.get_compressed_map_string)

Get compressed string representation of expert map for logging.

Returns string mapping local to global expert IDs.

## Source code in `vllm/model_executor/layers/fused_moe/expert_map_manager.py`


###

`get_local_expert_ids()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager.get_local_expert_ids)

Get list of global IDs for experts on this rank.

## Source code in `vllm/model_executor/layers/fused_moe/expert_map_manager.py`


###

`is_local_expert(global_id)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager.is_local_expert)

Check if expert is assigned to this rank.

###

`map_global_to_local(global_id)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager.map_global_to_local)

Map global expert ID to local expert ID.

Parameters:

Returns:

-

–[int](https://docs.python.org/3/builtins/functions.html#int)Local expert ID (0 to local_num_experts - 1)


Raises:

-

–[ValueError](https://docs.python.org/3/builtins/exceptions.html#ValueError)If expert is not on this rank


## Source code in `vllm/model_executor/layers/fused_moe/expert_map_manager.py`


###

`update(moe_parallel_config, global_num_experts)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager.update)

Update expert mappings for new EP configuration.

Used during dynamic reconfiguration (e.g., elastic scaling).

Parameters:

-

(`global_num_experts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager.update(global_num_experts))

) –[int](https://docs.python.org/3/builtins/functions.html#int)New total number of experts across all ranks

-

(`moe_parallel_config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.ExpertMapManager.update(moe_parallel_config))

) –[FusedMoEParallelConfig](https://docs.vllm.ai/config/#vllm.model_executor.layers.fused_moe.config.FusedMoEParallelConfig)New MoE parallel configuration (contains ep_size, ep_rank, backend flags)


## Source code in `vllm/model_executor/layers/fused_moe/expert_map_manager.py`


##

`determine_expert_map(ep_size, ep_rank, global_num_experts, expert_placement_strategy='linear', num_fused_shared_experts=0, return_expert_mask=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.determine_expert_map)

Calculates how many experts should be assigned to each rank for EP and creates a mapping from global to local expert index. Experts are distributed evenly across ranks. Any remaining are assigned to the last rank.

Parameters:

-

(`ep_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.determine_expert_map(ep_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)The size of the expert parallel group

-

(`ep_rank`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.determine_expert_map(ep_rank))

) –[int](https://docs.python.org/3/builtins/functions.html#int)The rank of the current process in the expert parallel group

-

(`global_num_experts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.determine_expert_map(global_num_experts))

) –[int](https://docs.python.org/3/builtins/functions.html#int)The total number of experts in the model.

-

(`expert_placement_strategy`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.determine_expert_map(expert_placement_strategy))`ExpertPlacementStrategy`

, default:`'linear'`

) –The expert placement strategy.

-

(`num_fused_shared_experts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.determine_expert_map(num_fused_shared_experts))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –Number of fused shared experts (for AITER)

-

(`return_expert_mask`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.expert_map_manager.determine_expert_map(return_expert_mask))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether to return expert mask for AITER


Returns:

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None,[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None]tuple[int, Optional[torch.Tensor], Optional[torch.Tensor]]: A tuple containing: - local_num_experts (int): The number of experts assigned to the current rank. - expert_map (Optional[torch.Tensor]): A tensor of shape (global_num_experts,) mapping from global to local index. Contains -1 for experts not assigned to the current rank. Returns None if ep_size is 1. - expert_mask (Optional[torch.Tensor]): A tensor of shape (global_num_experts + num_fused_shared_experts + 1,) containing 1 for experts assigned to the current rank and 0 for sentinel. Returns None if ep_size is 1. Used only when AITER MOE is enabled.