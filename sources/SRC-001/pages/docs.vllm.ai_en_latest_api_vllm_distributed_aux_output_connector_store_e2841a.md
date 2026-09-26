source: https://docs.vllm.ai/en/latest/api/vllm/distributed/aux_output_connector/store/
lastmod: 2026-09-24

#

`vllm.distributed.aux_output_connector.store`

[¶](https://docs.vllm.ai#vllm.distributed.aux_output_connector.store)

In-process auxiliary-output storage.

Classes:

-
–[BackgroundBlockObjectStore](https://docs.vllm.ai#vllm.distributed.aux_output_connector.store.BackgroundBlockObjectStore)Serialize store mutations on a background thread.

-
–[BlockObject](https://docs.vllm.ai#vllm.distributed.aux_output_connector.store.BlockObject)One immutable auxiliary output object.

-
–[BlockObjectStore](https://docs.vllm.ai#vllm.distributed.aux_output_connector.store.BlockObjectStore)Single-owner bounded store that fails closed after an eviction.

-
–[BlockObjectStoreError](https://docs.vllm.ai#vllm.distributed.aux_output_connector.store.BlockObjectStoreError)AuxOutput storage or retrieval failed.


##

`BackgroundBlockObjectStore`

[¶](https://docs.vllm.ai#vllm.distributed.aux_output_connector.store.BackgroundBlockObjectStore)

Serialize store mutations on a background thread.

## Source code in `vllm/distributed/aux_output_connector/store.py`


##

`BlockObject`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.aux_output_connector.store.BlockObject)

##

`BlockObjectStore`

[¶](https://docs.vllm.ai#vllm.distributed.aux_output_connector.store.BlockObjectStore)

Single-owner bounded store that fails closed after an eviction.

## Source code in `vllm/distributed/aux_output_connector/store.py`


|
|

##

`BlockObjectStoreError`

[¶](https://docs.vllm.ai#vllm.distributed.aux_output_connector.store.BlockObjectStoreError)

Bases: [RuntimeError](https://docs.python.org/3/builtins/exceptions.html#RuntimeError)

AuxOutput storage or retrieval failed.