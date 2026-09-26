source: https://docs.vllm.ai/en/latest/api/vllm/distributed/device_communicators/flashinfer_all_reduce/
lastmod: 2026-09-24

#

`vllm.distributed.device_communicators.flashinfer_all_reduce`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.flashinfer_all_reduce)

Classes:

Functions:

-
–[get_fi_ar_quant_workspace](https://docs.vllm.ai#vllm.distributed.device_communicators.flashinfer_all_reduce.get_fi_ar_quant_workspace)Return the allreduce workspace for quant patterns, initializing if needed.

-
–[get_fi_ar_workspace](https://docs.vllm.ai#vllm.distributed.device_communicators.flashinfer_all_reduce.get_fi_ar_workspace)Return the allreduce workspace for non-quant patterns, initializing if needed.


##

`FlashInferAllReduce`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.flashinfer_all_reduce.FlashInferAllReduce)

## Source code in `vllm/distributed/device_communicators/flashinfer_all_reduce.py`


|
|

###

`_ensure_workspace(hidden_dim, dtype)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.flashinfer_all_reduce.FlashInferAllReduce._ensure_workspace)

Ensure the all reduce workspace is initialized.

## Source code in `vllm/distributed/device_communicators/flashinfer_all_reduce.py`


##

`_create_workspace(backend, world_size, rank, max_token_num, hidden_dim, dtype, group)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.flashinfer_all_reduce._create_workspace)

Create a flashinfer allreduce workspace, returning None on failure.

## Source code in `vllm/distributed/device_communicators/flashinfer_all_reduce.py`


##

`_resolve_fi_ar_backend()`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.flashinfer_all_reduce._resolve_fi_ar_backend)

Resolve the flashinfer allreduce backend for the current setup.

Returns:

-

–[str](https://docs.python.org/3/builtins/stdtypes.html#str)A

`(backend, allow_trtllm_fallback)`

tuple.`allow_trtllm_fallback`

-

–[bool](https://docs.python.org/3/builtins/functions.html#bool)is True only when

`auto`

selects mnnvl for a single node, so that -

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[bool](https://docs.python.org/3/builtins/functions.html#bool)]workspace creation can fall back to trtllm on single-node topologies

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[bool](https://docs.python.org/3/builtins/functions.html#bool)]without NVSwitch multicast support (where mnnvl is unavailable).


## Source code in `vllm/distributed/device_communicators/flashinfer_all_reduce.py`


##

`get_fi_ar_quant_workspace(world_size, rank, max_token_num, hidden_dim, dtype, group)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.flashinfer_all_reduce.get_fi_ar_quant_workspace)

Return the allreduce workspace for quant patterns, initializing if needed.

Backend is controlled by VLLM_FLASHINFER_ALLREDUCE_BACKEND env var, matching non-quant fusion. With `auto`

this prefers mnnvl and falls back to trtllm only on single-node topologies where mnnvl multicast is unavailable.

## Source code in `vllm/distributed/device_communicators/flashinfer_all_reduce.py`


##

`get_fi_ar_workspace(world_size, rank, max_token_num, hidden_dim, dtype, group)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.flashinfer_all_reduce.get_fi_ar_workspace)

Return the allreduce workspace for non-quant patterns, initializing if needed.

Used by AllReduceFusionPass (non-quant patterns) and FlashInferAllReduce for standalone allreduce. Backend is controlled by VLLM_FLASHINFER_ALLREDUCE_BACKEND env var.