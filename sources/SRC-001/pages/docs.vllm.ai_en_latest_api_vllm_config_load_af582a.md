source: https://docs.vllm.ai/en/latest/api/vllm/config/load/
lastmod: 2026-09-24

#

`vllm.config.load`

[¶](https://docs.vllm.ai#vllm.config.load)

Classes:

-
–[LoadConfig](https://docs.vllm.ai#vllm.config.load.LoadConfig)Configuration for loading the model weights.


##

`LoadConfig`

[¶](https://docs.vllm.ai#vllm.config.load.LoadConfig)

Configuration for loading the model weights.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.load.LoadConfig.compute_hash)WARNING: Whenever a new field is added to this config,


Attributes:

-
([device](https://docs.vllm.ai#vllm.config.load.LoadConfig.device)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneDevice to which model weights will be loaded, default to

-
([download_dir](https://docs.vllm.ai#vllm.config.load.LoadConfig.download_dir)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneDirectory to download and load the weights, default to the default

-
([ignore_patterns](https://docs.vllm.ai#vllm.config.load.LoadConfig.ignore_patterns)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] |[str](https://docs.python.org/3/builtins/stdtypes.html#str)The list of patterns to ignore when loading the model. Default to

-
([load_format](https://docs.vllm.ai#vllm.config.load.LoadConfig.load_format)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| LoadFormatsThe format of the model weights to load.

-
([model_loader_extra_config](https://docs.vllm.ai#vllm.config.load.LoadConfig.model_loader_extra_config)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)|[TensorizerConfig](https://docs.vllm.ai/model_executor/model_loader/tensorizer/#vllm.model_executor.model_loader.tensorizer.TensorizerConfig)Extra config for model loader. This will be passed to the model loader

-
([pt_load_map_location](https://docs.vllm.ai#vllm.config.load.LoadConfig.pt_load_map_location)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)|[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[str](https://docs.python.org/3/builtins/stdtypes.html#str)]The map location for loading pytorch checkpoint, to support loading

-
([safetensors_load_strategy](https://docs.vllm.ai#vllm.config.load.LoadConfig.safetensors_load_strategy)`SafetensorsLoadStrategy | None`

) –Specifies the loading strategy for safetensors weights.

-
([safetensors_prefetch_block_size](https://docs.vllm.ai#vllm.config.load.LoadConfig.safetensors_prefetch_block_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Read size in bytes for each safetensors checkpoint file prefetch.

-
([safetensors_prefetch_num_threads](https://docs.vllm.ai#vllm.config.load.LoadConfig.safetensors_prefetch_num_threads)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of worker threads used to prefetch safetensors checkpoint files

-
([use_tqdm_on_load](https://docs.vllm.ai#vllm.config.load.LoadConfig.use_tqdm_on_load)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to enable tqdm for showing progress bar when loading model


## Source code in `vllm/config/load.py`


|
|

###

`device = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.load.LoadConfig.device)

Device to which model weights will be loaded, default to device_config.device

###

`download_dir = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.load.LoadConfig.download_dir)

Directory to download and load the weights, default to the default cache directory of Hugging Face.

###

`ignore_patterns = Field(default_factory=(lambda: ['original/**/*']))`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.load.LoadConfig.ignore_patterns)

The list of patterns to ignore when loading the model. Default to "original/**/*" to avoid repeated loading of llama's checkpoints.

###

`load_format = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.load.LoadConfig.load_format)

The format of the model weights to load.

- "auto" will try to load the weights in the safetensors format and fall back to the pytorch bin format if safetensors format is not available.
- "pt" will load the weights in the pytorch bin format.
- "safetensors" will load the weights in the safetensors format.
- "instanttensor" will load the Safetensors weights on CUDA devices using InstantTensor, which enables distributed loading with pipelined prefetching and fast direct I/O.
- "ipc_cache" will map post-quantized weights from a local weight cache daemon via CUDA IPC for fast engine restarts. See
`vllm/model_executor/model_loader/weight_cache/daemon.py`

for how to launch the daemon. - "npcache" will load the weights in pytorch format and store a numpy cache to speed up the loading.
- "dummy" will initialize the weights with random values, which is mainly for profiling.
- "tensorizer" will use CoreWeave's tensorizer library for fast weight loading. See the Tensorize vLLM Model script in the Examples section for more information.
- "runai_streamer" will load the Safetensors weights using Run:ai Model Streamer.
- "runai_streamer_sharded" will load weights from pre-sharded checkpoint files using Run:ai Model Streamer.
- "sharded_state" will load weights from pre-sharded checkpoint files, supporting efficient loading of tensor-parallel models.
- "mistral" will load weights from consolidated safetensors files used by Mistral models.
- "modelexpress" will load weights using ModelExpress.
- Other custom values can be supported via plugins.

###

`model_loader_extra_config = Field(default_factory=dict)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.load.LoadConfig.model_loader_extra_config)

Extra config for model loader. This will be passed to the model loader corresponding to the chosen load_format.

###

`pt_load_map_location = 'cpu'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.load.LoadConfig.pt_load_map_location)

The map location for loading pytorch checkpoint, to support loading checkpoints can only be loaded on certain devices like "cuda", this is equivalent to `{"": "cuda"}`

. Another supported format is mapping from different devices like from GPU 1 to GPU 0: `{"cuda:1": "cuda:0"}`

. Note that when passed from command line, the strings in dictionary need to be double quoted for json parsing. For more details, see the original doc for `map_location`

parameter in [ torch.load](https://pytorch.org/docs/stable/generated/torch.load.html#torch.load) parameter.

###

`safetensors_load_strategy = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.load.LoadConfig.safetensors_load_strategy)

Specifies the loading strategy for safetensors weights.

- None (default): Uses memory-mapped (lazy) loading. When an NFS filesystem is detected and the total checkpoint size fits within 90%% of available RAM, prefetching is enabled automatically.
- "lazy": Weights are memory-mapped from the file. This enables on-demand loading and is highly efficient for models on local storage. Unlike the default (None), auto-prefetch on NFS is not performed.
- "eager": The entire file is read into CPU memory upfront before loading. This is recommended for models on network filesystems (e.g., Lustre, NFS) as it avoids inefficient random reads, significantly speeding up model initialization. However, it uses more CPU RAM.
- "prefetch": Checkpoint files are read into the OS page cache before workers load them, speeding up the model loading phase. Useful on network or high-latency storage.
- "torchao": Weights are loaded in upfront and then reconstructed into torchao tensor subclasses. This is used when the checkpoint was quantized using torchao and saved using safetensors. Needs
`torchao >= 0.14.0`

.

###

`safetensors_prefetch_block_size = Field(default=DEFAULT_SAFETENSORS_PREFETCH_BLOCK_SIZE, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.load.LoadConfig.safetensors_prefetch_block_size)

Read size in bytes for each safetensors checkpoint file prefetch.

###

`safetensors_prefetch_num_threads = Field(default=DEFAULT_SAFETENSORS_PREFETCH_NUM_THREADS, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.load.LoadConfig.safetensors_prefetch_num_threads)

Number of worker threads used to prefetch safetensors checkpoint files into the OS page cache when safetensors prefetching is enabled.

###

`use_tqdm_on_load = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.load.LoadConfig.use_tqdm_on_load)

Whether to enable tqdm for showing progress bar when loading model weights.

###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.load.LoadConfig.compute_hash)

WARNING: Whenever a new field is added to this config, ensure that it is included in the factors list if it affects the computation graph.

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.