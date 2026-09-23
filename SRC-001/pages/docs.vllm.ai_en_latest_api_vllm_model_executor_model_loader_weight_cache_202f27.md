source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/model_loader/weight_cache/
lastmod: 2026-09-23

#

`vllm.model_executor.model_loader.weight_cache`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache)

Modules:

-
–[daemon](https://docs.vllm.ai/daemon/#vllm.model_executor.model_loader.weight_cache.daemon)Weight cache daemon for fast engine restarts.

-
–[ipc_loader](https://docs.vllm.ai/ipc_loader/#vllm.model_executor.model_loader.weight_cache.ipc_loader)IPC model loader: maps post-quantized weights from a local weight cache

-
–[protocol](https://docs.vllm.ai/protocol/#vllm.model_executor.model_loader.weight_cache.protocol)WeightCacheKey fingerprinting and socket protocol for the weight cache daemon.

-
–[utils](https://docs.vllm.ai/utils/#vllm.model_executor.model_loader.weight_cache.utils)Helpers shared by the weight cache daemon, the IPC loader and the engine.