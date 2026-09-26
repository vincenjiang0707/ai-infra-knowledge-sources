source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/serve/lora/api_router/
lastmod: 2026-09-24

#

`vllm.entrypoints.serve.lora.api_router`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.lora.api_router)

Functions:

-
–[attach_router](https://docs.vllm.ai#vllm.entrypoints.serve.lora.api_router.attach_router)Attach the LoRA adapter load/unload endpoints to the API server.


##

`_attach_router(app)`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.lora.api_router._attach_router)

Register the LoRA adapter load/unload routes on the app.

## Source code in `vllm/entrypoints/serve/lora/api_router.py`


##

`attach_router(app)`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.lora.api_router.attach_router)

Attach the LoRA adapter load/unload endpoints to the API server.

Does nothing when dynamic LoRA updating is disabled. Handler levels are snapshotted and restored because importing model_hosting_container_standards may reconfigure root logging.