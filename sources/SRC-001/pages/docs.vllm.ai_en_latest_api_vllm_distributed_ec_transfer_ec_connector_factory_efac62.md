source: https://docs.vllm.ai/en/latest/api/vllm/distributed/ec_transfer/ec_connector/factory/
lastmod: 2026-09-24

#

`vllm.distributed.ec_transfer.ec_connector.factory`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.factory)

Classes:

##

`ECConnectorFactory`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.factory.ECConnectorFactory)

Methods:

-
–[get_connector_class](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.factory.ECConnectorFactory.get_connector_class)Get the connector class by name.

-
–[register_connector](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.factory.ECConnectorFactory.register_connector)Register a connector with a lazy-loading module and class name.


## Source code in `vllm/distributed/ec_transfer/ec_connector/factory.py`


###

`get_connector_class(ec_transfer_config)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.factory.ECConnectorFactory.get_connector_class)

Get the connector class by name.

## Source code in `vllm/distributed/ec_transfer/ec_connector/factory.py`


###

`register_connector(name, module_path, class_name)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.factory.ECConnectorFactory.register_connector)

Register a connector with a lazy-loading module and class name.