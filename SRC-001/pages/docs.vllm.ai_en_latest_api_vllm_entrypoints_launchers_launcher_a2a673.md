source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/launchers/launcher/
lastmod: 2026-09-23

#

`vllm.entrypoints.launchers.launcher`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.launcher)

Classes:

-
–[NoSignalServer](https://docs.vllm.ai#vllm.entrypoints.launchers.launcher.NoSignalServer)Uvicorn server that never installs its own SIGINT/SIGTERM handlers.


Functions:

-
–[serve_http](https://docs.vllm.ai#vllm.entrypoints.launchers.launcher.serve_http)Start a FastAPI app using Uvicorn, with support for custom Uvicorn config

-
–[setup_server](https://docs.vllm.ai#vllm.entrypoints.launchers.launcher.setup_server)Validate API server args and create the server socket.

-
–[terminate_if_errored](https://docs.vllm.ai#vllm.entrypoints.launchers.launcher.terminate_if_errored)See discussions here on shutting down a uvicorn server

-
–[watchdog_loop](https://docs.vllm.ai#vllm.entrypoints.launchers.launcher.watchdog_loop)## Watchdog task that runs in the background, checking

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.launcher--watchdog-task-that-runs-in-the-background-checking)

##

`NoSignalServer`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.launcher.NoSignalServer)

Bases: `Server`


Uvicorn server that never installs its own SIGINT/SIGTERM handlers.

Callers register their own handlers on the event loop for graceful shutdown; uvicorn's would race with and override them (see #49668).

## Source code in `vllm/entrypoints/launchers/launcher.py`


##

`serve_http(app, sock, enable_ssl_refresh=False, **uvicorn_kwargs)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.launcher.serve_http)

Start a FastAPI app using Uvicorn, with support for custom Uvicorn config options. Supports http header limits via h11_max_incomplete_event_size and h11_max_header_count.

## Source code in `vllm/entrypoints/launchers/launcher.py`


|
|

##

`setup_server(args, *, reuse_port)`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.launcher.setup_server)

Validate API server args and create the server socket.

## Source code in `vllm/entrypoints/launchers/launcher.py`


##

`terminate_if_errored(server, engine)`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.launcher.terminate_if_errored)

See discussions here on shutting down a uvicorn server https://github.com/encode/uvicorn/discussions/1103 In this case we cannot await the server shutdown here because handler must first return to close the connection for this request.