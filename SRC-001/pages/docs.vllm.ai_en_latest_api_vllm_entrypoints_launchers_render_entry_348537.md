source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/launchers/render/entry/
lastmod: 2026-09-23

#

`vllm.entrypoints.launchers.render.entry`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.render.entry)

Functions:

-
–[build_and_serve_renderer](https://docs.vllm.ai#vllm.entrypoints.launchers.render.entry.build_and_serve_renderer)Build FastAPI app for a CPU-only render server, initialize state, and

-
–[run_launch_fastapi](https://docs.vllm.ai#vllm.entrypoints.launchers.render.entry.run_launch_fastapi)Run the online serving layer with FastAPI (no GPU inference).


##

`build_and_serve_renderer(vllm_config, listen_address, sock, args, **uvicorn_kwargs)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.render.entry.build_and_serve_renderer)

Build FastAPI app for a CPU-only render server, initialize state, and start serving.

Returns the shutdown task for the caller to await.

## Source code in `vllm/entrypoints/launchers/render/entry.py`


##

`run_launch_fastapi(args)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.render.entry.run_launch_fastapi)

Run the online serving layer with FastAPI (no GPU inference).