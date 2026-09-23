source: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_transfer_state/
lastmod: 2026-09-23

#

`vllm.distributed.kv_transfer.kv_transfer_state`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_transfer_state)

Functions:

-
–[ensure_kv_transfer_initialized](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_transfer_state.ensure_kv_transfer_initialized)Initialize KV cache transfer parallel group.

-
–[is_v1_kv_transfer_group](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_transfer_state.is_v1_kv_transfer_group)Check if the KV connector is the v1 connector.


##

`_sync_engine_id_across_tp(vllm_config)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_transfer_state._sync_engine_id_across_tp)

Broadcast engine_id from TP rank 0 so all workers in a multi-node TP group share the same value.

When PP is enabled, also broadcast across PP ranks so all workers in the same model-parallel engine share the same value.

## Source code in `vllm/distributed/kv_transfer/kv_transfer_state.py`


##

`ensure_kv_transfer_initialized(vllm_config, kv_cache_config)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_transfer_state.ensure_kv_transfer_initialized)

Initialize KV cache transfer parallel group.

## Source code in `vllm/distributed/kv_transfer/kv_transfer_state.py`


##

`is_v1_kv_transfer_group(connector=None)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_transfer_state.is_v1_kv_transfer_group)

Check if the KV connector is the v1 connector. If the argument is None, it will check the global KV connector

Parameters:

-

(`connector`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_transfer_state.is_v1_kv_transfer_group(connector))`KVConnectorBaseType | None`

, default:`None`

) –The KV connector to check. If None, it will check the global KV connector.


## Note

This function will no-longer be needed after the v1 KV connector becomes the default.