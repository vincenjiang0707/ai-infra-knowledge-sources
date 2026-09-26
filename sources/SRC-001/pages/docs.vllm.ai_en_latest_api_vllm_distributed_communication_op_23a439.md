source: https://docs.vllm.ai/en/latest/api/vllm/distributed/communication_op/
lastmod: 2026-09-24

#

`vllm.distributed.communication_op`

[¶](https://docs.vllm.ai#vllm.distributed.communication_op)

Functions:

-
–[tensor_model_parallel_all_gather](https://docs.vllm.ai#vllm.distributed.communication_op.tensor_model_parallel_all_gather)All-gather the input tensor across model parallel group.

-
–[tensor_model_parallel_all_reduce](https://docs.vllm.ai#vllm.distributed.communication_op.tensor_model_parallel_all_reduce)All-reduce the input tensor across model parallel group.

-
–[tensor_model_parallel_gather](https://docs.vllm.ai#vllm.distributed.communication_op.tensor_model_parallel_gather)Gather the input tensor across model parallel group.

-
–[tensor_model_parallel_reduce_scatter](https://docs.vllm.ai#vllm.distributed.communication_op.tensor_model_parallel_reduce_scatter)Reduce-Scatter the input tensor across model parallel group.


##

`tensor_model_parallel_all_gather(input_, dim=-1)`

[¶](https://docs.vllm.ai#vllm.distributed.communication_op.tensor_model_parallel_all_gather)

All-gather the input tensor across model parallel group.

##

`tensor_model_parallel_all_reduce(input_)`

[¶](https://docs.vllm.ai#vllm.distributed.communication_op.tensor_model_parallel_all_reduce)

##

`tensor_model_parallel_gather(input_, dst=0, dim=-1)`

[¶](https://docs.vllm.ai#vllm.distributed.communication_op.tensor_model_parallel_gather)

Gather the input tensor across model parallel group.

##

`tensor_model_parallel_reduce_scatter(input_, dim=-1)`

[¶](https://docs.vllm.ai#vllm.distributed.communication_op.tensor_model_parallel_reduce_scatter)

Reduce-Scatter the input tensor across model parallel group.