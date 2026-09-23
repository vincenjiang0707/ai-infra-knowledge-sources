source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/openai/api_server/
lastmod: 2026-09-23

#

`vllm.entrypoints.openai.api_server`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.api_server)

Functions:

-
–[build_and_serve](https://docs.vllm.ai#vllm.entrypoints.openai.api_server.build_and_serve)Build FastAPI app, initialize state, and start serving.

-
–[build_and_serve_renderer](https://docs.vllm.ai#vllm.entrypoints.openai.api_server.build_and_serve_renderer)Build FastAPI app for a CPU-only render server, initialize state, and

-
–[build_async_engine_client_from_engine_args](https://docs.vllm.ai#vllm.entrypoints.openai.api_server.build_async_engine_client_from_engine_args)Create EngineClient, either:

-
–[init_render_app_state](https://docs.vllm.ai#vllm.entrypoints.openai.api_server.init_render_app_state)Initialise FastAPI app state for a CPU-only render server.

-
–[run_server](https://docs.vllm.ai#vllm.entrypoints.openai.api_server.run_server)Run a single-worker API server.

-
–[run_server_worker](https://docs.vllm.ai#vllm.entrypoints.openai.api_server.run_server_worker)Run a single API server worker.

-
–[setup_server](https://docs.vllm.ai#vllm.entrypoints.openai.api_server.setup_server)Validate API server args and create the server socket.


##

`build_and_serve(engine_client, listen_address, sock, args, **uvicorn_kwargs)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.api_server.build_and_serve)

Build FastAPI app, initialize state, and start serving.

Returns the shutdown task for the caller to await.

## Source code in `vllm/entrypoints/launchers/api_server/entry.py`


##

`build_and_serve_renderer(vllm_config, listen_address, sock, args, **uvicorn_kwargs)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.api_server.build_and_serve_renderer)

Build FastAPI app for a CPU-only render server, initialize state, and start serving.

Returns the shutdown task for the caller to await.

## Source code in `vllm/entrypoints/launchers/render/entry.py`


##

`build_async_engine_client_from_engine_args(engine_args, *, usage_context=UsageContext.OPENAI_API_SERVER, client_config=None)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.api_server.build_async_engine_client_from_engine_args)

Create EngineClient, either: - in-process using the AsyncLLMEngine Directly - multiprocess using AsyncLLMEngine RPC

Returns the Client or None if the creation failed.

## Source code in `vllm/entrypoints/launchers/api_server/entry.py`


##

`init_render_app_state(vllm_config, state, args)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.api_server.init_render_app_state)

Initialise FastAPI app state for a CPU-only render server.

Unlike :func:`init_app_state`

this function does not require an :class:`~vllm.engine.protocol.EngineClient`

; it bootstraps the preprocessing pipeline (renderer, input_processor) directly from the :class:`~vllm.config.VllmConfig`

.

## Source code in `vllm/entrypoints/launchers/render/app_state.py`


##

`run_server(args, **uvicorn_kwargs)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.api_server.run_server)

Run a single-worker API server.

## Source code in `vllm/entrypoints/launchers/api_server/entry.py`


##

`run_server_worker(listen_address, sock, args, client_config=None, **uvicorn_kwargs)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.api_server.run_server_worker)

Run a single API server worker.

## Source code in `vllm/entrypoints/launchers/api_server/entry.py`


##

`setup_server(args, *, reuse_port)`

[¶](https://docs.vllm.ai#vllm.entrypoints.openai.api_server.setup_server)

Validate API server args and create the server socket.