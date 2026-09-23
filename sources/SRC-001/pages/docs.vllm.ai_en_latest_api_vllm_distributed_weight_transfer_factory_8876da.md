source: https://docs.vllm.ai/en/latest/api/vllm/distributed/weight_transfer/factory/
lastmod: 2026-09-23

#

`vllm.distributed.weight_transfer.factory`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.factory)

Factory for weight transfer engines with lazy loading.

Classes:

-
–[WeightTransferEngineFactory](https://docs.vllm.ai#vllm.distributed.weight_transfer.factory.WeightTransferEngineFactory)Factory for creating weight transfer engines with lazy loading.

-
–[WeightTransferTrainerFactory](https://docs.vllm.ai#vllm.distributed.weight_transfer.factory.WeightTransferTrainerFactory)Factory for creating trainer-side weight transfer engines.


##

`WeightTransferEngineFactory`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.factory.WeightTransferEngineFactory)

Factory for creating weight transfer engines with lazy loading.

This factory implements a registry pattern that supports: - Lazy loading: Engine modules are only imported when actually needed - Extensibility: Custom engines can be registered at runtime - Centralized registration: All built-in engines registered in one place

Methods:

-
–[create_engine](https://docs.vllm.ai#vllm.distributed.weight_transfer.factory.WeightTransferEngineFactory.create_engine)Create a weight transfer engine instance.

-
–[register_engine](https://docs.vllm.ai#vllm.distributed.weight_transfer.factory.WeightTransferEngineFactory.register_engine)Register an engine with lazy-loading or direct class reference.


## Source code in `vllm/distributed/weight_transfer/factory.py`


|
|

###

`create_engine(config, vllm_config, device, model)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.factory.WeightTransferEngineFactory.create_engine)

Create a weight transfer engine instance.

Parameters:

-

(`config`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.factory.WeightTransferEngineFactory.create_engine(config))

) –[WeightTransferConfig](https://docs.vllm.ai/config/weight_transfer/#vllm.config.weight_transfer.WeightTransferConfig)Weight transfer configuration containing the backend name

-

(`vllm_config`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.factory.WeightTransferEngineFactory.create_engine(vllm_config))

) –[VllmConfig](https://docs.vllm.ai/config/#vllm.config.VllmConfig)The full vLLM config (provides parallel/model config)

-

(`device`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.factory.WeightTransferEngineFactory.create_engine(device))

) –[device](https://pytorch.org/docs/stable/tensor_attributes.html#torch.device)The device this worker's model lives on

-

(`model`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.factory.WeightTransferEngineFactory.create_engine(model))

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

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.factory.WeightTransferEngineFactory.register_engine)

Register an engine with lazy-loading or direct class reference.

Supports two calling conventions: 1. Lazy loading: register_engine(name, module_path, class_name) 2. Direct class: register_engine(name, engine_cls)

Parameters:

-

(`name`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.factory.WeightTransferEngineFactory.register_engine(name))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The name to register the engine under (e.g., "nccl")

-

(`module_path_or_cls`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.factory.WeightTransferEngineFactory.register_engine(module_path_or_cls))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)|[type](https://docs.python.org/3/builtins/functions.html#type)[[WeightTransferEngine](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base.WeightTransferEngine)]Either a module path string for lazy loading, or the engine class directly

-

(`class_name`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.factory.WeightTransferEngineFactory.register_engine(class_name))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –Name of the engine class (required if module_path is string)


Raises:

-

–[ValueError](https://docs.python.org/3/builtins/exceptions.html#ValueError)If an engine with the same name is already registered


## Source code in `vllm/distributed/weight_transfer/factory.py`


##

`WeightTransferTrainerFactory`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.factory.WeightTransferTrainerFactory)

Factory for creating trainer-side weight transfer engines.

Parallel to `WeightTransferEngineFactory`

, with its own lazy-import registry. The trainer-side and worker-side registries are kept separate: they share backend names by convention, but the trainer process never instantiates a worker engine and vice versa, so unifying them would only couple the import graphs.

Methods:

-
–[register_engine](https://docs.vllm.ai#vllm.distributed.weight_transfer.factory.WeightTransferTrainerFactory.register_engine)Register a trainer engine. Same conventions as

-
–[trainer_init](https://docs.vllm.ai#vllm.distributed.weight_transfer.factory.WeightTransferTrainerFactory.trainer_init)Build and rendezvous a ready-to-send trainer engine.


## Source code in `vllm/distributed/weight_transfer/factory.py`


|
|

###

`register_engine(name, module_path_or_cls, class_name=None)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.factory.WeightTransferTrainerFactory.register_engine)

Register a trainer engine. Same conventions as `WeightTransferEngineFactory.register_engine`

.

## Source code in `vllm/distributed/weight_transfer/factory.py`


###

`trainer_init(init_info, *, client, source=None)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.factory.WeightTransferTrainerFactory.trainer_init)

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

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.factory.WeightTransferTrainerFactory.trainer_init(init_info))

) –[TrainerInitInfo](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base.TrainerInitInfo)Backend-specific trainer init info. Its

`backend`

selects the engine; it also carries the wire params (e.g.`packed`

). -

(`client`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.factory.WeightTransferTrainerFactory.trainer_init(client))

) –[VLLMWeightSyncClient](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base.VLLMWeightSyncClient)Inference-side control-plane client.

-

(`source`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.factory.WeightTransferTrainerFactory.trainer_init(source))

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