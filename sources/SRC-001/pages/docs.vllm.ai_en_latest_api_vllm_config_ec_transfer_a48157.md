source: https://docs.vllm.ai/en/latest/api/vllm/config/ec_transfer/
lastmod: 2026-09-24

#

`vllm.config.ec_transfer`

[¶](https://docs.vllm.ai#vllm.config.ec_transfer)

Classes:

-
–[ECTransferConfig](https://docs.vllm.ai#vllm.config.ec_transfer.ECTransferConfig)Configuration for distributed EC cache transfer.


##

`ECTransferConfig`

[¶](https://docs.vllm.ai#vllm.config.ec_transfer.ECTransferConfig)

Configuration for distributed EC cache transfer.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.ec_transfer.ECTransferConfig.compute_hash)WARNING: Whenever a new field is added to this config,


Attributes:

-
([ec_buffer_device](https://docs.vllm.ai#vllm.config.ec_transfer.ECTransferConfig.ec_buffer_device)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe device used by ec connector to buffer the EC cache.

-
([ec_buffer_size](https://docs.vllm.ai#vllm.config.ec_transfer.ECTransferConfig.ec_buffer_size)

) –[float](https://docs.python.org/3/builtins/functions.html#float)The buffer size for TorchDistributedConnector. Measured in number of

-
([ec_connector](https://docs.vllm.ai#vllm.config.ec_transfer.ECTransferConfig.ec_connector)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe EC connector for vLLM to transmit EC caches between vLLM instances.

-
([ec_connector_extra_config](https://docs.vllm.ai#vllm.config.ec_transfer.ECTransferConfig.ec_connector_extra_config)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)]any extra config that the connector may need.

-
([ec_connector_module_path](https://docs.vllm.ai#vllm.config.ec_transfer.ECTransferConfig.ec_connector_module_path)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe Python module path to dynamically load the EC connector from.

-
([ec_ip](https://docs.vllm.ai#vllm.config.ec_transfer.ECTransferConfig.ec_ip)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The EC connector ip, used to build distributed connection.

-
([ec_parallel_size](https://docs.vllm.ai#vllm.config.ec_transfer.ECTransferConfig.ec_parallel_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The number of parallel instances for EC cache transfer. For

-
([ec_port](https://docs.vllm.ai#vllm.config.ec_transfer.ECTransferConfig.ec_port)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The EC connector port, used to build distributed connection.

-
([ec_rank](https://docs.vllm.ai#vllm.config.ec_transfer.ECTransferConfig.ec_rank)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneThe rank of this vLLM instance in the EC cache transfer. Typical value:

-
([ec_role](https://docs.vllm.ai#vllm.config.ec_transfer.ECTransferConfig.ec_role)`ECRole | None`

) –Whether this vLLM instance produces, consumes EC cache, or both. Choices

-
([engine_id](https://docs.vllm.ai#vllm.config.ec_transfer.ECTransferConfig.engine_id)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe engine id for EC transfers.

-
([is_encode_only](https://docs.vllm.ai#vllm.config.ec_transfer.ECTransferConfig.is_encode_only)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether this instance encodes but does not run the language model.


## Source code in `vllm/config/ec_transfer.py`


|
|

###

`ec_buffer_device = 'cuda'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ec_transfer.ECTransferConfig.ec_buffer_device)

The device used by ec connector to buffer the EC cache. Currently only support 'cuda'.

###

`ec_buffer_size = 1000000000.0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ec_transfer.ECTransferConfig.ec_buffer_size)

The buffer size for TorchDistributedConnector. Measured in number of bytes. Recommended value: 1e9 (about 1GB).

###

`ec_connector = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ec_transfer.ECTransferConfig.ec_connector)

The EC connector for vLLM to transmit EC caches between vLLM instances.

Built-in options include `ECExampleConnector`

(shared filesystem via safetensors) and `ECMooncakeConnector`

(Mooncake TransferEngine RDMA; requires `mooncake-transfer-engine`

and matching producer/consumer `ec_connector_extra_config`

; see `mooncake_ec_connector`

module docstring). Set `cross_encoder_cache`

in Mooncake extra config to reuse shared Encoder outputs from Store before encoding, retaining P2P delivery.

###

`ec_connector_extra_config = field(default_factory=dict)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ec_transfer.ECTransferConfig.ec_connector_extra_config)

any extra config that the connector may need.

###

`ec_connector_module_path = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ec_transfer.ECTransferConfig.ec_connector_module_path)

The Python module path to dynamically load the EC connector from. Only supported in V1.

###

`ec_ip = '127.0.0.1'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ec_transfer.ECTransferConfig.ec_ip)

The EC connector ip, used to build distributed connection.

###

`ec_parallel_size = 1`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ec_transfer.ECTransferConfig.ec_parallel_size)

The number of parallel instances for EC cache transfer. For PyNcclConnector, this should be 2.

###

`ec_port = 14579`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ec_transfer.ECTransferConfig.ec_port)

The EC connector port, used to build distributed connection.

###

`ec_rank = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ec_transfer.ECTransferConfig.ec_rank)

The rank of this vLLM instance in the EC cache transfer. Typical value: 0 for encoder, 1 for pd instance. Currently only 1P1D is supported.

###

`ec_role = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ec_transfer.ECTransferConfig.ec_role)

Whether this vLLM instance produces, consumes EC cache, or both. Choices are 'ec_producer', 'ec_consumer', 'ec_both'.

###

`engine_id = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ec_transfer.ECTransferConfig.engine_id)

The engine id for EC transfers.

###

`is_encode_only`

`property`

[¶](https://docs.vllm.ai#vllm.config.ec_transfer.ECTransferConfig.is_encode_only)

Whether this instance encodes but does not run the language model.

It allocates no KV cache either -- `GPUModelRunner.get_kv_cache_spec`

returns {} for it -- so it is the one role that can spend accelerator time and memory on frontend work.

###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.ec_transfer.ECTransferConfig.compute_hash)

WARNING: Whenever a new field is added to this config, ensure that it is included in the factors list if it affects the computation graph.

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.