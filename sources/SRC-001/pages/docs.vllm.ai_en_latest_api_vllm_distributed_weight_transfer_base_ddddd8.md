source: https://docs.vllm.ai/en/latest/api/vllm/distributed/weight_transfer/base/
lastmod: 2026-09-23

#

`vllm.distributed.weight_transfer.base`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base)

Base class for weight transfer engines.

Classes:

-
–[ModuleSource](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.ModuleSource)`WeightSource`

over`module.named_parameters()`

— the common case. -
–[ParamMeta](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.ParamMeta)Name / wire dtype / full (HF) shape for one output parameter.

-
–[TrainerInitInfo](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.TrainerInitInfo)Base trainer-side init info: which trainer rank drives the transfer.

-
–[TrainerWeightTransferEngine](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.TrainerWeightTransferEngine)Trainer-side weight transfer engine.

-
–[VLLMWeightSyncClient](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.VLLMWeightSyncClient)Trainer-side stub for the inference engine's weight-sync control plane.

-
–[WeightSource](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightSource)A re-iterable source of the trainer's weights, handed to a trainer engine.

-
–[WeightTransferEngine](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferEngine)Base class for weight transfer engines that handle transport of model weights

-
–[WeightTransferInitInfo](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferInitInfo)Base class for backend-specific initialization info.

-
–[WeightTransferInitRequest](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferInitRequest)API-level weight transfer initialization request.

-
–[WeightTransferUpdateInfo](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferUpdateInfo)Base class for backend-specific weight update info.

-
–[WeightTransferUpdateRequest](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferUpdateRequest)API-level weight update request.


Functions:

-
–[layerwise_groups](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.layerwise_groups)Partition flat parameter names into one group per decoder layer, keyed on

-
–[materialize_full_tensor](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.materialize_full_tensor)Return a full, locally-materialized tensor ready to send.


##

`ModuleSource`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.ModuleSource)

Bases: [WeightSource](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightSource)

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

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.ParamMeta)

Name / wire dtype / full (HF) shape for one output parameter.

## Source code in `vllm/distributed/weight_transfer/base.py`


##

`TrainerInitInfo`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.TrainerInitInfo)

Base trainer-side init info: which trainer rank drives the transfer.

`rank`

is this trainer process's rank, provided **explicitly** by the caller — the engine does not read it from a global process group, which is ambiguous once several groups (FSDP / TP / PP / EP) exist. Rank 0 is always the sender: only it opens the endpoint and drives the inference-side RPCs, while every rank still runs the trainer-side collectives. Backend subclasses add their own (positional) fields; `rank`

is keyword-only so that ordering never conflicts.

Every concrete subclass sets a class-level `backend`

string (the same key it registers under in `WeightTransferTrainerFactory`

). The factory reads it to dispatch, so callers pass only the init info/ It is a `ClassVar`

(a fixed per-backend constant), so it is not an `__init__`

field.

## Source code in `vllm/distributed/weight_transfer/base.py`


##

`TrainerWeightTransferEngine`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.TrainerWeightTransferEngine)

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
–[send_weights](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.TrainerWeightTransferEngine.send_weights)Push weights to inference workers and drive the full update round

-
–[shutdown](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.TrainerWeightTransferEngine.shutdown)Tear down communicators / process groups. Default no-op.

-
–[trainer_init](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.TrainerWeightTransferEngine.trainer_init)Rendezvous with the inference side and return a ready instance.


## Source code in `vllm/distributed/weight_transfer/base.py`


|
|

###

`send_weights()`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.TrainerWeightTransferEngine.send_weights)

Push weights to inference workers and drive the full update round trip: `start_weight_update`

, `update_weights`

(run concurrently with the trainer-side broadcast when the backend requires it), then `finish_weight_update`

. Called on every trainer rank.

## Source code in `vllm/distributed/weight_transfer/base.py`


###

`shutdown()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.TrainerWeightTransferEngine.shutdown)

###

`trainer_init(init_info, *, client, source=None)`

`abstractmethod`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.TrainerWeightTransferEngine.trainer_init)

Rendezvous with the inference side and return a ready instance.

Called on every trainer rank. The sender drives the full handshake via `client`

(build the worker-side init info, call `client.init_weight_transfer_engine`

, open the trainer-side endpoint); non-sender ranks skip the rendezvous and the RPC.

## Source code in `vllm/distributed/weight_transfer/base.py`


##

`VLLMWeightSyncClient`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.VLLMWeightSyncClient)

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

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightSource)

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
–[groups](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightSource.groups)This rank's gather groups, in metadata order:

`layerwise_groups`

over -
–[held_names](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightSource.held_names)The parameters this rank holds, or None for all of them.

-
–[iter_groups](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightSource.iter_groups)Yield one

`(names, tensors)`

batch per group from`groups()`

. -
–[metadata](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightSource.metadata)Declare what iteration will yield, without transferring anything.


## Source code in `vllm/distributed/weight_transfer/base.py`


|
|

###

`groups()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightSource.groups)

This rank's gather groups, in metadata order: `layerwise_groups`

over `metadata()`

, restricted to the groups holding at least one held name.

A group with nothing held here is not iterated at all — its gather is a collective among the ranks that do hold part of it.

## Source code in `vllm/distributed/weight_transfer/base.py`


###

`held_names()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightSource.held_names)

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

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightSource.iter_groups)

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

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightSource.metadata)

Declare what iteration will yield, without transferring anything.

Must agree with iteration element for element: the same parameters, in the same order, with the same dtypes and shapes. Backends may read both channels and trust that they match (dense NCCL sizes the worker's receive buffers and its packed chunk boundaries from this, then sends the bytes from iteration), so a source that disagrees between the two splits the stream differently on each side.

## Source code in `vllm/distributed/weight_transfer/base.py`


##

`WeightTransferEngine`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferEngine)

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
–[__init__](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferEngine.__init__)Initialize the weight transfer engine.

-
–[drain_pending](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferEngine.drain_pending)Block until every deferred update has been applied to the model.

-
–[finish_weight_update](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferEngine.finish_weight_update)Finalize the current weight update.

-
–[init_transfer_engine](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferEngine.init_transfer_engine)Initialize the weight transfer mechanism.

-
–[parse_init_info](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferEngine.parse_init_info)Construct typed init info from dict with validation.

-
–[parse_update_info](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferEngine.parse_update_info)Construct typed update info from dict with validation.

-
–[receive_weights](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferEngine.receive_weights)Receive weights from the trainer and load them into the model.

-
–[reset_weight_update_target](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferEngine.reset_weight_update_target)Restore weight updates to the engine's default target model.

-
–[set_weight_update_target](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferEngine.set_weight_update_target)Set the model that will receive the active weight update.

-
–[shutdown](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferEngine.shutdown)Shutdown the weight transfer engine.

-
–[start_weight_update](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferEngine.start_weight_update)Prepare the engine for a new weight update.

-
–[update_weights](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferEngine.update_weights)Receive one weight update chunk and load it into the model.


Attributes:

-
([defers_processing](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferEngine.defers_processing)

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

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferEngine.defers_processing)

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

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferEngine.__init__)

Initialize the weight transfer engine.

Parameters:

-

(`config`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferEngine.__init__(config))

) –[WeightTransferConfig](https://docs.vllm.ai/config/weight_transfer/#vllm.config.weight_transfer.WeightTransferConfig)The configuration for the weight transfer engine

-

(`vllm_config`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferEngine.__init__(vllm_config))

) –[VllmConfig](https://docs.vllm.ai/config/#vllm.config.VllmConfig)The full vLLM config (provides parallel/model config)

-

(`device`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferEngine.__init__(device))

) –[device](https://pytorch.org/docs/stable/tensor_attributes.html#torch.device)The device this worker's model lives on

-

(`model`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferEngine.__init__(model))

) –[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)The local model instance which will receive the weights


## Source code in `vllm/distributed/weight_transfer/base.py`


###

`drain_pending()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferEngine.drain_pending)

Block until every deferred update has been applied to the model.

The companion to `defers_processing`

: a caller that has taken over the update tail calls this to re-establish the guarantee that `finish_weight_update`

would otherwise have given it. Idempotent, and a no-op by default — an engine that processes synchronously has nothing to drain, so this is always safe to call.

## Source code in `vllm/distributed/weight_transfer/base.py`


###

`finish_weight_update()`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferEngine.finish_weight_update)

Finalize the current weight update.

Checkpoint-format engines finalize layerwise reloading here; engines that apply weights in place leave this as a no-op.

## Source code in `vllm/distributed/weight_transfer/base.py`


###

`init_transfer_engine(init_info)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferEngine.init_transfer_engine)

Initialize the weight transfer mechanism. This is called once at the beginning of training.

Parameters:

-

(`init_info`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferEngine.init_transfer_engine(init_info))`TInitInfo`

) –Backend-specific initialization info


## Source code in `vllm/distributed/weight_transfer/base.py`


###

`parse_init_info(init_dict)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferEngine.parse_init_info)

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

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferEngine.parse_update_info)

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

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferEngine.receive_weights)

Receive weights from the trainer and load them into the model.

Parameters:

-

(`update_info`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferEngine.receive_weights(update_info))`TUpdateInfo`

) –Backend-specific update info containing parameter metadata and any backend-specific data


## Source code in `vllm/distributed/weight_transfer/base.py`


###

`reset_weight_update_target()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferEngine.reset_weight_update_target)

Restore weight updates to the engine's default target model.

###

`set_weight_update_target(model, model_config)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferEngine.set_weight_update_target)

Set the model that will receive the active weight update.

###

`shutdown()`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferEngine.shutdown)

Shutdown the weight transfer engine. This should be called when the worker is shutting down.

###

`start_weight_update()`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferEngine.start_weight_update)

Prepare the engine for a new weight update.

Engines that receive weights in checkpoint format initialize layerwise reloading here, else this is typically a no-op. See: https://docs.vllm.ai/en/latest/training/layerwise/ for more details.

## Source code in `vllm/distributed/weight_transfer/base.py`


###

`update_weights(update_info)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferEngine.update_weights)

Receive one weight update chunk and load it into the model.

Parameters:

## Source code in `vllm/distributed/weight_transfer/base.py`


##

`WeightTransferInitInfo`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferInitInfo)

##

`WeightTransferInitRequest`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferInitRequest)

##

`WeightTransferUpdateInfo`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferUpdateInfo)

##

`WeightTransferUpdateRequest`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.WeightTransferUpdateRequest)

##

`_stack_key(name)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base._stack_key)

`(prefix, index)`

of the OUTERMOST integer segment, or None if there is none.

Outermost is what keeps a MoE layer whole: `model.layers.3.mlp.experts.7.w1`

keys on the layer, not the expert.

## Source code in `vllm/distributed/weight_transfer/base.py`


##

`layerwise_groups(names)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.layerwise_groups)

Partition flat parameter names into one group per decoder layer, keyed on the outermost index segment of each name.

This defines what a *group index* means for `WeightSource.groups`

and `WeightSource.iter_groups`

: index *g* names the same group on every trainer rank and every consumer, because it is derived from one rank's `metadata()`

order.

Keying on the index rather than a literal prefix needs no per-architecture naming table: `model.layers.0.`

, `model.language_model.layers.0.`

, `transformer.h.0.`

, `backbone.layers.0.`

and a vision tower's `visual.blocks.0.`

all partition alike. Matching one fixed prefix does not, and its failure is silent — every name lands in a single group holding the whole model, which defeats the per-layer bound below.

Un-indexed names split by POSITION relative to the first indexed one: the pre block (embeddings) and the post block (the final norm, `lm_head`

, and any inter-stack projector). Post lands last however early it arrived, which is what a pipeline-parallel source needs — Megatron-Bridge streams the last stage's output block *before* its layers.

Stacks come out in first-appearance order of their prefix and ascending index within it, whatever order the source yielded them, so a source can normalize an arbitrary export order by flattening this partition.

Backends that gather and free per group (sharded RDT) also use it as the unit of transfer, which bounds their buffer sizes: without it a whole model becomes one chunk.

## Source code in `vllm/distributed/weight_transfer/base.py`


##

`materialize_full_tensor(tensor)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.base.materialize_full_tensor)

Return a full, locally-materialized tensor ready to send.

FSDP shards (DTensors) expose `full_tensor()`

, a collective all-gather; regular tensors do not and are returned unchanged. Trainer engines call this at send time so the (potentially expensive) gather happens exactly once — reading `.shape`

/`.dtype`

for metadata does not trigger it.