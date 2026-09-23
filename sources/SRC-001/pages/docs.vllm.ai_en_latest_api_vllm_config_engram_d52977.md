source: https://docs.vllm.ai/en/latest/api/vllm/config/engram/
lastmod: 2026-09-23

#

`vllm.config.engram`

[¶](https://docs.vllm.ai#vllm.config.engram)

Classes:

-
–[EngramConfig](https://docs.vllm.ai#vllm.config.engram.EngramConfig)Configuration for Engram embedding storage and sharding.


Functions:

-
–[model_has_engram_layers](https://docs.vllm.ai#vllm.config.engram.model_has_engram_layers)Whether the model carries n-gram embedding layers.


##

`EngramConfig`

[¶](https://docs.vllm.ai#vllm.config.engram.EngramConfig)

Configuration for Engram embedding storage and sharding.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.engram.EngramConfig.compute_hash)Hash settings that affect embedding execution and graph structure.

-
–[get_parallel_size](https://docs.vllm.ai#vllm.config.engram.EngramConfig.get_parallel_size)Derive the embedding group size from the parallel configuration.

-
–[resolve_dp_shared_memory](https://docs.vllm.ai#vllm.config.engram.EngramConfig.resolve_dp_shared_memory)Share host tables by default wherever the configuration permits.

-
–[verify_model_config](https://docs.vllm.ai#vllm.config.engram.EngramConfig.verify_model_config)Reject Engram configuration for models without n-gram embeddings.

-
–[verify_parallel_config](https://docs.vllm.ai#vllm.config.engram.EngramConfig.verify_parallel_config)Reject unsupported embedding parallel topologies.


Attributes:

-
([cpu_offload](https://docs.vllm.ai#vllm.config.engram.EngramConfig.cpu_offload)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Store embedding weights in pinned CPU memory for UVA lookup.

-
([dp_shared_memory](https://docs.vllm.ai#vllm.config.engram.EngramConfig.dp_shared_memory)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)| NoneShare CPU-offloaded embedding weights between co-located

-
([embedding_across_dp](https://docs.vllm.ai#vllm.config.engram.EngramConfig.embedding_across_dp)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Shard embeddings across TP and all DP ranks when enabled.


## Source code in `vllm/config/engram.py`


###

`cpu_offload = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.engram.EngramConfig.cpu_offload)

Store embedding weights in pinned CPU memory for UVA lookup.

###

`dp_shared_memory = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.engram.EngramConfig.dp_shared_memory)

Share CPU-offloaded embedding weights between co-located DP replicas. Each node stores one copy of every TP shard, reducing host memory without per-step Engram DP collectives. Requires sufficient /dev/shm capacity and a shared IPC namespace. Defaults to enabled whenever the other settings allow it, falling back to per-replica tables when DP replicas are not co-located on one node or /dev/shm cannot hold them.

###

`embedding_across_dp = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.engram.EngramConfig.embedding_across_dp)

Shard embeddings across TP and all DP ranks when enabled. Otherwise, each DP rank has a separate TP-sharded embedding replica.

###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.engram.EngramConfig.compute_hash)

###

`get_parallel_size(parallel_config)`

[¶](https://docs.vllm.ai#vllm.config.engram.EngramConfig.get_parallel_size)

Derive the embedding group size from the parallel configuration.

## Source code in `vllm/config/engram.py`


###

`resolve_dp_shared_memory(parallel_config)`

[¶](https://docs.vllm.ai#vllm.config.engram.EngramConfig.resolve_dp_shared_memory)

Share host tables by default wherever the configuration permits.

## Source code in `vllm/config/engram.py`


###

`verify_model_config(model_config)`

[¶](https://docs.vllm.ai#vllm.config.engram.EngramConfig.verify_model_config)

Reject Engram configuration for models without n-gram embeddings.

## Source code in `vllm/config/engram.py`


###

`verify_parallel_config(parallel_config)`

[¶](https://docs.vllm.ai#vllm.config.engram.EngramConfig.verify_parallel_config)

Reject unsupported embedding parallel topologies.

## Source code in `vllm/config/engram.py`


##

`model_has_engram_layers(model_config)`

[¶](https://docs.vllm.ai#vllm.config.engram.model_has_engram_layers)

Whether the model carries n-gram embedding layers.