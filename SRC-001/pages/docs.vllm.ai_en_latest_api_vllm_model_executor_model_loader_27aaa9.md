source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/model_loader/
lastmod: 2026-09-23

#

`vllm.model_executor.model_loader`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader)

Modules:

-
–[base_loader](https://docs.vllm.ai/base_loader/#vllm.model_executor.model_loader.base_loader) -
–[checkpoint_weight_patch](https://docs.vllm.ai/checkpoint_weight_patch/#vllm.model_executor.model_loader.checkpoint_weight_patch)Apply dense or sparse weight updates in checkpoint coordinates.

-
–[default_loader](https://docs.vllm.ai/default_loader/#vllm.model_executor.model_loader.default_loader) -
–[dummy_loader](https://docs.vllm.ai/dummy_loader/#vllm.model_executor.model_loader.dummy_loader) -
–[ep_weight_filter](https://docs.vllm.ai/ep_weight_filter/#vllm.model_executor.model_loader.ep_weight_filter)Filter out non-local expert weights during loading to avoid redundant I/O.

-
–[modelexpress_loader](https://docs.vllm.ai/modelexpress_loader/#vllm.model_executor.model_loader.modelexpress_loader) -
–[mtp_validation](https://docs.vllm.ai/mtp_validation/#vllm.model_executor.model_loader.mtp_validation)Scoped controls for MTP checkpoint completeness validation.

-
–[reload](https://docs.vllm.ai/reload/#vllm.model_executor.model_loader.reload)Layerwise weight reloading utilities for vLLM.

-
–[runai_streamer_loader](https://docs.vllm.ai/runai_streamer_loader/#vllm.model_executor.model_loader.runai_streamer_loader) -
–[sharded_state_loader](https://docs.vllm.ai/sharded_state_loader/#vllm.model_executor.model_loader.sharded_state_loader) -
–[tensorizer](https://docs.vllm.ai/tensorizer/#vllm.model_executor.model_loader.tensorizer) -
–[tensorizer_loader](https://docs.vllm.ai/tensorizer_loader/#vllm.model_executor.model_loader.tensorizer_loader) -
–[utils](https://docs.vllm.ai/utils/#vllm.model_executor.model_loader.utils)Utilities for selecting and loading models.

-
–[weight_cache](https://docs.vllm.ai/weight_cache/#vllm.model_executor.model_loader.weight_cache) -
–[weight_tying](https://docs.vllm.ai/weight_tying/#vllm.model_executor.model_loader.weight_tying)Reconcile word embedding tying with what the checkpoint actually contains.

-
–[weight_utils](https://docs.vllm.ai/weight_utils/#vllm.model_executor.model_loader.weight_utils)Utilities for downloading and initializing model weights.


Classes:

-
–[BaseModelLoader](https://docs.vllm.ai#vllm.model_executor.model_loader.BaseModelLoader)Base class for model loaders.

-
–[DefaultModelLoader](https://docs.vllm.ai#vllm.model_executor.model_loader.DefaultModelLoader)Model loader that can load different file types from disk.

-
–[DummyModelLoader](https://docs.vllm.ai#vllm.model_executor.model_loader.DummyModelLoader)Model loader that will set model weights to random values.

-
–[IpcModelLoader](https://docs.vllm.ai#vllm.model_executor.model_loader.IpcModelLoader)Loads a model by mapping the weight cache daemon's tensors via CUDA IPC.

-
–[ModelExpressModelLoader](https://docs.vllm.ai#vllm.model_executor.model_loader.ModelExpressModelLoader)Thin vLLM loader wrapper for ModelExpress.

-
–[RunaiModelStreamerLoader](https://docs.vllm.ai#vllm.model_executor.model_loader.RunaiModelStreamerLoader)Model loader that can load safetensors

-
–[ShardedStateLoader](https://docs.vllm.ai#vllm.model_executor.model_loader.ShardedStateLoader)Model loader that directly loads each worker's model state dict, which

-
–[TensorizerLoader](https://docs.vllm.ai#vllm.model_executor.model_loader.TensorizerLoader)Model loader using CoreWeave's tensorizer library.


Functions:

-
–[get_model_loader](https://docs.vllm.ai#vllm.model_executor.model_loader.get_model_loader)Get a model loader based on the load format.

-
–[register_model_loader](https://docs.vllm.ai#vllm.model_executor.model_loader.register_model_loader)Register a customized vllm model loader.


##

`BaseModelLoader`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.BaseModelLoader)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Base class for model loaders.

Methods:

-
–[create_model](https://docs.vllm.ai#vllm.model_executor.model_loader.BaseModelLoader.create_model)Create a model with the given configurations.

-
–[download_model](https://docs.vllm.ai#vllm.model_executor.model_loader.BaseModelLoader.download_model)Download a model so that it can be immediately loaded.

-
–[load_model](https://docs.vllm.ai#vllm.model_executor.model_loader.BaseModelLoader.load_model)Load a model with the given configurations.

-
–[load_weights](https://docs.vllm.ai#vllm.model_executor.model_loader.BaseModelLoader.load_weights)Load weights into a model. This standalone API allows


## Source code in `vllm/model_executor/model_loader/base_loader.py`


###

`create_model(vllm_config, model_config, prefix='')`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.BaseModelLoader.create_model)

Create a model with the given configurations.

## Source code in `vllm/model_executor/model_loader/base_loader.py`


###

`download_model(model_config)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.BaseModelLoader.download_model)

###

`load_model(vllm_config, model_config, prefix='')`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.BaseModelLoader.load_model)

Load a model with the given configurations.

## Source code in `vllm/model_executor/model_loader/base_loader.py`


###

`load_weights(model, model_config)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.BaseModelLoader.load_weights)

Load weights into a model. This standalone API allows inplace weights loading for an already-initialized model

## Source code in `vllm/model_executor/model_loader/base_loader.py`


##

`DefaultModelLoader`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.DefaultModelLoader)

Bases: [BaseModelLoader](https://docs.vllm.ai/base_loader/#vllm.model_executor.model_loader.base_loader.BaseModelLoader)

Model loader that can load different file types from disk.

Classes:

-
–[Source](https://docs.vllm.ai#vllm.model_executor.model_loader.DefaultModelLoader.Source)A source for weights.


## Source code in `vllm/model_executor/model_loader/default_loader.py`


|
|

###

`Source`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.DefaultModelLoader.Source)

A source for weights.

Attributes:

-
([allow_patterns_overrides](https://docs.vllm.ai#vllm.model_executor.model_loader.DefaultModelLoader.Source.allow_patterns_overrides)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | NoneIf defined, weights will load exclusively using these patterns.

-
([fall_back_to_pt](https://docs.vllm.ai#vllm.model_executor.model_loader.DefaultModelLoader.Source.fall_back_to_pt)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether .pt weights can be used.

-
([model_or_path](https://docs.vllm.ai#vllm.model_executor.model_loader.DefaultModelLoader.Source.model_or_path)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The model ID or path.

-
([prefix](https://docs.vllm.ai#vllm.model_executor.model_loader.DefaultModelLoader.Source.prefix)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)A prefix to prepend to all weights.

-
([revision](https://docs.vllm.ai#vllm.model_executor.model_loader.DefaultModelLoader.Source.revision)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe optional model revision.

-
([subfolder](https://docs.vllm.ai#vllm.model_executor.model_loader.DefaultModelLoader.Source.subfolder)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe subfolder inside the model repo.


## Source code in `vllm/model_executor/model_loader/default_loader.py`


####

`allow_patterns_overrides = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.DefaultModelLoader.Source.allow_patterns_overrides)

If defined, weights will load exclusively using these patterns.

####

`fall_back_to_pt = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.DefaultModelLoader.Source.fall_back_to_pt)

Whether .pt weights can be used.

####

`model_or_path`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.DefaultModelLoader.Source.model_or_path)

The model ID or path.

####

`prefix = ''`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.DefaultModelLoader.Source.prefix)

A prefix to prepend to all weights.

####

`revision`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.DefaultModelLoader.Source.revision)

The optional model revision.

####

`subfolder = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.DefaultModelLoader.Source.subfolder)

The subfolder inside the model repo.

###

`_get_weights_iterator(source)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.DefaultModelLoader._get_weights_iterator)

Get an iterator for the model weights based on the load format.

## Source code in `vllm/model_executor/model_loader/default_loader.py`


|
|

###

`_init_ep_weight_filter(model_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.DefaultModelLoader._init_ep_weight_filter)

Compute local expert ids for EP weight filtering.

When expert parallelism is active, each rank only needs a subset of expert weights. By computing the set upfront we can skip non-local expert tensors *before* reading them from disk.

## Source code in `vllm/model_executor/model_loader/default_loader.py`


###

`_prepare_weights(model_name_or_path, subfolder, revision, fall_back_to_pt, allow_patterns_overrides)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.DefaultModelLoader._prepare_weights)

Prepare weights for the model.

If the model is not local, it will be downloaded.

## Source code in `vllm/model_executor/model_loader/default_loader.py`


|
|

##

`DummyModelLoader`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.DummyModelLoader)

Bases: [BaseModelLoader](https://docs.vllm.ai/base_loader/#vllm.model_executor.model_loader.base_loader.BaseModelLoader)

Model loader that will set model weights to random values.

## Source code in `vllm/model_executor/model_loader/dummy_loader.py`


###

`_process_online_quant_layer(layer, info)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.DummyModelLoader._process_online_quant_layer)

Materialize, apply dummy weights, and run quantization processing.

## Source code in `vllm/model_executor/model_loader/dummy_loader.py`


##

`IpcModelLoader`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.IpcModelLoader)

Bases: [BaseModelLoader](https://docs.vllm.ai/base_loader/#vllm.model_executor.model_loader.base_loader.BaseModelLoader)

Loads a model by mapping the weight cache daemon's tensors via CUDA IPC.

The model is initialized on the meta device and every parameter/buffer is replaced by the daemon's post-quantized tensor, so process_weights_after_loading is skipped entirely. In "zero_copy" mode the engine shares the daemon's GPU memory; in "copy" mode the tensors are cloned into engine-owned memory and the daemon is asked to release its cache afterwards.

Extra config keys (via --model-loader-extra-config):

- socket_path: explicit daemon socket path. Defaults to a per-GPU path derived from the physical GPU uuid and the cache role (target/draft).
- socket_dir: directory containing the daemon sockets.
- mode: "zero_copy" (default) or "copy".
- fallback: fall back to disk loading when the daemon is unavailable or the fingerprints mismatch (default: True).
- connect_timeout_s: socket connect timeout (default: 5.0).
- state_timeout_s: timeout for the weight-transfer request (default: 300.0).

Note: in zero-copy mode the weights live in the daemon's CUDA IPC allocations, so sleep mode (CuMemAllocator weight offloading) must not be used with this loader.

Methods:

-
–[load_weights](https://docs.vllm.ai#vllm.model_executor.model_loader.IpcModelLoader.load_weights)Best-effort in-place reload for an already-initialized model.


## Source code in `vllm/model_executor/model_loader/weight_cache/ipc_loader.py`


|
|

###

`load_weights(model, model_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.IpcModelLoader.load_weights)

Best-effort in-place reload for an already-initialized model.

Copies daemon tensors into matching parameters/buffers. The model is expected to already be in the post-quantized layout (e.g. previously loaded through this loader).

## Source code in `vllm/model_executor/model_loader/weight_cache/ipc_loader.py`


##

`ModelExpressModelLoader`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.ModelExpressModelLoader)

Bases: [BaseModelLoader](https://docs.vllm.ai/base_loader/#vllm.model_executor.model_loader.base_loader.BaseModelLoader)

Thin vLLM loader wrapper for ModelExpress.

## Source code in `vllm/model_executor/model_loader/modelexpress_loader.py`


##

`RunaiModelStreamerLoader`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.RunaiModelStreamerLoader)

Bases: [BaseModelLoader](https://docs.vllm.ai/base_loader/#vllm.model_executor.model_loader.base_loader.BaseModelLoader)

Model loader that can load safetensors files from local FS, S3, GCS, or Azure Blob Storage.

Methods:

-
–[download_model](https://docs.vllm.ai#vllm.model_executor.model_loader.RunaiModelStreamerLoader.download_model)Download model if necessary.

-
–[load_weights](https://docs.vllm.ai#vllm.model_executor.model_loader.RunaiModelStreamerLoader.load_weights)Load weights into a model.


## Source code in `vllm/model_executor/model_loader/runai_streamer_loader.py`


|
|

###

`_get_weights_iterator(model_or_path, revision)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.RunaiModelStreamerLoader._get_weights_iterator)

Get an iterator for the model weights based on the load format.

## Source code in `vllm/model_executor/model_loader/runai_streamer_loader.py`


###

`_prepare_weights(model_name_or_path, revision)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.RunaiModelStreamerLoader._prepare_weights)

Prepare weights for the model.

If the model is not local, it will be downloaded.

## Source code in `vllm/model_executor/model_loader/runai_streamer_loader.py`


###

`download_model(model_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.RunaiModelStreamerLoader.download_model)

###

`load_weights(model, model_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.RunaiModelStreamerLoader.load_weights)

Load weights into a model.

## Source code in `vllm/model_executor/model_loader/runai_streamer_loader.py`


##

`ShardedStateLoader`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.ShardedStateLoader)

Bases: [BaseModelLoader](https://docs.vllm.ai/base_loader/#vllm.model_executor.model_loader.base_loader.BaseModelLoader)

Model loader that directly loads each worker's model state dict, which enables a fast load path for large tensor-parallel models where each worker only needs to read its own shard rather than the entire checkpoint. See `examples/features/sharded_state/save_sharded_state_offline.py`

for creating a sharded checkpoint.

## Source code in `vllm/model_executor/model_loader/sharded_state_loader.py`


|
|

###

`_filter_subtensors(tensors)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.ShardedStateLoader._filter_subtensors)

Filter out all tensors that share the same memory or a subset of the memory of another tensor.

## Source code in `vllm/model_executor/model_loader/sharded_state_loader.py`


##

`TensorizerLoader`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.TensorizerLoader)

Bases: [BaseModelLoader](https://docs.vllm.ai/base_loader/#vllm.model_executor.model_loader.base_loader.BaseModelLoader)

Model loader using CoreWeave's tensorizer library.

Methods:

-
–[load_weights](https://docs.vllm.ai#vllm.model_executor.model_loader.TensorizerLoader.load_weights)Load serialized model weights with tensorizer.


## Source code in `vllm/model_executor/model_loader/tensorizer_loader.py`


|
|

###

`_load_model_serialized_cpu(vllm_config, prefix='')`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.TensorizerLoader._load_model_serialized_cpu)

Load a serialized model with tensorizer to the CPU.

This is only necessary when the model isn't vLLM-tensorized (see examples/features/tensorize_vllm_model.py) This should still be faster than default HuggingFace loading, but will be slower than loading a vLLM-tensorized model.

## Source code in `vllm/model_executor/model_loader/tensorizer_loader.py`


###

`load_weights(model, model_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.TensorizerLoader.load_weights)

Load serialized model weights with tensorizer.

Expects a vLLM-tensorized model. See the examples/features/tensorize_vllm_model.py example script for serializing vLLM models.

## Source code in `vllm/model_executor/model_loader/tensorizer_loader.py`


##

`get_model_loader(load_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.get_model_loader)

Get a model loader based on the load format.

## Source code in `vllm/model_executor/model_loader/__init__.py`


##

`register_model_loader(load_format)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.register_model_loader)

Register a customized vllm model loader.

When a load format is not supported by vllm, you can register a customized model loader to support it.

Parameters:

Examples:

>>> from vllm.config.load import LoadConfig
>>> from vllm.model_executor.model_loader import (
... get_model_loader,
... register_model_loader,
... )
>>> from vllm.model_executor.model_loader.base_loader import BaseModelLoader
>>>
>>> @register_model_loader("my_loader")
... class MyModelLoader(BaseModelLoader):
... def download_model(self):
... pass
...
... def load_weights(self):
... pass
>>>
>>> load_config = LoadConfig(load_format="my_loader")
>>> type(get_model_loader(load_config))
<class 'MyModelLoader'>