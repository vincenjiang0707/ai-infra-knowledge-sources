source: https://docs.vllm.ai/en/latest/api/vllm/config/parallel/
lastmod: 2026-09-23

#

`vllm.config.parallel`

[¶](https://docs.vllm.ai#vllm.config.parallel)

Classes:

-
–[EPLBConfig](https://docs.vllm.ai#vllm.config.parallel.EPLBConfig)Configuration for Expert Parallel Load Balancing (EP).

-
–[ParallelConfig](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig)Configuration for the distributed execution.


##

`EPLBConfig`

[¶](https://docs.vllm.ai#vllm.config.parallel.EPLBConfig)

Configuration for Expert Parallel Load Balancing (EP).

Attributes:

-
([communicator](https://docs.vllm.ai#vllm.config.parallel.EPLBConfig.communicator)`EPLBCommunicatorBackend | None`

) –Backend for EPLB expert weight communication:

-
([log_balancedness](https://docs.vllm.ai#vllm.config.parallel.EPLBConfig.log_balancedness)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Log the balancedness each step of expert parallelism.

-
([log_balancedness_interval](https://docs.vllm.ai#vllm.config.parallel.EPLBConfig.log_balancedness_interval)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Interval for logging the balancedness.

-
([num_redundant_experts](https://docs.vllm.ai#vllm.config.parallel.EPLBConfig.num_redundant_experts)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of redundant experts to use for expert parallelism.

-
([policy](https://docs.vllm.ai#vllm.config.parallel.EPLBConfig.policy)`EPLBPolicyOption`

) –The policy type for expert parallel load balancing (EPLB).

-
([step_interval](https://docs.vllm.ai#vllm.config.parallel.EPLBConfig.step_interval)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Interval for rearranging experts in expert parallelism.

-
([use_async](https://docs.vllm.ai#vllm.config.parallel.EPLBConfig.use_async)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to use non-blocking EPLB.

-
([window_size](https://docs.vllm.ai#vllm.config.parallel.EPLBConfig.window_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Window size for expert load recording.


## Source code in `vllm/config/parallel.py`


###

`communicator = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.EPLBConfig.communicator)

Backend for EPLB expert weight communication: - "torch_nccl": Use torch.distributed on the device process group - "torch_gloo": Use torch.distributed gloo with CPU staging - "torch_xccl": Use torch.distributed XCCL device P2P on XPU - "nixl": Use NIXL with staged send/recv buffers - "pynccl": Use PyNccl send/recv - None: Auto-select backend ("torch_xccl" on XPU, prefers "nixl" on CUDA, falls back to "torch_gloo")

###

`log_balancedness = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.EPLBConfig.log_balancedness)

Log the balancedness each step of expert parallelism. This is turned off by default since it will cause communication overhead.

###

`log_balancedness_interval = Field(default=1, gt=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.EPLBConfig.log_balancedness_interval)

Interval for logging the balancedness.

###

`num_redundant_experts = Field(default=0, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.EPLBConfig.num_redundant_experts)

Number of redundant experts to use for expert parallelism.

###

`policy = 'default'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.EPLBConfig.policy)

The policy type for expert parallel load balancing (EPLB).

###

`step_interval = Field(default=3000, gt=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.EPLBConfig.step_interval)

Interval for rearranging experts in expert parallelism.

Note that if this is greater than the EPLB window size, only the metrics of the last `lb_window_size`

steps will be used for rearranging experts.

###

`use_async = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.EPLBConfig.use_async)

Whether to use non-blocking EPLB.

###

`window_size = Field(default=1000, gt=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.EPLBConfig.window_size)

Window size for expert load recording.

##

`ParallelConfig`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig)

Configuration for the distributed execution.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.compute_hash)Provide a hash that uniquely identifies all the configs

-
–[get_next_dp_init_port](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.get_next_dp_init_port)We might need to initialize process groups in multiple

-
–[reconfigure_for_independent_dp_rank](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.reconfigure_for_independent_dp_rank)Reconfigure for a single independent non-MoE DP rank.

-
–[set_dcp_defaults](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.set_dcp_defaults)Fill in the DCP options the user left unset.

-
–[sync_dp_state](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.sync_dp_state)Combined all-reduce for DP state synchronization.


Attributes:

-
([all2all_backend](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.all2all_backend)`All2AllBackend`

) –All2All backend for MoE expert parallel communication. Available options:

-
([assigned_physical_gpu_ids](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.assigned_physical_gpu_ids)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | NoneMapping from vLLM-local logical GPU IDs to physical GPU IDs.

-
([cp_kv_cache_interleave_size](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.cp_kv_cache_interleave_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Interleave size of kv_cache storage while using DCP.

-
([cpu_distributed_timeout_seconds](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.cpu_distributed_timeout_seconds)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneTimeout (in seconds) for cpu communication groups. If None, PyTorch's

-
([data_parallel_backend](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.data_parallel_backend)`DataParallelBackend`

) –Backend to use for data parallel, either "mp" or "ray".

-
([data_parallel_external_lb](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.data_parallel_external_lb)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to use "external" DP LB mode. Applies only to online serving

-
([data_parallel_hybrid_lb](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.data_parallel_hybrid_lb)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to use "hybrid" DP LB mode. Applies only to online serving

-
([data_parallel_index](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.data_parallel_index)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Equal to the data parallel rank but not used for torch process groups

-
([data_parallel_master_ip](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.data_parallel_master_ip)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)IP of the data parallel master.

-
([data_parallel_master_port](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.data_parallel_master_port)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Port of the data parallel master.

-
([data_parallel_rank](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.data_parallel_rank)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Rank of the data parallel group. The runtime check at

-
([data_parallel_rank_local](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.data_parallel_rank_local)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneLocal rank of the data parallel group, set only in SPMD mode.

-
([data_parallel_rpc_port](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.data_parallel_rpc_port)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Fixed port for data parallel messaging, shared by all nodes.

-
([data_parallel_size](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.data_parallel_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of data parallel groups. MoE layers will be sharded according to

-
([data_parallel_size_local](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.data_parallel_size_local)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of local data parallel groups. A value of 0 is a sentinel used by

-
([dbo_decode_token_threshold](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.dbo_decode_token_threshold)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The threshold for dual batch overlap for batches only containing decodes.

-
([dbo_prefill_token_threshold](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.dbo_prefill_token_threshold)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The threshold for dual batch overlap for batches that contain one or more

-
([dcp_comm_backend](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.dcp_comm_backend)`DCPCommBackend | None`

) –Communication backend for Decode Context Parallel (DCP).

-
([dcp_kv_cache_interleave_size](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.dcp_kv_cache_interleave_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Interleave size of kv_cache storage while using DCP.

-
([dcp_q_replicate](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.dcp_q_replicate)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)| NoneReplicate the MLA query projection within each DCP group so decode can skip the

-
([decode_context_parallel_size](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.decode_context_parallel_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of ranks that shard the decode KV cache. DCP does not expand

-
([disable_custom_all_reduce](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.disable_custom_all_reduce)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Disable the custom all-reduce kernel and fall back to NCCL.

-
([disable_nccl_for_dp_synchronization](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.disable_nccl_for_dp_synchronization)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)| NoneForces the dp synchronization logic in vllm/v1/worker/dp_utils.py

-
([distributed_executor_backend](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.distributed_executor_backend)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| DistributedExecutorBackend |[type](https://docs.python.org/3/builtins/functions.html#type)[[Executor](https://docs.vllm.ai/v1/executor/#vllm.v1.executor.Executor)] | NoneBackend to use for distributed model workers, either "ray" or "mp"

-
([distributed_timeout_seconds](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.distributed_timeout_seconds)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneTimeout in seconds for distributed operations (e.g., init_process_group).

-
([dp_sync_interval](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.dp_sync_interval)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Steps between DP finish-sync all-reduces; must match across DP ranks.

-
([elastic_ep_max_dp_size](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.elastic_ep_max_dp_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Maximum data parallel size supported by elastic expert parallelism.

-
([enable_batch_sharded_sampling](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.enable_batch_sharded_sampling)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)| NoneUse sharded sampling across tensor parallel ranks. Each rank samples

-
([enable_dbo](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.enable_dbo)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable dual batch overlap for the model executor.

-
([enable_elastic_ep](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.enable_elastic_ep)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable elastic expert parallelism with stateless NCCL groups for DP/EP.

-
([enable_ep_weight_filter](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.enable_ep_weight_filter)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Skip non-local expert weights during model loading when expert

-
([enable_eplb](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.enable_eplb)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable expert parallelism load balancing for MoE layers.

-
([enable_expert_parallel](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.enable_expert_parallel)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Use expert parallelism instead of tensor parallelism for MoE layers.

-
([enable_fault_tolerance](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.enable_fault_tolerance)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable fault tolerance for detailed error recovery,

-
([eplb_config](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.eplb_config)

) –[EPLBConfig](https://docs.vllm.ai#vllm.config.parallel.EPLBConfig)Expert parallelism configuration.

-
([expert_placement_strategy](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.expert_placement_strategy)`ExpertPlacementStrategy`

) –The expert placement strategy for MoE layers:

-
([fault_tolerance_config](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.fault_tolerance_config)

) –[FaultToleranceConfig](https://docs.vllm.ai/fault_tolerance/#vllm.config.fault_tolerance.FaultToleranceConfig)The configurations for fault tolerance.

-
([is_moe_model](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.is_moe_model)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)| NoneWhether the deployed model is MoE (if known).

-
([local_engines_only](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.local_engines_only)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Client manages local+remote EngineCores in pure internal LB case.

-
([master_addr](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.master_addr)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)distributed master address for multi-node distributed

-
([master_port](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.master_port)

) –[int](https://docs.python.org/3/builtins/functions.html#int)distributed master port for multi-node distributed

-
([max_parallel_loading_workers](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.max_parallel_loading_workers)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneMaximum number of parallel loading workers when loading model

-
([nnodes](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.nnodes)

) –[int](https://docs.python.org/3/builtins/functions.html#int)num of nodes for multi-node distributed

-
([nnodes_within_dp](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.nnodes_within_dp)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of nodes one DP replica spans.

-
([node_rank](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.node_rank)

) –[int](https://docs.python.org/3/builtins/functions.html#int)distributed node rank for multi-node distributed

-
([numa_bind](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.numa_bind)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable NUMA binding for GPU worker subprocesses.

-
([numa_bind_cpus](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.numa_bind_cpus)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | NoneOptional CPU lists to bind each GPU worker to.

-
([numa_bind_nodes](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.numa_bind_nodes)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | NoneNUMA node to bind each GPU worker to.

-
([pipeline_parallel_size](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.pipeline_parallel_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of pipeline parallel groups.

-
([placement_group](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.placement_group)`PlacementGroup | None`

) –ray distributed model workers placement group.

-
([prefill_context_parallel_size](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.prefill_context_parallel_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of ranks that split prefill sequence computation. PCP expands

-
([rank](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.rank)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Global rank in distributed setup.

-
([ray_runtime_env](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.ray_runtime_env)`RuntimeEnv | None`

) –Ray runtime environment to pass to distributed workers.

-
([ray_workers_use_nsight](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.ray_workers_use_nsight)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to profile Ray workers with nsight, see https://docs.ray.io/en/latest/ray-observability/user-guides/profiling.html#profiling-nsight-profiler.

-
([sd_worker_cls](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.sd_worker_cls)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The full name of the worker class to use for speculative decoding.

-
([tensor_parallel_size](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.tensor_parallel_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of tensor parallel groups.

-
([ubatch_size](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.ubatch_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of ubatch size.

-
([worker_cls](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.worker_cls)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The full name of the worker class to use. If "auto", the worker class

-
([worker_extension_cls](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.worker_extension_cls)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The full name of the worker extension class to use. The worker extension

-
([world_size](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.world_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)world_size is TPxPP, it affects the number of workers we create.

-
([world_size_across_dp](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.world_size_across_dp)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Process world size across TP, PCP, PP, and DP.


## Source code in `vllm/config/parallel.py`


|
|

###

`_allow_auto_resolve_cp_interleave_size = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig._allow_auto_resolve_cp_interleave_size)

Whether NIXL may select the interleave size automatically.

###

`_api_process_count = Field(default=1, gt=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig._api_process_count)

The number of API processes initialized.

## Note

This is an internal config that is only valid for and should only be set by API server scale-out.

###

`_api_process_rank = Field(default=0, ge=(-1))`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig._api_process_rank)

The rank of this API process, or `-1`

for engine core processes under API server scale-out.

## Note

This is an internal config that is only valid for and should only be set by API server scale-out.

###

`_coord_store_port = 0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig._coord_store_port)

Port of the coordination TCPStore. Can be set by the API server; workers connect as clients to exchange self-picked group ports at runtime.

###

`_data_parallel_master_port_list = Field(default_factory=list)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig._data_parallel_master_port_list)

List of open port auto-queried for data parallel messaging. Set to be private as it's not intended to be configured by users.

###

`all2all_backend = 'allgather_reducescatter'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.all2all_backend)

All2All backend for MoE expert parallel communication. Available options:

- "allgather_reducescatter": All2all based on allgather and reducescatter
- "deepep_high_throughput": Use deepep high-throughput kernels
- "deepep_low_latency": Use deepep low-latency kernels
- "mori_high_throughput": MoRI EP with InterNodeV1 for multi-node
- "mori_low_latency": MoRI EP with InterNodeV1LL for multi-node
- "moonep": MoonEP balanced EP with dynamic redundant experts (NVLink)
- "nixl_ep": Use nixl-ep kernels
- "flashinfer_nvlink_one_sided": Use flashinfer high-throughput a2a kernels
- "flashinfer_nvlink_two_sided": Use flashinfer two-sided kernels for mnnvl

###

`assigned_physical_gpu_ids = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.assigned_physical_gpu_ids)

Mapping from vLLM-local logical GPU IDs to physical GPU IDs.

For example, `[2, 3]`

means logical GPU 0 maps to physical GPU 2, and logical GPU 1 maps to physical GPU 3. Physical IDs are used only at platform/topology boundaries such as NVML, NIC affinity, P2P checks, and final CUDA device selection when needed. When None, logical IDs map to visible device IDs in order.

###

`cp_kv_cache_interleave_size = 1`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.cp_kv_cache_interleave_size)

Interleave size of kv_cache storage while using DCP. Store interleave_size tokens on dcp_rank i, then store next interleave_size tokens on dcp_rank i+1. Interleave_size=1: token-level alignment, where token `i`

is stored on dcp_rank `i % dcp_world_size`

. Interleave_size=block_size: block-level alignment, where tokens are first populated to the preceding ranks. Tokens are then stored in (rank i+1, block j) only after (rank i, block j) is fully occupied. Block_size should be greater than or equal to cp_kv_cache_interleave_size. Block_size should be divisible by cp_kv_cache_interleave_size.

When --cp-kv-cache-interleave-size is omitted (None), the interleave size is resolved automatically based on NIXL transfer requirements. Explicit settings take priority.

###

`cpu_distributed_timeout_seconds = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.cpu_distributed_timeout_seconds)

Timeout (in seconds) for cpu communication groups. If None, PyTorch's default timeout is used (1800s for gloo).

###

`data_parallel_backend = 'mp'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.data_parallel_backend)

Backend to use for data parallel, either "mp" or "ray".

###

`data_parallel_external_lb = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.data_parallel_external_lb)

Whether to use "external" DP LB mode. Applies only to online serving and when data_parallel_size > 0. This is useful for a "one-pod-per-rank" wide-EP setup in Kubernetes. Supported only for MoE deployments; non-MoE models should use independent vLLM instances without --data-parallel-* arguments. Set implicitly when --data-parallel-rank is provided explicitly to vllm serve.

###

`data_parallel_hybrid_lb = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.data_parallel_hybrid_lb)

Whether to use "hybrid" DP LB mode. Applies only to online serving and when data_parallel_size > 0. Enables running an AsyncLLM and API server on a "per-node" basis where vLLM load balances between local data parallel ranks, but an external LB balances between vLLM nodes/replicas. Set explicitly in conjunction with --data-parallel-start-rank.

###

`data_parallel_index = Field(init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.data_parallel_index)

Equal to the data parallel rank but not used for torch process groups and not overridden for dense models.

###

`data_parallel_master_ip = '127.0.0.1'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.data_parallel_master_ip)

IP of the data parallel master.

###

`data_parallel_master_port = 29500`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.data_parallel_master_port)

Port of the data parallel master.

###

`data_parallel_rank = Field(default=0, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.data_parallel_rank)

Rank of the data parallel group. The runtime check at `__post_init__`

further bounds this by `data_parallel_size`

.

###

`data_parallel_rank_local = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.data_parallel_rank_local)

Local rank of the data parallel group, set only in SPMD mode.

###

`data_parallel_rpc_port = Field(default=29550, ge=1, le=65535)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.data_parallel_rpc_port)

Fixed port for data parallel messaging, shared by all nodes.

###

`data_parallel_size = Field(default=1, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.data_parallel_size)

Number of data parallel groups. MoE layers will be sharded according to the product of the tensor, prefill-context, and data parallel sizes.

###

`data_parallel_size_local = Field(default=1, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.data_parallel_size_local)

Number of local data parallel groups. A value of 0 is a sentinel used by the engine-args layer to signal that data parallelism was specified externally (see `ParallelConfig.__post_init__`

).

###

`dbo_decode_token_threshold = Field(default=32, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.dbo_decode_token_threshold)

The threshold for dual batch overlap for batches only containing decodes. If the number of tokens in the request is greater than this threshold, microbatching will be used. Otherwise, the request will be processed in a single batch.

###

`dbo_prefill_token_threshold = Field(default=512, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.dbo_prefill_token_threshold)

The threshold for dual batch overlap for batches that contain one or more prefills. If the number of tokens in the request is greater than this threshold, microbatching will be used. Otherwise, the request will be processed in a single batch.

###

`dcp_comm_backend = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.dcp_comm_backend)

Communication backend for Decode Context Parallel (DCP). - "ag_rs": AllGather + ReduceScatter (existing behavior) - "a2a": All-to-All exchange of partial outputs + LSE, then combine with Triton kernel. Reduces NCCL calls from 3 to 2 per layer for MLA models.

`None`

selects the model default, which is "ag_rs" unless the model overrides it via [ set_dcp_defaults](https://docs.vllm.ai/#vllm.config.ParallelConfig.set_dcp_defaults).

###

`dcp_kv_cache_interleave_size = 1`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.dcp_kv_cache_interleave_size)

Interleave size of kv_cache storage while using DCP. dcp_kv_cache_interleave_size has been replaced by cp_kv_cache_interleave_size, and will be deprecated when PCP is fully supported.

###

`dcp_q_replicate = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.dcp_q_replicate)

Replicate the MLA query projection within each DCP group so decode can skip the query all-gather.

With DCP the KV cache is sharded across the group, so the standard MLA decode path all-gathers the query every step. Replicating the (small) query projection at load time lets each rank materialize the full group-local head set and skip that collective, at the cost of computing the projection redundantly on every rank in the group.

###

`decode_context_parallel_size = Field(default=1, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.decode_context_parallel_size)

Number of ranks that shard the decode KV cache. DCP does not expand the process world size. Without PCP, DCP reuses TP ranks. With PCP, DCP either spans the PCP axis or the full TP x PCP block.

###

`disable_custom_all_reduce = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.disable_custom_all_reduce)

Disable the custom all-reduce kernel and fall back to NCCL.

###

`disable_nccl_for_dp_synchronization = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.disable_nccl_for_dp_synchronization)

Forces the dp synchronization logic in vllm/v1/worker/dp_utils.py to use Gloo instead of NCCL for its all reduce.

Defaults to True when async scheduling is enabled, False otherwise.

###

`distributed_executor_backend = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.distributed_executor_backend)

Backend to use for distributed model workers, either "ray" or "mp" (multiprocessing). If the product of pipeline_parallel_size and tensor_parallel_size is less than or equal to the number of GPUs available, "mp" will be used to keep processing on a single host. Otherwise, an error will be raised. To use "mp" you must also set nnodes, and to use "ray" you must manually set distributed_executor_backend to "ray".

## Note

[TPU](https://docs.vllm.ai/projects/tpu/en/latest/) platform only supports Ray for distributed inference.

###

`distributed_timeout_seconds = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.distributed_timeout_seconds)

Timeout in seconds for distributed operations (e.g., init_process_group). If set, this value is passed to torch.distributed.init_process_group as the timeout parameter. If None, PyTorch's default timeout is used (600s for NCCL). Increase this for multi-node setups where model downloads may be slow.

###

`dp_sync_interval = Field(default=16, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.dp_sync_interval)

Steps between DP finish-sync all-reduces; must match across DP ranks.

###

`elastic_ep_max_dp_size = Field(default=None, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.elastic_ep_max_dp_size)

Maximum data parallel size supported by elastic expert parallelism.

###

`enable_batch_sharded_sampling = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.enable_batch_sharded_sampling)

Use sharded sampling across tensor parallel ranks. Each rank samples a slice of the batch instead of every rank sampling all of it. Currently defaults to False if not set. Enabling it explicitly raises when the config cannot support it (`tensor_parallel_size`

must be > 1, `max_num_seqs`

at least `tensor_parallel_size`

, and `max_logprobs`

non-negative). Models opt in by implementing `compute_logits_local`

.

###

`enable_dbo = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.enable_dbo)

Enable dual batch overlap for the model executor.

###

`enable_elastic_ep = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.enable_elastic_ep)

Enable elastic expert parallelism with stateless NCCL groups for DP/EP.

###

`enable_ep_weight_filter = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.enable_ep_weight_filter)

Skip non-local expert weights during model loading when expert parallelism is active. Each rank only reads its own expert shard from disk, which can drastically reduce storage I/O for MoE models with per-expert weight tensors (e.g. DeepSeek, Mixtral, Kimi-K2.5). Has no effect on 3D fused-expert checkpoints (e.g. GPT-OSS) or non-MoE models.

###

`enable_eplb = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.enable_eplb)

Enable expert parallelism load balancing for MoE layers.

###

`enable_expert_parallel = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.enable_expert_parallel)

Use expert parallelism instead of tensor parallelism for MoE layers.

###

`enable_fault_tolerance = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.enable_fault_tolerance)

Enable fault tolerance for detailed error recovery, such as scaling down fault DPEngineCore.

###

`eplb_config = Field(default_factory=EPLBConfig)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.eplb_config)

Expert parallelism configuration.

###

`expert_placement_strategy = 'linear'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.expert_placement_strategy)

The expert placement strategy for MoE layers:

- "linear": Experts are placed in a contiguous manner. For example, with 4 experts and 2 ranks, rank 0 will have experts [0, 1] and rank 1 will have experts [2, 3].
- "round_robin": Experts are placed in a round-robin manner. For example, with 4 experts and 2 ranks, rank 0 will have experts [0, 2] and rank 1 will have experts [1, 3]. This strategy can help improve load balancing for grouped expert models with no redundant experts.

###

`fault_tolerance_config = Field(default_factory=FaultToleranceConfig)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.fault_tolerance_config)

The configurations for fault tolerance.

###

`is_moe_model = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.is_moe_model)

Whether the deployed model is MoE (if known).

###

`local_engines_only`

`property`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.local_engines_only)

Client manages local+remote EngineCores in pure internal LB case. Client manages local EngineCores in hybrid and external LB case.

###

`master_addr = '127.0.0.1'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.master_addr)

distributed master address for multi-node distributed inference when distributed_executor_backend is mp.

###

`master_port = 29501`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.master_port)

distributed master port for multi-node distributed inference when distributed_executor_backend is mp.

###

`max_parallel_loading_workers = Field(default=None, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.max_parallel_loading_workers)

Maximum number of parallel loading workers when loading model sequentially in multiple batches. To avoid RAM OOM when using tensor parallel and large models.

###

`nnodes = Field(default=1, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.nnodes)

num of nodes for multi-node distributed inference when distributed_executor_backend is mp.

###

`nnodes_within_dp`

`property`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.nnodes_within_dp)

Number of nodes one DP replica spans.

External LB pins `data_parallel_size_local`

to 1, so the ratio rounds down to 0 once DP replicas outnumber nodes. A replica that does not span nodes still occupies exactly one.

###

`node_rank = Field(default=0, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.node_rank)

distributed node rank for multi-node distributed inference when distributed_executor_backend is mp.

###

`numa_bind = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.numa_bind)

Enable NUMA binding for GPU worker subprocesses.

By default, workers are pinned to their GPU's NUMA-local CPUs and memory; on PCT-capable Xeons they also auto-bind to the SKU's PCT priority cores.

###

`numa_bind_cpus = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.numa_bind_cpus)

Optional CPU lists to bind each GPU worker to.

Specify one CPU list per visible GPU, for example `["0-3", "4-7", "8-11", "12-15"]`

. When set, vLLM uses `numactl --physcpubind`

instead of `--cpunodebind`

. This is useful for custom policies such as binding to PCT or other high-frequency cores. Each entry must use `numactl --physcpubind`

CPU-list syntax, for example `"0-3"`

or `"0,2,4-7"`

.

###

`numa_bind_nodes = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.numa_bind_nodes)

NUMA node to bind each GPU worker to.

Specify one NUMA node per visible GPU, for example `[0, 0, 1, 1]`

for a 4-GPU system with GPUs 0-1 on NUMA node 0 and GPUs 2-3 on NUMA node 1. If unset and `numa_bind=True`

, vLLM auto-detects the GPU-to-NUMA topology. The values are passed to `numactl --membind`

and `--cpunodebind`

, so they must be valid `numactl`

NUMA node indices.

###

`pipeline_parallel_size = Field(default=1, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.pipeline_parallel_size)

Number of pipeline parallel groups.

###

`placement_group = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.placement_group)

ray distributed model workers placement group.

###

`prefill_context_parallel_size = Field(default=1, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.prefill_context_parallel_size)

Number of ranks that split prefill sequence computation. PCP expands the process world size but does not increase the KV-cache shard count.

###

`rank = 0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.rank)

Global rank in distributed setup.

###

`ray_runtime_env = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.ray_runtime_env)

Ray runtime environment to pass to distributed workers.

###

`ray_workers_use_nsight = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.ray_workers_use_nsight)

Whether to profile Ray workers with nsight, see https://docs.ray.io/en/latest/ray-observability/user-guides/profiling.html#profiling-nsight-profiler.

###

`sd_worker_cls = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.sd_worker_cls)

The full name of the worker class to use for speculative decoding. If "auto", the worker class will be determined based on the platform.

###

`tensor_parallel_size = Field(default=1, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.tensor_parallel_size)

Number of tensor parallel groups.

###

`ubatch_size = Field(default=0, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.ubatch_size)

Number of ubatch size.

###

`worker_cls = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.worker_cls)

The full name of the worker class to use. If "auto", the worker class will be determined based on the platform.

###

`worker_extension_cls = ''`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.worker_extension_cls)

The full name of the worker extension class to use. The worker extension class is dynamically inherited by the worker class. This is used to inject new attributes and methods to the worker class for use in collective_rpc calls.

###

`world_size = Field(init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.world_size)

world_size is TPxPP, it affects the number of workers we create.

###

`world_size_across_dp`

`property`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.world_size_across_dp)

Process world size across TP, PCP, PP, and DP.

###

`_pick_stateless_dp_port()`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig._pick_stateless_dp_port)

Return `(port, listen_socket)`

for DP group init.

With a coord store, rank 0 binds a socket and publishes the port; others read it. Without one, pops a pre-allocated port and returns `listen_socket=None`

.

## Source code in `vllm/config/parallel.py`


###

`_skip_none_validation(value, handler)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig._skip_none_validation)

Skip validation if the value is `None`

when initialisation is delayed.

## Source code in `vllm/config/parallel.py`


###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.compute_hash)

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.

This hash is also used for DP worker configuration validation to prevent hangs from mismatched collective communication patterns.

## Source code in `vllm/config/parallel.py`


###

`get_next_dp_init_port()`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.get_next_dp_init_port)

We might need to initialize process groups in multiple processes that is related to data parallelism, e.g. both in the worker and in the engine, which can live in different processes. To avoid port conflicts, we pop a new port from the prepared port list each time we need to initialize a new process group related to data parallelism.

## Source code in `vllm/config/parallel.py`


###

`reconfigure_for_independent_dp_rank()`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.reconfigure_for_independent_dp_rank)

Reconfigure for a single independent non-MoE DP rank.

## Source code in `vllm/config/parallel.py`


###

`set_dcp_defaults(comm_backend='ag_rs', q_replicate=False)`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.set_dcp_defaults)

Fill in the DCP options the user left unset.

Models can set their preferred DCP settings by calling this from their `verify_and_update_config`

hook.

## Source code in `vllm/config/parallel.py`


###

`sync_dp_state(dp_group, has_unfinished, pending_pause)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.config.parallel.ParallelConfig.sync_dp_state)

Combined all-reduce for DP state synchronization.

## Uses a single SUM all-reduce on a 2-element tensor

[0] = 1 if this rank has unfinished work, else 0. SUM > 0 ≡ logical OR across ranks → any rank has work. [1] = 1 if this rank has a pending pause request, else 0. SUM == dp_size ≡ all ranks reached pause consensus.

has_unfinished_global is true if any rank has unfinished work, or if some ranks are waiting for a pause consensus.

Returns: