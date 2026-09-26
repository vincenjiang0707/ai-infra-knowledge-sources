source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/launchers/api_server/entry/
lastmod: 2026-09-24

#

`vllm.entrypoints.launchers.api_server.entry`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.api_server.entry)

Functions:

-
–[build_and_serve](https://docs.vllm.ai#vllm.entrypoints.launchers.api_server.entry.build_and_serve)Build FastAPI app, initialize state, and start serving.

-
–[build_async_engine_client_from_engine_args](https://docs.vllm.ai#vllm.entrypoints.launchers.api_server.entry.build_async_engine_client_from_engine_args)Create EngineClient, either:

-
–[run_server](https://docs.vllm.ai#vllm.entrypoints.launchers.api_server.entry.run_server)Run a single-worker API server.

-
–[run_server_worker](https://docs.vllm.ai#vllm.entrypoints.launchers.api_server.entry.run_server_worker)Run a single API server worker.


##

`build_and_serve(engine_client, listen_address, sock, args, **uvicorn_kwargs)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.api_server.entry.build_and_serve)

Build FastAPI app, initialize state, and start serving.

Returns the shutdown task for the caller to await.

## Source code in `vllm/entrypoints/launchers/api_server/entry.py`


##

`build_async_engine_client_from_engine_args(engine_args, *, usage_context=UsageContext.OPENAI_API_SERVER, client_config=None)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.api_server.entry.build_async_engine_client_from_engine_args)

Create EngineClient, either: - in-process using the AsyncLLMEngine Directly - multiprocess using AsyncLLMEngine RPC

Returns the Client or None if the creation failed.

## Source code in `vllm/entrypoints/launchers/api_server/entry.py`


##

`run_server(args, **uvicorn_kwargs)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.api_server.entry.run_server)

Run a single-worker API server.

## Source code in `vllm/entrypoints/launchers/api_server/entry.py`


##

`run_server_worker(listen_address, sock, args, client_config=None, **uvicorn_kwargs)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.api_server.entry.run_server_worker)

Run a single API server worker.