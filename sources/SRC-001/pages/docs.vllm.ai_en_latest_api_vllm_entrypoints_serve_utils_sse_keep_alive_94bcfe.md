source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/serve/utils/sse_keep_alive/
lastmod: 2026-09-24

#

`vllm.entrypoints.serve.utils.sse_keep_alive`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.utils.sse_keep_alive)

SSE keep-alive comments for idle streaming responses.

Reverse proxies and tunnels (Cloudflare Tunnel, NGINX `proxy_read_timeout`

, AWS ALB, ...) can close a streaming connection when no bytes are sent for a while. That happens while a request is queued, during prefill, or in gaps between tokens. `with_sse_keep_alive`

wraps the final SSE generator and emits a comment line (`": keep-alive\n\n"`

) whenever it has been idle for `interval`

seconds. Comments are ignored by SSE-compliant clients but still count as bytes for proxy read-timeout logic.

Functions:

-
–[with_sse_keep_alive](https://docs.vllm.ai#vllm.entrypoints.serve.utils.sse_keep_alive.with_sse_keep_alive)Emit an SSE keep-alive comment when

`generator`

is idle.

##

`with_sse_keep_alive(generator, interval)`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.utils.sse_keep_alive.with_sse_keep_alive)

Emit an SSE keep-alive comment when `generator`

is idle.

A non-positive or non-finite `interval`

returns `generator`

unchanged, so the default path has no overhead. Otherwise a keep-alive comment is yielded whenever no chunk arrives within `interval`

seconds.