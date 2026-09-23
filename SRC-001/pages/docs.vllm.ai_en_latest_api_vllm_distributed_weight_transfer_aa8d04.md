source: https://docs.vllm.ai/en/latest/api/vllm/distributed/weight_transfer/
lastmod: 2026-09-23

#

`vllm.distributed.weight_transfer`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer)

Weight transfer engines for syncing model weights from trainers to inference workers.

Modules:

-
–[base](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base)Base class for weight transfer engines.

-
–[clients](https://docs.vllm.ai/clients/#vllm.distributed.weight_transfer.clients)Built-in

`VLLMWeightSyncClient`

implementations. -
–[factory](https://docs.vllm.ai/factory/#vllm.distributed.weight_transfer.factory)Factory for weight transfer engines with lazy loading.

-
–[ipc_engine](https://docs.vllm.ai/ipc_engine/#vllm.distributed.weight_transfer.ipc_engine)IPC-based weight transfer engine using CUDA IPC for communication.

-
–[nccl_common](https://docs.vllm.ai/nccl_common/#vllm.distributed.weight_transfer.nccl_common)Shared NCCL initialization helpers for weight transfer engines.

-
–[nccl_engine](https://docs.vllm.ai/nccl_engine/#vllm.distributed.weight_transfer.nccl_engine)NCCL-based (dense) weight transfer engine.

-
–[packed_tensor](https://docs.vllm.ai/packed_tensor/#vllm.distributed.weight_transfer.packed_tensor)Packed tensor utilities for efficient weight transfer.

-
–[sharded_rdt_common](https://docs.vllm.ai/sharded_rdt_common/#vllm.distributed.weight_transfer.sharded_rdt_common)Shared pieces of the sharded-RDT backend: the op-chain allowlist, buffer

-
–[sharded_rdt_engine](https://docs.vllm.ai/sharded_rdt_engine/#vllm.distributed.weight_transfer.sharded_rdt_engine)Sharded Ray Direct Transport (RDT) weight transfer engine (consumer side).

-
–[sharded_rdt_fake](https://docs.vllm.ai/sharded_rdt_fake/#vllm.distributed.weight_transfer.sharded_rdt_fake)Op-chain recording for the sharded-RDT backend.

-
–[sharded_rdt_trainer](https://docs.vllm.ai/sharded_rdt_trainer/#vllm.distributed.weight_transfer.sharded_rdt_trainer)Trainer-side engine for the sharded-RDT (pull-based NIXL) backend.

-
–[sparse_nccl_engine](https://docs.vllm.ai/sparse_nccl_engine/#vllm.distributed.weight_transfer.sparse_nccl_engine)Sparse NCCL weight transfer engine.


Classes:

-
–[HTTPVLLMWeightSyncClient](https://docs.vllm.ai#vllm.distributed.weight_transfer.HTTPVLLMWeightSyncClient)Talks to a vLLM server over the RLHF HTTP routes.

-
–[ModuleSource](https://docs.vllm.ai#vllm.distributed.weight_transfer.ModuleSource)`WeightSource`

over`module.named_parameters()`

— the common case. -
–[ParamMeta](https://docs.vllm.ai#vllm.distributed.weight_transfer.ParamMeta)Name / wire dtype / full (HF) shape for one output parameter.

-
–[RayVLLMWeightSyncClient](https://docs.vllm.ai#vllm.distributed.weight_transfer.RayVLLMWeightSyncClient)Talks to one or more vLLM

`AsyncLLM`

/`LLM`

Ray actors. -
–[TrainerWeightTransferEngine](https://docs.vllm.ai#vllm.distributed.weight_transfer.TrainerWeightTransferEngine)Trainer-side weight transfer engine.

-
–[VLLMWeightSyncClient](https://docs.vllm.ai#vllm.distributed.weight_transfer.VLLMWeightSyncClient)Trainer-side stub for the inference engine's weight-sync control plane.

-
–[WeightSource](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightSource)A re-iterable source of the trainer's weights, handed to a trainer engine.

-
–[WeightTransferEngine](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngine)Base class for weight transfer engines that handle transport of model weights

-
–[WeightTransferEngineFactory](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngineFactory)Factory for creating weight transfer engines with lazy loading.

-
–[WeightTransferTrainerFactory](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferTrainerFactory)Factory for creating trainer-side weight transfer engines.


##

`HTTPVLLMWeightSyncClient`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.HTTPVLLMWeightSyncClient)

Talks to a vLLM server over the RLHF HTTP routes.

Mirrors `vllm/entrypoints/serve/dev/rlhf/api_router.py`

: `/init_weight_transfer_engine`

, `/start_weight_update`

, `/update_weights`

, `/finish_weight_update`

.

## Source code in `vllm/distributed/weight_transfer/clients.py`


##

`ModuleSource`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.ModuleSource)

Bases: [WeightSource](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base.WeightSource)

`WeightSource`

over `module.named_parameters()`

— the common case.

Handles both plain dense modules and FSDP-sharded ones with no special casing: iteration all-gathers each `DTensor`

via `full_tensor()`

(a collective) and passes regular tensors through. `metadata()`

reads the *global* `.shape`

/ `.dtype`

, so it never triggers a gather.

## Source code in `vllm/distributed/weight_transfer/base.py`


##

`ParamMeta`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.ParamMeta)

Name / wire dtype / full (HF) shape for one output parameter.

## Source code in `vllm/distributed/weight_transfer/base.py`


##

`RayVLLMWeightSyncClient`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.RayVLLMWeightSyncClient)

Talks to one or more vLLM `AsyncLLM`

/`LLM`

Ray actors.

Each call fans out to every handle and blocks on all of them, so a multi-actor (e.g. multi-DP) deployment is driven as one unit.

## Source code in `vllm/distributed/weight_transfer/clients.py`


##

`TrainerWeightTransferEngine`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.TrainerWeightTransferEngine)

Bases:

, [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)[Generic](https://docs.python.org/3/library/typing.html#typing.Generic)[TTrainerInitInfo]

Trainer-side weight transfer engine.

Symmetric to `WeightTransferEngine`

but lives in the training process. Constructed via the `trainer_init`

factory classmethod; carries any backend-specific state (NCCL communicators, IPC device info, transfer plans) on `self`

. Full-resync backends (NCCL, IPC) take a `WeightSource`

at `trainer_init`

and replay it each round via the no-argument `send_weights()`

. Backends that push per-round deltas instead (e.g. sparse patches) leave `source`

as `None`

and take their payload as a `send_weights`

argument.

Unlike the worker engine, the trainer side does not take a `WeightTransferConfig`

: the backend is selected from the init info's `backend`

`ClassVar`

(so callers pass only the init info), and the static wire params (packed, buffer sizes) ride the backend-specific `TrainerInitInfo`

, which the sender also propagates to the worker at the init handshake.

Multi-rank trainers: `trainer_init`

and `send_weights`

are called on *every* trainer rank. Rank 0 is the sender, resolved once at `trainer_init`

into `is_sender`

. Non-sender ranks still run every collective (iterating the source, metadata export, IPC handle all-gather) so the group stays aligned, but each engine explicitly guards the control-plane RPCs and the transmit on `self.is_sender`

, so only the sender touches the client.

## Subclasses should define

init_info_cls: Type of backend-specific trainer init info

Methods:

-
–[send_weights](https://docs.vllm.ai#vllm.distributed.weight_transfer.TrainerWeightTransferEngine.send_weights)Push weights to inference workers and drive the full update round

-
–[shutdown](https://docs.vllm.ai#vllm.distributed.weight_transfer.TrainerWeightTransferEngine.shutdown)Tear down communicators / process groups. Default no-op.

-
–[trainer_init](https://docs.vllm.ai#vllm.distributed.weight_transfer.TrainerWeightTransferEngine.trainer_init)Rendezvous with the inference side and return a ready instance.


## Source code in `vllm/distributed/weight_transfer/base.py`


|
|

###

`send_weights()`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.TrainerWeightTransferEngine.send_weights)

Push weights to inference workers and drive the full update round trip: `start_weight_update`

, `update_weights`

(run concurrently with the trainer-side broadcast when the backend requires it), then `finish_weight_update`

. Called on every trainer rank.

## Source code in `vllm/distributed/weight_transfer/base.py`


###

`shutdown()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.TrainerWeightTransferEngine.shutdown)

###

`trainer_init(init_info, *, client, source=None)`

`abstractmethod`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.TrainerWeightTransferEngine.trainer_init)

Rendezvous with the inference side and return a ready instance.

Called on every trainer rank. The sender drives the full handshake via `client`

(build the worker-side init info, call `client.init_weight_transfer_engine`

, open the trainer-side endpoint); non-sender ranks skip the rendezvous and the RPC.

## Source code in `vllm/distributed/weight_transfer/base.py`


##

`VLLMWeightSyncClient`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.VLLMWeightSyncClient)

Bases: [Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)

Trainer-side stub for the inference engine's weight-sync control plane.

Mirrors the weight-sync methods that the inference engine exposes (`EngineClient`

/ the HTTP RLHF routes / Ray actors). A `TrainerWeightTransferEngine`

drives the full handshake through this protocol so trainer code never has to know the transport.

All methods are synchronous and accept plain dicts (matching what the inference side already accepts). Concurrency that some backends need (e.g. NCCL must run `update_weights`

concurrently with the trainer-side broadcast) is the engine's responsibility, not the client's, so the protocol stays a flat four-method surface that any wrapper can implement.

The protocol is structural (PEP 544), so user implementations need only define these four methods — no import or subclassing required.

## Source code in `vllm/distributed/weight_transfer/base.py`


##

`WeightSource`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightSource)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

A re-iterable source of the trainer's weights, handed to a trainer engine.

Two channels:

`metadata()`

—`(name, wire dtype, full shape)`

for every parameter,*without*transferring. Cheap when shapes are known locally (FSDP`DTensor`

global shape); may be expensive on first call for backends that must materialize to learn shapes (e.g. a Megatron-Bridge export), in which case it should cache.- iteration — yields fully-materialized
`(name, tensor)`

pairs, one at a time. Materializing is typically a collective (FSDP`full_tensor()`

, a Megatron export), so the ranks that share a parameter must iterate it in the same order in lockstep, or they deadlock. `held_names()`

— which parameters this rank holds, for producers that are split so each rank holds only part of the model. Defaults to all.`iter_groups()`

— the same stream batched per gather group (see`layerwise_groups`

). Defaults to batching`__iter__`

; override to materialize a whole group in one step.

`iter(source)`

must yield a *fresh* pass each round. Backends with custom producer logic (Megatron export, RDT plans, MoE re-fusing) subclass this.

Methods:

-
–[groups](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightSource.groups)This rank's gather groups, in metadata order:

`layerwise_groups`

over -
–[held_names](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightSource.held_names)The parameters this rank holds, or None for all of them.

-
–[iter_groups](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightSource.iter_groups)Yield one

`(names, tensors)`

batch per group from`groups()`

. -
–[metadata](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightSource.metadata)Declare what iteration will yield, without transferring anything.


## Source code in `vllm/distributed/weight_transfer/base.py`


|
|

###

`groups()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightSource.groups)

This rank's gather groups, in metadata order: `layerwise_groups`

over `metadata()`

, restricted to the groups holding at least one held name.

A group with nothing held here is not iterated at all — its gather is a collective among the ranks that do hold part of it.

## Source code in `vllm/distributed/weight_transfer/base.py`


###

`held_names()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightSource.held_names)

The parameters this rank holds, or None for all of them.

This is the whole ownership contract. Override it when producers are split so each holds only part of the model — pipeline parallelism (a rank holds some layers), expert parallelism (a rank holds some experts), or any combination, including layouts that fit neither. A consumer routes each name to a rank that holds it, so per-name is the granularity that matters; the engine derives everything else from this.

Three requirements come with overriding it:

`metadata()`

must still describe the WHOLE model on every rank. The group partition, the iteration checks and the consumers' pull plans are all built from one rank's metadata, so a rank that reported only its own share would leave the rest of the model silently un-transferred. The sharded-RDT engine cross-checks this across ranks at init.- Every name must be held by at least one rank, or it can never be served. The engine raises at init naming the first orphan.
- Iteration must cover exactly
`groups()`

in metadata order, yielding a real tensor for each held name and`None`

for the rest. A group's gather is a collective among the ranks that hold part of it, so the name must still appear (to keep the order check aligned) while the data is absent.

Returns:

-

–[Collection](https://docs.python.org/3/library/collections.abc.html#collections.abc.Collection)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | NoneThe held parameter names, or None to hold every one.


## Source code in `vllm/distributed/weight_transfer/base.py`


###

`iter_groups()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightSource.iter_groups)

Yield one `(names, tensors)`

batch per group from `groups()`

.

The default drives `__iter__`

and batches its output, checking as it goes that the names arrive in metadata order — ranks sharing a parameter materialize it with a collective, so a rank that iterates out of order deadlocks its peers rather than returning wrong data.

Override when a backend can produce a whole group at once. Materializing is usually a collective, and driving it per group instead of per tensor turns ~37k generator resumes into ~95 on a per-expert MoE model (worth ~0.9s per sync there). An override must yield the same batches in the same order as this default.

## Source code in `vllm/distributed/weight_transfer/base.py`


###

`metadata()`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightSource.metadata)

Declare what iteration will yield, without transferring anything.

Must agree with iteration element for element: the same parameters, in the same order, with the same dtypes and shapes. Backends may read both channels and trust that they match (dense NCCL sizes the worker's receive buffers and its packed chunk boundaries from this, then sends the bytes from iteration), so a source that disagrees between the two splits the stream differently on each side.

## Source code in `vllm/distributed/weight_transfer/base.py`


##

`WeightTransferEngine`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngine)

Bases:

, [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)[Generic](https://docs.python.org/3/library/typing.html#typing.Generic)[TInitInfo, TUpdateInfo]

Base class for weight transfer engines that handle transport of model weights from a trainer to inference workers.

This abstraction separates weight transfer transport logic from the worker implementation, allowing different backends (NCCL, CUDA IPC, RDMA[TODO]) to be plugged in.

Each engine owns its full weight-update lifecycle: `start_weight_update`

, `update_weights`

, and `finish_weight_update`

. Layerwise reloading (used by checkpoint-format engines) is opted into per engine by running it inside `start_weight_update`

/`finish_weight_update`

. Engines that apply weights in place (e.g. sparse patches) leave those methods as no-ops.

## Subclasses should define

init_info_cls: Type of backend-specific initialization info update_info_cls: Type of backend-specific update info

Methods:

-
–[__init__](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngine.__init__)Initialize the weight transfer engine.

-
–[drain_pending](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngine.drain_pending)Block until every deferred update has been applied to the model.

-
–[finish_weight_update](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngine.finish_weight_update)Finalize the current weight update.

-
–[init_transfer_engine](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngine.init_transfer_engine)Initialize the weight transfer mechanism.

-
–[parse_init_info](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngine.parse_init_info)Construct typed init info from dict with validation.

-
–[parse_update_info](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngine.parse_update_info)Construct typed update info from dict with validation.

-
–[receive_weights](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngine.receive_weights)Receive weights from the trainer and load them into the model.

-
–[reset_weight_update_target](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngine.reset_weight_update_target)Restore weight updates to the engine's default target model.

-
–[set_weight_update_target](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngine.set_weight_update_target)Set the model that will receive the active weight update.

-
–[shutdown](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngine.shutdown)Shutdown the weight transfer engine.

-
–[start_weight_update](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngine.start_weight_update)Prepare the engine for a new weight update.

-
–[update_weights](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngine.update_weights)Receive one weight update chunk and load it into the model.


Attributes:

-
([defers_processing](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngine.defers_processing)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether

`update_weights`

returns before the weights are on the device.

## Source code in `vllm/distributed/weight_transfer/base.py`


|
|

###

`defers_processing = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngine.defers_processing)

Whether `update_weights`

returns before the weights are on the device.

An engine that pipelines its GPU post-processing onto background threads cannot let `update_weights`

synchronize the device — that would block on those threads and serialize the pipeline. Such an engine sets this True, omits the per-update sync, and guarantees completion in `finish_weight_update`

instead.

Callers that go through `finish_weight_update`

need do nothing: the engine drains there. A caller that instead drives the tail itself — running its own `finalize_layerwise_reload`

, say — must read this flag and call `drain_pending()`

first, because with it set a returned `update_weights`

means "queued", not "applied".

###

`__init__(config, vllm_config, device, model)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngine.__init__)

Initialize the weight transfer engine.

Parameters:

-

(`config`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngine.__init__(config))

) –[WeightTransferConfig](https://docs.vllm.ai/config/weight_transfer/#vllm.config.weight_transfer.WeightTransferConfig)The configuration for the weight transfer engine

-

(`vllm_config`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngine.__init__(vllm_config))

) –[VllmConfig](https://docs.vllm.ai/config/#vllm.config.VllmConfig)The full vLLM config (provides parallel/model config)

-

(`device`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngine.__init__(device))

) –[device](https://pytorch.org/docs/stable/tensor_attributes.html#torch.device)The device this worker's model lives on

-

(`model`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngine.__init__(model))

) –[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)The local model instance which will receive the weights


## Source code in `vllm/distributed/weight_transfer/base.py`


###

`drain_pending()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngine.drain_pending)

Block until every deferred update has been applied to the model.

The companion to `defers_processing`

: a caller that has taken over the update tail calls this to re-establish the guarantee that `finish_weight_update`

would otherwise have given it. Idempotent, and a no-op by default — an engine that processes synchronously has nothing to drain, so this is always safe to call.

## Source code in `vllm/distributed/weight_transfer/base.py`


###

`finish_weight_update()`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngine.finish_weight_update)

Finalize the current weight update.

Checkpoint-format engines finalize layerwise reloading here; engines that apply weights in place leave this as a no-op.

## Source code in `vllm/distributed/weight_transfer/base.py`


###

`init_transfer_engine(init_info)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngine.init_transfer_engine)

Initialize the weight transfer mechanism. This is called once at the beginning of training.

Parameters:

-

(`init_info`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngine.init_transfer_engine(init_info))`TInitInfo`

) –Backend-specific initialization info


## Source code in `vllm/distributed/weight_transfer/base.py`


###

`parse_init_info(init_dict)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngine.parse_init_info)

Construct typed init info from dict with validation.

Parameters:

Returns:

-
`TInitInfo`

–Typed backend-specific init info dataclass


Raises:

-

–[ValueError](https://docs.python.org/3/builtins/exceptions.html#ValueError)If init_dict is invalid for this backend


## Source code in `vllm/distributed/weight_transfer/base.py`


###

`parse_update_info(update_dict)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngine.parse_update_info)

Construct typed update info from dict with validation.

Parameters:

Returns:

-
`TUpdateInfo`

–Typed backend-specific update info dataclass


Raises:

-

–[ValueError](https://docs.python.org/3/builtins/exceptions.html#ValueError)If update_dict is invalid for this backend


## Source code in `vllm/distributed/weight_transfer/base.py`


###

`receive_weights(update_info)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngine.receive_weights)

Receive weights from the trainer and load them into the model.

Parameters:

-

(`update_info`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngine.receive_weights(update_info))`TUpdateInfo`

) –Backend-specific update info containing parameter metadata and any backend-specific data


## Source code in `vllm/distributed/weight_transfer/base.py`


###

`reset_weight_update_target()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngine.reset_weight_update_target)

Restore weight updates to the engine's default target model.

###

`set_weight_update_target(model, model_config)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngine.set_weight_update_target)

Set the model that will receive the active weight update.

###

`shutdown()`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngine.shutdown)

Shutdown the weight transfer engine. This should be called when the worker is shutting down.

###

`start_weight_update()`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngine.start_weight_update)

Prepare the engine for a new weight update.

Engines that receive weights in checkpoint format initialize layerwise reloading here, else this is typically a no-op. See: https://docs.vllm.ai/en/latest/training/layerwise/ for more details.

## Source code in `vllm/distributed/weight_transfer/base.py`


###

`update_weights(update_info)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngine.update_weights)

Receive one weight update chunk and load it into the model.

Parameters:

## Source code in `vllm/distributed/weight_transfer/base.py`


##

`WeightTransferEngineFactory`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngineFactory)

Factory for creating weight transfer engines with lazy loading.

This factory implements a registry pattern that supports: - Lazy loading: Engine modules are only imported when actually needed - Extensibility: Custom engines can be registered at runtime - Centralized registration: All built-in engines registered in one place

Methods:

-
–[create_engine](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngineFactory.create_engine)Create a weight transfer engine instance.

-
–[register_engine](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngineFactory.register_engine)Register an engine with lazy-loading or direct class reference.


## Source code in `vllm/distributed/weight_transfer/factory.py`


|
|

###

`create_engine(config, vllm_config, device, model)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngineFactory.create_engine)

Create a weight transfer engine instance.

Parameters:

-

(`config`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngineFactory.create_engine(config))

) –[WeightTransferConfig](https://docs.vllm.ai/config/weight_transfer/#vllm.config.weight_transfer.WeightTransferConfig)Weight transfer configuration containing the backend name

-

(`vllm_config`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngineFactory.create_engine(vllm_config))

) –[VllmConfig](https://docs.vllm.ai/config/#vllm.config.VllmConfig)The full vLLM config (provides parallel/model config)

-

(`device`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngineFactory.create_engine(device))

) –[device](https://pytorch.org/docs/stable/tensor_attributes.html#torch.device)The device this worker's model lives on

-

(`model`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngineFactory.create_engine(model))

) –[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)The local model instance which will receive the weights


Returns:

-

–[WeightTransferEngine](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base.WeightTransferEngine)An initialized weight transfer engine instance


Raises:

-

–[ValueError](https://docs.python.org/3/builtins/exceptions.html#ValueError)If the backend is not registered


## Source code in `vllm/distributed/weight_transfer/factory.py`


###

`register_engine(name, module_path_or_cls, class_name=None)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngineFactory.register_engine)

Register an engine with lazy-loading or direct class reference.

Supports two calling conventions: 1. Lazy loading: register_engine(name, module_path, class_name) 2. Direct class: register_engine(name, engine_cls)

Parameters:

-

(`name`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngineFactory.register_engine(name))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The name to register the engine under (e.g., "nccl")

-

(`module_path_or_cls`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngineFactory.register_engine(module_path_or_cls))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)|[type](https://docs.python.org/3/builtins/functions.html#type)[[WeightTransferEngine](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base.WeightTransferEngine)]Either a module path string for lazy loading, or the engine class directly

-

(`class_name`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferEngineFactory.register_engine(class_name))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –Name of the engine class (required if module_path is string)


Raises:

-

–[ValueError](https://docs.python.org/3/builtins/exceptions.html#ValueError)If an engine with the same name is already registered


## Source code in `vllm/distributed/weight_transfer/factory.py`


##

`WeightTransferTrainerFactory`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferTrainerFactory)

Factory for creating trainer-side weight transfer engines.

Parallel to `WeightTransferEngineFactory`

, with its own lazy-import registry. The trainer-side and worker-side registries are kept separate: they share backend names by convention, but the trainer process never instantiates a worker engine and vice versa, so unifying them would only couple the import graphs.

Methods:

-
–[register_engine](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferTrainerFactory.register_engine)Register a trainer engine. Same conventions as

-
–[trainer_init](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferTrainerFactory.trainer_init)Build and rendezvous a ready-to-send trainer engine.


## Source code in `vllm/distributed/weight_transfer/factory.py`


|
|

###

`register_engine(name, module_path_or_cls, class_name=None)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferTrainerFactory.register_engine)

Register a trainer engine. Same conventions as `WeightTransferEngineFactory.register_engine`

.

## Source code in `vllm/distributed/weight_transfer/factory.py`


###

`trainer_init(init_info, *, client, source=None)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferTrainerFactory.trainer_init)

Build and rendezvous a ready-to-send trainer engine.

Called on every trainer rank (multi-rank trainers construct on all ranks; the sender is resolved inside the engine's `trainer_init`

).

The trainer side takes no `WeightTransferConfig`

and no separate `backend`

argument: the backend is read from `init_info.backend`

(a `ClassVar`

on each `TrainerInitInfo`

subclass), and the static wire params ride `init_info`

.

Parameters:

-

(`init_info`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferTrainerFactory.trainer_init(init_info))

) –[TrainerInitInfo](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base.TrainerInitInfo)Backend-specific trainer init info. Its

`backend`

selects the engine; it also carries the wire params (e.g.`packed`

). -

(`client`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferTrainerFactory.trainer_init(client))

) –[VLLMWeightSyncClient](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base.VLLMWeightSyncClient)Inference-side control-plane client.

-

(`source`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.WeightTransferTrainerFactory.trainer_init(source))

, default:[WeightSource](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base.WeightSource)| None`None`

) –`WeightSource`

of`(name, tensor)`

pairs to send each round, for full-resync backends (NCCL, IPC). Sparse backend omits it and passes its per-round payload to`send_weights`

.

Raises:

-

–[ValueError](https://docs.python.org/3/builtins/exceptions.html#ValueError)If

`init_info.backend`

is not registered.