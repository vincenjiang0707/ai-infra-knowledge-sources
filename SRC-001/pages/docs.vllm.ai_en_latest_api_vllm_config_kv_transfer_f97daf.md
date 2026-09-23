source: https://docs.vllm.ai/en/latest/api/vllm/config/kv_transfer/
lastmod: 2026-09-23

#

`vllm.config.kv_transfer`

[¶](https://docs.vllm.ai#vllm.config.kv_transfer)

Classes:

-
–[KVTransferConfig](https://docs.vllm.ai#vllm.config.kv_transfer.KVTransferConfig)Configuration for distributed KV cache transfer.


##

`KVTransferConfig`

[¶](https://docs.vllm.ai#vllm.config.kv_transfer.KVTransferConfig)

Configuration for distributed KV cache transfer.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.kv_transfer.KVTransferConfig.compute_hash)WARNING: Whenever a new field is added to this config,

-
–[has_connector](https://docs.vllm.ai#vllm.config.kv_transfer.KVTransferConfig.has_connector)Whether

`connector_name`

is configured, directly or in MultiConnector.

Attributes:

-
([enable_permute_local_kv](https://docs.vllm.ai#vllm.config.kv_transfer.KVTransferConfig.enable_permute_local_kv)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Experiment feature flag to enable HND to NHD KV Transfer

-
([engine_id](https://docs.vllm.ai#vllm.config.kv_transfer.KVTransferConfig.engine_id)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe engine id for KV transfers.

-
([kv_buffer_device](https://docs.vllm.ai#vllm.config.kv_transfer.KVTransferConfig.kv_buffer_device)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The device used by kv connector to buffer the KV cache. Choices are

-
([kv_buffer_size](https://docs.vllm.ai#vllm.config.kv_transfer.KVTransferConfig.kv_buffer_size)

) –[float](https://docs.python.org/3/builtins/functions.html#float)The buffer size for TorchDistributedConnector. Measured in number of

-
([kv_connector](https://docs.vllm.ai#vllm.config.kv_transfer.KVTransferConfig.kv_connector)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe KV connector for vLLM to transmit KV caches between vLLM instances.

-
([kv_connector_extra_config](https://docs.vllm.ai#vllm.config.kv_transfer.KVTransferConfig.kv_connector_extra_config)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)]any extra config that the connector may need.

-
([kv_connector_module_path](https://docs.vllm.ai#vllm.config.kv_transfer.KVTransferConfig.kv_connector_module_path)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe Python module path to dynamically load the KV connector from.

-
([kv_ip](https://docs.vllm.ai#vllm.config.kv_transfer.KVTransferConfig.kv_ip)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The KV connector ip, used to build distributed connection.

-
([kv_load_failure_policy](https://docs.vllm.ai#vllm.config.kv_transfer.KVTransferConfig.kv_load_failure_policy)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['recompute', 'fail']Policy for handling KV cache load failures.

-
([kv_parallel_size](https://docs.vllm.ai#vllm.config.kv_transfer.KVTransferConfig.kv_parallel_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The number of parallel instances for KV cache transfer.

-
([kv_port](https://docs.vllm.ai#vllm.config.kv_transfer.KVTransferConfig.kv_port)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The KV connector port, used to build distributed connection.

-
([kv_rank](https://docs.vllm.ai#vllm.config.kv_transfer.KVTransferConfig.kv_rank)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneThe rank of this vLLM instance in the KV cache transfer. Typical value:

-
([kv_role](https://docs.vllm.ai#vllm.config.kv_transfer.KVTransferConfig.kv_role)`KVRole | None`

) –Whether this vLLM instance produces, consumes KV cache, or both. Choices


## Source code in `vllm/config/kv_transfer.py`


|
|

###

`enable_permute_local_kv = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.kv_transfer.KVTransferConfig.enable_permute_local_kv)

Experiment feature flag to enable HND to NHD KV Transfer

###

`engine_id = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.kv_transfer.KVTransferConfig.engine_id)

The engine id for KV transfers.

###

`kv_buffer_device = field(default_factory=kv_buffer_device_default_factory)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.kv_transfer.KVTransferConfig.kv_buffer_device)

The device used by kv connector to buffer the KV cache. Choices are 'cuda', 'cpu' and 'xpu'.

###

`kv_buffer_size = 1000000000.0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.kv_transfer.KVTransferConfig.kv_buffer_size)

The buffer size for TorchDistributedConnector. Measured in number of bytes. Recommended value: 1e9 (about 1GB).

###

`kv_connector = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.kv_transfer.KVTransferConfig.kv_connector)

The KV connector for vLLM to transmit KV caches between vLLM instances.

###

`kv_connector_extra_config = field(default_factory=dict)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.kv_transfer.KVTransferConfig.kv_connector_extra_config)

any extra config that the connector may need.

###

`kv_connector_module_path = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.kv_transfer.KVTransferConfig.kv_connector_module_path)

The Python module path to dynamically load the KV connector from. Only supported in V1.

###

`kv_ip = '127.0.0.1'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.kv_transfer.KVTransferConfig.kv_ip)

The KV connector ip, used to build distributed connection.

###

`kv_load_failure_policy = 'fail'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.kv_transfer.KVTransferConfig.kv_load_failure_policy)

Policy for handling KV cache load failures. 'recompute': reschedule the request to recompute failed blocks 'fail': immediately fail the request with an error finish reason (default)

###

`kv_parallel_size = 1`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.kv_transfer.KVTransferConfig.kv_parallel_size)

The number of parallel instances for KV cache transfer.

###

`kv_port = 14579`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.kv_transfer.KVTransferConfig.kv_port)

The KV connector port, used to build distributed connection.

###

`kv_rank = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.kv_transfer.KVTransferConfig.kv_rank)

The rank of this vLLM instance in the KV cache transfer. Typical value: 0 for prefill instance, 1 for decode instance. Currently only 1P1D is supported.

###

`kv_role = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.kv_transfer.KVTransferConfig.kv_role)

Whether this vLLM instance produces, consumes KV cache, or both. Choices are 'kv_producer', 'kv_consumer', and 'kv_both'.

###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.kv_transfer.KVTransferConfig.compute_hash)

WARNING: Whenever a new field is added to this config, ensure that it is included in the factors list if it affects the computation graph.

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.

## Source code in `vllm/config/kv_transfer.py`


###

`has_connector(connector_name)`

[¶](https://docs.vllm.ai#vllm.config.kv_transfer.KVTransferConfig.has_connector)

Whether `connector_name`

is configured, directly or in MultiConnector.