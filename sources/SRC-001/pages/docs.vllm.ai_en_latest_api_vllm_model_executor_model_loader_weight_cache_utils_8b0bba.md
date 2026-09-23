source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/model_loader/weight_cache/utils/
lastmod: 2026-09-23

#

`vllm.model_executor.model_loader.weight_cache.utils`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.utils)

Helpers shared by the weight cache daemon, the IPC loader and the engine.

These live outside `protocol`

so callers that only need to know whether a draft is cached, or how a daemon group is named, do not have to import the wire format.

Functions:

-
–[format_daemon_role](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.utils.format_daemon_role)Name of a daemon group: the target model or the draft.

-
–[format_socket_role_suffix](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.utils.format_socket_role_suffix)Socket-name suffix keeping the draft group distinct from the target.

-
–[is_draft_model_cacheable](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.utils.is_draft_model_cacheable)Whether the daemon serves the speculative draft as a separate role.


##

`format_daemon_role(is_draft)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.utils.format_daemon_role)

##

`format_socket_role_suffix(is_draft)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.utils.format_socket_role_suffix)

Socket-name suffix keeping the draft group distinct from the target.

##

`is_draft_model_cacheable(speculative_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.utils.is_draft_model_cacheable)

Whether the daemon serves the speculative draft as a separate role.