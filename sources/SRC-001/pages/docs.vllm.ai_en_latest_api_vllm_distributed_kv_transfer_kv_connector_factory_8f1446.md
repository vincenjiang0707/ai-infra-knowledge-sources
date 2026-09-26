source: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/factory/
lastmod: 2026-09-24

#

`vllm.distributed.kv_transfer.kv_connector.factory`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.factory)

Classes:

##

`KVConnectorFactory`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.factory.KVConnectorFactory)

Methods:

-
–[get_connector_class_by_name](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.factory.KVConnectorFactory.get_connector_class_by_name)Get a registered connector class by name.

-
–[register_connector](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.factory.KVConnectorFactory.register_connector)Register a connector with a lazy-loading module and class name.

-
–[supports_hma_config](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.factory.KVConnectorFactory.supports_hma_config)Return whether this KV transfer config supports HMA.


## Source code in `vllm/distributed/kv_transfer/kv_connector/factory.py`


|
|

###

`get_connector_class_by_name(connector_name)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.factory.KVConnectorFactory.get_connector_class_by_name)

Get a registered connector class by name.

Raises ValueError if the connector is not registered.

Parameters:

Returns:

-

–[type](https://docs.python.org/3/builtins/functions.html#type)[KVConnectorBaseType]The connector class.


## Source code in `vllm/distributed/kv_transfer/kv_connector/factory.py`


###

`register_connector(name, module_path, class_name)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.factory.KVConnectorFactory.register_connector)

Register a connector with a lazy-loading module and class name.

## Source code in `vllm/distributed/kv_transfer/kv_connector/factory.py`


###

`supports_hma_config(kv_transfer_config)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.factory.KVConnectorFactory.supports_hma_config)

Return whether this KV transfer config supports HMA.

MultiConnector is a special case: the wrapper class implements SupportsHMA, but effective support depends on every configured child.