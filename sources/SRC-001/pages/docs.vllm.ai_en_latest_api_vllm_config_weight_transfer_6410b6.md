source: https://docs.vllm.ai/en/latest/api/vllm/config/weight_transfer/
lastmod: 2026-09-23

#

`vllm.config.weight_transfer`

[¶](https://docs.vllm.ai#vllm.config.weight_transfer)

Classes:

-
–[WeightTransferConfig](https://docs.vllm.ai#vllm.config.weight_transfer.WeightTransferConfig)Configuration for weight transfer during RL training.


##

`WeightTransferConfig`

[¶](https://docs.vllm.ai#vllm.config.weight_transfer.WeightTransferConfig)

Configuration for weight transfer during RL training.

Attributes:

-
([backend](https://docs.vllm.ai#vllm.config.weight_transfer.WeightTransferConfig.backend)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['nccl', 'ipc', 'sparse_nccl', 'sharded_rdt'] |[str](https://docs.python.org/3/builtins/stdtypes.html#str)The backend to use for weight transfer. Validated against the


## Source code in `vllm/config/weight_transfer.py`


###

`backend = 'nccl'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.weight_transfer.WeightTransferConfig.backend)

The backend to use for weight transfer. Validated against the `WeightTransferEngineFactory`

registry at engine creation time.