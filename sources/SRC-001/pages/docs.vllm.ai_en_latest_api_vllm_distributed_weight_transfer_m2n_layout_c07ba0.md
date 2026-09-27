source: https://docs.vllm.ai/en/latest/api/vllm/distributed/weight_transfer/m2n_layout/
lastmod: 2026-09-27

#

`vllm.distributed.weight_transfer.m2n_layout`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_layout)

Destination-layout resolution for the NCCL M2N weight transfer backend.

For every incoming checkpoint parameter the worker needs a destination buffer plus its placement over the inference mesh. Two outcomes are possible:

**direct**— when the model is not quantized, the parameter maps 1:1 onto a live vLLM parameter and its loader is a small, known-safe copy or tensor- parallel loader. The loader's declared input/output dimension determines the placement; shapes are validation, not an inference mechanism. The reshard writes straight into the live parameter, so each rank receives only its own shard and nothing is copied afterwards.**fallback**— anything else. The reshard delivers the whole tensor to every rank and`load_weights`

does the sharding, exactly as the broadcast NCCL backend does. Fused parameters (`qkv_proj`

,`gate_up_proj`

, MoE`w13`

/`w2`

) take this path: the checkpoint name does not name a vLLM parameter, so there is nothing to resolve against.

Correctness never depends on a parameter resolving — the fallback is always available and is the same path the existing backend uses.

Classes:

-
–[M2NDestination](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_layout.M2NDestination)Where one checkpoint parameter lands on this worker.


Functions:

-
–[resolve_parameter_destinations](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_layout.resolve_parameter_destinations)Build this worker's destination plan, one entry per checkpoint parameter.


##

`M2NDestination`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_layout.M2NDestination)

Where one checkpoint parameter lands on this worker.

Attributes:

-
([placements](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_layout.M2NDestination.placements)`Placements | None`

) –Placement over the inference mesh, or

`REPLICATED`

for the fallback. -
([tensor](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_layout.M2NDestination.tensor)

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| NoneThe live parameter view to reshard into, or None for the fallback path


## Source code in `vllm/distributed/weight_transfer/m2n_layout.py`


##

`_base_loader_shard_dim(param, shard_axis_size)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_layout._base_loader_shard_dim)

Return a known-safe loader's declared shard dim, or reject it.

Loader identity is deliberately fail-closed. A missing loader is not treated as `default_weight_loader`

because a model-level `load_weights`

implementation may transform the tensor before it reaches that default. Wrappers and partials are also rejected: recognizing their wrapped callable would ignore behavior added by the wrapper.

## Source code in `vllm/distributed/weight_transfer/m2n_layout.py`


##

`_destination_placements(shard_dim)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_layout._destination_placements)

Place one tensor shard on the configured destination mesh axis.

## Source code in `vllm/distributed/weight_transfer/m2n_layout.py`


##

`_validated_shard_dim(global_shape, local_shape, declared_dim, shard_axis_size)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_layout._validated_shard_dim)

Validate a loader-declared shard dimension against both shapes.

## Source code in `vllm/distributed/weight_transfer/m2n_layout.py`


##

`resolve_parameter_destinations(model, names, dtypes, shapes, *, num_workers, shard_axis_size, allow_direct)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_layout.resolve_parameter_destinations)

Build this worker's destination plan, one entry per checkpoint parameter.

Placements are relative to the inference mesh: axis 0 replicates and axis 1 shards. `allow_direct=False`

forces every parameter onto the fallback path; the engine sets it for pipeline-parallel or quantized deployments, where a parameter's local shape is not simply the checkpoint shape split across the shard axis. Parameters below a model type with known model-level checkpoint preprocessing also fall back, since bypassing `load_weights`

would skip the transformation.

## Source code in `vllm/distributed/weight_transfer/m2n_layout.py`


|
|