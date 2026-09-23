source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/speech_to_text/realtime/metrics/
lastmod: 2026-09-23

#

`vllm.entrypoints.speech_to_text.realtime.metrics`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.realtime.metrics)

ASGI middleware for WebSocket Prometheus metrics.

Modeled after prometheus-fastapi-instrumentator, this middleware transparently instruments WebSocket endpoints with standard metrics without requiring changes to handler code.

NOTE: This module intentionally has zero vllm imports so that it can be extracted into a standalone package (similar to prometheus-fastapi-instrumentator) in the future. Please keep it that way.

Classes:

-
–[WebSocketMetricsMiddleware](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.realtime.metrics.WebSocketMetricsMiddleware)Pure ASGI middleware that instruments WebSocket connections.


##

`WebSocketMetricsMiddleware`

[¶](https://docs.vllm.ai#vllm.entrypoints.speech_to_text.realtime.metrics.WebSocketMetricsMiddleware)

Pure ASGI middleware that instruments WebSocket connections.

Tracks active connections (gauge), total connections (counter), and connection duration (histogram) for all WebSocket endpoints.

Usage::

```
app.add_middleware(WebSocketMetricsMiddleware)
```