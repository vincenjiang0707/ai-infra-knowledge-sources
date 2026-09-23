source: https://docs.vllm.ai/en/latest/training/weight_transfer/
lastmod: 2026-09-23

# Weight Transfer[¶](https://docs.vllm.ai#weight-transfer)

vLLM provides a pluggable weight transfer system for synchronizing model weights from a training process to the inference engine during reinforcement learning (RL) workflows. This is essential for RLHF, GRPO, and other online RL methods where the policy model is iteratively updated during training and the updated weights must be reflected in the inference engine for rollout generation.

## Architecture[¶](https://docs.vllm.ai#architecture)

Weight transfer has **two engines, one per process**, and they are symmetric:

| Trainer process | Inference workers | |
|---|---|---|
| Class |
`TrainerWeightTransferEngine` |

`WeightTransferEngine`

`WeightTransferTrainerFactory.trainer_init(...)`

`WeightTransferConfig`

`send_weights()`

The trainer engine is stateful: it owns its communicators and wire params, pulls weights from a [ WeightSource](https://docs.vllm.ai/base/#weightsource), and drives the inference side through a

[. Trainer code never has to know the transport, and never has to thread transfer state back in on every round — one](https://docs.vllm.ai/base/#vllmweightsyncclient)

`VLLMWeightSyncClient`

`send_weights()`

call per sync.Under the hood every round is the same **four-phase protocol**, which the trainer engine drives on your behalf:

**Initialization**(`init_weight_transfer_engine`

): establishes the communication channel between the trainer and inference workers. Called once, from`trainer_init`

, before the training loop begins.**Start**(`start_weight_update`

): prepares the inference engine for a weight update.**Weight Update**(`update_weights`

): transfers updated weights. May be called one or more times (e.g. for chunked transfers).**Finish**(`finish_weight_update`

): finalizes the update (e.g. runs post-processing for checkpoint-format weights). Called once after all weights have been transferred.

## Available Backends[¶](https://docs.vllm.ai#available-backends)

| Backend | Transport | Use Case |
|---|---|---|
|

[IPC](https://docs.vllm.ai/ipc/)[sparse_nccl](https://docs.vllm.ai/nccl/#sparse-nccl)[sharded_rdt](https://docs.vllm.ai/sharded_rdt/)## Quickstart[¶](https://docs.vllm.ai#quickstart)

### Inference Side[¶](https://docs.vllm.ai#inference-side)

The inference side takes only a backend name. Everything else about the transfer is decided by the trainer and shipped over at the init handshake.

from vllm import LLM
from vllm.config import WeightTransferConfig
llm = LLM(
model="my-model",
weight_transfer_config=WeightTransferConfig(backend="nccl"), # or "ipc", "sparse_nccl", "sharded_rdt"
)


Or, for online serving:

### Trainer Side[¶](https://docs.vllm.ai#trainer-side)

Build the engine once, then call `send_weights()`

once per sync:

from vllm.distributed.weight_transfer import (
ModuleSource,
HTTPVLLMWeightSyncClient,
WeightTransferTrainerFactory,
)
from vllm.distributed.weight_transfer.nccl_engine import NCCLTrainerInitInfo
# Once, before the training loop.
engine = WeightTransferTrainerFactory.trainer_init(
init_info=NCCLTrainerInitInfo(
master_address=master_address,
master_port=master_port,
world_size=world_size, # trainer + all inference workers
rank=0, # this trainer rank; rank 0 is the sender
packed=True,
),
client=HTTPVLLMWeightSyncClient("http://localhost:8000"),
source=ModuleSource(model),
)
# Once per weight sync.
for step in range(num_steps):
train_one_step(model)
engine.send_weights()


`send_weights()`

drives start → update → finish on the inference side *and* the data-plane transfer, including any concurrency the backend needs (NCCL, for example, must run the workers' `update_weights`

at the same time as the trainer's broadcast, since both rendezvous inside the same NCCL calls).

There is no `backend=`

argument on the trainer side: each [ TrainerInitInfo](https://docs.vllm.ai/api/vllm/distributed/weight_transfer/base/#vllm.distributed.weight_transfer.base.TrainerInitInfo) subclass declares its own

`backend`

, and the factory dispatches on it.## Where Each Setting Lives[¶](https://docs.vllm.ai#where-each-setting-lives)

The trainer is the single source of truth for anything the two sides must agree on. This is the main rule to internalize:

| Setting | Lives on | Notes |
|---|---|---|
| Backend, inference side | `WeightTransferConfig(backend=...)` | A plain string selector — that is all this config holds |
| Backend, trainer side | `init_info.backend` | A `ClassVar` on each init info; never passed by hand |
Wire params (`packed` , buffer sizes) | the backend's
`TrainerInitInfo` |

`trainer_init`

, so the two sides *cannot*disagree`WeightSource`

`ModuleSource(model)`

covers plain and FSDP-sharded modules`source.metadata()`

, or from a delta backend's per-round payload); you never construct itNote

Wire params are deliberately *not* on [ WeightTransferConfig](https://docs.vllm.ai/api/vllm/config/weight_transfer/#vllm.config.weight_transfer.WeightTransferConfig) and

*not*on the per-round update info. Because the trainer ships them at init and the worker reads what it was told, a mismatched

`packed`

flag between the two sides is unrepresentable rather than merely discouraged.## Multi-Rank Trainers[¶](https://docs.vllm.ai#multi-rank-trainers)

For sharded trainers (FSDP, TP/PP/EP), **every trainer rank builds an engine and calls send_weights()**. Rank 0 is the sender: only it holds a communicator, talks to the client, and puts bytes on the wire. Non-sender ranks still iterate the

[, because materializing a parameter is usually itself a collective (an FSDP](https://docs.vllm.ai/api/vllm/distributed/weight_transfer/base/#vllm.distributed.weight_transfer.base.WeightSource)

`WeightSource`

`full_tensor()`

all-gather, a Megatron export) that would deadlock if some ranks skipped it.Pass each process's own `rank`

on the init info. It is explicit rather than read from a global process group, which is ambiguous once several groups (FSDP / TP / PP / EP) exist.

engine = WeightTransferTrainerFactory.trainer_init(
init_info=NCCLTrainerInitInfo(..., rank=torch.distributed.get_rank()),
client=client,
source=ModuleSource(model),
)
engine.send_weights() # called on every rank


## API Endpoints[¶](https://docs.vllm.ai#api-endpoints)

When running vLLM as an HTTP server, the following endpoints are available for weight transfer. [ HTTPVLLMWeightSyncClient](https://docs.vllm.ai/api/vllm/distributed/weight_transfer/clients/#vllm.distributed.weight_transfer.clients.HTTPVLLMWeightSyncClient) speaks the first four for you.

| Endpoint | Method | Description |
|---|---|---|
`/init_weight_transfer_engine` | POST | Initialize the weight transfer engine with backend-specific info |
`/start_weight_update` | POST | Start a weight update |
`/update_weights` | POST | Transfer a batch of weights with backend-specific metadata |
`/finish_weight_update` | POST | Finish the update and optionally commit its `weight_version` |
`/update_weight_version` | POST | Update `weight_version` without changing model weights |
`/weight_info` | GET | Get the latest committed weight version |
`/pause` | POST | Pause generation before weight sync to handle inflight requests |
`/resume` | POST | Resume generation after weight sync |
`/get_world_size` | GET | Get the number of inference workers (useful for NCCL world size calculation) |

Note

The HTTP weight transfer endpoints require `VLLM_SERVER_DEV_MODE=1`

to be set.

The Rust frontend's optional gRPC `Control`

service exposes the same pause, sleep, weight-transfer, and weight-version lifecycle for trusted sidecars. The `ServerInfo.rl_capabilities`

response reports whether weight transfer and sleep mode were configured. Backend-specific `init_info`

and `update_info`

remain JSON metadata; model tensors continue to move over the configured NCCL, IPC, sparse-NCCL, or sharded-RDT transport.

## Extending the System[¶](https://docs.vllm.ai#extending-the-system)

Every piece of the system is replaceable: the weights you send ([ WeightSource](https://docs.vllm.ai/api/vllm/distributed/weight_transfer/base/#vllm.distributed.weight_transfer.base.WeightSource)), the control-plane transport (

[), and the transports themselves (both engine ABCs, each with its own factory registry). See](https://docs.vllm.ai/api/vllm/distributed/weight_transfer/base/#vllm.distributed.weight_transfer.base.VLLMWeightSyncClient)

`VLLMWeightSyncClient`

[Base Classes](https://docs.vllm.ai/base/).